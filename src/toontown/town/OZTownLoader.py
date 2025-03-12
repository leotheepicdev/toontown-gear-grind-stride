from toontown.suit import Suit
from toontown.town import OZStreet
from toontown.town import TownLoader

class OZTownLoader(TownLoader.TownLoader):
    def __init__(self, hood, parentFSM, doneEvent):
        TownLoader.TownLoader.__init__(self, hood, parentFSM, doneEvent)
        self.streetClass = OZStreet.OZStreet
        self.musicFile = 'phase_9/audio/bgm/sellbot_hq_courtyard.ogg'
        self.activityMusicFile = 'phase_6/audio/bgm/OZ_SZ.ogg'
        self.townStorageDNAFile = 'phase_6/dna/storage_OZ_town.pdna'
		
    def load(self, zoneId):
        TownLoader.TownLoader.load(self, zoneId)
        #Suit.loadSuits(2)
        dnaFile = 'phase_6/dna/outdoor_zone_' + str(self.canonicalBranchZone) + '.pdna'
        self.createHood(dnaFile)
		
    def unload(self):
        TownLoader.TownLoader.unload(self)
        #Suit.unloadSuits(2)