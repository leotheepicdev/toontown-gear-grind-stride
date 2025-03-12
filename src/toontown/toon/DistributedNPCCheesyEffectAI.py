from toontown.base import ToontownGlobals
import DistributedNPCToonBaseAI, CheesyEffectShopGlobals
    
class DistributedNPCCheesyEffectAI(DistributedNPCToonBaseAI.DistributedNPCToonBaseAI):

    def buyCheesyEffect(self, effect):
        avId = self.air.getAvatarIdFromSender()
        av = self.air.doId2do.get(avId)
        if av is None:
            return
        if effect in av.getCheesyEffects():
            self.sendUpdate('cheesyEffectBuyResult', [CheesyEffectShopGlobals.PURCHASE_OWN])
            return
        if av.getTotalMoney() < ToontownGlobals.CheesyCost:
            self.sendUpdate('cheesyEffectBuyResult', [CheesyEffectShopGlobals.NOT_ENOUGH_MONEY])
            return
        av.takeMoney(ToontownGlobals.CheesyCost)
        av.addCheesyEffect(effect)
        self.sendUpdate('cheesyEffectBuyResult', [CheesyEffectShopGlobals.PURCHASE_SUCCESSFUL])