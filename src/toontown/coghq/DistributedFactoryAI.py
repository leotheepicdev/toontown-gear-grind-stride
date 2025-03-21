from direct.directnotify import DirectNotifyGlobal
from direct.task import Task
from toontown.distributed import DistrictGlobals
from toontown.level import DistributedLevelAI, LevelSpec
from toontown.suit import DistributedFactorySuitAI
from toontown.base import ToontownGlobals, ToontownBattleGlobals
from toontown.distributed import DistrictGlobals
from toontown.coghq import DistributedBattleFactoryAI
import FactoryBase, FactoryEntityCreatorAI, FactorySpecs, LevelSuitPlannerAI
from toontown.coghq.sellbothq import FactorySpecsHard, FactorySpecsExtreme
from toontown.toon import NPCToons
import random

class DistributedFactoryAI(DistributedLevelAI.DistributedLevelAI, FactoryBase.FactoryBase):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedFactoryAI')
    EXTREME_SOS_RANGE = NPCToons.npcFriendsMinMaxStars(5, 5)
    HARD_SOS_RANGE = NPCToons.npcFriendsMinMaxStars(3, 4)

    def __init__(self, air, factoryId, zoneId, entranceId, avIds):
        DistributedLevelAI.DistributedLevelAI.__init__(self, air, zoneId, entranceId, avIds)
        FactoryBase.FactoryBase.__init__(self)
        self.setFactoryId(factoryId)

    def createEntityCreator(self):
        return FactoryEntityCreatorAI.FactoryEntityCreatorAI(level=self)

    def getBattleCreditMultiplier(self):
        return ToontownBattleGlobals.getFactoryCreditMultiplier(self.factoryId, self.air.distributedDistrict.getDifficulty())

    def generate(self):
        self.notify.info('generate')
        self.notify.info('start factory %s %s creation, frame=%s' % (self.factoryId, self.doId, globalClock.getFrameCount()))
        self.notify.info('loading spec')
        if self.air.distributedDistrict.getDifficulty() == DistrictGlobals.DIFFICULTY_HARD:
            spec = FactorySpecsHard
        elif self.air.distributedDistrict.getDifficulty() == DistrictGlobals.DIFFICULTY_EXTREME:
            spec = FactorySpecsExtreme
        else:
            spec = FactorySpecs
        specModule = spec.getFactorySpecModule(self.factoryId)
        factorySpec = LevelSpec.LevelSpec(specModule)
        self.notify.info('creating entities')
        DistributedLevelAI.DistributedLevelAI.generate(self, factorySpec)
        self.notify.info('creating cogs')
        cogSpecModule = spec.getCogSpecModule(self.factoryId)
        self.planner = LevelSuitPlannerAI.LevelSuitPlannerAI(self.air, self, DistributedFactorySuitAI.DistributedFactorySuitAI, DistributedBattleFactoryAI.DistributedBattleFactoryAI, cogSpecModule.CogData, cogSpecModule.ReserveCogData, cogSpecModule.BattleCells)
        suitHandles = self.planner.genSuits()
        messenger.send('plannerCreated-' + str(self.doId))
        self.suits = suitHandles['activeSuits']
        self.reserveSuits = suitHandles['reserveSuits']
        self.d_setSuits()
        scenario = 0
        description = '%s|%s|%s|%s' % (self.factoryId,
         self.entranceId,
         scenario,
         self.avIdList)
        for avId in self.avIdList:
            self.air.writeServerEvent('factoryEntered', avId, description)

        self.notify.info('finish factory %s %s creation' % (self.factoryId, self.doId))

    def delete(self):
        self.notify.info('delete: %s' % self.doId)
        suits = self.suits
        for reserve in self.reserveSuits:
            suits.append(reserve[0])

        self.planner.destroy()
        del self.planner
        for suit in suits:
            if not suit.isDeleted():
                suit.factoryIsGoingDown()
                suit.requestDelete()

        DistributedLevelAI.DistributedLevelAI.delete(self)

    def getTaskZoneId(self):
        return self.factoryId

    def getFactoryId(self):
        return self.factoryId

    def d_setForemanConfronted(self, avId):
        if avId in self.avIdList:
            self.sendUpdate('setForemanConfronted', [avId])
        else:
            self.notify.warning('%s: d_setForemanConfronted: av %s not in av list %s' % (self.doId, avId, self.avIdList))

    def setVictors(self, victorIds):
        activeVictors = []
        activeVictorIds = []
        for victorId in victorIds:
            toon = self.air.doId2do.get(victorId)
            if toon is not None:
                activeVictors.append(toon)
                activeVictorIds.append(victorId)
        scenario = 0
        description = '%s|%s|%s|%s' % (self.factoryId, self.entranceId, scenario, activeVictorIds)
        for avId in activeVictorIds:
            self.air.writeServerEvent('factoryDefeated', avId, description)
        difficulty = simbase.air.distributedDistrict.getDifficulty()
        if difficulty == DistrictGlobals.DIFFICULTY_EXTREME:
            npcId = random.choice(self.EXTREME_SOS_RANGE)
        elif difficulty == DistrictGlobals.DIFFICULTY_HARD:
            npcId = random.choice(self.HARD_SOS_RANGE)
        for toon in activeVictors:
            simbase.air.questManager.toonDefeatedFactory(toon, self.factoryId)
            if difficulty == DistrictGlobals.DIFFICULTY_EXTREME:
                toon.attemptAddNPCFriend(npcId)
                toon.addMoney(ToontownGlobals.FACTORY_JELLYBEAN_REWARD_EXTREME)
                self.sendUpdate('announceFactoryReward', [difficulty, npcId])
            elif difficulty == DistrictGlobals.DIFFICULTY_HARD:
                toon.attemptAddNPCFriend(npcId)
                toon.addMoney(ToontownGlobals.FACTORY_JELLYBEAN_REWARD_HARD)
                self.sendUpdate('announceFactoryReward', [difficulty, npcId])
                
    def b_setDefeated(self):
        self.d_setDefeated()
        self.setDefeated()

    def d_setDefeated(self):
        self.sendUpdate('setDefeated')

    def setDefeated(self):
        pass

    def getCogLevel(self):
        return self.cogLevel

    def d_setSuits(self):
        self.sendUpdate('setSuits', [self.getSuits(), self.getReserveSuits()])

    def getSuits(self):
        suitIds = []
        for suit in self.suits:
            suitIds.append(suit.doId)

        return suitIds

    def getReserveSuits(self):
        suitIds = []
        for suit in self.reserveSuits:
            suitIds.append(suit[0].doId)

        return suitIds
