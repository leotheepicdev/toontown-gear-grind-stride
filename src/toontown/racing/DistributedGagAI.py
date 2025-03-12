from direct.directnotify import DirectNotifyGlobal
from direct.distributed.ClockDelta import globalClockDelta
from direct.distributed.DistributedObjectAI import DistributedObjectAI

class DistributedGagAI(DistributedObjectAI):
    notify = DirectNotifyGlobal.directNotify.newCategory("DistributedGagAI")

    def __init__(self, air, avId, race, todo0, x, y, z, type):
        DistributedObjectAI.__init__(self, air)
        self.initTime = globalClockDelta.getFrameNetworkTime()
        self.ownerId = avId
        self.race = race
        self.activateTime = 0
        self.pos = (x, y, z)
        self.type = type

    def getInitTime(self):
        return self.initTime

    def getActivateTime(self):
        return self.activateTime

    def getPos(self):
        return self.pos

    def getRace(self):
        return self.race.getDoId()

    def getOwnerId(self):
        return self.ownerId

    def getType(self):
        return self.type

    def hitSomebody(self, avId, timestamp):
        self.race.thrownGags.remove(self)
        self.requestDelete()
