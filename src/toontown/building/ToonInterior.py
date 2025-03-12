from panda3d.core import ModelPool, Texture, TexturePool
from direct.directnotify import DirectNotifyGlobal
from direct.fsm import ClassicFSM, State
from direct.fsm import StateData
from direct.showbase import DirectObject
from direct.task import Task
import DistributedToonInterior
from toontown.distributed.TelemetryLimiter import RotationLimitToH, TLGatherAllAvs
from toontown.hood import Place
from toontown.hood import ZoneUtil
from lib.nametag.NametagConstants import *
from lib.nametag import NametagGlobals
from toontown.toon import HealthForceAcknowledge
from toontown.toon import NPCForceAcknowledge
from toontown.base import TTLocalizer
from toontown.base import ToontownGlobals
from toontown.base.ToonBaseGlobal import *
from toontown.building import Elevator

##[x, y, h]
InteriorTypes = {'toon_interior':[1.0, 13.0, 8.0],
                 'toon_interior_2':[1.0, 13.0, 8.0],
                 'toon_interior_L':[10.0, 7.5, -70.0],
                 'toon_interior_T':[-1.0, 5.0, 14.0]
}

class ToonInterior(Place.Place):
    notify = DirectNotifyGlobal.directNotify.newCategory('ToonInterior')

    def __init__(self, loader, parentFSMState, doneEvent):
        Place.Place.__init__(self, loader, doneEvent)
        self.dnaFile = 'phase_7/models/modules/toon_interior'
        self.isInterior = 1
        self.hfaDoneEvent = 'hfaDoneEvent'
        self.npcfaDoneEvent = 'npcfaDoneEvent'
        self.fsm = ClassicFSM.ClassicFSM('ToonInterior', [State.State('start', self.enterStart, self.exitStart, ['doorIn', 'teleportIn']),
         State.State('walk', self.enterWalk, self.exitWalk, ['sit',
          'stickerBook',
          'doorOut',
          'elevator',
          'teleportOut',
          'quest',
          'purchase',
          'phone',
          'stopped',
          'pet',
          'NPCFA']),
         State.State('sit', self.enterSit, self.exitSit, ['walk']),
         State.State('stickerBook', self.enterStickerBook, self.exitStickerBook, ['walk',
          'sit',
          'doorOut',
          'elevator',
          'teleportOut',
          'quest',
          'purchase',
          'phone',
          'stopped',
          'pet',
          'NPCFA']),
         State.State('NPCFA', self.enterNPCFA, self.exitNPCFA, ['NPCFAReject', 'HFA', 'teleportOut', 'doorOut']),
         State.State('NPCFAReject', self.enterNPCFAReject, self.exitNPCFAReject, ['walk']),
         State.State('HFA', self.enterHFA, self.exitHFA, ['HFAReject', 'teleportOut', 'tunnelOut']),
         State.State('HFAReject', self.enterHFAReject, self.exitHFAReject, ['walk']),
         State.State('doorIn', self.enterDoorIn, self.exitDoorIn, ['walk', 'stopped']),
         State.State('doorOut', self.enterDoorOut, self.exitDoorOut, ['walk', 'stopped']),
         State.State('elevator', self.enterElevator, self.exitElevator, ['walk']),
         State.State('teleportIn', self.enterTeleportIn, self.exitTeleportIn, ['walk']),
         State.State('teleportOut', self.enterTeleportOut, self.exitTeleportOut, ['teleportIn']),
         State.State('quest', self.enterQuest, self.exitQuest, ['walk', 'doorOut']),
         State.State('purchase', self.enterPurchase, self.exitPurchase, ['walk', 'doorOut']),
         State.State('pet', self.enterPet, self.exitPet, ['walk']),
         State.State('phone', self.enterPhone, self.exitPhone, ['walk', 'doorOut']),
         State.State('stopped', self.enterStopped, self.exitStopped, ['walk', 'doorOut']),
         State.State('final', self.enterFinal, self.exitFinal, ['start'])], 'start', 'final')
        self.parentFSMState = parentFSMState
        self.elevatorDoneEvent = 'elevatorDone'

    def load(self):
        Place.Place.load(self)
        self.parentFSMState.addChild(self.fsm)

    def unload(self):
        Place.Place.unload(self)
        self.parentFSMState.removeChild(self.fsm)
        del self.parentFSMState
        del self.fsm
        ModelPool.garbageCollect()
        TexturePool.garbageCollect()

    def enter(self, requestStatus):
        self.zoneId = requestStatus['zoneId']
        self.fsm.enterInitialState()
        messenger.send('enterToonInterior')
        self.accept('doorDoneEvent', self.handleDoorDoneEvent)
        self.accept('DistributedDoor_doorTrigger', self.handleDoorTrigger)
        volume = requestStatus.get('musicVolume', 0.7)
        base.playMusic(self.loader.activityMusic, looping=1, volume=volume)
        self._telemLimiter = TLGatherAllAvs('ToonInterior', RotationLimitToH)
        NametagGlobals.setMasterArrowsOn(1)
        self.fsm.request(requestStatus['how'], [requestStatus])

    def exit(self):
        self.ignoreAll()
        messenger.send('exitToonInterior')
        self._telemLimiter.destroy()
        del self._telemLimiter
        NametagGlobals.setMasterArrowsOn(0)
        self.loader.activityMusic.stop()

    def setState(self, state):
        self.fsm.request(state)

    def doRequestLeave(self, requestStatus):
        self.fsm.request('NPCFA', [requestStatus])

    def enterNPCFA(self, requestStatus):
        self.acceptOnce(self.npcfaDoneEvent, self.enterNPCFACallback, [requestStatus])
        self.npcfa = NPCForceAcknowledge.NPCForceAcknowledge(self.npcfaDoneEvent)
        self.npcfa.enter()

    def exitNPCFA(self):
        self.ignore(self.npcfaDoneEvent)

    def enterNPCFACallback(self, requestStatus, doneStatus):
        self.npcfa.exit()
        del self.npcfa
        if doneStatus['mode'] == 'complete':
            outHow = {'teleportIn': 'teleportOut',
             'tunnelIn': 'tunnelOut',
             'doorIn': 'doorOut'}
            self.fsm.request(outHow[requestStatus['how']], [requestStatus])
        elif doneStatus['mode'] == 'incomplete':
            self.fsm.request('NPCFAReject')
        else:
            self.notify.error('Unknown done status for NPCForceAcknowledge: ' + `doneStatus`)

    def enterNPCFAReject(self):
        self.fsm.request('walk')

    def exitNPCFAReject(self):
        pass

    def enterHFA(self, requestStatus):
        self.acceptOnce(self.hfaDoneEvent, self.enterHFACallback, [requestStatus])
        self.hfa = HealthForceAcknowledge.HealthForceAcknowledge(self.hfaDoneEvent)
        self.hfa.enter(1)

    def exitHFA(self):
        self.ignore(self.hfaDoneEvent)

    def enterHFACallback(self, requestStatus, doneStatus):
        self.hfa.exit()
        del self.hfa
        if doneStatus['mode'] == 'complete':
            outHow = {'teleportIn': 'teleportOut',
             'tunnelIn': 'tunnelOut',
             'doorIn': 'doorOut'}
            self.fsm.request(outHow[requestStatus['how']], [requestStatus])
        elif doneStatus['mode'] == 'incomplete':
            self.fsm.request('HFAReject')
        else:
            self.notify.error('Unknown done status for HealthForceAcknowledge: ' + `doneStatus`)

    def enterHFAReject(self):
        self.fsm.request('walk')

    def exitHFAReject(self):
        pass

    def enterTeleportIn(self, requestStatus):
        modelType = DistributedToonInterior.DistributedToonInterior(base.cr).getModelType(self.getZoneId())
        if self.zoneId == ToontownGlobals.ToonHall:
            base.localAvatar.setPosHpr(-63.5, 30.5, ToontownGlobals.FloorOffset, 90.0, 0.0, 0.0)
        elif ZoneUtil.isHQ(self.zoneId):
            base.localAvatar.setPosHpr(-5.5, -1.5, ToontownGlobals.FloorOffset, 0.0, 0.0, 0.0)
        elif ZoneUtil.isPetshop(self.zoneId):
            base.localAvatar.setPosHpr(0, 0, ToontownGlobals.FloorOffset, 45.0, 0.0, 0.0)
        elif modelType in InteriorTypes:
            area = InteriorTypes[modelType]
            base.localAvatar.setPosHpr(area[0], area[1], ToontownGlobals.FloorOffset, area[2], 0.0, 0.0)
        else:
            base.localAvatar.setPosHpr(2.5, 11.5, ToontownGlobals.FloorOffset, 45.0, 0.0, 0.0)
        Place.Place.enterTeleportIn(self, requestStatus)

    def enterTeleportOut(self, requestStatus):
        Place.Place.enterTeleportOut(self, requestStatus, self.__teleportOutDone)

    def __teleportOutDone(self, requestStatus):
        hoodId = requestStatus['hoodId']
        zoneId = requestStatus['zoneId']
        shardId = requestStatus['shardId']
        if hoodId == self.loader.hood.id and zoneId == self.zoneId and shardId == None:
            self.fsm.request('teleportIn', [requestStatus])
        elif hoodId == ToontownGlobals.MyEstate:
            self.getEstateZoneAndGoHome(requestStatus)
        else:
            self.doneStatus = requestStatus
            messenger.send(self.doneEvent)
        return

    def goHomeFailed(self, task):
        self.notifyUserGoHomeFailed()
        self.ignore('setLocalEstateZone')
        self.doneStatus['avId'] = -1
        self.doneStatus['zoneId'] = self.getZoneId()
        self.fsm.request('teleportIn', [self.doneStatus])
        return Task.done

    def exitTeleportOut(self):
        Place.Place.exitTeleportOut(self)
		
    def enterElevator(self, distElevator):
        base.localAvatar.cantLeaveGame = 1
        self.accept(self.elevatorDoneEvent, self.handleElevatorDone)
        self.elevator = Elevator.Elevator(self.fsm.getStateNamed('elevator'), self.elevatorDoneEvent, distElevator)
        self.elevator.load()
        self.elevator.enter()

    def exitElevator(self):
        base.localAvatar.cantLeaveGame = 0
        self.ignore(self.elevatorDoneEvent)
        self.elevator.unload()
        self.elevator.exit()
        del self.elevator
		
    def handleElevatorDone(self, doneStatus):
        self.notify.debug('handling elevator done event')
        where = doneStatus['where']
        if where == 'reject':
            if hasattr(base.localAvatar, 'elevatorNotifier') and base.localAvatar.elevatorNotifier.isNotifierOpen():
                pass
            else:
                self.fsm.request('walk')
        elif where == 'exit':
            self.fsm.request('walk')
        elif where == 'cogTowerInterior':
            self.doneStatus = doneStatus
            messenger.send(self.doneEvent)
        else:
            self.notify.error('Unknown mode: ' + where + ' in handleElevatorDone')
		
    def detectedElevatorCollision(self, distElevator):
        self.fsm.request('elevator', [distElevator])
