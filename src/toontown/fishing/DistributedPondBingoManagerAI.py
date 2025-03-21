from direct.directnotify import DirectNotifyGlobal
from direct.distributed.DistributedObjectAI import DistributedObjectAI
from direct.distributed.ClockDelta import *
from toontown.fishing import BingoGlobals
from toontown.fishing import FishGlobals
from toontown.fishing.NormalBingo import NormalBingo
from toontown.fishing.ThreewayBingo import ThreewayBingo
from toontown.fishing.DiagonalBingo import DiagonalBingo
from toontown.fishing.BlockoutBingo import BlockoutBingo
from toontown.fishing.FourCornerBingo import FourCornerBingo
import random

RequestCard = {}

class DistributedPondBingoManagerAI(DistributedObjectAI):
    notify = DirectNotifyGlobal.directNotify.newCategory("DistributedPondBingoManagerAI")

    def __init__(self, air):
        DistributedObjectAI.__init__(self, air)
        self.air = air
        self.bingoCard = None
        self.tileSeed = None
        self.typeId = None
        self.state = 'Off'
        self.pond = None
        self.canCall = False
        self.lastUpdate = globalClockDelta.getRealNetworkTime()
        self.cardId = 0
    
    def delete(self):
        taskMgr.remove(self.uniqueName('startWait'))
        taskMgr.remove(self.uniqueName('createGame'))
        taskMgr.remove(self.uniqueName('finishGame'))
        DistributedObjectAI.delete(self)

    def setPondDoId(self, pondId):
        self.pond = self.air.doId2do[pondId]

    def getPondDoId(self):
        return self.pond.getDoId()

    def cardUpdate(self, cardId, cellId, genus, species):
        avId = self.air.getAvatarIdFromSender()
        spot = self.pond.hasToon(avId)
        if not spot:
            self.air.writeServerEvent('suspicious', avId, 'Toon tried to call bingo while not fishing!')
            return
        fishTuple = (genus, species)
        if (genus != spot.lastFish[1] or species != spot.lastFish[2]):
            self.air.writeServerEvent('suspicious', avId, 'Toon tried to update bingo card with a fish they didn\'t catch!')
            return
        if cardId != self.cardId:
            self.air.writeServerEvent('suspicious', avId, 'Toon tried to update expired bingo card!')
            return
        if self.state != 'Playing':
            self.air.writeServerEvent('suspicious', avId, 'Toon tried to update while the game is not running!')
            return
        spot.lastFish = [None, None, None, None]
        result = self.bingoCard.cellUpdateCheck(cellId, genus, species)
        if result == BingoGlobals.WIN:
            self.canCall = True
            self.sendCanBingo()
            self.sendGameStateUpdate(cellId)
        elif result == BingoGlobals.UPDATE:
            self.sendGameStateUpdate(cellId)

    def handleBingoCall(self, cardId):
        avId = self.air.getAvatarIdFromSender()
        av = self.air.doId2do.get(avId)
        
        if not av:
            self.air.writeServerEvent('suspicious', avId, 'Toon tried to call bingo while not on district!')
            return

        spot = self.pond.hasToon(avId)

        if not spot:
            self.air.writeServerEvent('suspicious', avId, 'Toon tried to call bingo while not fishing!')
            return
        if not self.canCall:
            self.air.writeServerEvent('suspicious', avId, 'Toon tried to call bingo whle the game is not running!')
            return
        if cardId != self.cardId:
            self.air.writeServerEvent('suspicious', avId, 'Toon tried to call bingo with an expired cardId!')
            return

        av.d_announceBingo()
        self.rewardAll()

    def setJackpot(self, jackpot):
        self.jackpot = jackpot

    def d_setJackpot(self, jackpot):
        self.sendUpdate('setJackpot', [jackpot])

    def b_setJackpot(self, jackpot):
        self.setJackpot(jackpot)
        self.d_setJackpot(jackpot)

    def activateBingoForPlayer(self, avId):
        self.sendUpdateToAvatarId(avId, 'setCardState', [self.cardId, self.typeId, self.tileSeed, self.bingoCard.getGameState()])
        self.sendUpdateToAvatarId(avId, 'setState', [self.state, self.lastUpdate])
        self.canCall = True

    def sendStateUpdate(self):
        self.lastUpdate = globalClockDelta.getRealNetworkTime()
        for spot in self.pond.spots:
            if self.pond.spots[spot].avId == None or self.pond.spots[spot].avId == 0:
                continue
            avId = self.pond.spots[spot].avId
            self.sendUpdateToAvatarId(avId, 'setState', [self.state, self.lastUpdate])

    def sendCardStateUpdate(self):
        for spot in self.pond.spots:
            if self.pond.spots[spot].avId == None or self.pond.spots[spot].avId == 0:
                continue
            avId = self.pond.spots[spot].avId
            self.sendUpdateToAvatarId(avId, 'setCardState', [self.cardId, self.typeId, self.tileSeed, self.bingoCard.getGameState()])

    def sendGameStateUpdate(self, cellId):
        for spot in self.pond.spots:
            if self.pond.spots[spot].avId == None or self.pond.spots[spot].avId == 0:
                continue
            avId = self.pond.spots[spot].avId
            self.sendUpdateToAvatarId(avId, 'updateGameState', [self.bingoCard.getGameState(), cellId])

    def sendCanBingo(self):
        for spot in self.pond.spots:
            if self.pond.spots[spot].avId == None or self.pond.spots[spot].avId == 0:
                continue
            avId = self.pond.spots[spot].avId
            self.sendUpdateToAvatarId(avId, 'enableBingo', [])

    def rewardAll(self):
        self.state = 'Reward'
        self.sendStateUpdate()
        for spot in self.pond.spots:
            if self.pond.spots[spot].avId == None or self.pond.spots[spot].avId == 0:
                continue
            av = self.air.doId2do[self.pond.spots[spot].avId]
            av.addMoney(self.jackpot)
        taskMgr.doMethodLater(5, self.startWait, self.uniqueName('startWait'))
        taskMgr.remove(self.uniqueName('finishGame'))

    def finishGame(self, task=None):
        self.state = 'GameOver'
        self.sendStateUpdate()
        taskMgr.doMethodLater(5, self.startWait, self.uniqueName('startWait'))

    def startIntermission(self):
        self.state = 'Intermission'
        self.sendStateUpdate()
        taskMgr.doMethodLater(300, self.startWait, self.uniqueName('startWait'))

    def startWait(self, task=None):
        self.state = 'WaitCountdown'
        self.sendStateUpdate()
        taskMgr.doMethodLater(15, self.createGame, self.uniqueName('createGame'))

    def createGame(self, task=None):
        self.canCall = False
        self.tileSeed = None
        self.typeId = None
        self.cardId += 1
        for spot in self.pond.spots:
            avId = self.pond.spots[spot].avId
            request = RequestCard.get(avId)
            if request:
                self.typeId, self.tileSeed = request
                del RequestCard[avId]
        if self.cardId > 65535:
            self.cardId = 0
        if not self.tileSeed:
            self.tileSeed = random.randrange(0, 65535)
        if self.typeId == None:
            self.typeId = random.randrange(0, 5)
        if self.typeId == BingoGlobals.NORMAL_CARD:
            self.bingoCard = NormalBingo()
        elif self.typeId == BingoGlobals.DIAGONAL_CARD:
            self.bingoCard = DiagonalBingo()
        elif self.typeId == BingoGlobals.THREEWAY_CARD:
            self.bingoCard = ThreewayBingo()
        elif self.typeId == BingoGlobals.FOURCORNER_CARD:
            self.bingoCard = FourCornerBingo()
        else:
            self.bingoCard = BlockoutBingo()
        self.bingoCard.generateCard(self.tileSeed, self.pond.getArea())
        self.sendCardStateUpdate()
        self.b_setJackpot(BingoGlobals.getJackpot(self.typeId))
        self.state = 'Playing'
        self.sendStateUpdate()
        taskMgr.doMethodLater(BingoGlobals.getGameTime(self.typeId), self.finishGame, self.uniqueName('finishGame'))
