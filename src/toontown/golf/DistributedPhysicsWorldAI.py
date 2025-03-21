import BuildGeometry
from direct.directnotify import DirectNotifyGlobal
from direct.distributed import DistributedObjectAI
from toontown.golf import PhysicsWorldBase
from toontown.base import ToontownGlobals

class DistributedPhysicsWorldAI(DistributedObjectAI.DistributedObjectAI, PhysicsWorldBase.PhysicsWorldBase):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedPhysicsWorldAI')

    def __init__(self, air):
        DistributedObjectAI.DistributedObjectAI.__init__(self, air)
        PhysicsWorldBase.PhysicsWorldBase.__init__(self, 0)
        self.commonHoldData = None
        self.storeAction = None
        self.holdingUpObjectData = 0

    def generate(self):
        DistributedObjectAI.DistributedObjectAI.generate(self)
        self.loadLevel()
        self.setupSimulation()

    def delete(self):
        self.notify.debug('Calling DistributedObjectAI.delete')
        DistributedObjectAI.DistributedObjectAI.delete(self)
        self.notify.debug('Calling PhysicsWorldBase.delete')
        PhysicsWorldBase.PhysicsWorldBase.delete(self)

    def loadLevel(self):
        pass

    def createCommonObject(self, type, pos, hpr, sizeX = 0, sizeY = 0, moveDistance = 0):
        commonObjectDatam = PhysicsWorldBase.PhysicsWorldBase.createCommonObject(self, type, None, pos, hpr, sizeX, sizeY, moveDistance)
        self.sendUpdate('clientCommonObject', commonObjectDatam)

    def updateCommonObjects(self):
        self.sendUpdate('setCommonObjects', [self.getCommonObjectData()])

    def doAction(self):
        self.performReadyAction()
        self.storeAction = None
        self.commonHoldData = None

    def upSetCommonObjects(self, objectData):
        self.holdingUpObjectData = 1
        self.commonHoldData = objectData
        if self.storeAction:
            self.doAction()

    def setupCommonObjects(self):
        self.notify.info(self.commonHoldData)
        if not self.commonHoldData:
            return
        elif self.commonHoldData[0][1] == 99:
            self.notify.info('no common objects')
        else:
            self.useCommonObjectData(self.commonHoldData, 0)

    def performReadyAction(self):
        pass
