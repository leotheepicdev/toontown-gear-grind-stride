from direct.directnotify.DirectNotifyGlobal import *
from toontown.hood import ZoneUtil, HoodUtil
from toontown.base import ToontownGlobals, ToontownBattleGlobals
from toontown.building import SuitBuildingGlobals
from toontown.dna.DNAParser import *

class SuitPlannerBase:
    notify = directNotify.newCategory('SuitPlannerBase')
    SuitHoodInfo = [[2100,
      5,
      15,
      0,
      5,
      20,
      4,
      (1,
       5,
       10,
       40,
       60,
       80),
      (25,
       25,
       25,
       25),
      (1, 2, 3),
      (0, 3),
      [], 0.1],
     [2200,
      3,
      10,
      0,
      5,
      15,
      4,
      (1,
       5,
       10,
       40,
       60,
       80),
      (10,
       70,
       10,
       10),
      (1, 2, 3),
      (0, 3),
      [], 0.1],
     [2300,
      3,
      10,
      0,
      5,
      15,
      4,
      (1,
       5,
       10,
       40,
       60,
       80),
      (10,
       10,
       40,
       40),
      (1, 2, 3),
      (0, 3),
      [], 0.1],
     [1100,
      1,
      5,
      0,
      99,
      100,
      4,
      (1,
       5,
       10,
       40,
       60,
       80),
      (90,
       10,
       0,
       0),
      (2, 3, 4, 5),
      (0, 4),
      [], 0.1],
     [1200,
      1,
      5,
      0,
      99,
      100,
      4,
      (1,
       5,
       10,
       40,
       60,
       80),
      (0,
       0,
       90,
       10),
      (3,
       4,
       5,
       6),
      (0, 4),
      [], 0.1],
     [1300,
      1,
      5,
      0,
      99,
      100,
      4,
      (1,
       5,
       10,
       40,
       60,
       80),
      (40,
       40,
       10,
       10),
      (3,
       4,
       5,
       6),
      (0, 4), 
      [], 0.1],
     [3100,
      1,
      5,
      0,
      99,
      100,
      4,
      (1,
       5,
       10,
       40,
       60,
       80),
      (90,
       10,
       0,
       0),
      (5, 6, 7, 8),
      (1, 6),
      [], 0.2],
     [3200,
      1,
      5,
      0,
      99,
      100,
      4,
      (1,
       5,
       10,
       40,
       60,
       80),
      (10,
       20,
       30,
       40),
      (6, 7, 8),
      (2, 6),
      [], 0.2],
     [3300,
      1,
      5,
      0,
      99,
      100,
      4,
      (1,
       5,
       10,
       40,
       60,
       80),
      (5,
       85,
       5,
       5),
      (7, 8, 9),
      (3, 7), 
      [], 0.2],
     [4100,
      1,
      5,
      0,
      99,
      100,
      4,
      (1,
       5,
       10,
       40,
       60,
       80),
      (0,
       0,
       50,
       50),
      (5, 6, 7, 8),
      (0, 5),
      [], 0.2],
     [4200,
      1,
      5,
      0,
      99,
      100,
      4,
      (1,
       5,
       10,
       40,
       60,
       80),
      (0,
       0,
       90,
       10),
      (6,
       7,
       8,
       9),
      (1, 6),
      [], 0.2],
     [4300,
      1,
      5,
      0,
      99,
      100,
      4,
      (1,
       5,
       10,
       40,
       60,
       80),
      (50,
       50,
       0,
       0),
      (6,
       7,
       8,
       9),
      (2, 6),
      [], 0.2],
     [5100,
      1,
      5,
      0,
      99,
      100,
      4,
      (1,
       5,
       10,
       40,
       60,
       80),
      (0,
       20,
       10,
       70),
      (2, 3, 4),
      (0, 5), 
      [], 0.1],
     [5200,
      1,
      5,
      0,
      99,
      100,
      4,
      (1,
       5,
       10,
       40,
       60,
       80),
      (10,
       70,
       0,
       20),
      (3,
       4,
       5,
       6),
      (0, 5), 
      [], 0.1],
     [5300,
      1,
      5,
      0,
      99,
      100,
      4,
      (1,
       5,
       10,
       40,
       60,
       80),
      (5,
       5,
       5,
       85),
      (4,
       5,
       6,
       7),
      (0, 6),
      [], 0.1],
     [9100,
      1,
      5,
      0,
      99,
      100,
      4,
      (1,
       5,
       10,
       40,
       60,
       80),
      (25,
       25,
       25,
       25),
      (9, 10, 11, 12, 13, 14, 15),
      (3, 7), 
      [], 0.2],
     [9200,
      1,
      5,
      0,
      99,
      100,
      4,
      (1,
       5,
       10,
       40,
       60,
       80),
      (5,
       5,
       85,
       5),
      (9, 10, 11, 12, 13, 14, 15),
      (3, 7),
      [], 0.2],
     [10000,
      3,
      15,
      0,
      5,
      15,
      3,
      (1,
       5,
       10,
       40,
       60,
       80),
      (100,
       0,
       0,
       0),
      (7, 8, 9, 10),
      (0, 7),
      [], 0.3],
     [11000,
      3,
      15,
      0,
      0,
      0,
      4,
      (1,
       5,
       10,
       40,
       60,
       80),
      (0,
       0,
       0,
       100),
      (4, 5, 6, 7),
      (0, 7),
      [], 0.3],
     [11200,
      10,
      20,
      0,
      0,
      0,
      4,
      (1,
       5,
       10,
       40,
       60,
       80),
      (0,
       0,
       0,
       100),
      (4, 5, 6, 7),
      (0, 7),
      [], 0.3],
     [12000,
      10,
      20,
      0,
      0,
      0,
      4,
      (1,
       5,
       10,
       40,
       60,
       80),
      (0,
       0,
       100,
       0),
      (7, 8, 9, 10),
      (0, 7),
      [], 0.3],
     [13000,
      10,
      20,
      0,
      0,
      0,
      4,
      (1,
       5,
       10,
       40,
       60,
       80),
      (0,
       100,
       0,
       0),
      (8, 9, 10),
      (0, 7),
      [], 0.3],
     [13200,
      10,
      20,
      0,
      0,
      0,
      4,
      (1,
       5,
       10,
       40,
       60,
       80),
      (0,
       100,
       0,
       0),
      (8, 9, 10),
      (5, 7),
      [], 0.3],     
     [14100,
      1,
      5,
      0,
      99,
      100,
      4,
      (1,
       5,
       10,
       40,
       60,
       80),
      (40,
       0,
       40,
       20),
      (11, 12, 13, 14, 15, 16, 17, 18),
      (3, 7),
      [], 0.2],
     [14200,
      1,
      5,
      0,
      99,
      100,
      4,
      (1,
       5,
       10,
       40,
       60,
       80),
      (10,
       50,
       30,
       10),
      (11, 12, 13, 14, 15, 16, 17, 18),
      (2, 7),
      [], 0.2],
     [14300,
      1,
      5,
      0,
      99,
      100,
      4,
      (1,
       5,
       10,
       40,
       60,
       80),
      (30,
       30,
       10,
       30),
      (12, 13, 14, 15, 16, 17, 18, 19, 20),
      (3, 7),
      [], 0.2]]
    SUIT_HOOD_INFO_ZONE = 0
    SUIT_HOOD_INFO_MIN = 1
    SUIT_HOOD_INFO_MAX = 2
    SUIT_HOOD_INFO_BMIN = 3
    SUIT_HOOD_INFO_BMAX = 4
    SUIT_HOOD_INFO_BWEIGHT = 5
    SUIT_HOOD_INFO_SMAX = 6
    SUIT_HOOD_INFO_JCHANCE = 7
    SUIT_HOOD_INFO_TRACK = 8
    SUIT_HOOD_INFO_LVL = 9
    SUIT_HOOD_INFO_MIN_MAX_TIER = 10
    SUIT_HOOD_INFO_HEIGHTS = 11
    SUIT_HOOD_INFO_EXECUTIVE_CHANCE = 12
    TOTAL_BWEIGHT = 0
    TOTAL_BWEIGHT_PER_TRACK = [0, 0, 0, 0]
    TOTAL_BWEIGHT_PER_HEIGHT = [0, 0, 0, 0, 0, 0, 0]
    
    def __init__(self):
        self.suitWalkSpeed = ToontownGlobals.SuitWalkSpeed
        self.dnaStore = None
        self.pointIndexes = {}

    def delete(self):
        del self.dnaStore

    def setupDNA(self):
        if self.dnaStore:
            return
        self.dnaStore = DNAStorage()
        dnaFileName = self.genDNAFileName()
        loadDNAFileAI(self.dnaStore, dnaFileName)
        self.initDNAInfo()

    def genDNAFileName(self):
        zoneId = ZoneUtil.getCanonicalZoneId(self.getZoneId())
        hoodId = ZoneUtil.getCanonicalHoodId(zoneId)
        hood = ToontownGlobals.dnaMap[hoodId]
        phase = ToontownGlobals.streetPhaseMap[hoodId]
        if hoodId == zoneId:
            zoneId = 'sz'
        return 'phase_%s/dna/%s_%s.pdna' % (phase, hood, zoneId)

    def getZoneId(self):
        return self.zoneId

    def setZoneId(self, zoneId):
        self.notify.debug('setting zone id for suit planner')
        self.zoneId = zoneId
        self.setupDNA()

    def extractGroupName(self, groupFullName):
        return groupFullName.split(':', 1)[0]

    def initDNAInfo(self):
        numGraphs = self.dnaStore.discoverContinuity()
        if numGraphs != 1:
            self.notify.info('zone %s has %s disconnected suit paths.' % (self.zoneId, numGraphs))
        self.battlePosDict = {}
        self.cellToGagBonusDict = {}

        for i in xrange(self.dnaStore.getNumDNAVisGroupsAI()):
            vg = self.dnaStore.getDNAVisGroupAI(i)
            zoneId = int(self.extractGroupName(vg.getName()))

            if vg.getNumBattleCells() == 1:
                battleCell = vg.getBattleCell(0)
                self.battlePosDict[zoneId] = vg.getBattleCell(0).getPos()
            elif vg.getNumBattleCells() > 1:
                self.notify.warning('multiple battle cells for zone: %d' % zoneId)
                self.battlePosDict[zoneId] = vg.getBattleCell(0).getPos()

            if True:
                for i in xrange(vg.getNumChildren()):
                    childDnaGroup = vg.at(i)

                    if isinstance(childDnaGroup, DNAInteractiveProp):
                        self.notify.debug('got interactive prop %s' % childDnaGroup)
                        battleCellId = childDnaGroup.getCellId()

                        if battleCellId == -1:
                            self.notify.warning('interactive prop %s  at %s not associated with a a battle' % (childDnaGroup, zoneId))

                        elif battleCellId == 0:
                            if zoneId in self.cellToGagBonusDict:
                                self.notify.error('FIXME battle cell at zone %s has two props %s %s linked to it' % (zoneId, self.cellToGagBonusDict[zoneId], childDnaGroup))
                            else:
                                name = childDnaGroup.getName()
                                propType = HoodUtil.calcPropType(name)
                                if propType in ToontownBattleGlobals.PropTypeToTrackBonus:
                                    trackBonus = ToontownBattleGlobals.PropTypeToTrackBonus[propType]
                                    self.cellToGagBonusDict[zoneId] = trackBonus

        self.dnaStore.resetDNAGroups()
        self.dnaStore.resetDNAVisGroups()
        self.dnaStore.resetDNAVisGroupsAI()
        self.streetPointList = []
        self.frontdoorPointList = []
        self.sidedoorPointList = []
        self.cogHQDoorPointList = []
        numPoints = self.dnaStore.getNumSuitPoints()
        for i in xrange(numPoints):
            point = self.dnaStore.getSuitPointAtIndex(i)
            if point.getPointType() == DNASuitPoint.FRONT_DOOR_POINT:
                self.frontdoorPointList.append(point)
            elif point.getPointType() == DNASuitPoint.SIDE_DOOR_POINT:
                self.sidedoorPointList.append(point)
            elif (point.getPointType() == DNASuitPoint.COGHQ_IN_POINT) or (point.getPointType() == DNASuitPoint.COGHQ_OUT_POINT):
                self.cogHQDoorPointList.append(point)
            else:
                self.streetPointList.append(point)
            self.pointIndexes[point.getIndex()] = point

    def performPathTest(self):
        if not self.notify.getDebug():
            return
        startAndEnd = self.pickPath()
        if not startAndEnd:
            return
        startPoint = startAndEnd[0]
        endPoint = startAndEnd[1]
        path = self.dnaStore.getSuitPath(startPoint, endPoint)
        numPathPoints = path.getNumPoints()
        for i in xrange(numPathPoints - 1):
            zone = self.dnaStore.getSuitEdgeZone(path.getPointIndex(i), path.getPointIndex(i + 1))
            travelTime = self.dnaStore.getSuitEdgeTravelTime(path.getPointIndex(i), path.getPointIndex(i + 1), self.suitWalkSpeed)
            self.notify.debug('edge from point ' + `i` + ' to point ' + `(i + 1)` + ' is in zone: ' + `zone` + ' and will take ' + `travelTime` + ' seconds to walk.')

    def genPath(self, startPoint, endPoint, minPathLen, maxPathLen):
        return self.dnaStore.getSuitPath(startPoint, endPoint, minPathLen, maxPathLen)

    def getDnaStore(self):
        return self.dnaStore
