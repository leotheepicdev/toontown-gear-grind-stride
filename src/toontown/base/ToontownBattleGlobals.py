from panda3d.core import Point3, Vec3
from ToontownGlobals import *
from toontown.distributed import DistrictGlobals
import math
import TTLocalizer

BattleCamFaceOffFov = 30.0
BattleCamFaceOffPos = Point3(0, -10, 4)
BattleCamDefaultPos = Point3(0, -8.6, 16.5)
BattleCamDefaultHpr = Vec3(0, -61, 0)
BattleCamDefaultFov = 80.0
BattleCamMenuFov = 65.0
BattleCamJoinPos = Point3(0, -12, 13)
BattleCamJoinHpr = Vec3(0, -45, 0)
SkipMovie = 0
Tracks = TTLocalizer.BattleGlobalTracks
NPCTracks = TTLocalizer.BattleGlobalNPCTracks
TrackColors = (
 (211 / 255.0, 148 / 255.0, 255 / 255.0),
 (211 / 255.0, 35 / 255.0, 12 / 255.0),
 (79 / 255.0, 186 / 255.0, 32 / 255.0),
 (93 / 255.0, 108 / 255.0, 239 / 255.0),
 (255 / 255.0, 145 / 255.0, 66 / 255.0),
 (255 / 255.0, 65 / 255.0, 199 / 255.0),
 (67 / 255.0, 243 / 255.0, 255 / 255.0)
)
HEAL_TRACK = 0
TRAP_TRACK = 1
LURE_TRACK = 2
SOUND_TRACK = 3
THROW_TRACK = 4
SQUIRT_TRACK = 5
DROP_TRACK = 6
NPC_RESTOCK_GAGS = 7
NPC_TOONS_HIT = 8
NPC_COGS_MISS = 9
NPC_ORGANIC_GAGS = 10
NPC_DOODLES_POWER = 11
NPC_BONUS_POWER = 12
MIN_TRACK_INDEX = 0
MAX_TRACK_INDEX = 6
MIN_LEVEL_INDEX = 0
MAX_LEVEL_INDEX = 6
LAST_REGULAR_GAG_LEVEL = 5
UBER_GAG_LEVEL_INDEX = 6
NUM_GAG_TRACKS = 7
PropTypeToTrackBonus = {AnimPropTypes.Hydrant: SQUIRT_TRACK,
 AnimPropTypes.Mailbox: THROW_TRACK,
 AnimPropTypes.Trashcan: HEAL_TRACK}
Levels = [
 [0, 10, 100, 500, 1500, 4500, 7500],
 [0, 10, 100, 500, 1500, 4500, 7500],
 [0, 10, 100, 500, 1500, 4500, 7500],
 [0, 10, 100, 500, 1500, 4500, 7500],
 [0, 10, 100, 500, 1500, 4500, 7500],
 [0, 10, 100, 500, 1500, 4500, 7500],
 [0, 10, 100, 500, 1500, 4500, 7500]
]
regMaxSkill = 7500
MaxSkill = regMaxSkill
ExperienceCap = 500

MaxToonAcc = 95
StartingLevel = 0
CarryLimits = (
  ( # Toon-Up
    (10, 0, 0, 0, 0, 0, 0),
    (10, 5, 0, 0, 0, 0, 0),
    (15, 10, 5, 0, 0, 0, 0),
    (20, 15, 10, 5, 0, 0, 0),
    (25, 20, 15, 10, 3, 0, 0),
    (30, 25, 20, 15, 7, 3, 0),
    (30, 25, 20, 15, 9, 5, 1)
  ),
  ( # Trap
    (10, 0, 0, 0, 0, 0, 0),
    (10, 5, 0, 0, 0, 0, 0),
    (15, 10, 5, 0, 0, 0, 0),
    (20, 15, 10, 5, 0, 0, 0),
    (25, 20, 15, 10, 3, 0, 0),
    (30, 25, 20, 15, 7, 3, 0),
    (30, 25, 20, 15, 9, 5, 1)
  ),
  ( # Lure
    (10, 0, 0, 0, 0, 0, 0),
    (10, 5, 0, 0, 0, 0, 0),
    (15, 10, 5, 0, 0, 0, 0),
    (20, 15, 10, 5, 0, 0, 0),
    (25, 20, 15, 10, 3, 0, 0),
    (30, 25, 20, 15, 7, 3, 0),
    (30, 25, 20, 15, 9, 5, 1)
  ),
  ( # Sound
    (10, 0, 0, 0, 0, 0, 0),
    (10, 5, 0, 0, 0, 0, 0),
    (15, 10, 5, 0, 0, 0, 0),
    (20, 15, 10, 5, 0, 0, 0),
    (25, 20, 15, 10, 3, 0, 0),
    (30, 25, 20, 15, 7, 3, 0),
    (30, 25, 20, 15, 7, 3, 1)
  ),
  ( # Throw
    (10, 0, 0, 0, 0, 0, 0),
    (10, 5, 0, 0, 0, 0, 0),
    (15, 10, 5, 0, 0, 0, 0),
    (20, 15, 10, 5, 0, 0, 0),
    (25, 20, 15, 10, 3, 0, 0),
    (30, 25, 20, 15, 7, 3, 0),
    (30, 25, 20, 15, 9, 5, 1)
  ),
  ( # Squirt
    (10, 0, 0, 0, 0, 0, 0),
    (10, 5, 0, 0, 0, 0, 0),
    (15, 10, 5, 0, 0, 0, 0),
    (20, 15, 10, 5, 0, 0, 0),
    (25, 20, 15, 10, 3, 0, 0),
    (30, 25, 20, 15, 7, 3, 0),
    (30, 25, 20, 15, 9, 5, 1)
  ),
  ( # Drop
    (10, 0, 0, 0, 0, 0, 0),
    (10, 5, 0, 0, 0, 0, 0),
    (15, 10, 5, 0, 0, 0, 0),
    (20, 15, 10, 5, 0, 0, 0),
    (25, 20, 15, 10, 3, 0, 0),
    (30, 25, 20, 15, 7, 3, 0),
    (30, 25, 20, 15, 9, 5, 1)
  )
)
MaxProps = ((15, 40), (30, 60), (75, 80))
DLF_SKELECOG = 1
DLF_FOREMAN = 2
DLF_BOSS = 4
DLF_SUPERVISOR = 8
DLF_VIRTUAL = 16
DLF_REVIVES = 32
DLF_EXECUTIVE = 64
pieNames = ['tart', 'fruitpie-slice', 'creampie-slice', 'fruitpie', 'creampie', 'birthday-cake', 'wedding-cake', 'lawbook']
AvProps = (
 ('feather', 'bullhorn', 'lipstick', 'bamboocane', 'pixiedust', 'baton', 'baton'),
 ('banana', 'rake', 'marbles', 'quicksand', 'trapdoor', 'tnt', 'traintrack'),
 ('1dollar', 'smmagnet', '5dollar', 'bigmagnet', '10dollar', 'hypnogogs', 'hypnogogs'),
 ('bikehorn', 'whistle', 'bugle', 'aoogah', 'elephant', 'foghorn', 'singing'),
 ('cupcake', 'fruitpieslice', 'creampieslice', 'fruitpie', 'creampie', 'cake', 'cake'),
 ('flower', 'waterglass', 'waterballoon', 'bottle', 'firehose', 'stormcloud', 'stormcloud'),
 ('flowerpot', 'sandbag', 'anvil', 'weight', 'safe', 'piano', 'piano')
)
AvPropsNew = (
 ('inventory_feather', 'inventory_megaphone', 'inventory_lipstick', 'inventory_bamboo_cane', 'inventory_pixiedust', 'inventory_juggling_cubes', 'inventory_ladder'),
 ('inventory_bannana_peel', 'inventory_rake', 'inventory_marbles', 'inventory_quicksand_icon', 'inventory_trapdoor', 'inventory_tnt', 'inventory_traintracks'),
 ('inventory_1dollarbill', 'inventory_small_magnet', 'inventory_5dollarbill', 'inventory_big_magnet', 'inventory_10dollarbill', 'inventory_hypno_goggles', 'inventory_screen'),
 ('inventory_bikehorn', 'inventory_whistle', 'inventory_bugle', 'inventory_aoogah', 'inventory_elephant', 'inventory_fog_horn', 'inventory_opera_singer'),
 ('inventory_tart', 'inventory_fruit_pie_slice', 'inventory_cream_pie_slice', 'inventory_fruitpie', 'inventory_creampie', 'inventory_cake', 'inventory_wedding'),
 ('inventory_squirt_flower', 'inventory_glass_of_water', 'inventory_water_gun', 'inventory_seltzer_bottle', 'inventory_firehose', 'inventory_storm_cloud', 'inventory_geyser'),
 ('inventory_flower_pot', 'inventory_sandbag', 'inventory_anvil', 'inventory_weight', 'inventory_safe_box', 'inventory_piano', 'inventory_ship')
)
AvPropStrings = TTLocalizer.BattleGlobalAvPropStrings
AvPropStringsSingular = TTLocalizer.BattleGlobalAvPropStringsSingular
AvPropStringsPlural = TTLocalizer.BattleGlobalAvPropStringsPlural
AvPropAccuracy = (
 (70, 70, 70, 70, 70, 70, 100), # Toon-up
 (100, 100, 100, 100, 100, 100, 100), # Trap
 (50, 50, 60, 60, 70, 70, 90), # Lure
 (85, 85, 85, 85, 85, 85, 85), # Sound
 (75, 75, 75, 75, 75, 75, 75), # Throw
 (95, 95, 95, 95, 95, 95, 95), # Squirt
 (55, 55, 55, 55, 55, 55, 60) # Drop
)
AvLureBonusAccuracy = (60, 60, 70, 70, 80, 80, 100)
AvPropDamage = (
 ( # Toon-up
  ((8, 10), (Levels[0][0], Levels[0][1])),
  ((15, 18), (Levels[0][1], Levels[0][2])),
  ((25, 30), (Levels[0][2], Levels[0][3])),
  ((40, 45), (Levels[0][3], Levels[0][4])),
  ((60, 70), (Levels[0][4], Levels[0][5])),
  ((90, 120), (Levels[0][5], Levels[0][6])),
  ((210, 210), (Levels[0][6], MaxSkill))
 ),
 ( # Trap
  ((10, 20), (Levels[1][0], Levels[1][1])),
  ((25, 30), (Levels[1][1], Levels[1][2])),
  ((40, 45), (Levels[1][2], Levels[1][3])),
  ((55, 60), (Levels[1][3], Levels[1][4])),
  ((65, 90), (Levels[1][4], Levels[1][5])),
  ((110, 200), (Levels[1][5], Levels[1][6])),
  ((240, 240), (Levels[1][6], MaxSkill))
 ),
 ( # Lure
  ((0, 0), (0, 0)),
  ((0, 0), (0, 0)),
  ((0, 0), (0, 0)),
  ((0, 0), (0, 0)),
  ((0, 0), (0, 0)),
  ((0, 0), (0, 0)),
  ((0, 0), (0, 0))
 ),
 ( # Sound
  ((3, 4), (Levels[3][0], Levels[3][1])),
  ((5, 7), (Levels[3][1], Levels[3][2])),
  ((9, 11), (Levels[3][2], Levels[3][3])),
  ((14, 16), (Levels[3][3], Levels[3][4])),
  ((19, 21), (Levels[3][4], Levels[3][5])),
  ((25, 50), (Levels[3][5], Levels[3][6])),
  ((90, 90), (Levels[3][6], MaxSkill))
 ),
 ( # Throw
  ((4, 6), (Levels[4][0], Levels[4][1])),
  ((8, 10), (Levels[4][1], Levels[4][2])),
  ((14, 17), (Levels[4][2], Levels[4][3])),
  ((24, 27), (Levels[4][3], Levels[4][4])),
  ((36, 40), (Levels[4][4], Levels[4][5])),
  ((48, 100), (Levels[4][5], Levels[4][6])),
  ((120, 120), (Levels[4][6], MaxSkill))
 ),
 ( # Squirt
  ((3, 4), (Levels[5][0], Levels[5][1])),
  ((6, 8), (Levels[5][1], Levels[5][2])),
  ((10, 12), (Levels[5][2], Levels[5][3])),
  ((18, 21), (Levels[5][3], Levels[5][4])),
  ((27, 30), (Levels[5][4], Levels[5][5])),
  ((36, 80), (Levels[5][5], Levels[5][6])),
  ((105, 105), (Levels[5][6], MaxSkill))
 ),
 ( # Drop
  ((10, 10), (Levels[6][0], Levels[6][1])),
  ((18, 18), (Levels[6][1], Levels[6][2])),
  ((30, 30), (Levels[6][2], Levels[6][3])),
  ((45, 45), (Levels[6][3], Levels[6][4])),
  ((60, 60), (Levels[6][4], Levels[6][5])),
  ((80, 170), (Levels[6][5], Levels[6][6])),
  ((195, 195), (Levels[6][6], MaxSkill))
 )
)
ATK_SINGLE_TARGET = 0
ATK_GROUP_TARGET = 1
AvPropTargetCat = (
 (ATK_SINGLE_TARGET, ATK_GROUP_TARGET, ATK_SINGLE_TARGET, ATK_GROUP_TARGET, ATK_SINGLE_TARGET, ATK_GROUP_TARGET, ATK_GROUP_TARGET),
 (ATK_SINGLE_TARGET, ATK_SINGLE_TARGET, ATK_SINGLE_TARGET, ATK_SINGLE_TARGET, ATK_SINGLE_TARGET, ATK_SINGLE_TARGET, ATK_SINGLE_TARGET),
 (ATK_GROUP_TARGET, ATK_GROUP_TARGET, ATK_GROUP_TARGET, ATK_GROUP_TARGET, ATK_GROUP_TARGET, ATK_GROUP_TARGET, ATK_GROUP_TARGET),
 (ATK_SINGLE_TARGET, ATK_SINGLE_TARGET, ATK_SINGLE_TARGET, ATK_SINGLE_TARGET, ATK_SINGLE_TARGET, ATK_SINGLE_TARGET, ATK_GROUP_TARGET)
)
AvPropTarget = (0, 3, 0, 2, 3, 3, 3)
NumRoundsLured = [2, 2, 3, 3, 4, 4, 12]

def getAvPropDamage(attackTrack, attackLevel, exp, organicBonus = False, propBonus = False, propAndOrganicBonusStack = False):
    if attackTrack == LURE_TRACK:
        return NumRoundsLured[attackLevel]
    minD = AvPropDamage[attackTrack][attackLevel][0][0]
    maxD = AvPropDamage[attackTrack][attackLevel][0][1]
    minE = AvPropDamage[attackTrack][attackLevel][1][0]
    maxE = AvPropDamage[attackTrack][attackLevel][1][1]
    expVal = min(exp, maxE)
    expPerHp = float(maxE - minE + 1) / float(maxD - minD + 1)
    damage = math.floor((expVal - minE) / expPerHp) + minD
    if damage <= 0:
        damage = minD
    if propAndOrganicBonusStack:
        originalDamage = damage
        if organicBonus:
            damage += getDamageBonus(originalDamage)
        if propBonus:
            damage += getDamageBonus(originalDamage)
    elif organicBonus or propBonus:
        damage += getDamageBonus(damage)
    return damage


def getDamageBonus(normal):
    bonus = int(normal * 0.1)
    if bonus < 1 and normal > 0:
        bonus = 1
    return bonus


def isGroup(track, level):
    return AvPropTargetCat[AvPropTarget[track]][level]


def getCreditMultiplier(floorIndex):
    return 1 + floorIndex * 0.5


def getFactoryCreditMultiplier(factoryId, difficulty=DistrictGlobals.DIFFICULTY_NORMAL):
    if factoryId == SellbotMegaCorpInt:
        return 6.0
    if difficulty == DistrictGlobals.DIFFICULTY_HARD:
        return 5.0
    elif difficulty == DistrictGlobals.DIFFICULTY_EXTREME:
        return 7.0
    return 2.0


def getFactoryMeritMultiplier(factoryId):
    return 4.0


def getMintCreditMultiplier(mintId):
    return {CashbotMintIntA: 2.0,
     CashbotMintIntB: 2.5,
     CashbotMintIntC: 3.0}.get(mintId, 1.0)


def getStageCreditMultiplier(floor):
    return getCreditMultiplier(floor)


def getCountryClubCreditMultiplier(countryClubId):
    return {BossbotCountryClubIntA: 2.5,
     BossbotCountryClubIntB: 3.5,
     BossbotCountryClubIntC: 4.5}.get(countryClubId, 1.0)


def getBossBattleCreditMultiplier(battleNumber):
    return 1 + battleNumber


def getInvasionMultiplier():
    return 2.0

def getMoreXpHolidayMultiplier():
    return 2.0

def getMoreXpHolidayAndInvasionMultiplier():
    return 3.0


