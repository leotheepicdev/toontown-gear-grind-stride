from toontown.base import ToontownGlobals, TTLocalizer
import DistributedNPCToonBaseAI, NametagNPCGlobals

class DistributedNPCNametagAI(DistributedNPCToonBaseAI.DistributedNPCToonBaseAI):

    def changeNametagColor(self, color):
        avId = self.air.getAvatarIdFromSender()
        av = self.air.doId2do.get(avId)

        if av is None or not hasattr(av, 'dna'):
            return
        elif len(TTLocalizer.NametagColorNames) < color:
            self.sendUpdate('changeNametagColorResult', [avId, NametagNPCGlobals.INVALID_ITEM])
            return
        elif av.nametagColor == color:
            self.sendUpdate('changeNametagColorResult', [avId, NametagNPCGlobals.SAME_ITEM])
            return
        elif av.getTotalMoney() < ToontownGlobals.NametagColorCost:
            self.sendUpdate('changeNametagColorResult', [avId, NametagNPCGlobals.NOT_ENOUGH_MONEY])
            return

        av.takeMoney(ToontownGlobals.NametagColorCost)
        taskMgr.doMethodLater(1.0, lambda task: self.performNametagColorChange(av, color), 'transform-%d' % avId)
        self.sendUpdate('changeNametagColorResult', [avId, NametagNPCGlobals.CHANGE_SUCCESSFUL])
        
    def performNametagColorChange(self, av, color):
        av.b_setNametagColor(color)
        av.addNametagColor(color)
        
    def changeNametagStyle(self, style):
        avId = self.air.getAvatarIdFromSender()
        av = self.air.doId2do.get(avId)

        if av is None or not hasattr(av, 'dna'):
            return
        elif len(TTLocalizer.NametagFontNames) < style:
            self.sendUpdate('changeNametagStyleResult', [avId, NametagNPCGlobals.INVALID_ITEM])
            return
        elif av.nametagStyle == style:
            self.sendUpdate('changeNametagStyleResult', [avId, NametagNPCGlobals.SAME_ITEM])
            return
        elif av.getTotalMoney() < ToontownGlobals.NametagStyleCost:
            self.sendUpdate('changeNametagStyleResult', [avId, NametagNPCGlobals.NOT_ENOUGH_MONEY])
            return

        av.takeMoney(ToontownGlobals.GloveCost)
        taskMgr.doMethodLater(1.0, lambda task: self.performNametagStyleChange(av, style), 'transform-%d' % avId)
        self.sendUpdate('changeNametagStyleResult', [avId, NametagNPCGlobals.CHANGE_SUCCESSFUL])
        
    def performNametagStyleChange(self, av, style):
        av.b_setNametagStyle(style)
        av.addNametagStyle(style)