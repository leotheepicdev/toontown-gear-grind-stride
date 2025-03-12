from panda3d.core import CardMaker, NodePath, Texture
from direct.directnotify import DirectNotifyGlobal
from direct.showbase import PythonUtil
from toontown.base import ToontownBattleGlobals
from toontown.base import ToontownGlobals
from toontown.base import TTLocalizer
from toontown.battle import SuitBattleGlobals
from toontown.coghq import CogDisguiseGlobals
from toontown.toon import NPCToons
from toontown.hood import ZoneUtil
import random
import copy
import time
import types

notify = DirectNotifyGlobal.directNotify.newCategory('Quests')
ItemDict = TTLocalizer.QuestsItemDict
CompleteString = TTLocalizer.QuestsCompleteString
NotChosenString = TTLocalizer.QuestsNotChosenString
DefaultGreeting = TTLocalizer.QuestsDefaultGreeting
DefaultIncomplete = TTLocalizer.QuestsDefaultIncomplete
DefaultIncompleteProgress = TTLocalizer.QuestsDefaultIncompleteProgress
DefaultIncompleteWrongNPC = TTLocalizer.QuestsDefaultIncompleteWrongNPC
DefaultComplete = TTLocalizer.QuestsDefaultComplete
DefaultLeaving = TTLocalizer.QuestsDefaultLeaving
DefaultReject = TTLocalizer.QuestsDefaultReject
DefaultTierNotDone = TTLocalizer.QuestsDefaultTierNotDone
DefaultQuest = TTLocalizer.QuestsDefaultQuest
DefaultVisitQuestDialog = TTLocalizer.QuestsDefaultVisitQuestDialog
GREETING = 0
QUEST = 1
INCOMPLETE = 2
INCOMPLETE_PROGRESS = 3
INCOMPLETE_WRONG_NPC = 4
COMPLETE = 5
LEAVING = 6
Any = 1
OBSOLETE = 'OBSOLETE'
Start = 1
Cont = 0
Anywhere = 1
NA = 2
Same = 3
AnyFish = 4
AnyCashbotSuitPart = 5
AnyLawbotSuitPart = 6
AnyBossbotSuitPart = 7
ToonTailor = 999
ToonHQ = 1000
InVP = 0
InFO = 1
WithCheat = 2
QuestDictTierIndex = 0
QuestDictStartIndex = 1
QuestDictDescIndex = 2
QuestDictFromNpcIndex = 3
QuestDictToNpcIndex = 4
QuestDictRewardIndex = 5
QuestDictNextQuestIndex = 6
QuestDictDialogIndex = 7
VeryEasy = 100
Easy = 75
Medium = 50
Hard = 25
VeryHard = 20
Fun = 15
TT_TIER = 0
DD_TIER = 4
DG_TIER = 7
MM_TIER = 10
BR_TIER = 13
CZ_TIER = 16
DL_TIER = 20
WW_TIER = 24
PRE_ELDER_TIER = 49
ELDER_TIER = 50
LOOPING_FINAL_TIER = ELDER_TIER
VISIT_QUEST_ID = 1000
TROLLEY_QUEST_ID = 110
FIRST_COG_QUEST_ID = 145
FRIEND_QUEST_ID = 150
PHONE_QUEST_ID = 175
from toontown.base.ToontownGlobals import FT_FullSuit, FT_Leg, FT_Arm, FT_Torso
QuestRandGen = random.Random()

def seedRandomGen(npcId, avId, tier, rewardHistory):
    QuestRandGen.seed(npcId * 100 + avId + tier + len(rewardHistory))


def seededRandomChoice(seq):
    return QuestRandGen.choice(seq)


def getCompleteStatusWithNpc(questComplete, toNpcId, npc):
    if questComplete:
        if npc:
            if npcMatches(toNpcId, npc):
                return COMPLETE
            else:
                return INCOMPLETE_WRONG_NPC
        else:
            return COMPLETE
    elif npc:
        if npcMatches(toNpcId, npc):
            return INCOMPLETE_PROGRESS
        else:
            return INCOMPLETE
    else:
        return INCOMPLETE


def npcMatches(toNpcId, npc):
    return toNpcId == npc.getNpcId() or toNpcId == Any or toNpcId == ToonHQ and npc.getHq() or toNpcId == ToonTailor and npc.getTailor()


def calcRecoverChance(numberNotDone, chance, cap = 1):
    avgNum2Kill = 1.0 / (chance / 100.0)
    diff = float(numberNotDone - avgNum2Kill * 0.5)
    luck = 1.0 + abs(diff / (avgNum2Kill * 0.5))
    chance *= luck
    return chance


def simulateRecoveryVar(numNeeded, baseChance, list = 0, cap = 1):
    numHave = 0
    numTries = 0
    greatestFailChain = 0
    currentFail = 0
    capHits = 0
    attemptList = {}
    while numHave < numNeeded:
        numTries += 1
        chance = calcRecoverChance(currentFail, baseChance, cap)
        test = random.random() * 100
        if chance == 1000:
            capHits += 1
        if test < chance:
            numHave += 1
            if currentFail > greatestFailChain:
                greatestFailChain = currentFail
            if attemptList.get(currentFail):
                attemptList[currentFail] += 1
            else:
                attemptList[currentFail] = 1
            currentFail = 0
        else:
            currentFail += 1

    print 'Test results: %s tries, %s longest failure chain, %s cap hits' % (numTries, greatestFailChain, capHits)
    if list:
        print 'failures for each succes %s' % attemptList


def simulateRecoveryFix(numNeeded, baseChance, list = 0):
    numHave = 0
    numTries = 0
    greatestFailChain = 0
    currentFail = 0
    attemptList = {}
    while numHave < numNeeded:
        numTries += 1
        chance = baseChance
        test = random.random() * 100
        if test < chance:
            numHave += 1
            if currentFail > greatestFailChain:
                greatestFailChain = currentFail
            if attemptList.get(currentFail):
                attemptList[currentFail] += 1
            else:
                attemptList[currentFail] = 1
            currentFail = 0
        else:
            currentFail += 1

    print 'Test results: %s tries, %s longest failure chain' % (numTries, greatestFailChain)
    if list:
        print 'failures for each success %s' % attemptList


class Quest:
    _cogTracks = [Any,
     'c',
     'l',
     'm',
     's']
    _factoryTypes = [Any,
     FT_FullSuit,
     FT_Leg,
     FT_Arm,
     FT_Torso]

    def check(self, cond, msg):
        pass

    def checkLocation(self, location):
        locations = [Anywhere] + TTLocalizer.GlobalStreetNames.keys()
        self.check(location in locations, 'invalid location: %s' % location)

    def checkNumCogs(self, num):
        self.check(1, 'invalid number of cogs: %s' % num)

    def checkCogType(self, type):
        types = [Any] + SuitBattleGlobals.SuitAttributes.keys()
        self.check(type in types, 'invalid cog type: %s' % type)

    def checkCogTrack(self, track):
        self.check(track in self._cogTracks, 'invalid cog track: %s' % track)

    def checkCogLevel(self, level):
        self.check(level >= 1 and level <= 12, 'invalid cog level: %s' % level)

    def checkNumSkelecogs(self, num):
        self.check(1, 'invalid number of cogs: %s' % num)

    def checkSkelecogTrack(self, track):
        self.check(track in self._cogTracks, 'invalid cog track: %s' % track)

    def checkSkelecogLevel(self, level):
        self.check(level >= 1 and level <= 12, 'invalid cog level: %s' % level)

    def checkNumSkeleRevives(self, num):
        self.check(1, 'invalid number of cogs: %s' % num)

    def checkNumForemen(self, num):
        self.check(num > 0, 'invalid number of foremen: %s' % num)

    def checkNumBosses(self, num):
        self.check(num > 0, 'invalid number of bosses: %s' % num)

    def checkNumSupervisors(self, num):
        self.check(num > 0, 'invalid number of supervisors: %s' % num)

    def checkNumBuildings(self, num):
        self.check(1, 'invalid num buildings: %s' % num)

    def checkBuildingTrack(self, track):
        self.check(track in self._cogTracks, 'invalid building track: %s' % track)

    def checkBuildingFloors(self, floors):
        self.check(floors >= 1 and floors <= 7, 'invalid num floors: %s' % floors)

    def checkBuildingType(self, cogdo):
        self.check(cogdo != 0 and cogdo != 1, 'invalid cogdo value: %s' % cogdo)

    def checkNumFactories(self, num):
        self.check(1, 'invalid num factories: %s' % num)

    def checkFactoryType(self, type):
        self.check(type in self._factoryTypes, 'invalid factory type: %s' % type)

    def checkNumMints(self, num):
        self.check(1, 'invalid num mints: %s' % num)

    def checkNumCogParts(self, num):
        self.check(1, 'invalid num cog parts: %s' % num)

    def checkNumGags(self, num):
        self.check(1, 'invalid num gags: %s' % num)

    def checkGagItem(self, item):
        self.check(item >= ToontownBattleGlobals.MIN_LEVEL_INDEX and item <= ToontownBattleGlobals.MAX_LEVEL_INDEX, 'invalid gag item: %s' % item)

    def checkDeliveryItem(self, item):
        self.check(item in ItemDict, 'invalid delivery item: %s' % item)

    def checkNumItems(self, num):
        self.check(1, 'invalid num items: %s' % num)

    def checkRecoveryItem(self, item):
        self.check(item in ItemDict, 'invalid recovery item: %s' % item)

    def checkPercentChance(self, chance):
        self.check(chance > 0 and chance <= 100, 'invalid percent chance: %s' % chance)

    def checkRecoveryItemHolderAndType(self, holder, holderType = 'type'):
        holderTypes = ['type', 'level', 'track']
        self.check(holderType in holderTypes, 'invalid recovery item holderType: %s' % holderType)
        if holderType == 'type':
            holders = [Any, AnyFish] + SuitBattleGlobals.SuitAttributes.keys()
            self.check(holder in holders, 'invalid recovery item holder: %s for holderType: %s' % (holder, holderType))
        elif holderType == 'level':
            pass
        elif holderType == 'track':
            self.check(holder in self._cogTracks, 'invalid recovery item holder: %s for holderType: %s' % (holder, holderType))

    def checkNumFriends(self, num):
        self.check(1, 'invalid number of friends: %s' % num)

    def checkNumMinigames(self, num):
        self.check(1, 'invalid number of minigames: %s' % num)

    def filterFunc(avatar):
        return 1

    filterFunc = staticmethod(filterFunc)

    def __init__(self, id, quest):
        self.id = id
        self.quest = quest

    def getId(self):
        return self.id

    def getType(self):
        return self.__class__

    def getObjectiveStrings(self):
        return ['']

    def getString(self):
        return self.getObjectiveStrings()[0]

    def getRewardString(self, progressString):
        return self.getString() + ' : ' + progressString

    def getChooseString(self):
        return self.getString()

    def getPosterString(self):
        return self.getString()

    def getHeadlineString(self):
        return self.getString()

    def getDefaultQuestDialog(self):
        return self.getString() + TTLocalizer.Period

    def getNumQuestItems(self):
        return -1

    def addArticle(self, num, oString):
        if len(oString) == 0:
            return oString
        if num == 1:
            return oString
        else:
            return '%d %s' % (num, oString)

    def __repr__(self):
        return 'Quest type: %s id: %s params: %s' % (self.__class__.__name__, self.id, self.quest[0:])

    def doesCogCount(self, avId, cogDict, zoneId):
        return 0

    def doesFactoryCount(self, avId, location):
        return 0

    def doesMintCount(self, avId, location):
        return 0

    def doesCogPartCount(self, avId, location):
        return 0

    def getCompletionStatus(self, av, questDesc, npc = None):
        notify.error('Pure virtual - please override me')
        return None


class LocationBasedQuest(Quest):
    def __init__(self, id, quest):
        Quest.__init__(self, id, quest)
        self.checkLocation(self.quest[0])

    def getLocation(self):
        return self.quest[0]

    def getLocationName(self):
        loc = self.getLocation()
        if loc == Anywhere:
            locName = ''
        elif loc in ToontownGlobals.hoodNameMap:
            locName = TTLocalizer.QuestInLocationString % {'inPhrase': ToontownGlobals.hoodNameMap[loc][1],
             'location': ToontownGlobals.hoodNameMap[loc][-1] + TTLocalizer.QuestsLocationArticle}
        elif loc in ToontownGlobals.StreetBranchZones:
            locName = TTLocalizer.QuestInLocationString % {'inPhrase': ToontownGlobals.StreetNames[loc][1],
             'location': ToontownGlobals.StreetNames[loc][-1] + TTLocalizer.QuestsLocationArticle}
        return locName

    def isLocationMatch(self, zoneId):
        loc = self.getLocation()
        if loc is Anywhere:
            return 1
        if ZoneUtil.isPlayground(loc):
            if loc == ZoneUtil.getCanonicalHoodId(zoneId):
                return 1
            else:
                return 0
        elif loc == ZoneUtil.getCanonicalBranchZone(zoneId):
            return 1
        elif loc == zoneId:
            return 1
        else:
            return 0

    def getChooseString(self):
        return TTLocalizer.QuestsLocationString % {'string': self.getString(),
         'location': self.getLocationName()}

    def getPosterString(self):
        return TTLocalizer.QuestsLocationString % {'string': self.getString(),
         'location': self.getLocationName()}

    def getDefaultQuestDialog(self):
        return (TTLocalizer.QuestsLocationString + TTLocalizer.Period) % {'string': self.getString(),
         'location': self.getLocationName()}

class CogQuest(LocationBasedQuest):
    def __init__(self, id, quest):
        LocationBasedQuest.__init__(self, id, quest)
        if self.__class__ == CogQuest:
            self.checkNumCogs(self.quest[1])
            self.checkCogType(self.quest[2])

    def getCogType(self):
        return self.quest[2]

    def getNumQuestItems(self):
        return self.getNumCogs()

    def getNumCogs(self):
        return self.quest[1]

    def getCompletionStatus(self, av, questDesc, npc = None):
        questId, fromNpcId, toNpcId, rewardId, toonProgress = questDesc
        questComplete = toonProgress >= self.getNumCogs()
        return getCompleteStatusWithNpc(questComplete, toNpcId, npc)

    def getProgressString(self, avatar, questDesc):
        if self.getCompletionStatus(avatar, questDesc) == COMPLETE:
            return CompleteString
        elif self.getNumCogs() == 1:
            return ''
        else:
            return TTLocalizer.QuestsCogQuestProgress % {'progress': questDesc[4],
             'numCogs': self.getNumCogs()}

    def getCogNameString(self):
        numCogs = self.getNumCogs()
        cogType = self.getCogType()
        if numCogs == 1:
            if cogType == Any:
                return TTLocalizer.Cog
            else:
                return SuitBattleGlobals.SuitAttributes[cogType]['singularname']
        elif cogType == Any:
            return TTLocalizer.Cogs
        else:
            return SuitBattleGlobals.SuitAttributes[cogType]['pluralname']

    def getObjectiveStrings(self):
        cogName = self.getCogNameString()
        numCogs = self.getNumCogs()
        if numCogs == 1:
            text = cogName
        else:
            text = TTLocalizer.QuestsCogQuestDefeatDesc % {'numCogs': numCogs,
             'cogName': cogName}
        return (text,)

    def getString(self):
        return TTLocalizer.QuestsCogQuestDefeat % self.getObjectiveStrings()[0]

    def getSCStrings(self, toNpcId, progress):
        if progress >= self.getNumCogs():
            return getFinishToonTaskSCStrings(toNpcId)
        cogName = self.getCogNameString()
        numCogs = self.getNumCogs()
        if numCogs == 1:
            text = TTLocalizer.QuestsCogQuestSCStringS
        else:
            text = TTLocalizer.QuestsCogQuestSCStringP
        cogLoc = self.getLocationName()
        return text % {'cogName': cogName,
         'cogLoc': cogLoc}

    def getHeadlineString(self):
        cogType = self.getCogType()
        if cogType == Any:
            return TTLocalizer.QuestsGenericCogHeadline
        return TTLocalizer.CogName2Headline[cogType]

    def doesCogCount(self, avId, cogDict, zoneId):
        questCogType = self.getCogType()
        return (questCogType is Any or questCogType is cogDict['type']) and avId in cogDict['activeToons'] and self.isLocationMatch(zoneId)


class CogTrackQuest(CogQuest):
    trackCodes = ['c',
     'l',
     'm',
     's']
    trackNamesS = [TTLocalizer.BossbotS,
     TTLocalizer.LawbotS,
     TTLocalizer.CashbotS,
     TTLocalizer.SellbotS]
    trackNamesP = [TTLocalizer.BossbotP,
     TTLocalizer.LawbotP,
     TTLocalizer.CashbotP,
     TTLocalizer.SellbotP]

    def __init__(self, id, quest):
        CogQuest.__init__(self, id, quest)
        if self.__class__ == CogTrackQuest:
            self.checkNumCogs(self.quest[1])
            self.checkCogTrack(self.quest[2])

    def getCogTrack(self):
        return self.quest[2]

    def getProgressString(self, avatar, questDesc):
        if self.getCompletionStatus(avatar, questDesc) == COMPLETE:
            return CompleteString
        elif self.getNumCogs() == 1:
            return ''
        else:
            return TTLocalizer.QuestsCogTrackQuestProgress % {'progress': questDesc[4],
             'numCogs': self.getNumCogs()}

    def getObjectiveStrings(self):
        numCogs = self.getNumCogs()
        track = self.trackCodes.index(self.getCogTrack())
        if numCogs == 1:
            text = self.trackNamesS[track]
        else:
            text = TTLocalizer.QuestsCogTrackDefeatDesc % {'numCogs': numCogs,
             'trackName': self.trackNamesP[track]}
        return (text,)

    def getString(self):
        return TTLocalizer.QuestsCogTrackQuestDefeat % self.getObjectiveStrings()[0]

    def getSCStrings(self, toNpcId, progress):
        if progress >= self.getNumCogs():
            return getFinishToonTaskSCStrings(toNpcId)
        numCogs = self.getNumCogs()
        track = self.trackCodes.index(self.getCogTrack())
        if numCogs == 1:
            cogText = self.trackNamesS[track]
            text = TTLocalizer.QuestsCogTrackQuestSCStringS
        else:
            cogText = self.trackNamesP[track]
            text = TTLocalizer.QuestsCogTrackQuestSCStringP
        cogLocName = self.getLocationName()
        return text % {'cogText': cogText,
         'cogLoc': cogLocName}

    def getHeadlineString(self):
        return TTLocalizer.CogTrack2Headline[self.getCogTrack()]

    def doesCogCount(self, avId, cogDict, zoneId):
        questCogTrack = self.getCogTrack()
        return questCogTrack == cogDict['track'] and avId in cogDict['activeToons'] and self.isLocationMatch(zoneId)


class CogLevelQuest(CogQuest):
    def __init__(self, id, quest):
        CogQuest.__init__(self, id, quest)
        self.checkNumCogs(self.quest[1])
        self.checkCogLevel(self.quest[2])

    def getCogType(self):
        return Any

    def getCogLevel(self):
        return self.quest[2]

    def getProgressString(self, avatar, questDesc):
        if self.getCompletionStatus(avatar, questDesc) == COMPLETE:
            return CompleteString
        elif self.getNumCogs() == 1:
            return ''
        else:
            return TTLocalizer.QuestsCogLevelQuestProgress % {'progress': questDesc[4],
             'numCogs': self.getNumCogs()}

    def getObjectiveStrings(self):
        count = self.getNumCogs()
        level = self.getCogLevel()
        name = self.getCogNameString()
        if count == 1:
            text = TTLocalizer.QuestsCogLevelQuestDesc
        else:
            text = TTLocalizer.QuestsCogLevelQuestDescC
        return (text % {'count': count,
          'level': level,
          'name': name},)

    def getString(self):
        return TTLocalizer.QuestsCogLevelQuestDefeat % self.getObjectiveStrings()[0]

    def getSCStrings(self, toNpcId, progress):
        if progress >= self.getNumCogs():
            return getFinishToonTaskSCStrings(toNpcId)
        count = self.getNumCogs()
        level = self.getCogLevel()
        name = self.getCogNameString()
        if count == 1:
            text = TTLocalizer.QuestsCogLevelQuestDesc
        else:
            text = TTLocalizer.QuestsCogLevelQuestDescI
        objective = text % {'level': level,
         'name': name}
        location = self.getLocationName()
        return TTLocalizer.QuestsCogLevelQuestSCString % {'objective': objective,
         'location': location}

    def getHeadlineString(self):
        return TTLocalizer.QuestsGenericCogHeadline

    def doesCogCount(self, avId, cogDict, zoneId):
        questCogLevel = self.getCogLevel()
        return questCogLevel <= cogDict['level'] and avId in cogDict['activeToons'] and self.isLocationMatch(zoneId)


class SkelecogQBase:
    def getCogNameString(self):
        numCogs = self.getNumCogs()
        if numCogs == 1:
            return TTLocalizer.ASkeleton
        else:
            return TTLocalizer.SkeletonP

    def doesCogCount(self, avId, cogDict, zoneId):
        return cogDict['isSkelecog'] and avId in cogDict['activeToons'] and self.isLocationMatch(zoneId)


class SkelecogQuest(CogQuest, SkelecogQBase):
    def __init__(self, id, quest):
        CogQuest.__init__(self, id, quest)
        self.checkNumSkelecogs(self.quest[1])

    def getCogType(self):
        return Any

    def getCogNameString(self):
        return SkelecogQBase.getCogNameString(self)

    def doesCogCount(self, avId, cogDict, zoneId):
        return SkelecogQBase.doesCogCount(self, avId, cogDict, zoneId)

class SkelecogTrackQuest(CogTrackQuest, SkelecogQBase):
    trackNamesS = [TTLocalizer.BossbotSkelS,
     TTLocalizer.LawbotSkelS,
     TTLocalizer.CashbotSkelS,
     TTLocalizer.SellbotSkelS]
    trackNamesP = [TTLocalizer.BossbotSkelP,
     TTLocalizer.LawbotSkelP,
     TTLocalizer.CashbotSkelP,
     TTLocalizer.SellbotSkelP]

    def __init__(self, id, quest):
        CogTrackQuest.__init__(self, id, quest)
        self.checkNumSkelecogs(self.quest[1])
        self.checkSkelecogTrack(self.quest[2])

    def getCogNameString(self):
        return SkelecogQBase.getCogNameString(self)

    def doesCogCount(self, avId, cogDict, zoneId):
        return SkelecogQBase.doesCogCount(self, avId, cogDict, zoneId) and self.getCogTrack() == cogDict['track']


class SkelecogLevelQuest(CogLevelQuest, SkelecogQBase):
    def __init__(self, id, quest):
        CogLevelQuest.__init__(self, id, quest)
        self.checkNumSkelecogs(self.quest[1])
        self.checkSkelecogLevel(self.quest[2])

    def getCogType(self):
        return Any

    def getCogNameString(self):
        return SkelecogQBase.getCogNameString(self)

    def doesCogCount(self, avId, cogDict, zoneId):
        return SkelecogQBase.doesCogCount(self, avId, cogDict, zoneId) and self.getCogLevel() <= cogDict['level']


class SkeleReviveQBase:
    def getCogNameString(self):
        numCogs = self.getNumCogs()
        if numCogs == 1:
            return TTLocalizer.Av2Cog
        else:
            return TTLocalizer.v2CogP

    def doesCogCount(self, avId, cogDict, zoneId):
        return cogDict['hasRevives'] and avId in cogDict['activeToons'] and self.isLocationMatch(zoneId)


class SkeleReviveQuest(CogQuest, SkeleReviveQBase):
    def __init__(self, id, quest):
        CogQuest.__init__(self, id, quest)
        self.checkNumSkeleRevives(self.quest[1])

    def getCogType(self):
        return Any

    def getCogNameString(self):
        return SkeleReviveQBase.getCogNameString(self)

    def doesCogCount(self, avId, cogDict, zoneId):
        return SkeleReviveQBase.doesCogCount(self, avId, cogDict, zoneId)


class ForemanQuest(CogQuest):
    def __init__(self, id, quest):
        CogQuest.__init__(self, id, quest)
        self.checkNumForemen(self.quest[1])

    def getCogType(self):
        return Any

    def getCogNameString(self):
        numCogs = self.getNumCogs()
        if numCogs == 1:
            return TTLocalizer.AForeman
        else:
            return TTLocalizer.ForemanP

    def doesCogCount(self, avId, cogDict, zoneId):
        return bool(CogQuest.doesCogCount(self, avId, cogDict, zoneId) and cogDict['isForeman'])

BOSS_NAMES = {
 Anywhere: [TTLocalizer.ACogBoss, TTLocalizer.CogBosses, 'phase_3.5/maps/boss_icon.jpg', 'blue'],
 ToontownGlobals.SellbotHQ: [TTLocalizer.ACogVP, TTLocalizer.CogVPs, 'phase_3.5/maps/vp_icon.jpg', 'red'],
 ToontownGlobals.CashbotHQ: [TTLocalizer.ACogCFO, TTLocalizer.CogCFOs, 'phase_3.5/maps/cfo_icon.jpg', 'green'],
 ToontownGlobals.LawbotHQ: [TTLocalizer.ACogCJ, TTLocalizer.CogCJs, 'phase_3.5/maps/cj_icon.jpg', 'blue'],
 ToontownGlobals.BossbotHQ: [TTLocalizer.ACogCEO, TTLocalizer.CogCEOs, 'phase_3.5/maps/ceo_icon.jpg', 'brown']
}

class TexturedQuest:
    def getModelFromTexture(self, texture):
        cardMaker = CardMaker('cm-%s' % time.time())
        cardMaker.setFrame(-0.5, 0.5, -0.5, 0.5)
        node = NodePath(cardMaker.generate())

        node.setTexture(loader.loadTexture(texture))
        return node

    def hasFrame(self):
        return True

    def getFrame(self):
        print 'getFrame from TexturedQuest not implemented!'
        return [None, None]

class BossQuest(CogQuest, TexturedQuest):
    def __init__(self, id, quest):
        CogQuest.__init__(self, id, quest)
        self.checkNumBosses(self.quest[1])

    def getFrame(self):
        boss = BOSS_NAMES[self.quest[0]]

        return [self.getModelFromTexture(boss[2]), boss[3]]

    def getCogType(self):
        return Any

    def getCogNameString(self):
        return BOSS_NAMES[self.quest[0]][self.getNumCogs() > 1]

    def doesCogCount(self, avId, cogDict, zoneId):
        return cogDict['isBoss'] > 0 and self.isLocationMatch(zoneId)

class SupervisorQuest(CogQuest):
    def __init__(self, id, quest):
        CogQuest.__init__(self, id, quest)
        self.checkNumSupervisors(self.quest[1])

    def getCogType(self):
        return Any

    def getCogNameString(self):
        numCogs = self.getNumCogs()
        if numCogs == 1:
            return TTLocalizer.ASupervisor
        else:
            return TTLocalizer.SupervisorP

    def doesCogCount(self, avId, cogDict, zoneId):
        return bool(CogQuest.doesCogCount(self, avId, cogDict, zoneId) and cogDict['isSupervisor'])

class RescueQuest(LocationBasedQuest):
    def __init__(self, id, quest):
        Quest.__init__(self, id, quest)
        self.checkNumCogs(self.quest[1])

    def getNumToons(self):
        return self.quest[1]

    def getNumQuestItems(self):
        return self.getNumToons()

    def getLocationName(self):
        return ' ' + TTLocalizer.InVP if self.quest[0] == InVP else TTLocalizer.InFieldOffice

    def getCompletionStatus(self, av, questDesc, npc = None):
        questId, fromNpcId, toNpcId, rewardId, toonProgress = questDesc
        questComplete = toonProgress >= self.getNumToons()
        return getCompleteStatusWithNpc(questComplete, toNpcId, npc)

    def getProgressString(self, avatar, questDesc):
        if self.getCompletionStatus(avatar, questDesc) == COMPLETE:
            return CompleteString
        elif self.getNumToons() == 1:
            return ''
        else:
            return TTLocalizer.QuestsRescueQuestProgress % {'progress': questDesc[4],
             'numToons': self.getNumToons()}

    def getObjectiveStrings(self):
        numToons = self.getNumToons()
        if numToons == 1:
            text = TTLocalizer.QuestsRescueQuestToonS
        else:
            text = TTLocalizer.QuestsRescueQuestRescueDesc % {'numToons': numToons}
        return (text,)

    def getString(self):
        return TTLocalizer.QuestsRescueQuestRescue % self.getObjectiveStrings()[0]

    def getSCStrings(self, toNpcId, progress):
        numToons = self.getNumToons()
        if progress >= numToons:
            return getFinishToonTaskSCStrings(toNpcId)
        if numToons == 1:
            text = TTLocalizer.QuestsRescueQuestSCStringS
        else:
            text = TTLocalizer.QuestsRescueQuestSCStringP
        return text % {'toonLoc': self.getLocationName().strip()}

    def getHeadlineString(self):
        return TTLocalizer.QuestsRescueQuestHeadline

    def isMethodMatch(self, method):
        return self.quest[0] == method

BUILDING_NAMES = {
 Any: ['phase_3.5/maps/cogdo_icon.jpg', 'brown'],
 'l': ['phase_3.5/maps/lawbot_cogdo_icon.jpg', 'blue'],
 's': ['phase_3.5/maps/sellbot_cogdo_icon.jpg', 'red']
}

class BuildingQuest(CogQuest, TexturedQuest):
    trackCodes = ['c',
     'l',
     'm',
     's']
    trackNames = [TTLocalizer.Bossbot,
     TTLocalizer.Lawbot,
     TTLocalizer.Cashbot,
     TTLocalizer.Sellbot]

    def __init__(self, id, quest):
        CogQuest.__init__(self, id, quest)
        self.checkNumBuildings(self.quest[1])
        self.checkBuildingTrack(self.quest[2])
        self.checkBuildingFloors(self.quest[3])
        self.checkBuildingType(self.quest[4])

    def hasFrame(self):
        return self.isCogdo()

    def getFrame(self):
        building = BUILDING_NAMES[self.quest[2]]

        return [self.getModelFromTexture(building[0]), building[1]]

    def getNumFloors(self):
        return self.quest[3]

    def getBuildingTrack(self):
        return self.quest[2]

    def isCogdo(self):
        return self.quest[4]

    def getNumQuestItems(self):
        return self.getNumBuildings()

    def getNumBuildings(self):
        return self.quest[1]

    def getCompletionStatus(self, av, questDesc, npc = None):
        questId, fromNpcId, toNpcId, rewardId, toonProgress = questDesc
        questComplete = toonProgress >= self.getNumBuildings()
        return getCompleteStatusWithNpc(questComplete, toNpcId, npc)

    def getProgressString(self, avatar, questDesc):
        if self.getCompletionStatus(avatar, questDesc) == COMPLETE:
            return CompleteString
        elif self.getNumBuildings() == 1:
            return ''
        else:
            return TTLocalizer.QuestsBuildingQuestProgressString % {'progress': questDesc[4],
             'num': self.getNumBuildings()}

    def getObjectiveStrings(self):
        count = self.getNumBuildings()
        buildingTrack = self.getBuildingTrack()
        if buildingTrack == Any:
            type = TTLocalizer.Cog
        else:
            type = self.trackNames[self.trackCodes.index(buildingTrack)]
        floors = ''

        if self.isCogdo():
            if buildingTrack == Any:
                text = TTLocalizer.QuestsCogdoQuestDescU if count == 1 else TTLocalizer.QuestsCogdoQuestDescUM
            else:
                text = TTLocalizer.QuestsCogdoQuestDesc if count == 1 else TTLocalizer.QuestsCogdoQuestDescM
        else:
            floors = TTLocalizer.QuestsBuildingQuestFloorNumbers[self.getNumFloors() - 1]

            if count == 1:
                text = TTLocalizer.QuestsBuildingQuestDesc if floors == '' else TTLocalizer.QuestsBuildingQuestDescF
            else:
                text = TTLocalizer.QuestsBuildingQuestDescC if floors == '' else TTLocalizer.QuestsBuildingQuestDescCF

        return (text % {'count': count,
          'floors': floors,
          'type': type},)

    def getString(self):
        return TTLocalizer.QuestsBuildingQuestString % self.getObjectiveStrings()[0]

    def getSCStrings(self, toNpcId, progress):
        if progress >= self.getNumBuildings():
            return getFinishToonTaskSCStrings(toNpcId)
        count = self.getNumBuildings()
        buildingTrack = self.getBuildingTrack()
        floors = ''

        if buildingTrack == Any:
            type = TTLocalizer.Cog
        else:
            type = self.trackNames[self.trackCodes.index(buildingTrack)]

        if self.isCogdo():
            if buildingTrack == Any:
                text = TTLocalizer.QuestsCogdoQuestDescU if count == 1 else TTLocalizer.QuestsCogdoQuestDescMI
            else:
                text = TTLocalizer.QuestsCogdoQuestDesc if count == 1 else TTLocalizer.QuestsCogdoQuestDescMUI
        else:
            floors = TTLocalizer.QuestsBuildingQuestFloorNumbers[self.getNumFloors() - 1]

            if count == 1:
                text = TTLocalizer.QuestsBuildingQuestDesc if floors == '' else TTLocalizer.QuestsBuildingQuestDescF
            else:
                text = TTLocalizer.QuestsBuildingQuestDescI if floors == '' else TTLocalizer.QuestsBuildingQuestDescIF
        objective = text % {'floors': floors,
         'type': type}
        return TTLocalizer.QuestsBuildingQuestSCString % {'objective': objective,
         'location': self.getLocationName()}

    def getHeadlineString(self):
        return TTLocalizer.QuestsBuildingQuestHeadline

    def doesCogCount(self, avId, cogDict, zoneId):
        return 0

    def doesBuildingTypeCount(self, type):
        buildingTrack = self.getBuildingTrack()
        if buildingTrack == Any or buildingTrack == type:
            return True
        return False

class FactoryQuest(LocationBasedQuest):
    factoryTypeNames = {FT_FullSuit: TTLocalizer.Cog,
     FT_Leg: TTLocalizer.FactoryTypeLeg,
     FT_Arm: TTLocalizer.FactoryTypeArm,
     FT_Torso: TTLocalizer.FactoryTypeTorso}

    def __init__(self, id, quest):
        LocationBasedQuest.__init__(self, id, quest)
        self.checkNumFactories(self.quest[1])

    def getNumQuestItems(self):
        return self.getNumFactories()

    def getNumFactories(self):
        return self.quest[1]

    def getFactoryType(self):
        loc = self.getLocation()
        type = Any
        if loc in ToontownGlobals.factoryId2factoryType:
            type = ToontownGlobals.factoryId2factoryType[loc]
        return type

    def getCompletionStatus(self, av, questDesc, npc = None):
        questId, fromNpcId, toNpcId, rewardId, toonProgress = questDesc
        questComplete = toonProgress >= self.getNumFactories()
        return getCompleteStatusWithNpc(questComplete, toNpcId, npc)

    def getProgressString(self, avatar, questDesc):
        if self.getCompletionStatus(avatar, questDesc) == COMPLETE:
            return CompleteString
        elif self.getNumFactories() == 1:
            return ''
        else:
            return TTLocalizer.QuestsFactoryQuestProgressString % {'progress': questDesc[4],
             'num': self.getNumFactories()}

    def getObjectiveStrings(self):
        count = self.getNumFactories()
        factoryType = self.getFactoryType()
        if factoryType == Any:
            type = TTLocalizer.Cog
        else:
            type = FactoryQuest.factoryTypeNames[factoryType]
        if count == 1:
            text = TTLocalizer.QuestsFactoryQuestDesc
        else:
            text = TTLocalizer.QuestsFactoryQuestDescC
        return (text % {'count': count,
          'type': type},)

    def getString(self):
        return TTLocalizer.QuestsFactoryQuestString % self.getObjectiveStrings()[0]

    def getSCStrings(self, toNpcId, progress):
        if progress >= self.getNumFactories():
            return getFinishToonTaskSCStrings(toNpcId)
        factoryType = self.getFactoryType()
        if factoryType == Any:
            type = TTLocalizer.Cog
        else:
            type = FactoryQuest.factoryTypeNames[factoryType]
        count = self.getNumFactories()
        if count == 1:
            text = TTLocalizer.QuestsFactoryQuestDesc
        else:
            text = TTLocalizer.QuestsFactoryQuestDescI
        objective = text % {'type': type}
        location = self.getLocationName()
        return TTLocalizer.QuestsFactoryQuestSCString % {'objective': objective,
         'location': location}

    def getHeadlineString(self):
        return TTLocalizer.QuestsFactoryQuestHeadline

    def doesFactoryCount(self, avId, location):
        return self.isLocationMatch(location)

class MintQuest(LocationBasedQuest):
    def __init__(self, id, quest):
        LocationBasedQuest.__init__(self, id, quest)
        self.checkNumMints(self.quest[1])

    def getNumQuestItems(self):
        return self.getNumMints()

    def getNumMints(self):
        return self.quest[1]

    def getCompletionStatus(self, av, questDesc, npc = None):
        questId, fromNpcId, toNpcId, rewardId, toonProgress = questDesc
        questComplete = toonProgress >= self.getNumMints()
        return getCompleteStatusWithNpc(questComplete, toNpcId, npc)

    def getProgressString(self, avatar, questDesc):
        if self.getCompletionStatus(avatar, questDesc) == COMPLETE:
            return CompleteString
        elif self.getNumMints() == 1:
            return ''
        else:
            return TTLocalizer.QuestsMintQuestProgressString % {'progress': questDesc[4],
             'num': self.getNumMints()}

    def getObjectiveStrings(self):
        count = self.getNumMints()
        if count == 1:
            text = TTLocalizer.QuestsMintQuestDesc
        else:
            text = TTLocalizer.QuestsMintQuestDescC % {'count': count}
        return (text,)

    def getString(self):
        return TTLocalizer.QuestsMintQuestString % self.getObjectiveStrings()[0]

    def getSCStrings(self, toNpcId, progress):
        if progress >= self.getNumMints():
            return getFinishToonTaskSCStrings(toNpcId)
        count = self.getNumMints()
        if count == 1:
            objective = TTLocalizer.QuestsMintQuestDesc
        else:
            objective = TTLocalizer.QuestsMintQuestDescI
        location = self.getLocationName()
        return TTLocalizer.QuestsMintQuestSCString % {'objective': objective,
         'location': location}

    def getHeadlineString(self):
        return TTLocalizer.QuestsMintQuestHeadline

    def doesMintCount(self, avId, location):
        return self.isLocationMatch(location)

class CogPartQuest(LocationBasedQuest):
    def __init__(self, id, quest):
        LocationBasedQuest.__init__(self, id, quest)
        self.checkNumCogParts(self.quest[1])

    def getNumQuestItems(self):
        return self.getNumParts()

    def getNumParts(self):
        return self.quest[1]

    def getCompletionStatus(self, av, questDesc, npc = None):
        questId, fromNpcId, toNpcId, rewardId, toonProgress = questDesc
        questComplete = toonProgress >= self.getNumParts()
        return getCompleteStatusWithNpc(questComplete, toNpcId, npc)

    def getProgressString(self, avatar, questDesc):
        if self.getCompletionStatus(avatar, questDesc) == COMPLETE:
            return CompleteString
        elif self.getNumParts() == 1:
            return ''
        else:
            return TTLocalizer.QuestsCogPartQuestProgressString % {'progress': questDesc[4],
             'num': self.getNumParts()}

    def getObjectiveStrings(self):
        count = self.getNumParts()
        if count == 1:
            text = TTLocalizer.QuestsCogPartQuestDesc
        else:
            text = TTLocalizer.QuestsCogPartQuestDescC
        return (text % {'count': count},)

    def getString(self):
        return TTLocalizer.QuestsCogPartQuestString % self.getObjectiveStrings()[0]

    def getSCStrings(self, toNpcId, progress):
        if progress >= self.getNumParts():
            return getFinishToonTaskSCStrings(toNpcId)
        count = self.getNumParts()
        if count == 1:
            text = TTLocalizer.QuestsCogPartQuestDesc
        else:
            text = TTLocalizer.QuestsCogPartQuestDescI
        objective = text
        location = self.getLocationName()
        return TTLocalizer.QuestsCogPartQuestSCString % {'objective': objective,
         'location': location}

    def getHeadlineString(self):
        return TTLocalizer.QuestsCogPartQuestHeadline

    def doesCogPartCount(self, avId, location):
        return self.isLocationMatch(location)

class DeliverGagQuest(Quest):
    def __init__(self, id, quest):
        Quest.__init__(self, id, quest)
        self.checkNumGags(self.quest[0])
        self.checkGagTrack(self.quest[1])
        self.checkGagItem(self.quest[2])

    def getGagType(self):
        return (self.quest[1], self.quest[2])

    def getNumQuestItems(self):
        return self.getNumGags()

    def getNumGags(self):
        return self.quest[0]

    def getCompletionStatus(self, av, questDesc, npc = None):
        questId, fromNpcId, toNpcId, rewardId, toonProgress = questDesc
        gag = self.getGagType()
        num = self.getNumGags()
        track = gag[0]
        level = gag[1]
        questComplete = npc and av.inventory and av.inventory.numItem(track, level) >= num
        return getCompleteStatusWithNpc(questComplete, toNpcId, npc)

    def getProgressString(self, avatar, questDesc):
        if self.getCompletionStatus(avatar, questDesc) == COMPLETE:
            return CompleteString
        elif self.getNumGags() == 1:
            return ''
        else:
            return TTLocalizer.QuestsDeliverGagQuestProgress % {'progress': questDesc[4],
             'numGags': self.getNumGags()}

    def getObjectiveStrings(self):
        track, item = self.getGagType()
        num = self.getNumGags()
        if num == 1:
            text = ToontownBattleGlobals.AvPropStringsSingular[track][item]
        else:
            gagName = ToontownBattleGlobals.AvPropStringsPlural[track][item]
            text = TTLocalizer.QuestsItemNameAndNum % {'num': TTLocalizer.getLocalNum(num),
             'name': gagName}
        return (text,)

    def getString(self):
        return TTLocalizer.QuestsDeliverGagQuestString % self.getObjectiveStrings()[0]

    def getRewardString(self, progress):
        return TTLocalizer.QuestsDeliverGagQuestStringLong % self.getObjectiveStrings()[0]

    def getDefaultQuestDialog(self):
        return TTLocalizer.QuestsDeliverGagQuestStringLong % self.getObjectiveStrings()[0] + '\x07' + TTLocalizer.QuestsDeliverGagQuestInstructions

    def getSCStrings(self, toNpcId, progress):
        if progress >= self.getNumGags():
            return getFinishToonTaskSCStrings(toNpcId)
        track, item = self.getGagType()
        num = self.getNumGags()
        if num == 1:
            text = TTLocalizer.QuestsDeliverGagQuestToSCStringS
            gagName = ToontownBattleGlobals.AvPropStringsSingular[track][item]
        else:
            text = TTLocalizer.QuestsDeliverGagQuestToSCStringP
            gagName = ToontownBattleGlobals.AvPropStringsPlural[track][item]
        return [text % {'gagName': gagName}, TTLocalizer.QuestsDeliverGagQuestSCString] + getVisitSCStrings(toNpcId)

    def getHeadlineString(self):
        return TTLocalizer.QuestsDeliverGagQuestHeadline

    def removeGags(self, av):
        gag = self.getGagType()
        inventory = av.inventory
        takenGags = 0
        for i in xrange(self.getNumGags()):
            if inventory.useItem(gag[0], gag[1]):
                takenGags += 1
        av.b_setInventory(inventory.makeNetString())
        return takenGags

class DeliverItemQuest(Quest):
    def __init__(self, id, quest):
        Quest.__init__(self, id, quest)
        self.checkDeliveryItem(self.quest[0])

    def getItem(self):
        return self.quest[0]

    def getCompletionStatus(self, av, questDesc, npc = None):
        questId, fromNpcId, toNpcId, rewardId, toonProgress = questDesc
        if npc and npcMatches(toNpcId, npc):
            return COMPLETE
        else:
            return INCOMPLETE_WRONG_NPC

    def getProgressString(self, avatar, questDesc):
        return TTLocalizer.QuestsDeliverItemQuestProgress

    def getObjectiveStrings(self):
        iDict = ItemDict[self.getItem()]
        article = iDict[2]
        itemName = iDict[0]
        return [article + itemName]

    def getString(self):
        return TTLocalizer.QuestsDeliverItemQuestString % self.getObjectiveStrings()[0]

    def getRewardString(self, progress):
        return TTLocalizer.QuestsDeliverItemQuestStringLong % self.getObjectiveStrings()[0]

    def getDefaultQuestDialog(self):
        return TTLocalizer.QuestsDeliverItemQuestStringLong % self.getObjectiveStrings()[0]

    def getSCStrings(self, toNpcId, progress):
        iDict = ItemDict[self.getItem()]
        article = iDict[2]
        itemName = iDict[0]
        return [TTLocalizer.QuestsDeliverItemQuestSCString % {'article': article,
          'itemName': itemName}] + getVisitSCStrings(toNpcId)

    def getHeadlineString(self):
        return TTLocalizer.QuestsDeliverItemQuestHeadline


class VisitQuest(Quest):
    def __init__(self, id, quest):
        Quest.__init__(self, id, quest)

    def getCompletionStatus(self, av, questDesc, npc = None):
        questId, fromNpcId, toNpcId, rewardId, toonProgress = questDesc
        if npc and npcMatches(toNpcId, npc):
            return COMPLETE
        else:
            return INCOMPLETE_WRONG_NPC

    def getProgressString(self, avatar, questDesc):
        return TTLocalizer.QuestsVisitQuestProgress

    def getObjectiveStrings(self):
        return ['']

    def getString(self):
        return TTLocalizer.QuestsVisitQuestStringShort

    def getChooseString(self):
        return TTLocalizer.QuestsVisitQuestStringLong

    def getRewardString(self, progress):
        return TTLocalizer.QuestsVisitQuestStringLong

    def getDefaultQuestDialog(self):
        return random.choice(DefaultVisitQuestDialog)

    def getSCStrings(self, toNpcId, progress):
        return getVisitSCStrings(toNpcId)

    def getHeadlineString(self):
        return TTLocalizer.QuestsVisitQuestHeadline
        
class TrackChoiceQuest(Quest):
    def __init__(self, id, quest):
        Quest.__init__(self, id, quest)
        
    def getCompletionStatus(self, av, questDesc, npc = None):
        questId, fromNpcId, toNpcId, rewardId, toonProgress = questDesc
        if npc and npcMatches(toNpcId, npc):
            return COMPLETE
        else:
            return INCOMPLETE_WRONG_NPC
            
    def getString(self):
        return TTLocalizer.QuestsTrackChoiceQuestString

    def getProgressString(self, avatar, questDesc):
        if self.getCompletionStatus(avatar, questDesc) == COMPLETE:
            return CompleteString
        else:
            return NotChosenString
           
    def getSCStrings(self, toNpcId, progress):
        return [TTLocalizer.QuestsTrackChoiceQuestSCString] + getVisitSCStrings(toNpcId)
            
    def getHeadlineString(self):
        return TTLocalizer.QuestsTrackChoiceQuestHeadline

class RecoverItemQuest(LocationBasedQuest):
    def __init__(self, id, quest):
        LocationBasedQuest.__init__(self, id, quest)
        self.checkNumItems(self.quest[1])
        self.checkRecoveryItem(self.quest[2])
        self.checkPercentChance(self.quest[3])
        if len(self.quest) > 5:
            self.checkRecoveryItemHolderAndType(self.quest[4], self.quest[5])
        else:
            self.checkRecoveryItemHolderAndType(self.quest[4])

    def testRecover(self, progress):
        test = random.random() * 100
        chance = self.getPercentChance()
        numberDone = progress & pow(2, 16) - 1
        numberNotDone = progress >> 16
        returnTest = None
        avgNum2Kill = 1.0 / (chance / 100.0)
        if numberNotDone >= avgNum2Kill * 1.5:
            chance = 100
        elif numberNotDone > avgNum2Kill * 0.5:
            diff = float(numberNotDone - avgNum2Kill * 0.5)
            luck = 1.0 + abs(diff / (avgNum2Kill * 0.5))
            chance *= luck
        if test <= chance:
            returnTest = 1
            numberNotDone = 0
            numberDone += 1
        else:
            returnTest = 0
            numberNotDone += 1
            numberDone += 0
        returnCount = numberNotDone << 16
        returnCount += numberDone
        return (returnTest, returnCount)

    def testDone(self, progress):
        numberDone = progress & pow(2, 16) - 1
        print 'Quest number done %s' % numberDone
        if numberDone >= self.getNumItems():
            return 1
        else:
            return 0

    def getNumQuestItems(self):
        return self.getNumItems()

    def getNumItems(self):
        return self.quest[1]

    def getItem(self):
        return self.quest[2]

    def getPercentChance(self):
        return self.quest[3]

    def getHolder(self):
        return self.quest[4]

    def getHolderType(self):
        if len(self.quest) == 5:
            return 'type'
        else:
            return self.quest[5]

    def getCompletionStatus(self, av, questDesc, npc = None):
        questId, fromNpcId, toNpcId, rewardId, toonProgress = questDesc
        forwardProgress = toonProgress & pow(2, 16) - 1
        questComplete = forwardProgress >= self.getNumItems()
        return getCompleteStatusWithNpc(questComplete, toNpcId, npc)

    def getProgressString(self, avatar, questDesc):
        if self.getCompletionStatus(avatar, questDesc) == COMPLETE:
            return CompleteString
        elif self.getNumItems() == 1:
            return ''
        else:
            progress = questDesc[4] & pow(2, 16) - 1
            return TTLocalizer.QuestsRecoverItemQuestProgress % {'progress': progress,
             'numItems': self.getNumItems()}

    def getObjectiveStrings(self):
        holder = self.getHolder()
        holderType = self.getHolderType()
        if holder == Any:
            holderName = TTLocalizer.TheCogs
        elif holder == AnyFish:
            holderName = TTLocalizer.AFish
        elif holderType == 'type':
            holderName = SuitBattleGlobals.SuitAttributes[holder]['pluralname']
        elif holderType == 'level':
            holderName = TTLocalizer.QuestsRecoverItemQuestHolderString % {'level': TTLocalizer.Level,
             'holder': holder,
             'cogs': TTLocalizer.Cogs}
        elif holderType == 'track':
            if holder == 'c':
                holderName = TTLocalizer.BossbotP
            elif holder == 's':
                holderName = TTLocalizer.SellbotP
            elif holder == 'm':
                holderName = TTLocalizer.CashbotP
            elif holder == 'l':
                holderName = TTLocalizer.LawbotP
        item = self.getItem()
        num = self.getNumItems()
        if num == 1:
            itemName = ItemDict[item][2] + ItemDict[item][0]
        else:
            itemName = TTLocalizer.QuestsItemNameAndNum % {'num': TTLocalizer.getLocalNum(num),
             'name': ItemDict[item][1]}
        return [itemName, holderName]

    def getString(self):
        return TTLocalizer.QuestsRecoverItemQuestString % {'item': self.getObjectiveStrings()[0],
         'holder': self.getObjectiveStrings()[1]}

    def getSCStrings(self, toNpcId, progress):
        item = self.getItem()
        num = self.getNumItems()
        forwardProgress = progress & pow(2, 16) - 1
        if forwardProgress >= self.getNumItems():
            if num == 1:
                itemName = ItemDict[item][2] + ItemDict[item][0]
            else:
                itemName = TTLocalizer.QuestsItemNameAndNum % {'num': TTLocalizer.getLocalNum(num),
                 'name': ItemDict[item][1]}
            if toNpcId == ToonHQ:
                strings = [TTLocalizer.QuestsRecoverItemQuestReturnToHQSCString % itemName, TTLocalizer.QuestsRecoverItemQuestGoToHQSCString]
            elif toNpcId:
                npcName, hoodName, buildingArticle, buildingName, toStreet, streetName, isInPlayground = getNpcInfo(toNpcId)
                strings = [TTLocalizer.QuestsRecoverItemQuestReturnToSCString % {'item': itemName,
                  'npcName': npcName}]
                if isInPlayground:
                    strings.append(TTLocalizer.QuestsRecoverItemQuestGoToPlaygroundSCString % hoodName)
                else:
                    strings.append(TTLocalizer.QuestsRecoverItemQuestGoToStreetSCString % {'to': toStreet,
                     'street': streetName,
                     'hood': hoodName})
                strings.extend([TTLocalizer.QuestsRecoverItemQuestVisitBuildingSCString % (buildingArticle, buildingName), TTLocalizer.QuestsRecoverItemQuestWhereIsBuildingSCString % (buildingArticle, buildingName)])
            return strings
        holder = self.getHolder()
        holderType = self.getHolderType()
        locName = self.getLocationName()
        if holder == Any:
            holderName = TTLocalizer.TheCogs
        elif holder == AnyFish:
            holderName = TTLocalizer.TheFish
        elif holderType == 'type':
            holderName = SuitBattleGlobals.SuitAttributes[holder]['pluralname']
        elif holderType == 'level':
            holderName = TTLocalizer.QuestsRecoverItemQuestHolderString % {'level': TTLocalizer.Level,
             'holder': holder,
             'cogs': TTLocalizer.Cogs}
        elif holderType == 'track':
            if holder == 'c':
                holderName = TTLocalizer.BossbotP
            elif holder == 's':
                holderName = TTLocalizer.SellbotP
            elif holder == 'm':
                holderName = TTLocalizer.CashbotP
            elif holder == 'l':
                holderName = TTLocalizer.LawbotP
        if num == 1:
            itemName = ItemDict[item][2] + ItemDict[item][0]
        else:
            itemName = TTLocalizer.QuestsItemNameAndNum % {'num': TTLocalizer.getLocalNum(num),
             'name': ItemDict[item][1]}
        return TTLocalizer.QuestsRecoverItemQuestRecoverFromSCString % {'item': itemName,
         'holder': holderName,
         'loc': locName}

    def getHeadlineString(self):
        return TTLocalizer.QuestsRecoverItemQuestHeadline

    def doesCogCount(self, avId, cogDict, zoneId):
        questCogType = self.getHolder()
        return (questCogType is Any or questCogType is cogDict[self.getHolderType()]) and avId in cogDict['activeToons'] and self.isLocationMatch(zoneId)

class FriendQuest(Quest):
    def filterFunc(avatar):
        if len(avatar.getFriendsList()) == 0:
            return 1
        else:
            return 0

    filterFunc = staticmethod(filterFunc)

    def __init__(self, id, quest):
        Quest.__init__(self, id, quest)

    def getCompletionStatus(self, av, questDesc, npc = None):
        questId, fromNpcId, toNpcId, rewardId, toonProgress = questDesc
        questComplete = toonProgress >= 1 or len(av.getFriendsList()) > 0
        return getCompleteStatusWithNpc(questComplete, toNpcId, npc)

    def getProgressString(self, avatar, questDesc):
        if self.getCompletionStatus(avatar, questDesc) == COMPLETE:
            return CompleteString
        else:
            return ''

    def getString(self):
        return TTLocalizer.QuestsFriendQuestString

    def getSCStrings(self, toNpcId, progress):
        if progress:
            return getFinishToonTaskSCStrings(toNpcId)
        return TTLocalizer.QuestsFriendQuestSCString

    def getHeadlineString(self):
        return TTLocalizer.QuestsFriendQuestHeadline

    def getObjectiveStrings(self):
        return [TTLocalizer.QuestsFriendQuestString]

class TrolleyQuest(Quest):
    def __init__(self, id, quest):
        Quest.__init__(self, id, quest)

    def getCompletionStatus(self, av, questDesc, npc = None):
        questId, fromNpcId, toNpcId, rewardId, toonProgress = questDesc
        questComplete = toonProgress >= 1
        return getCompleteStatusWithNpc(questComplete, toNpcId, npc)

    def getProgressString(self, avatar, questDesc):
        if self.getCompletionStatus(avatar, questDesc) == COMPLETE:
            return CompleteString
        else:
            return ''

    def getString(self):
        return TTLocalizer.QuestsFriendQuestString

    def getSCStrings(self, toNpcId, progress):
        if progress:
            return getFinishToonTaskSCStrings(toNpcId)
        return TTLocalizer.QuestsTrolleyQuestSCString

    def getHeadlineString(self):
        return TTLocalizer.QuestsTrolleyQuestHeadline

    def getObjectiveStrings(self):
        return [TTLocalizer.QuestsTrolleyQuestString]


class MailboxQuest(Quest):
    def __init__(self, id, quest):
        Quest.__init__(self, id, quest)

    def getCompletionStatus(self, av, questDesc, npc = None):
        questId, fromNpcId, toNpcId, rewardId, toonProgress = questDesc
        questComplete = toonProgress >= 1
        return getCompleteStatusWithNpc(questComplete, toNpcId, npc)

    def getProgressString(self, avatar, questDesc):
        if self.getCompletionStatus(avatar, questDesc) == COMPLETE:
            return CompleteString
        else:
            return ''

    def getString(self):
        return TTLocalizer.QuestsMailboxQuestString

    def getSCStrings(self, toNpcId, progress):
        if progress:
            return getFinishToonTaskSCStrings(toNpcId)
        return TTLocalizer.QuestsMailboxQuestSCString

    def getHeadlineString(self):
        return TTLocalizer.QuestsMailboxQuestHeadline

    def getObjectiveStrings(self):
        return [TTLocalizer.QuestsMailboxQuestString]


class PhoneQuest(Quest):
    def __init__(self, id, quest):
        Quest.__init__(self, id, quest)

    def getCompletionStatus(self, av, questDesc, npc = None):
        questId, fromNpcId, toNpcId, rewardId, toonProgress = questDesc
        questComplete = toonProgress >= 1
        return getCompleteStatusWithNpc(questComplete, toNpcId, npc)

    def getProgressString(self, avatar, questDesc):
        if self.getCompletionStatus(avatar, questDesc) == COMPLETE:
            return CompleteString
        else:
            return ''

    def getString(self):
        return TTLocalizer.QuestsPhoneQuestString

    def getSCStrings(self, toNpcId, progress):
        if progress:
            return getFinishToonTaskSCStrings(toNpcId)
        return TTLocalizer.QuestsPhoneQuestSCString

    def getHeadlineString(self):
        return TTLocalizer.QuestsPhoneQuestHeadline

    def getObjectiveStrings(self):
        return [TTLocalizer.QuestsPhoneQuestString]
    

DefaultDialog = {GREETING: DefaultGreeting,
 QUEST: DefaultQuest,
 INCOMPLETE: DefaultIncomplete,
 INCOMPLETE_PROGRESS: DefaultIncompleteProgress,
 INCOMPLETE_WRONG_NPC: DefaultIncompleteWrongNPC,
 COMPLETE: DefaultComplete,
 LEAVING: DefaultLeaving}

def getQuestFromNpcId(id):
    return QuestDict.get(id)[QuestDictFromNpcIndex]


def getQuestToNpcId(id):
    return QuestDict.get(id)[QuestDictToNpcIndex]

def getQuestDialog(id):
    return QuestDict.get(id)[QuestDictDialogIndex]


def getQuestReward(id, av):
    baseRewardId = QuestDict.get(id)[QuestDictRewardIndex]
    return transformReward(baseRewardId, av)


def isQuestJustForFun(questId, rewardId):
    questEntry = QuestDict.get(questId)
    if questEntry:
        tier = questEntry[QuestDictTierIndex]
        return isRewardOptional(tier, rewardId)
    else:
        return False

NoRewardTierZeroQuests = (101, 110, 120, 121, 130, 131, 140, 141, 142, 145, 150, 160, 161, 162, 163)
RewardTierZeroQuests = ()
PreClarabelleQuestIds = NoRewardTierZeroQuests + RewardTierZeroQuests
QuestDict = {
}

Tier2QuestsDict = {}

for questId, questDesc in QuestDict.items():
    if questDesc[QuestDictStartIndex] == Start:
        tier = questDesc[QuestDictTierIndex]
        if tier in Tier2QuestsDict:
            Tier2QuestsDict[tier].append(questId)
        else:
            Tier2QuestsDict[tier] = [questId]

Quest2RewardDict = {}
Tier2Reward2QuestsDict = {}
Quest2RemainingStepsDict = {}

def getAllRewardIdsForReward(rewardId):
    if rewardId is AnyCashbotSuitPart:
        return range(4000, 4011 + 1)
    if rewardId is AnyLawbotSuitPart:
        return range(4100, 4113 + 1)
    if rewardId is AnyBossbotSuitPart:
        return range(4200, 4216 + 1)
    return (rewardId,)

def findFinalRewardId(questId):
    finalRewardId = Quest2RewardDict.get(questId)
    if finalRewardId:
        remainingSteps = Quest2RemainingStepsDict.get(questId)
    else:
        try:
            questDesc = QuestDict[questId]
        except KeyError:
            print 'findFinalRewardId: Quest ID: %d not found' % questId
            return -1

        nextQuestId = questDesc[QuestDictNextQuestIndex]
        if nextQuestId == NA:
            finalRewardId = questDesc[QuestDictRewardIndex]
            remainingSteps = 1
        else:
            if type(nextQuestId) == type(()):
                finalRewardId, remainingSteps = findFinalRewardId(nextQuestId[0])
                for id in nextQuestId[1:]:
                    findFinalRewardId(id)

            else:
                finalRewardId, remainingSteps = findFinalRewardId(nextQuestId)
            remainingSteps += 1
        if finalRewardId != OBSOLETE:
            if questDesc[QuestDictStartIndex] == Start:
                tier = questDesc[QuestDictTierIndex]
                tier2RewardDict = Tier2Reward2QuestsDict.setdefault(tier, {})
                rewardIds = getAllRewardIdsForReward(finalRewardId)
                for rewardId in rewardIds:
                    questList = tier2RewardDict.setdefault(rewardId, [])
                    questList.append(questId)

        else:
            finalRewardId = None
        Quest2RewardDict[questId] = finalRewardId
        Quest2RemainingStepsDict[questId] = remainingSteps
    return (finalRewardId, remainingSteps)


for questId in QuestDict.keys():
    findFinalRewardId(questId)

def getStartingQuests(tier = None):
    startingQuests = []
    for questId in QuestDict.keys():
        if isStartingQuest(questId):
            if tier is None:
                startingQuests.append(questId)
            elif questId in Tier2QuestsDict[tier]:
                startingQuests.append(questId)

    startingQuests.sort()
    return startingQuests


def getFinalRewardId(questId, fAll = 0):
    if fAll or isStartingQuest(questId):
        return Quest2RewardDict.get(questId)
    else:
        return None
    return None


def isStartingQuest(questId):
    try:
        return QuestDict[questId][QuestDictStartIndex] == Start
    except KeyError:
        return None

    return None


def getNumChoices(tier):
    if tier in (0,):
        return 0
    if tier in (1,):
        return 2
    else:
        return 3


def getAvatarRewardId(av, questId):
    for quest in av.quests:
        if questId == quest[0]:
            return quest[3]

    notify.warning('getAvatarRewardId(): quest not found on avatar')
    return None


def getNextQuest(id, currentNpc, av):
    nextQuest = QuestDict[id][QuestDictNextQuestIndex]
    if nextQuest == NA:
        return (NA, NA)
    elif type(nextQuest) == type(()):
        nextReward = QuestDict[nextQuest[0]][QuestDictRewardIndex]
        nextNextQuest, nextNextToNpcId = getNextQuest(nextQuest[0], currentNpc, av)
        nextQuest = random.choice(nextQuest)
    if not getQuestClass(nextQuest).filterFunc(av):
        return getNextQuest(nextQuest, currentNpc, av)
    nextToNpcId = getQuestToNpcId(nextQuest)
    if nextToNpcId == Any:
        nextToNpcId = 2004
    elif nextToNpcId == Same:
        if currentNpc.getHq():
            nextToNpcId = ToonHQ
        else:
            nextToNpcId = currentNpc.getNpcId()
    elif nextToNpcId == ToonHQ:
        nextToNpcId = ToonHQ
    return (nextQuest, nextToNpcId)


def filterQuests(entireQuestPool, currentNpc, av):
    if notify.getDebug():
        notify.debug('filterQuests: entireQuestPool: %s' % entireQuestPool)
    validQuestPool = dict([ (questId, 1) for questId in entireQuestPool ])
    if isLoopingFinalTier(av.getRewardTier()):
        history = map(lambda questDesc: questDesc[0], av.quests)
    else:
        history = av.getQuestHistory()
    if notify.getDebug():
        notify.debug('filterQuests: av quest history: %s' % history)
    currentQuests = av.quests
    for questId in entireQuestPool:
        if questId in history:
            if notify.getDebug():
                notify.debug('filterQuests: Removed %s because in history' % questId)
            validQuestPool[questId] = 0
            continue
        potentialFromNpc = getQuestFromNpcId(questId)
        if not npcMatches(potentialFromNpc, currentNpc):
            if notify.getDebug():
                notify.debug('filterQuests: Removed %s: potentialFromNpc does not match currentNpc' % questId)
            validQuestPool[questId] = 0
            continue
        potentialToNpc = getQuestToNpcId(questId)
        if currentNpc.getNpcId() == potentialToNpc:
            if notify.getDebug():
                notify.debug('filterQuests: Removed %s because potentialToNpc is currentNpc' % questId)
            validQuestPool[questId] = 0
            continue
        if not getQuestClass(questId).filterFunc(av):
            if notify.getDebug():
                notify.debug('filterQuests: Removed %s because of filterFunc' % questId)
            validQuestPool[questId] = 0
            continue
        for quest in currentQuests:
            fromNpcId = quest[1]
            toNpcId = quest[2]
            if potentialToNpc == toNpcId and toNpcId != ToonHQ:
                validQuestPool[questId] = 0
                if notify.getDebug():
                    notify.debug('filterQuests: Removed %s because npc involved' % questId)
                break

    finalQuestPool = filter(lambda key: validQuestPool[key], validQuestPool.keys())
    if notify.getDebug():
        notify.debug('filterQuests: finalQuestPool: %s' % finalQuestPool)
    return finalQuestPool

def chooseMatchingQuest(tier, validQuestPool, rewardId, npc, av):
    questsMatchingReward = Tier2Reward2QuestsDict[tier].get(rewardId, [])
    if notify.getDebug():
        notify.debug('questsMatchingReward: %s tier: %s = %s' % (rewardId, tier, questsMatchingReward))
    validQuestsMatchingReward = PythonUtil.intersection(questsMatchingReward, validQuestPool)
    if notify.getDebug():
        notify.debug('validQuestsMatchingReward: %s tier: %s = %s' % (rewardId, tier, validQuestsMatchingReward))
    if validQuestsMatchingReward:
        bestQuest = seededRandomChoice(validQuestsMatchingReward)
    else:
        questsMatchingReward = Tier2Reward2QuestsDict[tier].get(AnyCashbotSuitPart, [])
        if notify.getDebug():
            notify.debug('questsMatchingReward: AnyCashbotSuitPart tier: %s = %s' % (tier, questsMatchingReward))
        validQuestsMatchingReward = PythonUtil.intersection(questsMatchingReward, validQuestPool)
        if validQuestsMatchingReward:
            if notify.getDebug():
                notify.debug('validQuestsMatchingReward: AnyCashbotSuitPart tier: %s = %s' % (tier, validQuestsMatchingReward))
            bestQuest = seededRandomChoice(validQuestsMatchingReward)
        else:
            questsMatchingReward = Tier2Reward2QuestsDict[tier].get(AnyLawbotSuitPart, [])
            if notify.getDebug():
                    notify.debug('questsMatchingReward: AnyLawbotSuitPart tier: %s = %s' % (tier, questsMatchingReward))
            validQuestsMatchingReward = PythonUtil.intersection(questsMatchingReward, validQuestPool)
            if validQuestsMatchingReward:
                if notify.getDebug():
                    notify.debug('validQuestsMatchingReward: AnyLawbotSuitPart tier: %s = %s' % (tier, validQuestsMatchingReward))
                bestQuest = seededRandomChoice(validQuestsMatchingReward)
            else:
                questsMatchingReward = Tier2Reward2QuestsDict[tier].get(Any, [])
                if notify.getDebug():
                    notify.debug('questsMatchingReward: Any tier: %s = %s' % (tier, questsMatchingReward))
                if not questsMatchingReward:
                    notify.warning('chooseMatchingQuests, no questsMatchingReward')
                    return None
                validQuestsMatchingReward = PythonUtil.intersection(questsMatchingReward, validQuestPool)
                if not validQuestsMatchingReward:
                    notify.warning('chooseMatchingQuests, no validQuestsMatchingReward')
                    return None
                if notify.getDebug():
                    notify.debug('validQuestsMatchingReward: Any tier: %s = %s' % (tier, validQuestsMatchingReward))
                bestQuest = seededRandomChoice(validQuestsMatchingReward)
    return bestQuest

	
def transformReward(baseRewardId, av):
    if baseRewardId == 900:
        trackId, progress = av.getTrackProgress()
        if trackId == -1:
            notify.warning('transformReward: asked to transform 900 but av is not training')
            actualRewardId = baseRewardId
        else:
            actualRewardId = 900 + 1 + trackId
        return actualRewardId
    elif baseRewardId > 800 and baseRewardId < 900:
        trackId, progress = av.getTrackProgress()
        if trackId < 0:
            notify.warning('transformReward: av: %s is training a track with none chosen!' % av.getDoId())
            return 601
        else:
            actualRewardId = baseRewardId + 200 + trackId * 100
            return actualRewardId
    else:
        return baseRewardId


def chooseBestQuests(tier, currentNpc, av):
    if isLoopingFinalTier(tier):
        rewardHistory = map(lambda questDesc: questDesc[3], av.quests)
    else:
        rewardHistory = av.getRewardHistory()[1]

    seedRandomGen(currentNpc.getNpcId(), av.getDoId(), tier, rewardHistory)
    numChoices = getNumChoices(tier)
    rewards = getNextRewards(numChoices, tier, av)
    if not rewards:
        return []
    possibleQuests = []
    possibleRewards = list(rewards)
    if Any not in possibleRewards:
        possibleRewards.append(Any)
    for rewardId in possibleRewards:
        possibleQuests.extend(Tier2Reward2QuestsDict[tier].get(rewardId, []))

    validQuestPool = filterQuests(possibleQuests, currentNpc, av)
    if not validQuestPool:
        return []
    if numChoices == 0:
        numChoices = 1
    bestQuests = []
    for i in xrange(numChoices):
        if len(validQuestPool) == 0:
            break
        if len(rewards) == 0:
            break
        rewardId = rewards.pop(0)
        bestQuestId = chooseMatchingQuest(tier, validQuestPool, rewardId, currentNpc, av)
        if bestQuestId is None:
            continue
        validQuestPool.remove(bestQuestId)
        bestQuestToNpcId = getQuestToNpcId(bestQuestId)
        if bestQuestToNpcId == Any:
            bestQuestToNpcId = 2003
        elif bestQuestToNpcId == Same:
            if currentNpc.getHq():
                bestQuestToNpcId = ToonHQ
            else:
                bestQuestToNpcId = currentNpc.getNpcId()
        elif bestQuestToNpcId == ToonHQ:
            bestQuestToNpcId = ToonHQ
        bestQuests.append([bestQuestId, rewardId, bestQuestToNpcId])

    for quest in bestQuests:
        quest[1] = transformReward(quest[1], av)

    return bestQuests


def questExists(id):
    return id in QuestDict


def getQuest(id):
    questEntry = QuestDict.get(id)
    if questEntry:
        questDesc = questEntry[QuestDictDescIndex]
        questClass = questDesc[0]
        return questClass(id, questDesc[1:])
    else:
        return None
    return None


def getQuestClass(id):
    questEntry = QuestDict.get(id)
    if questEntry:
        return questEntry[QuestDictDescIndex][0]
    else:
        return None
    return None


def getVisitSCStrings(npcId):
    if npcId == ToonHQ:
        strings = [TTLocalizer.QuestsRecoverItemQuestSeeHQSCString, TTLocalizer.QuestsRecoverItemQuestGoToHQSCString]
    elif npcId == ToonTailor:
        strings = [TTLocalizer.QuestsTailorQuestSCString]
    elif npcId:
        npcName, hoodName, buildingArticle, buildingName, toStreet, streetName, isInPlayground = getNpcInfo(npcId)
        strings = [TTLocalizer.QuestsVisitQuestSeeSCString % npcName]
        if isInPlayground:
            strings.append(TTLocalizer.QuestsRecoverItemQuestGoToPlaygroundSCString % hoodName)
        else:
            strings.append(TTLocalizer.QuestsRecoverItemQuestGoToStreetSCString % {'to': toStreet,
             'street': streetName,
             'hood': hoodName})
        strings.extend([TTLocalizer.QuestsRecoverItemQuestVisitBuildingSCString % (buildingArticle, buildingName), TTLocalizer.QuestsRecoverItemQuestWhereIsBuildingSCString % (buildingArticle, buildingName)])
    return strings


def getFinishToonTaskSCStrings(npcId):
    return [TTLocalizer.QuestsGenericFinishSCString] + getVisitSCStrings(npcId)


def chooseQuestDialog(id, status):
    questDialog = getQuestDialog(id).get(status)
    if questDialog == None:
        if status == QUEST:
            quest = getQuest(id)
            questDialog = quest.getDefaultQuestDialog()
        else:
            questDialog = DefaultDialog[status]
    if type(questDialog) == type(()):
        return random.choice(questDialog)
    else:
        return questDialog
    return


def chooseQuestDialogReject():
    return random.choice(DefaultReject)


def chooseQuestDialogTierNotDone():
    return random.choice(DefaultTierNotDone)


def getNpcInfo(npcId):
    npcName = NPCToons.getNPCName(npcId)
    npcZone = NPCToons.getNPCZone(npcId)
    hoodId = ZoneUtil.getCanonicalHoodId(npcZone)
    hoodName = base.cr.hoodMgr.getFullnameFromId(hoodId)
    buildingArticle = NPCToons.getBuildingArticle(npcZone)
    buildingName = NPCToons.getBuildingTitle(npcZone)
    branchId = ZoneUtil.getCanonicalBranchZone(npcZone)
    toStreet = ToontownGlobals.StreetNames[branchId][0]
    streetName = ToontownGlobals.StreetNames[branchId][-1]
    isInPlayground = ZoneUtil.isPlayground(branchId)
    return (npcName,
     hoodName,
     buildingArticle,
     buildingName,
     toStreet,
     streetName,
     isInPlayground)


def getNpcLocationDialog(fromNpcId, toNpcId):
    if not toNpcId:
        return (None, None, None)
    fromNpcZone = None
    fromBranchId = None
    if fromNpcId:
        fromNpcZone = NPCToons.getNPCZone(fromNpcId)
        fromBranchId = ZoneUtil.getCanonicalBranchZone(fromNpcZone)
    toNpcZone = NPCToons.getNPCZone(toNpcId)
    toBranchId = ZoneUtil.getCanonicalBranchZone(toNpcZone)
    toNpcName, toHoodName, toBuildingArticle, toBuildingName, toStreetTo, toStreetName, isInPlayground = getNpcInfo(toNpcId)
    if fromBranchId == toBranchId:
        if isInPlayground:
            streetDesc = TTLocalizer.QuestsStreetLocationThisPlayground
        else:
            streetDesc = TTLocalizer.QuestsStreetLocationThisStreet
    elif isInPlayground:
        streetDesc = TTLocalizer.QuestsStreetLocationNamedPlayground % toHoodName
    else:
        streetDesc = TTLocalizer.QuestsStreetLocationNamedStreet % {'toStreetName': toStreetName,
         'toHoodName': toHoodName}
    paragraph = TTLocalizer.QuestsLocationParagraph % {'building': TTLocalizer.QuestsLocationBuilding % toNpcName,
     'buildingName': toBuildingName,
     'buildingVerb': TTLocalizer.QuestsLocationBuildingVerb,
     'street': streetDesc}
    return (paragraph, toBuildingName, streetDesc)


def fillInQuestNames(text, avName = None, fromNpcId = None, toNpcId = None):
    text = copy.deepcopy(text)
    if avName != None:
        text = text.replace('_avName_', avName)
    if toNpcId:
        if toNpcId == ToonHQ:
            toNpcName = TTLocalizer.QuestsHQOfficerFillin
            where = TTLocalizer.QuestsHQWhereFillin
            buildingName = TTLocalizer.QuestsHQBuildingNameFillin
            streetDesc = TTLocalizer.QuestsHQLocationNameFillin
        elif toNpcId == ToonTailor:
            toNpcName = TTLocalizer.QuestsTailorFillin
            where = TTLocalizer.QuestsTailorWhereFillin
            buildingName = TTLocalizer.QuestsTailorBuildingNameFillin
            streetDesc = TTLocalizer.QuestsTailorLocationNameFillin
        else:
            toNpcName = str(NPCToons.getNPCName(toNpcId))
            where, buildingName, streetDesc = getNpcLocationDialog(fromNpcId, toNpcId)
        text = text.replace('_toNpcName_', toNpcName)
        text = text.replace('_where_', where)
        text = text.replace('_buildingName_', buildingName)
        text = text.replace('_streetDesc_', streetDesc)
    return text


def getVisitingQuest():
    return VisitQuest(VISIT_QUEST_ID)


class Reward:
    def __init__(self, id, reward):
        self.id = id
        self.reward = reward

    def getId(self):
        return self.id

    def getType(self):
        return self.__class__

    def getAmount(self):
        return None

    def sendRewardAI(self, av):
        raise 'not implemented'

    def countReward(self, qrc):
        raise 'not implemented'

    def getString(self):
        return 'undefined'

    def getPosterString(self):
        return 'base class'


class MaxHpReward(Reward):
    def __init__(self, id, reward):
        Reward.__init__(self, id, reward)

    def getAmount(self):
        return self.reward[0]

    def sendRewardAI(self, av):
        maxHp = av.getMaxHp()
        maxHp = min(ToontownGlobals.MaxHpLimit, maxHp + self.getAmount())
        av.b_setMaxHp(maxHp)
        av.toonUp(maxHp)

    def countReward(self, qrc):
        qrc.maxHp += self.getAmount()

    def getString(self):
        return TTLocalizer.QuestsMaxHpReward % self.getAmount()

    def getPosterString(self):
        return TTLocalizer.QuestsMaxHpRewardPoster % self.getAmount()


class MoneyReward(Reward):
    def __init__(self, id, reward):
        Reward.__init__(self, id, reward)

    def getAmount(self):
        return self.reward[0]

    def sendRewardAI(self, av):
        money = av.getMoney()
        maxMoney = av.getMaxMoney()
        av.addMoney(self.getAmount())

    def countReward(self, qrc):
        qrc.money += self.getAmount()

    def getString(self):
        amt = self.getAmount()
        if amt == 1:
            return TTLocalizer.QuestsMoneyRewardSingular
        else:
            return TTLocalizer.QuestsMoneyRewardPlural % amt

    def getPosterString(self):
        amt = self.getAmount()
        if amt == 1:
            return TTLocalizer.QuestsMoneyRewardPosterSingular
        else:
            return TTLocalizer.QuestsMoneyRewardPosterPlural % amt


class MaxGagCarryReward(Reward):
    def __init__(self, id, reward):
        Reward.__init__(self, id, reward)

    def getAmount(self):
        return self.reward[0]

    def getName(self):
        return self.reward[1]

    def sendRewardAI(self, av):
        av.b_setMaxCarry(self.getAmount())

    def countReward(self, qrc):
        qrc.maxCarry = self.getAmount()

    def getString(self):
        name = self.getName()
        amt = self.getAmount()
        return TTLocalizer.QuestsMaxGagCarryReward % {'name': name,
         'num': amt}

    def getPosterString(self):
        name = self.getName()
        amt = self.getAmount()
        return TTLocalizer.QuestsMaxGagCarryRewardPoster % {'name': name,
         'num': amt}


class MaxQuestCarryReward(Reward):
    def __init__(self, id, reward):
        Reward.__init__(self, id, reward)

    def getAmount(self):
        return self.reward[0]

    def sendRewardAI(self, av):
        av.b_setQuestCarryLimit(self.getAmount())

    def countReward(self, qrc):
        qrc.questCarryLimit = self.getAmount()

    def getString(self):
        amt = self.getAmount()
        return TTLocalizer.QuestsMaxQuestCarryReward % amt

    def getPosterString(self):
        amt = self.getAmount()
        return TTLocalizer.QuestsMaxQuestCarryRewardPoster % amt

TrackTrainingQuotas = {ToontownBattleGlobals.HEAL_TRACK: 15,
 ToontownBattleGlobals.TRAP_TRACK: 15,
 ToontownBattleGlobals.LURE_TRACK: 15,
 ToontownBattleGlobals.SOUND_TRACK: 15,
 ToontownBattleGlobals.THROW_TRACK: 15,
 ToontownBattleGlobals.SQUIRT_TRACK: 15,
 ToontownBattleGlobals.DROP_TRACK: 15}

class TrackTrainingReward(Reward):
    def __init__(self, id, reward):
        Reward.__init__(self, id, reward)

    def getTrack(self):
        track = self.reward[0]
        if track == None:
            track = 0
        return track

    def sendRewardAI(self, av):
        av.b_setTrackProgress(self.getTrack(), 0)

    def countReward(self, qrc):
        qrc.trackProgressId = self.getTrack()
        qrc.trackProgress = 0

    def getString(self):
        trackName = ToontownBattleGlobals.Tracks[self.getTrack()].capitalize()
        return TTLocalizer.QuestsTrackTrainingReward % trackName

    def getPosterString(self):
        return TTLocalizer.QuestsTrackTrainingRewardPoster

class TrackProgressReward(Reward):
    def __init__(self, id, reward):
        Reward.__init__(self, id, reward)

    def getTrack(self):
        track = self.reward[0]
        if track == None:
            track = 0
        return track

    def getProgressIndex(self):
        return self.reward[1]

    def sendRewardAI(self, av):
        av.addTrackProgress(self.getTrack(), self.getProgressIndex())

    def countReward(self, qrc):
        qrc.addTrackProgress(self.getTrack(), self.getProgressIndex())

    def getString(self):
        trackName = ToontownBattleGlobals.Tracks[self.getTrack()].capitalize()
        return TTLocalizer.QuestsTrackProgressReward % {'frameNum': self.getProgressIndex(), 'trackName': trackName}

    def getPosterString(self):
        trackName = ToontownBattleGlobals.Tracks[self.getTrack()].capitalize()
        return TTLocalizer.QuestsTrackProgressRewardPoster % {'trackName': trackName, 'frameNum': self.getProgressIndex()}

class TrackCompleteReward(Reward):
    def __init__(self, id, reward):
        Reward.__init__(self, id, reward)

    def getTrack(self):
        track = self.reward[0]
        if track == None:
            track = 0
        return track

    def sendRewardAI(self, av):
        av.addTrackAccess(self.getTrack())
        av.clearTrackProgress()

    def countReward(self, qrc):
        qrc.addTrackAccess(self.getTrack())
        qrc.clearTrackProgress()

    def getString(self):
        trackName = ToontownBattleGlobals.Tracks[self.getTrack()].capitalize()
        return TTLocalizer.QuestsTrackCompleteReward % trackName

    def getPosterString(self):
        trackName = ToontownBattleGlobals.Tracks[self.getTrack()].capitalize()
        return TTLocalizer.QuestsTrackCompleteRewardPoster % trackName

class BuffReward(Reward):
    def sendRewardAI(self, av):
        av.addBuff(self.getBuffId(), self.getBuffTime())

    def getBuffId(self):
        return self.reward[0]

    def getBuffTime(self):
        return self.reward[1]

    def getString(self):
        return TTLocalizer.getBuffString(self.getBuffId(), self.getBuffTime())

    def getPosterString(self):
        return TTLocalizer.getBuffPosterString(self.getBuffId())  

class MeritReward(Reward):
    def __init__(self, id, reward):
        Reward.__init__(self, id, reward)
        self.meritLabel = TTLocalizer.RewardPanelMeritBarLabels[self.getMeritId()]

    def sendRewardAI(self, av):
        av.doQuestMerits(self.getMeritId())

    def getMeritId(self):
        return self.reward[0]

    def getString(self):
        return TTLocalizer.QuestsCogMeritReward % (self.meritLabel)

    def getPosterString(self):
        return TTLocalizer.QuestsCogMeritRewardPoster % (self.meritLabel)
        
def getRewardClass(id):
    reward = RewardDict.get(id)
    if reward:
        return reward[0]
    else:
        return None
    return None


def getReward(id):
    reward = RewardDict.get(id)
    if reward:
        rewardClass = reward[0]
        return rewardClass(id, reward[1:])
    else:
        notify.warning('getReward(): id %s not found.' % id)
        return None
    return None


def getNextRewards(numChoices, tier, av):
    rewardTier = list(getRewardsInTier(tier))
    optRewards = list(getOptionalRewardsInTier(tier))
    if tier == TT_TIER + 3:
        optRewards = []
    if isLoopingFinalTier(tier):
        rewardHistory = map(lambda questDesc: questDesc[3], av.quests)
        if notify.getDebug():
            notify.debug('getNextRewards: current rewards (history): %s' % rewardHistory)
    else:
        rewardHistory = av.getRewardHistory()[1]
        if notify.getDebug():
            notify.debug('getNextRewards: rewardHistory: %s' % rewardHistory)
    if notify.getDebug():
        notify.debug('getNextRewards: rewardTier: %s' % rewardTier)
        notify.debug('getNextRewards: numChoices: %s' % numChoices)
    for rewardId in getOptionalRewardsInTier(tier):
        if getRewardClass(rewardId) == MeritReward:
            dept = RewardDict.get(rewardId)[1]
            if av.isCogSuitMaxed(dept):
                notify.debug('getNextRewards: already maxed cog suit for dept %s' % dept)
                optRewards.remove(rewardId)

    for rewardId in rewardHistory:
        if rewardId in rewardTier:
            rewardTier.remove(rewardId)
        elif rewardId in optRewards:
            optRewards.remove(rewardId)
        elif rewardId in (901, 902, 903, 904, 905, 906, 907):
            genericRewardId = 900
            if genericRewardId in rewardTier:
                rewardTier.remove(genericRewardId)
        elif rewardId > 1000 and rewardId < 1699:
            index = rewardId % 100
            genericRewardId = 800 + index
            if genericRewardId in rewardTier:
                rewardTier.remove(genericRewardId)

    if numChoices == 0:
        if len(rewardTier) == 0:
            return []
        else:
            return [rewardTier[0]]
    rewardPool = rewardTier[:numChoices]
    for i in xrange(len(rewardPool), numChoices * 2):
        if optRewards:
            optionalReward = seededRandomChoice(optRewards)
            optRewards.remove(optionalReward)
            rewardPool.append(optionalReward)
        else:
            break

    if notify.getDebug():
        notify.debug('getNextRewards: starting reward pool: %s' % rewardPool)
    if len(rewardPool) == 0:
        if notify.getDebug():
            notify.debug('getNextRewards: no rewards left at all')
        return []
    finalRewardPool = [rewardPool.pop(0)]
    for i in xrange(numChoices - 1):
        if len(rewardPool) == 0:
            break
        selectedReward = seededRandomChoice(rewardPool)
        rewardPool.remove(selectedReward)
        finalRewardPool.append(selectedReward)

    if notify.getDebug():
        notify.debug('getNextRewards: final reward pool: %s' % finalRewardPool)
    return finalRewardPool


RewardDict = {
    100: (MaxHpReward, 1),
    101: (MaxHpReward, 2),
    102: (MaxHpReward, 3),
    103: (MaxHpReward, 4),
    104: (MaxHpReward, 5),
    105: (MaxHpReward, 6),
    106: (MaxHpReward, 7),
    107: (MaxHpReward, 8),
    108: (MaxHpReward, 9),
    109: (MaxHpReward, 10),
    200: (MaxGagCarryReward, 25, TTLocalizer.QuestsMediumPouch),
    201: (MaxGagCarryReward, 30, TTLocalizer.QuestsLargePouch),
    202: (MaxGagCarryReward, 35, TTLocalizer.QuestsSmallBag),
    203: (MaxGagCarryReward, 40, TTLocalizer.QuestsMediumBag),
    204: (MaxGagCarryReward, 50, TTLocalizer.QuestsLargeBag),
    205: (MaxGagCarryReward, 60, TTLocalizer.QuestsSmallBackpack),
    206: (MaxGagCarryReward, 70, TTLocalizer.QuestsMediumBackpack),
    207: (MaxGagCarryReward, 80, TTLocalizer.QuestsLargeBackpack),
    500: (MaxQuestCarryReward, 2),
    501: (MaxQuestCarryReward, 3),
    502: (MaxQuestCarryReward, 4),
    600: (MoneyReward, 10),
    601: (MoneyReward, 20),
    602: (MoneyReward, 40),
    603: (MoneyReward, 60),
    604: (MoneyReward, 100),
    605: (MoneyReward, 150),
    606: (MoneyReward, 200),
    607: (MoneyReward, 250),
    608: (MoneyReward, 300),
    609: (MoneyReward, 400),
    610: (MoneyReward, 500),
    611: (MoneyReward, 600),
    612: (MoneyReward, 700),
    613: (MoneyReward, 800),
    614: (MoneyReward, 900),
    615: (MoneyReward, 1000),
    616: (MoneyReward, 1100),
    617: (MoneyReward, 1200),
    618: (MoneyReward, 1300),
    619: (MoneyReward, 1400),
    620: (MoneyReward, 1500),
    621: (MoneyReward, 1750),
    622: (MoneyReward, 2000),
    623: (MoneyReward, 2500),
    801: (TrackProgressReward, None, 1),
    802: (TrackProgressReward, None, 2),
    803: (TrackProgressReward, None, 3),
    804: (TrackProgressReward, None, 4),
    805: (TrackProgressReward, None, 5),
    806: (TrackProgressReward, None, 6),
    807: (TrackProgressReward, None, 7),
    808: (TrackProgressReward, None, 8),
    809: (TrackProgressReward, None, 9),
    810: (TrackProgressReward, None, 10),
    811: (TrackProgressReward, None, 11),
    812: (TrackProgressReward, None, 12),
    813: (TrackProgressReward, None, 13),
    814: (TrackProgressReward, None, 14),
    815: (TrackProgressReward, None, 15),
    1001: (TrackProgressReward, ToontownBattleGlobals.HEAL_TRACK, 1),
    1002: (TrackProgressReward, ToontownBattleGlobals.HEAL_TRACK, 2),
    1003: (TrackProgressReward, ToontownBattleGlobals.HEAL_TRACK, 3),
    1004: (TrackProgressReward, ToontownBattleGlobals.HEAL_TRACK, 4),
    1005: (TrackProgressReward, ToontownBattleGlobals.HEAL_TRACK, 5),
    1006: (TrackProgressReward, ToontownBattleGlobals.HEAL_TRACK, 6),
    1007: (TrackProgressReward, ToontownBattleGlobals.HEAL_TRACK, 7),
    1008: (TrackProgressReward, ToontownBattleGlobals.HEAL_TRACK, 8),
    1009: (TrackProgressReward, ToontownBattleGlobals.HEAL_TRACK, 9),
    1010: (TrackProgressReward, ToontownBattleGlobals.HEAL_TRACK, 10),
    1011: (TrackProgressReward, ToontownBattleGlobals.HEAL_TRACK, 11),
    1012: (TrackProgressReward, ToontownBattleGlobals.HEAL_TRACK, 12),
    1013: (TrackProgressReward, ToontownBattleGlobals.HEAL_TRACK, 13),
    1014: (TrackProgressReward, ToontownBattleGlobals.HEAL_TRACK, 14),
    1015: (TrackProgressReward, ToontownBattleGlobals.HEAL_TRACK, 15),
    1101: (TrackProgressReward, ToontownBattleGlobals.TRAP_TRACK, 1),
    1102: (TrackProgressReward, ToontownBattleGlobals.TRAP_TRACK, 2),
    1103: (TrackProgressReward, ToontownBattleGlobals.TRAP_TRACK, 3),
    1104: (TrackProgressReward, ToontownBattleGlobals.TRAP_TRACK, 4),
    1105: (TrackProgressReward, ToontownBattleGlobals.TRAP_TRACK, 5),
    1106: (TrackProgressReward, ToontownBattleGlobals.TRAP_TRACK, 6),
    1107: (TrackProgressReward, ToontownBattleGlobals.TRAP_TRACK, 7),
    1108: (TrackProgressReward, ToontownBattleGlobals.TRAP_TRACK, 8),
    1109: (TrackProgressReward, ToontownBattleGlobals.TRAP_TRACK, 9),
    1110: (TrackProgressReward, ToontownBattleGlobals.TRAP_TRACK, 10),
    1111: (TrackProgressReward, ToontownBattleGlobals.TRAP_TRACK, 11),
    1112: (TrackProgressReward, ToontownBattleGlobals.TRAP_TRACK, 12),
    1113: (TrackProgressReward, ToontownBattleGlobals.TRAP_TRACK, 13),
    1114: (TrackProgressReward, ToontownBattleGlobals.TRAP_TRACK, 14),
    1115: (TrackProgressReward, ToontownBattleGlobals.TRAP_TRACK, 15),
    1201: (TrackProgressReward, ToontownBattleGlobals.LURE_TRACK, 1),
    1202: (TrackProgressReward, ToontownBattleGlobals.LURE_TRACK, 2),
    1203: (TrackProgressReward, ToontownBattleGlobals.LURE_TRACK, 3),
    1204: (TrackProgressReward, ToontownBattleGlobals.LURE_TRACK, 4),
    1205: (TrackProgressReward, ToontownBattleGlobals.LURE_TRACK, 5),
    1206: (TrackProgressReward, ToontownBattleGlobals.LURE_TRACK, 6),
    1207: (TrackProgressReward, ToontownBattleGlobals.LURE_TRACK, 7),
    1208: (TrackProgressReward, ToontownBattleGlobals.LURE_TRACK, 8),
    1209: (TrackProgressReward, ToontownBattleGlobals.LURE_TRACK, 9),
    1210: (TrackProgressReward, ToontownBattleGlobals.LURE_TRACK, 10),
    1211: (TrackProgressReward, ToontownBattleGlobals.LURE_TRACK, 11),
    1212: (TrackProgressReward, ToontownBattleGlobals.LURE_TRACK, 12),
    1213: (TrackProgressReward, ToontownBattleGlobals.LURE_TRACK, 13),
    1214: (TrackProgressReward, ToontownBattleGlobals.LURE_TRACK, 14),
    1215: (TrackProgressReward, ToontownBattleGlobals.LURE_TRACK, 15),
    1301: (TrackProgressReward, ToontownBattleGlobals.SOUND_TRACK, 1),
    1302: (TrackProgressReward, ToontownBattleGlobals.SOUND_TRACK, 2),
    1303: (TrackProgressReward, ToontownBattleGlobals.SOUND_TRACK, 3),
    1304: (TrackProgressReward, ToontownBattleGlobals.SOUND_TRACK, 4),
    1305: (TrackProgressReward, ToontownBattleGlobals.SOUND_TRACK, 5),
    1306: (TrackProgressReward, ToontownBattleGlobals.SOUND_TRACK, 6),
    1307: (TrackProgressReward, ToontownBattleGlobals.SOUND_TRACK, 7),
    1308: (TrackProgressReward, ToontownBattleGlobals.SOUND_TRACK, 8),
    1309: (TrackProgressReward, ToontownBattleGlobals.SOUND_TRACK, 9),
    1310: (TrackProgressReward, ToontownBattleGlobals.SOUND_TRACK, 10),
    1311: (TrackProgressReward, ToontownBattleGlobals.SOUND_TRACK, 11),
    1312: (TrackProgressReward, ToontownBattleGlobals.SOUND_TRACK, 12),
    1313: (TrackProgressReward, ToontownBattleGlobals.SOUND_TRACK, 13),
    1314: (TrackProgressReward, ToontownBattleGlobals.SOUND_TRACK, 14),
    1315: (TrackProgressReward, ToontownBattleGlobals.SOUND_TRACK, 15),
    1601: (TrackProgressReward, ToontownBattleGlobals.DROP_TRACK, 1),
    1602: (TrackProgressReward, ToontownBattleGlobals.DROP_TRACK, 2),
    1603: (TrackProgressReward, ToontownBattleGlobals.DROP_TRACK, 3),
    1604: (TrackProgressReward, ToontownBattleGlobals.DROP_TRACK, 4),
    1605: (TrackProgressReward, ToontownBattleGlobals.DROP_TRACK, 5),
    1606: (TrackProgressReward, ToontownBattleGlobals.DROP_TRACK, 6),
    1607: (TrackProgressReward, ToontownBattleGlobals.DROP_TRACK, 7),
    1608: (TrackProgressReward, ToontownBattleGlobals.DROP_TRACK, 8),
    1609: (TrackProgressReward, ToontownBattleGlobals.DROP_TRACK, 9),
    1610: (TrackProgressReward, ToontownBattleGlobals.DROP_TRACK, 10),
    1611: (TrackProgressReward, ToontownBattleGlobals.DROP_TRACK, 11),
    1612: (TrackProgressReward, ToontownBattleGlobals.DROP_TRACK, 12),
    1613: (TrackProgressReward, ToontownBattleGlobals.DROP_TRACK, 13),
    1614: (TrackProgressReward, ToontownBattleGlobals.DROP_TRACK, 14),
    1615: (TrackProgressReward, ToontownBattleGlobals.DROP_TRACK, 15),
    900: (TrackCompleteReward, None),
    901: (TrackCompleteReward, ToontownBattleGlobals.HEAL_TRACK),
    902: (TrackCompleteReward, ToontownBattleGlobals.TRAP_TRACK),
    903: (TrackCompleteReward, ToontownBattleGlobals.LURE_TRACK),
    904: (TrackCompleteReward, ToontownBattleGlobals.SOUND_TRACK),
    905: (TrackCompleteReward, ToontownBattleGlobals.THROW_TRACK),
    906: (TrackCompleteReward, ToontownBattleGlobals.SQUIRT_TRACK),
    907: (TrackCompleteReward, ToontownBattleGlobals.DROP_TRACK),
    # Buff rewards (BuffID, Time):
    # Movement Speed Increase
    3001: (BuffReward, ToontownGlobals.BMovementSpeed, 30),
    3002: (BuffReward, ToontownGlobals.BMovementSpeed, 60),
    3003: (BuffReward, ToontownGlobals.BMovementSpeed, 180),
    3004: (BuffReward, ToontownGlobals.BMovementSpeed, 360),
    # Merit Rewards (Dept (0-3)):
    5001: (MeritReward, 0, None),
    5002: (MeritReward, 1, None),
    5003: (MeritReward, 2, None),
    5004: (MeritReward, 3, None)
}

BuffRewardIds = [3001, 3002, 3003, 3004]

def getNumTiers():
    return len(RequiredRewardTrackDict) - 1


def isLoopingFinalTier(tier):
    return tier == LOOPING_FINAL_TIER


def getRewardsInTier(tier):
    return RequiredRewardTrackDict.get(tier, [])


def getNumRewardsInTier(tier):
    return len(RequiredRewardTrackDict.get(tier, []))


def rewardTierExists(tier):
    return tier in RequiredRewardTrackDict


def getOptionalRewardsInTier(tier):
    return OptionalRewardTrackDict.get(tier, [])
    
def getRewardIdFromTrackId(trackId):
    return 401 + trackId

RequiredRewardTrackDict = {}
OptionalRewardTrackDict = {}


def isRewardOptional(tier, rewardId):
    return tier in OptionalRewardTrackDict and rewardId in OptionalRewardTrackDict[tier]


def getItemName(itemId):
    return ItemDict[itemId][0]


def getPluralItemName(itemId):
    return ItemDict[itemId][1]


def avatarHasTrolleyQuest(av):
    return len(av.quests) == 1 and av.quests[0][0] == TROLLEY_QUEST_ID


def avatarHasCompletedTrolleyQuest(av):
    return av.quests[0][4] > 0


def avatarHasFirstCogQuest(av):
    return len(av.quests) == 1 and av.quests[0][0] == FIRST_COG_QUEST_ID


def avatarHasCompletedFirstCogQuest(av):
    return av.quests[0][4] > 0


def avatarHasFriendQuest(av):
    return len(av.quests) == 1 and av.quests[0][0] == FRIEND_QUEST_ID


def avatarHasCompletedFriendQuest(av):
    return av.quests[0][4] > 0


def avatarHasPhoneQuest(av):
    return len(av.quests) == 1 and av.quests[0][0] == PHONE_QUEST_ID


def avatarHasCompletedPhoneQuest(av):
    return av.quests[0][4] > 0


def avatarWorkingOnRequiredRewards(av):
    tier = av.getRewardTier()
    rewardList = list(getRewardsInTier(tier))
    for i in xrange(len(rewardList)):
        actualRewardId = transformReward(rewardList[i], av)
        rewardList[i] = actualRewardId

    for questDesc in av.quests:
        questId = questDesc[0]
        rewardId = questDesc[3]
        if rewardId in rewardList:
            return 1
        elif rewardId == NA:
            rewardId = transformReward(getFinalRewardId(questId, fAll=1), av)
            if rewardId in rewardList:
                return 1

    return 0


def avatarHasAllRequiredRewards(av, tier):
    # Get the reward history.
    rewardHistory = list(av.getRewardHistory()[1])

    # Delete quests we're working on from the reward History.
    avQuests = av.getQuests()

    # Iterate through the current quests.
    for i in xrange(0, len(avQuests), 5):
        questDesc = avQuests[i:i + 5]
        questId, fromNpcId, toNpcId, rewardId, toonProgress = questDesc
        transformedRewardId = transformReward(rewardId, av)

        if rewardId in rewardHistory:
            rewardHistory.remove(rewardId)

        if transformedRewardId in rewardHistory:
            rewardHistory.remove(transformedRewardId)

    rewardList = getRewardsInTier(tier)
    notify.debug('checking avatarHasAllRequiredRewards: history: %s, tier: %s' % (rewardHistory, rewardList))
    for rewardId in rewardList:
        if rewardId == 900:
            found = 0
            for actualRewardId in (901, 902, 903, 904, 905, 906, 907):
                if actualRewardId in rewardHistory:
                    found = 1
                    rewardHistory.remove(actualRewardId)
                    if notify.getDebug():
                        notify.debug('avatarHasAllRequiredRewards: rewardId 900 found as: %s' % actualRewardId)
                    break

            if not found:
                if notify.getDebug():
                    notify.debug('avatarHasAllRequiredRewards: rewardId 900 not found')
                return 0
        else:
            actualRewardId = transformReward(rewardId, av)
            if actualRewardId in rewardHistory:
                rewardHistory.remove(actualRewardId)
            elif getRewardClass(rewardId) == CogSuitPartReward:
                deptStr = RewardDict.get(rewardId)[1]
                cogPart = RewardDict.get(rewardId)[2]
                dept = ToontownGlobals.cogDept2index[deptStr]
                if av.hasCogPart(cogPart, dept):
                    if notify.getDebug():
                        notify.debug('avatarHasAllRequiredRewards: rewardId: %s counts, avatar has cog part: %s dept: %s' % (actualRewardId, cogPart, dept))
                else:
                    if notify.getDebug():
                        notify.debug('avatarHasAllRequiredRewards: CogSuitPartReward: %s not found' % actualRewardId)
                    return 0
            else:
                if notify.getDebug():
                    notify.debug('avatarHasAllRequiredRewards: rewardId %s not found' % actualRewardId)
                return 0

    if notify.getDebug():
        notify.debug('avatarHasAllRequiredRewards: remaining rewards: %s' % rewardHistory)
        for rewardId in rewardHistory:
            if not isRewardOptional(tier, rewardId):
                notify.warning('required reward found, expected only optional: %s' % rewardId)

    return 1


def nextQuestList(nextQuest):
    if nextQuest == NA:
        return None
    seqTypes = (types.ListType, types.TupleType)
    if type(nextQuest) in seqTypes:
        return nextQuest
    else:
        return (nextQuest,)
    return None


def checkReward(questId, forked = 0):
    quest = QuestDict[questId]
    reward = quest[5]
    nextQuests = nextQuestList(quest[6])
    if nextQuests is None:
        validRewards = RewardDict.keys() + [Any,
         AnyCashbotSuitPart,
         AnyLawbotSuitPart,
         OBSOLETE]
        if reward is OBSOLETE:
            print 'warning: quest %s is obsolete' % questId
        return reward
    else:
        forked = forked or len(nextQuests) > 1
        firstReward = checkReward(nextQuests[0], forked)
        for qId in nextQuests[1:]:
            thisReward = checkReward(qId, forked)

        return firstReward
    return


def assertAllQuestsValid():
    print 'checking quests...'
    for questId in QuestDict.keys():
        try:
            quest = getQuest(questId)
        except AssertionError, e:
            err = 'invalid quest: %s' % questId
            print err
            raise

    for questId in QuestDict.keys():
        quest = QuestDict[questId]
        tier, start, questDesc, fromNpc, toNpc, reward, nextQuest, dialog = quest
        if start:
            checkReward(questId)
