from toontown.town import CZStreet
from toontown.town import TownLoader


class CZTownLoader(TownLoader.TownLoader):
    def __init__(self, hood, parentFSM, doneEvent):
        TownLoader.TownLoader.__init__(self, hood, parentFSM, doneEvent)
        self.streetClass = CZStreet.CZStreet
        self.musicFile = 'phase_14/audio/bgm/CZ_SZ.ogg'
        self.activityMusicFile = 'phase_14/audio/bgm/CZ_SZ_activity.ogg'
        self.townStorageDNAFile = 'phase_14/dna/storage_CZ_town.pdna'

    def load(self, zoneId):
        TownLoader.TownLoader.load(self, zoneId)
        dnaFile = 'phase_14/dna/construction_zone_' + str(self.canonicalBranchZone) + '.pdna'
        self.createHood(dnaFile)

    def unload(self):
        TownLoader.TownLoader.unload(self)
      
