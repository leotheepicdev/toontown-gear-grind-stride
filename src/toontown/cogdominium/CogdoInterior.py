from panda3d.core import ModelPool, Texture, TexturePool
from direct.task.Task import Task
from direct.directnotify import DirectNotifyGlobal
from direct.fsm import ClassicFSM, State
from toontown.hood import Place
from toontown.base.ToonBaseGlobal import *
from toontown.town import TownBattle
from toontown.building import Elevator
from toontown.base import ToontownGlobals
from toontown.base import ToontownBattleGlobals

class CogdoInterior(Place.Place):
    notify = DirectNotifyGlobal.directNotify.newCategory('CogdoInterior')

    def __init__(self, loader, parentFSM, doneEvent):
        Place.Place.__init__(self, loader, doneEvent)
        self.fsm = ClassicFSM.ClassicFSM('CogdoInterior', [State.State('entrance', self.enterEntrance, self.exitEntrance, ['Game', 'walk']),
         State.State('Elevator', self.enterElevator, self.exitElevator, ['Game',
          'battle',
          'walk',
          'crane']),
         State.State('Game', self.enterGame, self.exitGame, ['battle',
          'died',
          'crane',
          'walk']),
         State.State('battle', self.enterBattle, self.exitBattle, ['walk', 'died']),
         State.State('crane', self.enterCrane, self.exitCrane, ['walk',
          'battle',
          'finalBattle',
          'died',
          'ouch',
          'squished']),
         State.State('walk', self.enterWalk, self.exitWalk, ['stickerBook',
          'stopped',
          'battle',
          'sit',
          'died',
          'teleportOut',
          'Elevator',
          'crane']),
         State.State('sit', self.enterSit, self.exitSit, ['walk']),
         State.State('stickerBook', self.enterStickerBook, self.exitStickerBook, ['walk',
          'stopped',
          'sit',
          'died',
          'teleportOut',
          'Elevator']),
         State.State('teleportIn', self.enterTeleportIn, self.exitTeleportIn, ['walk']),
         State.State('teleportOut', self.enterTeleportOut, self.exitTeleportOut, ['teleportIn']),
         State.State('stopped', self.enterStopped, self.exitStopped, ['walk', 'elevatorOut', 'battle']),
         State.State('died', self.enterDied, self.exitDied, []),
         State.State('elevatorOut', self.enterElevatorOut, self.exitElevatorOut, [])], 'entrance', 'elevatorOut')
        self.parentFSM = parentFSM
        self.elevatorDoneEvent = 'elevatorDoneSI'
        self.currentFloor = 0

    def enter(self, requestStatus):
        self.fsm.enterInitialState()
        self.zoneId = requestStatus['zoneId']
        self.accept('DSIDoneEvent', self.handleDSIDoneEvent)

    def exit(self):
        self.ignoreAll()

    def load(self):
        Place.Place.load(self)
        self.parentFSM.getStateNamed('cogdoInterior').addChild(self.fsm)
        self.townBattle = TownBattle.TownBattle('town-battle-done')
        self.townBattle.load()

    def unload(self):
        Place.Place.unload(self)
        self.parentFSM.getStateNamed('cogdoInterior').removeChild(self.fsm)
        del self.parentFSM
        del self.fsm
        self.ignoreAll()
        ModelPool.garbageCollect()
        TexturePool.garbageCollect()
        self.townBattle.unload()
        self.townBattle.cleanup()
        del self.townBattle

    def setState(self, state, battleEvent = None):
        if battleEvent:
            self.fsm.request(state, [battleEvent])
        else:
            self.fsm.request(state)

    def getZoneId(self):
        return self.zoneId

    def enterZone(self, zoneId):
        pass

    def handleDSIDoneEvent(self, requestStatus):
        self.doneStatus = requestStatus
        messenger.send(self.doneEvent)

    def enterEntrance(self):
        pass

    def exitEntrance(self):
        pass

    def enterElevator(self, distElevator):
        self.accept(self.elevatorDoneEvent, self.handleElevatorDone)
        self.elevator = Elevator.Elevator(self.fsm.getStateNamed('Elevator'), self.elevatorDoneEvent, distElevator)
        self.elevator.load()
        self.elevator.enter()
        base.localAvatar.cantLeaveGame = 1

    def exitElevator(self):
        base.localAvatar.cantLeaveGame = 0
        self.ignore(self.elevatorDoneEvent)
        self.elevator.unload()
        self.elevator.exit()
        del self.elevator

    def detectedElevatorCollision(self, distElevator):
        self.fsm.request('Elevator', [distElevator])

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
        elif where == 'cogdoInterior':
            pass
        else:
            self.notify.error('Unknown mode: ' + where + ' in handleElevatorDone')

    def enterGame(self):
        base.localAvatar.setTeleportAvailable(0)
        base.localAvatar.laffMeter.start()

    def exitGame(self):
        base.localAvatar.laffMeter.stop()

    def enterBattle(self, event):
        mult = ToontownBattleGlobals.getCreditMultiplier(self.currentFloor)
        self.townBattle.enter(event, self.fsm.getStateNamed('battle'), bldg=1, creditMultiplier=mult)
        base.localAvatar.b_setAnimState('off', 1)
        base.localAvatar.cantLeaveGame = 1

    def exitBattle(self):
        self.townBattle.exit()
        base.localAvatar.cantLeaveGame = 0

    def enterCrane(self):
        base.localAvatar.setTeleportAvailable(0)
        base.localAvatar.laffMeter.start()
        base.localAvatar.collisionsOn()

    def exitCrane(self):
        base.localAvatar.collisionsOff()
        base.localAvatar.laffMeter.stop()

    def enterWalk(self, teleportIn = 0):
        Place.Place.enterWalk(self, teleportIn)
        self.ignore('teleportQuery')
        base.localAvatar.setTeleportAvailable(0)

    def enterStickerBook(self, page = None):
        Place.Place.enterStickerBook(self, page)
        self.ignore('teleportQuery')
        base.localAvatar.setTeleportAvailable(0)

    def enterSit(self):
        Place.Place.enterSit(self)
        self.ignore('teleportQuery')
        base.localAvatar.setTeleportAvailable(0)

    def enterTeleportIn(self, requestStatus):
        base.localAvatar.setPosHpr(2.5, 11.5, ToontownGlobals.FloorOffset, 45.0, 0.0, 0.0)
        Place.Place.enterTeleportIn(self, requestStatus)

    def enterTeleportOut(self, requestStatus):
        Place.Place.enterTeleportOut(self, requestStatus, self.__teleportOutDone)

    def __teleportOutDone(self, requestStatus):
        hoodId = requestStatus['hoodId']
        if hoodId == ToontownGlobals.MyEstate:
            self.getEstateZoneAndGoHome(requestStatus)
        else:
            messenger.send('localToonLeft')
            self.doneStatus = requestStatus
            messenger.send(self.doneEvent)

    def exitTeleportOut(self):
        Place.Place.exitTeleportOut(self)

    def goHomeFailed(self, task):
        self.notifyUserGoHomeFailed()
        self.ignore('setLocalEstateZone')
        self.doneStatus['avId'] = -1
        self.doneStatus['zoneId'] = self.getZoneId()
        self.fsm.request('teleportIn', [self.doneStatus])
        return Task.done

    def enterElevatorOut(self):
        pass

    def __elevatorOutDone(self, requestStatus):
        self.doneStatus = requestStatus
        messenger.send(self.doneEvent)

    def exitElevatorOut(self):
        pass
