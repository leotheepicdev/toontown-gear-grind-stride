from panda3d.core import NodePath
import ZoneEntityBase
import BasicEntities

class ZoneEntity(ZoneEntityBase.ZoneEntityBase, BasicEntities.NodePathAttribs):

    def __init__(self, level, entId):
        ZoneEntityBase.ZoneEntityBase.__init__(self, level, entId)
        self.nodePath = self.level.getZoneNode(self.entId)
        if self.nodePath is None:
            self.notify.error('zone %s not found in level model' % self.entId)
        BasicEntities.NodePathAttribs.initNodePathAttribs(self, doReparent=0)
        self.visibleZoneNums = {}
        self.incrementRefCounts(self.visibility)

    def destroy(self):
        BasicEntities.NodePathAttribs.destroy(self)
        ZoneEntityBase.ZoneEntityBase.destroy(self)

    def getNodePath(self):
        return self.nodePath

    def getVisibleZoneNums(self):
        return self.visibleZoneNums.keys()

    def incrementRefCounts(self, zoneNumList):
        for zoneNum in zoneNumList:
            self.visibleZoneNums.setdefault(zoneNum, 0)
            self.visibleZoneNums[zoneNum] += 1

    def decrementRefCounts(self, zoneNumList):
        for zoneNum in zoneNumList:
            self.visibleZoneNums[zoneNum] -= 1
            if self.visibleZoneNums[zoneNum] == 0:
                del self.visibleZoneNums[zoneNum]
