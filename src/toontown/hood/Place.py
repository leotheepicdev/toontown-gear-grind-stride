from panda3d.core import Camera, NodePath
from toontown.base.ToonBaseGlobal import *
from direct.directnotify import DirectNotifyGlobal
from direct.fsm import StateData
from toontown.base.PythonUtil import PriorityCallbacks
from toontown.safezone import PublicWalk
import ZoneUtil
from toontown.friends import FriendsListManager
from toontown.base import ToontownGlobals
from toontown.toon.Toon import teleportDebug
from toontown.estate import HouseGlobals
from toontown.base import TTLocalizer
from otp.otpbase import OTPLocalizer
from toontown.avatar import Emote
from toontown.avatar.Avatar import teleportNotify
from direct.task import Task
import QuietZoneState
from toontown.distributed import ToontownDistrictStats

class Place(StateData.StateData, FriendsListManager.FriendsListManager):
    notify = DirectNotifyGlobal.directNotify.newCategory('Place')

    def __init__(self, loader, doneEvent):
        StateData.StateData.__init__(self, doneEvent)
        FriendsListManager.FriendsListManager.__init__(self)
        self.loader = loader
        self.zoneId = None
        self._tiToken = None
        self._leftQuietZoneLocalCallbacks = PriorityCallbacks()
        self._leftQuietZoneSubframeCall = None
        self._setZoneCompleteLocalCallbacks = PriorityCallbacks()
        self._setZoneCompleteSubframeCall = None

    def load(self):
        StateData.StateData.load(self)
        FriendsListManager.FriendsListManager.load(self)
        self.walkDoneEvent = 'walkDone'
        self.walkStateData = PublicWalk.PublicWalk(self.fsm, self.walkDoneEvent)
        self.walkStateData.load()
        self._tempFSM = self.fsm

    def unload(self):
        StateData.StateData.unload(self)
        FriendsListManager.FriendsListManager.unload(self)
        self.notify.info('Unloading Place (%s). Fsm in %s' % (self.zoneId, self._tempFSM.getCurrentState().getName()))
        if self._leftQuietZoneSubframeCall:
            self._leftQuietZoneSubframeCall.cleanup()
            self._leftQuietZoneSubframeCall = None
        if self._setZoneCompleteSubframeCall:
            self._setZoneCompleteSubframeCall.cleanup()
            self._setZoneCompleteSubframeCall = None
        self._leftQuietZoneLocalCallbacks = None
        self._setZoneCompleteLocalCallbacks = None
        del self._tempFSM
        taskMgr.remove('goHomeFailed')
        del self.walkDoneEvent
        self.walkStateData.unload()
        del self.walkStateData
        del self.loader

    def _getQZState(self):
        if hasattr(base, 'cr') and hasattr(base.cr, 'playGame'):
            if hasattr(base.cr.playGame, 'quietZoneStateData') and base.cr.playGame.quietZoneStateData:
                return base.cr.playGame.quietZoneStateData
        return None

    def addLeftQuietZoneCallback(self, callback, priority = None):
        qzsd = self._getQZState()
        if qzsd:
            return qzsd.addLeftQuietZoneCallback(callback, priority)
        else:
            token = self._leftQuietZoneLocalCallbacks.add(callback, priority=priority)
            if not self._leftQuietZoneSubframeCall:
                self._leftQuietZoneSubframeCall = SubframeCall(self._doLeftQuietZoneCallbacks, taskMgr.getCurrentTask().getPriority() - 1)
            return token

    def removeLeftQuietZoneCallback(self, token):
        if token is not None:
            if token in self._leftQuietZoneLocalCallbacks:
                self._leftQuietZoneLocalCallbacks.remove(token)
            qzsd = self._getQZState()
            if qzsd:
                qzsd.removeLeftQuietZoneCallback(token)

    def _doLeftQuietZoneCallbacks(self):
        self._leftQuietZoneLocalCallbacks()
        self._leftQuietZoneLocalCallbacks.clear()
        self._leftQuietZoneSubframeCall = None

    def addSetZoneCompleteCallback(self, callback, priority = None):
        qzsd = self._getQZState()
        if qzsd:
            return qzsd.addSetZoneCompleteCallback(callback, priority)
        else:
            token = self._setZoneCompleteLocalCallbacks.add(callback, priority=priority)
            if not self._setZoneCompleteSubframeCall:
                self._setZoneCompleteSubframeCall = SubframeCall(self._doSetZoneCompleteLocalCallbacks, taskMgr.getCurrentTask().getPriority() - 1)
            return token

    def removeSetZoneCompleteCallback(self, token):
        if token is not None:
            if any(token==x[1] for x in self._setZoneCompleteLocalCallbacks._callbacks):
                self._setZoneCompleteLocalCallbacks.remove(token)
            qzsd = self._getQZState()
            if qzsd:
                qzsd.removeSetZoneCompleteCallback(token)

    def _doSetZoneCompleteLocalCallbacks(self):
        self._setZoneCompleteSubframeCall = None
        localCallbacks = self._setZoneCompleteLocalCallbacks
        self._setZoneCompleteLocalCallbacks()
        localCallbacks.clear()

    def setState(self, state):
        if hasattr(self, 'fsm'):
            curState = self.fsm.getName()
            if state == 'pet' or curState == 'pet':
                self.preserveFriendsList()
            self.fsm.request(state)

    def getState(self):
        if hasattr(self, 'fsm'):
            curState = self.fsm.getCurrentState().getName()
            return curState

    def getZoneId(self):
        return self.zoneId

    def getTaskZoneId(self):
        return self.getZoneId()

    def handleTeleportQuery(self, fromAvatar, toAvatar):
        if toAvatar == localAvatar:
            toAvatar.doTeleportResponse(fromAvatar, toAvatar, toAvatar.doId, 1, toAvatar.defaultShard, base.cr.playGame.getPlaceId(), self.getZoneId(), fromAvatar.doId)
        else:
            self.notify.warning('handleTeleportQuery toAvatar.doId != localAvatar.doId' % (toAvatar.doId, localAvatar.doId))

    def detectedPhoneCollision(self):
        self.fsm.request('phone')

    def detectedFishingCollision(self):
        self.fsm.request('fishing')

    def enterStart(self):
        pass

    def exitStart(self):
        pass

    def enterFinal(self):
        pass

    def exitFinal(self):
        pass

    def enterWalk(self, teleportIn = 0):
        self.enterFLM()
        self.walkStateData.enter()
        if teleportIn == 0:
            self.walkStateData.fsm.request('walking')
        self.acceptOnce(self.walkDoneEvent, self.handleWalkDone)
        self.accept('teleportQuery', self.handleTeleportQuery)
        base.localAvatar.setTeleportAvailable(1)
        base.localAvatar.questPage.acceptOnscreenHooks()
        base.localAvatar.invPage.acceptOnscreenHooks()
        base.localAvatar.questMap.acceptOnscreenHooks()
        base.localAvatar.acceptOnscreenHooks()
        self.walkStateData.fsm.request('walking')

    def exitWalk(self):
        self.exitFLM()
        messenger.send('wakeup')
        self.walkStateData.exit()
        self.ignore(self.walkDoneEvent)
        base.localAvatar.setTeleportAvailable(0)
        self.ignore('teleportQuery')
        if base.cr.playGame.hood != None:
            base.cr.playGame.hood.hideTitleText()
        base.localAvatar.questPage.hideQuestsOnscreen()
        base.localAvatar.questPage.ignoreOnscreenHooks()
        base.localAvatar.invPage.ignoreOnscreenHooks()
        base.localAvatar.invPage.hideInventoryOnscreen()
        base.localAvatar.ignoreOnscreenHooks()
        base.localAvatar.questMap.hide()
        base.localAvatar.questMap.ignoreOnscreenHooks()

    def handleWalkDone(self, doneStatus):
        mode = doneStatus['mode']
        if mode == 'StickerBook':
            self.last = self.fsm.getCurrentState().getName()
            self.fsm.request('stickerBook')
        elif mode == 'Options':
            self.last = self.fsm.getCurrentState().getName()
            self.fsm.request('stickerBook', [base.localAvatar.optionsPage])
        elif mode == 'Sit':
            self.last = self.fsm.getCurrentState().getName()
            self.fsm.request('sit')
        else:
            Place.notify.error('Invalid mode: %s' % mode)

    def enterSit(self):
        self.enterFLM()
        base.localAvatar.laffMeter.start()
        self.accept('teleportQuery', self.handleTeleportQuery)
        base.localAvatar.setTeleportAvailable(1)
        base.localAvatar.b_setAnimState('SitStart', 1)
        self.accept(base.getKey('MOVE_UP'), self.fsm.request, extraArgs=['walk'])

    def exitSit(self):
        self.exitFLM()
        base.localAvatar.laffMeter.stop()
        base.localAvatar.setTeleportAvailable(0)
        self.ignore('teleportQuery')
        self.ignore(base.getKey('MOVE_UP'))

    def enterDrive(self):
        self.enterFLM()
        base.localAvatar.laffMeter.start()
        self.accept('teleportQuery', self.handleTeleportQuery)
        base.localAvatar.setTeleportAvailable(1)
        base.localAvatar.b_setAnimState('SitStart', 1)

    def exitDrive(self):
        self.exitFLM()
        base.localAvatar.laffMeter.stop()
        base.localAvatar.setTeleportAvailable(0)
        self.ignore('teleportQuery')

    def enterPush(self):
        self.enterFLM()
        base.localAvatar.laffMeter.start()
        self.accept('teleportQuery', self.handleTeleportQuery)
        base.localAvatar.setTeleportAvailable(1)
        base.localAvatar.attachCamera()
        base.localAvatar.startUpdateSmartCamera()
        base.localAvatar.startPosHprBroadcast()
        base.localAvatar.b_setAnimState('Push', 1)

    def exitPush(self):
        self.exitFLM()
        base.localAvatar.laffMeter.stop()
        base.localAvatar.setTeleportAvailable(0)
        base.localAvatar.stopUpdateSmartCamera()
        base.localAvatar.detachCamera()
        base.localAvatar.stopPosHprBroadcast()
        self.ignore('teleportQuery')

    def enterStickerBook(self, page = None):
        self.enterFLM()
        base.localAvatar.laffMeter.start()
        target = base.cr.doFind('DistributedTarget')
        if target:
            target.hideGui()
        self.accept('teleportQuery', self.handleTeleportQuery)
        base.localAvatar.setTeleportAvailable(1)
        if page:
            base.localAvatar.book.setPage(page)
        base.localAvatar.b_setAnimState('OpenBook', 1, self.enterStickerBookGUI)
        base.localAvatar.obscureMoveFurnitureButton(1)

    def enterStickerBookGUI(self):
        base.localAvatar.collisionsOn()
        base.localAvatar.book.showButton()
        base.localAvatar.book.enter()
        base.localAvatar.setGuiConflict(1)
        base.localAvatar.startSleepWatch(self.__handleFallingAsleep)
        self.accept('bookDone', self.__handleBook)
        base.localAvatar.b_setAnimState('ReadBook', 1)

    def __handleFallingAsleep(self, task):
        base.localAvatar.book.exit()
        base.localAvatar.b_setAnimState('CloseBook', 1, callback=self.__handleFallingAsleepBookClose)
        return Task.done

    def __handleFallingAsleepBookClose(self):
        if hasattr(self, 'fsm'):
            self.fsm.request('walk')
        base.localAvatar.forceGotoSleep()

    def exitStickerBook(self):
        base.localAvatar.stopSleepWatch()
        self.exitFLM()
        base.localAvatar.laffMeter.stop()
        base.localAvatar.setGuiConflict(0)
        base.localAvatar.book.exit()
        base.localAvatar.book.hideButton()
        base.localAvatar.collisionsOff()
        self.ignore('bookDone')
        base.localAvatar.setTeleportAvailable(0)
        self.ignore('teleportQuery')
        base.localAvatar.obscureMoveFurnitureButton(0)
        target = base.cr.doFind('DistributedTarget')
        if target:
            target.showGui()

    def __handleBook(self):
        base.localAvatar.stopSleepWatch()
        base.localAvatar.book.exit()
        bookStatus = base.localAvatar.book.getDoneStatus()
        if bookStatus['mode'] == 'close':
            base.localAvatar.b_setAnimState('CloseBook', 1, callback=self.handleBookClose)
        elif bookStatus['mode'] == 'teleport':
            zoneId = bookStatus['hood']
            base.localAvatar.collisionsOff()
            base.localAvatar.b_setAnimState('CloseBook', 1, callback=self.handleBookCloseTeleport, extraArgs=[zoneId, zoneId])
        elif bookStatus['mode'] == 'exit':
            self.exitTo = bookStatus.get('exitTo')
            base.localAvatar.collisionsOff()
            base.localAvatar.b_setAnimState('CloseBook', 1, callback=self.__handleBookCloseExit)
        elif bookStatus['mode'] == 'gohome':
            zoneId = bookStatus['hood']
            base.localAvatar.collisionsOff()
            base.localAvatar.b_setAnimState('CloseBook', 1, callback=self.goHomeNow, extraArgs=[zoneId])
        elif bookStatus['mode'] == 'startparty':
            firstStart = bookStatus['firstStart']
            hostId = bookStatus['hostId']
            base.localAvatar.collisionsOff()
            base.localAvatar.b_setAnimState('CloseBook', 1, callback=self.startPartyNow, extraArgs=[firstStart, hostId])

    def handleBookCloseTeleport(self, hoodId, zoneId):
        if localAvatar.hasActiveBoardingGroup():
            rejectText = TTLocalizer.BoardingCannotLeaveZone
            localAvatar.elevatorNotifier.showMe(rejectText)
            return
        self.requestLeave({'loader': ZoneUtil.getBranchLoaderName(zoneId),
         'where': ZoneUtil.getToonWhereName(zoneId),
         'how': 'teleportIn',
         'hoodId': hoodId,
         'zoneId': zoneId,
         'shardId': None,
         'avId': -1})

    def __handleBookCloseExit(self):
        base.localAvatar.b_setAnimState('TeleportOut', 1, self.__handleBookExitTeleport, [0])

    def __handleBookExitTeleport(self, requestStatus):
        if base.cr.timeManager:
            base.cr.timeManager.setDisconnectReason(ToontownGlobals.DisconnectBookExit)
        base.transitions.fadeScreen(1.0)
        base.cr.gameFSM.request(self.exitTo)

    def goHomeNow(self, curZoneId):
        if localAvatar.hasActiveBoardingGroup():
            rejectText = TTLocalizer.BoardingCannotLeaveZone
            localAvatar.elevatorNotifier.showMe(rejectText)
            return
        hoodId = ToontownGlobals.MyEstate
        self.requestLeave({'loader': 'safeZoneLoader',
         'where': 'estate',
         'how': 'teleportIn',
         'hoodId': hoodId,
         'zoneId': -1,
         'shardId': None,
         'avId': -1})

    def startPartyNow(self, firstStart, hostId):
        if localAvatar.hasActiveBoardingGroup():
            rejectText = TTLocalizer.BoardingCannotLeaveZone
            localAvatar.elevatorNotifier.showMe(rejectText)
            return
        base.localAvatar.creatingNewPartyWithMagicWord = False
        base.localAvatar.aboutToPlanParty = False
        hoodId = ToontownGlobals.PartyHood
        if firstStart:
            zoneId = 0
            ToontownDistrictStats.refresh('shardInfoUpdated')
            curShardTuples = base.cr.listActiveShards()
            lowestPop = 100000000000000000L
            shardId = None
            for shardInfo in curShardTuples:
                pop = shardInfo[2]
                if pop < lowestPop:
                    lowestPop = pop
                    shardId = shardInfo[0]

            if shardId == base.localAvatar.defaultShard:
                shardId = None
            base.cr.playGame.getPlace().requestLeave({'loader': 'safeZoneLoader',
             'where': 'party',
             'how': 'teleportIn',
             'hoodId': hoodId,
             'zoneId': zoneId,
             'shardId': None, # ALPHA BANDAGE: should be shardId, but this causes the AI it teleports to to die right now.
             'avId': -1})
        else:
            if hostId is None:
                hostId = base.localAvatar.doId
            base.cr.partyManager.sendAvatarToParty(hostId)
            return

    def handleBookClose(self):
        if hasattr(self, 'fsm'):
            self.fsm.request('walk')
        if hasattr(self, 'toonSubmerged') and self.toonSubmerged == 1:
            if hasattr(self, 'walkStateData'):
                self.walkStateData.fsm.request('swimming', [self.loader.swimSound])

    def requestLeave(self, requestStatus):
        teleportDebug(requestStatus, 'requestLeave(%s)' % (requestStatus,))
        if hasattr(self, 'fsm'):
            self.doRequestLeave(requestStatus)

    def handleEnterTunnel(self, requestStatus, collEntry):
        if localAvatar.hasActiveBoardingGroup():
            rejectText = TTLocalizer.BoardingCannotLeaveZone
            localAvatar.elevatorNotifier.showMe(rejectText)
            dummyNP = NodePath('dummyNP')
            dummyNP.reparentTo(render)
            tunnelOrigin = requestStatus['tunnelOrigin']
            dummyNP.setPos(localAvatar.getPos())
            dummyNP.setH(tunnelOrigin.getH())
            dummyNP.setPos(dummyNP, 0, 4, 0)
            localAvatar.setPos(dummyNP.getPos())
            dummyNP.removeNode()
            del dummyNP
            return
        self.requestLeave(requestStatus)

    def doRequestLeave(self, requestStatus):
        out = {'teleportIn': 'teleportOut',
         'tunnelIn': 'tunnelOut',
         'doorIn': 'doorOut'}
        self.fsm.request(out[requestStatus['how']], [requestStatus])

    def enterDoorIn(self, requestStatus):
        NametagGlobals.setMasterArrowsOn(0)
        door = base.cr.doId2do.get(requestStatus['doorDoId'])
        if not door is None:
            door.readyToExit()
        base.localAvatar.obscureMoveFurnitureButton(1)
        base.localAvatar.startQuestMap()

    def exitDoorIn(self):
        NametagGlobals.setMasterArrowsOn(1)
        base.localAvatar.obscureMoveFurnitureButton(0)

    def enterDoorOut(self):
        base.localAvatar.obscureMoveFurnitureButton(1)

    def exitDoorOut(self):
        base.localAvatar.obscureMoveFurnitureButton(0)
        base.localAvatar.stopQuestMap()

    def handleDoorDoneEvent(self, requestStatus):
        self.doneStatus = requestStatus
        messenger.send(self.doneEvent)

    def handleDoorTrigger(self):
        self.fsm.request('doorOut')

    def enterTunnelIn(self, requestStatus):
        self.notify.debug('enterTunnelIn(requestStatus=' + str(requestStatus) + ')')
        tunnelOrigin = base.render.find(requestStatus['tunnelName'])
        self.accept('tunnelInMovieDone', self.__tunnelInMovieDone)
        base.localAvatar.reconsiderCheesyEffect()
        base.localAvatar.tunnelIn(tunnelOrigin)
        base.localAvatar.startQuestMap()

    def __tunnelInMovieDone(self):
        self.ignore('tunnelInMovieDone')
        self.fsm.request('walk')

    def exitTunnelIn(self):
        pass
        
    def enterSkipTunnelIn(self, requestStatus):
        tunnelOrigin = base.render.find(requestStatus['tunnelName'])
        base.localAvatar.reconsiderCheesyEffect()
        if base.localAvatar.doId in base.cr.karts:
            kart = base.cr.karts[base.localAvatar.doId]
            kart.setPos(tunnelOrigin, 0, 6, 0)
            kart.setHpr(tunnelOrigin, 0, 0, 0)
            kart.resetVelocity()
            kart.restartKart()
        self.fsm.request('stopped')
        
    def exitSkipTunnelIn(self):
        pass

    def enterTunnelOut(self, requestStatus):
        hoodId = requestStatus['hoodId']
        zoneId = requestStatus['zoneId']
        how = requestStatus['how']
        tunnelOrigin = requestStatus['tunnelOrigin']
        fromZoneId = ZoneUtil.getCanonicalZoneId(self.getZoneId())
        tunnelName = requestStatus.get('tunnelName')
        if tunnelName == None:
            tunnelName = base.cr.hoodMgr.makeLinkTunnelName(self.loader.hood.id, fromZoneId)
        self.doneStatus = {'loader': ZoneUtil.getLoaderName(zoneId),
         'where': ZoneUtil.getToonWhereName(zoneId),
         'how': how,
         'hoodId': hoodId,
         'zoneId': zoneId,
         'shardId': None,
         'tunnelName': tunnelName}
        self.accept('tunnelOutMovieDone', self.__tunnelOutMovieDone)
        base.localAvatar.tunnelOut(tunnelOrigin)
        base.localAvatar.stopQuestMap()
        
    def tunnelOutSkip(self, fromZoneId, zoneId):
        self.doneStatus = {'loader': ZoneUtil.getLoaderName(zoneId),
         'where': ZoneUtil.getToonWhereName(zoneId),
         'how': 'skipTunnelIn',
         'hoodId': ZoneUtil.getHoodId(zoneId),
         'zoneId': zoneId,
         'shardId': None,
         'tunnelName': base.cr.hoodMgr.makeLinkTunnelName(self.loader.hood.id, fromZoneId)}
        messenger.send(self.doneEvent)

    def __tunnelOutMovieDone(self):
        self.ignore('tunnelOutMovieDone')
        messenger.send(self.doneEvent)

    def exitTunnelOut(self):
        pass

    def enterTeleportOut(self, requestStatus, callback):
        base.localAvatar.laffMeter.start()
        base.localAvatar.b_setAnimState('TeleportOut', 1, callback, [requestStatus])
        base.localAvatar.obscureMoveFurnitureButton(1)

    def exitTeleportOut(self):
        base.localAvatar.laffMeter.stop()
        base.localAvatar.stopQuestMap()
        base.localAvatar.obscureMoveFurnitureButton(0)

    def enterDied(self, requestStatus, callback = None):
        if callback == None:
            callback = self.__diedDone
        base.localAvatar.laffMeter.start()
        camera.wrtReparentTo(render)
        base.localAvatar.b_setAnimState('Died', 1, callback, [requestStatus])
        base.localAvatar.obscureMoveFurnitureButton(1)

    def __diedDone(self, requestStatus):
        self.doneStatus = requestStatus
        messenger.send(self.doneEvent)

    def exitDied(self):
        base.localAvatar.laffMeter.stop()
        base.localAvatar.obscureMoveFurnitureButton(0)

    def getEstateZoneAndGoHome(self, requestStatus):
        self.doneStatus = requestStatus
        avId = requestStatus['avId']
        self.acceptOnce('setLocalEstateZone', self.goHome)
        if avId > 0:
            base.cr.estateMgr.getLocalEstateZone(avId)
        else:
            base.cr.estateMgr.getLocalEstateZone(base.localAvatar.getDoId())
        if HouseGlobals.WANT_TELEPORT_TIMEOUT:
            taskMgr.doMethodLater(HouseGlobals.TELEPORT_TIMEOUT, self.goHomeFailed, 'goHomeFailed')

    def goHome(self, ownerId, zoneId):
        self.notify.debug('goHome ownerId = %s' % ownerId)
        taskMgr.remove('goHomeFailed')
        if ownerId > 0 and ownerId != base.localAvatar.doId and not base.cr.isFriend(ownerId):
            self.doneStatus['failed'] = 1
            self.goHomeFailed(None)
            return
        if ownerId == 0 and zoneId == 0:
            if self.doneStatus['shardId'] is None or self.doneStatus['shardId'] is base.localAvatar.defaultShard:
                self.doneStatus['failed'] = 1
                self.goHomeFailed(None)
                return
            else:
                self.doneStatus['hood'] = ToontownGlobals.MyEstate
                self.doneStatus['zone'] = base.localAvatar.lastHood
                self.doneStatus['loaderId'] = 'safeZoneLoader'
                self.doneStatus['whereId'] = 'estate'
                self.doneStatus['how'] = 'teleportIn'
                messenger.send(self.doneEvent)
                return
        if self.doneStatus['zoneId'] == -1:
            self.doneStatus['zoneId'] = zoneId
        elif self.doneStatus['zoneId'] != zoneId:
            self.doneStatus['where'] = 'house'
        self.doneStatus['ownerId'] = ownerId
        messenger.send(self.doneEvent)
        messenger.send('localToonLeft')

    def goHomeFailed(self, task):
        self.notify.debug('goHomeFailed')
        self.notifyUserGoHomeFailed()
        self.ignore('setLocalEstateZone')
        self.doneStatus['hood'] = base.localAvatar.lastHood
        self.doneStatus['zone'] = base.localAvatar.lastHood
        self.fsm.request('teleportIn', [self.doneStatus])
        return Task.done

    def notifyUserGoHomeFailed(self):
        self.notify.debug('notifyUserGoHomeFailed')
        failedToVisitAvId = self.doneStatus.get('avId', -1)
        avName = None
        if failedToVisitAvId != -1:
            avatar = base.cr.identifyAvatar(failedToVisitAvId)
            if avatar:
                avName = avatar.getName()
        if avName:
            message = TTLocalizer.EstateTeleportFailedNotFriends % avName
        else:
            message = TTLocalizer.EstateTeleportFailed
        base.localAvatar.setSystemMessage(0, message)

    def enterTeleportIn(self, requestStatus):
        self._tiToken = self.addSetZoneCompleteCallback(Functor(self._placeTeleportInPostZoneComplete, requestStatus), 100)

    def _placeTeleportInPostZoneComplete(self, requestStatus):
        teleportDebug(requestStatus, '_placeTeleportInPostZoneComplete(%s)' % (requestStatus,))
        NametagGlobals.setMasterArrowsOn(0)
        base.localAvatar.laffMeter.start()
        base.localAvatar.startQuestMap()
        base.localAvatar.reconsiderCheesyEffect()
        base.localAvatar.obscureMoveFurnitureButton(1)
        avId = requestStatus.get('avId', -1)
        if avId != -1:
            if avId in base.cr.doId2do:
                teleportDebug(requestStatus, 'teleport to avatar')
                avatar = base.cr.doId2do[avId]
                avatar.forceToTruePosition()
                base.localAvatar.gotoNode(avatar)
                base.localAvatar.b_teleportGreeting(avId)
            else:
                friend = base.cr.identifyAvatar(avId)
                if friend == None:
                    teleportDebug(requestStatus, 'friend not here, giving up')
                    base.localAvatar.setSystemMessage(avId, OTPLocalizer.WhisperTargetLeftVisit % (friend.getName(),))
                    friend.d_teleportGiveup(base.localAvatar.doId)
                else:
                    def doTeleport(task):
                        avatar = base.cr.doId2do[friend.getDoId()]
                        base.localAvatar.gotoNode(avatar)
                        base.localAvatar.b_teleportGreeting(friend.getDoId())
                        return task.done
                    self.acceptOnce('generate-%d' % friend.getDoId(), lambda x: taskMgr.doMethodLater(1, doTeleport, uniqueName('doTeleport')))
        base.transitions.irisIn()
        self.nextState = requestStatus.get('nextState', 'walk')
        base.localAvatar.attachCamera()
        base.localAvatar.startUpdateSmartCamera()
        base.localAvatar.startPosHprBroadcast()
        globalClock.tick()
        base.localAvatar.b_setAnimState('TeleportIn', 1, callback=self.teleportInDone)
        base.localAvatar.d_broadcastPositionNow()
        base.localAvatar.b_setParent(ToontownGlobals.SPRender)

    def teleportInDone(self):
        if hasattr(self, 'fsm'):
            teleportNotify.debug('teleportInDone: %s' % self.nextState)
            self.fsm.request(self.nextState, [1])

    def exitTeleportIn(self):
        self.removeSetZoneCompleteCallback(self._tiToken)
        self._tiToken = None
        NametagGlobals.setMasterArrowsOn(1)
        base.localAvatar.laffMeter.stop()
        base.localAvatar.obscureMoveFurnitureButton(0)
        base.localAvatar.stopUpdateSmartCamera()
        base.localAvatar.detachCamera()
        base.localAvatar.stopPosHprBroadcast()

    def requestTeleport(self, hoodId, zoneId, shardId, avId):
        if avId > 0:
            teleportNotify.debug('requestTeleport%s' % ((hoodId,
              zoneId,
              shardId,
              avId),))
        if localAvatar.hasActiveBoardingGroup():
            if avId > 0:
                teleportNotify.debug('requestTeleport: has active boarding group')
            rejectText = TTLocalizer.BoardingCannotLeaveZone
            localAvatar.elevatorNotifier.showMe(rejectText)
            return
        loaderId = ZoneUtil.getBranchLoaderName(zoneId)
        whereId = ZoneUtil.getToonWhereName(zoneId)
        if hoodId == ToontownGlobals.MyEstate:
            loaderId = 'safeZoneLoader'
            whereId = 'estate'
        if hoodId == ToontownGlobals.PartyHood:
            loaderId = 'safeZoneLoader'
            whereId = 'party'
        self.requestLeave({'loader': loaderId,
         'where': whereId,
         'how': 'teleportIn',
         'hoodId': hoodId,
         'zoneId': zoneId,
         'shardId': shardId,
         'avId': avId})

    def enterQuest(self, npcToon):
        base.localAvatar.b_setAnimState('neutral', 1)
        self.accept('teleportQuery', self.handleTeleportQuery)
        base.localAvatar.setTeleportAvailable(1)
        base.localAvatar.laffMeter.start()
        base.localAvatar.obscureMoveFurnitureButton(1)

    def exitQuest(self):
        base.localAvatar.setTeleportAvailable(0)
        self.ignore('teleportQuery')
        base.localAvatar.laffMeter.stop()
        base.localAvatar.obscureMoveFurnitureButton(0)

    def enterPurchase(self):
        base.localAvatar.b_setAnimState('neutral', 1)
        self.accept('teleportQuery', self.handleTeleportQuery)
        base.localAvatar.setTeleportAvailable(1)
        base.localAvatar.laffMeter.start()
        base.localAvatar.obscureMoveFurnitureButton(1)

    def exitPurchase(self):
        base.localAvatar.setTeleportAvailable(0)
        self.ignore('teleportQuery')
        base.localAvatar.laffMeter.stop()
        base.localAvatar.obscureMoveFurnitureButton(0)

    def enterFishing(self):
        base.localAvatar.b_setAnimState('neutral', 1)
        self.accept('teleportQuery', self.handleTeleportQuery)
        base.localAvatar.setTeleportAvailable(1)
        base.localAvatar.laffMeter.start()

    def exitFishing(self):
        base.localAvatar.setTeleportAvailable(0)
        self.ignore('teleportQuery')
        base.localAvatar.laffMeter.stop()

    def enterBanking(self):
        base.localAvatar.b_setAnimState('neutral', 1)
        self.accept('teleportQuery', self.handleTeleportQuery)
        base.localAvatar.setTeleportAvailable(1)
        base.localAvatar.laffMeter.start()
        base.localAvatar.obscureMoveFurnitureButton(1)
        base.localAvatar.startSleepWatch(self.__handleFallingAsleepBanking)

    def __handleFallingAsleepBanking(self, arg):
        if hasattr(self, 'fsm'):
            messenger.send('bankAsleep')
            self.fsm.request('walk')
        base.localAvatar.forceGotoSleep()

    def exitBanking(self):
        base.localAvatar.setTeleportAvailable(0)
        self.ignore('teleportQuery')
        base.localAvatar.laffMeter.stop()
        base.localAvatar.obscureMoveFurnitureButton(0)
        base.localAvatar.stopSleepWatch()

    def enterPhone(self):
        base.localAvatar.b_setAnimState('neutral', 1)
        self.accept('teleportQuery', self.handleTeleportQuery)
        base.localAvatar.setTeleportAvailable(1)
        base.localAvatar.laffMeter.start()
        base.localAvatar.obscureMoveFurnitureButton(1)
        base.localAvatar.startSleepWatch(self.__handleFallingAsleepPhone)

    def __handleFallingAsleepPhone(self, arg):
        if hasattr(self, 'fsm'):
            self.fsm.request('walk')
        messenger.send('phoneAsleep')
        base.localAvatar.forceGotoSleep()

    def exitPhone(self):
        base.localAvatar.setTeleportAvailable(0)
        self.ignore('teleportQuery')
        base.localAvatar.laffMeter.stop()
        base.localAvatar.obscureMoveFurnitureButton(0)
        base.localAvatar.stopSleepWatch()

    def enterStopped(self):
        base.localAvatar.b_setAnimState('neutral', 1)
        Emote.globalEmote.disableBody(base.localAvatar, 'enterStopped')
        self.accept('teleportQuery', self.handleTeleportQuery)
        if base.localAvatar.isDisguised:
            base.localAvatar.setTeleportAvailable(0)
        else:
            base.localAvatar.setTeleportAvailable(1)
        base.localAvatar.laffMeter.start()
        base.localAvatar.obscureMoveFurnitureButton(1)
        base.localAvatar.startSleepWatch(self.__handleFallingAsleepStopped)

    def __handleFallingAsleepStopped(self, arg):
        if hasattr(self, 'fsm'):
            self.fsm.request('walk')
        base.localAvatar.forceGotoSleep()
        messenger.send('stoppedAsleep')

    def exitStopped(self):
        Emote.globalEmote.releaseBody(base.localAvatar, 'exitStopped')
        base.localAvatar.setTeleportAvailable(0)
        self.ignore('teleportQuery')
        base.localAvatar.laffMeter.stop()
        base.localAvatar.obscureMoveFurnitureButton(0)
        base.localAvatar.stopSleepWatch()
        messenger.send('exitingStoppedState')

    def enterPet(self):
        base.localAvatar.b_setAnimState('neutral', 1)
        Emote.globalEmote.disableBody(base.localAvatar, 'enterPet')
        self.accept('teleportQuery', self.handleTeleportQuery)
        base.localAvatar.setTeleportAvailable(1)
        base.localAvatar.setTeleportAllowed(0)
        base.localAvatar.laffMeter.start()
        self.enterFLM()

    def exitPet(self):
        base.localAvatar.setTeleportAvailable(0)
        base.localAvatar.setTeleportAllowed(1)
        Emote.globalEmote.releaseBody(base.localAvatar, 'exitPet')
        self.ignore('teleportQuery')
        base.localAvatar.laffMeter.stop()
        self.exitFLM()

    def enterQuietZone(self, requestStatus):
        self.quietZoneDoneEvent = uniqueName('quietZoneDone')
        self.acceptOnce(self.quietZoneDoneEvent, self.handleQuietZoneDone)
        self.quietZoneStateData = QuietZoneState.QuietZoneState(self.quietZoneDoneEvent)
        self.quietZoneStateData.load()
        self.quietZoneStateData.enter(requestStatus)

    def exitQuietZone(self):
        self.ignore(self.quietZoneDoneEvent)
        del self.quietZoneDoneEvent
        self.quietZoneStateData.exit()
        self.quietZoneStateData.unload()
        self.quietZoneStateData = None

    def handleQuietZoneDone(self):
        how = base.cr.handlerArgs['how']
        self.fsm.request(how, [base.cr.handlerArgs])
