from panda3d.core import Vec4
from toontown.base import TTLocalizer, ToontownGlobals
from direct.interval.IntervalGlobal import Sequence, LerpColorScaleInterval
from direct.gui.DirectGui import *
from direct.gui.DirectGuiGlobals import FADE_SORT_INDEX
import LaffMeter

class DeathForceAcknowledge(DirectFrame):

    def __init__(self):
        render.setColorScale(0.4, 0.4, 0.4, 1)
        DirectFrame.__init__(self, parent=aspect2d, relief=None, geom=DGG.getDefaultDialogGeom(), geom_color=ToontownGlobals.GlobalDialogColor, 
                             geom_scale=(1.7, 1, 0.75), pos=(0, 0, 0), suppressKeys=True)
        self.initialiseoptions(DeathForceAcknowledge)
                             
        self.sadMsg = DirectLabel(parent=self, relief=None, text="YOU'VE GONE SAD!", text_font=ToontownGlobals.getSignFont(), text_fg=(1, 1, 0, 1), text_shadow=(0, 0, 0, 1), pos=(-0.2, 0, 0.2), text_scale=0.1)
        self.sadMsgSeq = Sequence(LerpColorScaleInterval(self.sadMsg, 1, Vec4(1, 1, 1, 0), startColorScale=Vec4(1, 1, 1, 1), blendType='easeIn'), 
                                        LerpColorScaleInterval(self.sadMsg, 1, Vec4(1, 1, 1, 1), startColorScale=Vec4(1, 1, 1, 0), blendType='easeIn'))
        self.sadMsgSeq.loop()
        self.gagMsg = DirectLabel(parent=self, relief=None, text=TTLocalizer.DeathAck_1, text_font=ToontownGlobals.getMinnieFont(), text_fg=(0, 0, 0, 1), pos=(-0.2, 0, 0.1), text_scale=0.06)
        self.leaveMsg = DirectLabel(parent=self, relief=None, text=TTLocalizer.DeathAck_2, text_font=ToontownGlobals.getMinnieFont(), text_fg=(1, 0, 0, 1), pos=(0, 0, -0.1), text_scale=0.06)         
        av = base.localAvatar
        self.laffMeter = LaffMeter.LaffMeter(av.style, av.hp, av.maxHp)
        self.laffMeter.reparentTo(self)
        if av.style.getAnimal() == 'monkey':
            self.laffMeter.setPos(0.57, 0, 0.15)
            self.laffMeter.setScale(0.085)
        else:
            self.laffMeter.setPos(0.55, 0, 0.15)
            self.laffMeter.setScale(0.1)
        self.laffMeter.start()
        guiButton = loader.loadModel('phase_3/models/gui/quit_button')
        buttonImage = (guiButton.find('**/QuitBtn_UP'), guiButton.find('**/QuitBtn_DN'), guiButton.find('**/QuitBtn_RLVR'))
        guiButton.removeNode()
        self.continueButton = DirectButton(parent=self, relief=None, image=buttonImage, text=TTLocalizer.DeathAck_3, text_font=ToontownGlobals.getMinnieFont(), text_fg=(1, 1, 1, 1), text_shadow=(0, 0, 0, 1),
                                           pos=(0, 0, -0.25), text_scale=0.05, text_pos=(0, -0.02), command=self.handleClick)
        
    def handleClick(self):
        messenger.send('deathAck')

    def destroy(self):
        render.clearColorScale()
        if self.sadMsgSeq:
            self.sadMsgSeq.finish()
        for x in (self.sadMsg, self.gagMsg, self.leaveMsg, self.continueButton, self.laffMeter):
            x.destroy()
            del x
        DirectFrame.destroy(self)
