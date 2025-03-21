from panda3d.core import NodePath, Point3
from direct.distributed.ClockDelta import *
from direct.interval.IntervalGlobal import *
from direct.directnotify import DirectNotifyGlobal
from direct.distributed import DistributedNode
from direct.fsm import ClassicFSM
from direct.fsm import State
from direct.directutil import Mopath
from toontown.base import ToontownGlobals
from toontown.hood import FishAnimatedProp
from direct.actor import Actor
import FishingTargetGlobals
import math
from toontown.effects import Bubbles

class DistributedFishingTarget(DistributedNode.DistributedNode):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedFishingTarget')
    radius = 2.5

    def __init__(self, cr):
        DistributedNode.DistributedNode.__init__(self, cr)
        NodePath.__init__(self)
        self.pond = None
        self.centerPoint = (0, 0, 0)
        self.maxRadius = 1.0
        self.track = None
        self.pondDoId = None

    def generate(self):
        self.assign(render.attachNewNode('DistributedFishingTarget'))
        shadow = loader.loadModel('phase_3/models/props/drop_shadow')
        shadow.setPos(0, 0, -0.1)
        shadow.setScale(0.33)
        shadow.setColorScale(1, 1, 1, 0.75)
        shadow.reparentTo(self)
        self.bubbles = Bubbles.Bubbles(self, render)
        self.bubbles.renderParent.setDepthWrite(0)
        self.bubbles.start()
        self.fish = FishAnimatedProp.FishAnimatedProp(self)
        self.fish.enter()
        DistributedNode.DistributedNode.generate(self)

    def disable(self):
        if self.track:
            self.track.finish()
            self.track = None
        self.bubbles.destroy()
        del self.bubbles
        self.fish.exit()
        self.fish.delete()
        del self.fish
        if self.pond:
            self.pond.removeTarget(self)
        self.pond = None
        self.ignore('generate-%d' % self.pondDoId)
        DistributedNode.DistributedNode.disable(self)

    def delete(self):
        del self.pond
        DistributedNode.DistributedNode.delete(self)

    def setPondDoId(self, pondDoId):
        self.pondDoId = pondDoId
        if pondDoId in self.cr.doId2do:
            self.setPond(self.cr.doId2do[pondDoId])
        else:
            self.acceptOnce('generate-%d' % pondDoId, self.setPond)

    def setPond(self, pond):
        self.pond = pond
        self.pond.addTarget(self)
        self.centerPoint = FishingTargetGlobals.getTargetCenter(self.pond.getArea())
        self.maxRadius = FishingTargetGlobals.getTargetRadius(self.pond.getArea())

    def getDestPos(self, angle, radius):
        x = radius * math.cos(angle) + self.centerPoint[0]
        y = radius * math.sin(angle) + self.centerPoint[1]
        z = self.centerPoint[2]
        return (x, y, z)

    def setState(self, stateIndex, angle, radius, time, timeStamp):
        ts = globalClockDelta.localElapsedTime(timeStamp)
        pos = self.getDestPos(angle, radius)
        if self.track and self.track.isPlaying():
            self.track.finish()
        self.track = Sequence(LerpPosInterval(self, time - ts, Point3(*pos), blendType='easeInOut'))
        self.track.start()

    def getRadius(self):
        return self.radius
