from panda3d.core import Camera, Connection, CullBinManager, DSearchPath, Filename, Lens, MouseWatcher, PGButton, TextProperties, TextPropertiesManager, TrueClock, URLSpec, VBase4, VirtualFile, VirtualFileSystem, WindowProperties, loadPrcFileData
import atexit
from direct.directnotify import DirectNotifyGlobal
from direct.filter.CommonFilters import CommonFilters
from direct.gui import DirectGuiGlobals
from direct.gui.DirectGui import *
from direct.showbase.PythonUtil import *
from direct.showbase.Transitions import Transitions
from direct.task import *
import os
import random
import shutil
from sys import platform
import sys
import tempfile
import time

import ToontownGlobals
import ToontownLoader
from direct.interval.IntervalGlobal import Sequence, Func, Wait
from direct.showbase.ShowBase import ShowBase
from toontown.magicword.MagicWordGlobal import *
from otp.otpbase import OTPGlobals
from lib.nametag.ChatBalloon import ChatBalloon
from lib.nametag import NametagGlobals
from lib.margins.MarginManager import MarginManager
from toontown.chat import WhiteList, WhiteListData, SequenceListData
from toontown.base import TTLocalizer
from toontown.base import ToontownBattleGlobals
from toontown.base import ToontownRender
from toontown.base.TTFrameRateMeter import TTFrameRateMeter
from toontown.gui import TTDialog

tempdir = tempfile.mkdtemp()
vfs = VirtualFileSystem.getGlobalPtr()
searchPath = DSearchPath()
if __debug__:
    searchPath.appendDirectory(Filename('../resources/phase_3/etc'))
searchPath.appendDirectory(Filename('/phase_3/etc'))

for filename in ['toonmono.cur', 'icon.ico']:
    p3filename = Filename(filename)
    found = vfs.resolveFilename(p3filename, searchPath)
    if not found:
        continue
    with open(os.path.join(tempdir, filename), 'wb') as f:
        f.write(vfs.readFile(p3filename, False))
loadPrcFileData('Window: icon', 'icon-filename %s' % Filename.fromOsSpecific(os.path.join(tempdir, 'icon.ico')))

class ToonBase(ShowBase):
    notify = DirectNotifyGlobal.directNotify.newCategory('ToonBase')
    defaultKeybinds = {ToontownGlobals.KeybindNames[0]: 'arrow_up', 
                       ToontownGlobals.KeybindNames[1]: 'arrow_down',
                       ToontownGlobals.KeybindNames[2]: 'arrow_left',
                       ToontownGlobals.KeybindNames[3]: 'arrow_right',
                       ToontownGlobals.KeybindNames[4]: 't',
                       ToontownGlobals.KeybindNames[5]: 'control',
                       ToontownGlobals.KeybindNames[6]: 'delete',
                       ToontownGlobals.KeybindNames[7]: 'f9',
                       ToontownGlobals.KeybindNames[8]: 'alt',
                       ToontownGlobals.KeybindNames[9]: 'shift'}

    def __init__(self, windowType=None):
        ShowBase.__init__(self, windowType=windowType)
        self.disableShowbaseMouse()
        self.addCullBins()
        self.debugRunningMultiplier /= OTPGlobals.ToonSpeedFactor
        self.baseXpMultiplier = self.config.GetFloat('base-xp-multiplier', 1.0)
        self.toonChatSounds = self.config.GetBool('toon-chat-sounds', 1)
        self.placeBeforeObjects = self.config.GetBool('place-before-objects', 1)
        self.endlessQuietZone = False
        self.exitErrorCode = 0
        self.cam.node().setCameraMask(ToontownRender.MainCameraBitmask)
        camera.setPosHpr(0, 0, 0, 0, 0, 0)
        self.camLens.setMinFov(settings['fov']/(4./3.))
        self.camLens.setNearFar(ToontownGlobals.DefaultCameraNear, ToontownGlobals.DefaultCameraFar)
        self.musicManager.setVolume(0.65)
        self.setBackgroundColor(ToontownGlobals.DefaultBackgroundColor)
        tpm = TextPropertiesManager.getGlobalPtr()
        candidateActive = TextProperties()
        candidateActive.setTextColor(0, 0, 1, 1)
        tpm.setProperties('candidate_active', candidateActive)
        candidateInactive = TextProperties()
        candidateInactive.setTextColor(0.3, 0.3, 0.7, 1)
        tpm.setProperties('candidate_inactive', candidateInactive)
        self.transitions.IrisModelName = 'phase_3/models/misc/iris'
        self.transitions.FadeModelName = 'phase_3/models/misc/fade'
        self.exitFunc = self.userExit
        globalClock.setMaxDt(0.2)
        if self.config.GetBool('want-particles', 1) == 1:
            self.notify.debug('Enabling particles')
            self.enableParticles()

        # OS X Specific Actions
        if platform == "darwin":
            self.acceptOnce(ToontownGlobals.QuitGameHotKeyOSX, self.exitOSX)
            self.accept(ToontownGlobals.QuitGameHotKeyRepeatOSX, self.exitOSX)
            self.acceptOnce(ToontownGlobals.HideGameHotKeyOSX, self.hideGame)
            self.accept(ToontownGlobals.HideGameHotKeyRepeatOSX, self.hideGame)
            self.acceptOnce(ToontownGlobals.MinimizeGameHotKeyOSX, self.minimizeGame)
            self.accept(ToontownGlobals.MinimizeGameHotKeyRepeatOSX, self.minimizeGame)

        self.accept('f3', self.toggleGui)
        if __debug__:
            self.accept('f4', self.oobe)
        self.accept('panda3d-render-error', self.panda3dRenderError)
        oldLoader = self.loader
        self.loader = ToontownLoader.ToontownLoader(self)
        __builtins__['loader'] = self.loader
        oldLoader.destroy()
        self.accept('PandaPaused', self.disableAllAudio)
        self.accept('PandaRestarted', self.enableAllAudio)
        self.idTags = self.config.GetBool('want-id-tags', 0)
        if not self.idTags:
            del self.idTags
        self.wantNametags = self.config.GetBool('want-nametags', 1)
        self.wantDynamicShadows = self.config.GetBool('want-dynamic-shadows', 1)
        self.whiteList = None
        if config.GetBool('want-whitelist', True):
            self.whiteList = WhiteList.WhiteList()
            self.whiteList.setWords(WhiteListData.WHITELIST)
            if config.GetBool('want-sequence-list', True):
                self.whiteList.setSequenceList(SequenceListData.SEQUENCES)
        self.wantPets = self.config.GetBool('want-pets', 1)
        self.wantBingo = self.config.GetBool('want-fish-bingo', 1)
        self.wantKarts = self.config.GetBool('want-karts', 1)
        self.inactivityTimeout = self.config.GetFloat('inactivity-timeout', ToontownGlobals.KeyboardTimeout)
        if self.inactivityTimeout:
            self.notify.debug('Enabling Panda timeout: %s' % self.inactivityTimeout)
            self.mouseWatcherNode.setInactivityTimeout(self.inactivityTimeout)
            self.mouseWatcherNode.setEnterPattern('mouse-enter-%r')
        self.mouseWatcherNode.setLeavePattern('mouse-leave-%r')
        self.mouseWatcherNode.setButtonDownPattern('button-down-%r')
        self.mouseWatcherNode.setButtonUpPattern('button-up-%r')
        self.randomMinigameAbort = self.config.GetBool('random-minigame-abort', 0)
        self.randomMinigameDisconnect = self.config.GetBool('random-minigame-disconnect', 0)
        self.randomMinigameNetworkPlugPull = self.config.GetBool('random-minigame-netplugpull', 0)
        self.autoPlayAgain = self.config.GetBool('auto-play-again', 0)
        self.skipMinigameReward = self.config.GetBool('skip-minigame-reward', 0)
        self.wantMinigameDifficulty = self.config.GetBool('want-minigame-difficulty', 0)
        self.minigameDifficulty = self.config.GetFloat('minigame-difficulty', -1.0)
        if self.minigameDifficulty == -1.0:
            del self.minigameDifficulty
        self.minigameSafezoneId = self.config.GetInt('minigame-safezone-id', -1)
        if self.minigameSafezoneId == -1:
            del self.minigameSafezoneId
        cogdoGameSafezoneId = self.config.GetInt('cogdo-game-safezone-id', -1)
        cogdoGameDifficulty = self.config.GetFloat('cogdo-game-difficulty', -1)
        if cogdoGameDifficulty != -1:
            self.cogdoGameDifficulty = cogdoGameDifficulty
        if cogdoGameSafezoneId != -1:
            self.cogdoGameSafezoneId = cogdoGameSafezoneId
        ToontownBattleGlobals.SkipMovie = self.config.GetBool('skip-battle-movies', 0)
        self.housingEnabled = self.config.GetBool('want-housing', 1)
        self.cannonsEnabled = self.config.GetBool('estate-cannons', 0)
        self.fireworksEnabled = self.config.GetBool('estate-fireworks', 0)
        self.dayNightEnabled = self.config.GetBool('estate-day-night', 0)
        self.cloudPlatformsEnabled = self.config.GetBool('estate-clouds', 0)
        self.greySpacing = self.config.GetBool('allow-greyspacing', 0)
        self.slowQuietZone = self.config.GetBool('slow-quiet-zone', 0)
        self.slowQuietZoneDelay = self.config.GetFloat('slow-quiet-zone-delay', 5)
        self.killInterestResponse = self.config.GetBool('kill-interest-response', 0)
        tpMgr = TextPropertiesManager.getGlobalPtr()
        WLDisplay = TextProperties()
        WLDisplay.setSlant(0.3)
        tpMgr.setProperties('WLDisplay', WLDisplay)
        WLRed = tpMgr.getProperties('red')
        WLRed.setTextColor(1.0, 0.0, 0.0, 1)
        tpMgr.setProperties('WLRed', WLRed)
        del tpMgr
        self.lastScreenShotTime = globalClock.getRealTime()
        self.localAvatarStyle = None
        
        self.frameRateMeter = None
        
        self.filters = CommonFilters(self.win, self.cam)
        self.wantCogInterface = settings.get('cogInterface', True)

        if not settings['keybindings']:
            settings['keybindings'] = self.defaultKeybinds
        self.snapshotSfx = loader.loadSfx('phase_4/audio/sfx/Photo_shutter.ogg')
        self.flashTrack = None
        self.accept(self.getKey('SCREENSHOT'), self.takeScreenShot)

    def getRepository(self):
        return self.cr

    def openMainWindow(self, *args, **kw):
        result = ShowBase.openMainWindow(self, *args, **kw)
        self.setCursorAndIcon()
        return result

    def setCursorAndIcon(self):
        atexit.register(shutil.rmtree, tempdir)

        wp = WindowProperties()
        wp.setCursorFilename(Filename.fromOsSpecific(os.path.join(tempdir, 'toonmono.cur')))
        wp.setIconFilename(Filename.fromOsSpecific(os.path.join(tempdir, 'icon.ico')))
        self.win.requestProperties(wp)

    def addCullBins(self):
        cbm = CullBinManager.getGlobalPtr()
        cbm.addBin('ground', CullBinManager.BTUnsorted, 14)
        cbm.addBin('shadow', CullBinManager.BTBackToFront, 15)
        cbm.addBin('gui-popup', CullBinManager.BTUnsorted, 60)

    def disableShowbaseMouse(self):
        self.useDrive()
        self.disableMouse()
        if self.mouseInterface: self.mouseInterface.detachNode()
        if self.mouse2cam: self.mouse2cam.detachNode()

    def toggleGui(self):
        if aspect2d.isHidden():
            aspect2d.show()
        else:
            aspect2d.hide()

    def takeScreenShot(self):
        if self.flashTrack and self.flashTrack.isPlaying():
            return
        if not os.path.exists(TTLocalizer.ScreenshotPath):
            os.mkdir(TTLocalizer.ScreenshotPath)
            self.notify.info('Made new directory to save screenshots.')
        namePrefix = TTLocalizer.ScreenshotPath + 'geargrind-screenshot'
        self.graphicsEngine.renderFrame()
        messenger.send('takingScreenshot')
        self.screenshot(namePrefix=namePrefix)
        base.playSfx(self.snapshotSfx)
        self.transitions.setFadeColor(1, 1, 1)
        self.transitions.fadeOut(0.15)
        self.flashTrack = Sequence(Func(self.transitions.fadeIn, 0.8), Wait(1), Func(self.transitions.setFadeColor, 0, 0, 0))
        self.flashTrack.start()

    def initNametagGlobals(self):
        arrow = loader.loadModel('phase_3/models/props/arrow')
        card = loader.loadModel('phase_3/models/props/panel')
        miner_panel = loader.loadModel('phase_3/models/props/miner_panel')
        speech3d = ChatBalloon(loader.loadModel('phase_3/models/props/chatbox'))
        thought3d = ChatBalloon(loader.loadModel('phase_3/models/props/chatbox_thought_cutout'))
        speech2d = ChatBalloon(loader.loadModel('phase_3/models/props/chatbox_noarrow'))
        chatButtonGui = loader.loadModel('phase_3/models/gui/chat_button_gui')
        NametagGlobals.setCamera(self.cam)
        NametagGlobals.setArrowModel(arrow)
        NametagGlobals.setNametagCard(card, VBase4(-0.5, 0.5, -0.5, 0.5))
        NametagGlobals.setNametagCard(miner_panel, VBase4(-0.5, 0.5, -0.5, 0.5))
        if self.mouseWatcherNode:
            NametagGlobals.setMouseWatcher(self.mouseWatcherNode)
        NametagGlobals.setSpeechBalloon3d(speech3d)
        NametagGlobals.setThoughtBalloon3d(thought3d)
        NametagGlobals.setSpeechBalloon2d(speech2d)
        NametagGlobals.setThoughtBalloon2d(thought3d)
        NametagGlobals.setPageButton(PGButton.SReady, chatButtonGui.find('**/Horiz_Arrow_UP'))
        NametagGlobals.setPageButton(PGButton.SDepressed, chatButtonGui.find('**/Horiz_Arrow_DN'))
        NametagGlobals.setPageButton(PGButton.SRollover, chatButtonGui.find('**/Horiz_Arrow_Rllvr'))
        NametagGlobals.setQuitButton(PGButton.SReady, chatButtonGui.find('**/CloseBtn_UP'))
        NametagGlobals.setQuitButton(PGButton.SDepressed, chatButtonGui.find('**/CloseBtn_DN'))
        NametagGlobals.setQuitButton(PGButton.SRollover, chatButtonGui.find('**/CloseBtn_Rllvr'))
        rolloverSound = DirectGuiGlobals.getDefaultRolloverSound()
        if rolloverSound:
            NametagGlobals.setRolloverSound(rolloverSound)
        clickSound = DirectGuiGlobals.getDefaultClickSound()
        if clickSound:
            NametagGlobals.setClickSound(clickSound)
        NametagGlobals.setToon(self.cam)

        self.marginManager = MarginManager()
        self.margins = self.aspect2d.attachNewNode(self.marginManager, DirectGuiGlobals.MIDGROUND_SORT_INDEX + 1)
        mm = self.marginManager

        # TODO: Dynamicaly add more and reposition cells
        padding = 0.0225

        # Order: Top to bottom
        self.leftCells = [
            mm.addGridCell(0.2 + padding, -0.45, base.a2dTopLeft), # Above boarding groups
            mm.addGridCell(0.2 + padding, -0.9, base.a2dTopLeft),  # 1
            mm.addGridCell(0.2 + padding, -1.35, base.a2dTopLeft)  # Below Boarding Groups
        ]

        # Order: Left to right
        self.bottomCells = [
            mm.addGridCell(-0.87, 0.2 + padding, base.a2dBottomCenter), # To the right of the laff meter
            mm.addGridCell(-0.43, 0.2 + padding, base.a2dBottomCenter), # 1
            mm.addGridCell(0.01, 0.2 + padding, base.a2dBottomCenter),  # 2
            mm.addGridCell(0.45, 0.2 + padding, base.a2dBottomCenter),  # 3
            mm.addGridCell(0.89, 0.2 + padding, base.a2dBottomCenter)   # To the left of the shtiker book
        ]

        # Order: Bottom to top
        self.rightCells = [
            mm.addGridCell(-0.2 - padding, -1.35, base.a2dTopRight), # Above the street map
            mm.addGridCell(-0.2 - padding, -0.9, base.a2dTopRight),  # Below the friends list
            mm.addGridCell(-0.2 - padding, -0.45, base.a2dTopRight)  # Behind the friends list
        ]

    def hideFriendMargins(self):
        middleCell = self.rightCells[1]
        topCell = self.rightCells[2]

        self.setCellsAvailable([middleCell, topCell], False)

    def showFriendMargins(self):
        middleCell = self.rightCells[1]
        topCell = self.rightCells[2]

        self.setCellsAvailable([middleCell, topCell], True)

    def setCellsAvailable(self, cell_list, available):
        for cell in cell_list:
            self.marginManager.setCellAvailable(cell, available)

    def startShow(self, cr):
        self.cr = cr
        base.graphicsEngine.renderFrame()
        # Get the base port.
        serverPort = base.config.GetInt('server-port', 6667)

        # Get the number of client-agents.
        clientagents = base.config.GetInt('client-agents', 1) - 1

        # Get a new port.
        serverPort += (random.randint(0, clientagents) * 100)

        serverList = []

        for name in launcher.getGameServer().split(';'):
            url = URLSpec(name, 1)
            url.setScheme('https')

            if url.getServer() == "127.0.0.1":
                url.setScheme('')

            if not url.hasPort():
                url.setPort(serverPort)
            serverList.append(url)

        if len(serverList) == 1:
            failover = base.config.GetString('server-failover', '')
            serverURL = serverList[0]
            for arg in failover.split():
                try:
                    port = int(arg)
                    url = URLSpec(serverURL)
                    url.setPort(port)
                except:
                    url = URLSpec(arg, 1)

                if url != serverURL:
                    serverList.append(url)

        cr.loginFSM.request('connect', [serverList])

        # If enabled, start detecting speed hacks:
        if config.GetBool('want-speedhack-check', False):
            self.lastSpeedHackCheck = time.time()
            self.lastTrueClockTime = TrueClock.getGlobalPtr().getLongTime()
            taskMgr.add(self.__speedHackCheckTick, 'speedHackCheck-tick')

    def __speedHackCheckTick(self, task):
        elapsed = time.time() - self.lastSpeedHackCheck
        tcElapsed = TrueClock.getGlobalPtr().getLongTime() - self.lastTrueClockTime

        if tcElapsed > (elapsed + 0.05):
            # The TrueClock is running faster than it should. This means the
            # player may have sped up the process. Disconnect them:
            self.cr.stopReaderPollTask()
            self.cr.lostConnection()
            return task.done

        self.lastSpeedHackCheck = time.time()
        self.lastTrueClockTime = TrueClock.getGlobalPtr().getLongTime()

        return task.cont

    def removeGlitchMessage(self):
        self.ignore('InputState-forward')

    def exitShow(self, errorCode = None):
        self.notify.info('Exiting Toontown: errorCode = %s' % errorCode)
        sys.exit()

    def setExitErrorCode(self, code):
        self.exitErrorCode = code

    def getExitErrorCode(self):
        return self.exitErrorCode

    def userExit(self):
        if hasattr(self, 'localAvatar'):
            self.localAvatar.d_setAnimState('TeleportOut', 1)
        if self.cr.timeManager:
            self.cr.timeManager.setDisconnectReason(ToontownGlobals.DisconnectCloseWindow)
        base.cr._userLoggingOut = False
        if hasattr(self, 'localAvatar'):
            messenger.send('clientLogout')
            self.cr.dumpAllSubShardObjects()
        self.cr.loginFSM.request('shutdown')
        self.notify.info('User exiting...')
        self.ignore(ToontownGlobals.QuitGameHotKeyOSX)
        self.ignore(ToontownGlobals.QuitGameHotKeyRepeatOSX)
        self.ignore(ToontownGlobals.HideGameHotKeyOSX)
        self.ignore(ToontownGlobals.HideGameHotKeyRepeatOSX)
        self.ignore(ToontownGlobals.MinimizeGameHotKeyOSX)
        self.ignore(ToontownGlobals.MinimizeGameHotKeyRepeatOSX)
        self.exitShow()

    def panda3dRenderError(self):
        if self.cr.timeManager:
            self.cr.timeManager.setDisconnectReason(ToontownGlobals.DisconnectGraphicsError)
        self.cr.sendDisconnect()
        sys.exit()

    def playMusic(self, music, looping = 0, interrupt = 1, volume = None, time = 0.0):
        ShowBase.playMusic(self, music, looping, interrupt, volume, time)

    # OS X Specific Actions
    def exitOSX(self):
        self.confirm = TTDialog.TTGlobalDialog(doneEvent='confirmDone', message=TTLocalizer.OptionsPageExitConfirm, style=TTDialog.TwoChoice)
        self.confirm.show()
        self.accept('confirmDone', self.handleConfirm)

    def handleConfirm(self):
        status = self.confirm.doneStatus
        self.ignore('confirmDone')
        self.confirm.cleanup()
        del self.confirm
        if status == 'ok':
            self.userExit()

    def hideGame(self):
        # Hacky, I know, but it works
        hideCommand = """osascript -e 'tell application "System Events"
                                            set frontProcess to first process whose frontmost is true
                                            set visible of frontProcess to false
                                       end tell'"""
        os.system(hideCommand)

    def minimizeGame(self):
        wp = WindowProperties()
        wp.setMinimized(True)
        base.win.requestProperties(wp)

    def run(self):
        try:
            taskMgr.run()
        except SystemExit:
            self.notify.info('Normal exit.')
            self.destroy()
            raise
        except:
            self.notify.warning('Handling Python exception.')
            if getattr(self, 'cr', None):
                if self.cr.timeManager:
                    from otp.otpbase import OTPGlobals
                    self.cr.timeManager.setDisconnectReason(OTPGlobals.DisconnectPythonError)
                    self.cr.timeManager.setExceptionInfo()
                self.cr.sendDisconnect()
            self.notify.info('Exception exit.\n')
            self.destroy()
            import traceback
            traceback.print_exc()
            if settings['automaticErrorReporting']:
                from raven import Client
                if hasattr(self, 'localAvatar'):
                    avatarId = self.localAvatar.doId
                else:
                    avatarId = 'NONE'
                errorReporter = Client(config.GetString('sentry-dsn', ''))
                errorReporter.user_context({
                    'PLAYTOKEN': self.cr.playToken,
                    'AVATAR_ID': avatarId
                })
                errorReporter.captureMessage(traceback.format_exc())
			
    def updateKeybinds(self, keys={}): 
        for key, value in keys.iteritems():
            settings['keybindings'][key] = value
        settings.write()
        if hasattr(self, 'localAvatar'):
            self.localAvatar.controlManager.update()
            self.localAvatar.chatMgr.updateChatKey()			
    
    def getKey(self, key):
        if key not in settings['keybindings']:
            settings['keybindings'][key] = self.defaultKeybinds[key]
        return settings['keybindings'][key]
        
    def setFrameRateMeter(self, flag):
        if flag:
            if not self.frameRateMeter:
                self.frameRateMeter = TTFrameRateMeter('frameRateMeter')
                self.frameRateMeter.setupWindow(self.win)
        else:
            if self.frameRateMeter:
                self.frameRateMeter.clearWindow()
                self.frameRateMeter = None

@magicWord(category=CATEGORY_COMMUNITY_MANAGER)
def oobe():
    """
    Toggle the 'out of body experience' view.
    """
    base.oobe()

@magicWord(category=CATEGORY_PROGRAMMER)
def oobeCull():
    """
    Toggle the 'out of body experience' view with culling debugging.
    """
    base.oobeCull()

@magicWord(category=CATEGORY_COMMUNITY_MANAGER)
def wire():
    """
    Toggle the 'wireframe' view.
    """
    base.toggleWireframe()

@magicWord(category=CATEGORY_COMMUNITY_MANAGER)
def idNametags():
    """
    Display avatar IDs inside nametags.
    """
    messenger.send('nameTagShowAvId')

@magicWord(category=CATEGORY_COMMUNITY_MANAGER)
def nameNametags():
    """
    Display only avatar names inside nametags.
    """
    messenger.send('nameTagShowName')

@magicWord(category=CATEGORY_COMMUNITY_MANAGER)
def a2d():
    """
    Toggle aspect2d.
    """
    if aspect2d.isHidden():
        aspect2d.show()
    else:
        aspect2d.hide()

@magicWord(category=CATEGORY_COMMUNITY_MANAGER)
def placer():
    """
    Toggle the camera placer.
    """
    base.camera.place()

@magicWord(category=CATEGORY_COMMUNITY_MANAGER)
def explorer():
    """
    Toggle the scene graph explorer.
    """
    base.render.explore()

@magicWord(category=CATEGORY_COMMUNITY_MANAGER)
def neglect():
    """
    toggle the neglection of network updates on the invoker's client.
    """
    if base.cr.networkPlugPulled():
        base.cr.restoreNetworkPlug()
        return 'You are no longer neglecting network updates.'
    else:
        base.cr.pullNetworkPlug()
        return 'You are now neglecting network updates.'

@magicWord(category=CATEGORY_COMMUNITY_MANAGER, types=[float, float, float, float])
def backgroundColor(r=None, g=1, b=1, a=1):
    """
    set the background color. Specify no arguments for the default background
    color.
    """
    if r is None:
        r, g, b, a = OTPGlobals.DefaultBackgroundColor
    base.setBackgroundColor(Vec4(r, g, b, a))
    return 'The background color has been changed.'
