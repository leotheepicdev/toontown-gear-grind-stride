from panda3d.core import BitMask32, CollideMask, CollisionHandler, CollisionHandlerEvent, CollisionNode, CollisionSphere, NodePath, Notify, Point3, TextNode, VBase4, Vec2, Vec3, Vec4
from direct.directnotify import DirectNotifyGlobal
from direct.distributed.ClockDelta import *
from direct.gui import DirectGuiGlobals
from direct.gui.DirectGui import *
from direct.interval.IntervalGlobal import *
from direct.showbase import PythonUtil
from direct.showbase.PythonUtil import *
from direct.task import Task
import math
import DistributedToon
import LaffMeter
import Toon
from toontown.hood import ZoneUtil
from toontown.avatar import DistributedPlayer
from toontown.avatar import LocalAvatar
from toontown.avatar import PositionExaminer
from toontown.battle import Fanfare
from toontown.battle.BattleSounds import *
from toontown.catalog import CatalogNotifyDialog
from toontown.chat import TTTalkAssistant
from toontown.chat import ToontownChatManager
from lib.nametag.NametagConstants import *
from lib.margins.WhisperPopup import *
from toontown.estate import GardenGlobals
from toontown.parties import PartyGlobals
from toontown.quest import QuestMap
from toontown.quest import QuestParser
from toontown.quest import Quests
from toontown.shtiker import DisguisePage
from toontown.shtiker import PhotoAlbumPage
from toontown.shtiker import EventsPage
from toontown.shtiker import ItemPage
from toontown.shtiker import FishPage
from toontown.shtiker import GardenPage
from toontown.shtiker import GolfPage
from toontown.shtiker import InventoryPage
from toontown.shtiker import KartPage
from toontown.shtiker import MapPage
from toontown.shtiker import NPCFriendPage
from toontown.shtiker import OptionsPage
from toontown.shtiker import QuestPage
from toontown.shtiker import ShardPage
from toontown.shtiker import ShtikerBook
from toontown.shtiker import SuitPage
from toontown.shtiker import TrackPage
from toontown.toon import ElevatorNotifier
from toontown.toon import ToonDNA
from toontown.toon.DistributedNPCToonBase import DistributedNPCToonBase
from toontown.toon.ChatLog import ChatLog
from toontown.base import TTLocalizer
from otp.otpbase import OTPGlobals # temp until we shift movement stuff to ToontownGlobals
from toontown.base import ToontownGlobals
from toontown.base.ToontownGlobals import *
from toontown.friends.FriendHandle import FriendHandle

ClaraBaseXPos = 0.12

class LocalToon(DistributedToon.DistributedToon, LocalAvatar.LocalAvatar):
    neverDisable = 1
    piePowerSpeed = base.config.GetDouble('pie-power-speed', 0.2)
    piePowerExponent = base.config.GetDouble('pie-power-exponent', 0.75)

    def __init__(self, cr):
        try:
            self.LocalToon_initialized
        except:
            self.LocalToon_initialized = 1
            self.numFlowers = 0
            self.maxFlowerBasket = 0
            DistributedToon.DistributedToon.__init__(self, cr)
            chatMgr = ToontownChatManager.ToontownChatManager(cr, self)
            talkAssistant = TTTalkAssistant.TTTalkAssistant()
            LocalAvatar.LocalAvatar.__init__(self, cr, chatMgr, talkAssistant, passMessagesThrough=True)
            self.soundRun = loader.loadSfx('phase_3.5/audio/sfx/AV_footstep_runloop.ogg')
            self.soundWalk = loader.loadSfx('phase_3.5/audio/sfx/AV_footstep_walkloop.ogg')
            self.soundWhisper = loader.loadSfx('phase_3.5/audio/sfx/GUI_whisper_3.ogg')
            self.soundPhoneRing = loader.loadSfx('phase_3.5/audio/sfx/telephone_ring.ogg')
            self.soundSystemMessage = loader.loadSfx('phase_4/audio/sfx/clock03.ogg')
            self.positionExaminer = PositionExaminer.PositionExaminer()
            friendsGui = loader.loadModel('phase_3.5/models/gui/friendslist_gui')
            friendsButtonNormal = friendsGui.find('**/FriendsBox_Closed')
            friendsButtonPressed = friendsGui.find('**/FriendsBox_Rollover')
            friendsButtonRollover = friendsGui.find('**/FriendsBox_Rollover')
            self.bFriendsList = DirectButton(image=(friendsButtonNormal, friendsButtonPressed, friendsButtonRollover), relief=None, pos=(-0.141, 0, -0.125), parent=base.a2dTopRight, scale=0.8, text=('', TTLocalizer.FriendsListLabel, TTLocalizer.FriendsListLabel), text_scale=0.09, text_fg=Vec4(1, 1, 1, 1), text_shadow=Vec4(0, 0, 0, 1), text_pos=(0, -0.18), text_font=ToontownGlobals.getInterfaceFont(), command=self.sendFriendsListEvent)
            self.bFriendsList.hide()
            self.friendsListButtonActive = 0
            self.friendsListButtonObscured = 0
            self.moveFurnitureButtonObscured = 0
            self.clarabelleButtonObscured = 0
            friendsGui.removeNode()
            self.__furnitureGui = None
            self.__lerpFurnitureButton = None
            self.__clarabelleButton = None
            self.__clarabelleFlash = None
            self.furnitureManager = None
            self.furnitureDirector = None
            self.gotCatalogNotify = 0
            self.__catalogNotifyDialog = None
            Toon.loadDialog()
            self.isIt = 0
            self.cantLeaveGame = 0
            self.tunnelX = 0.0
            self.estate = None
            self.__pieBubble = None
            self.allowPies = 0
            self.__pieButton = None
            self.__piePowerMeter = None
            self.__piePowerMeterSequence = None
            self.__pieButtonType = None
            self.__pieButtonCount = None
            self.tossPieStart = None
            self.__presentingPie = 0
            self.__pieSequence = 0
            self.wantBattles = base.config.GetBool('want-battles', 1)
            wantNameTagAvIds = base.config.GetBool('want-nametag-avids', 0)
            if wantNameTagAvIds:
                messenger.send('nameTagShowAvId', [])
                base.idTags = 1
            self.glitchX = 0
            self.glitchY = 0
            self.glitchZ = 0
            self.glitchCount = 0
            self.ticker = 0
            self.glitchOkay = 1
            self.tempGreySpacing = 0
            self.wantStatePrint = base.config.GetBool('want-statePrint', 0)
            self.__gardeningGui = None
            self.__gardeningGuiFake = None
            self.__shovelButton = None
            self.shovelRelatedDoId = 0
            self.shovelAbility = ''
            self.plantToWater = 0
            self.petId = 0
            self.shovelButtonActiveCount = 0
            self.wateringCanButtonActiveCount = 0
            self.showingWateringCan = 0
            self.showingShovel = 0
            self.touchingPlantList = []
            self.inGardenAction = None
            self.guiConflict = 0
            self.elevatorNotifier = ElevatorNotifier.ElevatorNotifier()
            self._zoneId = None
            self.accept('system message aknowledge', self.systemWarning)
            self.systemMsgAckGuiDoneEvent = 'systemMsgAckGuiDoneEvent'
            self.accept(self.systemMsgAckGuiDoneEvent, self.hideSystemMsgAckGui)
            self.systemMsgAckGui = None
            self.createSystemMsgAckGui()
            self.acceptingNewFriends = True
            self.acceptingNonFriendWhispers = True
            self.acceptingTeleport = True
            self.physControls.event.addAgainPattern('again%in')
            self.oldPos = None
            self.questMap = None
            self.prevToonIdx = 0
            self.houseType = 0
            self.inEstate = 0
            self.kartToggleAllowed = 1

    def setDNA(self, dna):
        base.localAvatarStyle = dna
        DistributedToon.DistributedToon.setDNA(self, dna)

    def setName(self, name):
        base.localAvatarName = name
        DistributedToon.DistributedToon.setName(self, name)
        messenger.send('refreshNametagStyle')

    def wantLegacyLifter(self):
        return True

    def startGlitchKiller(self):
        if localAvatar.getZoneId() not in GlitchKillerZones:
            return
        taskMgr.remove(self.uniqueName('glitchKiller'))
        taskMgr.add(self.glitchKiller, self.uniqueName('glitchKiller'))
        self.glitchOkay = 1

    def pauseGlitchKiller(self):
        self.tempGreySpacing = 1

    def unpauseGlitchKiller(self):
        self.tempGreySpacing = 0

    def stopGlitchKiller(self):
        taskMgr.remove(self.uniqueName('glitchKiller'))
        self.glitchOkay = 1

    def glitchKiller(self, taskFooler = 0):
        if base.greySpacing or self.tempGreySpacing:
            return Task.cont
        self.ticker += 1
        if not self.physControls.lifter.hasContact() and not self.glitchOkay:
            self.glitchCount += 1
        else:
            self.glitchX = self.getX()
            self.glitchY = self.getY()
            self.glitchZ = self.getZ()
            self.glitchCount = 0
            if self.physControls.lifter.hasContact():
                self.glitchOkay = 0
        if hasattr(self, 'physControls'):
            if self.ticker >= 10:
                self.ticker = 0
        if self.glitchCount >= 7:
            print 'GLITCH MAXED!!! resetting pos'
            self.setX(self.glitchX - 1 * (self.getX() - self.glitchX))
            self.setY(self.glitchY - 1 * (self.getY() - self.glitchY))
            self.glitchCount = 0
        return Task.cont

    def announceGenerate(self):
        self.startLookAround()
        DistributedToon.DistributedToon.announceGenerate(self)

        acceptingNewFriends = settings.get('acceptingNewFriends', {})
        acceptingNonFriendWhispers = settings.get('acceptingNonFriendWhispers', {})
        acceptingTeleport = settings.get('acceptingTeleport', {})
        if str(self.doId) not in acceptingNewFriends:
            acceptingNewFriends[str(self.doId)] = True
            settings['acceptingNewFriends'] = acceptingNewFriends
        if str(self.doId) not in acceptingNonFriendWhispers:
            acceptingNonFriendWhispers[str(self.doId)] = True
            settings['acceptingNonFriendWhispers'] = acceptingNonFriendWhispers
        if str(self.doId) not in acceptingTeleport:
            acceptingTeleport[str(self.doId)] = True
            settings['acceptingTeleport'] = acceptingTeleport
        self.acceptingNewFriends = acceptingNewFriends[str(self.doId)]
        self.acceptingNonFriendWhispers = acceptingNonFriendWhispers[str(self.doId)]
        self.acceptingTeleport = acceptingTeleport[str(self.doId)]

    def disable(self):
        self.laffMeter.destroy()
        del self.laffMeter
        self.questMap.destroy()
        self.questMap = None
        self.book.unload()
        del self.optionsPage
        del self.shardPage
        del self.mapPage
        del self.invPage
        del self.questPage
        del self.suitPage
        del self.sosPage
        del self.disguisePage
        del self.fishPage
        del self.gardenPage
        del self.trackPage
        del self.book
        if base.wantKarts:
            if hasattr(self, 'kartPage'):
                del self.kartPage
        self.ignoreAll()
        DistributedToon.DistributedToon.disable(self)
        return

    def disableBodyCollisions(self):
        pass

    def delete(self):
        try:
            self.LocalToon_deleted
        except:
            self.LocalToon_deleted = 1
            Toon.unloadDialog()
            QuestParser.clear()
            DistributedToon.DistributedToon.delete(self)
            LocalAvatar.LocalAvatar.delete(self)
            self.bFriendsList.destroy()
            del self.bFriendsList
            if self.__pieButton:
                self.__pieButton.destroy()
                self.__pieButton = None
            if self.__piePowerMeter:
                self.__piePowerMeter.destroy()
                self.__piePowerMeter = None
            taskMgr.remove('unlockGardenButtons')
            if self.__lerpFurnitureButton:
                self.__lerpFurnitureButton.finish()
            if self.__furnitureGui:
                self.__furnitureGui.destroy()
            del self.__furnitureGui
            if self.__gardeningGui:
                self.__gardeningGui.destroy()
            del self.__gardeningGui
            if self.__gardeningGuiFake:
                self.__gardeningGuiFake.destroy()
            del self.__gardeningGuiFake
            if self.__clarabelleButton:
                self.__clarabelleButton.destroy()
            del self.__clarabelleButton
            if self.__clarabelleFlash:
                self.__clarabelleFlash.finish()
            del self.__clarabelleFlash
            if self.__catalogNotifyDialog:
                self.__catalogNotifyDialog.cleanup()
            del self.__catalogNotifyDialog

        return

    def initInterface(self):
        self.book = ShtikerBook.ShtikerBook('bookDone')
        self.book.load()
        self.book.hideButton()
        self.optionsPage = OptionsPage.OptionsPage()
        self.optionsPage.load()
        self.book.addPage(self.optionsPage, pageName=TTLocalizer.OptionsPageTitle)
        self.itemPage = ItemPage.ItemPage()
        self.itemPage.load()
        self.book.addPage(self.itemPage, pageName=TTLocalizer.ItemPageTitle)
        self.shardPage = ShardPage.ShardPage()
        self.shardPage.load()
        self.book.addPage(self.shardPage, pageName=TTLocalizer.ShardPageTitle)
        self.mapPage = MapPage.MapPage()
        self.mapPage.load()
        self.book.addPage(self.mapPage, pageName=TTLocalizer.MapPageTitle)
        self.invPage = InventoryPage.InventoryPage()
        self.invPage.load()
        self.book.addPage(self.invPage, pageName=TTLocalizer.InventoryPageTitle)
        self.questPage = QuestPage.QuestPage()
        self.questPage.load()
        self.book.addPage(self.questPage, pageName=TTLocalizer.QuestPageToonTasks)
        self.trackPage = TrackPage.TrackPage()
        self.trackPage.load()
        self.book.addPage(self.trackPage, pageName=TTLocalizer.TrackPageShortTitle)
        self.suitPage = SuitPage.SuitPage()
        self.suitPage.load()
        self.book.addPage(self.suitPage, pageName=TTLocalizer.SuitPageTitle)
        self.fishPage = FishPage.FishPage()
        self.fishPage.setAvatar(self)
        self.fishPage.load()
        self.book.addPage(self.fishPage, pageName=TTLocalizer.FishPageTitle)
        if base.wantKarts:
            self.addKartPage()
        self.disguisePage = DisguisePage.DisguisePage()
        self.disguisePage.load()
        self.book.addPage(self.disguisePage, pageName=TTLocalizer.DisguisePageTitle)
        self.sosPage = NPCFriendPage.NPCFriendPage()
        self.sosPage.load()
        self.book.addPage(self.sosPage, pageName=TTLocalizer.NPCFriendPageTitle)
        if self.gardenStarted:
            self.loadGardenPages()
        self.addGolfPage()
        self.photoPage = PhotoAlbumPage.PhotoAlbumPage()
        self.photoPage.load()
        self.book.addPage(self.photoPage, pageName=TTLocalizer.PhotoPageTitle)
        self.addEventsPage()
        self.book.setPage(self.mapPage, enterPage=False)
        self.laffMeter = LaffMeter.LaffMeter(self.style, self.hp, self.maxHp)
        self.laffMeter.setAvatar(self)
        self.laffMeter.setScale(0.075)
        self.laffMeter.reparentTo(base.a2dBottomLeft)
        if self.style.getAnimal() == 'monkey':
            self.laffMeter.setPos(0.153, 0.0, 0.13)
        else:
            self.laffMeter.setPos(0.133, 0.0, 0.13)
        self.laffMeter.stop()
        self.chatLog = ChatLog()
        self.chatLog.hide()
        self.questMap = QuestMap.QuestMap(self)
        self.questMap.stop()
        self.accept('time-insert', self.__beginTossPie)
        self.accept('time-insert-up', self.__endTossPie)
        self.accept('time-%s' % base.getKey('ACTION'), self.__beginTossPie)
        self.accept('time-%s-up' % base.getKey('ACTION'), self.__endTossPie)
        self.accept('pieHit', self.__pieHit)
        self.accept('interrupt-pie', self.interruptPie)
        self.accept(base.getKey('SPRINT'), self.__beginSprint)
        self.accept('{0}-up'.format(base.getKey('SPRINT')), self.__endSprint)
        self.accept('InputState-jump', self.__toonMoved)
        self.accept('InputState-forward', self.__toonMoved)
        self.accept('InputState-reverse', self.__toonMoved)
        self.accept('InputState-turnLeft', self.__toonMoved)
        self.accept('InputState-turnRight', self.__toonMoved)
        self.accept('InputState-slide', self.__toonMoved)

        QuestParser.init()

    if base.wantKarts:

        def addKartPage(self):
            if self.hasKart():
                if hasattr(self, 'kartPage') and self.kartPage != None:
                    return
                self.kartPage = KartPage.KartPage()
                self.kartPage.setAvatar(self)
                self.kartPage.load()
                self.book.addPage(self.kartPage, pageName=TTLocalizer.KartPageTitle)
            return
            
    def acceptOnscreenHooks(self):
        self.accept('insert', self.__toggleKart)
        
    def ignoreOnscreenHooks(self):
        self.ignore('insert')
        
    def __toggleKart(self):
        if not self.hasKart():
            return self.showHpString(TTLocalizer.NoKartAvailable, duration=1.1, scale=0.5)
        if not self.racingZoneCheck():
            return self.showHpString(TTLocalizer.CannotRaceHere, duration=1.1, scale=0.5)
        if not self.kartToggleAllowed:
            return self.showHpString(TTLocalizer.KartToggleTooFast, duration=1.1, scale=0.5)
        self.kartToggleAllowed = 0
        self.sendUpdate('toggleKart')
        taskMgr.doMethodLater(2, self.allowKartToggle, 'allowKartToggle')
        
    def allowKartToggle(self, task=None):
        self.kartToggleAllowed = 1
        if task:
            return task.done

    def setWantBattles(self, wantBattles):
        self.wantBattles = wantBattles

    def loadGardenPages(self):
        if self.gardenPage != None:
            return
        self.gardenPage = GardenPage.GardenPage()
        self.gardenPage.load()
        self.book.addPage(self.gardenPage, pageName=TTLocalizer.GardenPageTitle)

    def displayTalkWhisper(self, avId, chat):
        sender = base.cr.identifyAvatar(avId)

        if not sender:
            return

        if base.whiteList:
            chat = base.whiteList.processThroughAll(chat, sender, sender.chatGarbler)

        chatString = '%s: %s' % (sender.getName(), chat)
        whisper = WhisperPopup(chatString, ToontownGlobals.getInterfaceFont(), WTNormal)
        whisper.setClickable(avId)
        whisper.manage(base.marginManager)
        base.playSfx(self.soundWhisper)

    def isLocal(self):
        return 1

    def startChat(self):
        self.notify.info('calling LocalAvatar.startchat')
        LocalAvatar.LocalAvatar.startChat(self)
        self.accept('chatUpdateSCToontask', self.b_setSCToontask)
        self.accept('chatUpdateSCResistance', self.d_reqSCResistance)
        self.accept('whisperUpdateSCToontask', self.whisperSCToontaskTo)

    def stopChat(self):
        LocalAvatar.LocalAvatar.stopChat(self)
        self.ignore('chatUpdateSCToontask')
        self.ignore('chatUpdateSCResistance')
        self.ignore('whisperUpdateSCToontask')

    def tunnelIn(self, tunnelOrigin):
        self.b_setTunnelIn(self.tunnelX * 0.8, tunnelOrigin)

    def tunnelOut(self, tunnelOrigin):
        self.tunnelX = self.getX(tunnelOrigin)
        tunnelY = self.getY(tunnelOrigin)
        self.b_setTunnelOut(self.tunnelX * 0.95, tunnelY, tunnelOrigin)

    def handleTunnelIn(self, startTime, endX, x, y, z, h):
        self.notify.debug('LocalToon.handleTunnelIn')
        tunnelOrigin = render.attachNewNode('tunnelOrigin')
        tunnelOrigin.setPosHpr(x, y, z, h, 0, 0)
        self.b_setAnimState('run', self.animMultiplier)
        self.stopLookAround()
        self.reparentTo(render)
        self.runSound()
        camera.reparentTo(render)
        camera.setPosHpr(tunnelOrigin, 0, 20, 12, 180, -20, 0)
        base.transitions.irisIn(0.4)
        toonTrack = self.getTunnelInToonTrack(endX, tunnelOrigin)

        def cleanup(self = self, tunnelOrigin = tunnelOrigin):
            self.stopSound()
            tunnelOrigin.removeNode()
            messenger.send('tunnelInMovieDone')

        self.tunnelTrack = Sequence(toonTrack, Func(cleanup))
        self.tunnelTrack.start(globalClock.getFrameTime() - startTime)

    def handleTunnelOut(self, startTime, startX, startY, x, y, z, h):
        self.notify.debug('LocalToon.handleTunnelOut')
        tunnelOrigin = render.attachNewNode('tunnelOrigin')
        tunnelOrigin.setPosHpr(x, y, z, h, 0, 0)
        self.b_setAnimState('run', self.animMultiplier)
        self.runSound()
        self.stopLookAround()
        tracks = Parallel()
        camera.wrtReparentTo(render)
        startPos = camera.getPos(tunnelOrigin)
        startHpr = camera.getHpr(tunnelOrigin)
        camLerpDur = 1.0
        reducedCamH = fitDestAngle2Src(startHpr[0], 180)
        tracks.append(LerpPosHprInterval(camera, camLerpDur, pos=Point3(0, 20, 12), hpr=Point3(reducedCamH, -20, 0), startPos=startPos, startHpr=startHpr, other=tunnelOrigin, blendType='easeInOut', name='tunnelOutLerpCamPos'))
        toonTrack = self.getTunnelOutToonTrack(startX, startY, tunnelOrigin)
        tracks.append(toonTrack)
        irisDur = 0.4
        tracks.append(Sequence(Wait(toonTrack.getDuration() - (irisDur + 0.1)), Func(base.transitions.irisOut, irisDur)))

        def cleanup(self = self, tunnelOrigin = tunnelOrigin):
            self.stopSound()
            self.detachNode()
            tunnelOrigin.removeNode()
            messenger.send('tunnelOutMovieDone')

        self.tunnelTrack = Sequence(tracks, Func(cleanup))
        self.tunnelTrack.start(globalClock.getFrameTime() - startTime)

    def getPieBubble(self):
        if self.__pieBubble == None:
            bubble = CollisionSphere(0, 0, 0, 1)
            node = CollisionNode('pieBubble')
            node.addSolid(bubble)
            node.setFromCollideMask(ToontownGlobals.PieBitmask | ToontownGlobals.CameraBitmask | ToontownGlobals.FloorBitmask)
            node.setIntoCollideMask(BitMask32.allOff())
            self.__pieBubble = NodePath(node)
            self.pieHandler = CollisionHandlerEvent()
            self.pieHandler.addInPattern('pieHit')
            self.pieHandler.addInPattern('pieHit-%in')
        return self.__pieBubble

    def __beginTossPieMouse(self, mouseParam):
        self.__beginTossPie(globalClock.getFrameTime())

    def __endTossPieMouse(self, mouseParam):
        self.__endTossPie(globalClock.getFrameTime())

    def __beginTossPie(self, time):
        if self.tossPieStart != None:
            return
        if not self.allowPies:
            return
        if self.numPies == 0:
            messenger.send('outOfPies')
            return
        if self.__pieInHand():
            return
        if getattr(self.controlManager.currentControls, 'isAirborne', 0):
            return
        messenger.send('wakeup')
        self.localPresentPie(time)
        taskName = self.uniqueName('updatePiePower')
        taskMgr.add(self.__updatePiePower, taskName)

    def __endTossPie(self, time):
        if self.tossPieStart == None:
            return
        taskName = self.uniqueName('updatePiePower')
        taskMgr.remove(taskName)
        messenger.send('wakeup')
        power = self.__getPiePower(time)
        self.tossPieStart = None
        self.localTossPie(power)
        return
        
    def __beginSprint(self):
        if self.getCarActive():
            if self.doId in base.cr.karts:
                base.cr.karts[self.doId].startTurbo()
            return
        if ZoneUtil.isDynamicZone(self.getZoneId()) and not self.inEstate:
            self.showHpString(TTLocalizer.NoSprint, duration=1.1, scale=0.5)
            return
        if ZoneUtil.getWhereName(self.getZoneId(), 1) not in ('playground', 'street', 'toonInterior', 'cogHQExterior', 'factoryExterior'):
            self.showHpString(TTLocalizer.NoSprint, duration=1.1, scale=0.5)
            return
        self.controlManager.setSpeeds(OTPGlobals.ToonForwardSpeed * OTPGlobals.ToonSprintFactor, OTPGlobals.ToonJumpForce, OTPGlobals.ToonReverseSpeed * OTPGlobals.ToonSprintFactor, OTPGlobals.ToonRotateSpeed * OTPGlobals.ToonSprintFactor)

    def __endSprint(self):
        if self.getCarActive():
            return
        self.controlManager.setSpeeds(OTPGlobals.ToonForwardSpeed, OTPGlobals.ToonJumpForce, OTPGlobals.ToonReverseSpeed, OTPGlobals.ToonRotateSpeed)

    def localPresentPie(self, time):
        from toontown.avatar import Emote
        self.__stopPresentPie()
        if self.tossTrack:
            tossTrack = self.tossTrack
            self.tossTrack = None
            tossTrack.finish()
        self.interruptPie()
        self.tossPieStart = time
        self.__pieSequence = self.__pieSequence + 1 & 255
        sequence = self.__pieSequence
        self.__presentingPie = 1
        pos = self.getPos()
        hpr = self.getHpr()
        timestamp32 = globalClockDelta.getFrameNetworkTime(bits=32)
        self.sendUpdate('presentPie', [pos[0],
         pos[1],
         pos[2],
         hpr[0] % 360.0,
         timestamp32])
        Emote.globalEmote.disableBody(self)
        messenger.send('begin-pie')
        ival = self.getPresentPieInterval(pos[0], pos[1], pos[2], hpr[0])
        ival = Sequence(ival, name=self.uniqueName('localPresentPie'))
        self.tossTrack = ival
        ival.start()
        self.makePiePowerMeter()
        self.__piePowerMeter.show()
        self.__piePowerMeterSequence = sequence
        self.__piePowerMeter['value'] = 0
    def __stopPresentPie(self):
        if self.__presentingPie:
            from toontown.avatar import Emote
            Emote.globalEmote.releaseBody(self)
            messenger.send('end-pie')
            self.__presentingPie = 0
        taskName = self.uniqueName('updatePiePower')
        taskMgr.remove(taskName)

    def __getPiePower(self, time):
        elapsed = max(time - self.tossPieStart, 0.0)
        t = elapsed / self.piePowerSpeed
        t = math.pow(t, self.piePowerExponent)
        power = int(t * 100) % 200
        if power > 100:
            power = 200 - power
        return power

    def __updatePiePower(self, task):
        if not self.__piePowerMeter:
            return Task.done
        self.__piePowerMeter['value'] = self.__getPiePower(globalClock.getFrameTime())
        return Task.cont

    def interruptPie(self):
        self.cleanupPieInHand()
        self.__stopPresentPie()
        if self.__piePowerMeter:
            self.__piePowerMeter.hide()
        pie = self.pieTracks.get(self.__pieSequence)
        if pie and pie.getT() < 14.0 / 24.0:
            del self.pieTracks[self.__pieSequence]
            pie.pause()

    def __pieInHand(self):
        pie = self.pieTracks.get(self.__pieSequence)
        return pie and pie.getT() < 15.0 / 24.0

    def __toonMoved(self, isSet):
        if isSet:
            self.interruptPie()

    def localTossPie(self, power):
        if not self.__presentingPie:
            return
        pos = self.getPos()
        hpr = self.getHpr()
        timestamp32 = globalClockDelta.getFrameNetworkTime(bits=32)
        sequence = self.__pieSequence
        if self.tossTrack:
            tossTrack = self.tossTrack
            self.tossTrack = None
            tossTrack.finish()
        if sequence in self.pieTracks:
            pieTrack = self.pieTracks[sequence]
            del self.pieTracks[sequence]
            pieTrack.finish()
        if sequence in self.splatTracks:
            splatTrack = self.splatTracks[sequence]
            del self.splatTracks[sequence]
            splatTrack.finish()
        self.makePiePowerMeter()
        self.__piePowerMeter['value'] = power
        self.__piePowerMeter.show()
        self.__piePowerMeterSequence = sequence
        pieBubble = self.getPieBubble().instanceTo(NodePath())

        def pieFlies(self = self, pos = pos, hpr = hpr, sequence = sequence, power = power, timestamp32 = timestamp32, pieBubble = pieBubble):
            self.sendUpdate('tossPie', [pos[0],
             pos[1],
             pos[2],
             hpr[0] % 360.0,
             sequence,
             power,
             self.pieThrowType,
             timestamp32])
            if self.numPies != ToontownGlobals.FullPies:
                self.setNumPies(self.numPies - 1)
            base.cTrav.addCollider(pieBubble, self.pieHandler)

        toss, pie, flyPie = self.getTossPieInterval(pos[0], pos[1], pos[2], hpr[0], power, self.pieThrowType, beginFlyIval=Func(pieFlies))
        pieBubble.reparentTo(flyPie)
        flyPie.setTag('pieSequence', str(sequence))
        toss = Sequence(toss)
        self.tossTrack = toss
        toss.start()
        pie = Sequence(pie, Func(base.cTrav.removeCollider, pieBubble), Func(self.pieFinishedFlying, sequence))
        self.pieTracks[sequence] = pie
        pie.start()

    def pieFinishedFlying(self, sequence):
        DistributedToon.DistributedToon.pieFinishedFlying(self, sequence)
        if self.__piePowerMeterSequence == sequence:
            self.__piePowerMeter.hide()

    def __finishPieTrack(self, sequence):
        if sequence in self.pieTracks:
            pieTrack = self.pieTracks[sequence]
            del self.pieTracks[sequence]
            pieTrack.finish()

    def __pieHit(self, entry):
        if not entry.hasSurfacePoint() or not entry.hasInto():
            return
        if not entry.getInto().isTangible():
            return
        sequence = int(entry.getFromNodePath().getNetTag('pieSequence'))
        self.__finishPieTrack(sequence)
        if sequence in self.splatTracks:
            splatTrack = self.splatTracks[sequence]
            del self.splatTracks[sequence]
            splatTrack.finish()
        pieCode = 0
        pieCodeStr = entry.getIntoNodePath().getNetTag('pieCode')
        if pieCodeStr:
            pieCode = int(pieCodeStr)
        pos = entry.getSurfacePoint(render)
        timestamp32 = globalClockDelta.getFrameNetworkTime(bits=32)
        self.sendUpdate('pieSplat', [pos[0],
         pos[1],
         pos[2],
         sequence,
         pieCode,
         timestamp32])
        splat = self.getPieSplatInterval(pos[0], pos[1], pos[2], pieCode)
        splat = Sequence(splat, Func(self.pieFinishedSplatting, sequence))
        self.splatTracks[sequence] = splat
        splat.start()
        messenger.send('pieSplat', [self, pieCode])
        messenger.send('localPieSplat', [pieCode, entry])

    def beginAllowPies(self):
        self.allowPies = 1
        self.updatePieButton()

    def endAllowPies(self):
        self.allowPies = 0
        self.updatePieButton()

    def makePiePowerMeter(self):
        from direct.gui.DirectGui import DirectWaitBar, DGG
        if self.__piePowerMeter == None:
            self.__piePowerMeter = DirectWaitBar(frameSize=(-0.2,
             0.2,
             -0.03,
             0.03), relief=DGG.SUNKEN, borderWidth=(0.005, 0.005), barColor=(0.4, 0.6, 1.0, 1), pos=(0, 0.1, 0.8))
            self.__piePowerMeter.hide()

    def updatePieButton(self):
        from toontown.base import ToontownBattleGlobals
        from direct.gui.DirectGui import DirectButton, DGG
        wantButton = 0
        if self.allowPies and self.numPies > 0:
            wantButton = 1
        haveButton = self.__pieButton != None
        if not haveButton and not wantButton:
            return
        if haveButton and not wantButton:
            self.__pieButton.destroy()
            self.__pieButton = None
            self.__pieButtonType = None
            self.__pieButtonCount = None
            return
        if self.__pieButtonType != self.pieType:
            if self.__pieButton:
                self.__pieButton.destroy()
                self.__pieButton = None
        if self.__pieButton == None:
            inv = self.inventory
            if self.pieType >= len(inv.invModels[ToontownBattleGlobals.THROW_TRACK]):
                gui = loader.loadModel('phase_3.5/models/gui/stickerbook_gui')
                pieGui = gui.find('**/summons')
                pieScale = 0.1
            else:
                gui = None
                pieGui = (inv.invModels[ToontownBattleGlobals.THROW_TRACK][self.pieType],)
                pieScale = 0.85
            self.__pieButton = DirectButton(image=(inv.upButton, inv.downButton, inv.rolloverButton), geom=pieGui, text='50', text_scale=0.04, text_align=TextNode.ARight, geom_scale=pieScale, geom_pos=(-0.01, 0, 0), text_fg=Vec4(1, 1, 1, 1), text_pos=(0.07, -0.04), relief=None, image_color=(0, 0.6, 1, 1), pos=(0, 0.1, 0.9))
            self.__pieButton.bind(DGG.B1PRESS, self.__beginTossPieMouse)
            self.__pieButton.bind(DGG.B1RELEASE, self.__endTossPieMouse)
            self.__pieButtonType = self.pieType
            self.__pieButtonCount = None
            if gui:
                del gui
        if self.__pieButtonCount != self.numPies:
            if self.numPies == ToontownGlobals.FullPies:
                self.__pieButton['text'] = ''
            else:
                self.__pieButton['text'] = str(self.numPies)
            self.__pieButtonCount = self.numPies
    
    def displayWhisper(self, fromId, chatString, whisperType):
        LocalAvatar.LocalAvatar.displayWhisper(self, fromId, chatString, whisperType)

    def loadFurnitureGui(self):
        if self.__furnitureGui:
            return
        guiModels = loader.loadModel('phase_5.5/models/gui/house_design_gui')
        self.__furnitureGui = DirectFrame(relief=None, parent=base.a2dTopLeft, pos=(0.115, 0.0, -0.66), scale=0.04, image=guiModels.find('**/attic'))
        DirectLabel(parent=self.__furnitureGui, relief=None, image=guiModels.find('**/rooftile'))
        bMoveStartUp = guiModels.find('**/bu_attic/bu_attic_up')
        bMoveStartDown = guiModels.find('**/bu_attic/bu_attic_down')
        bMoveStartRollover = guiModels.find('**/bu_attic/bu_attic_rollover')
        DirectButton(parent=self.__furnitureGui, relief=None, image=[bMoveStartUp,
         bMoveStartDown,
         bMoveStartRollover,
         bMoveStartUp], text=['', TTLocalizer.HDMoveFurnitureButton, TTLocalizer.HDMoveFurnitureButton], text_fg=(1, 1, 1, 1), text_shadow=(0, 0, 0, 1), text_font=ToontownGlobals.getInterfaceFont(), pos=(-0.3, 0, 9.4), command=self.__startMoveFurniture)
        self.__furnitureGui.hide()
        guiModels.removeNode()

    def showFurnitureGui(self):
        self.loadFurnitureGui()
        self.__furnitureGui.show()

    def hideFurnitureGui(self):
        if self.__furnitureGui:
            self.__furnitureGui.hide()

    def loadClarabelleGui(self):
        if self.__clarabelleButton:
            return
        guiItems = loader.loadModel('phase_5.5/models/gui/catalog_gui')
        circle = guiItems.find('**/cover/blue_circle')
        icon = guiItems.find('**/cover/clarabelle')
        icon.reparentTo(circle)
        rgba = VBase4(0.71589, 0.784547, 0.974, 1.0)
        white = VBase4(1.0, 1.0, 1.0, 1.0)
        icon.setColor(white)
        claraXPos = ClaraBaseXPos
        self.__clarabelleButton = DirectButton(relief=None, image=circle, text='', text_fg=(1, 1, 1, 1), text_shadow=(0, 0, 0, 1), text_scale=0.1, text_pos=(-1.06, 1.06), text_font=ToontownGlobals.getInterfaceFont(), pos=(claraXPos, 1.0, -0.63), scale=0.5, command=self.__handleClarabelleButton)
        self.__clarabelleButton.reparentTo(base.a2dTopRight, DGG.BACKGROUND_SORT_INDEX - 1)
        button = self.__clarabelleButton.stateNodePath[0]
        self.__clarabelleFlash = Sequence(LerpColorInterval(button, 2, white, blendType='easeInOut'), LerpColorInterval(button, 2, rgba, blendType='easeInOut'))
        self.__clarabelleFlash.loop()
        self.__clarabelleFlash.pause()

    def showClarabelleGui(self, mailboxItems):
        self.loadClarabelleGui()
        if mailboxItems:
            self.__clarabelleButton['text'] = ['', TTLocalizer.CatalogNewDeliveryButton, TTLocalizer.CatalogNewDeliveryButton]
        else:
            self.__clarabelleButton['text'] = ['', TTLocalizer.CatalogNewCatalogButton, TTLocalizer.CatalogNewCatalogButton]
        if not self.mailboxNotify and not self.awardNotify and self.catalogNotify == ToontownGlobals.OldItems and (self.simpleMailNotify != ToontownGlobals.NoItems or self.inviteMailNotify != ToontownGlobals.NoItems):
            self.__clarabelleButton['text'] = ['', TTLocalizer.MailNewMailButton, TTLocalizer.MailNewMailButton]
        self.__clarabelleButton.show()
        self.__clarabelleFlash.resume()

    def hideClarabelleGui(self):
        if self.__clarabelleButton:
            self.__clarabelleButton.hide()
            self.__clarabelleFlash.pause()

    def __handleClarabelleButton(self):
        self.stopMoveFurniture()
        place = base.cr.playGame.getPlace()
        if place == None:
            self.notify.warning('Tried to go home, but place is None.')
            return
        if self.__catalogNotifyDialog:
            self.__catalogNotifyDialog.cleanup()
            self.__catalogNotifyDialog = None
        if base.config.GetBool('want-qa-regression', 0):
            self.notify.info('QA-REGRESSION: VISITESTATE: Visit estate')
        place.goHomeNow(self.lastHood)

    def __startMoveFurniture(self):
        self.oldPos = self.getPos()
        if base.config.GetBool('want-qa-regression', 0):
            self.notify.info('QA-REGRESSION: ESTATE:  Furniture Placement')
        if self.cr.furnitureManager != None:
            self.cr.furnitureManager.d_suggestDirector(self.doId)
        elif self.furnitureManager != None:
            self.furnitureManager.d_suggestDirector(self.doId)

    def stopMoveFurniture(self):
        self.controlManager.collisionsOn()
        if self.oldPos:
            self.setPos(self.oldPos)
        if self.furnitureManager != None:
            self.furnitureManager.d_suggestDirector(0)

    def setFurnitureDirector(self, avId, furnitureManager):
        if avId == 0:
            if self.furnitureManager == furnitureManager:
                messenger.send('exitFurnitureMode', [furnitureManager])
                self.furnitureManager = None
                self.furnitureDirector = None
        elif avId != self.doId:
            if self.furnitureManager == None or self.furnitureDirector != avId:
                self.furnitureManager = furnitureManager
                self.furnitureDirector = avId
                messenger.send('enterFurnitureMode', [furnitureManager, 0])
        else:
            if self.furnitureManager != None:
                messenger.send('exitFurnitureMode', [self.furnitureManager])
                self.furnitureManager = None
            self.furnitureManager = furnitureManager
            self.furnitureDirector = avId
            messenger.send('enterFurnitureMode', [furnitureManager, 1])
        self.refreshOnscreenButtons()

    def getAvPosStr(self):
        pos = self.getPos()
        hpr = self.getHpr()
        serverVersion = base.cr.getServerVersion()
        districtName = base.cr.getShardName(base.localAvatar.defaultShard)
        if hasattr(base.cr.playGame.hood, 'loader') and hasattr(base.cr.playGame.hood.loader, 'place') and base.cr.playGame.getPlace() != None:
            zoneId = base.cr.playGame.getPlace().getZoneId()
        else:
            zoneId = '?'
        strPosCoordText = 'X: %.3f' % pos[0] + ', Y: %.3f' % pos[1] + '\nZ: %.3f' % pos[2] + ', H: %.3f' % hpr[0] + '\nZone: %s' % str(zoneId) + ', Ver: %s, ' % serverVersion + 'District: %s' % districtName
        return strPosCoordText
        self.refreshOnscreenButtons()

    def thinkPos(self):
        pos = self.getPos()
        hpr = self.getHpr()
        serverVersion = base.cr.getServerVersion()
        districtName = base.cr.getShardName(base.localAvatar.defaultShard)
        if hasattr(base.cr.playGame.hood, 'loader') and hasattr(base.cr.playGame.hood.loader, 'place') and base.cr.playGame.getPlace() != None:
            zoneId = base.cr.playGame.getPlace().getZoneId()
        else:
            zoneId = '?'
        strPos = '(%.3f' % pos[0] + '\n %.3f' % pos[1] + '\n %.3f)' % pos[2] + '\nH: %.3f' % hpr[0] + '\nZone: %s' % str(zoneId) + ',\nVer: %s, ' % serverVersion + '\nDistrict: %s' % districtName
        print 'Current position=', strPos.replace('\n', ', ')
        self.setChatAbsolute(strPos, CFThought | CFTimeout)

    def __placeMarker(self):
        pos = self.getPos()
        hpr = self.getHpr()
        chest = loader.loadModel('phase_4/models/props/coffin')
        chest.reparentTo(render)
        chest.setColor(1, 0, 0, 1)
        chest.setPosHpr(pos, hpr)
        chest.setScale(0.5)

    def setFriendsListButtonActive(self, active):
        self.friendsListButtonActive = active
        self.refreshOnscreenButtons()

    def obscureFriendsListButton(self, increment):
        self.friendsListButtonObscured += increment
        self.refreshOnscreenButtons()

    def obscureMoveFurnitureButton(self, obscured):
        self.moveFurnitureButtonObscured = obscured
        self.refreshOnscreenButtons()

    def obscureClarabelleButton(self, increment):
        self.clarabelleButtonObscured += increment
        self.refreshOnscreenButtons()

    def refreshOnscreenButtons(self):
        self.bFriendsList.hide()
        self.hideFurnitureGui()
        self.hideClarabelleGui()
        clarabelleHidden = 1
        self.ignore(ToontownGlobals.FriendsListHotkey)
        if self.friendsListButtonActive and self.friendsListButtonObscured <= 0:
            self.bFriendsList.show()
            self.accept(ToontownGlobals.FriendsListHotkey, self.sendFriendsListEvent)
            if self.clarabelleButtonObscured <= 0 and self.isTeleportAllowed():
                if self.catalogNotify == ToontownGlobals.NewItems or self.mailboxNotify == ToontownGlobals.NewItems or self.simpleMailNotify == ToontownGlobals.NewItems or self.inviteMailNotify == ToontownGlobals.NewItems or self.awardNotify == ToontownGlobals.NewItems:
                    showClarabelle = 1
                    for quest in self.quests:
                        if quest[0] in Quests.PreClarabelleQuestIds and self.mailboxNotify != ToontownGlobals.NewItems and self.awardNotify != ToontownGlobals.NewItems:
                            showClarabelle = 0

                    if base.cr.playGame.getPlace().getState() == 'stickerBook':
                        showClarabelle = 0
                    if showClarabelle:
                        newItemsInMailbox = self.mailboxNotify == ToontownGlobals.NewItems or self.awardNotify == ToontownGlobals.NewItems
                        self.showClarabelleGui(newItemsInMailbox)
                        clarabelleHidden = 0
        if clarabelleHidden:
            if self.__catalogNotifyDialog:
                self.__catalogNotifyDialog.cleanup()
                self.__catalogNotifyDialog = None
        else:
            self.newCatalogNotify()
        if self.moveFurnitureButtonObscured:
            if self.__furnitureGui:
                self.__furnitureGui.hide()
        else:
            if self.furnitureManager != None and self.furnitureDirector == self.doId:
                self.loadFurnitureGui()
                self.__furnitureGui.setPos(0.155, -0.6, -1.045)
                self.__furnitureGui.setScale(0.06)
            elif self.cr.furnitureManager != None:
                self.showFurnitureGui()
                if self.__lerpFurnitureButton:
                    self.__lerpFurnitureButton.finish()
                self.__lerpFurnitureButton = self.__furnitureGui.posHprScaleInterval(1.0, pos=Point3(0.115, 0.0, -0.66), hpr=Vec3(0.0, 0.0, 0.0), scale=Vec3(0.04, 0.04, 0.04), blendType='easeInOut', name='lerpFurnitureButton')
                self.__lerpFurnitureButton.start()
        if hasattr(self, 'inEstate') and self.inEstate:
            self.loadGardeningGui()
            self.hideGardeningGui()
        else:
            self.hideGardeningGui()

    def setGhostMode(self, flag):
        if flag == 2:
            self.seeGhosts = 1
        DistributedToon.DistributedToon.setGhostMode(self, flag)

    def newCatalogNotify(self):
        if not self.gotCatalogNotify:
            return
        if not self.friendsListButtonActive or self.friendsListButtonObscured > 0:
            return
        self.gotCatalogNotify = 0
        currentWeek = self.catalogScheduleCurrentWeek - 1
        if currentWeek < 57:
            seriesNumber = currentWeek / ToontownGlobals.CatalogNumWeeksPerSeries + 1
            weekNumber = currentWeek % ToontownGlobals.CatalogNumWeeksPerSeries + 1
        elif currentWeek < 65:
            seriesNumber = 6
            weekNumber = currentWeek - 56
        else:
            seriesNumber = currentWeek / ToontownGlobals.CatalogNumWeeksPerSeries + 2
            weekNumber = currentWeek % ToontownGlobals.CatalogNumWeeksPerSeries + 1
        message = None
        if self.mailboxNotify == ToontownGlobals.NoItems:
            if self.catalogNotify == ToontownGlobals.NewItems:
                if self.catalogScheduleCurrentWeek == 1:
                    message = (TTLocalizer.CatalogNotifyFirstCatalog, TTLocalizer.CatalogNotifyInstructions)
                else:
                    message = (TTLocalizer.CatalogNotifyNewCatalog % weekNumber,)
        elif self.mailboxNotify == ToontownGlobals.NewItems:
            if self.catalogNotify == ToontownGlobals.NewItems:
                message = (TTLocalizer.CatalogNotifyNewCatalogNewDelivery % weekNumber,)
            else:
                message = (TTLocalizer.CatalogNotifyNewDelivery,)
        elif self.mailboxNotify == ToontownGlobals.OldItems:
            if self.catalogNotify == ToontownGlobals.NewItems:
                message = (TTLocalizer.CatalogNotifyNewCatalogOldDelivery % weekNumber,)
            else:
                message = (TTLocalizer.CatalogNotifyOldDelivery,)
        if self.awardNotify == ToontownGlobals.NoItems:
            pass
        elif self.awardNotify == ToontownGlobals.NewItems:
            oldStr = ''
            if message:
                oldStr = message[0] + ' '
            oldStr += TTLocalizer.AwardNotifyNewItems
            message = (oldStr,)
        elif self.awardNotify == ToontownGlobals.OldItems:
            oldStr = ''
            if message:
                oldStr = message[0] + ' '
            oldStr += TTLocalizer.AwardNotifyOldItems
            message = (oldStr,)
        if self.simpleMailNotify == ToontownGlobals.NewItems or self.inviteMailNotify == ToontownGlobals.NewItems:
            oldStr = ''
            if message:
                oldStr = message[0] + ' '
            oldStr += TTLocalizer.MailNotifyNewItems
            message = (oldStr,)
        if message == None:
            return
        if self.__catalogNotifyDialog:
            self.__catalogNotifyDialog.cleanup()
        self.__catalogNotifyDialog = CatalogNotifyDialog.CatalogNotifyDialog(message)
        base.playSfx(self.soundPhoneRing)

    def allowHardLand(self):
        retval = LocalAvatar.LocalAvatar.allowHardLand(self)
        return retval and not self.isDisguised

    def setShovelGuiLevel(self, level = 0):
        pass

    def setWateringCanGuiLevel(self, level = 0):
        pass

    def loadGardeningGui(self):
        if self.__gardeningGui:
            return
        gardenGuiCard = loader.loadModel('phase_5.5/models/gui/planting_gui')
        self.__gardeningGui = DirectFrame(relief=None, parent=base.a2dTopLeft, geom=gardenGuiCard, geom_color=GlobalDialogColor, geom_scale=(0.17, 1.0, 0.3), pos=(0.1335, 0.0, -0.50), scale=1.0)
        self.__gardeningGui.setName('gardeningFrame')
        self.__gardeningGuiFake = DirectFrame(relief=None, parent=base.a2dTopLeft, geom=None, geom_color=GlobalDialogColor, geom_scale=(0.17, 1.0, 0.3), pos=(0.1335, 0.0, -0.50), scale=1.0)
        self.__gardeningGuiFake.setName('gardeningFrameFake')
        iconScale = 1
        iconColorWhite = Vec4(1.0, 1.0, 1.0, 1.0)
        iconColorGrey = Vec4(0.7, 0.7, 0.7, 1.0)
        iconColorBrown = Vec4(0.7, 0.4, 0.3, 1.0)
        iconColorBlue = Vec4(0.2, 0.3, 1.0, 1.0)
        shovelCardP = loader.loadModel('phase_5.5/models/gui/planting_but_shovel_P')
        shovelCardY = loader.loadModel('phase_5.5/models/gui/planting_but_shovel_Y')
        wateringCanCardP = loader.loadModel('phase_5.5/models/gui/planting_but_can_P')
        wateringCanCardY = loader.loadModel('phase_5.5/models/gui/planting_but_can_Y')
        backCard = loader.loadModel('phase_5.5/models/gui/planting_gui')
        iconImage = None
        iconModels = loader.loadModel('phase_3.5/models/gui/sos_textures')
        iconGeom = iconModels.find('**/fish')
        buttonText = TTLocalizer.GardeningPlant
        self.shovelText = ('',
         '',
         buttonText,
         '')
        self.__shovelButtonFake = DirectLabel(parent=self.__gardeningGuiFake, relief=None, text=self.shovelText, text_align=TextNode.ALeft, text_pos=(0.0, -0.0), text_scale=0.07, text_fg=(1, 1, 1, 1), text_shadow=(0, 0, 0, 1), image_scale=(0.18, 1.0, 0.36), geom=None, geom_scale=iconScale, geom_color=iconColorWhite, pos=(0.15, 0, 0.2), scale=0.775)
        self.shovelButtonFake = self.__shovelButtonFake
        self.shovelText = ('',
         '',
         buttonText,
         '')
        self.__shovelButton = DirectButton(parent=self.__gardeningGui, relief=None, text=self.shovelText, text_align=TextNode.ACenter, text_pos=(0.0, -0.0), text_scale=0.1, text_fg=(1, 1, 1, 1), text_shadow=(0, 0, 0, 1), image=(shovelCardP,
         shovelCardY,
         shovelCardY,
         shovelCardY), image_scale=(0.18, 1.0, 0.36), geom=None, geom_scale=iconScale, geom_color=iconColorWhite, pos=(0, 0, 0.2), scale=0.775, command=self.__shovelButtonClicked)
        self.shovelButton = self.__shovelButton
        iconGeom = iconModels.find('**/teleportIcon')
        buttonText = TTLocalizer.GardeningWater
        self.waterText = (buttonText,
         buttonText,
         buttonText,
         '')
        self.__wateringCanButtonFake = DirectLabel(parent=self.__gardeningGuiFake, relief=None, text=self.waterText, text_align=TextNode.ALeft, text_pos=(0.0, -0.0), text_scale=0.07, text_fg=(1, 1, 1, 1), text_shadow=(0, 0, 0, 1), image_scale=(0.18, 1.0, 0.36), geom=None, geom_scale=iconScale, geom_color=iconColorWhite, pos=(0.15, 0, 0.01), scale=0.775)
        self.wateringCanButtonFake = self.__wateringCanButtonFake
        self.__wateringCanButton = DirectButton(parent=self.__gardeningGui, relief=None, text=self.waterText, text_align=TextNode.ACenter, text_pos=(0.0, -0.0), text_scale=0.1, text_fg=(1, 1, 1, 1), text_shadow=(0, 0, 0, 1), image=(wateringCanCardP,
         wateringCanCardY,
         wateringCanCardY,
         wateringCanCardY), image_scale=(0.18, 1.0, 0.36), geom=None, geom_scale=iconScale, geom_color=iconColorWhite, pos=(0, 0, 0.01), scale=0.775, command=self.__wateringCanButtonClicked)
        self.wateringCanButton = self.__wateringCanButton
        self.basketText = '%s / %s' % (self.numFlowers, self.maxFlowerBasket)
        self.basketButton = DirectLabel(parent=self.__gardeningGui, relief=None, text=self.basketText, text_align=TextNode.ALeft, text_pos=(0.82, -1.4), text_scale=0.2, text_fg=(1, 1, 1, 1), text_shadow=(0, 0, 0, 1), image=None, image_scale=iconScale, geom=None, geom_scale=iconScale, geom_color=iconColorWhite, pos=(-0.34, 0, 0.16), scale=0.3, textMayChange=1)
        if hasattr(self, 'shovel'):
            self.setShovelGuiLevel(self.shovel)
        if hasattr(self, 'wateringCan'):
            self.setWateringCanGuiLevel(self.wateringCan)
        self.__shovelButton.hide()
        self.__wateringCanButton.hide()
        self.__shovelButtonFake.hide()
        self.__wateringCanButtonFake.hide()

    def changeButtonText(self, button, text):
        button['text'] = text

    def resetWaterText(self):
        self.wateringCanButton['text'] = self.waterText

    def resetShovelText(self):
        self.shovelButton['text'] = self.holdShovelText

    def showGardeningGui(self):
        self.loadGardeningGui()
        self.__gardeningGui.show()
        base.setCellsAvailable([base.leftCells[2]], 0)

    def hideGardeningGui(self):
        if self.__gardeningGui:
            self.__gardeningGui.hide()
            base.setCellsAvailable([base.leftCells[2]], 1)

    def showShovelButton(self, add = 0):
        if add:
            self.shovelButtonActiveCount += add
        else:
            self.showingShovel = 1
        self.notify.debug('showing shovel %s' % self.shovelButtonActiveCount)
        self.__gardeningGui.show()
        self.__shovelButton.show()

    def hideShovelButton(self, deduct = 0):
        self.shovelButtonActiveCount -= deduct
        if deduct == 0:
            self.showingShovel = 0
        if self.shovelButtonActiveCount < 1:
            self.shovelButtonActiveCount = 0
            if self.showingShovel == 0:
                self.__shovelButton.hide()
            self.handleAllGardeningButtonsHidden()
        self.notify.debug('hiding shovel %s' % self.shovelButtonActiveCount)

    def showWateringCanButton(self, add = 0):
        if add:
            self.wateringCanButtonActiveCount += add
        else:
            self.showingWateringCan = 1
        self.__gardeningGui.show()
        self.__wateringCanButton.show()
        self.basketButton.show()

    def hideWateringCanButton(self, deduct = 0):
        self.wateringCanButtonActiveCount -= deduct
        if deduct == 0:
            self.showingWateringCan = 0
        if self.wateringCanButtonActiveCount < 1:
            wateringCanButtonActiveCount = 0
            if self.showingWateringCan == 0:
                self.__wateringCanButton.hide()
            self.handleAllGardeningButtonsHidden()

    def showWateringCanButtonFake(self, add = 0):
        self.__wateringCanButtonFake.show()

    def hideWateringCanButtonFake(self, deduct = 0):
        self.__wateringCanButtonFake.hide()

    def showShovelButtonFake(self, add = 0):
        self.__shovelButtonFake.show()

    def hideShovelButtonFake(self, deduct = 0):
        self.__shovelButtonFake.hide()

    def levelWater(self, change = 1):
        if change < 0:
            return
        self.showWateringCanButtonFake(1)
        if change < 1:
            changeString = TTLocalizer.GardeningNoSkill
        else:
            changeString = '+%s %s' % (change, TTLocalizer.GardeningWaterSkill)
        self.waterTrack = Sequence(Wait(0.0), Func(self.changeButtonText, self.wateringCanButtonFake, changeString), SoundInterval(globalBattleSoundCache.getSound('GUI_balloon_popup.ogg'), node=self), Wait(1.0), Func(self.hideWateringCanButtonFake, 1))
        self.waterTrack.start()

    def levelShovel(self, change = 1):
        if change < 1:
            return
        self.showShovelButtonFake(1)
        if change < 1:
            changeString = TTLocalizer.GardeningNoSkill
        else:
            changeString = '+%s %s' % (change, TTLocalizer.GardeningShovelSkill)
        plant = base.cr.doId2do.get(self.shovelRelatedDoId)
        if plant:
            self.holdShovelText = plant.getShovelAction()
        self.shovelTrack = Sequence(Wait(0.0), Func(self.changeButtonText, self.shovelButtonFake, changeString), SoundInterval(globalBattleSoundCache.getSound('GUI_balloon_popup.ogg'), node=self), Wait(1.0), Func(self.hideShovelButtonFake, 1))
        self.shovelTrack.start()

    def setGuiConflict(self, con):
        self.guiConflict = con

    def getGuiConflict(self, con):
        return self.guiConflict

    def verboseState(self):
        self.lastPlaceState = 'None'
        taskMgr.add(self.__expressState, 'expressState', extraArgs=[])

    def __expressState(self, task = None):
        place = base.cr.playGame.getPlace()
        if place:
            state = place.fsm.getCurrentState()
            if state.getName() != self.lastPlaceState:
                print 'Place State Change From %s to %s' % (self.lastPlaceState, state.getName())
                self.lastPlaceState = state.getName()
        return Task.cont

    def addShovelRelatedDoId(self, doId):
        if hasattr(base.cr.playGame.getPlace(), 'detectedGardenPlotDone'):
            place = base.cr.playGame.getPlace()
            state = place.fsm.getCurrentState()
            if state.getName() == 'stopped':
                return
        self.touchingPlantList.append(doId)
        self.autoSetActivePlot()

    def removeShovelRelatedDoId(self, doId):
        if doId in self.touchingPlantList:
            self.touchingPlantList.remove(doId)
        self.autoSetActivePlot()

    def autoSetActivePlot(self):
        if self.guiConflict:
            return
        if len(self.touchingPlantList) > 0:
            minDist = 10000
            minDistPlot = 0
            for plot in self.touchingPlantList:
                plant = base.cr.doId2do.get(plot)
                if plant:
                    if self.getDistance(plant) < minDist:
                        minDist = self.getDistance(plant)
                        minDistPlot = plot
                else:
                    self.touchingPlantList.remove(plot)

            if len(self.touchingPlantList) == 0:
                self.setActivePlot(None)
            else:
                self.setActivePlot(minDistPlot)
        else:
            self.setActivePlot(None)
        return

    def setActivePlot(self, doId):
        if not self.gardenStarted:
            return
        self.shovelRelatedDoId = doId
        plant = base.cr.doId2do.get(doId)
        if plant:
            self.startStareAt(plant, Point3(0, 0, 1))
            self.__shovelButton['state'] = DGG.NORMAL
            if not plant.canBePicked():
                self.hideShovelButton()
            else:
                self.showShovelButton()
                self.setShovelAbility(TTLocalizer.GardeningPlant)
                if plant.getShovelAction():
                    self.setShovelAbility(plant.getShovelAction())
                    if plant.getShovelAction() == TTLocalizer.GardeningPick:
                        if not plant.unlockPick():
                            self.__shovelButton['state'] = DGG.DISABLED
                            self.setShovelAbility(TTLocalizer.GardeningFull)
                self.notify.debug('self.shovelRelatedDoId = %d' % self.shovelRelatedDoId)
                if plant.getShovelCommand():
                    self.extraShovelCommand = plant.getShovelCommand()
                    self.__shovelButton['command'] = self.__shovelButtonClicked
            if plant.canBeWatered():
                self.showWateringCanButton()
            else:
                self.hideWateringCanButton()
        else:
            self.stopStareAt()
            self.shovelRelatedDoId = 0
            if self.__shovelButton:
                self.__shovelButton['command'] = None
                self.hideShovelButton()
                self.hideWateringCanButton()
                self.handleAllGardeningButtonsHidden()
                if not self.inGardenAction:
                    if hasattr(base.cr.playGame.getPlace(), 'detectedGardenPlotDone'):
                        place = base.cr.playGame.getPlace()
                        if place:
                            place.detectedGardenPlotDone()
        return

    def setPlantToWater(self, plantId):
        if self.plantToWater == None:
            self.plantToWater = plantId
            self.notify.debug('setting plant to water %s' % plantId)
        return

    def clearPlantToWater(self, plantId):
        if not hasattr(self, 'secondaryPlant'):
            self.secondaryWaterPlant = None
        if self.plantToWater == plantId:
            self.plantToWater = None
            self.hideWateringCanButton()
        return

    def hasPlant(self):
        if self.plantToWater != None:
            return 1
        else:
            return 0
        return

    def handleAllGardeningButtonsHidden(self):
        somethingVisible = False
        if not self.__shovelButton.isHidden():
            somethingVisible = True
        if not self.__wateringCanButton.isHidden():
            somethingVisible = True
        if not somethingVisible:
            self.hideGardeningGui()

    def setShovelAbility(self, ability):
        self.shovelAbility = ability
        if self.__shovelButton:
            self.__shovelButton['text'] = ability

    def setFlowerBasket(self, speciesList, varietyList):
        DistributedToon.DistributedToon.setFlowerBasket(self, speciesList, varietyList)
        self.numFlowers = len(self.flowerBasket.flowerList)
        self.maxFlowerBasket
        if hasattr(self, 'basketButton'):
            self.basketText = '%s / %s' % (self.numFlowers, self.maxFlowerBasket)
            self.basketButton['text'] = self.basketText

    def setShovelSkill(self, skillLevel):
        if hasattr(self, 'shovelSkill') and hasattr(self, 'shovelButton'):
            if self.shovelSkill != None:
                self.levelShovel(skillLevel - self.shovelSkill)
        oldShovelSkill = self.shovelSkill
        DistributedToon.DistributedToon.setShovelSkill(self, skillLevel)
        if hasattr(self, 'shovel'):
            oldShovelPower = GardenGlobals.getShovelPower(self.shovel, oldShovelSkill)
            newShovelPower = GardenGlobals.getShovelPower(self.shovel, self.shovelSkill)
            almostMaxedSkill = GardenGlobals.ShovelAttributes[GardenGlobals.MAX_SHOVELS - 1]['skillPts'] - 2
            if skillLevel >= GardenGlobals.ShovelAttributes[self.shovel]['skillPts']:
                self.promoteShovel()
            elif oldShovelSkill and oldShovelPower < newShovelPower:
                self.promoteShovelSkill(self.shovel, self.shovelSkill)
            elif oldShovelSkill == almostMaxedSkill and newShovelPower == GardenGlobals.getNumberOfShovelBoxes():
                self.promoteShovelSkill(self.shovel, self.shovelSkill)
        return

    def setWateringCanSkill(self, skillLevel):
        skillDelta = skillLevel - self.wateringCanSkill
        if skillDelta or 1:
            if hasattr(self, 'wateringCanSkill') and hasattr(self, 'wateringCanButton'):
                if self.wateringCanSkill != None:
                    self.levelWater(skillDelta)
            DistributedToon.DistributedToon.setWateringCanSkill(self, skillLevel)
            if hasattr(self, 'wateringCan'):
                if skillLevel >= GardenGlobals.WateringCanAttributes[self.wateringCan]['skillPts']:
                    self.promoteWateringCan()
        return

    def unlockGardeningButtons(self, task = None):
        if hasattr(self, '_LocalToon__shovelButton'):
            try:
                self.__shovelButton['state'] = DGG.NORMAL
            except TypeError:
                self.notify.warning('Could not unlock the shovel button- Type Error')

        if hasattr(self, '_LocalToon__wateringCanButton'):
            try:
                self.__wateringCanButton['state'] = DGG.NORMAL
            except TypeError:
                self.notify.warning('Could not unlock the watering can button - Type Error')

        taskMgr.remove('unlockGardenButtons')
        return None

    def lockGardeningButtons(self, task = None):
        if hasattr(self, '_LocalToon__shovelButton'):
            try:
                self.__shovelButton['state'] = DGG.DISABLED
            except TypeError:
                self.notify.warning('Could not lock the shovel button- Type Error')

        if hasattr(self, '_LocalToon__wateringCanButton'):
            try:
                self.__wateringCanButton['state'] = DGG.DISABLED
            except TypeError:
                self.notify.warning('Could not lock the watering can button - Type Error')

        self.accept('endPlantInteraction', self.__handleEndPlantInteraction)
        return None

    def reactivateShovel(self, task = None):
        if hasattr(self, '_LocalToon__shovelButton'):
            self.__shovelButton['state'] = DGG.NORMAL
        taskMgr.remove('reactShovel')
        return None

    def reactivateWater(self, task = None):
        if hasattr(self, '_LocalToon__wateringCanButton'):
            self.__wateringCanButton['state'] = DGG.NORMAL
        taskMgr.remove('reactWater')
        return None

    def handleEndPlantInteraction(self, object = None, replacement = 0):
        if not replacement:
            self.setInGardenAction(None, object)
            self.autoSetActivePlot()
        return

    def __handleEndPlantInteraction(self, task = None):
        self.setInGardenAction(None)
        self.autoSetActivePlot()
        return

    def promoteShovelSkill(self, shovelLevel, shovelSkill):
        shovelName = GardenGlobals.ShovelAttributes[shovelLevel]['name']
        shovelBeans = GardenGlobals.getShovelPower(shovelLevel, shovelSkill)
        oldShovelBeans = GardenGlobals.getShovelPower(shovelLevel, shovelSkill - 1)
        doPartyBall = False
        message = TTLocalizer.GardenShovelSkillLevelUp % {'shovel': shovelName,
         'oldbeans': oldShovelBeans,
         'newbeans': shovelBeans}
        if shovelBeans == GardenGlobals.getNumberOfShovelBoxes():
            if shovelSkill == GardenGlobals.ShovelAttributes[shovelLevel]['skillPts'] - 1:
                doPartyBall = True
                message = TTLocalizer.GardenShovelSkillMaxed % {'shovel': shovelName,
                 'oldbeans': oldShovelBeans,
                 'newbeans': shovelBeans}
        messagePos = Vec2(0, 0.2)
        messageScale = 0.07
        image = loader.loadModel('phase_5.5/models/gui/planting_but_shovel_P')
        imagePos = Vec3(0, 0, -0.13)
        imageScale = Vec3(0.28, 0, 0.56)
        if doPartyBall:
            go = Fanfare.makeFanfareWithMessageImage(0, base.localAvatar, 1, message, Vec2(0, 0.2), 0.08, image, Vec3(0, 0, -0.1), Vec3(0.35, 0, 0.7), wordwrap=23)
            Sequence(go[0], Func(go[1].show), LerpColorScaleInterval(go[1], duration=0.5, startColorScale=Vec4(1, 1, 1, 0), colorScale=Vec4(1, 1, 1, 1)), Wait(10), LerpColorScaleInterval(go[1], duration=0.5, startColorScale=Vec4(1, 1, 1, 1), colorScale=Vec4(1, 1, 1, 0)), Func(go[1].remove)).start()
        else:
            go = Fanfare.makePanel(base.localAvatar, 1)
            Fanfare.makeMessageBox(go, message, messagePos, messageScale, wordwrap=24)
            Fanfare.makeImageBox(go.itemFrame, image, imagePos, imageScale)
            Sequence(Func(go.show), LerpColorScaleInterval(go, duration=0.5, startColorScale=Vec4(1, 1, 1, 0), colorScale=Vec4(1, 1, 1, 1)), Wait(10), LerpColorScaleInterval(go, duration=0.5, startColorScale=Vec4(1, 1, 1, 1), colorScale=Vec4(1, 1, 1, 0)), Func(go.remove)).start()

    def promoteShovel(self, shovelLevel = 0):
        shovelName = GardenGlobals.ShovelAttributes[shovelLevel]['name']
        shovelBeans = GardenGlobals.getShovelPower(shovelLevel, 0)
        message = TTLocalizer.GardenShovelLevelUp % {'shovel': shovelName,
         'oldbeans': shovelBeans - 1,
         'newbeans': shovelBeans}
        messagePos = Vec2(0, 0.2)
        messageScale = 0.07
        image = loader.loadModel('phase_5.5/models/gui/planting_but_shovel_P')
        imagePos = Vec3(0, 0, -0.13)
        imageScale = Vec3(0.28, 0, 0.56)
        go = Fanfare.makePanel(base.localAvatar, 1)
        Fanfare.makeMessageBox(go, message, messagePos, messageScale, wordwrap=24)
        Fanfare.makeImageBox(go.itemFrame, image, imagePos, imageScale)
        Sequence(Func(go.show), LerpColorScaleInterval(go, duration=0.5, startColorScale=Vec4(1, 1, 1, 0), colorScale=Vec4(1, 1, 1, 1)), Wait(10), LerpColorScaleInterval(go, duration=0.5, startColorScale=Vec4(1, 1, 1, 1), colorScale=Vec4(1, 1, 1, 0)), Func(go.remove)).start()

    def promoteWateringCan(self, wateringCanlevel = 0):
        message = TTLocalizer.GardenWateringCanLevelUp + ' \n' + GardenGlobals.WateringCanAttributes[wateringCanlevel]['name']
        messagePos = Vec2(0, 0.2)
        messageScale = 0.08
        image = loader.loadModel('phase_5.5/models/gui/planting_but_can_P')
        imagePos = Vec3(0, 0, -0.1)
        imageScale = Vec3(0.35, 0, 0.7)
        if wateringCanlevel >= GardenGlobals.MAX_WATERING_CANS - 1:
            go = Fanfare.makeFanfareWithMessageImage(0, base.localAvatar, 1, message, Vec2(0, 0.2), 0.08, image, Vec3(0, 0, -0.1), Vec3(0.35, 0, 0.7))
            Sequence(go[0], Func(go[1].show), LerpColorScaleInterval(go[1], duration=0.5, startColorScale=Vec4(1, 1, 1, 0), colorScale=Vec4(1, 1, 1, 1)), Wait(5), LerpColorScaleInterval(go[1], duration=0.5, startColorScale=Vec4(1, 1, 1, 1), colorScale=Vec4(1, 1, 1, 0)), Func(go[1].remove)).start()
        else:
            go = Fanfare.makePanel(base.localAvatar, 1)
            Fanfare.makeMessageBox(go, message, messagePos, messageScale)
            Fanfare.makeImageBox(go.itemFrame, image, imagePos, imageScale)
            Sequence(Func(go.show), LerpColorScaleInterval(go, duration=0.5, startColorScale=Vec4(1, 1, 1, 0), colorScale=Vec4(1, 1, 1, 1)), Wait(5), LerpColorScaleInterval(go, duration=0.5, startColorScale=Vec4(1, 1, 1, 1), colorScale=Vec4(1, 1, 1, 0)), Func(go.remove)).start()

    def setInGardenAction(self, actionObject, fromObject = None):
        if actionObject:
            self.lockGardeningButtons()
        elif fromObject:
            self.unlockGardeningButtons()
        else:
            self.unlockGardeningButtons()
        self.inGardenAction = actionObject

    def __wateringCanButtonClicked(self):
        self.notify.debug('wateringCanButtonClicked')
        if self.inGardenAction:
            return
        plant = base.cr.doId2do.get(self.shovelRelatedDoId)
        if plant:
            if hasattr(plant, 'handleWatering'):
                plant.handleWatering()
        messenger.send('wakeup')

    def __shovelButtonClicked(self):
        if self.inGardenAction:
            return
        self.notify.debug('shovelButtonClicked')
        messenger.send('wakeup')
        thingId = self.shovelRelatedDoId
        thing = base.cr.doId2do.get(thingId)
        if hasattr(self, 'extraShovelCommand'):
            self.extraShovelCommand()
            self.setActivePlot(thingId)

    def setShovel(self, shovelId):
        DistributedToon.DistributedToon.setShovel(self, shovelId)
        if self.__gardeningGui:
            self.setShovelGuiLevel(shovelId)

    def setWateringCan(self, wateringCanId):
        DistributedToon.DistributedToon.setWateringCan(self, wateringCanId)
        if self.__gardeningGui:
            self.setWateringCanGuiLevel(wateringCanId)

    def setGardenStarted(self, bStarted):
        self.gardenStarted = bStarted
        if self.gardenStarted and not self.gardenPage and hasattr(self, 'book'):
            self.loadGardenPages()

    def b_setAnimState(self, animName, animMultiplier = 1.0, callback = None, extraArgs = []):
        if self.wantStatePrint:
            print 'Local Toon Anim State %s' % animName
        DistributedToon.DistributedToon.b_setAnimState(self, animName, animMultiplier, callback, extraArgs)

    def __handleSwimExitTeleport(self, requestStatus):
        self.notify.info('closing shard...')
        base.cr.gameFSM.request('closeShard', ['afkTimeout'])

    def addGolfPage(self):
        if self.hasPlayedGolf():
            if hasattr(self, 'golfPage') and self.golfPage != None:
                return
            self.golfPage = GolfPage.GolfPage()
            self.golfPage.setAvatar(self)
            self.golfPage.load()
            self.book.addPage(self.golfPage, pageName=TTLocalizer.GolfPageTitle)
        return

    def addEventsPage(self):
        if hasattr(self, 'eventsPage') and self.eventsPage != None:
            return
        self.eventsPage = EventsPage.EventsPage()
        self.eventsPage.load()
        self.book.addPage(self.eventsPage, pageName=TTLocalizer.EventsPageName)
        return

    def setSpecialInventory(self, specialInventory):
        DistributedToon.DistributedToon.setSpecialInventory(self, specialInventory)
        self.inventory.updateTotalPropsText()

    def hasActiveBoardingGroup(self):
        if hasattr(localAvatar, 'boardingParty') and localAvatar.boardingParty:
            return localAvatar.boardingParty.hasActiveGroup(localAvatar.doId)
        else:
            return False

    def getZoneId(self):
        return self._zoneId

    def setZoneId(self, value):
        if value == -1:
            self.notify.error('zoneId should not be set to -1, tell Redmond')
        self._zoneId = value

    zoneId = property(getZoneId, setZoneId)

    def systemWarning(self, warningText = 'Acknowledge this system message.'):
        self.createSystemMsgAckGui()
        self.systemMsgAckGui['text'] = warningText
        self.systemMsgAckGui.show()

    def createSystemMsgAckGui(self):
        if self.systemMsgAckGui == None or self.systemMsgAckGui.isEmpty():
            message = 'o' * 100
            self.systemMsgAckGui = TTDialog.TTGlobalDialog(doneEvent=self.systemMsgAckGuiDoneEvent, message=message, style=TTDialog.Acknowledge)
            self.systemMsgAckGui.hide()
        return

    def hideSystemMsgAckGui(self):
        if self.systemMsgAckGui != None and not self.systemMsgAckGui.isEmpty():
            self.systemMsgAckGui.hide()
        return

    def setSleepAutoReply(self, fromId):
        av = base.cr.identifyAvatar(fromId)
        if isinstance(av, (DistributedToon.DistributedToon, FriendHandle)):
            base.localAvatar.setSystemMessage(0, TTLocalizer.SleepAutoReply % av.getName(), WTToontownBoardingGroup)
        elif av:
            self.notify.warning('setSleepAutoReply from non-toon %s' % fromId)

    def cheatCogdoMazeGame(self, kindOfCheat = 0):
        if base.config.GetBool('allow-cogdo-maze-suit-hit-cheat'):
            maze = base.cr.doFind('DistCogdoMazeGame')
            if maze:
                if kindOfCheat == 0:
                    for suitNum in maze.game.suitsById.keys():
                        suit = maze.game.suitsById[suitNum]
                        maze.sendUpdate('requestSuitHitByGag', [suit.type, suitNum])

                elif kindOfCheat == 1:
                    for joke in maze.game.pickups:
                        maze.sendUpdate('requestPickUp', [joke.serialNum])

        else:
            self.sendUpdate('logSuspiciousEvent', ['cheatCogdoMazeGame'])

    def doTeleportResponse(self, fromAvatar, toAvatar, avId, available, shardId, hoodId, zoneId, sendToId):
        self.d_teleportResponse(avId, available, shardId, hoodId, zoneId, sendToId)

    def startQuestMap(self):
        if self.questMap:
            self.questMap.start()

    def stopQuestMap(self):
        if self.questMap:
            self.questMap.stop()

    def getPetId(self):
        return self.petId

    def hasPet(self):
        return self.petId != 0

    def getPetDNA(self):
        if self.hasPet():
            pet = base.cr.identifyFriend(self.petId)
            return pet.style if pet else None
        return None

    def setPetId(self, petId):
        self.petId = petId
        if self.isLocal():
            base.cr.addPetToFriendsMap()

    def startAprilToonsControls(self):
        self.controlManager.currentControls.setGravity(ToontownGlobals.GravityValue * 0.75)

    def stopAprilToonsControls(self):
        self.controlManager.currentControls.setGravity(ToontownGlobals.GravityValue * 2.0)
