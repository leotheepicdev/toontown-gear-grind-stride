from panda3d.core import CollideMask, CollisionNode, CollisionTube, lookAt
from direct.actor.Actor import Actor
from direct.task.Task import Task
from toontown.base import ToontownGlobals
from toontown.base import TTLocalizer
from toontown.parties.DistributedPartyActivity import DistributedPartyActivity
from toontown.parties.PartyGlobals import ActivityIds, ActivityTypes, JUKEBOX_TIMEOUT
from toontown.parties.PartyGlobals import getMusicRepeatTimes, MUSIC_PATH, sanitizePhase
from toontown.parties.JukeboxGui import JukeboxGui

class DistributedPartyJukeboxActivityBase(DistributedPartyActivity):
    notify = directNotify.newCategory('DistributedPartyJukeboxActivityBase')

    def __init__(self, cr, actId, phaseToMusicData):
        DistributedPartyActivity.__init__(self, cr, actId, ActivityTypes.Continuous)
        self.phaseToMusicData = phaseToMusicData
        self.jukebox = None
        self.gui = None
        self.tunes = []
        self.music = None
        self.currentSongData = None
        self.localQueuedSongInfo = None
        self.localQueuedSongListItem = None

    def generateInit(self):
        self.gui = JukeboxGui(self.phaseToMusicData)

    def load(self):
        DistributedPartyActivity.load(self)
        self.jukebox = Actor('phase_13/models/parties/jukebox_model', {'dance': 'phase_13/models/parties/jukebox_dance'})
        self.jukebox.reparentTo(self.root)
        self.jukebox.loop('dance', fromFrame=0, toFrame=48)
        self.collNode = CollisionNode(self.getCollisionName())
        self.collNode.setCollideMask(ToontownGlobals.CameraBitmask | ToontownGlobals.WallBitmask)
        collTube = CollisionTube(0, 0, 0, 0.0, 0.0, 4.25, 2.25)
        collTube.setTangible(1)
        self.collNode.addSolid(collTube)
        self.collNodePath = self.jukebox.attachNewNode(self.collNode)
        self.sign.setPos(-5.0, 0, 0)
        self.activate()

    def unload(self):
        DistributedPartyActivity.unload(self)
        self.gui.unload()
        if self.music is not None:
            self.music.stop()
        self.jukebox.stop()
        self.jukebox.delete()
        self.jukebox = None
        self.ignoreAll()

    def getCollisionName(self):
        return self.uniqueName('jukeboxCollision')

    def activate(self):
        self.accept('enter' + self.getCollisionName(), self.__handleEnterCollision)

    def __handleEnterCollision(self, collisionEntry):
        if base.cr.playGame.getPlace().fsm.getCurrentState().getName() == 'walk':
            base.cr.playGame.getPlace().fsm.request('activity')
            self.d_toonJoinRequest()

    def joinRequestDenied(self, reason):
        DistributedPartyActivity.joinRequestDenied(self, reason)
        self.showMessage(TTLocalizer.PartyJukeboxOccupied)

    def handleToonJoined(self, toonId):
        toon = base.cr.doId2do.get(toonId)
        if toon:
            self.jukebox.lookAt(base.cr.doId2do[toonId])
            self.jukebox.setHpr(self.jukebox.getH() + 180.0, 0, 0)
        if toonId == base.localAvatar.doId:
            self.__localUseJukebox()

    def handleToonExited(self, toonId):
        if toonId == base.localAvatar.doId and self.gui.isLoaded():
            self.__deactivateGui()

    def handleToonDisabled(self, toonId):
        self.notify.warning('handleToonDisabled no implementation yet')

    def __localUseJukebox(self):
        base.localAvatar.disableAvatarControls()
        base.localAvatar.stopPosHprBroadcast()
        self.__activateGui()
        self.accept(JukeboxGui.CLOSE_EVENT, self.__handleGuiClose)
        taskMgr.doMethodLater(0.5, self.__localToonWillExitTask, self.uniqueName('toonWillExitJukeboxOnTimeout'), extraArgs=None)
        self.accept(JukeboxGui.ADD_SONG_CLICK_EVENT, self.__handleQueueSong)
        if self.isUserHost():
            self.accept(JukeboxGui.MOVE_TO_TOP_CLICK_EVENT, self.__handleMoveSongToTop)

    def __localToonWillExitTask(self, task):
        self.localToonExiting()
        return Task.done

    def __activateGui(self):
        self.gui.enable(timer=JUKEBOX_TIMEOUT)
        self.gui.disableAddSongButton()
        if self.currentSongData is not None:
            self.gui.setSongCurrentlyPlaying(self.currentSongData[0], self.currentSongData[1])
        self.d_queuedSongsRequest()

    def __deactivateGui(self):
        self.ignore(JukeboxGui.CLOSE_EVENT)
        self.ignore(JukeboxGui.SONG_SELECT_EVENT)
        self.ignore(JukeboxGui.MOVE_TO_TOP_CLICK_EVENT)
        base.cr.playGame.getPlace().setState('walk')
        base.localAvatar.startPosHprBroadcast()
        base.localAvatar.enableAvatarControls()
        self.gui.unload()
        self.__localClearQueuedSong()

    def isUserHost(self):
        return self.party.partyInfo.hostId == base.localAvatar.doId

    def d_queuedSongsRequest(self):
        self.sendUpdate('queuedSongsRequest')

    def queuedSongsResponse(self, songInfoList, index):
        if self.gui.isLoaded():
            for i in xrange(len(songInfoList)):
                songInfo = songInfoList[i]
                self.__addSongToQueue(songInfo, isLocalQueue=index >= 0 and i == index)

            self.gui.enableAddSongButton()

    def __handleGuiClose(self):
        self.__deactivateGui()
        self.d_toonExitDemand()

    def __handleQueueSong(self, name, values):
        self.d_setNextSong(values[0], values[1])

    def d_setNextSong(self, phase, filename):
        self.sendUpdate('setNextSong', [(phase, filename)])

    def setSongInQueue(self, songInfo):
        if self.gui.isLoaded():
            phase = sanitizePhase(songInfo[0])
            filename = songInfo[1]
            data = self.getMusicData(phase, filename)
            if data:
                if self.localQueuedSongListItem is not None:
                    self.localQueuedSongListItem['text'] = data[0]
                else:
                    self.__addSongToQueue(songInfo, isLocalQueue=True)

    def __addSongToQueue(self, songInfo, isLocalQueue = False):
        isHost = isLocalQueue and self.isUserHost()
        data = self.getMusicData(sanitizePhase(songInfo[0]), songInfo[1])
        if data:
            listItem = self.gui.addSongToQueue(data[0], highlight=isLocalQueue, moveToTopButton=isHost)
            if isLocalQueue:
                self.localQueuedSongInfo = songInfo
                self.localQueuedSongListItem = listItem

    def __localClearQueuedSong(self):
        self.localQueuedSongInfo = None
        self.localQueuedSongListItem = None

    def __play(self, phase, filename, length):
        self.music = loader.loadMusic((MUSIC_PATH + '%s') % (phase, filename))
        if self.music:
            if self.__checkPartyValidity() and hasattr(base.cr.playGame.getPlace().loader, 'music') and base.cr.playGame.getPlace().loader.music:
                base.cr.playGame.getPlace().loader.music.stop()
            self.music.setTime(getMusicRepeatTimes(length))
            self.music.setLoopCount(0)
            self.music.play()
            self.currentSongData = (phase, filename)

    def __stop(self):
        self.currentSongData = None
        if self.music:
            self.music.stop()
        if self.gui.isLoaded():
            self.gui.clearSongCurrentlyPlaying()

    def setSongPlaying(self, songInfo, toonId):
        phase = sanitizePhase(songInfo[0])
        filename = songInfo[1]
        if not filename:
            self.__stop()
            return
        data = self.getMusicData(phase, filename)
        if data:
            self.__play(phase, filename, data[1])
            self.setSignNote(data[0])
            if self.gui.isLoaded():
                item = self.gui.popSongFromQueue()
                self.gui.setSongCurrentlyPlaying(phase, filename)
                if item == self.localQueuedSongListItem:
                    self.__localClearQueuedSong()
        if toonId == localAvatar.doId:
            localAvatar.setSystemMessage(0, TTLocalizer.PartyJukeboxNowPlaying)

    def __handleMoveSongToTop(self):
        if self.isUserHost() and self.localQueuedSongListItem is not None:
            self.d_moveHostSongToTopRequest()

    def d_moveHostSongToTopRequest(self):
        self.notify.debug('d_moveHostSongToTopRequest')
        self.sendUpdate('moveHostSongToTopRequest')

    def moveHostSongToTop(self):
        self.notify.debug('moveHostSongToTop')
        if self.gui.isLoaded():
            self.gui.pushQueuedItemToTop(self.localQueuedSongListItem)

    def getMusicData(self, phase, filename):
        data = []
        phase = sanitizePhase(phase)
        phase = self.phaseToMusicData.get(phase)
        if phase:
            data = phase.get(filename, [])
        return data

    def __checkPartyValidity(self):
        if hasattr(base.cr.playGame, 'getPlace') and base.cr.playGame.getPlace() and hasattr(base.cr.playGame.getPlace(), 'loader') and base.cr.playGame.getPlace().loader:
            return True
        else:
            return False
