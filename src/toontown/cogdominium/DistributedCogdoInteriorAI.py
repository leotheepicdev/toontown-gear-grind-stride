from direct.directnotify import DirectNotifyGlobal
from direct.distributed.DistributedObjectAI import DistributedObjectAI
from direct.distributed.ClockDelta import *
from direct.fsm import FSM
from direct.task import Timer
from toontown.battle import BattleBase
from toontown.building.ElevatorConstants import *
from toontown.base.ToontownGlobals import *
from toontown.base.ToontownBattleGlobals import *
import DistCogdoMazeGameAI, CogdoMazeGameGlobals, DistributedCogdoElevatorIntAI
import DistCogdoFlyingGameAI, DistributedCogdoBarrelAI
from DistributedCogdoBattleBldgAI import DistributedCogdoBattleBldgAI
from SuitPlannerCogdoInteriorAI import SuitPlannerCogdoInteriorAI
from toontown.cogdominium import CogdoBarrelRoomConsts
from toontown.cogdominium import DistCogdoCraneGameAI
from toontown.toon import NPCToons
from toontown.quest import Quests
import random, math

NUM_FLOORS_DICT = {
                   's': 2,
                   'l': 2,
                   'm':1,
                   'c': 1
                   }

BATTLE_INTRO_DURATION = 2
BARREL_INTRO_DURATION = 12
BARREL_ROOM_DURATION = 30
BARREL_ROOM_REWARD_DURATION = 7

class DistributedCogdoInteriorAI(DistributedObjectAI, FSM.FSM):
    notify = DirectNotifyGlobal.directNotify.newCategory("DistributedCogdoInteriorAI")

    def __init__(self, air, exterior):
        DistributedObjectAI.__init__(self, air)
        FSM.FSM.__init__(self, 'CogdoInteriorAIFSM')
        self.toons = filter(None, exterior.elevator.seats[:])
        self.responses = {}
        self.bldgDoId = exterior.doId
        self.numFloors = NUM_FLOORS_DICT[exterior.track]
        self.sosNPC = self.__generateSOS(exterior.difficulty)
        self.shopOwnerNpcId = 0
        self.extZoneId, self.zoneId = exterior.getExteriorAndInteriorZoneId()
        npcIdList = NPCToons.zone2NpcDict.get(self.zoneId, [])

        if len(npcIdList) == 0:
            self.notify.info('No NPC in taken cogdo at %s' % self.zoneId)
        else:
            if len(npcIdList) > 1:
                self.notify.warning('Multiple NPCs in taken cogdo at %s' % self.zoneId)

            self.shopOwnerNpcId = npcIdList[0]

        self.gameDone = 0
        self.bossBattleDone = 0
        self.curFloor = 0
        self.topFloor = 2
        self.timer = Timer.Timer()
        self.exterior = exterior
        self.planner = self.exterior.planner
        self.savedByMap = { }
        self.battle = None
        self.FOType = exterior.track
        self.gameFloor = 1
        self.battleFloor = 2
        self.barrelFloor = -1

        if self.FOType in ('s', 'l'):
            self.battleFloor = 3
            self.barrelFloor = 2
            self.topFloor += 1

        self.toonSkillPtsGained = { }
        self.toonExp = { }
        self.toonOrigQuests = { }
        self.toonItems = { }
        self.toonOrigMerits = { }
        self.toonMerits = { }
        self.toonParts = { }
        self.helpfulToons = []
        self.barrels = []
        self.suits = []
        self.activeSuits = []
        self.reserveSuits = []
        self.joinedReserves = []
        self.suitsKilled = []
        self.suitsKilledPerFloor = []
        self.ignoreResponses = 0
        self.ignoreElevatorDone = 0
        self.ignoreReserveJoinDone = 0

    def __generateSOS(self, difficulty):
        g = lambda: random.choice(NPCToons.FOnpcFriends.keys())
        v = g()

        getStars = lambda x: NPCToons.getNPCTrackLevelHpRarity(x)[-1]

        maxStars = min(2, int(math.ceil(difficulty / 5.)))
        minStars = max(0, maxStars - 1)

        while not (minStars <= getStars(v) <= maxStars):
            v = g()

        self.notify.info('selected SOS %s (stars = %s)' % (v, getStars(v)))
        return v

    def setZoneId(self, zoneId):
        self.zoneId = zoneId

    def getZoneId(self):
        return self.zoneId

    def setExtZoneId(self, extZoneId):
        self.extZoneId = extZoneId

    def getExtZoneId(self):
        return self.extZoneId

    def setDistBldgDoId(self, bldgDoId):
        self.bldgDoId = bldgDoId

    def getDistBldgDoId(self):
        return self.bldgDoId

    def setNumFloors(self, numFloors):
        self.numFloors = numFloors

    def getNumFloors(self):
        return self.numFloors

    def setShopOwnerNpcId(self, id):
        self.shopOwnerNpcId = id

    def getShopOwnerNpcId(self):
        return self.shopOwnerNpcId

    def setState(self, state, timestamp):
        self.request(state)

    def getState(self):
        timestamp = globalClockDelta.getRealNetworkTime()
        return [self.state, timestamp]

    def b_setState(self, state):
        self.setState(state, 0)
        self.d_setState(state)

    def d_setState(self, state):
        timestamp = globalClockDelta.getRealNetworkTime()
        self.sendUpdate('setState', [state, timestamp])

    def reserveJoinDone(self):
        toonId = self.air.getAvatarIdFromSender()
        if self.ignoreResponses == 1:
            return None
        elif self.toons.count(toonId) == 0:
            self.notify.warning('reserveJoinDone() - toon not in list: %d' % toonId)
            return None
        self.b_setState('Battle')

    def elevatorDone(self):
        toonId = self.air.getAvatarIdFromSender()
        if self.ignoreResponses == 1:
            return None
        elif self.toons.count(toonId) == 0:
            self.notify.warning('elevatorDone() - toon not in toon list: %d' % toonId)

    def enterWaitForAllToonsInside(self):
        self.resetResponses()

        if self.FOType == "s":
            self.game = DistCogdoMazeGameAI.DistCogdoMazeGameAI(self.air)
            self.game.setNumSuits(CogdoMazeGameGlobals.NumSuits)
        elif self.FOType == "l":
            self.game = DistCogdoFlyingGameAI.DistCogdoFlyingGameAI(self.air)
        elif self.FOType == "m":
            self.game = DistCogdoCraneGameAI.DistCogdoCraneGameAI(self.air)

        self.sendUpdate("setSOSNpcId", [self.sosNPC])
        self.sendUpdate("setFOType", [ord(self.FOType)])

    def resetResponses(self):
        for toon in self.toons:
            self.responses[toon] = 0

    def setAvatarJoined(self):
        avId = self.air.getAvatarIdFromSender()
        self.responses[avId] = 1
        avatar = self.air.doId2do.get(avId)
        if avatar != None:
            self.savedByMap[avId] = (avatar.getName(), avatar.dna.asTuple())
            self.addToon(avId)
        if self.allToonsJoined():
            self.request('Elevator')

    def addToon(self, avId):
        if not avId in self.toons:
            self.toons.append(avId)

        if avId in self.air.doId2do:
            event = self.air.getAvatarExitEvent(avId)
            self.accept(event, self.__handleUnexpectedExit, [avId])

    def __handleUnexpectedExit(self, avId):
        self.removeToon(avId)
        if len(self.toons) == 0:
            self.exterior.deleteSuitInterior()
            if self.battle:
                self.battle.requestDelete()
                self.battle = None

    def removeToon(self, avId):
        if avId in self.toons: self.toons.pop(avId)

    def enterElevator(self):
        self.curFloor += 1
        self.d_setToons()
        self.resetResponses()

        if self.curFloor == self.gameFloor:
            self.enterGame()

        self.d_setState('Elevator')
        self.timer.stop()
        self.timer.startCallback(BattleBase.ELEVATOR_T + ElevatorData[ELEVATOR_FIELD]['openTime'], self.serverElevatorDone)

        if self.curFloor == self.battleFloor:
            self.planner.myPrint()
            suitHandles = self.planner.genFloorSuits(0)
            self.suits = suitHandles['activeSuits']
            self.activeSuits = self.suits[:]
            self.reserveSuits = suitHandles['reserveSuits']
            self.d_setSuits()

    def exitElevator(self):
        self.timer.stop()

    def serverElevatorDone(self):
        if self.curFloor == self.gameFloor:
            self.d_setState('Game')
        elif self.curFloor == self.battleFloor:
            self.b_setState('BattleIntro')
            self.timer.startCallback(BATTLE_INTRO_DURATION, self.battleIntroDone)
        else:
            self.notify.warning('Unknown floor %s (track=%s)' % (self.curFloor, self.FOType))

    def battleIntroDone(self):
        if self.air:
            self.createBattle()
            self.b_setState('Battle')

    def barrelIntroDone(self):
        if not self.air:
            return

        self.b_setState('CollectBarrels')
        for i in xrange(len(CogdoBarrelRoomConsts.BarrelProps)):
            barrel = DistributedCogdoBarrelAI.DistributedCogdoBarrelAI(self.air, i)
            barrel.generateWithRequired(self.zoneId)
            self.barrels.append(barrel)
        self.timer.startCallback(BARREL_ROOM_DURATION, self.barrelReward)

    def barrelReward(self):
        if not self.air:
            return

        self.b_setState('BarrelRoomReward')
        for i in self.barrels:
            i.requestDelete()
        self.timer.startCallback(BARREL_ROOM_REWARD_DURATION, self.barrelRewardDone)

    def barrelRewardDone(self):
        if not self.air:
            return
        barrelPlanner = SuitPlannerCogdoInteriorAI(self.exterior._cogdoLayout, max(0, self.exterior.difficulty - 5),
                                                   self.FOType, self.exterior.getExteriorAndInteriorZoneId()[1])
        barrelPlanner.myPrint()
        suitHandles = barrelPlanner.genFloorSuits(0)
        self.suits = suitHandles['activeSuits']
        self.activeSuits = self.suits[:]
        self.reserveSuits = suitHandles['reserveSuits']
        self.d_setSuits()
        self.battleIntroDone()

    def handleAllAboard(self, seats):
        if not hasattr(self, 'air') or not self.air:
            return None

        numOfEmptySeats = seats.count(None)
        if numOfEmptySeats == 4:
            self.exterior.deleteSuitInterior()
            return
        elif not 0 <= numOfEmptySeats <= 3:
            self.notify.error('Bad number of empty seats: %s' % numOfEmptySeats)

        for toon in self.toons:
            if toon not in seats:
                self.removeToon(toon)

        self.toons = filter(None, seats)
        self.d_setToons()
        self.request('Elevator')

    def enterGame(self):
        self.game.setToons(self.toons)
        self.game.setInteriorId(self.doId)
        self.game.setExteriorZone(self.exterior.zoneId)
        self.game.setDifficultyOverrides(2147483647, -1)
        self.game.generateWithRequired(self.zoneId)
        self.game.d_startIntro()
        self.accept(self.game.finishEvent, self.__handleGameDone)
        self.accept(self.game.gameOverEvent, self.__handleGameOver)

    def __handleGameDone(self, toons):
        self.game.requestDelete()
        self.gameDone = 1
        self.toons = toons
        if self.curFloor == self.barrelFloor - 1:
            self.curFloor += 1
            self.d_setToons()
            self.resetResponses()
            self.b_setState('BarrelRoomIntro')
            self.timer.startCallback(BARREL_INTRO_DURATION, self.barrelIntroDone)
        else:
            self.request('Elevator')

    def __handleGameOver(self):
        self.game.requestDelete()
        self.exterior.deleteSuitInterior()

    def createBattle(self):
        isBoss = self.curFloor == self.topFloor
        self.battle = DistributedCogdoBattleBldgAI(self.air, self.zoneId, self.__handleRoundDone, self.__handleBattleDone, bossBattle = isBoss)
        self.battle.suitsKilled = self.suitsKilled
        self.battle.suitsKilledPerFloor = self.suitsKilledPerFloor
        self.battle.battleCalc.toonSkillPtsGained = self.toonSkillPtsGained
        self.battle.toonExp = self.toonExp
        self.battle.toonOrigQuests = self.toonOrigQuests
        self.battle.toonItems = self.toonItems
        self.battle.toonOrigMerits = self.toonOrigMerits
        self.battle.toonMerits = self.toonMerits
        self.battle.toonParts = self.toonParts
        self.battle.helpfulToons = self.helpfulToons
        self.battle.setInitialMembers(self.toons, self.suits)
        self.battle.generateWithRequired(self.zoneId)
        mult = getCreditMultiplier(self.curFloor)
        self.battle.battleCalc.setSkillCreditMultiplier(self.battle.battleCalc.getSkillCreditMultiplier() * mult)

    def enterBattleDone(self, toonIds):
        toonIds = toonIds[0]
        if len(toonIds) != len(self.toons):
            deadToons = []
            for toon in self.toons:
                if toonIds.count(toon) == 0:
                    deadToons.append(toon)
                    continue
            for toon in deadToons:
                self.removeToon(toon)

        self.d_setToons()
        if len(self.toons) == 0:
            self.exterior.deleteSuitInterior()
        elif self.curFloor == self.topFloor:
            self.battle.resume(self.curFloor, topFloor = 1)
        else:
            self.battle.resume(self.curFloor, topFloor = 0)

    def __doDeleteInterior(self, task):
        self.exterior.deleteSuitInterior()
        return task.done

    def exitBattleDone(self):
        self.cleanupFloorBattle()

    def cleanupFloorBattle(self):
        for suit in self.suits:
            if suit.isDeleted():
                continue
            suit.requestDelete()

        self.suits = []
        self.reserveSuits = []
        self.activeSuits = []
        if self.battle != None:
            self.battle.requestDelete()

        self.battle = None

    def __handleRoundDone(self, toonIds, totalHp, deadSuits):
        totalMaxHp = 0
        for suit in self.suits:
            totalMaxHp += suit.maxHP

        for suit in deadSuits:
            self.activeSuits.remove(suit)

        if len(self.reserveSuits) > 0 and len(self.activeSuits) < 4:
            self.joinedReserves = []
            hpPercent = 100 - (totalHp / totalMaxHp) * 100.0
            for info in self.reserveSuits:
                if info[1] <= hpPercent and len(self.activeSuits) < 4:
                    self.suits.append(info[0])
                    self.activeSuits.append(info[0])
                    self.joinedReserves.append(info)
                    continue

            for info in self.joinedReserves:
                self.reserveSuits.remove(info)

            if len(self.joinedReserves) > 0:
                self.d_setSuits()
                self.request('ReservesJoining')
                return

        if len(self.activeSuits) == 0:
            self.request('BattleDone', [
                toonIds])
        else:
            self.battle.resume()

    def enterReservesJoining(self):
        self.resetResponses()
        self.timer.startCallback(ElevatorData[ELEVATOR_FIELD]['openTime'] + SUIT_HOLD_ELEVATOR_TIME + BattleBase.SERVER_BUFFER_TIME, self.serverReserveJoinDone)

    def exitReservesJoining(self):
        self.timer.stop()
        self.resetResponses()
        for info in self.joinedReserves:
            self.battle.suitRequestJoin(info[0])

        self.battle.resume()
        self.joinedReserves = []

    def serverReserveJoinDone(self):
        self.ignoreReserveJoinDone = 1
        self.b_setState('Battle')

    def __handleBattleDone(self, zoneId, toonIds):
        if len(toonIds) == 0:
            taskMgr.doMethodLater(10, self.__doDeleteInterior, self.taskName('deleteInterior'))
        elif self.curFloor == self.topFloor:
            self.request('Reward')
        else:
            self.b_setState('Resting')

    def enterResting(self):
        self.intElevator = DistributedCogdoElevatorIntAI.DistributedCogdoElevatorIntAI(self.air, self, self.toons)
        self.intElevator.generateWithRequired(self.zoneId)

    def exitResting(self):
        self.intElevator.requestDelete()

    def enterReward(self):
        victors = self.toons[:]
        savedBy = []
        for v in victors:
            tuple = self.savedByMap.get(v)
            if tuple:
                savedBy.append([
                    v,
                    tuple[0],
                    tuple[1]])

            toon = self.air.doId2do.get(v)
            if toon:
                if self.FOType == 's':
                    if not toon.attemptAddNPCFriend(self.sosNPC, Quests.InFO):
                        self.notify.info('%s unable to add NPCFriend %s to %s.' % (self.doId, self.sosNPC, v))
                elif self.FOType == 'l':
                    reward = self.getEmblemsReward()
                    toon.addEmblems(reward)
                else:
                    self.notify.warning('%s unable to reward %s: unknown reward for track %s' % (self.doId, v, self.FOType))

        self.exterior.fsm.request('waitForVictorsFromCogdo', [
            victors,
            savedBy])
        self.d_setState('Reward')

    def removeToon(self, toonId):
        if self.toons.count(toonId):
            self.toons.remove(toonId)

    def d_setToons(self):
        self.sendUpdate('setToons', self.getToons())

    def getToons(self):
        return [self.toons, 0]

    def d_setSuits(self):
        self.sendUpdate('setSuits', self.getSuits())

    def getSuits(self):
        suitIds = []
        for suit in self.activeSuits:
            suitIds.append(suit.doId)

        reserveIds = []
        values = []
        for info in self.reserveSuits:
            reserveIds.append(info[0].doId)
            values.append(info[1])

        return [
            suitIds,
            reserveIds,
            values]

    def allToonsJoined(self):
        for toon in self.toons:
            if self.responses[toon] == 0:
                return 0
        return 1

    def delete(self):
        DistributedObjectAI.delete(self)
        self.timer.stop()

    def getEmblemsReward(self):
        hoodIdMap = {2: .5, # Toontown Central
                     1: 1., # Donald's Dock
                     5: 1.5, # Daisy Gardens
                     4: 2., # Minnie's Melodyland
                     3: 2.7, # The Brrrgh
                     9: 3.5 # Donald's Dreamland
                     }

        hoodValue = hoodIdMap[int(self.exterior.zoneId // 1000)]
        diff = max(self.exterior.difficulty, 1)
        memos = self.game.getTotalMemos()
        E = (hoodValue * max(memos, 1) * diff) / 2.5
        return divmod(E, 100)[::-1]
