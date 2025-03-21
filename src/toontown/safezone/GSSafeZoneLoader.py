from direct.directnotify import DirectNotifyGlobal
from direct.fsm import ClassicFSM, State
from toontown.hood import ZoneUtil
from toontown.safezone.SafeZoneLoader import SafeZoneLoader
from toontown.safezone.GSPlayground import GSPlayground

class GSSafeZoneLoader(SafeZoneLoader):

    def __init__(self, hood, parentFSM, doneEvent):
        SafeZoneLoader.__init__(self, hood, parentFSM, doneEvent)
        self.musicFile = 'phase_6/audio/bgm/GS_SZ.ogg'
        self.activityMusicFile = 'phase_6/audio/bgm/GS_KartShop.ogg'
        self.dnaFile = 'phase_6/dna/goofy_speedway_sz.pdna'
        self.safeZoneStorageDNAFile = 'phase_6/dna/storage_GS_sz.pdna'
        del self.fsm
        self.fsm = ClassicFSM.ClassicFSM('SafeZoneLoader', [State.State('start', self.enterStart, self.exitStart, ['quietZone', 'playground', 'toonInterior']),
         State.State('playground', self.enterPlayground, self.exitPlayground, ['quietZone', 'racetrack']),
         State.State('toonInterior', self.enterToonInterior, self.exitToonInterior, ['quietZone']),
         State.State('quietZone', self.enterQuietZone, self.exitQuietZone, ['playground', 'toonInterior', 'racetrack']),
         State.State('racetrack', self.enterRacetrack, self.exitRacetrack, ['quietZone', 'playground']),
         State.State('final', self.enterFinal, self.exitFinal, ['start'])], 'start', 'final')

    def load(self):
        SafeZoneLoader.load(self)
        self.birdSound = map(loader.loadSfx, ['phase_4/audio/sfx/SZ_TC_bird1.ogg', 'phase_4/audio/sfx/SZ_TC_bird2.ogg', 'phase_4/audio/sfx/SZ_TC_bird3.ogg'])

    def unload(self):
        del self.birdSound
        SafeZoneLoader.unload(self)

    def enterPlayground(self, requestStatus):
        self.playgroundClass = GSPlayground
        SafeZoneLoader.enterPlayground(self, requestStatus)

    def exitPlayground(self):
        taskMgr.remove('titleText')
        self.hood.hideTitleText()
        SafeZoneLoader.exitPlayground(self)
        self.playgroundClass = None

    def handlePlaygroundDone(self):
        status = self.place.doneStatus
        if self.enteringARace(status) and status.get('shardId') == None:
            zoneId = status['zoneId']
            self.fsm.request('quietZone', [status])
        elif ZoneUtil.getBranchZone(status['zoneId']) == self.hood.hoodId and status['shardId'] == None:
            self.fsm.request('quietZone', [status])
        else:
            self.doneStatus = status
            messenger.send(self.doneEvent)

    def enteringARace(self, status):
        if not status['where'] == 'racetrack':
            return 0
        if ZoneUtil.isDynamicZone(status['zoneId']):
            return status['hoodId'] == self.hood.hoodId
        else:
            return ZoneUtil.getHoodId(status['zoneId']) == self.hood.hoodId

    def enterRacetrack(self, requestStatus):
        self.trackId = requestStatus['trackId']
        self.accept('raceOver', self.handleRaceOver)
        self.accept('leavingRace', self.handleLeftRace)
        base.transitions.fadeOut(t=0)

    def exitRacetrack(self):
        del self.trackId

    def handleRaceOver(self):
        print 'you done!!'

    def handleLeftRace(self):
        req = {'loader': 'safeZoneLoader',
         'where': 'playground',
         'how': 'teleportIn',
         'zoneId': 8000,
         'hoodId': 8000,
         'shardId': None}
        self.fsm.request('quietZone', [req])
        return
