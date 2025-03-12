from direct.directnotify import DirectNotifyGlobal
from direct.fsm import ClassicFSM, State
from toontown.base import ToontownGlobals
from toontown.building import Elevator
import FactoryExterior

class LawbotOfficeExterior(FactoryExterior.FactoryExterior):
    notify = DirectNotifyGlobal.directNotify.newCategory('LawbotOfficeExterior')

    def enterWalk(self, teleportIn = 0):
        FactoryExterior.FactoryExterior.enterWalk(self, teleportIn)
        self.ignore('teleportQuery')
        base.localAvatar.setTeleportAvailable(0)
