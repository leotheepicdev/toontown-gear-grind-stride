import SuitDNA
from libpandadna import *
import SuitTimings
from direct.directnotify import DirectNotifyGlobal
from direct.distributed.ClockDelta import *
from toontown.battle import SuitBattleGlobals
from toontown.base import TTLocalizer
TIME_BUFFER_PER_WPT = 0.25
TIME_DIVISOR = 100
DISTRIBUTE_TASK_CREATION = 0

class SuitBase:
    notify = DirectNotifyGlobal.directNotify.newCategory('SuitBase')

    def __init__(self):
        self.dna = None
        self.level = 0
        self.maxHP = 10
        self.currHP = 10
        self.defenseDebuff = 0
        self.defenseMaxedOut = 0
        self.isSkelecog = 0
        self.isWaiter = 0
        self.isExecutive = 0

    def delete(self):
        if hasattr(self, 'legList'):
            del self.legList

    def getCurrHp(self):
        if hasattr(self, 'currHP') and self.currHP:
            return self.currHP
        else:
            self.notify.error('currHP is None')
            return 'unknown'

    def getMaxHp(self):
        if hasattr(self, 'maxHP') and self.maxHP:
            return self.maxHP
        else:
            self.notify.error('maxHP is None')
            return 'unknown'

    def getStyleName(self):
        if hasattr(self, 'dna') and self.dna:
            return self.dna.name
        else:
            self.notify.error('called getStyleName() before dna was set!')
            return 'unknown'

    def getStyleDept(self):
        if hasattr(self, 'dna') and self.dna:
            return SuitDNA.getDeptFullname(self.dna.dept)
        else:
            self.notify.error('called getStyleDept() before dna was set!')
            return 'unknown'

    def getLevel(self):
        return self.level

    def setLevel(self, level): # todo: redo this
        self.level = level
        nameWLevel = TTLocalizer.SuitBaseNameWithLevel % {'name': self.name,
         'dept': self.getStyleDept(),
         'level': self.getActualLevel()}
        self.setDisplayName(nameWLevel)
        attributes = SuitBattleGlobals.SuitAttributes[self.dna.name]
        self.maxHP = SuitBattleGlobals.getDefaultCogHP(self.getActualLevel())
        self.currHP = self.maxHP

    def getSkelecog(self):
        return self.isSkelecog

    def setSkelecog(self, flag):
        self.isSkelecog = flag

    def setWaiter(self, flag):
        self.isWaiter = flag

    def getExecutive(self):
        return self.isExecutive

    def setExecutive(self, flag):
        self.isExecutive = flag

    def getActualLevel(self):
        if hasattr(self, 'dna'):
            return SuitBattleGlobals.getActualFromRelativeLevel(self.getStyleName(), self.level) + 1
        else:
            self.notify.warning('called getActualLevel with no DNA, returning 1 for level')
            return 1

    def setPath(self, path):
        self.path = path
        self.pathLength = self.path.getNumPoints()

    def getPath(self):
        return self.path

    def printPath(self):
        print '%d points in path' % self.pathLength
        for currPathPt in xrange(self.pathLength):
            indexVal = self.path.getPointIndex(currPathPt)
            print '\t', self.sp.dnaStore.getSuitPointWithIndex(indexVal)

    def makeLegList(self):
        self.legList = SuitLegList(self.path, self.sp.dnaStore)
