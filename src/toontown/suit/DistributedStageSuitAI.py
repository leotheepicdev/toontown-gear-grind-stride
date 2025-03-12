from direct.directnotify import DirectNotifyGlobal
from toontown.suit import DistributedFactorySuitAI


class DistributedStageSuitAI(DistributedFactorySuitAI.DistributedFactorySuitAI):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedStageSuitAI')
	
    def __init__(self, air, suitPlanner):
        DistributedFactorySuitAI.DistributedFactorySuitAI.__init__(self, air, suitPlanner)

    def isForeman(self):
        return 0

    def isSupervisor(self):
        return self.boss
