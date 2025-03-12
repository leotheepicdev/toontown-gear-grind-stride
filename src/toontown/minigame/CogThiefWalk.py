from toontown.safezone import Walk

class CogThiefWalk(Walk.Walk):
    notify = directNotify.newCategory('CogThiefWalk')

    def __init__(self, doneEvent):
        Walk.Walk.__init__(self, doneEvent)

    def enter(self):
        base.localAvatar.startPosHprBroadcast()
        base.localAvatar.startBlink()
        base.localAvatar.showName()
        base.localAvatar.collisionsOn()
        base.localAvatar.startGlitchKiller()
        base.localAvatar.enableAvatarControls()

    def exit(self):
        self.fsm.request('off')
        self.ignore(base.getKey('FIRE'))
        base.localAvatar.disableAvatarControls()
        base.localAvatar.stopPosHprBroadcast()
        base.localAvatar.stopBlink()
        base.localAvatar.stopGlitchKiller()
        base.localAvatar.collisionsOff()
        base.localAvatar.controlManager.placeOnFloor()
