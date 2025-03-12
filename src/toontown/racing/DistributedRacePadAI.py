from direct.directnotify import DirectNotifyGlobal
from toontown.racing.DistributedKartPadAI import DistributedKartPadAI
from toontown.racing.DistributedRaceAI import DistributedRaceAI
from toontown.racing import RaceGlobals
from direct.fsm.FSM import FSM
from direct.distributed.ClockDelta import *
from direct.task import *
from toontown.racing.KartShopGlobals import KartGlobals

#TODO - change race type

class DistributedRacePadAI(DistributedKartPadAI, FSM):
    notify = DirectNotifyGlobal.directNotify.newCategory("DistributedRacePadAI")
    defaultTransitions = {'Off': ['WaitEmpty'],
     'WaitEmpty': ['WaitCountdown', 'Off'],
     'WaitCountdown': ['WaitEmpty',
                       'WaitBoarding',
                       'Off',
                       'AllAboard'],
     'WaitBoarding': ['AllAboard', 'WaitEmpty', 'Off'],
     'AllAboard': ['Off', 'WaitEmpty', 'WaitCountdown']}

    def __init__(self, air):
        DistributedKartPadAI.__init__(self, air)
        FSM.__init__(self, 'DistributedRacePadAI')
        self.air = air
        self.avIds = []
        self.trackId, self.trackType = [None, None]
        self.lastTime = globalClockDelta.getRealNetworkTime()
        self.index = -1
        self.nameType = 'urban'

    def generate(self):
        DistributedKartPadAI.generate(self)
        self.b_setState('WaitEmpty', globalClockDelta.getRealNetworkTime())

    def enterOff(self):
        pass

    def exitOff(self):
        pass

    def enterWaitEmpty(self):
        taskMgr.doMethodLater(30, DistributedRacePadAI.changeTrack, 'changeTrack%i' % self.doId, [self])

    def exitWaitEmpty(self):
        taskMgr.remove('changeTrack%i' % self.doId)

    def enterWaitCountdown(self):
        taskMgr.doMethodLater(30, DistributedRacePadAI.startRace, 'startRace%i' % self.doId, [self])

    def exitWaitCountdown(self):
        taskMgr.remove('startRace%i' % self.doId)

    def enterWaitBoarding(self):
        pass

    def exitWaitBoarding(self):
        pass

    def enterAllAboard(self):
        taskMgr.doMethodLater(2, self.createRace, 'createRace%i' % self.doId)

    def exitAllAboard(self):
        self.avIds = []

    def changeTrack(self):
        nri = RaceGlobals.getNextRaceInfo(self.trackId, self.nameType, self.index)
        self.b_setTrackInfo([nri[0], nri[1]])
        taskMgr.doMethodLater(30, DistributedRacePadAI.changeTrack, 'changeTrack%i' % self.doId, [self])
                
    def startRace(self):
        for block in self.startingBlocks:
            if block.currentMovie:
                if not self.state == 'WaitBoarding':
                    self.b_setState('WaitBoarding', globalClockDelta.getRealNetworkTime())
                return
        if self.trackType in (RaceGlobals.ToonBattle, RaceGlobals.Circuit):
            if len(self.avIds) < 2:
                for block in self.startingBlocks:
                    if block.avId != 0:
                        block.normalExit()
                self.b_setState('WaitEmpty', globalClockDelta.getRealNetworkTime())
                return
        self.b_setState('AllAboard', globalClockDelta.getRealNetworkTime())
            
    def addAvBlock(self, avId, startingBlock):
        av = self.air.doId2do.get(avId)
        if not av:
            return
        if not av.hasKart():
            return KartGlobals.ERROR_CODE.eNoKart
        if self.state == 'Off':
            return KartGlobals.ERROR_CODE.eBoardOver
        if self.state in ('WaitBoarding', 'AllAboard'):
            return KartGlobals.ERROR_CODE.eBoardOver
        if RaceGlobals.getEntryFee(self.trackId, self.trackType) > av.getTickets():
            return KartGlobals.ERROR_CODE.eTickets
        self.avIds.append(avId)
        if not self.state == 'WaitCountdown':
            self.b_setState('WaitCountdown', globalClockDelta.getRealNetworkTime())
        return KartGlobals.ERROR_CODE.success
        
    def removeAvBlock(self, avId, startingBlocks):
        if avId in self.avIds:
            self.avIds.remove(avId)
            
    def kartMovieDone(self):
        if len(self.avIds) == 0 and not self.state == 'WaitEmpty':
            self.b_setState('WaitEmpty', globalClockDelta.getRealNetworkTime())
        if self.state == 'WaitBoarding':
            self.startRace()
        
    def createRace(self, task=None):
        circuitLoop = []
        lapCount = 3
        if self.trackType == RaceGlobals.Circuit:
            circuitLoop = RaceGlobals.getCircuitLoop(self.trackId)
        raceZone = self.air.raceMgr.createRace(self.trackId, self.trackType, lapCount, self.avIds, circuitLoop=circuitLoop[1:], circuitPoints={}, circuitTimes={})
        for block in self.startingBlocks:
            if block.avId != 0:
                self.sendUpdateToAvatarId(block.avId, 'setRaceZone', [raceZone])
                block.raceExit()
        if task: 
            return task.done

    def setState(self, state, timeStamp):
        self.lastTime = globalClockDelta.getRealNetworkTime()
        self.request(state)

    def d_setState(self, state, timeStamp):
        self.sendUpdate('setState', [state, timeStamp])

    def b_setState(self, state, timeStamp):
        self.setState(state, timeStamp)
        self.d_setState(state, timeStamp)

    def getState(self):
        return [self.state, self.lastTime]

    def getTrackInfo(self):
        return [self.trackId, self.trackType]

    def setTrackInfo(self, trackInfo):
        self.trackId, self.trackType = trackInfo

    def d_setTrackInfo(self, trackInfo):
        self.sendUpdate('setTrackInfo',  [trackInfo])

    def b_setTrackInfo(self, trackInfo):
        self.setTrackInfo(trackInfo)
        self.d_setTrackInfo(trackInfo)
