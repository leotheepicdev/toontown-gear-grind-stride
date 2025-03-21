from PurchaseManagerConstants import *
from direct.distributed.ClockDelta import *
from direct.distributed import DistributedObject
from direct.directnotify import DirectNotifyGlobal

class PurchaseManager(DistributedObject.DistributedObject):
    notify = DirectNotifyGlobal.directNotify.newCategory('PurchaseManager')

    def __init__(self, cr):
        DistributedObject.DistributedObject.__init__(self, cr)
        self.playAgain = 0

    def disable(self):
        DistributedObject.DistributedObject.disable(self)
        self.ignoreAll()

    def setAvIds(self, *avIds):
        self.notify.debug('setAvIds: %s' % (avIds,))
        self.avIds = avIds

    def setMinigamePoints(self, *mpArray):
        self.notify.debug('setMinigamePoints: %s' % (mpArray,))
        self.mpArray = mpArray

    def setPlayerMoney(self, *moneyArray):
        self.notify.debug('setPlayerMoney: %s' % (moneyArray,))
        self.moneyArray = moneyArray

    def setPlayerStates(self, *stateArray):
        self.notify.debug('setPlayerStates: %s' % (stateArray,))
        self.playerStates = stateArray
        if self.isGenerated() and self.hasLocalToon:
            self.announcePlayerStates()

    def setCountdown(self, timestamp):
        self.countdownTimestamp = timestamp

    def announcePlayerStates(self):
        messenger.send('purchaseStateChange', [self.playerStates])

    def announceGenerate(self):
        DistributedObject.DistributedObject.announceGenerate(self)
        self.hasLocalToon = self.calcHasLocalToon()
        if self.hasLocalToon:
            self.announcePlayerStates()
            et = globalClockDelta.localElapsedTime(self.countdownTimestamp)
            remain = PURCHASE_COUNTDOWN_TIME - et
            self.acceptOnce('purchasePlayAgain', self.playAgainHandler)
            self.acceptOnce('purchaseBackToToontown', self.backToToontownHandler)
            self.acceptOnce('purchaseTimeout', self.setPurchaseExit)
            self.accept('boughtGag', self.__handleBoughtGag)
            base.cr.playGame.hood.fsm.request('purchase', [self.mpArray,
             self.moneyArray,
             self.avIds,
             self.playerStates,
             remain])

    def calcHasLocalToon(self):
        retval = base.localAvatar.doId in self.avIds
        self.notify.debug('calcHasLocalToon returning %s' % retval)
        return retval

    def playAgainHandler(self):
        self.d_requestPlayAgain()

    def backToToontownHandler(self):
        self.notify.debug('requesting exit to toontown...')
        self.d_requestExit()
        self.playAgain = 0
        self.setPurchaseExit()

    def d_requestExit(self):
        self.sendUpdate('requestExit', [])

    def d_requestPlayAgain(self):
        self.notify.debug('requesting play again...')
        self.sendUpdate('requestPlayAgain', [])
        self.playAgain = 1

    def d_setInventory(self, invString, money, done):
        self.sendUpdate('setInventory', [invString, money, done])

    def __handleBoughtGag(self):
        self.d_setInventory(base.localAvatar.inventory.makeNetString(), base.localAvatar.getMoney(), 0)

    def setPurchaseExit(self):
        if self.hasLocalToon:
            self.ignore('boughtGag')
            self.d_setInventory(base.localAvatar.inventory.makeNetString(), base.localAvatar.getMoney(), 1)
            messenger.send('purchaseOver', [self.playAgain])
