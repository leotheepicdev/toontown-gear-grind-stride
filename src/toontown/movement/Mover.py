from panda3d.core import LVector3f
from direct.directnotify import DirectNotifyGlobal

class Mover:
    notify = DirectNotifyGlobal.directNotify.newCategory('Mover')

    def __init__(self, objNodePath, fwdSpeed = 1, rotSpeed = 1):
        self.objNodePath = objNodePath
        self.fwdSpeed = fwdSpeed
        self.rotSpeed = rotSpeed
        self.dt = 1.0
        self.dtClock = globalClock.getFrameTime()
        self.movement = LVector3f(0)
        self.rotation = LVector3f(0)
        self.impulses = {}

    def destroy(self):
        for name in self.impulses.keys():
            Mover.notify.debug('removing impulse: %s' % name)
            self.removeImpulse(name)
    
    def setFwdSpeed(self, fwdSpeed):
        self.fwdSpeed = fwdSpeed

    def getFwdSpeed(self):
        return self.fwdSpeed

    def setRotSpeed(self, rotSpeed):
        self.rotSpeed = rotSpeed

    def getRotSpeed(self):
        return self.rotSpeed

    def getNodePath(self):
        return self.objNodePath

    def getDt(self):
        return self.dt
        
    def addShove(self, shove):
        self.movement += shove

    def addRotShove(self, rotShove):
        self.rotation += rotShove
        
    def integrate(self):
        if not self.objNodePath or self.objNodePath.isEmpty():
            return

        self.movement *= self.getDt()
        self.objNodePath.setFluidPos(self.objNodePath, self.movement)
        self.rotation *= self.getDt()
        self.objNodePath.setHpr(self.objNodePath, self.rotation)
        self.movement = LVector3f(0)
        self.rotation = LVector3f(0)

    def addImpulse(self, name, impulse):
        self.impulses[name] = impulse
        impulse._setMover(self)

    def removeImpulse(self, name):
        self.impulses[name]._clearMover(self)
        del self.impulses[name]
        
    def processImpulses(self, dt):
        self.dt = dt
        if self.getDt() == -1.0:
            clockDelta = globalClock.getFrameTime()
            self.dt = clockDelta - self.dtClock
            self.dtClock = clockDelta

        for impulse in self.impulses.values():
            impulse._process(self.getDt())

    def getCollisionEventName(self):
        return 'moverCollision-%s' % id(self)

    def move(self, dt = -1):
        self.processImpulses(dt)
        self.integrate()
