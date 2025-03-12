from direct.directnotify.DirectNotifyGlobal import directNotify
from direct.distributed.DistributedObjectAI import DistributedObjectAI
from toontown.distributed import DistrictGlobals

class ToontownDistrictAI(DistributedObjectAI):
    notify = directNotify.newCategory('ToontownDistrictAI')

    def __init__(self, air):
        DistributedObjectAI.__init__(self, air)
        self.name = 'NotGiven'
        self.difficulty = DistrictGlobals.DIFFICULTY_NORMAL
        self.available = 0
        self.population = 0
        self.invasionStatus = 0

    def setName(self, name):
        self.name = name

    def d_setName(self, name):
        self.sendUpdate('setName', [name])

    def b_setName(self, name):
        self.setName(name)
        self.d_setName(name)

    def getName(self):
        return self.name

    def setDifficulty(self, difficulty):
        self.difficulty = difficulty

    def d_setDifficulty(self, difficulty):
        self.sendUpdate('setDifficulty', [difficulty])

    def b_setDifficulty(self, difficulty):
        self.setDifficulty(difficulty)
        self.d_setDifficulty(difficulty)

    def getDifficulty(self):
        return self.difficulty        
        
    def setAvailable(self, available):
        self.available = available

    def d_setAvailable(self, available):
        self.sendUpdate('setAvailable', [available])

    def b_setAvailable(self, available):
        self.setAvailable(available)
        self.d_setAvailable(available)

    def getAvailable(self):
        return self.available

    def setPopulation(self, population):
        self.population = population

    def d_setPopulation(self, population):
        self.sendUpdate('setPopulation', [population])

    def b_setPopulation(self, population):
        self.setPopulation(population)
        self.d_setPopulation(population)

    def getPopulation(self):
        return self.population

    def setInvasionStatus(self, invasionStatus):
        self.invasionStatus = invasionStatus

    def d_setInvasionStatus(self, invasionStatus):
        self.sendUpdate('setInvasionStatus', [invasionStatus])

    def b_setInvasionStatus(self, invasionStatus):
        self.setInvasionStatus(invasionStatus)
        self.d_setInvasionStatus(invasionStatus)

    def getInvasionStatus(self):
        return self.invasionStatus
		   