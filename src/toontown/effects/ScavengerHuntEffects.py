from panda3d.core import NodePath, VBase3, VBase4
from direct.interval.IntervalGlobal import *
from direct.gui.DirectFrame import DirectFrame
from direct.gui.DirectLabel import DirectLabel
from toontown.base import ToontownGlobals, TTLocalizer

class ScavengerHuntEffect:
    images = None

    def __init__(self, beanAmount):
        if not ScavengerHuntEffect.images:
            ScavengerHuntEffect.images = loader.loadModel('phase_4/models/props/tot_jar')

        self.npRoot = DirectFrame(parent=aspect2d, relief=None, scale=0.75, pos=(0, 0, 0.6))

        if beanAmount > 0:
            self.npRoot.setColorScale(VBase4(1, 1, 1, 0))
            self.jar = DirectFrame(parent=self.npRoot, relief=None, image=ScavengerHuntEffect.images.find('**/tot_jar'))
            self.jar.hide()
            self.eventImage = NodePath('EventImage')
            self.eventImage.reparentTo(self.npRoot)
            self.countLabel = DirectLabel(parent=self.jar, relief=None, text='+0', text_pos=(0.02, -0.2), text_scale=0.25, text_fg=(0.95, 0.0, 0, 1), text_font=ToontownGlobals.getSignFont())

            def countUp(t, startVal, endVal):
                beanCountStr = startVal + t * (endVal - startVal)
                self.countLabel['text'] = '+' + `(int(beanCountStr))`

            def setCountColor(color):
                self.countLabel['text_fg'] = color

            self.track = Sequence(LerpColorScaleInterval(self.npRoot, 1, colorScale=VBase4(1, 1, 1, 1), startColorScale=VBase4(1, 1, 1, 0)), Wait(1), Func(self.jar.show), LerpColorScaleInterval(self.eventImage, 1, colorScale=VBase4(1, 1, 1, 0), startColorScale=VBase4(1, 1, 1, 1)), Parallel(LerpScaleInterval(self.npRoot, 1, scale=0.5, startScale=0.75), LerpPosInterval(self.npRoot, 1, pos=VBase3(-0.9, 0, -0.83))), LerpFunc(countUp, duration=2, extraArgs=[0, beanAmount]), Func(setCountColor, VBase4(0.95, 0.95, 0, 1)), Wait(3), Func(self.destroy))
        else:
            self.npRoot.setColorScale(VBase4(1, 1, 1, 0))
            self.attemptFailedMsg()
            self.track = Sequence(LerpColorScaleInterval(self.npRoot, 1, colorScale=VBase4(1, 1, 1, 1), startColorScale=VBase4(1, 1, 1, 0)), Wait(5), LerpColorScaleInterval(self.npRoot, 1, colorScale=VBase4(1, 1, 1, 0), startColorScale=VBase4(1, 1, 1, 1)), Func(self.destroy))

    def play(self):
        if self.npRoot:
            self.track.start()

    def stop(self):
        if self.track != None and self.track.isPlaying():
            self.track.finish()

    def destroy(self):
        self.stop()
        self.track = None

        if hasattr(self, 'eventImage') and self.eventImage:
            self.eventImage.detachNode()
            del self.eventImage
        if hasattr(self, 'countLabel') and self.countLabel:
            self.countLabel.destroy()
            del self.countLabel
        if hasattr(self, 'jar') and self.jar:
            self.jar.destroy()
            del self.jar
        if hasattr(self, 'npRoot') and self.npRoot:
            self.npRoot.destroy()
            del self.npRoot

class TrickOrTreatTargetEffect(ScavengerHuntEffect):

    def __init__(self, beanAmount):
        ScavengerHuntEffect.__init__(self, beanAmount)

        if beanAmount > 0:
            self.pumpkin = DirectFrame(parent=self.eventImage, relief=None, image=ScavengerHuntEffect.images.find('**/tot_pumpkin_tall'))

    def attemptFailedMsg(self):
        pLabel = DirectLabel(parent=self.npRoot, relief=None, pos=(0.0, 0.0, -0.15), text=TTLocalizer.TrickOrTreatMsg, text_fg=(0.95, 0.5, 0.0, 1.0), text_scale=0.12, text_font=ToontownGlobals.getSignFont())

    def destroy(self):
        if hasattr(self, 'pumpkin') and self.pumpkin:
            self.pumpkin.destroy()

        ScavengerHuntEffect.destroy(self)

class WinterCarolingEffect(ScavengerHuntEffect):

    def __init__(self, beanAmount):
        ScavengerHuntEffect.__init__(self, beanAmount)

        if beanAmount > 0:
            sm = loader.loadModel('phase_5.5/models/estate/tt_m_prp_ext_snowman_icon')
            self.snowman = DirectFrame(parent=self.eventImage, relief=None, image=sm, scale=20.0)

    def attemptFailedMsg(self):
        pLabel = DirectLabel(parent=self.npRoot, relief=None, pos=(0.0, 0.0, -0.15), text=TTLocalizer.WinterCarolingMsg, text_fg=(0.9, 0.9, 1.0, 1.0), text_scale=0.12, text_font=ToontownGlobals.getSignFont())

    def destroy(self):
        if hasattr(self, 'snowman') and self.snowman:
            self.snowman.destroy()

        ScavengerHuntEffect.destroy(self)
