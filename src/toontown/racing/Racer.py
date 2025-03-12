from toontown.racing.DistributedVehicleAI import DistributedVehicleAI
from direct.distributed.ClockDelta import globalClockDelta

class Racer:

    def __init__(self, race, air, avId, zoneId):
        self.race = race
        self.air = air
        self.avId = avId
        self.avatar = self.air.doId2do.get(self.avId)
        self.kart = DistributedVehicleAI(self.air, self.avId)
        self.kart.generateWithRequired(zoneId)
        self.baseTime = 0
        self.exited = False
        self.finished = False
        self.hasGag = False
        self.gagType = 0
        self.anvilTarget = False
        self.maxLap = 1
        self.lapT = 0
        self.totalTime = 0
        self.timestamp = globalClockDelta.getRealNetworkTime()
        self.exitEvent = self.air.getAvatarExitEvent(self.avId)
        self.race.acceptOnce(self.exitEvent, self.race.unexpectedExit, extraArgs=[self.avId])
        
    def setLapT(self, numLaps, t, timestamp):
        self.maxLap = numLaps
        self.lapT = t
        self.totalTime += t
        self.timestamp = timestamp