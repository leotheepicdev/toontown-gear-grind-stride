from panda3d.core import Vec4
from direct.gui.DirectGui import *
from toontown.base import ToontownGlobals
from toontown.toon import ToonHead

class VineHeadFrame(DirectFrame):

    def __init__(self, av = None, color = Vec4(1, 1, 1, 1), *args, **kwargs):
        self.panelGeom = DGG.getDefaultDialogGeom()
        opts = {'relief': None,
         'geom': self.panelGeom,
         'geom_scale': (0.5, 1, 0.5),
         'pos': (0, 0, 0)}
        opts.update(kwargs)
        apply(DirectFrame.__init__, (self,) + args, opts)
        self.initialiseoptions(VineHeadFrame)
        if av:
            self.setAv(av)
        self.setScale(0.1)
        self.setTransparency(0)
        return

    def setAv(self, av):
        self.head = self.stateNodePath[0].attachNewNode('head', 20)
        self.head.setPosHprScale(0, -0.5, -0.09, 180.0, 0.0, 0.0, 0.2, 0.2, 0.2)
        self.headModel = ToonHead.ToonHead()
        self.headModel.setupHead(av.style, forGui=1)
        self.headModel.reparentTo(self.head)

    def destroy(self):
        self.headModel.delete()
        del self.headModel
        self.head.removeNode()
        del self.head
        DirectFrame.destroy(self)
