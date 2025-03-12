from direct.fsm import StateData
from direct.gui.DirectGui import *
from toontown.base import TTLocalizer
from toontown.base.ToontownBattleGlobals import *
from MakeAToonGlobals import *

class TrackShop(StateData.StateData):
    FIRST_TRACK_BTN_POS = [(-0.6, 0, 0.25), (-0.4, 0, 0.25), (-0.2, 0, 0.25), (0, 0, 0.25), (0.2, 0, 0.25), (0.4, 0, 0.25), (0.6, 0, 0.25)]
    SECOND_TRACK_BTN_POS = [(-0.6, 0, -0.35), (-0.4, 0, -0.35), (-0.2, 0, -0.35), (0, 0, -0.35), (0.2, 0, -0.35), (0.4, 0, -0.35), (0.6, 0, -0.35)]

    def __init__(self, doneEvent):
        StateData.StateData.__init__(self, doneEvent)
        self.toon = None
        self.firstTrackButtons = []
        self.secondTrackButtons = []
        self.firstTrack = 4
        self.secondTrack = 5
        
    def enter(self, toon, shopsVisited=[]):
        base.disableMouse()
        self.toon = toon
        self.dna = toon.getStyle()
        self.acceptOnce('last', self.__handleBackward)
        self.acceptOnce('next', self.__handleForward)
		
    def showButtons(self):
        self.parentFrame.show()
		
    def hideButtons(self):
        self.parentFrame.hide()
		
    def exit(self):
        self.ignore('last')
        self.ignore('next')
        self.ignore('enter')
        try:
            del self.toon
        except:
            print 'TrackShop: toon not found'

        self.hideButtons()
		
    def load(self):
        self.parentFrame = self.getNewFrame()
        self.parentFrame.hide()
        invIcons = loader.loadModel('phase_3.5/models/gui/inventory_icons')
        self.firstTrackLabel = DirectLabel(parent=self.parentFrame, relief=None, text=TTLocalizer.TrackShopFirstTrack, text_scale=0.06, pos=(0, 0, 0.35)) 
        self.secondTrackLabel = DirectLabel(parent=self.parentFrame, relief=None, text=TTLocalizer.TrackShopSecondTrack, text_scale=0.06, pos=(0, 0, -0.25)) 
        for x in xrange(0, 7):
            image = invIcons.find('**/' + AvPropsNew[x][0])
            # TODO: Change the current selection sfx. Couldn't find any fitting ones
            track1Btn = DirectButton(parent=self.parentFrame, clickSound=loader.loadSfx('phase_6/audio/sfx/KART_getGag.ogg'), relief=None, image=image, image_color=(1, 1, 1, 0.5), pos=self.FIRST_TRACK_BTN_POS[x], scale=1.3, command=self.chooseTrackOne, extraArgs=[x])
            track2Btn = DirectButton(parent=self.parentFrame, clickSound=loader.loadSfx('phase_6/audio/sfx/KART_getGag.ogg'), relief=None, image=image, image_color=(1, 1, 1, 0.5), pos=self.SECOND_TRACK_BTN_POS[x], scale=1.3, command=self.chooseTrackTwo, extraArgs=[x])
            self.firstTrackButtons.append(track1Btn)
            self.secondTrackButtons.append(track2Btn)
            if x == self.firstTrack:
                self.chooseTrackOne(x)
            if x == self.secondTrack:
                self.chooseTrackTwo(x)

    def unload(self):
        if self.parentFrame:
            self.parentFrame.destroy()
            del self.parentFrame
        self.firstTrackLabel.destroy()
        del self.firstTrackLabel
        for x in self.firstTrackButtons:
            x.destroy()
            del x
        self.secondTrackLabel.destroy()
        del self.secondTrackLabel
        for x in self.secondTrackButtons:
            x.destroy()
            del x
		
    def chooseTrackOne(self, track):
        if self.firstTrackButtons[self.firstTrack]['state'] == DGG.DISABLED:
            self.firstTrackButtons[self.firstTrack]['state'] = DGG.NORMAL
            self.secondTrackButtons[self.firstTrack]['state'] = DGG.NORMAL
            self.firstTrackButtons[self.firstTrack]['image_color'] = (1, 1, 1, 0.5)
            self.secondTrackButtons[self.firstTrack]['image_color'] = (1, 1, 1, 0.5)
        self.firstTrack = track
        if self.toon:
            self.toon.track1Type = track
        self.firstTrackButtons[track]['state'] = DGG.DISABLED
        self.firstTrackButtons[track]['image_color'] = (1, 1, 1, 1)
        self.secondTrackButtons[track]['state'] = DGG.DISABLED
        self.secondTrackButtons[track]['image_color'] = (1, 0.5, 0.5, 0.3)
		
    def chooseTrackTwo(self, track):
        if self.secondTrackButtons[self.secondTrack]['state'] == DGG.DISABLED:
            self.firstTrackButtons[self.secondTrack]['state'] = DGG.NORMAL
            self.secondTrackButtons[self.secondTrack]['state'] = DGG.NORMAL
            self.firstTrackButtons[self.secondTrack]['image_color'] = (1, 1, 1, 0.5)
            self.secondTrackButtons[self.secondTrack]['image_color'] = (1, 1, 1, 0.5)
        self.secondTrack = track
        if self.toon:
            self.toon.track2Type = track
        self.firstTrackButtons[track]['state'] = DGG.DISABLED
        self.firstTrackButtons[track]['image_color'] = (1, 0.5, 0.5, 0.3)
        self.secondTrackButtons[track]['state'] = DGG.DISABLED
        self.secondTrackButtons[track]['image_color'] = (1, 1, 1, 1)
		
    def __handleForward(self):
        self.doneStatus = 'next'
        messenger.send(self.doneEvent)

    def __handleBackward(self):
        self.doneStatus = 'last'
        messenger.send(self.doneEvent)
		
    def getNewFrame(self):
        frame = DirectFrame(relief=None, image=DGG.getDefaultDialogGeom(), image_scale=(1.8, 1.5, 1), pos=(-1.16, 0, -0.9), frameColor=(1, 1, 1, 1))
        frame.reparentTo(base.a2dTopRight)
        return frame