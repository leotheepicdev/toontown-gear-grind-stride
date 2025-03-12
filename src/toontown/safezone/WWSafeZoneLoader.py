from toontown.safezone import SafeZoneLoader
from toontown.safezone import WWPlayground

class WWSafeZoneLoader(SafeZoneLoader.SafeZoneLoader):
    def __init__(self, hood, parentFSM, doneEvent):
        SafeZoneLoader.SafeZoneLoader.__init__(self, hood, parentFSM, doneEvent)
        self.playgroundClass = WWPlayground.WWPlayground
        self.musicFile = 'phase_4/audio/bgm/TC_nbrhood.ogg' # TODO
        self.activityMusicFile = 'phase_3.5/audio/bgm/TC_SZ_activity.ogg' # TODO
        self.dnaFile = 'phase_14/dna/wacky_west_sz.pdna'
        self.safeZoneStorageDNAFile = 'phase_14/dna/storage_WW_sz.pdna'

    def load(self):
        SafeZoneLoader.SafeZoneLoader.load(self)
     
    def unload(self):
        SafeZoneLoader.SafeZoneLoader.unload(self)
