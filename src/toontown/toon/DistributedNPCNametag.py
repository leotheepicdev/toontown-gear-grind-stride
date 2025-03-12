from direct.gui.DirectGui import DirectButton, DirectLabel
from lib.nametag.NametagConstants import CFSpeech, CFTimeout
from toontown.base import TTLocalizer, ToontownGlobals
from toontown.toon import NPCToons
from DistributedNPCToonBase import DistributedNPCToonBase
import NametagNPCGlobals, NametagColorShopGui, NametagStyleShopGui
import NametagNPCGlobals
import time

class DistributedNPCNametag(DistributedNPCToonBase):

    def __init__(self, cr):
        DistributedNPCToonBase.__init__(self, cr)
        self.lastCollision = 0
        self.nametagColorDialog = None
        self.nametagStyleDialog = None
        self.toonTag = 'Nametag Clerk'

    def disable(self):
        self.ignoreAll()
        self.destroyDialog()
        DistributedNPCToonBase.disable(self)

    def destroyDialog(self):
        self.clearChat()
        if self.nametagColorDialog:
            self.nametagColorDialog.destroy()
            self.nametagColorDialog = None
        if self.nametagStyleDialog:
            self.nametagStyleDialog.destroy()
            self.nametagStyleDialog = None
            
    def initToonState(self):
        self.setAnimState('neutral', 0.9, None, None)
        if self.name in NPCToons.NametagColorPositions:
            pos = NPCToons.NametagColorPositions[self.name]
            self.setPos(*pos[0])
            self.setH(pos[1])

    def getCollSphereRadius(self):
        return 1.25

    def handleCollisionSphereEnter(self, collEntry):
        if self.lastCollision > time.time():
            return

        self.lastCollision = time.time() + ToontownGlobals.NPCCollisionDelay

        base.cr.playGame.getPlace().fsm.request('stopped')
        base.setCellsAvailable(base.bottomCells, 0)
        self.setChatAbsolute(TTLocalizer.NametagColorPickMessage, CFSpeech|CFTimeout)
        self.acceptOnce('nametagColorShopDone', self.__nametagColorShopDone)
        self.acceptOnce('nametagStyleShopDone', self.__nametagStyleShopDone)
        self.accept('nametagShopBack', self.__showInitialScreen)
        self.setupInitialButtons()
       
    def setupInitialButtons(self):
        gui = loader.loadModel('phase_3/models/gui/tt_m_gui_mat_mainGui')
        buttonImage = (gui.find('**/tt_t_gui_mat_shuffleUp'), gui.find('**/tt_t_gui_mat_shuffleDown'))
        self.title = DirectLabel(aspect2d, relief=None, text=TTLocalizer.NametagBuyMessage,
                     text_fg=(0, 1, 0, 1), text_scale=0.15, text_font=ToontownGlobals.getSignFont(),
                     pos=(0, 0, 0.2), text_shadow=(1, 1, 1, 1))
        self.nametagColorButton = DirectButton(aspect2d, relief=None, image=buttonImage, text=TTLocalizer.NametagColorButton,
                         text_font=ToontownGlobals.getInterfaceFont(), text_scale=0.11, text_pos=(0, -0.02),
                         pos=(0, 0, 0), text_fg=(1, 1, 1, 1), text_shadow=(0, 0, 0, 1), command=self.__createNametagColorDialog)       
        self.nametagStyleButton = DirectButton(aspect2d, relief=None, image=buttonImage, text=TTLocalizer.NametagStyleButton,
                         text_font=ToontownGlobals.getInterfaceFont(), text_scale=0.11, text_pos=(0, -0.02),
                         pos=(0, 0, -0.2), text_fg=(1, 1, 1, 1), text_shadow=(0, 0, 0, 1), command=self.__createNametagStyleDialog)       
        self.cancelButton = DirectButton(aspect2d, relief=None, image=buttonImage, text=TTLocalizer.lCancel,
                            clickSound=loader.loadSfx('phase_3/audio/sfx/GUI_create_toon_back.ogg'),
                            text_font=ToontownGlobals.getInterfaceFont(), text_scale=0.11, text_pos=(0, -0.02),
                            pos=(0, 0, -0.4), text_fg=(1, 1, 1, 1), text_shadow=(0, 0, 0, 1), command=self.__exit, extraArgs=[NametagNPCGlobals.USER_CANCEL])
        gui.removeNode()
        
    def __showInitialScreen(self):
        for x in (self.title, self.nametagColorButton, self.nametagStyleButton, self.cancelButton):
            if x:
                x.show()            
        
    def destroy(self):
        for x in (self.title, self.nametagColorButton, self.nametagStyleButton, self.cancelButton):
            if x:
                x.destroy()
                x = None
        
    def __createNametagColorDialog(self):
        for x in (self.title, self.nametagColorButton, self.nametagStyleButton, self.cancelButton):
            if x:
                x.hide()
        self.nametagColorDialog = NametagColorShopGui.NametagColorShopGui()
        
    def __createNametagStyleDialog(self):
        for x in (self.title, self.nametagColorButton, self.nametagStyleButton, self.cancelButton):
            if x:
                x.hide()
        self.nametagStyleDialog = NametagStyleShopGui.NametagStyleShopGui()

    def freeAvatar(self):
        base.cr.playGame.getPlace().fsm.request('walk')
        base.setCellsAvailable(base.bottomCells, 1)
      
    def __exit(self, state):
        self.destroy()
        self.freeAvatar()
        if state == NametagNPCGlobals.USER_CANCEL:
            self.setChatAbsolute(TTLocalizer.STOREOWNER_GOODBYE, CFSpeech|CFTimeout)

    def __nametagColorShopDone(self, state, nametagColor):
        self.destroy()
        self.freeAvatar()

        if state == NametagNPCGlobals.USER_CANCEL:
            self.setChatAbsolute(TTLocalizer.STOREOWNER_GOODBYE, CFSpeech|CFTimeout)
            return
        elif state == NametagNPCGlobals.CHANGE:
            self.sendUpdate('changeNametagColor', [nametagColor])
            
    def __nametagStyleShopDone(self, state, nametagStyle):
        self.destroy()
        self.freeAvatar()
        if state == NametagNPCGlobals.USER_CANCEL:
            self.setChatAbsolute(TTLocalizer.STOREOWNER_GOODBYE, CFSpeech|CFTimeout)
            return
        elif state == NametagNPCGlobals.CHANGE:
            self.sendUpdate('changeNametagStyle', [nametagStyle])

    def changeNametagColorResult(self, avId, state):
        if state in NametagNPCGlobals.ChangeMessagesColor:
            self.setChatAbsolute(NametagNPCGlobals.ChangeMessagesColor[state], CFSpeech|CFTimeout)
        if state == NametagNPCGlobals.CHANGE_SUCCESSFUL:
            av = self.cr.doId2do.get(avId)
            if av:
                av.getDustCloud().start()

    def changeNametagStyleResult(self, avId, state):
        if state in NametagNPCGlobals.ChangeMessagesColor:
            self.setChatAbsolute(NametagNPCGlobals.ChangeMessagesStyle[state], CFSpeech|CFTimeout)
        if state == NametagNPCGlobals.CHANGE_SUCCESSFUL:
            av = self.cr.doId2do.get(avId)
            if av:
                av.getDustCloud().start()