from panda3d.core import TextNode
from direct.gui.DirectGui import *
from toontown.base import ToontownGlobals, TTLocalizer

class KeybindDialog(DirectFrame):

    def __init__(self):
        DirectFrame.__init__(self, aspect2d, relief=None, geom=DGG.getDefaultDialogGeom(), geom_color=ToontownGlobals.GlobalDialogColor, geom_scale=(1.37, 1, 1.37), 
                             pos=(0, 0, 0), text=TTLocalizer.KeybindDialogTitle, text_scale=0.09, text_pos=(0, 0.58))
        self.initialiseoptions(KeybindDialog)
        self.doDisables()
        self.updatedKeys = {}
        self.controlLabels = {}
        self.popupDialog = None
        dialogModel = loader.loadModel('phase_3/models/gui/dialog_box_buttons_gui')
        guiButton = loader.loadModel('phase_3/models/gui/quit_button')
        self.cancelButton = DirectButton(parent=self, relief=None, image=(dialogModel.find('**/CloseBtn_UP'), dialogModel.find('**/CloseBtn_DN'), dialogModel.find('**/CloseBtn_Rllvr')), pos=(-0.2, 0, -0.55), text=TTLocalizer.lCancel, text_scale=0.06, text_pos=(0, -0.1), image_scale=1, command=self.destroy)
        self.okButton = DirectButton(parent=self, relief=None, image=(dialogModel.find('**/ChtBx_OKBtn_UP'), dialogModel.find('**/ChtBx_OKBtn_DN'), dialogModel.find('**/ChtBx_OKBtn_Rllvr')), pos=(0.2, 0, -0.55), text=TTLocalizer.lOK, text_scale=0.06, text_pos=(0, -0.1), image_scale=1, command=self.applyChanges)
        for i in xrange(len(ToontownGlobals.KeybindNames)):
            key = ToontownGlobals.KeybindNames[i]
            keyLabel = DirectLabel(parent=self, relief=None, pos=(-0.39, 0, 0.41 + i * -0.1), text=TTLocalizer.OfficialKeybindNames[i], text_scale=0.055, text_align=TextNode.ACenter)
            configButton = DirectButton(parent=self, relief=None, pos=(0, 0, 0.425 + i * -0.1), image=(guiButton.find('**/QuitBtn_UP'), guiButton.find('**/QuitBtn_DN'), guiButton.find('**/QuitBtn_RLVR')), image_scale=(0.9, 0, 0.9), text='Configure', text_scale=0.055, text_pos=(0, -0.01), command=self.configureKey, extraArgs=[key, i])
            self.controlLabels[key] = DirectLabel(parent=self, relief=None, pos=(0.39, 0, 0.41 + i * -0.1), text=base.getKey(key), text_scale=0.055, text_align=TextNode.ACenter)

    def destroy(self):
        self.destroyPopup()
        self.doEnables()
        del self.updatedKeys
        del self.controlLabels
        DirectFrame.destroy(self)

    def destroyPopup(self):
        if self.popupDialog:
           # base.transitions.noTransitions()
            self.popupDialog.cleanup()
            self.popupDialog = None

    def applyChanges(self):
        if not self.updatedKeys:
            self.destroy()
            return
        base.updateKeybinds(self.updatedKeys)
        self.destroy()

    def configureKey(self, key, i):
        self.destroyPopup()
       # base.transitions.fadeScreen(0.7)
        self.popupDialog = DirectDialog(relief=None, suppressMouse=True, suppressKeys=True, image=DGG.getDefaultDialogGeom(), image_color=ToontownGlobals.GlobalDialogColor, image_scale=(2.2, 0, 0.4), pos=(0, 0, 0), text=TTLocalizer.KeybindInstructions % TTLocalizer.OfficialKeybindNames[i], text_pos=(-1, -0.01), text_scale=0.08)
        event = 'registerButton-' + key
        base.buttonThrowers[0].node().setButtonDownEvent(event)
        self.popupDialog.accept(event, self.registerKey, [key])

    def registerKey(self, key, value):
        self.destroyPopup()
        self.updatedKeys[key] = value
        self.controlLabels[key]['text'] = value
		
    def doEnables(self):
        base.localAvatar.enableSleeping()
        base.localAvatar.chatMgr.enableChat()
        base.localAvatar.book.enableShtikerBookKeybinds()
		
    def doDisables(self):
        base.localAvatar.disableSleeping()
        base.localAvatar.chatMgr.disableChat()
        base.localAvatar.book.disableShtikerBookKeybinds()
		