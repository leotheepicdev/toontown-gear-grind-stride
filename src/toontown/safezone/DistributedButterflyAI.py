from direct.directnotify import DirectNotifyGlobal
from direct.distributed.DistributedObjectAI import DistributedObjectAI
from direct.distributed.ClockDelta import *
from direct.fsm import ClassicFSM, State
from direct.task import Task
import ButterflyGlobals, random

class DistributedButterflyAI(DistributedObjectAI):
    notify = DirectNotifyGlobal.directNotify.newCategory("DistributedButterflyAI")

    def __init__(self, air, playground, area, ownerId):
        DistributedObjectAI.__init__(self, air)
        self.playground = playground
        self.area = area
        self.ownerId = ownerId
        self.fsm = ClassicFSM.ClassicFSM('DistributedButterfliesAI', [State.State('off', self.enterOff, self.exitOff, ['Flying', 'Landed']), State.State('Flying', self.enterFlying, self.exitFlying, ['Landed']), State.State('Landed', self.enterLanded, self.exitLanded, ['Flying'])], 'off', 'off')
        self.fsm.enterInitialState()
        self.curPos, self.curIndex, self.destPos, self.destIndex, self.time = ButterflyGlobals.getFirstRoute(self.playground, self.area, self.ownerId)

    def delete(self):
        ButterflyGlobals.recycleIndex(self.curIndex, self.playground, self.area, self.ownerId)
        ButterflyGlobals.recycleIndex(self.destIndex, self.playground, self.area, self.ownerId)
        self.fsm.request('off')
        del self.fsm
        DistributedObjectAI.delete(self)

    def d_setState(self, stateIndex, curIndex, destIndex, time):
        self.sendUpdate('setState', [stateIndex,
         curIndex,
         destIndex,
         time,
         globalClockDelta.getRealNetworkTime()])

    def getArea(self):
        return [self.playground, self.area]

    def getState(self):
        return [self.stateIndex,
         self.curIndex,
         self.destIndex,
         self.time,
         globalClockDelta.getRealNetworkTime()]

    def start(self):
        self.fsm.request('Flying')

    def avatarEnter(self):
        if self.fsm.getCurrentState().getName() == 'Landed':
            self.__ready()

    def enterOff(self):
        self.stateIndex = ButterflyGlobals.OFF

    def exitOff(self):
        pass

    def enterFlying(self):
        self.stateIndex = ButterflyGlobals.FLYING
        ButterflyGlobals.recycleIndex(self.curIndex, self.playground, self.area, self.ownerId)
        self.d_setState(ButterflyGlobals.FLYING, self.curIndex, self.destIndex, self.time)
        taskMgr.doMethodLater(self.time, self.__handleArrival, self.uniqueName('butter-flying'))

    def exitFlying(self):
        taskMgr.remove(self.uniqueName('butter-flying'))

    def __handleArrival(self, task):
        self.curPos = self.destPos
        self.curIndex = self.destIndex
        self.fsm.request('Landed')
        return Task.done

    def enterLanded(self):
        self.stateIndex = ButterflyGlobals.LANDED
        self.time = random.random() * ButterflyGlobals.MAX_LANDED_TIME
        self.d_setState(ButterflyGlobals.LANDED, self.curIndex, self.destIndex, self.time)
        taskMgr.doMethodLater(self.time, self.__ready, self.uniqueName('butter-ready'))

    def exitLanded(self):
        taskMgr.remove(self.uniqueName('butter-ready'))

    def __ready(self, task = None):
        self.destPos, self.destIndex, self.time = ButterflyGlobals.getNextPos(self.curPos, self.playground, self.area, self.ownerId)
        self.fsm.request('Flying')
        return Task.done
