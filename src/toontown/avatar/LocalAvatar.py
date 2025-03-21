from panda3d.core import BitMask32, Camera, CollideMask, CollisionEntry, CollisionHandler, CollisionHandlerFloor, CollisionHandlerPusher, CollisionHandlerQueue, CollisionNode, CollisionRay, CollisionSegment, CollisionSphere, CollisionTraverser, GeomNode, Lens, NodePath, Point3, Vec3, deg2Rad, lookAt
from direct.controls.GhostWalker import GhostWalker
from direct.controls.GravityWalker import GravityWalker
from direct.controls.ObserverWalker import ObserverWalker
from direct.controls.SwimWalker import SwimWalker
from direct.controls.TwoDWalker import TwoDWalker
from direct.directnotify import DirectNotifyGlobal
from direct.distributed import DistributedSmoothNode
from direct.gui.DirectGui import *
from direct.interval.IntervalGlobal import *
from direct.showbase.InputStateGlobal import inputState
from direct.showbase.PythonUtil import *
from direct.task import Task
import math
import random
import webbrowser
import numbers
import DistributedAvatar
import PlayerControlManager
from toontown.magicword.MagicWordGlobal import *
from otp.otpbase import OTPGlobals
from otp.otpbase import OTPLocalizer
from lib.nametag.NametagConstants import *
from lib.margins.WhisperPopup import *
from toontown.base import ToontownGlobals


class LocalAvatar(DistributedAvatar.DistributedAvatar, DistributedSmoothNode.DistributedSmoothNode):
    notify = DirectNotifyGlobal.directNotify.newCategory('LocalAvatar')
    wantDevCameraPositions = base.config.GetBool('want-dev-camera-positions', 0)
    wantMouse = base.config.GetBool('want-mouse', 0)
    sleepTimeout = base.config.GetInt('sleep-timeout', 300)
    __enableMarkerPlacement = base.config.GetBool('place-markers', 0)

    def __init__(self, cr, chatMgr, talkAssistant = None, passMessagesThrough = False):
        try:
            self.LocalAvatar_initialized
            return
        except:
            self.LocalAvatar_initialized = 1
        DistributedAvatar.DistributedAvatar.__init__(self, cr)
        DistributedSmoothNode.DistributedSmoothNode.__init__(self, cr)
        self.cTrav = CollisionTraverser('base.cTrav')
        base.pushCTrav(self.cTrav)
        self.cTrav.setRespectPrevTransform(1)
        self.avatarControlsEnabled = 0
        self.controlManager = PlayerControlManager.PlayerControlManager(True, passMessagesThrough)
        self.initializeCollisions()
        self.initializeSmartCamera()
        self.cameraPositions = []
        self.animMultiplier = 1.0
        self.runTimeout = 2.5
        self.customMessages = []
        self.chatMgr = chatMgr
        base.talkAssistant = talkAssistant
        self.teleportAllowed = 1
        self.lockedDown = 0
        self.isPageUp = 0
        self.isPageDown = 0
        self.soundRun = None
        self.soundWalk = None
        self.sleepFlag = 0
        self.sleepDisabled = 0
        self.isDisguised = 0
        self.movingFlag = 0
        self.preventCameraDisable = False
        self.lastNeedH = None
        self.accept('friendOnline', self.__friendOnline)
        self.accept('friendOffline', self.__friendOffline)
        self.accept('clickedWhisper', self.clickedWhisper)
        self.sleepCallback = None
        self.accept('wakeup', self.wakeUp)
        self.jumpLandAnimFixTask = None
        self.fov = settings['fov']
        self.accept('avatarMoving', self.clearPageUpDown)
        self.showNametag2d()
        self.setPickable(0)
    
    def setPreventCameraDisable(self, prevent):
        self.preventCameraDisable = prevent

    def useSwimControls(self):
        self.controlManager.use('swim', self)

    def useGhostControls(self):
        self.controlManager.use('ghost', self)

    def useWalkControls(self):
        self.controlManager.use('walk', self)

    def useTwoDControls(self):
        self.controlManager.use('twoD', self)

    def isLockedDown(self):
        return self.lockedDown

    def lock(self):
        if self.lockedDown == 1:
            self.notify.debug('lock() - already locked!')
        self.lockedDown = 1

    def unlock(self):
        if self.lockedDown == 0:
            self.notify.debug('unlock() - already unlocked!')
        self.lockedDown = 0

    def isInWater(self):
        return self.getZ(render) <= 0.0

    def isTeleportAllowed(self):
        return self.teleportAllowed and not self.isDisguised

    def setTeleportAllowed(self, flag):
        self.teleportAllowed = flag
        self.refreshOnscreenButtons()

    def sendFriendsListEvent(self):
        self.wakeUp()
        messenger.send('openFriendsList')

    def delete(self):
        try:
            self.LocalAvatar_deleted
            return
        except:
            self.LocalAvatar_deleted = 1

        self.ignoreAll()
        self.stopJumpLandTask()
        base.popCTrav()
        taskMgr.remove('posCamera')
        self.disableAvatarControls()
        self.stopTrackAnimToSpeed()
        self.stopUpdateSmartCamera()
        self.shutdownSmartCamera()
        self.deleteCollisions()
        self.controlManager.delete()
        self.physControls = None
        del self.controlManager
        self.positionExaminer.delete()
        del self.positionExaminer
        taskMgr.remove(self.uniqueName('walkReturnTask'))
        self.chatMgr.delete()
        del self.chatMgr
        del self.soundRun
        del self.soundWalk
        if hasattr(self, 'soundWhisper'):
            del self.soundWhisper
        DistributedAvatar.DistributedAvatar.delete(self)

    def wantLegacyLifter(self):
        return False

    def setupControls(self, avatarRadius = 1.4, floorOffset = OTPGlobals.FloorOffset, reach = 4.0, wallBitmask = OTPGlobals.WallBitmask, floorBitmask = OTPGlobals.FloorBitmask, ghostBitmask = OTPGlobals.GhostBitmask):
        walkControls = GravityWalker(legacyLifter=self.wantLegacyLifter())
        walkControls.setWallBitMask(wallBitmask)
        walkControls.setFloorBitMask(floorBitmask)
        walkControls.initializeCollisions(self.cTrav, self, avatarRadius, floorOffset, reach)
        walkControls.setAirborneHeightFunc(self.getAirborneHeight)
        self.controlManager.add(walkControls, 'walk')
        self.physControls = walkControls
        twoDControls = TwoDWalker()
        twoDControls.setWallBitMask(wallBitmask)
        twoDControls.setFloorBitMask(floorBitmask)
        twoDControls.initializeCollisions(self.cTrav, self, avatarRadius, floorOffset, reach)
        twoDControls.setAirborneHeightFunc(self.getAirborneHeight)
        self.controlManager.add(twoDControls, 'twoD')
        swimControls = SwimWalker()
        swimControls.setWallBitMask(wallBitmask)
        swimControls.setFloorBitMask(floorBitmask)
        swimControls.initializeCollisions(self.cTrav, self, avatarRadius, floorOffset, reach)
        swimControls.setAirborneHeightFunc(self.getAirborneHeight)
        self.controlManager.add(swimControls, 'swim')
        ghostControls = GhostWalker()
        ghostControls.setWallBitMask(ghostBitmask)
        ghostControls.setFloorBitMask(floorBitmask)
        ghostControls.initializeCollisions(self.cTrav, self, avatarRadius, floorOffset, reach)
        ghostControls.setAirborneHeightFunc(self.getAirborneHeight)
        self.controlManager.add(ghostControls, 'ghost')
        observerControls = ObserverWalker()
        observerControls.setWallBitMask(ghostBitmask)
        observerControls.setFloorBitMask(floorBitmask)
        observerControls.initializeCollisions(self.cTrav, self, avatarRadius, floorOffset, reach)
        observerControls.setAirborneHeightFunc(self.getAirborneHeight)
        self.controlManager.add(observerControls, 'observer')
        self.controlManager.use('walk', self)
        self.controlManager.disable()

    def initializeCollisions(self):
        self.setupControls()
        self.cRayMoveNodePath = hidden.attachNewNode('cRayMoveNode')
        self.avatarFloorCollisionBroadcaster = CollisionHandlerFloor()
        self.avatarFloorCollisionBroadcaster.setInPattern('on-floor')
        self.avatarFloorCollisionBroadcaster.setOutPattern('off-floor')
        self.avatarFloorCollisionBroadcaster.addCollider(
            self.physControls.cRayNodePath, self.cRayMoveNodePath)
        self.cTrav.addCollider(self.physControls.cRayNodePath, self.avatarFloorCollisionBroadcaster)

    def deleteCollisions(self):
        self.cTrav.removeCollider(self.physControls.cRayNodePath)
        del self.avatarFloorCollisionBroadcaster
        self.cRayMoveNodePath.removeNode()
        del self.cRayMoveNodePath
        self.controlManager.deleteCollisions()
        self.ignore('entero157')
        del self.cTrav

    def initializeSmartCameraCollisions(self):
        self.ccTrav = CollisionTraverser('LocalAvatar.ccTrav')
        self.ccLine = CollisionSegment(0.0, 0.0, 0.0, 1.0, 0.0, 0.0)
        self.ccLineNode = CollisionNode('ccLineNode')
        self.ccLineNode.addSolid(self.ccLine)
        self.ccLineNodePath = self.attachNewNode(self.ccLineNode)
        self.ccLineBitMask = OTPGlobals.CameraBitmask
        self.ccLineNode.setFromCollideMask(self.ccLineBitMask)
        self.ccLineNode.setIntoCollideMask(BitMask32.allOff())
        self.camCollisionQueue = CollisionHandlerQueue()
        self.ccTrav.addCollider(self.ccLineNodePath, self.camCollisionQueue)
        self.ccSphere = CollisionSphere(0, 0, 0, 1)
        self.ccSphereNode = CollisionNode('ccSphereNode')
        self.ccSphereNode.addSolid(self.ccSphere)
        self.ccSphereNodePath = base.camera.attachNewNode(self.ccSphereNode)
        self.ccSphereNode.setFromCollideMask(OTPGlobals.CameraBitmask)
        self.ccSphereNode.setIntoCollideMask(BitMask32.allOff())
        self.camPusher = CollisionHandlerPusher()
        self.camPusher.addCollider(self.ccSphereNodePath, base.camera)
        self.camPusher.setCenter(self)
        self.ccPusherTrav = CollisionTraverser('LocalAvatar.ccPusherTrav')
        self.ccSphere2 = self.ccSphere
        self.ccSphereNode2 = CollisionNode('ccSphereNode2')
        self.ccSphereNode2.addSolid(self.ccSphere2)
        self.ccSphereNodePath2 = base.camera.attachNewNode(self.ccSphereNode2)
        self.ccSphereNode2.setFromCollideMask(OTPGlobals.CameraBitmask)
        self.ccSphereNode2.setIntoCollideMask(BitMask32.allOff())
        self.camPusher2 = CollisionHandlerPusher()
        self.ccPusherTrav.addCollider(self.ccSphereNodePath2, self.camPusher2)
        self.camPusher2.addCollider(self.ccSphereNodePath2, base.camera)
        self.camPusher2.setCenter(self)
        self.camFloorRayNode = self.attachNewNode('camFloorRayNode')
        self.ccRay = CollisionRay(0.0, 0.0, 0.0, 0.0, 0.0, -1.0)
        self.ccRayNode = CollisionNode('ccRayNode')
        self.ccRayNode.addSolid(self.ccRay)
        self.ccRayNodePath = self.camFloorRayNode.attachNewNode(self.ccRayNode)
        self.ccRayBitMask = OTPGlobals.FloorBitmask
        self.ccRayNode.setFromCollideMask(self.ccRayBitMask)
        self.ccRayNode.setIntoCollideMask(BitMask32.allOff())
        self.ccTravFloor = CollisionTraverser('LocalAvatar.ccTravFloor')
        self.camFloorCollisionQueue = CollisionHandlerQueue()
        self.ccTravFloor.addCollider(self.ccRayNodePath, self.camFloorCollisionQueue)
        self.ccTravOnFloor = CollisionTraverser('LocalAvatar.ccTravOnFloor')
        self.ccRay2 = CollisionRay(0.0, 0.0, 0.0, 0.0, 0.0, -1.0)
        self.ccRay2Node = CollisionNode('ccRay2Node')
        self.ccRay2Node.addSolid(self.ccRay2)
        self.ccRay2NodePath = self.camFloorRayNode.attachNewNode(self.ccRay2Node)
        self.ccRay2BitMask = OTPGlobals.FloorBitmask
        self.ccRay2Node.setFromCollideMask(self.ccRay2BitMask)
        self.ccRay2Node.setIntoCollideMask(BitMask32.allOff())
        self.ccRay2MoveNodePath = hidden.attachNewNode('ccRay2MoveNode')
        self.camFloorCollisionBroadcaster = CollisionHandlerFloor()
        self.camFloorCollisionBroadcaster.setInPattern('on-floor')
        self.camFloorCollisionBroadcaster.setOutPattern('off-floor')
        self.camFloorCollisionBroadcaster.addCollider(self.ccRay2NodePath, self.ccRay2MoveNodePath)

    def deleteSmartCameraCollisions(self):
        del self.ccTrav
        del self.ccLine
        del self.ccLineNode
        self.ccLineNodePath.removeNode()
        del self.ccLineNodePath
        del self.camCollisionQueue
        del self.ccRay
        del self.ccRayNode
        self.ccRayNodePath.removeNode()
        del self.ccRayNodePath
        del self.ccRay2
        del self.ccRay2Node
        self.ccRay2NodePath.removeNode()
        del self.ccRay2NodePath
        self.ccRay2MoveNodePath.removeNode()
        del self.ccRay2MoveNodePath
        del self.ccTravOnFloor
        del self.ccTravFloor
        del self.camFloorCollisionQueue
        del self.camFloorCollisionBroadcaster
        del self.ccSphere
        del self.ccSphereNode
        self.ccSphereNodePath.removeNode()
        del self.ccSphereNodePath
        del self.camPusher
        del self.ccPusherTrav
        del self.ccSphere2
        del self.ccSphereNode2
        self.ccSphereNodePath2.removeNode()
        del self.ccSphereNodePath2
        del self.camPusher2

    def collisionsOff(self):
        self.controlManager.collisionsOff()

    def collisionsOn(self):
        self.controlManager.collisionsOn()

    def recalcCameraSphere(self):
        nearPlaneDist = base.camLens.getNear()
        hFov = base.camLens.getHfov()
        vFov = base.camLens.getVfov()
        hOff = nearPlaneDist * math.tan(deg2Rad(hFov / 2.0))
        vOff = nearPlaneDist * math.tan(deg2Rad(vFov / 2.0))
        camPnts = [Point3(hOff, nearPlaneDist, vOff),
         Point3(-hOff, nearPlaneDist, vOff),
         Point3(hOff, nearPlaneDist, -vOff),
         Point3(-hOff, nearPlaneDist, -vOff),
         Point3(0.0, 0.0, 0.0)]
        avgPnt = Point3(0.0, 0.0, 0.0)
        for camPnt in camPnts:
            avgPnt = avgPnt + camPnt

        avgPnt = avgPnt / len(camPnts)
        sphereRadius = 0.0
        for camPnt in camPnts:
            dist = Vec3(camPnt - avgPnt).length()
            if dist > sphereRadius:
                sphereRadius = dist

        avgPnt = Point3(avgPnt)
        self.ccSphereNodePath.setPos(avgPnt)
        self.ccSphereNodePath2.setPos(avgPnt)
        self.ccSphere.setRadius(sphereRadius)

    def putCameraFloorRayOnAvatar(self):
        self.camFloorRayNode.setPos(self, 0, 0, 5)

    def putCameraFloorRayOnCamera(self):
        self.camFloorRayNode.setPos(self.ccSphereNodePath, 0, 0, 0)

    def attachCamera(self):
        camera.reparentTo(self)
        base.enableMouse()
        base.setMouseOnNode(self.node())
        self.ignoreMouse = not self.wantMouse
        self.setWalkSpeedNormal()

    def detachCamera(self):
        base.disableMouse()

    def stopJumpLandTask(self):
        if self.jumpLandAnimFixTask:
            self.jumpLandAnimFixTask.remove()
            self.jumpLandAnimFixTask = None
        return

    def jumpStart(self):
        if not self.sleepFlag and self.hp > 0:
            self.b_setAnimState('jumpAirborne', 1.0)
            self.stopJumpLandTask()

    def returnToWalk(self, task):
        if self.sleepFlag:
            state = 'Sleep'
        elif self.hp > 0:
            state = 'Happy'
        else:
            state = 'Sad'
        self.b_setAnimState(state, 1.0)
        return Task.done

    if 1:
        def jumpLandAnimFix(self, jumpTime):
            if self.playingAnim != 'run' and self.playingAnim != 'walk':
                return taskMgr.doMethodLater(jumpTime, self.returnToWalk, self.uniqueName('walkReturnTask'))

        def jumpHardLand(self):
            if self.allowHardLand():
                self.b_setAnimState('jumpLand', 1.0)
                self.stopJumpLandTask()
                self.jumpLandAnimFixTask = self.jumpLandAnimFix(1.0)
            if self.d_broadcastPosHpr:
                self.d_broadcastPosHpr()

        def jumpLand(self):
            self.jumpLandAnimFixTask = self.jumpLandAnimFix(0.01)
            if self.d_broadcastPosHpr:
                self.d_broadcastPosHpr()

    def setupAnimationEvents(self):
        self.accept('jumpStart', self.jumpStart, [])
        self.accept('jumpHardLand', self.jumpHardLand, [])
        self.accept('jumpLand', self.jumpLand, [])

    def ignoreAnimationEvents(self):
        self.ignore('jumpStart')
        self.ignore('jumpHardLand')
        self.ignore('jumpLand')

    def allowHardLand(self):
        return not self.sleepFlag and self.hp > 0

    def enableSmartCameraViews(self):
        self.accept('tab', self.nextCameraPos, [1])
        self.accept('shift-tab', self.nextCameraPos, [0])
        self.accept('page_up', self.pageUp)
        self.accept('page_down', self.pageDown)

    def disableSmartCameraViews(self):
        self.ignore('tab')
        self.ignore('shift-tab')
        self.ignore('page_up')
        self.ignore('page_down')
        self.ignore('page_down-up')

    def enableAvatarControls(self):
        if self.avatarControlsEnabled:
            return
        self.avatarControlsEnabled = 1
        self.setupAnimationEvents()
        self.controlManager.enable()

    def disableAvatarControls(self):
        if not self.avatarControlsEnabled:
            return
        self.avatarControlsEnabled = 0
        self.ignoreAnimationEvents()
        self.controlManager.disable()
        self.clearPageUpDown()

    def setWalkSpeedNormal(self):
        self.controlManager.setSpeeds(OTPGlobals.ToonForwardSpeed, OTPGlobals.ToonJumpForce, OTPGlobals.ToonReverseSpeed, OTPGlobals.ToonRotateSpeed)

    def pageUp(self):
        if not (self.avatarControlsEnabled or self.preventCameraDisable):
            return
        self.wakeUp()
        if not self.isPageUp:
            self.isPageDown = 0
            self.isPageUp = 1
            self.lerpCameraFov(70, 0.6)
            self.setCameraPositionByIndex(self.cameraIndex)
        else:
            self.clearPageUpDown()

    def pageDown(self):
        if not (self.avatarControlsEnabled or self.preventCameraDisable):
            return
        self.wakeUp()
        if not self.isPageDown:
            self.isPageUp = 0
            self.isPageDown = 1
            self.lerpCameraFov(70, 0.6)
            self.setCameraPositionByIndex(self.cameraIndex)
        else:
            self.clearPageUpDown()

    def clearPageUpDown(self):
        if self.isPageDown or self.isPageUp:
            self.lerpCameraFov(self.fov, 0.6)
            self.isPageDown = 0
            self.isPageUp = 0
            self.setCameraPositionByIndex(self.cameraIndex)

    def nextCameraPos(self, forward):
        if not (self.avatarControlsEnabled or self.preventCameraDisable):
            return
        self.wakeUp()
        self.__cameraHasBeenMoved = 1
        if forward:
            self.cameraIndex += 1
            if self.cameraIndex > len(self.cameraPositions) - 1:
                self.cameraIndex = 0
        else:
            self.cameraIndex -= 1
            if self.cameraIndex < 0:
                self.cameraIndex = len(self.cameraPositions) - 1
        self.setCameraPositionByIndex(self.cameraIndex)
    
    def setCameraPosition(self, index):
        self.cameraIndex = index
        self.setCameraPositionByIndex(index)

    def initCameraPositions(self):
        camHeight = self.getClampedAvatarHeight()
        heightScaleFactor = camHeight * 0.3333333333
        defLookAt = Point3(0.0, 1.5, camHeight)
        scXoffset = 3.0
        scPosition = (Point3(scXoffset - 1, -10.0, camHeight + 5.0), Point3(scXoffset, 2.0, camHeight))
        self.cameraPositions = [(Point3(0.0, -9.0 * heightScaleFactor, camHeight),
          defLookAt,
          Point3(0.0, camHeight, camHeight * 4.0),
          Point3(0.0, camHeight, camHeight * -1.0),
          0),
         (Point3(0.0, 0.7, camHeight),
          defLookAt,
          Point3(0.0, camHeight, camHeight * 1.33),
          Point3(0.0, camHeight, camHeight * 0.66),
          1),
         (Point3(5.7 * heightScaleFactor, 7.65 * heightScaleFactor, camHeight + 2.0),
          Point3(0.0, 1.0, camHeight),
          Point3(0.0, 1.0, camHeight * 4.0),
          Point3(0.0, 1.0, camHeight * -1.0),
          0),
         (Point3(0.0, 8.65 * heightScaleFactor, camHeight),
          Point3(0.0, 1.0, camHeight),
          Point3(0.0, 1.0, camHeight * 4.0),
          Point3(0.0, 1.0, camHeight * -1.0),
          0),
         (Point3(-camHeight * 3, 0.0, camHeight),
          Point3(0.0, 0.0, camHeight),
          Point3(0.0, camHeight, camHeight * 1.1),
          Point3(0.0, camHeight, camHeight * 0.9),
          1),
         (Point3(camHeight * 3, 0.0, camHeight),
          Point3(0.0, 0.0, camHeight),
          Point3(0.0, camHeight, camHeight * 1.1),
          Point3(0.0, camHeight, camHeight * 0.9),
          1),
         (Point3(0.0, -24.0 * heightScaleFactor, camHeight + 4.0),
          defLookAt,
          Point3(0.0, 1.5, camHeight * 4.0),
          Point3(0.0, 1.5, camHeight * -1.0),
          0),
         (Point3(0.0, -12.0 * heightScaleFactor, camHeight + 4.0),
          defLookAt,
          Point3(0.0, 1.5, camHeight * 4.0),
          Point3(0.0, 1.5, camHeight * -1.0),
          0)] + self.auxCameraPositions
        if self.wantDevCameraPositions:
            self.cameraPositions += [(Point3(0.0, 0.0, camHeight * 3),
              Point3(0.0, 0.0, 0.0),
              Point3(0.0, camHeight * 2, 0.0),
              Point3(0.0, -camHeight * 2, 0.0),
              1),
             (Point3(camHeight * 3, 0.0, camHeight),
              Point3(0.0, 0.0, camHeight),
              Point3(0.0, camHeight, camHeight * 1.1),
              Point3(0.0, camHeight, camHeight * 0.9),
              1),
             (Point3(camHeight * 3, 0.0, 0.0),
              Point3(0.0, 0.0, camHeight),
              Point3(0.0, camHeight, camHeight * 1.1),
              Point3(0.0, camHeight, camHeight * 0.9),
              1),
             (Point3(-camHeight * 3, 0.0, camHeight),
              Point3(0.0, 0.0, camHeight),
              Point3(0.0, camHeight, camHeight * 1.1),
              Point3(0.0, camHeight, camHeight * 0.9),
              1),
             (Point3(0.0, -60, 60),
              defLookAt + Point3(0, 15, 0),
              defLookAt + Point3(0, 15, 0),
              defLookAt + Point3(0, 15, 0),
              1),
             (Point3(0.0, -20, 20),
              defLookAt + Point3(0, 5, 0),
              defLookAt + Point3(0, 5, 0),
              defLookAt + Point3(0, 5, 0),
              1)]

    def addCameraPosition(self, camPos = None):
        if camPos == None:
            lookAtNP = self.attachNewNode('lookAt')
            lookAtNP.setPos(base.cam, 0, 1, 0)
            lookAtPos = lookAtNP.getPos()
            camHeight = self.getClampedAvatarHeight()
            camPos = (base.cam.getPos(self),
             lookAtPos,
             Point3(0.0, 1.5, camHeight * 4.0),
             Point3(0.0, 1.5, camHeight * -1.0),
             1)
            lookAtNP.removeNode()
        self.auxCameraPositions.append(camPos)
        self.cameraPositions.append(camPos)

    def resetCameraPosition(self):
        self.cameraIndex = 0
        self.setCameraPositionByIndex(self.cameraIndex)

    def removeCameraPosition(self):
        if len(self.cameraPositions) > 1:
            camPos = self.cameraPositions[self.cameraIndex]
            if camPos in self.auxCameraPositions:
                self.auxCameraPositions.remove(camPos)
            if camPos in self.cameraPositions:
                self.cameraPositions.remove(camPos)
            self.nextCameraPos(1)

    def posCamera(self, lerp, time):
        if not lerp:
            self.positionCameraWithPusher(self.getCompromiseCameraPos(), self.getLookAtPoint())
        else:
            camPos = self.getCompromiseCameraPos()
            savePos = camera.getPos()
            saveHpr = camera.getHpr()
            self.positionCameraWithPusher(camPos, self.getLookAtPoint())
            x = camPos[0]
            y = camPos[1]
            z = camPos[2]
            destHpr = camera.getHpr()
            h = destHpr[0]
            p = destHpr[1]
            r = destHpr[2]
            camera.setPos(savePos)
            camera.setHpr(saveHpr)
            taskMgr.remove('posCamera')
            self.cameraLerp = LerpPosHprInterval(camera, time, Point3(x, y, z), Point3(h, p, r), other=self, name='posCamera')
            self.cameraLerp.start()

    def getClampedAvatarHeight(self):
        return max(self.getHeight(), 3.0)

    def getVisibilityPoint(self):
        return Point3(0.0, 0.0, self.getHeight())

    def setLookAtPoint(self, la):
        self.__curLookAt = Point3(la)

    def getLookAtPoint(self):
        return Point3(self.__curLookAt)

    def setIdealCameraPos(self, pos):
        self.__idealCameraPos = Point3(pos)
        self.updateSmartCameraCollisionLineSegment()

    def getIdealCameraPos(self):
        return Point3(self.__idealCameraPos)

    def setCameraPositionByIndex(self, index):
        self.notify.debug('switching to camera position %s' % index)
        self.setCameraSettings(self.cameraPositions[index])

    def setCameraPosForPetInteraction(self):
        height = self.getClampedAvatarHeight()
        point = Point3(height * (7 / 3.0), height * (-7 / 3.0), height)
        self.prevIdealPos = self.getIdealCameraPos()
        self.setIdealCameraPos(point)
        self.posCamera(1, 0.7)

    def unsetCameraPosForPetInteraction(self):
        if hasattr(self, 'prevIdealPos'):
            self.setIdealCameraPos(self.prevIdealPos)
            del self.prevIdealPos
        self.posCamera(1, 0.7)

    def setCameraSettings(self, camSettings):
        self.setIdealCameraPos(camSettings[0])
        if self.isPageUp and self.isPageDown or not self.isPageUp and not self.isPageDown:
            self.__cameraHasBeenMoved = 1
            self.setLookAtPoint(camSettings[1])
        elif self.isPageUp:
            self.__cameraHasBeenMoved = 1
            self.setLookAtPoint(camSettings[2])
        elif self.isPageDown:
            self.__cameraHasBeenMoved = 1
            self.setLookAtPoint(camSettings[3])
        else:
            self.notify.error('This case should be impossible.')
        self.__disableSmartCam = camSettings[4]
        if self.__disableSmartCam:
            self.putCameraFloorRayOnAvatar()
            self.cameraZOffset = 0.0

    def getCompromiseCameraPos(self):
        if self.__idealCameraObstructed == 0:
            compromisePos = self.getIdealCameraPos()
        else:
            visPnt = self.getVisibilityPoint()
            idealPos = self.getIdealCameraPos()
            distance = Vec3(idealPos - visPnt).length()
            ratio = self.closestObstructionDistance / distance
            compromisePos = idealPos * ratio + visPnt * (1 - ratio)
            liftMult = 1.0 - ratio * ratio
            compromisePos = Point3(compromisePos[0], compromisePos[1], compromisePos[2] + self.getHeight() * 0.4 * liftMult)
        compromisePos.setZ(compromisePos[2] + self.cameraZOffset)
        return compromisePos

    def updateSmartCameraCollisionLineSegment(self):
        pointB = self.getIdealCameraPos()
        pointA = self.getVisibilityPoint()
        vectorAB = Vec3(pointB - pointA)
        lengthAB = vectorAB.length()
        if lengthAB > 0.001:
            self.ccLine.setPointA(pointA)
            self.ccLine.setPointB(pointB)

    def initializeSmartCamera(self):
        self.__idealCameraObstructed = 0
        self.closestObstructionDistance = 0.0
        self.cameraIndex = 0
        self.auxCameraPositions = []
        self.cameraZOffset = 0.0
        self.__onLevelGround = 0
        self.__camCollCanMove = 0
        self.__geom = render
        self.__disableSmartCam = 0
        self.initializeSmartCameraCollisions()
        self._smartCamEnabled = False

    def shutdownSmartCamera(self):
        self.deleteSmartCameraCollisions()

    def setOnLevelGround(self, flag):
        self.__onLevelGround = flag

    def setCameraCollisionsCanMove(self, flag):
        self.__camCollCanMove = flag

    def setGeom(self, geom):
        self.__geom = geom

    def startUpdateSmartCamera(self, push = 1):
        if self._smartCamEnabled:
            LocalAvatar.notify.warning('redundant call to startUpdateSmartCamera')
            return
        self._smartCamEnabled = True
        self.__floorDetected = 0
        self.__cameraHasBeenMoved = 0
        self.recalcCameraSphere()
        self.initCameraPositions()
        self.setCameraPositionByIndex(self.cameraIndex)
        self.posCamera(0, 0.0)
        self.__instantaneousCamPos = camera.getPos()
        if push:
            self.cTrav.addCollider(self.ccSphereNodePath, self.camPusher)
            self.ccTravOnFloor.addCollider(self.ccRay2NodePath, self.camFloorCollisionBroadcaster)
            self.__disableSmartCam = 0
        else:
            self.__disableSmartCam = 1
        self.__lastPosWrtRender = camera.getPos(render)
        self.__lastHprWrtRender = camera.getHpr(render)
        taskName = self.taskName('updateSmartCamera')
        taskMgr.remove(taskName)
        taskMgr.add(self.updateSmartCamera, taskName, priority=47)
        self.enableSmartCameraViews()

    def stopUpdateSmartCamera(self):
        if not self._smartCamEnabled:
            LocalAvatar.notify.warning('redundant call to stopUpdateSmartCamera')
            return
        self.disableSmartCameraViews()
        self.cTrav.removeCollider(self.ccSphereNodePath)
        self.ccTravOnFloor.removeCollider(self.ccRay2NodePath)
        if not base.localAvatar.isEmpty():
            self.putCameraFloorRayOnAvatar()
        taskName = self.taskName('updateSmartCamera')
        taskMgr.remove(taskName)
        self._smartCamEnabled = False

    def updateSmartCamera(self, task):
        if not self.__camCollCanMove and not self.__cameraHasBeenMoved:
            if self.__lastPosWrtRender == camera.getPos(render):
                if self.__lastHprWrtRender == camera.getHpr(render):
                    return Task.cont
        self.__cameraHasBeenMoved = 0
        self.__lastPosWrtRender = camera.getPos(render)
        self.__lastHprWrtRender = camera.getHpr(render)
        self.__idealCameraObstructed = 0
        if not self.__disableSmartCam:
            self.ccTrav.traverse(self.__geom)
            if self.camCollisionQueue.getNumEntries() > 0:
                try:
                    self.camCollisionQueue.sortEntries()
                    self.handleCameraObstruction(self.camCollisionQueue.getEntry(0))
                except AssertionError:  # FIXME: Hacky.
                    pass
            if not self.__onLevelGround:
                self.handleCameraFloorInteraction()
        if not self.__idealCameraObstructed:
            self.nudgeCamera()
        if not self.__disableSmartCam:
            self.ccPusherTrav.traverse(self.__geom)
            self.putCameraFloorRayOnCamera()
        self.ccTravOnFloor.traverse(self.__geom)
        return Task.cont

    def positionCameraWithPusher(self, pos, lookAt):
        camera.setPos(pos)
        self.ccPusherTrav.traverse(self.__geom)
        camera.lookAt(lookAt)

    def nudgeCamera(self):
        CLOSE_ENOUGH = 0.1
        curCamPos = self.__instantaneousCamPos
        curCamHpr = camera.getHpr()
        targetCamPos = self.getCompromiseCameraPos()
        targetCamLookAt = self.getLookAtPoint()
        posDone = 0
        if Vec3(curCamPos - targetCamPos).length() <= CLOSE_ENOUGH:
            camera.setPos(targetCamPos)
            posDone = 1
        camera.setPos(targetCamPos)
        camera.lookAt(targetCamLookAt)
        targetCamHpr = camera.getHpr()
        hprDone = 0
        if Vec3(curCamHpr - targetCamHpr).length() <= CLOSE_ENOUGH:
            hprDone = 1
        if posDone and hprDone:
            return
        lerpRatio = 0.15
        lerpRatio = 1 - pow(1 - lerpRatio, globalClock.getDt() * 30.0)
        self.__instantaneousCamPos = targetCamPos * lerpRatio + curCamPos * (1 - lerpRatio)
        if self.__disableSmartCam or not self.__idealCameraObstructed:
            newHpr = targetCamHpr * lerpRatio + curCamHpr * (1 - lerpRatio)
        else:
            newHpr = targetCamHpr
        camera.setPos(self.__instantaneousCamPos)
        camera.setHpr(newHpr)

    def popCameraToDest(self):
        newCamPos = self.getCompromiseCameraPos()
        newCamLookAt = self.getLookAtPoint()
        self.positionCameraWithPusher(newCamPos, newCamLookAt)
        self.__instantaneousCamPos = camera.getPos()

    def handleCameraObstruction(self, camObstrCollisionEntry):
        collisionPoint = camObstrCollisionEntry.getSurfacePoint(self.ccLineNodePath)
        collisionVec = Vec3(collisionPoint - self.ccLine.getPointA())
        distance = collisionVec.length()
        self.__idealCameraObstructed = 1
        self.closestObstructionDistance = distance
        self.popCameraToDest()

    def handleCameraFloorInteraction(self):
        self.putCameraFloorRayOnCamera()
        self.ccTravFloor.traverse(self.__geom)
        if self.__onLevelGround:
            return
        if self.camFloorCollisionQueue.getNumEntries() == 0:
            return
        self.camFloorCollisionQueue.sortEntries()
        camObstrCollisionEntry = self.camFloorCollisionQueue.getEntry(0)
        camHeightFromFloor = camObstrCollisionEntry.getSurfacePoint(self.ccRayNodePath)[2]
        self.cameraZOffset = camera.getPos()[2] + camHeightFromFloor
        if self.cameraZOffset < 0:
            self.cameraZOffset = 0
        if self.__floorDetected == 0:
            self.__floorDetected = 1
            self.popCameraToDest()

    def lerpCameraFov(self, fov, time):
        taskMgr.remove('cam-fov-lerp-play')
        oldFov = base.camLens.getHfov()
        if abs(fov - oldFov) > 0.1:

            def setCamFov(fov):
                base.camLens.setMinFov(fov/(4./3.))

            self.camLerpInterval = LerpFunctionInterval(setCamFov, fromData=oldFov, toData=fov, duration=time, name='cam-fov-lerp')
            self.camLerpInterval.start()

    def setCameraFov(self, fov):
        self.fov = fov
        if not (self.isPageDown or self.isPageUp):
            base.camLens.setMinFov(self.fov/(4./3.))

    def gotoNode(self, node, eyeHeight = 3):
        possiblePoints = (Point3(3, 6, 0),
         Point3(-3, 6, 0),
         Point3(6, 6, 0),
         Point3(-6, 6, 0),
         Point3(3, 9, 0),
         Point3(-3, 9, 0),
         Point3(6, 9, 0),
         Point3(-6, 9, 0),
         Point3(9, 9, 0),
         Point3(-9, 9, 0),
         Point3(6, 0, 0),
         Point3(-6, 0, 0),
         Point3(6, 3, 0),
         Point3(-6, 3, 0),
         Point3(9, 9, 0),
         Point3(-9, 9, 0),
         Point3(0, 12, 0),
         Point3(3, 12, 0),
         Point3(-3, 12, 0),
         Point3(6, 12, 0),
         Point3(-6, 12, 0),
         Point3(9, 12, 0),
         Point3(-9, 12, 0),
         Point3(0, -6, 0),
         Point3(-3, -6, 0),
         Point3(0, -9, 0),
         Point3(-6, -9, 0))
        for point in possiblePoints:
            pos = self.positionExaminer.consider(node, point, eyeHeight)
            if pos:
                self.setPos(node, pos)
                self.lookAt(node)
                self.setHpr(self.getH() + random.choice((-10, 10)), 0, 0)
                return

        self.setPos(node, 0, 0, 0)

    def setCustomMessages(self, customMessages):
        self.customMessages = customMessages
        messenger.send('customMessagesChanged')

    def displayWhisper(self, fromId, chatString, whisperType):
        sender = None

        if isinstance(fromId, numbers.Number):
            sender = base.cr.identifyAvatar(fromId)

            if whisperType == WTNormal:
                chatString = '%s: %s' % (sender.getName(), chatString)

        whisper = WhisperPopup(chatString, ToontownGlobals.getInterfaceFont(), whisperType)

        if sender or isinstance(fromId, basestring):
            whisper.setClickable(fromId)

        whisper.manage(base.marginManager)
        base.playSfx(self.soundSystemMessage if whisperType == WTSystem else self.soundWhisper)

    def setAnimMultiplier(self, value):
        self.animMultiplier = value

    def getAnimMultiplier(self):
        return self.animMultiplier

    def runSound(self):
        self.soundWalk.stop()
        base.playSfx(self.soundRun, looping=1)

    def walkSound(self):
        self.soundRun.stop()
        base.playSfx(self.soundWalk, looping=1)

    def stopSound(self):
        self.soundRun.stop()
        self.soundWalk.stop()
		
    def disableSleeping(self):
        self.sleepDisabled = 1
        taskMgr.remove(self.uniqueName('sleepwatch'))
		
    def enableSleeping(self):
        self.sleepDisabled = 0
        if self.sleepCallback:
            self.startSleepWatch(self.sleepCallback)
	
    def wakeUp(self):
        if self.sleepDisabled:
            return
        if self.sleepCallback != None:
            taskMgr.remove(self.uniqueName('sleepwatch'))
            self.startSleepWatch(self.sleepCallback)
        self.lastMoved = globalClock.getFrameTime()
        if self.sleepFlag:
            self.sleepFlag = 0

    def gotoSleep(self):
        if self.sleepDisabled:
            return
        if not self.sleepFlag:
            self.b_setAnimState('Sleep', self.animMultiplier)
            self.sleepFlag = 1

    def forceGotoSleep(self):
        if self.hp > 0:
            self.sleepFlag = 0
            self.gotoSleep()

    def startSleepWatch(self, callback):
        if self.sleepDisabled:
            return
        self.sleepCallback = callback
        taskMgr.doMethodLater(self.sleepTimeout, callback, self.uniqueName('sleepwatch'))

    def stopSleepWatch(self):
        taskMgr.remove(self.uniqueName('sleepwatch'))
        self.sleepCallback = None

    def trackAnimToSpeed(self, task):
        speed, rotSpeed, slideSpeed = self.controlManager.getSpeeds()
        if speed != 0.0 or rotSpeed != 0.0 or inputState.isSet('jump'):
            if not self.movingFlag:
                self.movingFlag = 1
                self.stopLookAround()
        elif self.movingFlag:
            self.movingFlag = 0
            self.startLookAround()
        if self.movingFlag or self.hp <= 0:
            self.wakeUp()
        elif not self.sleepFlag:
            now = globalClock.getFrameTime()
            if now - self.lastMoved > self.sleepTimeout:
                self.gotoSleep()
        state = None
        if self.sleepFlag:
            state = 'Sleep'
        elif self.hp > 0:
            state = 'Happy'
        else:
            state = 'Sad'
        if state != self.lastState:
            self.lastState = state
            self.b_setAnimState(state, self.animMultiplier)
            self.setWalkSpeedNormal()
        if self.cheesyEffect == ToontownGlobals.CEFlatProfile or self.cheesyEffect == ToontownGlobals.CEFlatPortrait:
            needH = None
            if rotSpeed > 0.0:
                needH = -10
            elif rotSpeed < 0.0:
                needH = 10
            elif speed != 0.0:
                needH = 0
            if needH != None and self.lastNeedH != needH:
                node = self.getGeomNode().getChild(0)
                lerp = Sequence(LerpHprInterval(node, 0.5, Vec3(needH, 0, 0), blendType='easeInOut'), name='cheesy-lerp-hpr', autoPause=1)
                lerp.start()
                self.lastNeedH = needH
        else:
            self.lastNeedH = None
        action = self.setSpeed(speed, rotSpeed)
        if action != self.lastAction:
            self.lastAction = action
            if self.emoteTrack:
                self.emoteTrack.finish()
                self.emoteTrack = None
            if action == OTPGlobals.WALK_INDEX or action == OTPGlobals.REVERSE_INDEX:
                self.walkSound()
            elif action == OTPGlobals.RUN_INDEX:
                self.runSound()
            else:
                self.stopSound()
        return Task.cont

    def hasTrackAnimToSpeed(self):
        taskName = self.taskName('trackAnimToSpeed')
        return taskMgr.hasTaskNamed(taskName)

    def startTrackAnimToSpeed(self):
        taskName = self.taskName('trackAnimToSpeed')
        taskMgr.remove(taskName)
        task = Task.Task(self.trackAnimToSpeed)
        self.lastMoved = globalClock.getFrameTime()
        self.lastState = None
        self.lastAction = None
        self.trackAnimToSpeed(task)
        taskMgr.add(self.trackAnimToSpeed, taskName, 35)

    def stopTrackAnimToSpeed(self):
        taskName = self.taskName('trackAnimToSpeed')
        taskMgr.remove(taskName)
        self.stopSound()

    def startChat(self):
        self.chatMgr.start()
        self.accept(ToontownGlobals.ThinkPosHotkey, self.thinkPos)
        if self.__enableMarkerPlacement:
            self.accept(ToontownGlobals.PlaceMarkerHotkey, self.__placeMarker)

    def stopChat(self):
        self.chatMgr.stop()
        self.ignore(ToontownGlobals.ThinkPosHotkey)
        if self.__enableMarkerPlacement:
            self.ignore(ToontownGlobals.PlaceMarkerHotkey)

    def d_broadcastPositionNow(self):
        self.d_clearSmoothing()
        self.d_broadcastPosHpr()

    def travCollisionsLOS(self, n = None):
        if n == None:
            n = self.__geom
        self.ccTrav.traverse(n)

    def travCollisionsFloor(self, n = None):
        if n == None:
            n = self.__geom
        self.ccTravFloor.traverse(n)

    def travCollisionsPusher(self, n = None):
        if n == None:
            n = self.__geom
        self.ccPusherTrav.traverse(n)

    def __friendOnline(self, doId):
        friend = base.cr.identifyFriend(doId)
        if friend != None:
            self.setSystemMessage(doId, OTPLocalizer.WhisperFriendComingOnline % friend.getName())

    def __friendOffline(self, doId):
        friend = base.cr.identifyFriend(doId)
        if friend != None:
            self.setSystemMessage(0, OTPLocalizer.WhisperFriendLoggedOut % friend.getName())

    def clickedWhisper(self, doId):
        if isinstance(doId, basestring):
            webbrowser.open(doId, new=2, autoraise=True)
            return

        friend = base.cr.identifyFriend(doId)

        if friend != None:
            messenger.send('clickedNametag', [friend])
            self.chatMgr.whisperTo(friend.getName(), doId)

    def d_setParent(self, parentToken):
        DistributedSmoothNode.DistributedSmoothNode.d_setParent(self, parentToken)


@magicWord(category=CATEGORY_COMMUNITY_MANAGER)
def run():
    """
    Toggles debugging run speed.
    """
    inputState.set('debugRunning', inputState.isSet('debugRunning') != True)
    return 'Toggled debug run speed.'

@magicWord(category=CATEGORY_COMMUNITY_MANAGER)
def collisionsOff():
    """
    Turns collisions off.
    """
    base.localAvatar.collisionsOff()
    return 'Collisions are disabled.'

@magicWord(category=CATEGORY_COMMUNITY_MANAGER)
def collisionsOn():
    """
    Turns collisions on.
    """
    base.localAvatar.collisionsOn()
    return 'Collisions are enabled.'

@magicWord(category=CATEGORY_ADMINISTRATOR, types=[int])
def gravity(value):
    """
    Modifies the invoker's gravity. For default, use 0.
    """
    if value < 0:
        return 'Invalid gravity value!'
    if value == 0:
        base.localAvatar.controlManager.currentControls.setGravity(ToontownGlobals.GravityValue * 2.0)
    else:
        base.localAvatar.controlManager.currentControls.setGravity(value)

@magicWord(category=CATEGORY_COMMUNITY_MANAGER, types=[float, float, float])
def xyz(x, y, z):
    """
    Modifies the position of the invoker.
    """
    base.localAvatar.setPos(x, y, z)

@magicWord(category=CATEGORY_COMMUNITY_MANAGER, types=[float, float, float])
def hpr(h, p, r):
    """
    Modifies the rotation of the invoker.
    """
    base.localAvatar.setHpr(h, p, r)
