from panda3d.core import CollisionNode, CollisionTube, NodePath, Point3
from direct.directnotify import DirectNotifyGlobal
from direct.distributed import ClockDelta, DistributedObject
from direct.fsm import ClassicFSM, State
from direct.interval.IntervalGlobal import *
import DistributedToon
import NPCToons
from lib.nametag.NametagGroup import NametagGroup
from toontown.quest import QuestChoiceGui, Quests
from toontown.base import ToontownGlobals

class DistributedNPCToonBase(DistributedToon.DistributedToon):

    def __init__(self, cr):
        try:
            self.DistributedNPCToon_initialized
        except:
            self.DistributedNPCToon_initialized = 1
            DistributedToon.DistributedToon.__init__(self, cr)
            self.__initCollisions()
            self.setPickable(0)
            self.setPlayerType(NametagGroup.CCNonPlayer)

    def disable(self):
        self.ignore('enter' + self.cSphereNode.getName())
        DistributedToon.DistributedToon.disable(self)

    def delete(self):
        try:
            self.DistributedNPCToon_deleted
        except:
            self.DistributedNPCToon_deleted = 1
            self.__deleteCollisions()
            DistributedToon.DistributedToon.delete(self)

    def generate(self):
        DistributedToon.DistributedToon.generate(self)
        self.cSphereNode.setName(self.uniqueName('NPCToon'))
        self.detectAvatars()
        self.setParent(ToontownGlobals.SPRender)
        self.startLookAround()

    def generateToon(self):
        self.setLODs()
        self.generateToonLegs()
        self.generateToonHead()
        self.generateToonTorso()
        self.generateToonColor()
        self.parentToonParts()
        self.rescaleToon()
        self.resetHeight()
        self.rightHands = []
        self.leftHands = []
        self.headParts = []
        self.hipsParts = []
        self.torsoParts = []
        self.legsParts = []
        self.__bookActors = []
        self.__holeActors = []

    def announceGenerate(self):
        self.initToonState()
        DistributedToon.DistributedToon.announceGenerate(self)

    def initToonState(self):
        self.setAnimState('neutral', 0.9, None, None)
        npcOrigin = render.find('**/npc_origin_' + str(self.posIndex))
        if not npcOrigin.isEmpty():
            self.reparentTo(npcOrigin)
            self.initPos()
        elif self.name in NPCToons.HqPositions:
            pos = NPCToons.HqPositions[self.name]
            self.setPos(*pos[0])
            self.setH(pos[1])
        

    def initPos(self):
        self.clearMat()

    def wantsSmoothing(self):
        return 0

    def detectAvatars(self):
        self.accept('enter' + self.cSphereNode.getName(), self.handleCollisionSphereEnter)

    def ignoreAvatars(self):
        self.ignore('enter' + self.cSphereNode.getName())

    def getCollSphereRadius(self):
        return 3.25

    def __initCollisions(self):
        self.cSphere = CollisionTube(0.0, 1.0, 0.0, 0.0, 1.0, 5.0, self.getCollSphereRadius())
        self.cSphere.setTangible(0)
        self.cSphereNode = CollisionNode('cSphereNode')
        self.cSphereNode.addSolid(self.cSphere)
        self.cSphereNodePath = self.attachNewNode(self.cSphereNode)
        self.cSphereNodePath.hide()
        self.cSphereNode.setCollideMask(ToontownGlobals.WallBitmask)

    def __deleteCollisions(self):
        del self.cSphere
        del self.cSphereNode
        self.cSphereNodePath.removeNode()
        del self.cSphereNodePath

    def handleCollisionSphereEnter(self, collEntry):
        pass

    def setupAvatars(self, av):
        self.ignoreAvatars()
        self.lookAtAvatar(av)
    
    def lookAtAvatar(self, av):
        av.headsUp(self, 0, 0, 0)
        self.headsUp(av, 0, 0, 0)
        av.stopLookAround()
        av.lerpLookAt(Point3(-0.5, 4, 0), time=0.5)
        self.stopLookAround()
        self.lerpLookAt(Point3(av.getPos(self)), time=0.5)

    def b_setPageNumber(self, paragraph, pageNumber):
        self.setPageNumber(paragraph, pageNumber)
        self.d_setPageNumber(paragraph, pageNumber)

    def d_setPageNumber(self, paragraph, pageNumber):
        timestamp = ClockDelta.globalClockDelta.getFrameNetworkTime()
        self.sendUpdate('setPageNumber', [paragraph, pageNumber, timestamp])

    def freeAvatar(self):
        base.localAvatar.posCamera(0, 0)
        base.cr.playGame.getPlace().setState('walk')

    def setPositionIndex(self, posIndex):
        self.posIndex = posIndex
