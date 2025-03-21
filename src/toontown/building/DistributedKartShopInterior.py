from direct.directnotify import DirectNotifyGlobal
from direct.distributed.DistributedObject import DistributedObject
from toontown.building import ToonInteriorColors
from toontown.hood import ZoneUtil
from toontown.base.ToonBaseGlobal import *
from toontown.base.ToontownGlobals import *
from toontown.toon.DistributedNPCToonBase import DistributedNPCToonBase

class DistributedKartShopInterior(DistributedObject):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedKartShopInterior')

    def __init__(self, cr):
        DistributedObject.__init__(self, cr)
        self.dnaStore = cr.playGame.dnaStore

    def generate(self):
        DistributedObject.generate(self)

    def announceGenerate(self):
        DistributedObject.announceGenerate(self)
        self.__handleInteriorSetup()

    def disable(self):
        self.interior.removeNode()
        del self.interior
        DistributedObject.disable(self)

    def setZoneIdAndBlock(self, zoneId, block):
        self.zoneId = zoneId
        self.block = block

    def __handleInteriorSetup(self):
        self.interior = loader.loadModel('phase_6/models/karting/KartShop_Interior')
        self.interior.reparentTo(render)
        self.interior.flattenMedium()
        for npcToon in self.cr.doFindAllInstances(DistributedNPCToonBase):
            npcToon.initToonState()
