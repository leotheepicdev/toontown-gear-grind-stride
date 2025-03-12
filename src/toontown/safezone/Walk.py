from panda3d.core import Camera
from direct.directnotify import DirectNotifyGlobal
from direct.fsm import ClassicFSM, StateData, State

class Walk(StateData.StateData):
    notify = DirectNotifyGlobal.directNotify.newCategory('Walk')

    def __init__(self, doneEvent):
        StateData.StateData.__init__(self, doneEvent)
        self.fsm = ClassicFSM.ClassicFSM('Walk', [State.State('off', self.enterOff, self.exitOff, ['walking', 'swimming', 'slowWalking']),
         State.State('walking', self.enterWalking, self.exitWalking, ['swimming', 'slowWalking']),
         State.State('swimming', self.enterSwimming, self.exitSwimming, ['walking', 'slowWalking'])], 'off', 'off')
        self.fsm.enterInitialState()
        self.swimSoundPlaying = 0

    def load(self):
        pass

    def unload(self):
        del self.fsm

    def enter(self):
        base.localAvatar.startPosHprBroadcast()
        base.localAvatar.startBlink()
        base.localAvatar.attachCamera()
        shouldPush = 1
        if len(base.localAvatar.cameraPositions) > 0:
            shouldPush = not base.localAvatar.cameraPositions[base.localAvatar.cameraIndex][4]
        base.localAvatar.startUpdateSmartCamera(shouldPush)
        base.localAvatar.showName()
        base.localAvatar.collisionsOn()
        base.localAvatar.startGlitchKiller()
        base.localAvatar.enableAvatarControls()

    def exit(self):
        self.fsm.request('off')
        self.ignore(base.getKey('FIRE'))
        base.localAvatar.disableAvatarControls()
        if not base.localAvatar.preventCameraDisable:
            base.localAvatar.stopUpdateSmartCamera()
            base.localAvatar.detachCamera()
        base.localAvatar.stopPosHprBroadcast()
        base.localAvatar.stopBlink()
        base.localAvatar.stopGlitchKiller()
        base.localAvatar.collisionsOff()
        base.localAvatar.controlManager.placeOnFloor()

    def enterOff(self):
        pass

    def exitOff(self):
        pass

    def enterWalking(self):
        base.localAvatar.startTrackAnimToSpeed()
        base.localAvatar.setWalkSpeedNormal()
        base.localAvatar.applyBuffs()

    def exitWalking(self):
        base.localAvatar.stopTrackAnimToSpeed()

    def enterSwimming(self, swimSound):
        base.localAvatar.setWalkSpeedNormal()
        base.localAvatar.applyBuffs()
        self.swimSound = swimSound
        self.swimSoundPlaying = 0
        base.localAvatar.b_setAnimState('swim', base.localAvatar.animMultiplier)
        taskMgr.add(self.__swimSoundTest, 'localToonSwimming')

    def exitSwimming(self):
        taskMgr.remove('localToonSwimming')
        self.swimSound.stop()
        del self.swimSound
        self.swimSoundPlaying = 0

    def __swimSoundTest(self, task):
        speed, rotSpeed, slideSpeed = base.localAvatar.controlManager.getSpeeds()

        if (speed or rotSpeed):
            if not self.swimSoundPlaying:
                self.swimSoundPlaying = 1
                base.playSfx(self.swimSound, looping=1)
        elif self.swimSoundPlaying:
            self.swimSoundPlaying = 0
            self.swimSound.stop()

        return task.cont

    def __handlePositiveHP(self):
        self.fsm.request('walking')
