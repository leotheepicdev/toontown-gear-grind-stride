from panda3d.core import NodePath
from direct.interval.IntervalGlobal import *
from DistributedTreasure import DistributedTreasure
import TreasureGlobals

class DistributedBeanBagTreasure(DistributedTreasure):

    def __init__(self, cr):
        DistributedTreasure.__init__(self, cr)
        self.model = None
        self.value = 0

    def setValue(self, value):
        self.value = value

    def loadModel(self):
        modelPath, grabSoundPath = TreasureGlobals.TreasureModels[self.treasureType]
        self.grabSound = loader.loadSfx(grabSoundPath)
        self.rejectSound = loader.loadSfx(self.rejectSoundPath)
        if not self.nodePath:
            self.makeNodePath()
        else:
            self.treasure.getChildren().detach()
        if self.model:
            self.model.removeNode()
        self.model = loader.loadModel(modelPath)
        self.model.instanceTo(self.treasure)
        self.model.setScale(0.15 * min(2 + self.value / 50.0, 4.5))
        self.model.setColorScale(*TreasureGlobals.BeanBagValueColors[self.value])
        self.model.setZ(1)

    def startAnimation(self):
        x, y, z = self.treasure.getPos()
        Parallel(Sequence(self.treasure.posInterval(2.0, (x, y, z + 1), startPos=(x, y, z), blendType='easeInOut'), self.treasure.posInterval(2.0, (x, y, z), startPos=(x, y, z + 1), blendType='easeInOut')), self.treasure.hprInterval(4.0, (360, 0, 0))).loop()

    def preGrab(self, av):
        av.showHpText(self.value, bonus=2)