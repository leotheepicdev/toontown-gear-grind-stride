from panda3d.core import Vec4
from toontown.magicword.MagicWordGlobal import *
from toontown.safezone.WWSafeZoneLoader import WWSafeZoneLoader
from toontown.town.WWTownLoader import WWTownLoader
from toontown.base import ToontownGlobals
from toontown.hood.ToonHood import ToonHood

class WWHood(ToonHood):
    notify = directNotify.newCategory('WWHood')

    ID = ToontownGlobals.WackyWest
    TOWNLOADER_CLASS = WWTownLoader
    SAFEZONELOADER_CLASS = WWSafeZoneLoader
    STORAGE_DNA = 'phase_14/dna/storage_WW.pdna'
    SKY_FILE = 'phase_14/models/props/WW_sky'
    SPOOKY_SKY_FILE = 'phase_3.5/models/props/BR_sky'
    TITLE_COLOR = (0.47, 0.36, 0.33, 1.0)

    HOLIDAY_DNA = {
      ToontownGlobals.CHRISTMAS: ['phase_4/dna/winter_storage_TT.pdna', 'phase_4/dna/winter_storage_TT_sz.pdna'],
      ToontownGlobals.HALLOWEEN: ['phase_4/dna/halloween_props_storage_TT.pdna', 'phase_4/dna/halloween_props_storage_TT_sz.pdna']}

@magicWord(category=CATEGORY_CREATIVE)
def spooky():
    """
    Activates the 'spooky' effect on the current area.
    """
    hood = base.cr.playGame.hood
    if not hasattr(hood, 'startSpookySky'):
        return "Couldn't find spooky sky."
    if hasattr(hood, 'magicWordSpookyEffect'):
        return 'The spooky effect is already active!'
    hood.magicWordSpookyEffect = True
    hood.startSpookySky()
    fadeOut = base.cr.playGame.getPlace().loader.geom.colorScaleInterval(
        1.5, Vec4(0.55, 0.55, 0.65, 1), startColorScale=Vec4(1, 1, 1, 1),
        blendType='easeInOut')
    fadeOut.start()
    spookySfx = loader.loadSfx('phase_4/audio/sfx/spooky.ogg')
    spookySfx.play()
    return 'Activating the spooky effect...'
