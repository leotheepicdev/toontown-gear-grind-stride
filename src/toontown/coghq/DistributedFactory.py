from panda3d.core import CollisionHandler
from toontown.base.ToontownGlobals import *
from direct.distributed.ClockDelta import *
from direct.interval.IntervalGlobal import *
from toontown.level import DistributedLevel
from direct.directnotify import DirectNotifyGlobal
import FactoryBase
import FactoryEntityCreator
import FactorySpecs
from toontown.distributed import DistrictGlobals
from toontown.coghq.sellbothq import FactorySpecsHard, FactorySpecsExtreme
from toontown.level import LevelSpec
from toontown.level import LevelConstants
from toontown.toon import NPCToons
from toontown.base import TTLocalizer
from toontown.coghq import FactoryCameraViews
from direct.controls.ControlManager import CollisionHandlerRayStart
from lib.nametag.NametagConstants import *
from toontown.magicword.MagicWordGlobal import *

class DistributedFactory(DistributedLevel.DistributedLevel, FactoryBase.FactoryBase):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedFactory')

    def __init__(self, cr):
        DistributedLevel.DistributedLevel.__init__(self, cr)
        FactoryBase.FactoryBase.__init__(self)
        self.suitIds = []
        self.suits = []
        self.reserveSuits = []
        self.joiningReserves = []
        self.suitsInitialized = 0
        self.goonClipPlanes = {}
        # Only record difficulty once incase the district difficulty gets swapped while the district is active to prevent difficulty mixing
        self.districtDifficulty = self.cr.distributedDistrict.getDifficulty()

    def createEntityCreator(self):
        return FactoryEntityCreator.FactoryEntityCreator(level=self)

    def generate(self):
        self.notify.debug('generate')
        DistributedLevel.DistributedLevel.generate(self)
        self.factoryViews = FactoryCameraViews.FactoryCameraViews(self)
        base.localAvatar.chatMgr.chatInputSpeedChat.addFactoryMenu()
        self.accept('SOSPanelEnter', self.handleSOSPanel)
        base.factory = self

    def delete(self):
        DistributedLevel.DistributedLevel.delete(self)
        base.localAvatar.chatMgr.chatInputSpeedChat.removeFactoryMenu()
        self.factoryViews.delete()
        del self.factoryViews
        del base.factory
        self.ignore('SOSPanelEnter')

    def setFactoryId(self, id):
        FactoryBase.FactoryBase.setFactoryId(self, id)

    def setForemanConfronted(self, avId):
        if avId == base.localAvatar.doId:
            return
        av = base.cr.identifyFriend(avId)
        if av is None:
            return
        base.localAvatar.setSystemMessage(avId, TTLocalizer.ForemanConfrontedMsg % av.getName())
        return

    def setDefeated(self):
        self.notify.info('setDefeated')
        messenger.send('FactoryWinEvent')

    def levelAnnounceGenerate(self):
        self.notify.debug('levelAnnounceGenerate')
        DistributedLevel.DistributedLevel.levelAnnounceGenerate(self)
        if self.districtDifficulty == DistrictGlobals.DIFFICULTY_HARD:
            spec = FactorySpecsHard
        elif self.districtDifficulty == DistrictGlobals.DIFFICULTY_EXTREME:
            spec = FactorySpecsExtreme
        else:
            spec = FactorySpecs
        specModule = spec.getFactorySpecModule(self.factoryId)
        factorySpec = LevelSpec.LevelSpec(specModule)
        DistributedLevel.DistributedLevel.initializeLevel(self, factorySpec)

    def privGotSpec(self, levelSpec):
        firstSetZoneDoneEvent = self.cr.getNextSetZoneDoneEvent()

        def handleFirstSetZoneDone():
            base.factoryReady = 1
            messenger.send('FactoryReady')

        self.acceptOnce(firstSetZoneDoneEvent, handleFirstSetZoneDone)
        modelCount = len(levelSpec.getAllEntIds())
        loader.beginBulkLoad('factory', TTLocalizer.HeadingToFactoryTitle % TTLocalizer.FactoryNames[self.factoryId], modelCount, 1, TTLocalizer.TIP_COGHQ, self.factoryId)
        DistributedLevel.DistributedLevel.privGotSpec(self, levelSpec)
        loader.endBulkLoad('factory')

        def printPos(self = self):
            pos = base.localAvatar.getPos(self.getZoneNode(self.lastToonZone))
            h = base.localAvatar.getH(self.getZoneNode(self.lastToonZone))
            print 'factory pos: %s, h: %s, zone %s' % (repr(pos), h, self.lastToonZone)
            posStr = 'X: %.3f' % pos[0] + '\nY: %.3f' % pos[1] + '\nZ: %.3f' % pos[2] + '\nH: %.3f' % h + '\nZone: %s' % str(self.lastToonZone)
            base.localAvatar.setChatAbsolute(posStr, CFThought | CFTimeout)

        self.accept('f2', printPos)
        base.localAvatar.setCameraCollisionsCanMove(1)
        self.acceptOnce('leavingFactory', self.announceLeaving)

    def handleSOSPanel(self, panel):
        avIds = []
        for avId in self.avIdList:
            if base.cr.doId2do.get(avId):
                avIds.append(avId)

        panel.setFactoryToonIdList(avIds)

    def disable(self):
        self.notify.debug('disable')
        base.localAvatar.setCameraCollisionsCanMove(0)
        if hasattr(self, 'suits'):
            del self.suits
        if hasattr(self, 'relatedObjectMgrRequest') and self.relatedObjectMgrRequest:
            self.cr.relatedObjectMgr.abortRequest(self.relatedObjectMgrRequest)
            del self.relatedObjectMgrRequest
        DistributedLevel.DistributedLevel.disable(self)

    def setSuits(self, suitIds, reserveSuitIds):
        oldSuitIds = list(self.suitIds)
        self.suitIds = suitIds
        self.reserveSuitIds = reserveSuitIds
        newSuitIds = []
        for suitId in self.suitIds:
            if suitId not in oldSuitIds:
                newSuitIds.append(suitId)

        if len(newSuitIds):

            def bringOutOfReserve(suits):
                for suit in suits:
                    if suit:
                        suit.comeOutOfReserve()

            self.relatedObjectMgrRequest = self.cr.relatedObjectMgr.requestObjects(newSuitIds, bringOutOfReserve)

    def reservesJoining(self):
        pass

    def getCogSpec(self, cogId):
        if self.districtDifficulty == DistrictGlobals.DIFFICULTY_HARD:
            spec = FactorySpecsHard
        elif self.districtDifficulty == DistrictGlobals.DIFFICULTY_EXTREME:
            spec = FactorySpecsExtreme
        else:
            spec = FactorySpecs
        cogSpecModule = spec.getCogSpecModule(self.factoryId)
        return cogSpecModule.CogData[cogId]

    def getReserveCogSpec(self, cogId):
        if self.districtDifficulty == DistrictGlobals.DIFFICULTY_HARD:
            spec = FactorySpecsHard
        elif self.districtDifficulty == DistrictGlobals.DIFFICULTY_EXTREME:
            spec = FactorySpecsExtreme
        else:
            spec = FactorySpecs
        cogSpecModule = spec.getCogSpecModule(self.factoryId)
        return cogSpecModule.ReserveCogData[cogId]

    def getBattleCellSpec(self, battleCellId):
        if self.districtDifficulty == DistrictGlobals.DIFFICULTY_HARD:
            spec = FactorySpecsHard
        elif self.districtDifficulty == DistrictGlobals.DIFFICULTY_EXTREME:
            spec = FactorySpecsExtreme
        else:
            spec = FactorySpecs
        cogSpecModule = spec.getCogSpecModule(self.factoryId)
        return cogSpecModule.BattleCells[battleCellId]

    def getFloorOuchLevel(self):
        factorySfxRoom = self.lastToonZone # Factory area id (See SellbotLegFactorySpec or press f2 in the factory in any location)
        if factorySfxRoom == 10: # Paint Mixer
            self.ouchSound = base.loadSfx('phase_9/audio/sfx/CHQ_FACT_paint_splash.ogg')
            base.playSfx(self.ouchSound, volume=0.5)
        elif factorySfxRoom == 19: # Lava Room
            self.ouchSound = base.loadSfx('phase_9/audio/sfx/CHQ_FACT_lava_fall_in.ogg')
            base.playSfx(self.ouchSound, volume=0.5)
        return 8

    def getGoonPathId(self):
        return 'sellbotFactory'

    def getTaskZoneId(self):
        return self.factoryId

    def getBossTaunt(self):
        return TTLocalizer.FactoryBossTaunt

    def getBossBattleTaunt(self):
        return TTLocalizer.FactoryBossBattleTaunt
      
    def announceFactoryReward(self, difficulty, npcId):
        npcName = NPCToons.getNPCName(npcId)
        if difficulty == DistrictGlobals.DIFFICULTY_EXTREME:
            base.localAvatar.setSystemMessage(0, TTLocalizer.FactoryRewardMessageExtreme.format(npcName))
        elif difficulty == DistrictGlobals.DIFFICULTY_HARD:
            base.localAvatar.setSystemMessage(0, TTLocalizer.FactoryRewardMessageHard.format(npcName))        

@magicWord(category=CATEGORY_PROGRAMMER, types=[int])
def factoryWarp(zoneNum):
    """
    Warp to a specific factory zone.
    """
    if not hasattr(base, 'factory'):
        return 'You must be in a factory!'
    base.factory.warpToZone(zoneNum)
    return 'Warped to zone: %d' % zoneNum
