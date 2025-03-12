from direct.directnotify import DirectNotifyGlobal
from toontown.racing.DistributedKartPadAI import DistributedKartPadAI
from toontown.racing.KartShopGlobals import KartGlobals
from direct.distributed.ClockDelta import *

class DistributedViewPadAI(DistributedKartPadAI):
    notify = DirectNotifyGlobal.directNotify.newCategory("DistributedViewPadAI")

    def __init__(self, air):
        DistributedKartPadAI.__init__(self, air)
        self.timestamp = globalClockDelta.getRealNetworkTime()

    def setLastEntered(self, timestamp):
        self.timestamp = timestamp

    def d_setLastEntered(self, timestamp):
        self.sendUpdate('setLastEntered', [timestamp])

    def b_setLastEntered(self, timestamp):
        self.setLastEntered(timestamp)
        self.d_setLastEntered(timestamp)

    def getLastEntered(self):
        return self.timestamp
        
    def addAvBlock(self, avId, startingBlock):
        av = self.air.doId2do.get(avId)
        if not av:
            return
        if not av.hasKart():
            return KartGlobals.ERROR_CODE.eNoKart
        if startingBlock.avId:
            return KartGlobals.ERROR_CODE_eOccupied
        self.b_setLastEntered(globalClockDelta.getRealNetworkTime())
        return KartGlobals.ERROR_CODE.success
        
    def removeAvBlock(self, avId, startingBlock):
        pass
        
    def kartMovieDone(self):
        pass
