from direct.directnotify.DirectNotifyGlobal import directNotify
from direct.distributed.DistributedObject import DistributedObject
from toontown.base import ToontownGlobals
from toontown.hood import ZoneUtil
from toontown.distributed import DistrictGlobals

class ToontownDistrict(DistributedObject):
    notify = directNotify.newCategory('ToontownDistrict')
    neverDisable = 1

    def __init__(self, cr):
        DistributedObject.__init__(self, cr)
        self.name = 'NotGiven'
        self.difficulty = 0
        self.available = 0
        self.population = 0
        self.invasionStatus = 0
        self.suitStatus = ''
        self.groupAvCount = []

    def announceGenerate(self):
        DistributedObject.announceGenerate(self)
        self.cr.activeDistrictMap[self.doId] = self
        messenger.send('shardInfoUpdated')

    def delete(self):
        if base.cr.distributedDistrict is self:
            base.cr.distributedDistrict = None
        if self.doId in self.cr.activeDistrictMap:
            del self.cr.activeDistrictMap[self.doId]
        DistributedObject.delete(self)
        messenger.send('shardInfoUpdated')

    def setAvailable(self, available):
        self.available = available
        messenger.send('shardInfoUpdated')

    def setName(self, name):
        self.name = name
        messenger.send('shardInfoUpdated')
        
    def setDifficulty(self, difficulty):
        self.difficulty = difficulty
        messenger.send('shardInfoUpdated')
        
    def getDifficulty(self):
        return self.difficulty

    def setPopulation(self, population):
        self.population = population
        messenger.send('shardInfoUpdated')

    def setInvasionStatus(self, invasionStatus):
        self.invasionStatus = invasionStatus
        messenger.send('shardInfoUpdated')
		
