from panda3d.physics import ForceNode, LinearEulerIntegrator, LinearForce, LinearIntegrator, LinearVectorForce, PhysicsManager
from panda3d.core import BitMask32, CollideMask, CollisionNode, CollisionPlane, CollisionPolygon, NodePath, Plane, Point3, Texture, Vec3
from pandac import PandaModules as PM
from direct.directnotify.DirectNotifyGlobal import directNotify
from direct.task.Task import Task
from toontown.level import LevelConstants
from otp.otpbase import OTPGlobals
from toontown.cogdominium.DistCogdoLevelGame import DistCogdoLevelGame
from toontown.cogdominium import CogdoCraneGameConsts as GameConsts
from toontown.cogdominium.CogdoCraneGameBase import CogdoCraneGameBase
from toontown.base import ToontownTimer
from toontown.base import TTLocalizer as TTL
from toontown.base import ToontownGlobals

class DistCogdoCraneGame(CogdoCraneGameBase, DistCogdoLevelGame):
    notify = directNotify.newCategory('DistCogdoCraneGame')

    def __init__(self, cr):
        DistCogdoLevelGame.__init__(self, cr)
        self.cranes = {}
        self.moneyBags = {}

    def getTitle(self):
        return TTL.CogdoCraneGameTitle

    def getInstructions(self):
        return TTL.CogdoCraneGameInstructions

    def announceGenerate(self):
        DistCogdoLevelGame.announceGenerate(self)
        self.timer = ToontownTimer.ToontownTimer()
        self.timer.stash()

    def disable(self):
        self.timer.destroy()
        self.timer = None
        DistCogdoLevelGame.disable(self)
        return

    def enterLoaded(self):
        DistCogdoLevelGame.enterLoaded(self)
        self.lightning = loader.loadModel('phase_10/models/cogHQ/CBLightning.bam')
        self.magnet = loader.loadModel('phase_10/models/cogHQ/CBMagnet.bam')
        self.craneArm = loader.loadModel('phase_10/models/cogHQ/CBCraneArm.bam')
        self.controls = loader.loadModel('phase_10/models/cogHQ/CBCraneControls.bam')
        self.stick = loader.loadModel('phase_10/models/cogHQ/CBCraneStick.bam')
        self.cableTex = self.craneArm.findTexture('MagnetControl')
        self.moneyBag = loader.loadModel('phase_10/models/cashbotHQ/MoneyBag')
        self.geomRoot = PM.NodePath('geom')
        self.sceneRoot = self.geomRoot.attachNewNode('sceneRoot')
        self.sceneRoot.setPos(35.84, -115.46, 6.46)
        self.physicsMgr = PM.PhysicsManager()
        integrator = PM.LinearEulerIntegrator()
        self.physicsMgr.attachLinearIntegrator(integrator)
        fn = PM.ForceNode('gravity')
        self.fnp = self.geomRoot.attachNewNode(fn)
        gravity = PM.LinearVectorForce(0, 0, GameConsts.Settings.Gravity.get())
        fn.addForce(gravity)
        self.physicsMgr.addLinearForce(gravity)
        self._gravityForce = gravity
        self._gravityForceNode = fn

    def getSceneRoot(self):
        return self.sceneRoot

    def privGotSpec(self, levelSpec):
        DistCogdoLevelGame.privGotSpec(self, levelSpec)
        levelMgr = self.getEntity(LevelConstants.LevelMgrEntId)
        self.endVault = levelMgr.geom
        self.endVault.reparentTo(self.geomRoot)
        self.endVault.findAllMatches('**/MagnetArms').detach()
        self.endVault.findAllMatches('**/Safes').detach()
        self.endVault.findAllMatches('**/MagnetControlsAll').detach()
        cn = self.endVault.find('**/wallsCollision').node()
        cn.setIntoCollideMask(OTPGlobals.WallBitmask | ToontownGlobals.PieBitmask | PM.BitMask32.lowerOn(3) << 21)
        walls = self.endVault.find('**/RollUpFrameCillison')
        walls.detachNode()
        self.evWalls = self.replaceCollisionPolysWithPlanes(walls)
        self.evWalls.reparentTo(self.endVault)
        self.evWalls.stash()
        floor = self.endVault.find('**/EndVaultFloorCollision')
        floor.detachNode()
        self.evFloor = self.replaceCollisionPolysWithPlanes(floor)
        self.evFloor.reparentTo(self.endVault)
        self.evFloor.setName('floor')
        plane = PM.CollisionPlane(PM.Plane(PM.Vec3(0, 0, 1), PM.Point3(0, 0, -50)))
        planeNode = PM.CollisionNode('dropPlane')
        planeNode.addSolid(plane)
        planeNode.setCollideMask(ToontownGlobals.PieBitmask)
        self.geomRoot.attachNewNode(planeNode)

    def replaceCollisionPolysWithPlanes(self, model):
        newCollisionNode = PM.CollisionNode('collisions')
        newCollideMask = PM.BitMask32(0)
        planes = []
        collList = model.findAllMatches('**/+CollisionNode')
        if not collList:
            collList = [model]
        for cnp in collList:
            cn = cnp.node()
            if not isinstance(cn, PM.CollisionNode):
                self.notify.warning('Not a collision node: %s' % repr(cnp))
                break
            newCollideMask = newCollideMask | cn.getIntoCollideMask()
            for i in xrange(cn.getNumSolids()):
                solid = cn.getSolid(i)
                if isinstance(solid, PM.CollisionPolygon):
                    plane = PM.Plane(solid.getPlane())
                    planes.append(plane)
                else:
                    self.notify.warning('Unexpected collision solid: %s' % repr(solid))
                    newCollisionNode.addSolid(plane)

        newCollisionNode.setIntoCollideMask(newCollideMask)
        threshold = 0.1
        planes.sort(lambda p1, p2: p1.compareTo(p2, threshold))
        lastPlane = None
        for plane in planes:
            if lastPlane == None or plane.compareTo(lastPlane, threshold) != 0:
                cp = PM.CollisionPlane(plane)
                newCollisionNode.addSolid(cp)
                lastPlane = plane

        return PM.NodePath(newCollisionNode)

    def exitLoaded(self):
        self.fnp.removeNode()
        self.physicsMgr.clearLinearForces()
        self.geomRoot.removeNode()
        self._gravityForce = None
        self._gravityForceNode = None
        DistCogdoLevelGame.exitLoaded(self)
        return

    def toCraneMode(self):
        if self.cr:
            place = self.cr.playGame.getPlace()
            if place and hasattr(place, 'fsm'):
                place.setState('crane')

    def enterVisible(self):
        DistCogdoLevelGame.enterVisible(self)
        self.geomRoot.reparentTo(render)

    def placeEntranceElev(self, elev):
        elev.setPos(-10.63, -113.64, 6.03)
        elev.setHpr(90, 0, 0)

    def enterGame(self):
        DistCogdoLevelGame.enterGame(self)
        self._physicsTask = taskMgr.add(self._doPhysics, self.uniqueName('physics'), priority=25)
        self.evWalls.stash()
        self._startTimer()

    def _startTimer(self):
        timeLeft = GameConsts.Settings.GameDuration.get() - self.getCurrentGameTime()
        self.timer.posInTopRightCorner()
        self.timer.setTime(timeLeft)
        self.timer.countdown(timeLeft, self.timerExpired)
        self.timer.unstash()

    def _doPhysics(self, task):
        dt = globalClock.getDt()
        self.physicsMgr.doPhysics(dt)
        return Task.cont

    def exitGame(self):
        DistCogdoLevelGame.exitGame(self)
        self._physicsTask.remove()

    def enterFinish(self):
        DistCogdoLevelGame.enterFinish(self)
        timeLeft = 10 - (globalClock.getRealTime() - self.getFinishTime())
        self.timer.setTime(timeLeft)
        self.timer.countdown(timeLeft, self.timerExpired)
        self.timer.unstash()

    def timerExpired(self):
        pass
