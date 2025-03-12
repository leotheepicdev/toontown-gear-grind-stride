from direct.interval.IntervalGlobal import *
from toontown.battle.BattleBase import *
from toontown.coghq import DistributedLevelBattle
from direct.directnotify import DirectNotifyGlobal
from toontown.toon import TTEmote
from toontown.avatar import Emote
from toontown.battle import SuitBattleGlobals
from toontown.suit import SuitDNA
from direct.fsm import ClassicFSM, State
from toontown.base import ToontownGlobals
from lib.nametag import NametagGlobals

class DistributedStageBattle(DistributedLevelBattle.DistributedLevelBattle):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedStageBattle')

    def __init__(self, cr):
        DistributedLevelBattle.DistributedLevelBattle.__init__(self, cr)
        self.fsm.addState(State.State('StageReward', self.enterStageReward, self.exitStageReward, ['Resume']))
        offState = self.fsm.getStateNamed('Off')
        offState.addTransition('StageReward')
        playMovieState = self.fsm.getStateNamed('PlayMovie')
        playMovieState.addTransition('StageReward')

    def enterStageReward(self, ts):
        self.notify.debug('enterStageReward()')
        self.disableCollision()
        self.delayDeleteMembers()
        if self.hasLocalToon():
            NametagGlobals.setMasterArrowsOn(0)
            if self.bossBattle:
                messenger.send('localToonConfrontedStageBoss')
        self.movie.playReward(ts, self.uniqueName('building-reward'), self.__handleStageRewardDone, noSkip=True)

    def __handleStageRewardDone(self):
        self.notify.debug('stage reward done')
        if self.hasLocalToon():
            self.d_rewardDone()
        self.movie.resetReward()
        self.fsm.request('Resume')

    def exitStageReward(self):
        self.notify.debug('exitStageReward()')
        self.movie.resetReward(finish=1)
        self._removeMembersKeep()
        NametagGlobals.setMasterArrowsOn(1)
