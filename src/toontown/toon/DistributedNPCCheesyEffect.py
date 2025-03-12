from lib.nametag.NametagConstants import CFSpeech, CFTimeout
from toontown.base import TTLocalizer, ToontownGlobals
from toontown.toon import NPCToons
from DistributedNPCToonBase import DistributedNPCToonBase
import CheesyEffectShopGlobals, CheesyEffectShopGui, time

class DistributedNPCCheesyEffect(DistributedNPCToonBase):

    def __init__(self, cr):
        DistributedNPCToonBase.__init__(self, cr)
        self.lastCollision = 0
        self.cheesyDialog = None
        self.toonTag = 'Cheesy Effects'

    def disable(self):
        self.ignoreAll()
        self.destroyDialog()
        DistributedNPCToonBase.disable(self)

    def destroyDialog(self):
        self.clearChat()
        if self.cheesyDialog:
            self.cheesyDialog.destroy()
            self.cheesyDialog = None

    def initToonState(self):
        self.setAnimState('neutral', 0.9, None, None)
        if self.name in NPCToons.CheesyPositions:
            pos = NPCToons.CheesyPositions[self.name]
            self.setPos(*pos[0])
            self.setH(pos[1])

    def getCollSphereRadius(self):
        return 1.25

    def handleCollisionSphereEnter(self, collEntry):
        if self.lastCollision > time.time():
            return
        self.lastCollision = time.time() + ToontownGlobals.NPCCollisionDelay
        if base.localAvatar.getTotalMoney() < ToontownGlobals.CheesyCost:
            self.setChatAbsolute(TTLocalizer.CheesyNoMoneyMessage % ToontownGlobals.CheesyCost, CFSpeech|CFTimeout)
            return
        base.cr.playGame.getPlace().fsm.request('stopped')
        base.setCellsAvailable(base.bottomCells, 0)
        self.setChatAbsolute(TTLocalizer.CheesyPickMessage, CFSpeech|CFTimeout)
        self.accept('cheesyEffectShopDone', self.__cheesyEffectShopDone)
        self.accept('purchaseCheesyEffect', self.purchaseCheesyEffect)
        self.cheesyDialog = CheesyEffectShopGui.CheesyEffectShopGui()

    def freeAvatar(self):
        base.cr.playGame.getPlace().fsm.request('walk')
        base.setCellsAvailable(base.bottomCells, 1)

    def __cheesyEffectShopDone(self, state, index=None):
        self.freeAvatar()
        if state == CheesyEffectShopGlobals.USER_CANCEL:
            self.setChatAbsolute(TTLocalizer.STOREOWNER_GOODBYE, CFSpeech|CFTimeout)
            return
        elif state == CheesyEffectShopGlobals.USER_BUY:
            if index in base.localAvatar.getCheesyEffects():
                self.setChatAbsolute(TTLocalizer.CheesyAlreadyOwn, CFSpeech|CFTimeout)
                return
            self.sendUpdate('buyCheesyEffect', [index])
            
    def purchaseCheesyEffect(self, index):
        self.sendUpdate('buyCheesyEffect', [index])

    def cheesyEffectBuyResult(self, state):
        messenger.send('purchaseCheesyEffectResponse', [state])
