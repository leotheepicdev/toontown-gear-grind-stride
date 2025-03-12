from toontown.town import WWStreet
from toontown.town import TownLoader

class WWTownLoader(TownLoader.TownLoader):
    def __init__(self, hood, parentFSM, doneEvent):
        TownLoader.TownLoader.__init__(self, hood, parentFSM, doneEvent)
        self.streetClass = WWStreet.WWStreet
        self.musicFile = 'phase_3.5/audio/bgm/TC_SZ.ogg' # TODO
        self.activityMusicFile = 'phase_3.5/audio/bgm/TC_SZ_activity.ogg' # TODO
        self.townStorageDNAFile = 'phase_14/dna/storage_WW_town.pdna'

    def load(self, zoneId):
        TownLoader.TownLoader.load(self, zoneId)
        dnaFile = 'phase_14/dna/wacky_west_' + str(self.canonicalBranchZone) + '.pdna'
        self.createHood(dnaFile)

    def unload(self):
        TownLoader.TownLoader.unload(self)
