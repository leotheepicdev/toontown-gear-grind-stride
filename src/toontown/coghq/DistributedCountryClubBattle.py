
from direct.directnotify import DirectNotifyGlobal
from direct.fsm import ClassicFSM, State
from direct.interval.IntervalGlobal import *
from toontown.avatar import Emote
from lib.nametag import NametagGlobals
from toontown.battle import SuitBattleGlobals
from toontown.battle.BattleBase import *
from toontown.coghq import DistributedLevelBattle
from toontown.suit import SuitDNA
from toontown.toon import TTEmote
from toontown.base import ToontownGlobals


class DistributedCountryClubBattle(DistributedLevelBattle.DistributedLevelBattle):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedCountryClubBattle')

    def __init__(self, cr):
        DistributedLevelBattle.DistributedLevelBattle.__init__(self, cr)
        self.fsm.addState(State.State('CountryClubReward', self.enterCountryClubReward, self.exitCountryClubReward, ['Resume']))
        offState = self.fsm.getStateNamed('Off')
        offState.addTransition('CountryClubReward')
        playMovieState = self.fsm.getStateNamed('PlayMovie')
        playMovieState.addTransition('CountryClubReward')

    def enterCountryClubReward(self, ts):
        self.notify.debug('enterCountryClubReward()')
        self.disableCollision()
        self.delayDeleteMembers()
        if self.hasLocalToon():
            NametagGlobals.setMasterArrowsOn(0)
            if self.bossBattle:
                messenger.send('localToonConfrontedCountryClubBoss')
        self.movie.playReward(ts, self.uniqueName('building-reward'), self.__handleCountryClubRewardDone, noSkip=True)

    def __handleCountryClubRewardDone(self):
        self.notify.debug('countryClub reward done')
        if self.hasLocalToon():
            self.d_rewardDone()
        self.movie.resetReward()
        self.fsm.request('Resume')

    def exitCountryClubReward(self):
        self.notify.debug('exitCountryClubReward()')
        self.movie.resetReward(finish=1)
        self._removeMembersKeep()
        NametagGlobals.setMasterArrowsOn(1)
