from direct.directnotify.DirectNotifyGlobal import directNotify
from direct.distributed.DistributedObjectAI import DistributedObjectAI
from toontown.base import ToontownGlobals
from toontown.toon import DistributedToonAI

class ToontownDistrictStatsAI(DistributedObjectAI):
    notify = directNotify.newCategory('ToontownDistrictStatsAI')
    districtId = 0
    groupAvCount = [0] * len(ToontownGlobals.GROUP_ZONES)

    def announceGenerate(self):
        DistributedObjectAI.announceGenerate(self)
        taskMgr.doMethodLater(15, self.__countGroups, self.uniqueName('countGroups'))
    
    def delete(self):
        taskMgr.remove(self.uniqueName('countGroups'))
        DistributedObjectAI.delete(self)

    def setDistrictId(self, districtId):
        self.districtId = districtId

    def d_setDistrictId(self, districtId):
        self.sendUpdate('setDistrictId', [districtId])

    def b_setDistrictId(self, districtId):
        self.setDistrictId(districtId)
        self.d_setDistrictId(districtId)

    def getDistrictId(self):
        return self.districtId
    
    def setGroupAvCount(self, groupAvCount):
        self.groupAvCount = groupAvCount

    def d_setGroupAvCount(self, groupAvCount):
        self.sendUpdate('setGroupAvCount', [groupAvCount])

    def b_setGroupAvCount(self, groupAvCount):
        self.setGroupAvCount(groupAvCount)
        self.d_setGroupAvCount(groupAvCount)

    def getGroupAvCount(self):
        return self.groupAvCount
    
    def __countGroups(self, task):
        zones = ToontownGlobals.GROUP_ZONES
        self.groupAvCount = [0] * len(zones)
        
        for av in self.air.doId2do.values():
            if isinstance(av, DistributedToonAI.DistributedToonAI) and av.isPlayerControlled() and av.zoneId in zones:
                self.groupAvCount[zones.index(av.zoneId)] += 1

        taskMgr.doMethodLater(15, self.__countGroups, self.uniqueName('countGroups'))
        self.b_setGroupAvCount(self.groupAvCount)