
from direct.showbase.InputStateGlobal import inputState
from direct.directnotify import DirectNotifyGlobal

CollisionHandlerRayStart = 4000.0 # This is a hack, it may be better to use a line instead of a ray.

class PlayerControlManager:
    notify = DirectNotifyGlobal.directNotify.newCategory("PlayerControlManager")

    def __init__(self, enable=True, passMessagesThrough = True):
        self.passMessagesThrough = passMessagesThrough
        self.inputStateTokens = []
        self.controls = {}
        self.currentControls = None
        self.currentControlsName = None
        self.isEnabled = 0
        if enable:
            self.enable()
        self.forceAvJumpToken = None
        self.istForce = []

        if self.passMessagesThrough:
            self.inputStateTokens.extend((
                inputState.watchWithModifiers("forward", base.getKey('MOVE_UP'), inputSource=inputState.ArrowKeys),
                inputState.watchWithModifiers("reverse", base.getKey('MOVE_DOWN'), inputSource=inputState.ArrowKeys),
                inputState.watchWithModifiers("turnLeft", base.getKey('MOVE_LEFT'), inputSource=inputState.ArrowKeys),
                inputState.watchWithModifiers("turnRight", base.getKey('MOVE_RIGHT'), inputSource=inputState.ArrowKeys)
            ))

    def add(self, controls, name="basic"):
        oldControls = self.controls.get(name)
        if oldControls is not None:
            oldControls.disableAvatarControls()
            oldControls.setCollisionsActive(0)
            oldControls.delete()
        controls.disableAvatarControls()
        controls.setCollisionsActive(0)
        self.controls[name] = controls

    def get(self, name):
        return self.controls.get(name)

    def remove(self, name):
        oldControls = self.controls.pop(name,None)
        if oldControls is not None:
            oldControls.disableAvatarControls()
            oldControls.setCollisionsActive(0)

    if __debug__:
        def lockControls(self):
            self.ignoreUse=True

        def unlockControls(self):
            if hasattr(self, "ignoreUse"):
                del self.ignoreUse

    def use(self, name, avatar):
        if __debug__ and hasattr(self, "ignoreUse"):
            return
        controls = self.controls.get(name)

        if controls is not None:
            if controls is not self.currentControls:
                if self.currentControls is not None:
                    self.currentControls.disableAvatarControls()
                    self.currentControls.setCollisionsActive(0)
                    self.currentControls.setAvatar(None)
                self.currentControls = controls
                self.currentControlsName = name
                self.currentControls.setAvatar(avatar)
                self.currentControls.setCollisionsActive(1)
                if self.isEnabled:
                    self.currentControls.enableAvatarControls()
                messenger.send('use-%s-controls'%(name,), [avatar])
        else:
            self.notify.debug("Unknown controls: %s" % name)

    def setSpeeds(self, forwardSpeed, jumpForce, reverseSpeed, rotateSpeed, strafeLeft=0, strafeRight=0):
        for controls in self.controls.values():
            controls.setWalkSpeed(forwardSpeed, jumpForce, reverseSpeed, rotateSpeed)

    def delete(self):
        self.disable()
        for controls in self.controls.keys():
            self.remove(controls)
        del self.controls
        del self.currentControls
        for token in self.inputStateTokens:
            token.release()

    def getSpeeds(self):
        if self.currentControls:
            return self.currentControls.getSpeeds()
        return None

    def getIsAirborne(self):
        if self.currentControls:
            return self.currentControls.getIsAirborne()
        return False

    def setTag(self, key, value):
        for controls in self.controls.values():
            controls.setTag(key, value)

    def deleteCollisions(self):
        for controls in self.controls.values():
            controls.deleteCollisions()

    def collisionsOn(self):
        if self.currentControls:
            self.currentControls.setCollisionsActive(1)

    def collisionsOff(self):
        if self.currentControls:
            self.currentControls.setCollisionsActive(0)

    def placeOnFloor(self):
        if self.currentControls:
            self.currentControls.placeOnFloor()

    def enable(self):

        if self.isEnabled:
            return

        self.isEnabled = 1

        # keep track of what we do on the inputState so we can undo it later on
        #self.inputStateTokens = []
        self.inputStateTokens.extend((
            inputState.watch("run", 'runningEvent', "running-on", "running-off"),
            inputState.watch('turnLeft', 'mouse-look_left', 'mouse-look_left-done'),
            inputState.watch('turnLeft', 'force-turnLeft', 'force-turnLeft-stop'),
            inputState.watch('turnRight', 'mouse-look_right', 'mouse-look_right-done'),
            inputState.watch('turnRight', 'force-turnRight', 'force-turnRight-stop'),
            inputState.watchWithModifiers('forward', base.getKey('MOVE_UP'), inputSource=inputState.ArrowKeys),
            inputState.watchWithModifiers('reverse', base.getKey('MOVE_DOWN'), inputSource=inputState.ArrowKeys),
            inputState.watchWithModifiers('turnLeft', base.getKey('MOVE_LEFT'), inputSource=inputState.ArrowKeys),
            inputState.watchWithModifiers('turnRight', base.getKey('MOVE_RIGHT'), inputSource=inputState.ArrowKeys),
            inputState.watchWithModifiers('jump', base.getKey('FIRE'))
        ))

        if self.currentControls:
            self.currentControls.enableAvatarControls()

    def disable(self):
        self.isEnabled = 0

        for token in self.inputStateTokens:
            token.release()
        self.inputStateTokens = []

        if self.currentControls:
            self.currentControls.disableAvatarControls()

        if self.passMessagesThrough:
            self.inputStateTokens.extend((
                inputState.watchWithModifiers("forward", base.getKey('MOVE_UP'), inputSource=inputState.ArrowKeys),
                inputState.watchWithModifiers("reverse", base.getKey('MOVE_DOWN'), inputSource=inputState.ArrowKeys),
                inputState.watchWithModifiers("turnLeft", base.getKey('MOVE_LEFT'), inputSource=inputState.ArrowKeys),
                inputState.watchWithModifiers("turnRight", base.getKey('MOVE_RIGHT'), inputSource=inputState.ArrowKeys)
            ))

    def stop(self):
        self.disable()
        if self.currentControls:
            self.currentControls.setCollisionsActive(0)
            self.currentControls.setAvatar(None)
        self.currentControls = None

    def disableAvatarJump(self):
        self.forceAvJumpToken = inputState.force("jump", 0, 'PlayerControlManager.disableAvatarJump')

    def enableAvatarJump(self):
        self.forceAvJumpToken.release()
        self.forceAvJumpToken = None
		
    def update(self):
        for token in self.inputStateTokens:
            token.release()
        self.inputStateTokens = []
        self.inputStateTokens.extend((
            inputState.watch("run", 'runningEvent', "running-on", "running-off"),
            inputState.watch('turnLeft', 'mouse-look_left', 'mouse-look_left-done'),
            inputState.watch('turnLeft', 'force-turnLeft', 'force-turnLeft-stop'),
            inputState.watch('turnRight', 'mouse-look_right', 'mouse-look_right-done'),
            inputState.watch('turnRight', 'force-turnRight', 'force-turnRight-stop'),
            inputState.watchWithModifiers('forward', base.getKey('MOVE_UP'), inputSource=inputState.ArrowKeys),
            inputState.watchWithModifiers('reverse', base.getKey('MOVE_DOWN'), inputSource=inputState.ArrowKeys),
            inputState.watchWithModifiers('turnLeft', base.getKey('MOVE_LEFT'), inputSource=inputState.ArrowKeys),
            inputState.watchWithModifiers('turnRight', base.getKey('MOVE_RIGHT'), inputSource=inputState.ArrowKeys),
            inputState.watchWithModifiers('jump', base.getKey('FIRE'))
        ))
		
    def listenToControls(self):
        if self.istForce:
            for token in self.istForce:
                token.release()
            self.istForce = []
			  
    def ignoreControls(self):
        self.istForce = [
            inputState.force('forward', 0, 'PlayerControlManager.ignoreControls'),
            inputState.force('reverse', 0, 'PlayerControlManager.ignoreControls'),
            inputState.force('turnLeft', 0, 'PlayerControlManager.ignoreControls'),
            inputState.force('turnRight', 0, 'PlayerControlManager.ignoreControls'),
            inputState.force('jump', 0, 'PlayerControlManager.ignoreControls'),
        ]


