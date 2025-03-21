from TrolleyConstants import *
from direct.directnotify import DirectNotifyGlobal
from direct.distributed import DistributedObjectAI
from direct.distributed.ClockDelta import *
from direct.fsm import ClassicFSM, State
from direct.showbase import RandomNumGen
from direct.task import Task
from otp.ai.AIBase import *
from toontown.base import ToontownGlobals
from toontown.base.ToontownGlobals import *

class DistributedPicnicBasketAI(DistributedObjectAI.DistributedObjectAI):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedPicnicBasketAI')

    def __init__(self, air, tableNumber, x, y, z, h, p, r):
        DistributedObjectAI.DistributedObjectAI.__init__(self, air)
        self.seats = [None, None, None, None]
        self.posHpr = (x, y, z, h, p, r)
        self.tableNumber = int(tableNumber)
        self.seed = RandomNumGen.randHash(globalClock.getRealTime())
        self.accepting = 0
        self.numPlayersExiting = 0
        self.trolleyCountdownTime = simbase.config.GetFloat('picnic-countdown-time', ToontownGlobals.PICNIC_COUNTDOWN_TIME)
        self.fsm = ClassicFSM.ClassicFSM(
            'DistributedPicnicBasketAI',
            [
                State.State('off', self.enterOff, self.exitOff, ['waitEmpty']),
                State.State('waitEmpty', self.enterWaitEmpty, self.exitWaitEmpty, ['waitCountdown']),
                State.State('waitCountdown', self.enterWaitCountdown, self.exitWaitCountdown, ['waitEmpty'])
            ], 'off', 'off')
        self.fsm.enterInitialState()

    def delete(self):
        self.fsm.requestFinalState()
        del self.fsm
        DistributedObjectAI.DistributedObjectAI.delete(self)

    def findAvailableSeat(self):
        for i in xrange(len(self.seats)):
            if self.seats[i] is None:
                return i

    def findAvatar(self, avId):
        for i in xrange(len(self.seats)):
            if self.seats[i] == avId:
                return i

    def countFullSeats(self):
        avCounter = 0
        for i in self.seats:
            if i:
                avCounter += 1
        return avCounter

    def rejectingBoardersHandler(self, avId, si):
        self.rejectBoarder(avId)

    def rejectBoarder(self, avId):
        self.sendUpdateToAvatarId(avId, 'rejectBoard', [avId])

    def acceptingBoardersHandler(self, avId, si):
        self.notify.debug('acceptingBoardersHandler')
        seatIndex = si
        if not seatIndex is None:
            self.acceptBoarder(avId, seatIndex)

    def acceptBoarder(self, avId, seatIndex):
        self.notify.debug('acceptBoarder %d' % avId)
        if self.findAvatar(avId) is not None:
            return None
        self.seats[seatIndex] = avId
        self.acceptOnce(
            self.air.getAvatarExitEvent(avId), self.__handleUnexpectedExit,
            extraArgs=[avId])
        self.timeOfBoarding = globalClock.getRealTime()
        self.sendUpdate('fillSlot' + str(seatIndex), [avId])
        self.waitCountdown()

    def _DistributedPicnicBasketAI__handleUnexpectedExit(self, avId):
        self.notify.warning('Avatar: ' + str(avId) + ' has exited unexpectedly')
        seatIndex = self.findAvatar(avId)
        if seatIndex == None:
            return
        self.clearFullNow(seatIndex)
        self.clearEmptyNowUnexpected(seatIndex)
        if self.countFullSeats() == 0:
            self.waitEmpty()

    def clearEmptyNowUnexpected(self, seatIndex):
        self.sendUpdate('emptySlot' + str(seatIndex), [1, globalClockDelta.getRealNetworkTime()])

    def rejectingExitersHandler(self, avId):
        self.rejectExiter(avId)

    def rejectExiter(self, avId):
        pass

    def acceptingExitersHandler(self, avId):
        self.acceptExiter(avId)

    def acceptExiter(self, avId):
        seatIndex = self.findAvatar(avId)
        if seatIndex == None:
            return
        self.clearFullNow(seatIndex)
        self.sendUpdate('emptySlot' + str(seatIndex), [avId, globalClockDelta.getRealNetworkTime()])
        taskMgr.doMethodLater(
            TOON_EXIT_TIME, self.clearEmptyNow,
            self.uniqueName('clearEmpty-%s' % seatIndex), extraArgs=(seatIndex,))

    def clearEmptyNow(self, seatIndex):
        self.notify.debugStateCall(self)
        self.sendUpdate('emptySlot' + str(seatIndex), [0, globalClockDelta.getRealNetworkTime()])

    def clearFullNow(self, seatIndex):
        avId = self.seats[seatIndex]
        if avId == 0:
            self.notify.warning('Clearing an empty seat index: ' + str(seatIndex) + ' ... Strange...')
        else:
            self.seats[seatIndex] = None
            self.sendUpdate('fillSlot' + str(seatIndex), [0])
            self.ignore(self.air.getAvatarExitEvent(avId))

    def d_setState(self, state, seed):
        self.sendUpdate('setState', [state, seed, globalClockDelta.getRealNetworkTime()])

    def getState(self):
        return self.fsm.getCurrentState().getName()

    def requestBoard(self, si):
        self.notify.debug('requestBoard')
        avId = self.air.getAvatarIdFromSender()
        if self.findAvatar(avId) != None:
            self.notify.warning('Ignoring multiple requests from %s to board.' % avId)
            return None
        av = self.air.doId2do.get(avId)
        if av:
            if av.hp > 0 and self.accepting and self.seats[si] == None:
                self.notify.debug('accepting boarder %d' % avId)
                self.acceptingBoardersHandler(avId, si)
            else:
                self.notify.debug('rejecting boarder %d' % avId)
                self.rejectingBoardersHandler(avId, si)
        else:
            self.notify.warning('avid: %s does not exist, but tried to board a trolley' % avId)

    def requestExit(self, *args):
        self.notify.debug('requestExit')
        avId = self.air.getAvatarIdFromSender()
        av = self.air.doId2do.get(avId)
        if av:
            if self.countFullSeats() > 0:
                newArgs = (avId,) + args
                self.numPlayersExiting += 1
                if self.accepting:
                    self.acceptingExitersHandler(*newArgs)
                else:
                    self.rejectingExitersHandler(*newArgs)
            else:
                self.notify.debug('Player tried to exit after AI already kicked everyone out')
        else:
            self.notify.warning('avId: %s does not exist, but tried to exit a trolley' % avId)

    def doneExit(self):
        if self.numPlayersExiting > 0:
            self.numPlayersExiting -= 1
            if self.numPlayersExiting == 0 and self.countFullSeats() == 0:
                self.waitEmpty()

    def start(self):
        self.waitEmpty()

    def enterOff(self):
        self.accepting = 0
        if hasattr(self, 'doId'):
            for seatIndex in xrange(4):
                taskMgr.remove(self.uniqueName('clearEmpty-' + str(seatIndex)))

    def exitOff(self):
        self.accepting = 0

    def waitEmptyTask(self, task):
        self.waitEmpty()
        return Task.done

    def waitEmpty(self):
        self.fsm.request('waitEmpty')

    def enterWaitEmpty(self):
        self.notify.debugStateCall(self)
        self.d_setState('waitEmpty', self.seed)
        self.seats = [None, None, None, None]
        self.accepting = 1

    def exitWaitEmpty(self):
        self.notify.debugStateCall(self)
        self.accepting = 0

    def waitCountdown(self):
        self.notify.debugStateCall(self)
        self.fsm.request('waitCountdown')

    def enterWaitCountdown(self):
        self.notify.debugStateCall(self)
        self.d_setState('waitCountdown', self.seed)
        self.accepting = 1
        taskMgr.doMethodLater(self.trolleyCountdownTime, self.timeToGoTask, self.uniqueName('countdown-timer'))

    def timeToGoTask(self, task):
        self.accepting = 0
        if self.countFullSeats() > 0:
            for x in xrange(len(self.seats)):
                if not self.seats[x] == None:
                    self.sendUpdateToAvatarId(self.seats[x], 'setPicnicDone', [])
                    self.acceptExiter(self.seats[x])
                    self.numPlayersExiting += 1
        self.waitEmpty()
        return Task.done

    def exitWaitCountdown(self):
        self.notify.debugStateCall(self)
        self.accepting = 0
        taskMgr.remove(self.uniqueName('countdown-timer'))

    def getPosHpr(self):
        return self.posHpr

    def getTableNumber(self):
        return self.tableNumber
