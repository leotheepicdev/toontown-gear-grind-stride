from panda3d.core import NodePath, Vec3
import DistributedLawnDecor
from direct.directnotify import DirectNotifyGlobal
from direct.showbase.ShowBase import *
import GardenGlobals
from toontown.base import TTLocalizer
from toontown.estate import PlantingGUI
from toontown.estate import PlantTreeGUI
from direct.distributed import DistributedNode

class DistributedGardenBox(DistributedLawnDecor.DistributedLawnDecor):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedGardenPlot')
    
    def __init__(self, cr):
        DistributedLawnDecor.DistributedLawnDecor.__init__(self, cr)
        self.plantPath = NodePath('plantPath')
        self.plantPath.reparentTo(self)
        self.plotScale = 1.0
        self.plantingGuiDoneEvent = 'plantingGuiDone'
        self.defaultModel = 'phase_5.5/models/estate/planterC'
    
    def doModelSetup(self):
        if self.typeIndex == GardenGlobals.BOX_THREE:
            self.defaultModel = 'phase_5.5/models/estate/planterA'
        elif self.typeIndex == GardenGlobals.BOX_TWO:
            self.defaultModel = 'phase_5.5/models/estate/planterC'
        else:
            self.defaultModel = 'phase_5.5/models/estate/planterD'
            self.collSphereOffset = 0.0
            self.collSphereRadius = self.collSphereRadius * 1.41
            self.plotScale = Vec3(1.0, 1.0, 1.0)
    
    def setupShadow(self):
        pass
    
    def loadModel(self):
        self.rotateNode = self.plantPath.attachNewNode('rotate')
        self.model = None
        self.model = loader.loadModel(self.defaultModel)
        self.model.setScale(self.plotScale)
        self.model.reparentTo(self.rotateNode)
        self.stick2Ground()
    
    def handleEnterPlot(self, entry = None):
        pass
    
    def handleExitPlot(self, entry = None):
        DistributedLawnDecor.DistributedLawnDecor.handleExitPlot(self, entry)
    
    def setTypeIndex(self, typeIndex):
        self.typeIndex = typeIndex
