from toontown.suit import DistributedFactorySuit
from toontown.suit.Suit import *
from direct.directnotify import DirectNotifyGlobal
from direct.actor import Actor
from toontown.avatar import Avatar
import SuitDNA
from toontown.base import ToontownGlobals
from toontown.battle import SuitBattleGlobals
from direct.task import Task
from toontown.battle import BattleProps
from toontown.base import TTLocalizer

class DistributedStageSuit(DistributedFactorySuit.DistributedFactorySuit):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedStageSuit')

    def setCogSpec(self, spec):
        self.spec = spec
        self.setPos(spec['pos'])
        self.setH(spec['h'])
        self.originalPos = spec['pos']
        self.escapePos = spec['pos']
        self.pathEntId = spec['path']
        self.behavior = spec['behavior']
        self.skeleton = spec['skeleton']
        self.boss = spec['boss']
        self.revives = spec.get('revives')
        if self.reserve:
            self.reparentTo(hidden)
        else:
            self.doReparent()
