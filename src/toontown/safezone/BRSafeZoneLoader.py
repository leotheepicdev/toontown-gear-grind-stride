from toontown.safezone import BRPlayground
from toontown.safezone import SafeZoneLoader
import SZUtil

class BRSafeZoneLoader(SafeZoneLoader.SafeZoneLoader):
    def __init__(self, hood, parentFSM, doneEvent):
        SafeZoneLoader.SafeZoneLoader.__init__(self, hood, parentFSM, doneEvent)
        self.playgroundClass = BRPlayground.BRPlayground
        self.musicFile = 'phase_8/audio/bgm/TB_nbrhood.ogg'
        self.activityMusicFile = 'phase_8/audio/bgm/TB_SZ_activity.ogg'
        self.dnaFile = 'phase_8/dna/the_burrrgh_sz.pdna'
        self.safeZoneStorageDNAFile = 'phase_8/dna/storage_BR_sz.pdna'

    def load(self):
        SafeZoneLoader.SafeZoneLoader.load(self)
        self.windSound = map(loader.loadSfx, ['phase_8/audio/sfx/SZ_TB_wind_1.ogg',
                                            'phase_8/audio/sfx/SZ_TB_wind_2.ogg',
                                            'phase_8/audio/sfx/SZ_TB_wind_3.ogg'])
        self.snow, self.snowRender = SZUtil.createSnow(self.geom)

    def unload(self):
        SafeZoneLoader.SafeZoneLoader.unload(self)
        del self.windSound
        del self.snow
        del self.snowRender

    def enter(self, requestStatus):
        SafeZoneLoader.SafeZoneLoader.enter(self, requestStatus)
        self.snow.start(camera, self.snowRender)

    def exit(self):
        SafeZoneLoader.SafeZoneLoader.exit(self)
        self.snow.cleanup()
        self.snowRender.removeNode()
