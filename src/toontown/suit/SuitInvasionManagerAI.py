import random, time
from direct.showbase.DirectObject import DirectObject
from toontown.ai.HolidayGlobals import Holidays2Cog
from toontown.suit.SuitInvasionGlobals import *
from toontown.suit import SuitDNA
from toontown.base import ToontownGlobals
from SuitInvasionGlobalsAI import *

class SuitInvasionManagerAI(DirectObject):
    notify = directNotify.newCategory('SuitInvasionManagerAI')
    notify.setInfo(True)

    def __init__(self, air, wantRandomInvasions=True, invasionOnly=False):
        self.air = air
        self.wantRandomInvasions = wantRandomInvasions
        self.invasionOnly = invasionOnly
        self.invading = False
        self.activeInvasionHolidays = []
        self.start = 0
        self.remaining = 0
        self.total = 0
        self.suitDeptIndex = None
        self.suitTypeIndex = None
        self.flags = 0
        
    def areSummonsAllowed(self):
        if self.invasionOnly:
            return False
        return True
        
    def getInitialDelayTime(self):
        return random.randint(450, 900)
        
    def getDelayTime(self):
        return random.randint(1800, 3600)
        
    def beginRandomInvasions(self):
        if self.invasionOnly:
            self.notify.info('Starting invasion-only district invasion...')
            self.doRandomInvasion()
        else:
            self.notify.info('Starting random invasions...')
            taskMgr.doMethodLater(self.getInitialDelayTime(), self.doRandomInvasion, TASK_NAME)
        
    def doRandomInvasion(self, task=None):
        if self.activeInvasionHolidays:
            if random.random() < 0.4:
                # We want to create a holiday invasion. Forget most of the randomness of this code, and begin an invasion for the holiday Cog!
                chosenHoliday = random.choice(self.activeInvasionHolidays)
                if chosenHoliday in Holidays2Cog:
                    suitDeptIndex = Holidays2Cog[chosenHoliday][0]
                    suitTypeIndex = Holidays2Cog[chosenHoliday][1]
                    type = INVASION_TYPE_BRUTAL
                    flags = random.choice([0, IFSkelecog, IFWaiter, IFV2, IFExecutive, IFVirtual])
                    self.notify.info('A random holiday Invasion is beginning: suitDeptIndex={0}, suitTypeIndex={1}, flags={2}, type={3}'.format(suitDeptIndex, suitTypeIndex, flags, type))
                    self.beginInvasion(suitDeptIndex, suitTypeIndex, flags, type)
                    return
                    
        suitDeptIndex = random.randint(0, len(SuitDNA.suitDepts) - 1)
        if random.random () <= 0.1:
            suitTypeIndex = None
        else:
            suitTypeIndex = random.randint(0, SuitDNA.suitsPerDept - 1)
        type = random.choice([INVASION_TYPE_NORMAL, INVASION_TYPE_MEGA])
        flags = random.choice([0, IFSkelecog, IFWaiter, IFV2, IFExecutive, IFVirtual])
        self.notify.info('A random invasion is beginning: suitDeptIndex={0}, suitTypeIndex={1}, flags={2}, type={3}'.format(suitDeptIndex, suitTypeIndex, flags, type))
        self.beginInvasion(suitDeptIndex, suitTypeIndex, flags, type)
                    
    def addMegaInvasionHoliday(self, id):
        self.activeInvasionHolidays.append(id)
        
    def removeMegaInvasionHoliday(self, id):
        self.activeInvasionHolidays.remove(id)
        
    def beginInvasion(self, suitDeptIndex=None, suitTypeIndex=None, flags=0, type=INVASION_TYPE_NORMAL, summoned=False):
        if self.invading:
            # An invasion is currently in progress; ignore this request.
            return False
        if (suitDeptIndex is None) and (suitTypeIndex is None) and (not flags):
            # This invasion is no-op.
            return False
        if (suitDeptIndex is None) and (suitTypeIndex is not None):
            # It's impossible to determine the invading Cog.
            return False
        if flags not in (0, IFV2, IFSkelecog, IFWaiter, IFExecutive, IFVirtual):
            # The provided flag combination is not possible.
            return False
        if (suitDeptIndex is not None) and (suitDeptIndex >= len(SuitDNA.suitDepts)):
            # Invalid suit department.
            return False
        if (suitTypeIndex is not None) and (suitTypeIndex >= SuitDNA.suitsPerDept):
            # Invalid suit type.
            return False
        if type not in (INVASION_TYPE_NORMAL, INVASION_TYPE_MEGA, INVASION_TYPE_BRUTAL):
            # Invalid invasion type.
            return False
        if summoned and taskMgr.hasTaskNamed(TASK_NAME):
            # Someone has used a summon before random invasions occurred. Turn off the task.
            taskMgr.remove(TASK_NAME)
        self.invading = True
        self.start = int(time.time())
        self.suitDeptIndex = suitDeptIndex
        self.suitTypeIndex = suitTypeIndex
        self.flags = flags
        if type == INVASION_TYPE_NORMAL:
            self.total = random.randint(1000, 3000)
        elif type == INVASION_TYPE_MEGA:
            self.total = 5000
        elif type == INVASION_TYPE_BRUTAL:
            self.total = 10000
        self.remaining = self.total
        self.flySuits()
        self.notifyInvasionStarted()
        if self.suitDeptIndex is not None:
            self.air.distributedDistrict.b_setInvasionStatus(self.suitDeptIndex + 1)
        else:
            self.air.distributedDistrict.b_setInvasionStatus(5)
        if type == INVASION_TYPE_NORMAL:
            timeout = config.GetInt('invasion-timeout', 1800)
            taskMgr.doMethodLater(timeout, self.endInvasion, 'invasionTimeout')
        if type == INVASION_TYPE_MEGA:
            timeout = config.GetInt('invasion-timeout', 3200)
        if type == INVASION_TYPE_BRUTAL:
            timeout = config.GetInt('invasion-timeout', 10000)
        return True
        
    def endInvasion(self, task=None):
        if not self.invading:
            # We are not currently invading.
            return False
        # Stop the invasion timeout task:
        taskMgr.remove('invasionTimeout')
        # Update the invasion tracker on the districts page in the Shticker Book:
        self.air.distributedDistrict.b_setInvasionStatus(0)
        # Revert what was done when the invasion started:
        self.notifyInvasionEnded()
        self.invading = False
        self.start = 0
        self.suitDeptIndex = None
        self.suitTypeIndex = None
        self.flags = 0
        self.total = 0
        self.remaining = 0
        self.flySuits()
        if self.invasionOnly:
            # We are an invasion only district. Start another invasion!
            self.doRandomInvasion()
        else:
            if self.wantRandomInvasions:
                # The invasion has ended! Start the task again.
                taskMgr.doMethodLater(self.getDelayTime(), self.doRandomInvasion, TASK_NAME) 
        return True
        
    def getInvading(self):
        return self.invading

    def getInvadingCog(self):
        return (self.suitDeptIndex, self.suitTypeIndex, self.flags)
        
    def getSuitName(self):
        if self.suitDeptIndex is not None:
            if self.suitTypeIndex is not None:
                return SuitDNA.getSuitName(self.suitDeptIndex, self.suitTypeIndex)
            else:
                return SuitDNA.suitDepts[self.suitDeptIndex]
        else:
            return SuitDNA.suitHeadTypes[0]

    def notifyInvasionStarted(self):
        msgType = ToontownGlobals.SuitInvasionBegin
        if self.flags & IFSkelecog:
            msgType = ToontownGlobals.SkelecogInvasionBegin
        elif self.flags & IFWaiter:
            msgType = ToontownGlobals.WaiterInvasionBegin
        elif self.flags & IFV2:
            msgType = ToontownGlobals.V2InvasionBegin
        elif self.flags & IFExecutive:
            msgType = ToontownGlobals.ExecutiveInvasionBegin
        elif self.flags & IFVirtual:
            msgType = ToontownGlobals.VirtualInvasionBegin
        self.air.newsManager.sendUpdate('setInvasionStatus', [msgType, self.getSuitName(), self.total, self.flags])

    def notifyInvasionEnded(self):
        msgType = ToontownGlobals.SuitInvasionEnd
        if self.flags & IFSkelecog:
            msgType = ToontownGlobals.SkelecogInvasionEnd
        elif self.flags & IFWaiter:
            msgType = ToontownGlobals.WaiterInvasionEnd
        elif self.flags & IFV2:
            msgType = ToontownGlobals.V2InvasionEnd
        elif self.flags & IFExecutive:
            msgType = ToontownGlobals.ExecutiveInvasionEnd
        elif self.flags & IFVirtual:
            msgType = ToontownGlobals.VirtualInvasionEnd
        self.air.newsManager.sendUpdate('setInvasionStatus', [msgType, self.getSuitName(), 0, self.flags])

    def notifyInvasionUpdate(self):
        self.air.newsManager.sendUpdate('setInvasionStatus', [ToontownGlobals.SuitInvasionUpdate, self.getSuitName(), self.remaining, self.flags])

    def notifyInvasionBulletin(self, avId):
        msgType = ToontownGlobals.SuitInvasionBulletin
        if self.flags & IFSkelecog:
            msgType = ToontownGlobals.SkelecogInvasionBulletin
        elif self.flags & IFWaiter:
            msgType = ToontownGlobals.WaiterInvasionBulletin
        elif self.flags & IFV2:
            msgType = ToontownGlobals.V2InvasionBulletin
        elif self.flags & IFExecutive:
            msgType = ToontownGlobals.ExecutiveInvasionBulletin
        elif self.flags & IFVirtual:
            msgType = ToontownGlobals.VirtualInvasionBulletin
        self.air.newsManager.sendUpdateToAvatarId(avId, 'setInvasionStatus', [msgType, self.getSuitName(), self.remaining, self.flags])

    def flySuits(self):
        for suitPlanner in list(self.air.suitPlanners.values()):
            suitPlanner.flySuits()
            
    def handleSuitDefeated(self):
        self.remaining -= 1
        if self.remaining == 0:
            self.endInvasion()
        elif self.remaining == (self.total/2):
            self.notifyInvasionUpdate()
