from direct.directnotify import DirectNotifyGlobal
from direct.fsm import StateData
AttackPanelHidden = 0

def hideAttackPanel(flag):
    global AttackPanelHidden
    AttackPanelHidden = flag
    messenger.send('hide-attack-panel')


class TownBattleAttackPanel(StateData.StateData):
    notify = DirectNotifyGlobal.directNotify.newCategory('TownBattleAttackPanel')

    def __init__(self, doneEvent):
        StateData.StateData.__init__(self, doneEvent)

    def load(self):
        StateData.StateData.load(self)

    def unload(self):
        StateData.StateData.unload(self)

    def enter(self):
        StateData.StateData.enter(self)
        if not AttackPanelHidden:
            base.localAvatar.inventory.show()
        self.accept('inventory-selection', self.__handleInventory)
        self.accept('inventory-run', self.__handleRun)
        self.accept('inventory-sos', self.__handleSOS)
        self.accept('inventory-pass', self.__handlePass)
        self.accept('inventory-fire', self.__handleFire)
        self.accept('hide-attack-panel', self.__handleHide)
        return

    def exit(self):
        StateData.StateData.exit(self)
        self.ignore('inventory-selection')
        self.ignore('inventory-run')
        self.ignore('inventory-sos')
        self.ignore('inventory-pass')
        self.ignore('inventory-fire')
        self.ignore('hide-attack-panel')
        base.localAvatar.inventory.hide()

    def __handleRun(self):
        doneStatus = {'mode': 'Run'}
        messenger.send(self.doneEvent, [doneStatus])

    def __handleSOS(self):
        doneStatus = {'mode': 'SOS'}
        messenger.send(self.doneEvent, [doneStatus])

    def __handlePass(self):
        doneStatus = {'mode': 'Pass'}
        messenger.send(self.doneEvent, [doneStatus])

    def __handleFire(self):
        doneStatus = {'mode': 'Fire'}
        messenger.send(self.doneEvent, [doneStatus])

    def __handleInventory(self, track, level):
        if base.localAvatar.inventory.numItem(track, level) > 0:
            doneStatus = {}
            doneStatus['mode'] = 'Inventory'
            doneStatus['track'] = track
            doneStatus['level'] = level
            messenger.send(self.doneEvent, [doneStatus])
        else:
            self.notify.error("An item we don't have: track %s level %s was selected." % [track, level])

    def __handleHide(self):
        if AttackPanelHidden:
            base.localAvatar.inventory.hide()
        else:
            base.localAvatar.inventory.show()
