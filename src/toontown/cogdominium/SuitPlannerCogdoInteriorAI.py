from otp.ai.AIBaseGlobal import *
from toontown.suit import SuitDNA
from direct.directnotify import DirectNotifyGlobal
from toontown.suit import DistributedSuitAI
from toontown.building import SuitBuildingGlobals
from toontown.suit.SuitInvasionGlobals import IFSkelecog, IFWaiter, IFV2, IFExecutive, IFVirtual
import types, math, random

BASE_RESERVE = 10

MAX_RESERVES = {
                's': BASE_RESERVE * .9,
                'm': BASE_RESERVE * 1.1,
                'l': BASE_RESERVE * 1.25,
                'c': BASE_RESERVE * 1.5,
               }

def filterReviveChance(track, revive):
    if revive >= 0:
        return revive

    return random.randint(config.GetInt('min-lt-vs', 0), config.GetInt('max-lt-vs', 2))
    # Implements difficulty 19 / LT.

def getMaxReserves(track):
    return int(math.ceil(MAX_RESERVES[track]))

class SuitPlannerCogdoInteriorAI:
    notify = DirectNotifyGlobal.directNotify.newCategory('SuitPlannerCogdoInteriorAI')

    def __init__(self, layout, difficulty, track, zoneId, numFloors = 1):
        self.zoneId = zoneId
        self.numFloors = layout.getNumFloors()
        self.respectInvasions = 1

        if isinstance(difficulty, types.StringType):
            self.notify.warning('difficulty is a string!')
            difficulty = int(difficulty)

        self._genSuitInfos(numFloors, difficulty, track)

    def __genJoinChances(self, num):
        joinChances = []
        for currChance in xrange(num):
            joinChances.append(random.randint(1, 100))

        joinChances.sort(cmp)
        return joinChances

    def _genSuitInfos(self, numFloors, difficulty, bldgTrack):
        self.suitInfos = []
        self.notify.debug('\n\ngenerating suitsInfos with numFloors (' + str(numFloors) + ') difficulty (' + str(difficulty) + '+1) and bldgTrack (' + str(bldgTrack) + ')')
        for currFloor in xrange(numFloors):
            infoDict = {}
            lvls = self.__genLevelList(difficulty, currFloor, numFloors)
            activeDicts = []
            numActive = random.randint(1, min(4, len(lvls)))

            if currFloor + 1 == numFloors and len(lvls) > 1:
                origBossSpot = len(lvls) - 1

                if numActive == 1:
                    newBossSpot = numActive - 1
                else:
                    newBossSpot = numActive - 2

                tmp = lvls[newBossSpot]
                lvls[newBossSpot] = lvls[origBossSpot]
                lvls[origBossSpot] = tmp

            bldgInfo = SuitBuildingGlobals.CogBuildings[difficulty]

            if len(bldgInfo) > SuitBuildingGlobals.SUIT_BLDG_INFO_REVIVES:
                revives = bldgInfo[SuitBuildingGlobals.SUIT_BLDG_INFO_REVIVES][0]
            else:
                revives = 0

            for currActive in xrange(numActive - 1, -1, -1):
                level = lvls[currActive]
                type = self.__genNormalSuitType(level)
                activeDict = {}
                activeDict['type'] = type
                activeDict['track'] = bldgTrack
                activeDict['level'] = level
                activeDict['revives'] = filterReviveChance(bldgTrack, revives)
                activeDicts.append(activeDict)

            infoDict['activeSuits'] = activeDicts
            reserveDicts = []
            numReserve = min(len(lvls) - numActive, getMaxReserves(bldgTrack))
            joinChances = self.__genJoinChances(numReserve)
            for currReserve in xrange(numReserve):
                level = lvls[currReserve + numActive]
                type = self.__genNormalSuitType(level)
                reserveDict = {}
                reserveDict['type'] = type
                reserveDict['track'] = bldgTrack
                reserveDict['level'] = level
                reserveDict['revives'] = filterReviveChance(bldgTrack, revives)
                reserveDict['joinChance'] = joinChances[currReserve]
                reserveDicts.append(reserveDict)

            infoDict['reserveSuits'] = reserveDicts
            self.suitInfos.append(infoDict)

    def __genNormalSuitType(self, lvl):
        return SuitDNA.getRandomSuitType(lvl)

    def __genLevelList(self, difficulty, currFloor, numFloors):
        bldgInfo = SuitBuildingGlobals.CogBuildings[difficulty]

        lvlPoolRange = bldgInfo[SuitBuildingGlobals.SUIT_BLDG_INFO_LVL_POOL]
        maxFloors = bldgInfo[SuitBuildingGlobals.SUIT_BLDG_INFO_FLOORS][1]
        lvlPoolMults = bldgInfo[SuitBuildingGlobals.SUIT_BLDG_INFO_LVL_POOL_MULTS]
        floorIdx = min(currFloor, maxFloors - 1)
        lvlPoolMin = lvlPoolRange[0] * lvlPoolMults[floorIdx]
        lvlPoolMax = lvlPoolRange[1] * lvlPoolMults[floorIdx]
        lvlPool = random.randint(int(lvlPoolMin), int(lvlPoolMax))
        lvlMin = bldgInfo[SuitBuildingGlobals.SUIT_BLDG_INFO_SUIT_LVLS][0]
        lvlMax = bldgInfo[SuitBuildingGlobals.SUIT_BLDG_INFO_SUIT_LVLS][1]
        self.notify.debug('Level Pool: ' + str(lvlPool))
        lvlList = []
        while lvlPool >= lvlMin:
            newLvl = random.randint(lvlMin, min(lvlPool, lvlMax))
            lvlList.append(newLvl)
            lvlPool -= newLvl

        if currFloor + 1 == numFloors:
            bossLvlRange = bldgInfo[SuitBuildingGlobals.SUIT_BLDG_INFO_BOSS_LVLS]
            newLvl = random.randint(bossLvlRange[0], bossLvlRange[1])
            lvlList.append(newLvl)
        lvlList.sort(cmp)
        self.notify.debug('LevelList: ' + repr(lvlList))
        return lvlList

    def __setupSuitInfo(self, suit, bldgTrack, suitLevel, suitType):
        suitDeptIndex, suitTypeIndex, flags = simbase.air.suitInvasionManager.getInvadingCog()
        if self.respectInvasions:
            if suitDeptIndex is not None:
                bldgTrack = SuitDNA.suitDepts[suitDeptIndex]
            if suitTypeIndex is not None:
                suitName = SuitDNA.getSuitName(suitDeptIndex, suitTypeIndex)
                suitType = SuitDNA.getSuitType(suitName)
                suitLevel = min(max(suitLevel, suitType), suitType + 4)
        dna = SuitDNA.SuitDNA()
        dna.newSuitRandom(suitType, bldgTrack)
        suit.dna = dna
        self.notify.debug('Creating suit type ' + suit.dna.name + ' of level ' + str(suitLevel) + ' from type ' + str(suitType) + ' and track ' + str(bldgTrack))
        suit.setLevel(suitLevel)
        return flags

    def __genSuitObject(self, suitZone, suitType, bldgTrack, suitLevel, revives = 0):
        newSuit = DistributedSuitAI.DistributedSuitAI(simbase.air, None)
        flags = self.__setupSuitInfo(newSuit, bldgTrack, suitLevel, suitType)
        if flags & IFSkelecog:
            newSuit.setSkelecog(1)
        newSuit.setSkeleRevives(revives)
        newSuit.generateWithRequired(suitZone)
        if flags & IFVirtual:
            newSuit.b_setSkelecog(1)
            newSuit.b_setVirtual((1, random.randint(0, 4)))
        if flags & IFWaiter:
            newSuit.b_setWaiter(1)
        if flags & IFV2:
            newSuit.b_setSkeleRevives(1)
        if flags & IFExecutive:
            newSuit.b_setExecutive(1)
        newSuit.node().setName('suit-%s' % newSuit.doId)
        return newSuit

    def myPrint(self):
        print 'Generated suits for cogdo: '

        for floor, currInfo in enumerate(self.suitInfos):
            floor += 1

            actives = currInfo['activeSuits']
            reserves = currInfo['reserveSuits']

            print ' Floor %d has %d active suits.' % (floor, len(actives))
            print ' Floor %d has %d reserve suits.' % (floor, len(reserves))

            for idx, currActive in enumerate(actives):
                type, track, level, revives = map(lambda x: currActive[x], ('type', 'track', 'level', 'revives'))

                print '-- Active suit %d is %s, %s and level %d and revives is %d' % (idx, type, track, level, revives)

            for idx, currReserve in enumerate(reserves):
                type, track, level, revives, res = map(lambda x: currReserve[x], ('type', 'track', 'level', 'revives', 'joinChance'))
                print '- Reserve suit %d is %s, %s and level %d and JC = %d and revives is %d' % (idx, type, track, level, res, revives)

    def genFloorSuits(self, floor):
        suitHandles = {}
        floorInfo = self.suitInfos[floor]
        activeSuits = []
        for activeSuitInfo in floorInfo['activeSuits']:
            suit = self.__genSuitObject(self.zoneId, activeSuitInfo['type'], activeSuitInfo['track'], activeSuitInfo['level'], activeSuitInfo['revives'])
            activeSuits.append(suit)

        suitHandles['activeSuits'] = activeSuits
        reserveSuits = []
        for reserveSuitInfo in floorInfo['reserveSuits']:
            suit = self.__genSuitObject(self.zoneId, reserveSuitInfo['type'], reserveSuitInfo['track'], reserveSuitInfo['level'], reserveSuitInfo['revives'])
            reserveSuits.append((suit, reserveSuitInfo['joinChance']))

        suitHandles['reserveSuits'] = reserveSuits
        return suitHandles

    def genSuits(self):
        suitHandles = []
        for floor in xrange(len(self.suitInfos)):
            floorSuitHandles = self.genFloorSuits(floor)
            suitHandles.append(floorSuitHandles)

        return suitHandles
