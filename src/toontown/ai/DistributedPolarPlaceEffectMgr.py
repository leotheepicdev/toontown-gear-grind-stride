from direct.directnotify import DirectNotifyGlobal
from direct.distributed import DistributedObject
from direct.interval.IntervalGlobal import *
from toontown.speedchat import SpeedChatGlobals
from toontown.base import TTLocalizer
from toontown.base.ToontownGlobals import CEBigWhite

class DistributedPolarPlaceEffectMgr(DistributedObject.DistributedObject):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedPolarPlaceEffectMgr')

    def __init__(self, cr):
        DistributedObject.DistributedObject.__init__(self, cr)

    def announceGenerate(self):
        DistributedObject.DistributedObject.announceGenerate(self)
        DistributedPolarPlaceEffectMgr.notify.debug('announceGenerate')
        self.accept(SpeedChatGlobals.SCStaticTextMsgEvent, self.phraseSaid)

    def phraseSaid(self, phraseId):
        if base.localAvatar.hasCheesyEffect(CEBigWhite):
            return
        helpPhrase = 104
        if phraseId == helpPhrase:
            self.addPolarPlaceEffect()

    def delete(self):
        self.ignore(SpeedChatGlobals.SCStaticTextMsgEvent)
        DistributedObject.DistributedObject.delete(self)

    def addPolarPlaceEffect(self):
        DistributedPolarPlaceEffectMgr.notify.debug('addResitanceEffect')
        av = base.localAvatar
        self.sendUpdate('addPolarPlaceEffect', [])
        msgTrack = Sequence(Func(av.setSystemMessage, 0, TTLocalizer.PolarPlaceEffect1), Wait(2), Func(av.setSystemMessage, 0, TTLocalizer.PolarPlaceEffect2))
        msgTrack.start()
