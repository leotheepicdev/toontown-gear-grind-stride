from panda3d.core import Vec4, TextNode
from direct.gui.DirectGui import DirectButton, DirectLabel, DirectFrame, DirectScrolledList, DGG
from direct.interval.IntervalGlobal import Sequence, Func, LerpColorScaleInterval
from toontown.base import ToontownGlobals, TTLocalizer
import CheesyEffectShopGlobals

class CheesyEffectShopGui(DirectFrame):

    def __init__(self):
        DirectFrame.__init__(self, parent=aspect2d, relief=None, geom=DGG.getDefaultDialogGeom(), geom_color=ToontownGlobals.GlobalDialogColor, 
                             geom_scale=(2, 1, 1.5), pos=(0, 0, 0))
        self.initialiseoptions(CheesyEffectShopGui)
        self.cheesyEffectButtons = []
        
        self.title = DirectLabel(parent=self, relief=None, text=TTLocalizer.CheesyTitle, text_font=ToontownGlobals.getSignFont(), text_fg=(1, 1, 1, 1), text_shadow=(0, 0, 0, 1), pos=(0, 0, 0.6), text_scale=0.12)
        
        self.gui = loader.loadModel('phase_3.5/models/gui/friendslist_gui')
        self.scrollList = None
        self.listXorigin = -0.02
        self.listFrameSizeX = 0.67
        self.listZorigin = -0.96
        self.listFrameSizeZ = 1.04
        self.arrowButtonScale = 1.3
        self.itemFrameXorigin = -0.247
        self.itemFrameZorigin = 0.365
        self.buttonXstart = self.itemFrameXorigin + 0.293
        self.oldCheesyEffect = base.localAvatar.getCheesyEffect()
        self.info = None
        self.cheesyName = None
        self.cheesyCost = None
        self.cheesyDesc = None
        self.previewButton = None
        self.purchaseButton = None
        self.backButton = None
        self.callbackMsg = None
        self.callbackSeq = None
        
        guiButton = loader.loadModel('phase_3/models/gui/quit_button')
        self.buttonImage = (guiButton.find('**/QuitBtn_UP'), guiButton.find('**/QuitBtn_DN'), guiButton.find('**/QuitBtn_RLVR'))
        self.generateCheesyEffectButtons()
        self.generateScrollList()
        self.exitButton = DirectButton(parent=self, relief=None, image=self.buttonImage, text=TTLocalizer.CheesyExit, pos=(0.75, 0, -0.68), text_scale=0.07, text_pos=(0, -0.02), command=self.__exit, extraArgs=[CheesyEffectShopGlobals.USER_CANCEL])

    def generateCheesyEffectButtons(self):
        if self.cheesyEffectButtons:
            for button in self.cheesyEffectButtons:
                button.destroy()
                del button
        self.cheesyEffectButtons = []
        for i in xrange(1, ToontownGlobals.CETotalAvailableNum):
            if i in base.localAvatar.getCheesyEffects():
                continue
            cheesyEffectButton = DirectButton(parent=self, relief=None, text=TTLocalizer.CheesyEffectNames[i], text_scale=0.06, text_align=TextNode.ALeft, text_fg=Vec4(0, 0, 0, 1),
                                              text3_fg=Vec4(0.4, 0.8, 0.4, 1), text1_bg=Vec4(0.5, 0.9, 1, 1), text2_bg=Vec4(1, 1, 0, 1), command=self.loadCheesyPage, extraArgs=[i])
            self.cheesyEffectButtons.append(cheesyEffectButton)
        self.info = DirectLabel(parent=self, relief=None, text='', pos=(0.35, 0, 0.1), text_wordwrap=16.5, text_scale=0.07)
        if not self.cheesyEffectButtons:
            self.info['text'] = TTLocalizer.AllCheesyPurchased
        else:
            self.info['text'] = TTLocalizer.NoCheesySelected
                                              
    def loadCheesyPage(self, i):
        for x in (self.info, self.cheesyName, self.cheesyDesc, self.previewButton, self.purchaseButton):
            if x:
                x.destroy()
                x = None
        self.cheesyName = DirectLabel(parent=self, relief=None, text=TTLocalizer.CheesyName % TTLocalizer.CheesyEffectNames[i], pos=(0.35, 0, 0.1), text_scale=0.07)
        if not self.cheesyCost:
            self.cheesyCost = DirectLabel(parent=self, relief=None, text=TTLocalizer.CheesyCost % ToontownGlobals.CheesyCost, pos=(0.35, 0, 0.0), text_scale=0.07)
        self.cheesyDesc = DirectLabel(parent=self, relief=None, text=TTLocalizer.CheesyDescription + '\n%s' % TTLocalizer.CheesyEffectDesc[i], text_wordwrap=16.5, pos=(0.35, 0, -0.1), text_scale=0.07)
        self.previewButton = DirectButton(parent=self, relief=None, image=self.buttonImage, text=TTLocalizer.CheesyPreview, pos=(0.33, 0, -0.68), text_scale=0.07, text_pos=(0, -0.02), command=self.previewCheesyEffect, extraArgs=[i])
        self.purchaseButton = DirectButton(parent=self, relief=None, image=self.buttonImage, text=TTLocalizer.CheesyPurchase, pos=(-0.09, 0, -0.68), text_scale=0.07, text_pos=(0, -0.02), command=self.purchaseCheesyEffect, extraArgs=[i])
        
    def previewCheesyEffect(self, i):
        self.hide()
        base.localAvatar.setCheesyEffect(i)
        self.backButton = DirectButton(parent=base.a2dBottomRight, relief=None, image=self.buttonImage, text=TTLocalizer.CheesyGoBack, pos=(-0.25, 0, 0.075), text_scale=0.07, text_pos=(0, -0.02), command=self.previewGoBack)
        
    def previewGoBack(self):
        self.backButton.destroy()
        self.backButton = None
        base.localAvatar.setCheesyEffect(self.oldCheesyEffect)
        self.show()
        
    def purchaseCheesyEffect(self, i):
        self.acceptOnce('purchaseCheesyEffectResponse', self.purchaseCheesyEffectResponse)
        messenger.send('purchaseCheesyEffect', [i])
        
    def purchaseCheesyEffectResponse(self, state):
        if state == CheesyEffectShopGlobals.PURCHASE_SUCCESSFUL:
            msg = TTLocalizer.CheesyPurchaseSuccess
            for x in (self.info, self.cheesyName, self.cheesyCost, self.cheesyDesc, self.previewButton, self.purchaseButton):
                if x:
                    x.destroy()
                    x = None
            self.scrollList.destroy()
            self.scrollList = None
            self.generateCheesyEffectButtons()
            self.generateScrollList()
            if self.callbackSeq:
                # We purchased another cheesy effect while this is still going on
                self.destroyCallback()
            self.callbackMsg = DirectLabel(parent=self, relief=None, text=TTLocalizer.CheesyPurchaseSuccess, text_font=ToontownGlobals.getSignFont(), text_fg=(0, 1, 0, 1), text_shadow=(0, 0, 0, 1), pos=(0, 0, -0.9), text_scale=0.1)
            self.callbackSeq = Sequence(LerpColorScaleInterval(self.callbackMsg, 1.33, Vec4(1, 1, 1, 0), startColorScale=Vec4(1, 1, 1, 1), blendType='easeIn'), 
                                        LerpColorScaleInterval(self.callbackMsg, 1.33, Vec4(1, 1, 1, 1), startColorScale=Vec4(1, 1, 1, 0), blendType='easeIn'),
                                        LerpColorScaleInterval(self.callbackMsg, 1.33, Vec4(1, 1, 1, 0), startColorScale=Vec4(1, 1, 1, 1), blendType='easeIn'),
                                        Func(self.destroyCallback))
            self.callbackSeq.start()
                                        
    def destroyCallback(self):
        if self.callbackSeq:
            self.callbackSeq.finish()
        if self.callbackMsg:
            self.callbackMsg.destroy()
            self.callbackMsg = None
            
    def updateScrollList(self):
        self.scrollList.scrollTo
            
    def generateScrollList(self):
        selectedIndex = 0
        self.scrollList = DirectScrolledList(parent=self, relief=None, pos=(-0.66, 0, 0), incButton_image=(self.gui.find('**/FndsLst_ScrollUp'),
         self.gui.find('**/FndsLst_ScrollDN'),
         self.gui.find('**/FndsLst_ScrollUp_Rllvr'),
         self.gui.find('**/FndsLst_ScrollUp')), incButton_relief=None, incButton_scale=(self.arrowButtonScale, self.arrowButtonScale, -self.arrowButtonScale), incButton_pos=(self.buttonXstart + 0.005, 0, self.itemFrameZorigin - 1.000), incButton_image3_color=Vec4(1, 1, 1, 0.2), decButton_image=(self.gui.find('**/FndsLst_ScrollUp'),
         self.gui.find('**/FndsLst_ScrollDN'),
         self.gui.find('**/FndsLst_ScrollUp_Rllvr'),
         self.gui.find('**/FndsLst_ScrollUp')), decButton_relief=None, decButton_scale=(self.arrowButtonScale, self.arrowButtonScale, self.arrowButtonScale), decButton_pos=(self.buttonXstart, 0.0025, self.itemFrameZorigin + 0.130), decButton_image3_color=Vec4(1, 1, 1, 0.2), itemFrame_pos=(self.itemFrameXorigin, 0, self.itemFrameZorigin), itemFrame_scale=1.0, itemFrame_relief=DGG.SUNKEN, itemFrame_frameSize=(self.listXorigin,
         self.listXorigin + self.listFrameSizeX,
         self.listZorigin,
         self.listZorigin + self.listFrameSizeZ), itemFrame_frameColor=(0.85, 0.95, 1, 1), itemFrame_borderWidth=(0.01, 0.01), numItemsVisible=15, forceHeight=0.065, items=self.cheesyEffectButtons)
        self.scrollList.scrollTo(selectedIndex)

    def destroy(self):
        self.ignoreAll()
            
        self.title.destroy()
        del self.title        

        if self.scrollList:
            self.scrollList.destroy()
            del self.scrollList
        del self.cheesyEffectButtons
        self.info.destroy()
        del self.info
        for x in (self.cheesyName, self.cheesyDesc, self.cheesyCost, self.previewButton, self.purchaseButton):
            if x:
                x.destroy()
                del x
        self.destroyCallback()
        self.exitButton.destroy()
        del self.exitButton
        DirectFrame.destroy(self)

    def __exit(self, state, index=None):
        self.destroy()
        messenger.send('cheesyEffectShopDone', [state, index if index is not None else 0])