from otp.ai.AIBaseGlobal import *
from toontown.avatar import DistributedAvatarAI
import SuitPlannerBase
import SuitBase
import SuitDNA
from direct.directnotify import DirectNotifyGlobal
from toontown.battle import SuitBattleGlobals
from toontown.base.ToontownGlobals import VIRTUAL_HP, VIRTUAL_HP_MULT, RANDOM_VIRTUAL_CHOICES
import random

class DistributedSuitBaseAI(DistributedAvatarAI.DistributedAvatarAI, SuitBase.SuitBase):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedSuitBaseAI')

    def __init__(self, air, suitPlanner):
        DistributedAvatarAI.DistributedAvatarAI.__init__(self, air)
        SuitBase.SuitBase.__init__(self)
        self.sp = suitPlanner
        self.maxHP = 10
        self.currHP = 10
        self.defenseDebuff = 0
        self.defenseMaxedOut = 0
        self.zoneId = 0
        self.dna = SuitDNA.SuitDNA()
        self.virtual = 0
        self.waiter = 0
        self.skeleRevives = 0
        self.maxSkeleRevives = 0
        self.reviveFlag = 0
        self.isExecutive = 0
        self.buildingHeight = None

    def generate(self):
        DistributedAvatarAI.DistributedAvatarAI.generate(self)

    def delete(self):
        self.sp = None
        del self.dna
        DistributedAvatarAI.DistributedAvatarAI.delete(self)
        SuitBase.SuitBase.delete(self)

    def requestRemoval(self):
        if self.sp != None:
            self.sp.removeSuit(self)
        else:
            self.requestDelete()

    def setLevel(self, lvl = None):
        attributes = SuitBattleGlobals.SuitAttributes[self.dna.name]
        if lvl:
            self.level = lvl - attributes['level'] - 1
        else:
            self.level = random.randint(1, 50)
        self.notify.debug('Assigning level ' + str(lvl))
        if hasattr(self, 'doId'):
            self.d_setLevelDist(self.level)
        hp = SuitBattleGlobals.getDefaultCogHP(lvl)
        self.maxHP = hp
        self.currHP = hp

    def getLevelDist(self):
        return self.getLevel()

    def d_setLevelDist(self, level):
        self.sendUpdate('setLevelDist', [level])

    def setupSuitDNA(self, level, type, track):
        dna = SuitDNA.SuitDNA()
        dna.newSuitRandom(type, track)
        self.dna = dna
        self.track = track
        self.setLevel(level)

    def getDNAString(self):
        if self.dna:
            return self.dna.makeNetString()
        else:
            self.notify.debug('No dna has been created for suit %d!' % self.getDoId())
            return ''

    def b_setBrushOff(self, index):
        self.setBrushOff(index)
        self.d_setBrushOff(index)

    def d_setBrushOff(self, index):
        self.sendUpdate('setBrushOff', [index])

    def setBrushOff(self, index):
        pass

    def d_denyBattle(self, toonId):
        self.sendUpdateToAvatarId(toonId, 'denyBattle', [])

    def b_setSkeleRevives(self, num):
        if num == None:
            num = 0
        self.setSkeleRevives(num)
        self.d_setSkeleRevives(self.getSkeleRevives())

    def d_setSkeleRevives(self, num):
        self.sendUpdate('setSkeleRevives', [num])

    def getSkeleRevives(self):
        return self.skeleRevives

    def setSkeleRevives(self, num):
        if num == None:
            num = 0
        self.skeleRevives = num
        if num > self.maxSkeleRevives:
            self.maxSkeleRevives = num

    def getMaxSkeleRevives(self):
        return self.maxSkeleRevives

    def useSkeleRevive(self):
        self.skeleRevives -= 1
        self.currHP = self.maxHP
        self.reviveFlag = 1

    def reviveCheckAndClear(self):
        returnValue = 0
        if self.reviveFlag == 1:
            returnValue = 1
            self.reviveFlag = 0
        return returnValue

    def b_setExecutive(self, flag):
        self.setExecutive(flag)
        self.d_setExecutive(flag)

    def setExecutive(self, flag):
        self.isExecutive = flag

    def d_setExecutive(self, flag):
        self.sendUpdate('setExecutive', [flag])

    def getExecutive(self):
        return self.isExecutive

    def getHP(self):
        return self.currHP
		
    def getMaxHP(self):
        return self.maxHP

    def setHP(self, hp):
        if hp > self.maxHP:
            self.currHP = self.maxHP
        else:
            self.currHP = hp

    def b_setHP(self, hp):
        self.setHP(hp)
        self.d_setHP(hp)

    def d_setHP(self, hp):
        self.sendUpdate('setHP', [hp])
        
    def getDefenseDebuff(self):
        return (self.defenseDebuff, self.defenseMaxedOut)
        
    def setDefenseDebuff(self, defenseDebuff, defenseMaxedOut):
        self.defenseDebuff = defenseDebuff
        self.defenseMaxedOut = defenseMaxedOut
        
    def b_setDefenseDebuff(self, defenseDebuff, defenseMaxedOut):
        self.setDefenseDebuff(defenseDebuff, defenseMaxedOut)
        self.d_setDefenseDebuff(defenseDebuff, defenseMaxedOut)
        
    def d_setDefenseDebuff(self, defenseDebuff, defenseMaxedOut):
        self.sendUpdate('setDefenseDebuff', [defenseDebuff, defenseMaxedOut])

    def releaseControl(self):
        pass

    def getDeathEvent(self):
        return 'cogDead-%s' % self.doId

    def resume(self):
        self.notify.debug('resume, hp=%s' % self.currHP)
        if self.currHP <= 0:
            messenger.send(self.getDeathEvent())
            self.requestRemoval()

    def prepareToJoinBattle(self):
        pass

    def b_setSkelecog(self, flag):
        self.setSkelecog(flag)
        self.d_setSkelecog(flag)

    def setSkelecog(self, flag):
        SuitBase.SuitBase.setSkelecog(self, flag)

    def d_setSkelecog(self, flag):
        self.sendUpdate('setSkelecog', [flag])

    def isForeman(self):
        return 0

    def isSupervisor(self):
        return 0
		
    def b_setVirtual(self, virtual):
        self.setVirtual(virtual)
        self.d_setVirtual(virtual)

    def setVirtual(self, virtual):
        self.virtual = virtual
        if self.virtual == VIRTUAL_HP:
            self.maxHP *= VIRTUAL_HP_MULT
            self.currHP *= VIRTUAL_HP_MULT
		
    def d_setVirtual(self, virtual):
        self.sendUpdate('setVirtual', [virtual])

    def getVirtual(self):
        return self.virtual
        
    def isVirtual(self):
        return self.getVirtual() > 0
        
    def makeRandomVirtual(self):
        self.b_setVirtual(random.choice(RANDOM_VIRTUAL_CHOICES))

    def setWaiter(self, flag):
        SuitBase.SuitBase.setWaiter(self, flag)

    def d_setWaiter(self, flag):
        self.sendUpdate('setWaiter', [flag])

    def b_setWaiter(self, flag):
        self.setWaiter(flag)
        self.d_setWaiter(flag)

    def getWaiter(self):
        return self.waiter
