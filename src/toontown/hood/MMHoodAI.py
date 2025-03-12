from toontown.hood import HoodAI
from toontown.safezone import DistributedTrolleyAI
from toontown.safezone import DistributedMMPianoAI
from toontown.base import ToontownGlobals
from toontown.ai import DistributedEffectMgrAI

class MMHoodAI(HoodAI.HoodAI):
    __slots__ = ('air', 'zoneId', 'canonicalHoodId', 'fishingPonds', 'partyGates', 'treasurePlanner', 'buildingManagers', 'suitPlanners', 'trolley', 'piano')
    
    def __init__(self, air):
        HoodAI.HoodAI.__init__(self, air,
                               ToontownGlobals.MinniesMelodyland,
                               ToontownGlobals.MinniesMelodyland)

        self.trolley = None
        self.piano = None

        self.startup()

    def startup(self):
        HoodAI.HoodAI.startup(self)

        if simbase.config.GetBool('want-minigames', True):
            self.createTrolley()

        self.piano = DistributedMMPianoAI.DistributedMMPianoAI(self.air)
        self.piano.generateWithRequired(self.zoneId)

        self.trickOrTreatMgr = DistributedEffectMgrAI.DistributedEffectMgrAI(self.air, ToontownGlobals.HALLOWEEN, 12)
        self.trickOrTreatMgr.generateWithRequired(4835) # Ursatz for Really Kool Katz, Tenor Terrace

        self.winterCarolingMgr = DistributedEffectMgrAI.DistributedEffectMgrAI(self.air, ToontownGlobals.CHRISTMAS, 14)
        self.winterCarolingMgr.generateWithRequired(4614) # Shave and a Haircut for a Song, Alto Avenue

    def createTrolley(self):
        self.trolley = DistributedTrolleyAI.DistributedTrolleyAI(self.air)
        self.trolley.generateWithRequired(self.zoneId)
        self.trolley.start()
