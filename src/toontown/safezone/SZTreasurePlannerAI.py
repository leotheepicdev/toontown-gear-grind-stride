from RegenTreasurePlannerAI import RegenTreasurePlannerAI
from direct.directnotify import DirectNotifyGlobal
from toontown.base import ToontownGlobals

class SZTreasurePlannerAI(RegenTreasurePlannerAI):
    notify = DirectNotifyGlobal.directNotify.newCategory('SZTreasurePlannerAI')

    def __init__(self, zoneId, treasureType, healAmount, spawnPoints, spawnRate, maxTreasures):
        self.zoneId = zoneId
        self.spawnPoints = spawnPoints
        self.healAmount = healAmount
        RegenTreasurePlannerAI.__init__(self, zoneId, treasureType, 'SZTreasurePlanner-%d' % zoneId, spawnRate, maxTreasures)

    def initSpawnPoints(self):
        pass

    def validAvatar(self, treasure, av):
        if treasure.__class__.__name__ == 'DistributedBeanBagTreasureAI':
            av.addMoney(treasure.getValue())
            return True
        if av.getHp() < av.getMaxHp():
            av.toonUp(self.healAmount * 2 if simbase.air.newsManager.isHolidayRunning(ToontownGlobals.VALENTOONS_DAY) else self.healAmount)
            return True
        else:
            return False
