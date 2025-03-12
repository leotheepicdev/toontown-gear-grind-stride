from direct.showbase.DirectObject import DirectObject
from direct.interval.IntervalGlobal import Sequence, LerpScaleInterval, LerpColorScaleInterval
from direct.gui.DirectLabel import *
from direct.gui.OnscreenImage import *
from direct.gui.DirectButton import *
from panda3d.core import TextNode, VBase3, TransparencyAttrib, Vec3, Vec4
import TTLocalizer, ToontownGlobals, random

class ToontownTitleScreen(DirectObject):

    def __init__(self):
        DirectObject.__init__(self)
        self.clickBackground = OnscreenImage(parent=render2d, pos=(0, 0, 0), scale=(render2d, VBase3(1)), image='phase_3/maps/loading_bg_town.jpg')
        self.clickBackground.setBin('fixed', 10)
        self.logo = OnscreenImage(parent=base.a2dTopCenter,
        image='phase_3/maps/toontown-logo.png',
        scale=(0.9, 1, 0.6),
        pos=(0, 0, -0.6))
        self.logo.setTransparency(TransparencyAttrib.MAlpha)
        self.logo.setBin('fixed', 20)
        self.version = DirectLabel(parent=base.a2dBottomLeft, relief=None, text=base.cr.getServerVersion(), text_align=TextNode.ALeft, scale=(0.06, 1, 0.06), pos=(0.03, 0, 0.03), text_fg=(1, 1, 1, 1), text_shadow=(0, 0, 0, 1))
        self.bottomLabel = DirectLabel(parent=base.a2dBottomCenter, relief=None, text=TTLocalizer.ToontownTitleScreenClickToStart, scale=(0.14, 1, 0.14), pos=(0, 0, 0.3), text_font=ToontownGlobals.getSignFont(), text_fg=(1, 1, 1, 1), text_shadow=(0, 0, 0, 1))
        self.bottomLabelSeq = Sequence(LerpColorScaleInterval(self.bottomLabel, 1, Vec4(1, 1, 1, 0), startColorScale=Vec4(1, 1, 1, 1), blendType='easeIn'), 
                                        LerpColorScaleInterval(self.bottomLabel, 1, Vec4(1, 1, 1, 1), startColorScale=Vec4(1, 1, 1, 0), blendType='easeIn'))
        self.bottomLabelSeq.loop()
        self.randomText = DirectLabel(parent=base.a2dBottomCenter, relief=None, text=random.choice(TTLocalizer.ToontownTitleScreenRandomText), scale=(0.08, 1, 0.08), pos=(0, 0, 0.2), text_font=ToontownGlobals.getSignFont(), text_fg=(1, 1, 0, 1), text_shadow=(0, 0, 0, 1), text_wordwrap=30.5)
        gui = loader.loadModel('phase_3/models/gui/pick_a_toon_gui')
        quitHover = gui.find('**/QuitBtn_RLVR')
        self.quitButton = DirectButton(parent=base.a2dBottomRight, image=(quitHover, quitHover, quitHover), relief=None, text=TTLocalizer.AvatarChooserQuit, text_font=ToontownGlobals.getSignFont(), text_fg=(0.977, 0.816, 0.133, 1), text_pos=TTLocalizer.ACquitButtonPos, text_scale=TTLocalizer.ACquitButton, image_scale=1, image1_scale=1.05, image2_scale=1.05, scale=1.05, pos=(-0.25, 0, 0.075), command=self.__handleQuit)
        gui.removeNode()
        self.logoScaleTrack = Sequence(LerpScaleInterval(self.logo, 3, Vec3(1, 1, 0.7), Vec3(0.9, 1, 0.6), blendType='easeInOut'), LerpScaleInterval(self.logo, 3, Vec3(0.9, 1, 0.6), Vec3(1, 1, 0.7), blendType='easeInOut')).loop()
        base.cr.music = loader.loadMusic('phase_3/audio/bgm/tt_theme.ogg')
        if base.cr.music:
            base.cr.music.setLoop(1)
            base.cr.music.play()
        self.accept('mouse1', self.__handleMouseClick)
        
    def __handleQuit(self):
        base.exitFunc()

    def __handleMouseClick(self):
        self.ignore('mouse1')
        if self.bottomLabelSeq is not None:
            self.bottomLabelSeq.finish()
            self.bottomLabelSeq = None
        base.startShow(base.cr)
        
    def setLabelText(self, text):
        self.bottomLabel['text'] = text
        
    def destroy(self):
        if self.logoScaleTrack is not None:
            self.logoScaleTrack.finish()
            del self.logoScaleTrack
        if self.bottomLabelSeq is not None:
            self.bottomLabelSeq.finish()
            del self.bottomLabelSeq
        for x in (self.clickBackground, self.logo, self.version, self.bottomLabel, self.randomText, self.quitButton):
            if x is not None:
                x.destroy()
                del x