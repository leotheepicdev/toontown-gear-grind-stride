from direct.directnotify.DirectNotifyGlobal import *
from direct.distributed import DistributedObjectAI
from direct.task import Task
import random

import DistributedSuitAI
import SuitDNA
import SuitPlannerBase
import SuitTimings
from otp.ai.AIBaseGlobal import *
from toontown.magicword.MagicWordGlobal import *
from toontown.battle import BattleManagerAI
from toontown.battle import SuitBattleGlobals
from toontown.building import HQBuildingAI
from toontown.building import SuitBuildingGlobals
from toontown.dna.DNAParser import DNASuitPoint
from toontown.hood import ZoneUtil
from toontown.suit.SuitInvasionGlobals import IFSkelecog, IFWaiter, IFV2, IFExecutive, IFVirtual
from libpandadna import *
from toontown.toon import NPCToons
from toontown.base import ToontownGlobals


ALLOWED_FO_TRACKS = 's'
if config.GetBool('want-lawbot-cogdo', True):
    ALLOWED_FO_TRACKS += 'l'
if config.GetBool('want-cashbot-cogdo', False):
    ALLOWED_FO_TRACKS += 'm'
if config.GetBool('want-bossbot-cogdo', False):
    ALLOWED_FO_TRACKS += 'b'
if config.GetBool('want-omni-cogdo', False):
    ALLOWED_FO_TRACKS += 'slcb'

DEFAULT_COGDO_RATIO = .5

class DistributedSuitPlannerAI(DistributedObjectAI.DistributedObjectAI, SuitPlannerBase.SuitPlannerBase):
    notify = directNotify.newCategory('DistributedSuitPlannerAI')
    CogdoPopFactor = config.GetFloat('cogdo-pop-factor', 1.5)
    CogdoRatio = min(1.0, max(0.0, config.GetFloat('cogdo-ratio', DEFAULT_COGDO_RATIO)))
    MAX_SUIT_TYPES = 6
    MAX_SUIT_TYPES_HQ = 7
    POP_UPKEEP_DELAY = 10
    POP_ADJUST_DELAY = 300
    PATH_COLLISION_BUFFER = 5
    TOTAL_MAX_SUITS = 50
    MIN_PATH_LEN = 40
    MAX_PATH_LEN = 300
    MIN_TAKEOVER_PATH_LEN = 2
    SUITS_ENTER_BUILDINGS = 1
    SUIT_BUILDING_NUM_SUITS = 1.5
    SUIT_BUILDING_TIMEOUT = [
        None, None, None, None, None, None, None,
        84, 72, 60, 48, 36, 24, 12, 6, 3, 1, 0.5
    ]
    TOTAL_SUIT_BUILDING_PCT = 18 * CogdoPopFactor
    BUILDING_HEIGHT_DISTRIBUTION = [14, 18, 25, 23, 20, 19, 17]
    defaultSuitName = simbase.config.GetString('suit-type', 'random')
    if defaultSuitName == 'random':
        defaultSuitName = None

    def __init__(self, air, zoneId):
        DistributedObjectAI.DistributedObjectAI.__init__(self, air)
        SuitPlannerBase.SuitPlannerBase.__init__(self)
        self.air = air
        self.zoneId = zoneId
        self.canonicalZoneId = ZoneUtil.getCanonicalZoneId(zoneId)
        if simbase.air.wantCogdominiums:
            if not hasattr(self.__class__, 'CogdoPopAdjusted'):
                self.__class__.CogdoPopAdjusted = True
                for index in xrange(len(self.SuitHoodInfo)):
                    SuitBuildingGlobals.buildingMinMax[self.zoneId][0] = int(0.5 + self.CogdoPopFactor * SuitBuildingGlobals.buildingMinMax[self.zoneId][0])
                    SuitBuildingGlobals.buildingMinMax[self.zoneId][1] = int(0.5 + self.CogdoPopFactor * SuitBuildingGlobals.buildingMinMax[self.zoneId][1])
        self.hoodInfoIdx = -1
        for index in xrange(len(self.SuitHoodInfo)):
            currHoodInfo = self.SuitHoodInfo[index]
            if currHoodInfo[self.SUIT_HOOD_INFO_ZONE] == self.canonicalZoneId:
                self.hoodInfoIdx = index
        self.currDesired = None
        self.baseNumSuits = (
            self.SuitHoodInfo[self.hoodInfoIdx][self.SUIT_HOOD_INFO_MIN] +
            self.SuitHoodInfo[self.hoodInfoIdx][self.SUIT_HOOD_INFO_MAX]) / 2
        self.targetNumSuitBuildings = SuitBuildingGlobals.buildingMinMax[self.zoneId][0]
        self.suitList = []
        self.numFlyInSuits = 0
        self.numBuildingSuits = 0
        self.numAttemptingTakeover = 0
        self.zoneInfo = {}
        self.zoneIdToPointMap = None
        self.cogHQDoors = []
        self.battleList = []
        self.battleMgr = BattleManagerAI.BattleManagerAI(self.air)
        self.setupDNA()
        if self.notify.getDebug():
            self.notify.debug('Creating a building manager AI in zone' + str(self.zoneId))
        self.buildingMgr = self.air.buildingManagers.get(self.zoneId)
        if self.buildingMgr:
            (blocks, hqBlocks, gagshopBlocks, petshopBlocks, kartshopBlocks) = self.buildingMgr.getDNABlockLists()
            for currBlock in blocks:
                bldg = self.buildingMgr.getBuilding(currBlock)
                bldg.setSuitPlannerExt(self)
        self.dnaStore.resetBlockNumbers()
        self.initBuildingsAndPoints()
        numSuits = simbase.config.GetInt('suit-count', -1)
        if numSuits >= 0:
            self.currDesired = numSuits
        suitHood = simbase.config.GetInt('suits-only-in-hood', -1)
        if suitHood >= 0:
            if self.SuitHoodInfo[self.hoodInfoIdx][self.SUIT_HOOD_INFO_ZONE] != suitHood:
                self.currDesired = 0
        self.suitCountAdjust = 0

    def cleanup(self):
        taskMgr.remove(self.taskName('sptUpkeepPopulation'))
        taskMgr.remove(self.taskName('sptAdjustPopulation'))
        for suit in self.suitList:
            suit.stopTasks()
            if suit.isGenerated():
                self.zoneChange(suit, suit.zoneId)
                suit.requestDelete()
        self.suitList = []
        self.numFlyInSuits = 0
        self.numBuildingSuits = 0
        self.numAttemptingTakeover = 0

    def delete(self):
        self.cleanup()
        DistributedObjectAI.DistributedObjectAI.delete(self)
        SuitPlannerBase.SuitPlannerBase.delete(self)

    def initBuildingsAndPoints(self):
        if not self.buildingMgr:
            return
        if self.notify.getDebug():
            self.notify.debug('Initializing building points')
        self.buildingFrontDoors = {}
        self.buildingSideDoors = {}
        for p in self.frontdoorPointList:
            blockNumber = p.getLandmarkBuildingIndex()
            if blockNumber < 0:
                self.notify.debug('No landmark building for (%s) in zone %s' % (str(p), self.zoneId))
                continue
            if blockNumber in self.buildingFrontDoors:
                self.notify.debug('Multiple front doors for building %s in zone %s' % (blockNumber, self.zoneId))
                continue
            self.buildingFrontDoors[blockNumber] = p
        for p in self.sidedoorPointList:
            blockNumber = p.getLandmarkBuildingIndex()
            if blockNumber < 0:
                self.notify.debug('No landmark building for (%s) in zone %s' % (str(p), self.zoneId))
                continue
            if blockNumber in self.buildingSideDoors:
                self.buildingSideDoors[blockNumber].append(p)
                continue
            self.buildingSideDoors[blockNumber] = [p]
        for bldg in self.buildingMgr.getBuildings():
            if isinstance(bldg, HQBuildingAI.HQBuildingAI):
                continue
            blockNumber = bldg.getBlock()[0]
            if blockNumber not in self.buildingFrontDoors:
                self.notify.debug('No front door for building %s in zone %s' % (blockNumber, self.zoneId))
            if blockNumber not in self.buildingSideDoors:
                self.notify.debug('No side door for building %s in zone %s' % (blockNumber, self.zoneId))

    def countNumSuitsPerTrack(self, count):
        for suit in self.suitList:
            if suit.track in count:
                count[suit.track] += 1
                continue
            count[suit.track] = 1

    def countNumBuildingsPerTrack(self, count):
        if not self.buildingMgr:
            return
        for building in self.buildingMgr.getBuildings():
            if building.isSuitBuilding():
                if building.track in count:
                    count[building.track] += 1
                else:
                    count[building.track] = 1

    def calcDesiredNumFlyInSuits(self):
        if self.currDesired is not None:
            return 0
        return self.baseNumSuits + self.suitCountAdjust

    def calcDesiredNumBuildingSuits(self):
        if self.currDesired is not None:
            return self.currDesired
        if not self.buildingMgr:
            return 0
        suitBuildings = self.buildingMgr.getEstablishedSuitBlocks()
        return int(len(suitBuildings) * self.SUIT_BUILDING_NUM_SUITS)

    def getZoneIdToPointMap(self):
        if self.zoneIdToPointMap is not None:
            return self.zoneIdToPointMap
        self.zoneIdToPointMap = {}
        for point in self.streetPointList:
            points = self.dnaStore.getAdjacentPoints(point)
            i = points.getNumPoints() - 1
            while i >= 0:
                pi = points.getPointIndex(i)
                p = self.pointIndexes[pi]
                i -= 1
                zoneId = self.dnaStore.getSuitEdgeZone(point.getIndex(), p.getIndex())
                if zoneId in self.zoneIdToPointMap:
                    self.zoneIdToPointMap[zoneId].append(point)
                    continue
                self.zoneIdToPointMap[zoneId] = [point]
        return self.zoneIdToPointMap

    def getStreetPointsForBuilding(self, blockNumber):
        pointList = []
        if blockNumber in self.buildingSideDoors:
            for doorPoint in self.buildingSideDoors[blockNumber]:
                points = self.dnaStore.getAdjacentPoints(doorPoint)
                i = points.getNumPoints() - 1
                while i >= 0:
                    pi = points.getPointIndex(i)
                    point = self.pointIndexes[pi]
                    if point.getPointType() == DNASuitPoint.STREET_POINT:
                        pointList.append(point)
                    i -= 1
        if blockNumber in self.buildingFrontDoors:
            doorPoint = self.buildingFrontDoors[blockNumber]
            points = self.dnaStore.getAdjacentPoints(doorPoint)
            i = points.getNumPoints() - 1
            while i >= 0:
                pi = points.getPointIndex(i)
                pointList.append(self.pointIndexes[pi])
                i -= 1
        return pointList

    def createNewSuit(self, blockNumbers, streetPoints, toonBlockTakeover=None,
            cogdoTakeover=None, minPathLen=None, maxPathLen=None,
            buildingHeight=None, suitLevel=None, suitType=None, suitTrack=None,
            suitName=None, skelecog=None, revives=None, waiter=None, executive=None, virtual=None):
        startPoint = None
        blockNumber = None
        if self.notify.getDebug():
            self.notify.debug('Choosing origin from %d+%d possibles.' % (len(streetPoints), len(blockNumbers)))
        while startPoint == None and len(blockNumbers) > 0:
            bn = random.choice(blockNumbers)
            blockNumbers.remove(bn)
            if bn in self.buildingSideDoors:
                for doorPoint in self.buildingSideDoors[bn]:
                    points = self.dnaStore.getAdjacentPoints(doorPoint)
                    i = points.getNumPoints() - 1
                    while blockNumber == None and i >= 0:
                        pi = points.getPointIndex(i)
                        p = self.pointIndexes[pi]
                        i -= 1
                        startTime = SuitTimings.fromSuitBuilding
                        startTime += self.dnaStore.getSuitEdgeTravelTime(doorPoint.getIndex(), pi, self.suitWalkSpeed)
                        if not self.pointCollision(p, doorPoint, startTime):
                            startTime = SuitTimings.fromSuitBuilding
                            startPoint = doorPoint
                            blockNumber = bn
        while startPoint == None and len(streetPoints) > 0:
            p = random.choice(streetPoints)
            streetPoints.remove(p)
            if not self.pointCollision(p, None, SuitTimings.fromSky):
                startPoint = p
                startTime = SuitTimings.fromSky
                continue
        if startPoint == None:
            return None
        newSuit = DistributedSuitAI.DistributedSuitAI(simbase.air, self)
        newSuit.startPoint = startPoint
        if blockNumber != None:
            newSuit.buildingSuit = 1
            if suitTrack == None:
                suitTrack = self.buildingMgr.getBuildingTrack(blockNumber)
        else:
            newSuit.flyInSuit = 1
            newSuit.attemptingTakeover = self.newSuitShouldAttemptTakeover()
        if suitName is None:
            suitDeptIndex, suitTypeIndex, flags = self.air.suitInvasionManager.getInvadingCog()
            if flags & IFSkelecog:
                skelecog = 1
            if flags & IFWaiter:
                waiter = True
            if flags & IFV2:
                revives = 1
            if flags & IFExecutive:
                executive = 1
            if flags & IFVirtual:
                skelecog = 1
                virtual = 1
            if suitDeptIndex is not None:
                suitTrack = SuitDNA.suitDepts[suitDeptIndex]
            if suitTypeIndex is not None:
                suitName = self.air.suitInvasionManager.getSuitName()
            else:
                suitName = self.defaultSuitName
        if (suitType is None) and (suitName is not None):
            suitType = SuitDNA.getSuitType(suitName)
            suitTrack = SuitDNA.getSuitDept(suitName)
        if (suitLevel is None) and (buildingHeight is not None):
            suitLevel = self.chooseSuitLevel(self.SuitHoodInfo[self.hoodInfoIdx][self.SUIT_HOOD_INFO_LVL], buildingHeight)
        (suitLevel, suitType, suitTrack) = self.pickLevelTypeAndTrack(suitLevel, suitType, suitTrack)
        newSuit.setupSuitDNA(suitLevel, suitType, suitTrack)
        newSuit.buildingHeight = buildingHeight
        gotDestination = self.chooseDestination(newSuit, startTime, toonBlockTakeover = toonBlockTakeover, cogdoTakeover = cogdoTakeover, minPathLen = minPathLen, maxPathLen = maxPathLen)
        if not gotDestination:
            self.notify.debug("Couldn't get a destination in %d!" % self.zoneId)
            newSuit.doNotDeallocateChannel = None
            newSuit.delete()
            return None
        if ZoneUtil.isCogHQZone(self.zoneId) and not self.air.suitInvasionManager.getInvading():
            if random.random() <= 0.1:
                skelecog = 1
                if self.zoneId == ToontownGlobals.LawbotHQ and random.random() <= 0.5:
                    virtual = 1
        newSuit.initializePath()
        self.zoneChange(newSuit, None, newSuit.zoneId)
        if skelecog and revives is None:
            newSuit.setSkelecog(skelecog)
        newSuit.generateWithRequired(newSuit.zoneId)
        if virtual:
            newSuit.makeRandomVirtual()
        if revives is not None:
            newSuit.b_setSkeleRevives(revives)
        if waiter:
            newSuit.b_setWaiter(1)
        if executive:
            newSuit.b_setExecutive(1)
        if skelecog is None and waiter is None and revives is None and executive is None and virtual is None:
            if random.random() <= self.SuitHoodInfo[self.hoodInfoIdx][self.SUIT_HOOD_INFO_EXECUTIVE_CHANCE]:
                newSuit.b_setExecutive(1)        
        newSuit.d_setSPDoId(self.doId)
        newSuit.moveToNextLeg(None)
        self.suitList.append(newSuit)
        if newSuit.flyInSuit:
            self.numFlyInSuits += 1
        if newSuit.buildingSuit:
            self.numBuildingSuits += 1
        if newSuit.attemptingTakeover:
            self.numAttemptingTakeover += 1
        return newSuit

    def countNumNeededBuildings(self):
        if not self.buildingMgr:
            return False
        numSuitBuildings = len(self.buildingMgr.getSuitBlocks())
        if (random.random() * 100) < SuitBuildingGlobals.buildingChance[self.zoneId]:
            return SuitBuildingGlobals.buildingMinMax[self.zoneId][1] - numSuitBuildings
        else:
            return self.targetNumSuitBuildings - numSuitBuildings

    def newSuitShouldAttemptTakeover(self):
        if not self.SUITS_ENTER_BUILDINGS:
            return False
        numNeeded = self.countNumNeededBuildings()
        if self.numAttemptingTakeover >= numNeeded:
            return False
        self.notify.debug('DSP %s is planning a takeover attempt in zone %s' % (self.getDoId(), self.zoneId))
        return True

    def chooseDestination(self, suit, startTime, toonBlockTakeover=None,
            cogdoTakeover=None, minPathLen=None, maxPathLen=None):
        possibles = []
        backup = []

        if toonBlockTakeover is not None:
            suit.attemptingTakeover = 1
            blockNumber = toonBlockTakeover
            if blockNumber in self.buildingFrontDoors:
                possibles.append((blockNumber, self.buildingFrontDoors[blockNumber]))
        elif suit.attemptingTakeover:
            for blockNumber in self.buildingMgr.getToonBlocks():
                building = self.buildingMgr.getBuilding(blockNumber)
                (extZoneId, intZoneId) = building.getExteriorAndInteriorZoneId()
                if not NPCToons.isZoneProtected(intZoneId):
                    if blockNumber in self.buildingFrontDoors:
                        possibles.append((blockNumber, self.buildingFrontDoors[blockNumber]))
            if cogdoTakeover is None:
                if suit.dna.dept in ALLOWED_FO_TRACKS:
                    cogdoTakeover = random.random() < self.CogdoRatio
        elif self.buildingMgr:
            for blockNumber in self.buildingMgr.getSuitBlocks():
                track = self.buildingMgr.getBuildingTrack(blockNumber)
                if (track == suit.track) and (blockNumber in self.buildingSideDoors):
                    for doorPoint in self.buildingSideDoors[blockNumber]:
                        possibles.append((blockNumber, doorPoint))
        backup = []
        for p in self.streetPointList:
            backup.append((None, p))
        if self.notify.getDebug():
            self.notify.debug('Choosing destination point from %s+%s possibles.' % (len(possibles), len(backup)))
        if len(possibles) == 0:
            possibles = backup
            backup = []
        if minPathLen is None:
            if suit.attemptingTakeover:
                minPathLen = self.MIN_TAKEOVER_PATH_LEN
            else:
                minPathLen = self.MIN_PATH_LEN
        if maxPathLen is None:
            maxPathLen = self.MAX_PATH_LEN
        retryCount = 0
        while (len(possibles) > 0) and (retryCount < 50):
            p = random.choice(possibles)
            possibles.remove(p)
            if len(possibles) == 0:
                possibles = backup
                backup = []
            path = self.genPath(suit.startPoint, p[1], minPathLen, maxPathLen)
            if path and (not self.pathCollision(path, startTime)):
                suit.endPoint = p[1]
                suit.minPathLen = minPathLen
                suit.maxPathLen = maxPathLen
                suit.buildingDestination = p[0]
                suit.buildingDestinationIsCogdo = cogdoTakeover
                suit.setPath(path)
                return 1
            retryCount += 1
        return 0

    def pathCollision(self, path, elapsedTime):
        i = 0
        pi = path.getPointIndex(i)
        point = self.pointIndexes[pi]
        adjacentPoint = self.pointIndexes[path.getPointIndex(i + 1)]
        while (point.getPointType() == DNASuitPoint.FRONT_DOOR_POINT) or (
                point.getPointType() == DNASuitPoint.SIDE_DOOR_POINT):
            i += 1
            lastPi = pi
            pi = path.getPointIndex(i)
            adjacentPoint = point
            point = self.pointIndexes[pi]
            elapsedTime += self.dnaStore.getSuitEdgeTravelTime(lastPi, pi, self.suitWalkSpeed)
        result = self.pointCollision(point, adjacentPoint, elapsedTime)
        return result

    def pointCollision(self, point, adjacentPoint, elapsedTime):
        for suit in self.suitList:
            if suit.pointInMyPath(point, elapsedTime):
                return 1
        if adjacentPoint is not None:
            return self.battleCollision(point, adjacentPoint)
        else:
            points = self.dnaStore.getAdjacentPoints(point)
            i = points.getNumPoints() - 1
            while i >= 0:
                pi = points.getPointIndex(i)
                p = self.pointIndexes[pi]
                i -= 1
                if self.battleCollision(point, p):
                    return 1
        return 0

    def battleCollision(self, point, adjacentPoint):
        zoneId = self.dnaStore.getSuitEdgeZone(point.getIndex(), adjacentPoint.getIndex())
        return self.battleMgr.cellHasBattle(zoneId)

    def removeSuit(self, suit):
        self.zoneChange(suit, suit.zoneId)
        if self.suitList.count(suit) > 0:
            self.suitList.remove(suit)
            if suit.flyInSuit:
                self.numFlyInSuits -= 1
            if suit.buildingSuit:
                self.numBuildingSuits -= 1
            if suit.attemptingTakeover:
                self.numAttemptingTakeover -= 1
        suit.requestDelete()

    def countTakeovers(self):
        count = 0
        for suit in self.suitList:
            if suit.attemptingTakeover:
                count += 1
        return count

    def __waitForNextUpkeep(self):
        t = random.random() * 2.0 + self.POP_UPKEEP_DELAY
        taskMgr.doMethodLater(t, self.upkeepSuitPopulation, self.taskName('sptUpkeepPopulation'))

    def __waitForNextAdjust(self):
        t = random.random() * 10.0 + self.POP_ADJUST_DELAY
        taskMgr.doMethodLater(t, self.adjustSuitPopulation, self.taskName('sptAdjustPopulation'))

    def upkeepSuitPopulation(self, task):
        targetFlyInNum = self.calcDesiredNumFlyInSuits()
        targetFlyInNum = min(targetFlyInNum, self.TOTAL_MAX_SUITS - self.numBuildingSuits)
        streetPoints = self.streetPointList[:]
        flyInDeficit = ((targetFlyInNum - self.numFlyInSuits) + 3) / 4
        while flyInDeficit > 0:
            if not self.createNewSuit([], streetPoints):
                break
            flyInDeficit -= 1
        if self.buildingMgr:
            suitBuildings = self.buildingMgr.getEstablishedSuitBlocks()
        else:
            suitBuildings = []
        if self.currDesired != None:
            targetBuildingNum = max(0, self.currDesired - self.numFlyInSuits)
        else:
            targetBuildingNum = int(len(suitBuildings) * self.SUIT_BUILDING_NUM_SUITS)
        targetBuildingNum += flyInDeficit
        targetBuildingNum = min(targetBuildingNum, self.TOTAL_MAX_SUITS - self.numFlyInSuits)
        buildingDeficit = ((targetBuildingNum - self.numBuildingSuits) + 3) / 4
        while buildingDeficit > 0:
            if not self.createNewSuit(suitBuildings, streetPoints):
                break
            buildingDeficit -= 1
        if self.notify.getDebug() and self.currDesired == None:
            self.notify.debug('zone %d has %d of %d fly-in and %d of %d building suits.' % (self.zoneId, self.numFlyInSuits, targetFlyInNum, self.numBuildingSuits, targetBuildingNum))
            if buildingDeficit != 0:
                self.notify.debug('remaining deficit is %d.' % buildingDeficit)
        if self.buildingMgr:
            suitBuildings = self.buildingMgr.getEstablishedSuitBlocks()
            timeoutIndex = min(len(suitBuildings), len(self.SUIT_BUILDING_TIMEOUT) - 1)
            timeout = self.SUIT_BUILDING_TIMEOUT[timeoutIndex]
            if timeout != None:
                timeout *= 3600.0
                oldest = None
                oldestAge = 0
                now = time.time()
                for b in suitBuildings:
                    building = self.buildingMgr.getBuilding(b)
                    if hasattr(building, 'elevator'):
                        if building.elevator.fsm.getCurrentState().getName() == 'waitEmpty':
                            age = now - building.becameSuitTime
                            if age > oldestAge:
                                oldest = building
                                oldestAge = age
                if oldestAge > timeout:
                    self.notify.info('Street %d has %d buildings; reclaiming %0.2f-hour-old building.' % (self.zoneId, len(suitBuildings), oldestAge / 3600.0))
                    oldest.b_setVictorList([0, 0, 0, 0])
                    oldest.updateSavedBy(None)
                    oldest.toonTakeOver()
        self.__waitForNextUpkeep()
        return Task.done

    def adjustSuitPopulation(self, task):
        hoodInfo = self.SuitHoodInfo[self.hoodInfoIdx]
        if hoodInfo[self.SUIT_HOOD_INFO_MAX] == 0:
            self.__waitForNextAdjust()
            return Task.done
        min = hoodInfo[self.SUIT_HOOD_INFO_MIN]
        max = hoodInfo[self.SUIT_HOOD_INFO_MAX]
        adjustment = random.choice((-3, -2, -2, -2, -1, -1, 0, 0, 0, 1, 1, 2, 2, 2, 3))
        self.suitCountAdjust += adjustment
        desiredNum = self.calcDesiredNumFlyInSuits()
        if desiredNum < min:
            self.suitCountAdjust = min - self.baseNumSuits
        elif desiredNum > max:
            self.suitCountAdjust = max - self.baseNumSuits
        self.__waitForNextAdjust()
        return Task.done

    def suitTakeOver(self, blockNumber, dept, suitLevel):
        building = self.buildingMgr.getBuilding(blockNumber)
        if building is None:
            return
        building.suitTakeOver(dept, suitLevel)

    def cogdoTakeOver(self, blockNumber, dept, suitLevel):
        building = self.buildingMgr.getBuilding(blockNumber)
        if building:
            building.cogdoTakeOver(dept, suitLevel)

    def recycleBuilding(self):
        bmin = SuitBuildingGlobals.buildingMinMax[self.zoneId][0]
        current = len(self.buildingMgr.getSuitBlocks())
        if (self.targetNumSuitBuildings > bmin) and (current <= self.targetNumSuitBuildings):
            self.targetNumSuitBuildings -= 1
            self.assignSuitBuildings(1)

    def createInitialSuitBuildings(self):
        if self.buildingMgr is None:
            return

        # If we aren't at our minimum number of buildings, let's spawn some!
        suitBlockCount = len(self.buildingMgr.getSuitBlocks())
        if suitBlockCount < self.targetNumSuitBuildings:
            for _ in xrange(self.targetNumSuitBuildings - suitBlockCount):
                blockNumber = random.choice(self.buildingMgr.getToonBlocks())
                building = self.buildingMgr.getBuilding(blockNumber)
                if building is None:
                    continue
                if NPCToons.isZoneProtected(building.getExteriorAndInteriorZoneId()[1]):
                    continue
                suitName = self.air.suitInvasionManager.getInvadingCog()[0]
                if suitName is None:
                    suitName = self.defaultSuitName
                suitType = None
                suitTrack = None
                if suitName is not None:
                    suitType = SuitDNA.getSuitType(suitName)
                    suitTrack = SuitDNA.getSuitDept(suitName)
                (suitLevel, suitType, suitTrack) = self.pickLevelTypeAndTrack(None, suitType, suitTrack)
                building.suitTakeOver(suitTrack, suitLevel)

        # Save the building manager's state:
        self.buildingMgr.save()
        
    def assignSuitBuildings(self, numToAssign):
        hoodInfo = self.SuitHoodInfo[:]
        totalWeight = self.TOTAL_BWEIGHT
        while numToAssign > 0:
            repeat = 1
            while repeat:
                if len(hoodInfo) == 0:
                    return
                currHoodInfo = self.chooseStreetNoPreference(hoodInfo, totalWeight)
                zoneId = currHoodInfo[self.SUIT_HOOD_INFO_ZONE]
                if zoneId in self.air.suitPlanners:
                    sp = self.air.suitPlanners[zoneId]
                    numTarget = sp.targetNumSuitBuildings
                    numTotalBuildings = len(sp.frontdoorPointList)
                else:
                    numTarget = 0
                    numTotalBuildings = 0
                if numTarget >= SuitBuildingGlobals.buildingMinMax[self.zoneId][1] or numTarget >= numTotalBuildings:
                    hoodInfo.remove(currHoodInfo)
                    repeat = 1
                else:
                    repeat = 0
                chosenBlock = random.choice(possibleBlocks)
                sp.targetNumSuitBuildings += 1
                numToAssign -= 1                
          
    def unassignSuitBuildings(self, numToAssign):
        hoodInfo = self.SuitHoodInfo[:]
        totalWeight = self.TOTAL_BWEIGHT
        while numToAssign > 0:
            repeat = 1
            while repeat:
                if len(hoodInfo) == 0:
                    self.notify.warning('No more streets can remove suit buildings, with %s buildings too many!' % numToAssign)
                    return
                repeat = 0
                currHoodInfo = self.chooseStreetNoPreference(hoodInfo, totalWeight)
                zoneId = currHoodInfo[self.SUIT_HOOD_INFO_ZONE]
                if zoneId in self.air.suitPlanners:
                    sp = self.air.suitPlanners[zoneId]
                    numTarget = sp.targetNumSuitBuildings
                    numTotalBuildings = len(sp.frontdoorPointList)
                else:
                    numTarget = 0
                    numTotalBuildings = 0
                if numTarget <= SuitBuildingGlobals.buildingMinMax[self.zoneId][0]:
                    self.notify.info("Zone %s can't remove any more buildings." % zoneId)
                    hoodInfo.remove(currHoodInfo)
                    totalWeight -= currHoodInfo[self.SUIT_HOOD_INFO_BWEIGHT]
                    repeat = 1
            self.notify.info('Unassigning building from zone %s.' % zoneId)
            sp.targetNumSuitBuildings -= 1
            numToAssign -= 1

    def chooseStreetNoPreference(self, hoodInfo, totalWeight):
        c = random.random() * totalWeight
        t = 0
        for currHoodInfo in hoodInfo:
            weight = currHoodInfo[self.SUIT_HOOD_INFO_BWEIGHT]
            t += weight
            if c < t:
                return currHoodInfo
        self.notify.warning('Weighted random choice failed! Total is %s, chose %s' % (t, c))
        return random.choice(hoodInfo)

    def chooseSuitLevel(self, possibleLevels, buildingHeight):
        choices = []
        for level in possibleLevels:
            (minFloors, maxFloors) = SuitBuildingGlobals.SuitBuildingInfo[level - 1][0]
            if buildingHeight >= minFloors - 1 and buildingHeight <= maxFloors - 1:
                choices.append(level)
        return random.choice(choices)

    def initTasks(self):
        if self.air.wantCogbuildings:
            self.createInitialSuitBuildings()
        self.__waitForNextUpkeep()
        self.__waitForNextAdjust()

    def resyncSuits(self):
        for suit in self.suitList:
            suit.resync()

    def flySuits(self):
        for suit in self.suitList:
            if suit.pathState == 1:
                suit.flyAwayNow()

    def requestBattle(self, zoneId, suit, toonId):
        self.notify.debug('requestBattle() - zone: %s suit: %s toon: %s' % (zoneId, suit.doId, toonId))
        canonicalZoneId = ZoneUtil.getCanonicalZoneId(zoneId)
        if canonicalZoneId not in self.battlePosDict:
            return 0
        toon = self.air.doId2do.get(toonId)
        if toon.getBattleId() > 0:
            self.notify.warning('We tried to request a battle when the toon was already in battle')
            return 0
        if toon:
            if hasattr(toon, 'doId'):
                toon.b_setBattleId(toonId)

        pos = self.battlePosDict[canonicalZoneId]

        interactivePropTrackBonus = -1
        if config.GetBool('props-buff-battles', True) and canonicalZoneId in self.cellToGagBonusDict:
            interactivePropTrackBonus = self.cellToGagBonusDict[canonicalZoneId]

        self.battleMgr.newBattle(
            zoneId, zoneId, pos, suit, toonId, self.__battleFinished,
            self.SuitHoodInfo[self.hoodInfoIdx][self.SUIT_HOOD_INFO_SMAX],
            interactivePropTrackBonus)
        for currOther in self.zoneInfo[zoneId]:
            self.notify.debug('Found suit %s in this new battle zone %s' % (currOther.getDoId(), zoneId))
            if currOther != suit:
                if currOther.pathState == 1 and currOther.legType == SuitLeg.TWalk:
                    self.checkForBattle(zoneId, currOther)
        return 1

    def __battleFinished(self, zoneId):
        self.notify.debug('DistSuitPlannerAI: battle in zone ' + str(zoneId) + ' finished')
        currBattleIdx = 0
        while currBattleIdx < len(self.battleList):
            currBattle = self.battleList[currBattleIdx]
            if currBattle[0] == zoneId:
                self.notify.debug('DistSuitPlannerAI: battle removed')
                self.battleList.remove(currBattle)
            currBattleIdx = currBattleIdx + 1

    def __suitCanJoinBattle(self, zoneId):
        battle = self.battleMgr.getBattle(zoneId)
        if len(battle.suits) >= 4:
            return 0
        if battle:
            if simbase.config.GetBool('suits-always-join', 0):
                return 1
            jChanceList = self.SuitHoodInfo[self.hoodInfoIdx][self.SUIT_HOOD_INFO_JCHANCE]
            ratioIdx = (len(battle.toons) - battle.numSuitsEver) + 2
            if ratioIdx >= 0:
                if ratioIdx < len(jChanceList):
                    if random.randint(0, 99) < jChanceList[ratioIdx]:
                        return 1
                else:
                    self.notify.warning('__suitCanJoinBattle idx out of range!')
                    return 1
        return 0

    def checkForBattle(self, zoneId, suit):
        if self.battleMgr.cellHasBattle(zoneId):
            if self.__suitCanJoinBattle(zoneId) and self.battleMgr.requestBattleAddSuit(zoneId, suit):
                return 1
            suit.flyAwayNow()
            return 1
        else:
            return 0


    def postBattleResumeCheck(self, suit):
        self.notify.debug('DistSuitPlannerAI:postBattleResumeCheck: suit ' + str(suit.getDoId()) + ' is leaving battle')
        battleIndex = 0
        for currBattle in self.battleList:
            if suit.zoneId == currBattle[0]:
                self.notify.debug(' battle found' + str(suit.zoneId))
                for currPath in currBattle[1]:
                    for currPathPtSuit in xrange(suit.currWpt, suit.myPath.getNumPoints()):
                        ptIdx = suit.myPath.getPointIndex(currPathPtSuit)
                        if self.notify.getDebug():
                            self.notify.debug(' comparing' + str(ptIdx) + 'with' + str(currPath))
                        if currPath == ptIdx:
                            if self.notify.getDebug():
                                self.notify.debug(' match found, telling' + 'suit to fly')
                            return 0
            battleIndex += 1
        pointList = []
        for currPathPtSuit in xrange(suit.currWpt, suit.myPath.getNumPoints()):
            ptIdx = suit.myPath.getPointIndex(currPathPtSuit)
            if self.notify.getDebug():
                self.notify.debug(' appending point with index of' + str(ptIdx))
            pointList.append(ptIdx)
        self.battleList.append([suit.zoneId, pointList])
        return 1

    def zoneChange(self, suit, oldZone, newZone=None):
        if (oldZone in self.zoneInfo) and (suit in self.zoneInfo[oldZone]):
            self.zoneInfo[oldZone].remove(suit)
        if newZone is not None:
            if newZone not in self.zoneInfo:
                self.zoneInfo[newZone] = []
            self.zoneInfo[newZone].append(suit)

    def d_setZoneId(self, zoneId):
        self.sendUpdate('setZoneId', [self.getZoneId()])

    def getZoneId(self):
        return self.zoneId

    def suitListQuery(self):
        suitIndexList = []
        for suit in self.suitList:
            suitIndexList.append(SuitDNA.suitHeadTypes.index(suit.dna.name))
        self.sendUpdateToAvatarId(self.air.getAvatarIdFromSender(), 'suitListResponse', [suitIndexList])

    def buildingListQuery(self):
        buildingDict = {}
        self.countNumBuildingsPerTrack(buildingDict)
        buildingList = [0, 0, 0, 0]
        for dept in SuitDNA.suitDepts:
            if dept in buildingDict:
                buildingList[SuitDNA.suitDepts.index(dept)] = buildingDict[dept]
        self.sendUpdateToAvatarId(self.air.getAvatarIdFromSender(), 'buildingListResponse', [buildingList])

    def pickLevelTypeAndTrack(self, level=None, type=None, track=None):
        if level is None:
            level = random.choice(self.SuitHoodInfo[self.hoodInfoIdx][self.SUIT_HOOD_INFO_LVL])
        if type is None:
            min = self.SuitHoodInfo[self.hoodInfoIdx][self.SUIT_HOOD_INFO_MIN_MAX_TIER][0]
            max = self.SuitHoodInfo[self.hoodInfoIdx][self.SUIT_HOOD_INFO_MIN_MAX_TIER][1]
            type = random.randint(min, max)
        if track is None:
            track = SuitDNA.suitDepts[SuitBattleGlobals.pickFromFreqList(self.SuitHoodInfo[self.hoodInfoIdx][self.SUIT_HOOD_INFO_TRACK])]
        return (level, type, track)

# TODO: special cogs
@magicWord(types=[str, int], category=CATEGORY_ADMINISTRATOR)
def spawnCog(name, level):
    av = spellbook.getInvoker()
    zoneId = av.getLocation()[1]
    sp = simbase.air.suitPlanners.get(zoneId - zoneId % 100)
    pointmap = sp.streetPointList
    sp.createNewSuit([], pointmap, suitName=name, suitLevel=level)
    return 'Spawned %s in current zone.' % name