from direct.distributed.ClockDelta import *
from direct.fsm import ClassicFSM
from direct.fsm import State
from direct.task import Task
from otp.ai.AIBase import *
from toontown.building import DistributedElevatorExtAI
from toontown.building.ElevatorConstants import *
from toontown.base import ToontownGlobals


class DistributedLawOfficeElevatorExtAI(DistributedElevatorExtAI.DistributedElevatorExtAI):
    def __init__(self, air, bldg, lawOfficeId, entranceId):
        DistributedElevatorExtAI.DistributedElevatorExtAI.__init__(self, air, bldg)
        self.lawOfficeId = lawOfficeId
        self.entranceId = entranceId

    def getEntranceId(self):
        return self.entranceId

    def elevatorClosed(self):
        numPlayers = self.countFullSeats()
        if numPlayers > 0:
            players = []
            for i in self.seats:
                if i not in [
                    None,
                    0]:
                    players.append(i)
                    continue
            lawOfficeZone = self.bldg.createLawOffice(self.lawOfficeId, self.entranceId, players)
            for seatIndex in xrange(len(self.seats)):
                avId = self.seats[seatIndex]
                if avId:
                    self.sendUpdateToAvatarId(avId, 'setLawOfficeInteriorZone', [lawOfficeZone])
                    self.clearFullNow(seatIndex)
        else:
            self.notify.warning('The elevator left, but was empty.')
        self.fsm.request('closed')

    def enterClosed(self):
        DistributedElevatorExtAI.DistributedElevatorExtAI.enterClosed(self)
        self.fsm.request('opening')

    def sendAvatarsToDestination(self, avIdList):
        if len(avIdList) > 0:
            officeZone = self.bldg.createLawOffice(self.lawOfficeId, self.entranceId, avIdList)
            for avId in avIdList:
                if avId:
                    self.sendUpdateToAvatarId(avId, 'setLawOfficeInteriorZoneForce', [officeZone])
