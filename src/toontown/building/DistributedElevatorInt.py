from panda3d.core import NodePath
from direct.distributed.ClockDelta import *
from direct.interval.IntervalGlobal import *
from ElevatorConstants import *
from ElevatorUtils import *
import DistributedElevator
from toontown.base import ToontownGlobals
from direct.directnotify import DirectNotifyGlobal
from direct.fsm import ClassicFSM
from direct.fsm import State
from toontown.hood import ZoneUtil
from toontown.base import TTLocalizer

from toontown.cogdominium.CogdoInterior import CogdoInterior

class DistributedElevatorInt(DistributedElevator.DistributedElevator):

    def __init__(self, cr):
        DistributedElevator.DistributedElevator.__init__(self, cr)
        self.countdownTime = base.config.GetFloat('int-elevator-timeout', INTERIOR_ELEVATOR_COUNTDOWN_TIME)

    def setupElevator(self):
        self.leftDoor = self.bldg.leftDoorOut
        self.rightDoor = self.bldg.rightDoorOut
        DistributedElevator.DistributedElevator.setupElevator(self)

        if isinstance(base.cr.playGame.getPlace(), CogdoInterior):
            self.elevatorSphereNodePath.setY(self.elevatorSphereNodePath, -3)

    def forcedExit(self, avId):
        target_sz = base.localAvatar.defaultZone
        base.cr.playGame.getPlace().fsm.request('teleportOut', [{'loader': ZoneUtil.getLoaderName(target_sz),
          'where': ZoneUtil.getWhereName(target_sz, 1),
          'how': 'teleportIn',
          'hoodId': target_sz,
          'zoneId': target_sz,
          'shardId': None,
          'avId': -1}], force=1)
        return

    def enterWaitCountdown(self, ts):
        DistributedElevator.DistributedElevator.enterWaitCountdown(self, ts)
        self.acceptOnce('localToonLeft', self.__handleTeleportOut)
        self.startCountdownClock(self.countdownTime, ts)

    def __handleTeleportOut(self):
        self.sendUpdate('requestBuildingExit', [])

    def exitWaitCountdown(self):
        self.ignore('localToonLeft')
        DistributedElevator.DistributedElevator.exitWaitCountdown(self)

    def getZoneId(self):
        return self.bldg.getZoneId()

    def getElevatorModel(self):
        return self.bldg.elevatorModelOut
