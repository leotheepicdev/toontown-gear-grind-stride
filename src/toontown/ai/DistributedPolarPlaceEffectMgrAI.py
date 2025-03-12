from direct.directnotify import DirectNotifyGlobal
from direct.distributed.DistributedObjectAI import DistributedObjectAI
from direct.distributed.ClockDelta import *
from direct.fsm.FSM import FSM
from toontown.base.ToontownGlobals import CEBigWhite

class DistributedPolarPlaceEffectMgrAI(DistributedObjectAI, FSM):
    notify = DirectNotifyGlobal.directNotify.newCategory("DistributedPolarPlaceEffectMgrAI")

    def __init__(self, air):
        DistributedObjectAI.__init__(self, air)
        FSM.__init__(self, 'ResistanceFSM')
        self.air = air

    def enterOff(self):
        self.requestDelete()

    def addPolarPlaceEffect(self):
        avId = self.air.getAvatarIdFromSender()
        av = self.air.doId2do.get(avId)
        if not av:
            return
        if not av.hasCheesyEffect(CEBigWhite):
            av.addCheesyEffect(CEBigWhite)
