from panda3d.core import ModelPool, Texture, TexturePool
from toontown.base.ToonBaseGlobal import *
from direct.directnotify import DirectNotifyGlobal
from direct.fsm import StateData
from direct.fsm import ClassicFSM, State
from direct.task.Task import Task
from ToontownMsgTypes import *
from toontown.base import ToontownGlobals
from toontown.hood import TTHood
from toontown.hood import DDHood
from toontown.hood import MMHood
from toontown.hood import BRHood
from toontown.hood import DGHood
from toontown.hood import DLHood
from toontown.hood import WWHood
from toontown.hood import GSHood
from toontown.hood import OZHood
from toontown.hood import GZHood
from toontown.hood import CZHood
from toontown.hood import SellbotHQ, CashbotHQ, LawbotHQ, BossbotHQ
from direct.task import TaskManagerGlobal
from toontown.hood import QuietZoneState
from toontown.hood import ZoneUtil
from toontown.hood import EstateHood
from toontown.hood import PartyHood
from toontown.base import TTLocalizer
from toontown.parties.PartyGlobals import GoToPartyStatus
from toontown.dna.DNAParser import *

class PlayGame(StateData.StateData):
    notify = DirectNotifyGlobal.directNotify.newCategory('PlayGame')
    Hood2ClassDict = {ToontownGlobals.ToontownCentral: TTHood.TTHood,
     ToontownGlobals.DonaldsDock: DDHood.DDHood,
     ToontownGlobals.TheBrrrgh: BRHood.BRHood,
     ToontownGlobals.MinniesMelodyland: MMHood.MMHood,
     ToontownGlobals.DaisyGardens: DGHood.DGHood,
     ToontownGlobals.DonaldsDreamland: DLHood.DLHood,
     ToontownGlobals.WackyWest: WWHood.WWHood,
     ToontownGlobals.ConstructionZone: CZHood.CZHood,
     ToontownGlobals.GoofySpeedway: GSHood.GSHood,
     ToontownGlobals.OutdoorZone: OZHood.OZHood,
     ToontownGlobals.MyEstate: EstateHood.EstateHood,
     ToontownGlobals.BossbotHQ: BossbotHQ.BossbotHQ,
     ToontownGlobals.SellbotHQ: SellbotHQ.SellbotHQ,
     ToontownGlobals.CashbotHQ: CashbotHQ.CashbotHQ,
     ToontownGlobals.LawbotHQ: LawbotHQ.LawbotHQ,
     ToontownGlobals.GolfZone: GZHood.GZHood,
     ToontownGlobals.PartyHood: PartyHood.PartyHood}
    Hood2StateDict = {ToontownGlobals.ToontownCentral: 'TTHood',
     ToontownGlobals.DonaldsDock: 'DDHood',
     ToontownGlobals.TheBrrrgh: 'BRHood',
     ToontownGlobals.MinniesMelodyland: 'MMHood',
     ToontownGlobals.DaisyGardens: 'DGHood',
     ToontownGlobals.DonaldsDreamland: 'DLHood',
     ToontownGlobals.WackyWest: 'WWHood',
     ToontownGlobals.ConstructionZone: 'CZHood',
     ToontownGlobals.GoofySpeedway: 'GSHood',
     ToontownGlobals.OutdoorZone: 'OZHood',
     ToontownGlobals.MyEstate: 'EstateHood',
     ToontownGlobals.BossbotHQ: 'BossbotHQ',
     ToontownGlobals.SellbotHQ: 'SellbotHQ',
     ToontownGlobals.CashbotHQ: 'CashbotHQ',
     ToontownGlobals.LawbotHQ: 'LawbotHQ',
     ToontownGlobals.GolfZone: 'GZHood',
     ToontownGlobals.PartyHood: 'PartyHood'}

    def __init__(self, parentFSM, doneEvent):
        StateData.StateData.__init__(self, doneEvent)
        self.place = None
        self.fsm = ClassicFSM.ClassicFSM('PlayGame', [State.State('start', self.enterStart, self.exitStart, ['quietZone']),
         State.State('quietZone', self.enterQuietZone, self.exitQuietZone, ['TTHood',
          'DDHood',
          'BRHood',
          'MMHood',
          'DGHood',
          'DLHood',
          'WWHood',
          'CZHood',
          'GSHood',
          'OZHood',
          'GZHood',
          'SellbotHQ',
          'CashbotHQ',
          'LawbotHQ',
          'BossbotHQ',
          'EstateHood',
          'PartyHood']),
         State.State('TTHood', self.enterTTHood, self.exitTTHood, ['quietZone']),
         State.State('DDHood', self.enterDDHood, self.exitDDHood, ['quietZone']),
         State.State('BRHood', self.enterBRHood, self.exitBRHood, ['quietZone']),
         State.State('MMHood', self.enterMMHood, self.exitMMHood, ['quietZone']),
         State.State('DGHood', self.enterDGHood, self.exitDGHood, ['quietZone']),
         State.State('DLHood', self.enterDLHood, self.exitDLHood, ['quietZone']),
         State.State('WWHood', self.enterWWHood, self.exitWWHood, ['quietZone']),
         State.State('CZHood', self.enterCZHood, self.exitCZHood, ['quietZone']),
         State.State('GSHood', self.enterGSHood, self.exitGSHood, ['quietZone']),
         State.State('OZHood', self.enterOZHood, self.exitOZHood, ['quietZone']),
         State.State('GZHood', self.enterGZHood, self.exitGZHood, ['quietZone']),
         State.State('BossbotHQ', self.enterBossbotHQ, self.exitBossbotHQ, ['quietZone']),
         State.State('SellbotHQ', self.enterSellbotHQ, self.exitSellbotHQ, ['quietZone']),
         State.State('CashbotHQ', self.enterCashbotHQ, self.exitCashbotHQ, ['quietZone']),
         State.State('LawbotHQ', self.enterLawbotHQ, self.exitLawbotHQ, ['quietZone']),
         State.State('EstateHood', self.enterEstateHood, self.exitEstateHood, ['quietZone']),
         State.State('PartyHood', self.enterPartyHood, self.exitPartyHood, ['quietZone'])], 'start', 'start')
        self.fsm.enterInitialState()
        self.parentFSM = parentFSM
        self.parentFSM.getStateNamed('playGame').addChild(self.fsm)
        self.hoodDoneEvent = 'hoodDone'
        self.hood = None
        self.quietZoneDoneEvent = uniqueName('quietZoneDone')
        self.quietZoneStateData = None

    def enter(self, hoodId, zoneId, avId):
        if hoodId == ToontownGlobals.MyEstate:
            self.getEstateZoneAndGoHome(avId, zoneId)
            return
        elif hoodId == ToontownGlobals.PartyHood:
            self.getPartyZoneAndGoToParty(avId, zoneId)
            return
        else:
            loaderName = ZoneUtil.getLoaderName(zoneId)
            whereName = ZoneUtil.getToonWhereName(zoneId)
        self.fsm.request('quietZone', [{'loader': loaderName,
          'where': whereName,
          'how': 'teleportIn',
          'hoodId': hoodId,
          'zoneId': zoneId,
          'shardId': None,
          'avId': avId}])

    def exit(self):
        if base.placeBeforeObjects and self.quietZoneStateData:
            self.quietZoneStateData.exit()
            self.quietZoneStateData.unload()
            self.quietZoneStateData = None
        self.ignore(self.quietZoneDoneEvent)

    def load(self):
        pass

    def loadDnaStore(self):
        if not hasattr(self, 'dnaStore'):
            self.dnaStore = DNAStorage()
            files = ('phase_4/dna/storage.pdna', 'phase_3.5/dna/storage_interior.pdna')
            dnaBulk = DNABulkLoader(self.dnaStore, files)
            dnaBulk.loadDNAFiles()
            self.dnaStore.storeFont('humanist', ToontownGlobals.getInterfaceFont())
            self.dnaStore.storeFont('mickey', ToontownGlobals.getSignFont())
            self.dnaStore.storeFont('suit', ToontownGlobals.getSuitFont())

    def unloadDnaStore(self):
        if hasattr(self, 'dnaStore'):
            del self.dnaStore
            ModelPool.garbageCollect()
            TexturePool.garbageCollect()

    def unload(self):
        self.unloadDnaStore()
        if self.hood:
            self.notify.info('Aggressively cleaning up hood: %s' % self.hood)
            self.hood.exit()
            self.hood.unload()
            self.hood = None
        base.cr.cache.flush()

    def enterStart(self):
        pass

    def exitStart(self):
        pass

    def handleHoodDone(self):
        doneStatus = self.hood.getDoneStatus()
        shardId = doneStatus['shardId']
        if shardId != None:
            self.doneStatus = doneStatus
            messenger.send(self.doneEvent)
            base.transitions.fadeOut(0)
            return
        if doneStatus['where'] == 'party':
            self.getPartyZoneAndGoToParty(doneStatus['avId'], doneStatus['zoneId'])
            return
        how = doneStatus['how']
        if how in ['tunnelIn',
         'teleportIn',
         'doorIn',
         'elevatorIn',
         'skipTunnelIn']:
            self.fsm.request('quietZone', [doneStatus])
        else:
            self.notify.error('Exited hood with unexpected mode %s' % how)

    def _destroyHood(self):
        self.unload()

    def enterQuietZone(self, requestStatus):
        self.acceptOnce(self.quietZoneDoneEvent, self.handleQuietZoneDone)
        self.quietZoneStateData = QuietZoneState.QuietZoneState(self.quietZoneDoneEvent)
        self._quietZoneLeftEvent = self.quietZoneStateData.getQuietZoneLeftEvent()
        if base.placeBeforeObjects:
            self.acceptOnce(self._quietZoneLeftEvent, self.handleLeftQuietZone)
        self._enterWaitForSetZoneResponseMsg = self.quietZoneStateData.getEnterWaitForSetZoneResponseMsg()
        self.acceptOnce(self._enterWaitForSetZoneResponseMsg, self.handleWaitForSetZoneResponse)
        self.quietZoneStateData.load()
        self.quietZoneStateData.enter(requestStatus)

    def exitQuietZone(self):
        self.ignore(self._quietZoneLeftEvent)
        self.ignore(self._enterWaitForSetZoneResponseMsg)
        if not base.placeBeforeObjects:
            self.ignore(self.quietZoneDoneEvent)
            self.quietZoneStateData.exit()
            self.quietZoneStateData.unload()
            self.quietZoneStateData = None

    def handleWaitForSetZoneResponse(self, requestStatus):
        hoodId = requestStatus['hoodId']
        canonicalHoodId = ZoneUtil.getCanonicalZoneId(hoodId)
        toHoodPhrase = ToontownGlobals.hoodNameMap[canonicalHoodId][0]
        hoodName = ToontownGlobals.hoodNameMap[canonicalHoodId][-1]
        zoneId = requestStatus['zoneId']
        loaderName = requestStatus['loader']
        avId = requestStatus.get('avId', -1)
        ownerId = requestStatus.get('ownerId', avId)
        if base.config.GetBool('want-qa-regression', 0):
            self.notify.info('QA-REGRESSION: NEIGHBORHOODS: Visit %s' % hoodName)
        count = ToontownGlobals.hoodCountMap[canonicalHoodId]
        if loaderName == 'safeZoneLoader':
            count += ToontownGlobals.safeZoneCountMap[canonicalHoodId]
        elif loaderName == 'townLoader':
            count += ToontownGlobals.townCountMap[canonicalHoodId]
        if not loader.inBulkBlock:
            if hoodId == ToontownGlobals.MyEstate:
                if avId == -1:
                    loader.beginBulkLoad('hood', TTLocalizer.HeadingToYourEstate, count, 1, TTLocalizer.TIP_ESTATE, zoneId)
                else:
                    owner = base.cr.identifyAvatar(ownerId)
                    if owner == None:
                        friend = base.cr.identifyAvatar(avId)
                        if friend != None:
                            avName = friend.getName()
                            loader.beginBulkLoad('hood', TTLocalizer.HeadingToFriend % avName, count, 1, TTLocalizer.TIP_ESTATE, zoneId)
                        else:
                            self.notify.warning("we can't perform this teleport")
                            return
                    else:
                        avName = owner.getName()
                        loader.beginBulkLoad('hood', TTLocalizer.HeadingToEstate % avName, count, 1, TTLocalizer.TIP_ESTATE, zoneId)
            elif ZoneUtil.isCogHQZone(zoneId):
                loader.beginBulkLoad('hood', TTLocalizer.HeadingToHood % {'to': toHoodPhrase,
                 'hood': hoodName}, count, 1, TTLocalizer.TIP_COGHQ, zoneId)
            elif ZoneUtil.isGoofySpeedwayZone(zoneId):
                loader.beginBulkLoad('hood', TTLocalizer.HeadingToHood % {'to': toHoodPhrase,
                 'hood': hoodName}, count, 1, TTLocalizer.TIP_KARTING, zoneId)
            else:
                loader.beginBulkLoad('hood', TTLocalizer.HeadingToHood % {'to': toHoodPhrase,
                 'hood': hoodName}, count, 1, TTLocalizer.TIP_GENERAL, zoneId)
        if not hasattr(self, 'dnaStore'):
            self.loadDnaStore()
        hoodClass = self.getHoodClassByNumber(canonicalHoodId)
        self.hood = hoodClass(self.fsm, self.hoodDoneEvent, self.dnaStore, hoodId)
        self.hood.load()
        self.hood.loadLoader(requestStatus)
        if not base.placeBeforeObjects:
            loader.endBulkLoad('hood')

    def handleLeftQuietZone(self):
        status = self.quietZoneStateData.getRequestStatus()
        hoodId = ZoneUtil.getCanonicalZoneId(status['hoodId'])
        hoodState = self.getHoodStateByNumber(hoodId)
        self.fsm.request(hoodState, [status])

    def handleQuietZoneDone(self):
        if base.placeBeforeObjects:
            self.quietZoneStateData.exit()
            self.quietZoneStateData.unload()
            self.quietZoneStateData = None
            loader.endBulkLoad('hood')
        else:
            self.handleLeftQuietZone()

    def enterTTHood(self, requestStatus):
        self.accept(self.hoodDoneEvent, self.handleHoodDone)
        self.hood.enter(requestStatus)

    def exitTTHood(self):
        self._destroyHood()

    def enterDDHood(self, requestStatus):
        self.accept(self.hoodDoneEvent, self.handleHoodDone)
        self.hood.enter(requestStatus)

    def exitDDHood(self):
        self._destroyHood()

    def enterMMHood(self, requestStatus):
        self.accept(self.hoodDoneEvent, self.handleHoodDone)
        self.hood.enter(requestStatus)

    def exitMMHood(self):
        self._destroyHood()

    def enterBRHood(self, requestStatus):
        self.accept(self.hoodDoneEvent, self.handleHoodDone)
        self.hood.enter(requestStatus)

    def exitBRHood(self):
        self._destroyHood()

    def enterCZHood(self, requestStatus):
        self.accept(self.hoodDoneEvent, self.handleHoodDone)
        self.hood.enter(requestStatus)

    def exitCZHood(self):
        self._destroyHood()


    def enterDGHood(self, requestStatus):
        self.accept(self.hoodDoneEvent, self.handleHoodDone)
        self.hood.enter(requestStatus)

    def exitDGHood(self):
        self._destroyHood()

    def enterDLHood(self, requestStatus):
        self.accept(self.hoodDoneEvent, self.handleHoodDone)
        self.hood.enter(requestStatus)

    def exitDLHood(self):
        self._destroyHood()

    def enterWWHood(self, requestStatus):
        self.accept(self.hoodDoneEvent, self.handleHoodDone)
        self.hood.enter(requestStatus)

    def exitWWHood(self):
        self._destroyHood()        
        
    def enterGSHood(self, requestStatus):
        self.accept(self.hoodDoneEvent, self.handleHoodDone)
        self.hood.enter(requestStatus)

    def exitGSHood(self):
        self._destroyHood()

    def enterOZHood(self, requestStatus):
        self.accept(self.hoodDoneEvent, self.handleHoodDone)
        self.hood.enter(requestStatus)

    def exitOZHood(self):
        self._destroyHood()

    def enterGZHood(self, requestStatus):
        self.accept(self.hoodDoneEvent, self.handleHoodDone)
        self.hood.enter(requestStatus)

    def exitGZHood(self):
        self._destroyHood()

    def enterSellbotHQ(self, requestStatus):
        self.accept(self.hoodDoneEvent, self.handleHoodDone)
        self.hood.enter(requestStatus)

    def exitSellbotHQ(self):
        self._destroyHood()

    def enterCashbotHQ(self, requestStatus):
        self.accept(self.hoodDoneEvent, self.handleHoodDone)
        self.hood.enter(requestStatus)

    def exitCashbotHQ(self):
        self._destroyHood()

    def enterLawbotHQ(self, requestStatus):
        self.accept(self.hoodDoneEvent, self.handleHoodDone)
        self.hood.enter(requestStatus)

    def exitLawbotHQ(self):
        self._destroyHood()

    def enterBossbotHQ(self, requestStatus):
        self.accept(self.hoodDoneEvent, self.handleHoodDone)
        self.hood.enter(requestStatus)

    def exitBossbotHQ(self):
        self._destroyHood()

    def enterEstateHood(self, requestStatus):
        self.accept(self.hoodDoneEvent, self.handleHoodDone)
        self.hood.enter(requestStatus)

    def exitEstateHood(self):
        self._destroyHood()

    def getEstateZoneAndGoHome(self, avId, zoneId):
        self.doneStatus = {'avId': avId,
         'zoneId': zoneId,
         'hoodId': ToontownGlobals.MyEstate,
         'loader': 'safeZoneLoader',
         'how': 'teleportIn',
         'shardId': None}
        self.acceptOnce('setLocalEstateZone', self.goHome)
        if avId > 0:
            base.cr.estateMgr.getLocalEstateZone(avId)
        else:
            base.cr.estateMgr.getLocalEstateZone(base.localAvatar.getDoId())

    def goHome(self, ownerId, zoneId):
        self.notify.debug('goHome ownerId = %s' % ownerId)
        if ownerId > 0 and ownerId != base.localAvatar.doId and not base.cr.isFriend(ownerId):
            self.doneStatus['failed'] = 1
            taskMgr.remove('goHomeFailed')
            taskMgr.add(self.goHomeFailed, 'goHomeFailed')
            return
        if ownerId == 0 and zoneId == 0:
            self.doneStatus['failed'] = 1
            self.goHomeFailed(None)
            return
        if self.doneStatus['zoneId'] != zoneId:
            self.doneStatus['where'] = 'house'
        else:
            self.doneStatus['where'] = 'estate'
        self.doneStatus['ownerId'] = ownerId
        self.fsm.request('quietZone', [self.doneStatus])

    def goHomeFailed(self, task):
        self.notify.debug('goHomeFailed')
        failedToVisitAvId = self.doneStatus.get('avId')
        if failedToVisitAvId > 0:
            message = TTLocalizer.EstateTeleportFailedNotFriends % base.cr.identifyAvatar(failedToVisitAvId).getName()
        else:
            message = TTLocalizer.EstateTeleportFailed
        self.notify.debug('goHomeFailed, why =: %s' % message)
        self.ignore('setLocalEstateZone')
        zoneId = base.localAvatar.lastHood
        loaderName = ZoneUtil.getLoaderName(zoneId)
        whereName = ZoneUtil.getToonWhereName(zoneId)
        base.localAvatar.setSystemMessage(0, message)
        self.fsm.request('quietZone', [{'loader': loaderName,
          'where': whereName,
          'how': 'teleportIn',
          'hoodId': zoneId,
          'zoneId': zoneId,
          'shardId': None}])
        return Task.done

    def enterPartyHood(self, requestStatus):
        self.accept(self.hoodDoneEvent, self.handleHoodDone)
        requestStatus['where'] = 'party'
        self.hood.enter(requestStatus)

    def exitPartyHood(self):
        self._destroyHood()

    def getPartyZoneAndGoToParty(self, avId, zoneId):
        self.doneStatus = {'avId': avId,
         'zoneId': zoneId,
         'hoodId': ToontownGlobals.PartyHood,
         'loader': 'safeZoneLoader',
         'how': 'teleportIn',
         'shardId': None}
        if avId < 0:
            avId = base.localAvatar.getDoId()
        base.cr.partyManager.requestPartyZone(avId, zoneId, callback=self.goToParty)

    def goToParty(self, ownerId, partyId, zoneId):
        if ownerId == 0 or partyId == 0 or zoneId == 0:
            self.doneStatus['where'] = 'playground'
        else:
            self.doneStatus['where'] = 'party'
        self.doneStatus['ownerId'] = ownerId
        self.doneStatus['partyId'] = partyId
        self.doneStatus['zoneId'] = zoneId
        self.fsm.request('quietZone', [self.doneStatus])

    def goToPartyFailed(self, reason):
        self.notify.debug('goToPartyFailed')
        failedToVisitAvId = self.doneStatus.get('avId')
        message = base.cr.partyManager.getGoToPartyFailedMessage(reason)
        self.notify.debug('goToPartyFailed, why =: %s' % message)
        self.ignore('gotLocalPartyZone')
        zoneId = base.localAvatar.lastHood
        loaderName = ZoneUtil.getLoaderName(zoneId)
        whereName = ZoneUtil.getToonWhereName(zoneId)
        base.localAvatar.setSystemMessage(0, message)
        self.fsm.request('quietZone', [{'loader': loaderName,
          'where': whereName,
          'how': 'teleportIn',
          'hoodId': zoneId,
          'zoneId': zoneId,
          'shardId': None}])
        return Task.done

    def getCatalogCodes(self, category):
        numCodes = self.dnaStore.getNumCatalogCodes(category)
        codes = []
        for i in xrange(numCodes):
            codes.append(self.dnaStore.getCatalogCode(category, i))
        return codes

    def getNodePathList(self, catalogGroup):
        result = []
        codes = self.getCatalogCodes(catalogGroup)
        for code in codes:
            np = self.dnaStore.findNode(code)
            result.append(np)
        return result

    def getNodePathDict(self, catalogGroup):
        result = {}
        codes = self.getCatalogCodes(catalogGroup)
        for code in codes:
            np = self.dnaStore.findNode(code)
            result[code] = np
        return result

    def getHoodClassByNumber(self, hoodNumber):
        return self.Hood2ClassDict[hoodNumber]

    def getHoodStateByNumber(self, hoodNumber):
        return self.Hood2StateDict[hoodNumber]

    def setPlace(self, place):
        self.place = place
        if self.place:
            messenger.send('playGameSetPlace')

    def getPlace(self):
        return self.place

    def getPlaceId(self):
        return self.hood.hoodId if self.hood else None
