
from toontown.safezone.CZSafeZoneLoader import CZSafeZoneLoader
from toontown.town.CZTownLoader import CZTownLoader
from toontown.base import ToontownGlobals
from toontown.hood.ToonHood import ToonHood
from panda3d.core import Fog, Vec4

class CZHood(ToonHood):
    notify = directNotify.newCategory('CZHood')

    ID = ToontownGlobals.ConstructionZone
    TOWNLOADER_CLASS = CZTownLoader
    SAFEZONELOADER_CLASS = CZSafeZoneLoader
    STORAGE_DNA = 'phase_14/dna/storage_CZ.pdna'
    SKY_FILE = 'phase_3.5/models/props/TT_sky'
    SPOOKY_SKY_FILE = 'phase_3.5/models/props/BR_sky'
    TITLE_COLOR = (1.0, 0.5, 0.4, 1.0)

    def load(self):
        ToonHood.load(self)

        self.fog = Fog('DDFog')
    

    HOLIDAY_DNA = {
      ToontownGlobals.CHRISTMAS: ['phase_4/dna/winter_storage_TT.pdna', 'phase_4/dna/winter_storage_TT_sz.pdna'],
      ToontownGlobals.HALLOWEEN: ['phase_4/dna/halloween_props_storage_TT.pdna', 'phase_4/dna/halloween_props_storage_TT_sz.pdna']}

    def enter(self, requestStatus):
        ToonHood.enter(self, requestStatus)
        base.camLens.setNearFar(ToontownGlobals.DreamlandCameraNear, ToontownGlobals.DreamlandCameraFar)
		
    def exit(self):
        base.camLens.setNearFar(ToontownGlobals.DefaultCameraNear, ToontownGlobals.DefaultCameraFar)
        ToonHood.exit(self)