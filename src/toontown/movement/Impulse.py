from panda3d.core import *
from direct.showbase import DirectObject

class Impulse(DirectObject.DirectObject):

    def __init__(self):
        self.mover = None
        self.nodePath = None

    def destroy(self):
        self.mover = None
        self.nodePath = None

    def _process(self, dt):
        pass

    def _setMover(self, mover):
        if self.mover != mover:
            self.mover = mover
            self.nodePath = self.mover.getNodePath()
        
    def getNodePath(self):
        return self.nodePath

    def _clearMover(self, mover):
        if self.mover == mover:
            self.mover = None
            self.nodePath = None

