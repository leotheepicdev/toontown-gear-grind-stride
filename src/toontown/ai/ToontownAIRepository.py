from panda3d.core import Datagram, Thread, UniqueIdAllocator
from direct.distributed.PyDatagram import *
from otp.ai.AIZoneData import AIZoneDataStore
from toontown.magicword.MagicWordGlobal import *
from toontown.distributed.ToontownDoGlobals import *
from toontown.ai.PunishmentManagerAI import PunishmentManagerAI
from toontown.ai import CogPageManagerAI
from toontown.ai import CogSuitManagerAI
from toontown.ai import PromotionManagerAI
from toontown.ai.FishManagerAI import FishManagerAI
from toontown.ai.NewsManagerAI import NewsManagerAI
from toontown.ai.QuestManagerAI import QuestManagerAI
from toontown.ai.DistributedBlackToonMgrAI import DistributedBlackToonMgrAI
from toontown.ai.DistributedReportMgrAI import DistributedReportMgrAI
from toontown.building.DistributedBuildingQueryMgrAI import DistributedBuildingQueryMgrAI
from toontown.building.DistributedTrophyMgrAI import DistributedTrophyMgrAI
from toontown.catalog.CatalogManagerAI import CatalogManagerAI
from toontown.coghq import CountryClubManagerAI
from toontown.coghq import FactoryManagerAI
from toontown.coghq import LawOfficeManagerAI
from toontown.coghq import MintManagerAI
from toontown.distributed.TimeManagerAI import TimeManagerAI
from toontown.distributed.ToontownDistrictAI import ToontownDistrictAI
from toontown.distributed.ToontownDistrictStatsAI import ToontownDistrictStatsAI
from toontown.distributed.ToontownInternalRepository import ToontownInternalRepository
from toontown.dna.DNAParser import loadDNAFileAI
from toontown.estate.EstateManagerAI import EstateManagerAI
from toontown.friends.FriendManagerAI import FriendManagerAI
from toontown.hood import BRHoodAI
from toontown.hood import BossbotHQAI
from toontown.hood import CashbotHQAI
from toontown.hood import DDHoodAI
from toontown.hood import DGHoodAI
from toontown.hood import DLHoodAI
from toontown.hood import WWHoodAI
from toontown.hood import CZHoodAI
from toontown.hood import GSHoodAI
from toontown.hood import GZHoodAI
from toontown.hood import LawbotHQAI
from toontown.hood import MMHoodAI
from toontown.hood import OZHoodAI
from toontown.hood import SellbotHQAI
from toontown.hood import TTHoodAI
from toontown.hood import ZoneUtil
from toontown.magicword.MagicWordManagerAI import MagicWordManagerAI
from toontown.racing.RaceManagerAI import RaceManagerAI
from toontown.golf.GolfManagerAI import GolfManagerAI
from toontown.pets.PetManagerAI import PetManagerAI
from toontown.safezone.SafeZoneManagerAI import SafeZoneManagerAI
from toontown.suit import SuitInvasionGlobalsAI
from toontown.suit.SuitInvasionManagerAI import SuitInvasionManagerAI
from toontown.toon import NPCToons
from toontown.base import ToontownGlobals
from toontown.parties.ToontownTimeManagerAI import ToontownTimeManagerAI
from toontown.uberdog.DistributedPartyManagerAI import DistributedPartyManagerAI
import threading

class ToontownAIRepository(ToontownInternalRepository):
    def __init__(self, baseChannel, stateServerChannel, districtName, districtDifficulty):
        ToontownInternalRepository.__init__(
            self, baseChannel, stateServerChannel, dcSuffix='AI')

        self.districtName = districtName
        self.districtDifficulty = districtDifficulty

        self.notify.setInfo(True)  # Our AI repository should always log info.
        self.hoods = []
        self.cogHeadquarters = []
        self.dnaStoreMap = {}
        self.dnaDataMap = {}
        self.suitPlanners = {}
        self.buildingManagers = {}
        self.factoryMgr = None
        self.mintMgr = None
        self.lawOfficeMgr = None
        self.countryClubMgr = None	
		
        self.zoneAllocator = UniqueIdAllocator(ToontownGlobals.DynamicZonesBegin,
                                               ToontownGlobals.DynamicZonesEnd)
        self.zoneDataStore = AIZoneDataStore()

        self.wantFishing = self.config.GetBool('want-fishing', True)
        self.wantHousing = self.config.GetBool('want-housing', True)
        self.wantPets = self.config.GetBool('want-pets', True)
        self.wantKarts = self.config.GetBool('want-karts', True)
        self.wantGolf = self.config.GetBool('want-golf', True)
        self.wantParties = self.config.GetBool('want-parties', True)
        self.wantEmblems = self.config.GetBool('want-emblems', True)
        self.wantCogbuildings = self.config.GetBool('want-cogbuildings', True)
        self.wantCogdominiums = self.config.GetBool('want-cogdominiums', True)
        self.baseXpMultiplier = self.config.GetFloat('base-xp-multiplier', 1.0)

        self.cogSuitMessageSent = False

    def createManagers(self):
        self.timeManager = TimeManagerAI(self)
        self.timeManager.generateWithRequired(2)
        self.magicWordManager = MagicWordManagerAI(self)
        self.magicWordManager.generateWithRequired(2)
        self.newsManager = NewsManagerAI(self)
        self.newsManager.generateWithRequired(2)
        self.safeZoneManager = SafeZoneManagerAI(self)
        self.safeZoneManager.generateWithRequired(2)
        self.friendManager = FriendManagerAI(self)
        self.friendManager.generateWithRequired(2)
        self.questManager = QuestManagerAI(self)       
        self.punishmentManager = PunishmentManagerAI(self)
        self.createSuitInvasionManager()
        self.blackToonMgr = DistributedBlackToonMgrAI(self)
        self.blackToonMgr.generateWithRequired(2)
        self.reportMgr = DistributedReportMgrAI(self)
        self.reportMgr.generateWithRequired(2)
        self.trophyMgr = DistributedTrophyMgrAI(self)
        self.trophyMgr.generateWithRequired(2)
        self.cogSuitMgr = CogSuitManagerAI.CogSuitManagerAI()
        self.promotionMgr = PromotionManagerAI.PromotionManagerAI(self)
        self.cogPageManager = CogPageManagerAI.CogPageManagerAI()
        self.buildingQueryMgr = DistributedBuildingQueryMgrAI(self)
        self.buildingQueryMgr.generateWithRequired(2)
        if self.wantKarts:
            self.raceMgr = RaceManagerAI(self)
        if self.wantGolf:
            self.golf = GolfManagerAI()
        if self.wantFishing:
            self.fishManager = FishManagerAI(self)
        if self.wantHousing:
            self.estateManager = EstateManagerAI(self)
            self.estateManager.generateWithRequired(2)
            self.catalogManager = CatalogManagerAI(self)
            self.catalogManager.generateWithRequired(2)
        if self.wantPets:
            self.petMgr = PetManagerAI(self)
        self.toontownTimeManager = ToontownTimeManagerAI()
        if self.wantParties:
            self.partyManager = DistributedPartyManagerAI(self)
            self.partyManager.generateWithRequired(2)
            self.globalPartyMgr = self.generateGlobalObject(
                DO_ID_GLOBAL_PARTY_MANAGER, 'GlobalPartyManager')
        self.chatAgent = self.generateGlobalObject(DO_ID_CHAT_MANAGER, 'ChatAgent')

    def createSafeZones(self):
        NPCToons.generateZone2NpcDict()
        if self.config.GetBool('want-toontown-central', True):
            self.hoods.append(TTHoodAI.TTHoodAI(self))
        if self.config.GetBool('want-donalds-dock', True):
            self.hoods.append(DDHoodAI.DDHoodAI(self))
        if self.config.GetBool('want-daisys-garden', True):
            self.hoods.append(DGHoodAI.DGHoodAI(self))
        if self.config.GetBool('want-minnies-melodyland', True):
            self.hoods.append(MMHoodAI.MMHoodAI(self))
        if self.config.GetBool('want-the-brrrgh', True):
            self.hoods.append(BRHoodAI.BRHoodAI(self))
        if self.config.GetBool('want-donalds-dreamland', True):
            self.hoods.append(DLHoodAI.DLHoodAI(self))
        if self.config.GetBool('want-wacky-west', True):
            self.hoods.append(WWHoodAI.WWHoodAI(self))
        if self.config.GetBool('want-construction-zone', True):
            self.hoods.append(CZHoodAI.CZHoodAI(self))
        if self.config.GetBool('want-goofy-speedway', True):
            self.hoods.append(GSHoodAI.GSHoodAI(self))
        if self.config.GetBool('want-outdoor-zone', True):
            self.hoods.append(OZHoodAI.OZHoodAI(self))
        if self.config.GetBool('want-golf-zone', True):
            self.hoods.append(GZHoodAI.GZHoodAI(self))

    def createCogHeadquarters(self):
        NPCToons.generateZone2NpcDict()
        if self.config.GetBool('want-sellbot-headquarters', True):
            self.factoryMgr = FactoryManagerAI.FactoryManagerAI(self)
            self.cogHeadquarters.append(SellbotHQAI.SellbotHQAI(self))
        if self.config.GetBool('want-cashbot-headquarters', True):
            self.mintMgr = MintManagerAI.MintManagerAI(self)
            self.cogHeadquarters.append(CashbotHQAI.CashbotHQAI(self))
        if self.config.GetBool('want-lawbot-headquarters', True):
            self.lawOfficeMgr = LawOfficeManagerAI.LawOfficeManagerAI(self)
            self.cogHeadquarters.append(LawbotHQAI.LawbotHQAI(self))
        if self.config.GetBool('want-bossbot-headquarters', True):
            self.countryClubMgr = CountryClubManagerAI.CountryClubManagerAI(self)
            self.cogHeadquarters.append(BossbotHQAI.BossbotHQAI(self))

    def createSuitInvasionManager(self):
        if self.districtId in SuitInvasionGlobalsAI.INVASION_ONLY_DISTRICTS:
            self.suitInvasionManager = SuitInvasionManagerAI(self, True, True)
        elif self.districtId in SuitInvasionGlobalsAI.INVASION_SAFE_DISTRICTS:
            self.suitInvasionManager = SuitInvasionManagerAI(self, False, False)
        else:
            self.suitInvasionManager = SuitInvasionManagerAI(self)

    def handleConnected(self):
        ToontownInternalRepository.handleConnected(self)
        threading.Thread(target=self.startDistrict).start()
    
    def startDistrict(self):
        self.districtId = self.allocateChannel()
        self.notify.info('Creating ToontownDistrictAI(%d)...' % self.districtId)
        self.notify.info('District difficulty is %s!' % self.districtDifficulty)
        self.distributedDistrict = ToontownDistrictAI(self)
        self.distributedDistrict.setName(self.districtName)
        self.distributedDistrict.setDifficulty(self.districtDifficulty)
        self.distributedDistrict.generateWithRequiredAndId(
            self.districtId, self.getGameDoId(), 2)
        self.notify.info('Claiming ownership of channel ID: %d...' % self.districtId)
        self.claimOwnership(self.districtId)

        self.districtStats = ToontownDistrictStatsAI(self)
        self.districtStats.setDistrictId(self.districtId)
        self.districtStats.generateWithRequiredAndId(
            self.allocateChannel(), self.getGameDoId(), 3)
        self.notify.info('Created ToontownDistrictStats(%d)' % self.districtStats.doId)
        self.notify.info('Registered AI Channel.')
        self.notify.info('Creating managers...')
        self.createManagers()
        if self.config.GetBool('want-safe-zones', True):
            self.notify.info('Creating safe zones...')
            self.createSafeZones()
        if self.config.GetBool('want-cog-headquarters', True):
            self.notify.info('Creating Cog headquarters...')
            self.createCogHeadquarters()
        self.notify.info('Making district available...')
        self.distributedDistrict.b_setAvailable(1)
        self.notify.info('Done.')

    def claimOwnership(self, channelId):
        datagram = PyDatagram()
        datagram.addServerHeader(channelId, self.ourChannel, STATESERVER_OBJECT_SET_AI)
        datagram.addChannel(self.ourChannel)
        self.send(datagram)

    def lookupDNAFileName(self, zoneId):
        zoneId = ZoneUtil.getCanonicalZoneId(zoneId)
        hoodId = ZoneUtil.getCanonicalHoodId(zoneId)
        hood = ToontownGlobals.dnaMap[hoodId]
        if hoodId == zoneId:
            zoneId = 'sz'
            phaseNum = ToontownGlobals.phaseMap[hoodId]
        else:
            phaseNum = ToontownGlobals.streetPhaseMap[hoodId]
        return 'phase_%s/dna/%s_%s.pdna' % (phaseNum, hood, zoneId)

    def loadDNAFileAI(self, dnastore, filename):
        return loadDNAFileAI(dnastore, filename)

    def incrementPopulation(self):
        self.distributedDistrict.b_setPopulation(self.distributedDistrict.getPopulation() + 1)

    def decrementPopulation(self):
        self.distributedDistrict.b_setPopulation(self.distributedDistrict.getPopulation() - 1)

    def allocateZone(self):
        return self.zoneAllocator.allocate()

    def deallocateZone(self, zone):
        self.zoneAllocator.free(zone)

    def getZoneDataStore(self):
        return self.zoneDataStore

    def getAvatarExitEvent(self, avId):
        return 'distObjDelete-%d' % avId

    def trueUniqueName(self, name):
        return self.uniqueName(name)

@magicWord(category=CATEGORY_SYSTEM_ADMINISTRATOR, types=[str])
def cpu(percpu = ''):
    try:
        from psutil import cpu_percent
        return 'Current CPU usage for district %s: %s%%!' % (simbase.air.distributedDistrict.getName(), str(cpu_percent(interval=None, percpu=percpu)))
    except ImportError:
        return 'The psutil module is not installed on %s! Cannot fetch CPU usage.' % simbase.air.distributedDistrict.getName()

@magicWord(category=CATEGORY_SYSTEM_ADMINISTRATOR)
def mem():
    try:
        from psutil import virtual_memory
        return 'Current memory usage for district %s: %s%%' % (simbase.air.distributedDistrict.getName(), str(virtual_memory().percent))
    except ImportError:
        return 'The psutil module is not installed on %s! Cannot fetch CPU usage.' % simbase.air.distributedDistrict.getName()
