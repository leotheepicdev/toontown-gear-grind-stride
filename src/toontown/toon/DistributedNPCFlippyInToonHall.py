from panda3d.core import lookAt
from DistributedNPCToon import *

class DistributedNPCFlippyInToonHall(DistributedNPCToon):

    def __init__(self, cr):
        DistributedNPCToon.__init__(self, cr)
        self.toonTag = 'Mayor'

    def getCollSphereRadius(self):
        return 4

    def initPos(self):
        self.clearMat()
        self.setScale(1.25)

    def handleCollisionSphereEnter(self, collEntry):
        base.cr.playGame.getPlace().fsm.request('quest', [self])
        self.sendUpdate('avatarEnter', [])
        self.nametag3d.setDepthTest(0)
        self.nametag3d.setBin('fixed', 0)
        self.lookAt(base.localAvatar)
