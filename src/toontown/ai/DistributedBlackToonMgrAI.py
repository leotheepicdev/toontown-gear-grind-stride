from direct.directnotify import DirectNotifyGlobal
from direct.distributed.DistributedObjectAI import DistributedObjectAI
from toontown.toon.ToonDNA import ToonDNA
from toontown.base import ToontownGlobals

class DistributedBlackToonMgrAI(DistributedObjectAI):
    notify = DirectNotifyGlobal.directNotify.newCategory("DistributedBlackToonMgrAI")

    def requestBlackToonTransformation(self):
        if not self.air.newsManager.isHolidayRunning(ToontownGlobals.BLACK_TOON_DAY):
            return
        avId = self.air.getAvatarIdFromSender()
        av = self.air.doId2do.get(avId)
        if not av or av.dna.headColor == 0x1a:
            return
        newDNA = ToonDNA()
        newDNA.makeFromNetString(av.getDNAString())
        newDNA.updateToonProperties(armColor=26, legColor=26, headColor=26)
        taskMgr.doMethodLater(1.0, lambda task: av.b_setDNAString(newDNA.makeNetString()), 'transform-%d' % avId)
        self.sendUpdateToAvatarId(avId, 'doBlackToonTransformation', [])
