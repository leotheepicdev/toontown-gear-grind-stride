from direct.directnotify import DirectNotifyGlobal
from direct.distributed.DistributedObject import DistributedObject
from toontown.base import ToontownGlobals

class DistributedBlackToonMgr(DistributedObject):
    neverDisable = 1
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedBlackToonMgr')

    def announceGenerate(self):
        DistributedObject.announceGenerate(self)
        base.cr.blackToonMgr = self

    def delete(self):
        base.cr.blackToonMgr = None
        DistributedObject.delete(self)

    def requestBlackToonTransformation(self):
        if not base.cr.newsManager.isHolidayRunning(ToontownGlobals.BLACK_TOON_DAY):
            return
        self.sendUpdate('requestBlackToonTransformation')

    def doBlackToonTransformation(self):
        base.localAvatar.getDustCloud(0.0, color=base.localAvatar.style.getBlackColor()).start()
