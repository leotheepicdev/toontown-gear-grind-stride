from toontown.hood import HoodAI
from toontown.safezone import DistributedTrolleyAI
from toontown.base import ToontownGlobals

class WWHoodAI(HoodAI.HoodAI):
    __slots__ = ('air', 'zoneId', 'canonicalHoodId', 'fishingPonds', 'partyGates', 'treasurePlanner', 'buildingManagers', 'suitPlanners', 'trolley')

    def __init__(self, air):
        HoodAI.HoodAI.__init__(self, air,
                               ToontownGlobals.WackyWest,
                               ToontownGlobals.WackyWest)

        self.trolley = None

        self.startup()

    def startup(self):
        HoodAI.HoodAI.startup(self)

        if simbase.config.GetBool('want-minigames', True):
            self.createTrolley()

    def shutdown(self):
        HoodAI.HoodAI.shutdown(self)

    def createTrolley(self):
        self.trolley = DistributedTrolleyAI.DistributedTrolleyAI(self.air)
        self.trolley.generateWithRequired(self.zoneId)
        self.trolley.start()
