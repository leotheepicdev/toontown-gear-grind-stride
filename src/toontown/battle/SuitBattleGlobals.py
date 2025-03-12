from BattleBase import *
import random, math
from direct.directnotify import DirectNotifyGlobal
from otp.otpbase import OTPLocalizer
from toontown.base import TTLocalizer
notify = DirectNotifyGlobal.directNotify.newCategory('SuitBattleGlobals')
debugAttackSequence = {}

# ATTACKS FREQ SHOULD REALLY JUST BE REDONE, BUT WE PUT A TEMP THING FOR NOW
# COG ATTACK DAMAGE SHOULD REALLY BE READJUSTED 

def getDefaultCogHP(level):
    if level >= 1 and level <= 11:
        return (level + 1) * (level + 2)
    elif level == 12:
        return 200
    else:
        return 200 + ((level - 12) * 10)
        
def getAttackDamage(attack, level):
    if level >= 1 and level <= 12:
        return attack[level-1]
    else:
        if attack[11] == 0:
            return attack[11]
        else:
            return attack[11] + (level - 12)
    
def getSuitACCDefense(tier, level, bonus=0):
    accDef = int(tier * 5 + (level * 5))
    if accDef > 55:
        accDef = 55
    elif accDef <= 0:
        accDef = 2
    accDef += bonus
    return accDef
    
def getAttackAccuracy(acc, level):
    if level >= 1 and level <= 12:
        return acc[level-1]
    else:
        return acc[11]

def pickFromFreqList(freqList):
    randNum = random.randint(0, 99)
    count = 0
    index = 0
    level = None
    for f in freqList:
        count = count + f
        if randNum < count:
            level = index
            break
        index = index + 1
    return level

def getActualFromRelativeLevel(name, relLevel):
    data = SuitAttributes[name]
    actualLevel = data['level'] + relLevel
    return actualLevel

def pickSuitAttack(attacks, suitLevel):
    randNum = random.randint(0, 99)
    notify.debug('pickSuitAttack: rolled %d' % randNum)
    count = 0
    for i, c in enumerate(attacks):
        count += c[3]
        if randNum < count:
            return i
    return 0

def getSuitAttack(suitName, suitLevel, attackNum = -1): # TODO
    attackChoices = SuitAttributes[suitName]['attacks']
    if attackNum == -1:
        notify.debug('getSuitAttack: picking attacking for %s' % suitName)
        attackNum = pickSuitAttack(attackChoices, suitLevel)
    attack = attackChoices[attackNum]
    adict = {}
    adict['suitName'] = suitName
    name = attack[0]
    adict['name'] = name
    adict['id'] = SuitAttacks.keys().index(name)
    adict['animName'] = SuitAttacks[name][0]
    adict['hp'] = getAttackDamage(attack[1], suitLevel)
    adict['acc'] = getAttackAccuracy(attack[2], suitLevel)
    adict['freq'] = attack[3]
    adict['group'] = SuitAttacks[name][1]
    return adict

SuitAttributes = {'f': {'name': TTLocalizer.SuitFlunky,
       'singularname': TTLocalizer.SuitFlunkyS,
       'pluralname': TTLocalizer.SuitFlunkyP,
       'level': 0,
       'attacks': (('PoundKey',
                    (2, 2, 3, 4, 5, 5, 6, 7, 8, 8, 9, 10),
                    (75, 75, 80, 80, 80, 85, 85, 90, 90, 90, 90, 90),
                    (30)),
                   ('Shred',
                    (3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14),
                    (50, 55, 60, 65, 70, 70, 70, 75, 75, 75, 80, 80),
                    (20)),
                   ('ClipOnTie',
                    (1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6),
                    (75, 80, 85, 85, 90, 90, 90, 90, 90, 90, 90, 95),
                    (50)))},
 'p': {'name': TTLocalizer.SuitPencilPusher,
       'singularname': TTLocalizer.SuitPencilPusherS,
       'pluralname': TTLocalizer.SuitPencilPusherP,
       'level': 1,
       'attacks': (('FountainPen',
                    (2, 3, 4, 6, 9, 10, 11, 12, 13, 15, 16, 17),
                    (75, 75, 75, 75, 75, 75, 75, 75, 75, 75, 80, 80),
                    (20)),
                   ('RubOut',
                    (4, 5, 6, 8, 12, 13, 14, 15, 16, 17, 18, 19),
                    (75, 75, 75, 75, 75, 75, 75, 75, 75, 75, 75, 75),
                    (20)),
                   ('FingerWag',
                    (1, 2, 2, 3, 4, 4, 5, 6, 6, 7, 8, 8),
                    (85, 85, 85, 85, 90, 90, 90, 90, 95, 95, 95, 95),
                    (20)),
                   ('WriteOff',
                    (2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24),
                    (75, 75, 75, 75, 75, 75, 75, 75, 75, 75, 75, 75),
                    (15)),
                   ('FillWithLead',
                    (4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26),
                    (70, 70, 70, 70, 70, 70, 70, 70, 70, 70, 70, 70),
                    (25)))},
 'ym': {'name': TTLocalizer.SuitYesman,
        'singularname': TTLocalizer.SuitYesmanS,
        'pluralname': TTLocalizer.SuitYesmanP,
        'level': 2,
        'attacks': (('RubberStamp',
                     (3, 5, 6, 8, 9, 11, 12, 14, 15, 17, 19, 20),
                     (70, 70, 75, 75, 80, 80, 85, 85, 90, 90, 90, 90),
                     (30)),
                    ('RazzleDazzle',
                     (2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24),
                     (60, 65, 70, 75, 80, 80, 80, 80, 85, 85, 85, 85),
                     (25)),
                    ('Synergy',
                     (4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26),
                     (50, 55, 60, 65, 70, 75, 80, 80, 80, 80, 80, 80),
                     (15)),
                    ('TeeOff',
                     (1, 3, 4, 6, 7, 9, 10, 12, 13, 15, 16, 18),
                     (80, 80, 80, 80, 85, 85, 85, 85, 90, 90, 90, 90),
                     (30)))},
 'mm': {'name': TTLocalizer.SuitMicromanager,
        'singularname': TTLocalizer.SuitMicromanagerS,
        'pluralname': TTLocalizer.SuitMicromanagerP,
        'level': 3,
        'attacks': (('Demotion',
                     (2, 4, 8, 12, 15, 18, 20, 22, 24, 26, 28, 30),
                     (50, 55, 60, 65, 70, 70, 75, 75, 80, 80, 85, 85),
                     (30)),
                    ('FingerWag',
                     (1, 2, 4, 6, 9, 12, 15, 16, 17, 18, 19, 20),
                     (50, 55, 60, 65, 70, 75, 80, 85, 90, 90, 90, 95),
                     (10)),
                    ('FountainPen',
                     (1, 2, 3, 4, 6, 8, 10, 12, 13, 14, 15, 16),
                     (75, 75, 75, 75, 80, 80, 85, 85, 90, 90, 95, 95),
                     (15)),
                    ('BrainStorm',
                     (1, 3, 6, 8, 11, 13, 16, 18, 21, 23, 26, 28),
                     (50, 60, 60, 70, 70, 70, 75, 75, 80, 85, 85, 90),
                     (25)),
                    ('BuzzWord',
                     (2, 3, 5, 6, 8, 9, 11, 12, 14, 15, 17, 18),
                     (65, 65, 70, 70, 75, 75, 75, 75, 80, 85, 90, 95),
                     (20)))},
 'ds': {'name': TTLocalizer.SuitDownsizer,
        'singularname': TTLocalizer.SuitDownsizerS,
        'pluralname': TTLocalizer.SuitDownsizerP,
        'level': 4,
        'attacks': (('Canned',
                     (2, 3, 5, 6, 8, 9, 11, 12, 14, 15, 17, 18),
                     (75, 75, 75, 75, 80, 80, 85, 85, 90, 90, 95, 95),
                     (25)),
                    ('Downsize',
                     (3, 5, 8, 10, 12, 15, 17, 19, 22, 24, 26, 29),
                     (55, 60, 60, 65, 65, 65, 70, 70, 75, 75, 80, 80),
                     (35)),
                    ('PinkSlip',
                     (2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24),
                     (60, 65, 70, 70, 75, 75, 80, 80, 85, 85, 90, 90),
                     (25)),
                    ('Sacked',
                     (3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25),
                     (60, 65, 70, 70, 75, 75, 80, 80, 85, 85, 90, 90),
                     (15)))},
 'hh': {'name': TTLocalizer.SuitHeadHunter,
        'singularname': TTLocalizer.SuitHeadHunterS,
        'pluralname': TTLocalizer.SuitHeadHunterP,
        'level': 5,
        'attacks': (('FountainPen',
                     (2, 3, 5, 6, 8, 9, 11, 12, 14, 15, 17, 18),
                     (75, 75, 75, 75, 80, 80, 85, 85, 90, 90, 90, 90),
                     (15)),
                    ('GlowerPower',
                     (3, 4, 6, 7, 9, 10, 12, 13, 15, 16, 18, 19),
                     (75, 75, 75, 75, 80, 80, 85, 85, 90, 90, 90, 90),
                     (20)),
                    ('HalfWindsor',
                     (2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24),
                     (70, 70, 70, 70, 75, 75, 75, 75, 80, 80, 80, 85),
                     (20)),
                    ('HeadShrink',
                     (4, 6, 8, 10, 12, 14, 16, 18, 21, 24, 27, 30),
                     (65, 65, 65, 70, 70, 70, 75, 75, 75, 80, 80, 85),
                     (20)),
                    ('ReOrg',
                     (2, 2, 5, 5, 8, 8, 11, 11, 14, 14, 17, 17),
                     (95, 95, 95, 95, 95, 95, 95, 95, 95, 95, 95, 95),
                     (15)),
                    ('Rolodex',
                     (2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24),
                     (70, 70, 70, 70, 75, 75, 75, 75, 80, 80, 80, 85),
                     (10)))},
 'cr': {'name': TTLocalizer.SuitCorporateRaider,
        'singularname': TTLocalizer.SuitCorporateRaiderS,
        'pluralname': TTLocalizer.SuitCorporateRaiderP,
        'level': 6,
        'attacks': (('Canned',
                     (3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25),
                     (65, 70, 70, 75, 80, 80, 80, 80, 85, 85, 90, 90),
                     (20)),
                    ('EvilEye',
                     (5, 8, 10, 13, 15, 18, 20, 23, 25, 28, 30, 33),
                     (60, 65, 70, 70, 75, 75, 75, 75, 80, 80, 80, 80),
                     (35)),
                    ('PlayHardball',
                     (3, 6, 8, 11, 13, 16, 18, 21, 23, 26, 28, 31),
                     (60, 65, 70, 70, 75, 75, 75, 75, 80, 80, 85, 85),
                     (30)),
                    ('PowerTie',
                     (2, 4, 7, 10, 12, 14, 17, 20, 22, 24, 27, 30),
                     (60, 65, 70, 70, 75, 75, 75, 75, 80, 80, 85, 85),
                     (15)))},
 'tbc': {'name': TTLocalizer.SuitTheBigCheese,
         'singularname': TTLocalizer.SuitTheBigCheeseS,
         'pluralname': TTLocalizer.SuitTheBigCheeseP,
         'level': 7,
         'attacks': (('CigarSmoke',
                      (4, 6, 8, 12, 14, 16, 18, 22, 24, 26, 28, 32),
                      (60, 60, 60, 65, 65, 65, 65, 70, 70, 70, 70, 75),
                      (20)),
                     ('PowerTrip',
                      (3, 5, 7, 9, 12, 15, 18, 21, 24, 27, 30, 33),
                      (70, 70, 70, 70, 75, 75, 75, 75, 80, 80, 80, 80),
                      (10)),
                     ('SongAndDance',
                      (3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25),
                      (70, 70, 70, 75, 75, 75, 80, 80, 80, 85, 90, 95),
                      (20)),
                     ('TeeOff',
                      (3, 4, 7, 8, 11, 12, 15, 16, 19, 20, 23, 24),
                      (70, 70, 70, 70, 75, 75, 75, 75, 80, 85, 90, 95),
                      (50)))},
 'cc': {'name': TTLocalizer.SuitColdCaller,
        'singularname': TTLocalizer.SuitColdCallerS,
        'pluralname': TTLocalizer.SuitColdCallerP,
        'level': 0,
        'attacks': (('FreezeAssets',
                     (4, 5, 7, 8, 10, 11, 13, 14, 16, 17, 19, 20),
                     (80, 80, 80, 80, 85, 85, 85, 85, 90, 90, 90, 90),
                     (30)),
                    ('PoundKey',
                     (1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7),
                     (95, 95, 95, 95, 95, 95, 95, 95, 95, 95, 95, 95),
                     (15)),
                    ('DoubleTalk',
                     (2, 2, 4, 4, 6, 6, 8, 8, 10, 10, 12, 12),
                     (95, 95, 95, 95, 95, 95, 95, 95, 95, 95, 95, 95),
                     (20)),
                    ('HotAir',
                     (2, 3, 5, 6, 8, 9, 11, 12, 14, 15, 17, 18),
                     (85, 85, 85, 85, 90, 90, 90, 90, 95, 95, 95, 95),
                     (35)))},
 'tm': {'name': TTLocalizer.SuitTelemarketer,
        'singularname': TTLocalizer.SuitTelemarketerS,
        'pluralname': TTLocalizer.SuitTelemarketerP,
        'level': 1,
        'attacks': (('ClipOnTie',
                     (2, 2, 3, 3, 4, 5, 6, 7, 8, 9, 10, 11),
                     (75, 75, 75, 75, 80, 80, 80, 80, 85, 85, 85, 85),
                     (15)),
                    ('PickPocket',
                     (2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13),
                     (75, 75, 75, 75, 80, 80, 80, 80, 85, 85, 85, 85),
                     (15)),
                    ('Rolodex',
                     (3, 4, 6, 7, 9, 12, 14, 15, 17, 18, 20, 21),
                     (65, 65, 65, 65, 70, 70, 70, 70, 75, 75, 75, 75),
                     (30)),
                    ('DoubleTalk',
                     (3, 4, 6, 7, 9, 12, 14, 15, 17, 18, 20, 21),
                     (75, 75, 75, 75, 80, 80, 85, 85, 90, 90, 90, 90),
                     (40)))},
 'nd': {'name': TTLocalizer.SuitNameDropper,
        'singularname': TTLocalizer.SuitNameDropperS,
        'pluralname': TTLocalizer.SuitNameDropperP,
        'level': 2,
        'attacks': (('RazzleDazzle',
                     (2, 3, 5, 6, 9, 12, 13, 15, 17, 18, 21, 22),
                     (75, 80, 80, 80, 85, 85, 85, 85, 85, 85, 85, 85),
                     (25)),
                    ('Rolodex',
                     (3, 5, 6, 9, 12, 14, 15, 17, 20, 21, 23, 25),
                     (65, 65, 70, 70, 75, 75, 75, 75, 80, 80, 80, 85),
                     (30)),
                    ('DropAnvil',
                     (1, 2, 4, 6, 7, 9, 10, 12, 13, 15, 16, 18),
                     (95, 95, 95, 95, 95, 95, 95, 95, 95, 95, 95, 95),
                     (15)),
                    ('Synergy',
                     (1, 2, 4, 6, 7, 9, 10, 12, 13, 15, 16, 18),
                     (60, 60, 65, 65, 70, 70, 70, 70, 75, 75, 80, 80),
                     (15)),
                    ('PickPocket',
                     (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12),
                     (95, 95, 95, 95, 95, 95, 95, 95, 95, 95, 95, 95),
                     (15)))},
 'gh': {'name': TTLocalizer.SuitGladHander,
        'singularname': TTLocalizer.SuitGladHanderS,
        'pluralname': TTLocalizer.SuitGladHanderP,
        'level': 3,
        'attacks': (('RubberStamp',
                     (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12),
                     (95, 95, 95, 95, 95, 95, 95, 95, 95, 95, 95, 95),
                     (10)),
                    ('FountainPen',
                     (3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14),
                     (90, 90, 90, 90, 90, 90, 90, 90, 90, 90, 90, 90),
                     (10)),
                    ('Filibuster',
                     (1, 2, 4, 6, 10, 14, 16, 18, 20, 22, 24, 26),
                     (65, 70, 70, 75, 80, 80, 85, 85, 90, 90, 95, 95),
                     (30)),
                    ('Barrier',
                     (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
                     (100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100),
                     (20)),
                    ('Schmooze',
                     (3, 4, 6, 8, 12, 16, 18, 20, 22, 24, 26, 28),
                     (65, 70, 70, 75, 80, 80, 85, 85, 90, 90, 95, 95),
                     (30)))},
 'ms': {'name': TTLocalizer.SuitMoverShaker,
        'singularname': TTLocalizer.SuitMoverShakerS,
        'pluralname': TTLocalizer.SuitMoverShakerP,
        'level': 4,
        'attacks': (('BrainStorm',
                     (1, 2, 4, 6, 7, 8, 10, 12, 13, 14, 16, 18),
                     (85, 85, 85, 85, 90, 90, 90, 90, 95, 95, 95, 95),
                     (15)),
                    ('HalfWindsor',
                     (1, 3, 4, 5, 7, 8, 10, 11, 13, 14, 16, 17),
                     (80, 80, 80, 80, 85, 85, 85, 85, 90, 90, 90, 90),
                     (20)),
                    ('Quake',
                     (4, 6, 8, 10, 12, 15, 18, 21, 24, 27, 30, 33),
                     (60, 60, 65, 65, 70, 70, 75, 75, 80, 80, 85, 85),
                     (20)),
                    ('Shake',
                     (2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24),
                     (70, 70, 75, 75, 80, 80, 85, 85, 90, 90, 90, 90),
                     (25)),
                    ('Tremor',
                     (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12),
                     (95, 95, 95, 95, 95, 95, 95, 95, 95, 95, 95, 95),
                     (20)))},
 'tf': {'name': TTLocalizer.SuitTwoFace,
        'singularname': TTLocalizer.SuitTwoFaceS,
        'pluralname': TTLocalizer.SuitTwoFaceP,
        'level': 5,
        'attacks': (('EvilEye',
                     (3, 5, 6, 8, 10, 12, 14, 16, 18, 20, 22, 25),
                     (75, 75, 75, 75, 80, 80, 80, 80, 85, 85, 85, 85),
                     (25)),
                    ('HangUp',
                     (1, 3, 4, 6, 7, 9, 10, 12, 13, 15, 16, 18),
                     (85, 85, 85, 85, 90, 90, 90, 90, 95, 95, 95, 95),
                     (15)),
                    ('RazzleDazzle',
                     (2, 4, 6, 8, 10, 12, 14, 15, 18, 20, 22, 24),
                     (75, 75, 75, 75, 80, 80, 80, 80, 85, 85, 85, 85),
                     (25)),
                    ('ReOrg',
                     (3, 5, 7, 9, 11, 13, 15, 16, 19, 21, 23, 25),
                     (75, 75, 75, 75, 80, 80, 80, 80, 85, 85, 85, 85),
                     (15)),
                    ('RedTape',
                     (2, 3, 4, 5, 7, 9, 11, 13, 15, 17, 19, 21),
                     (75, 75, 75, 75, 80, 80, 80, 80, 85, 85, 85, 85),
                     (20)))},
 'm': {'name': TTLocalizer.SuitTheMingler,
       'singularname': TTLocalizer.SuitTheMinglerS,
       'pluralname': TTLocalizer.SuitTheMinglerP,
       'level': 6,
       'attacks': (('BuzzWord',
                    (1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23),
                    (70, 70, 70, 70, 75, 75, 75, 75, 80, 80, 85, 85),
                    (20)),
                   ('ParadigmShift',
                    (4, 6, 8, 11, 13, 15, 18, 20, 22, 25, 27, 29),
                    (65, 65, 65, 65, 70, 70, 70, 70, 75, 75, 75, 75),
                    (20)),
                   ('PowerTrip',
                    (2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24),
                    (65, 65, 65, 65, 70, 70, 70, 70, 75, 75, 75, 75),
                    (15)),
                   ('Schmooze',
                    (1, 2, 5, 6, 7, 10, 11, 12, 15, 16, 17, 20),
                    (85, 85, 85, 85, 90, 90, 90, 90, 95, 95, 95, 95),
                    (20)),
                   ('CigarSmoke',
                    (2, 3, 6, 7, 8, 11, 12, 13, 16, 17, 18, 21),
                    (85, 85, 85, 85, 90, 90, 90, 90, 95, 95, 95, 95),
                    (15)),
                   ('TeeOff',
                    (2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13),
                    (95, 95, 95, 95, 95, 95, 95, 95, 95, 95, 95, 95),
                    (10)))},
 'mh': {'name': TTLocalizer.SuitMrHollywood,
        'singularname': TTLocalizer.SuitMrHollywoodS,
        'pluralname': TTLocalizer.SuitMrHollywoodP,
        'level': 7,
        'attacks': (('PowerTrip',
                     (1, 2, 5, 7, 10, 12, 15, 18, 20, 23, 25, 28),
                     (60, 60, 60, 65, 70, 70, 70, 70, 75, 75, 75, 80),
                     (40)),
                    ('SongAndDance',
                     (3, 5, 8, 10, 12, 15, 18, 21, 24, 27, 30, 33),
                     (75, 75, 75, 75, 80, 80, 80, 80, 85, 85, 90, 90),
                     (30)),
                    ('RazzleDazzle',
                     (2, 4, 5, 7, 9, 12, 15, 18, 21, 24, 27, 30),
                     (75, 75, 75, 75, 80, 80, 80, 80, 85, 85, 90, 90),
                     (30)))},
 'sc': {'name': TTLocalizer.SuitShortChange,
        'singularname': TTLocalizer.SuitShortChangeS,
        'pluralname': TTLocalizer.SuitShortChangeP,
        'level': 0,
        'attacks': (('Watercooler',
                     (2, 2, 3, 4, 5, 6, 7, 9, 10, 12, 14, 15),
                     (85, 85, 85, 85, 90, 90, 90, 90, 90, 90, 90, 90),
                     (20)),
                    ('BounceCheck',
                     (3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25),
                     (75, 75, 75, 75, 80, 80, 80, 80, 85, 85, 85, 85),
                     (15)),
                    ('ClipOnTie',
                     (2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7),
                     (95, 95, 95, 95, 95, 95, 95, 95, 95, 95, 95, 95),
                     (25)),
                    ('PickPocket',
                     (2, 3, 4, 6, 7, 8, 9, 11, 12, 13, 14, 16),
                     (95, 95, 95, 95, 95, 95, 95, 95, 95, 95, 95, 95),
                     (40)))},
 'pp': {'name': TTLocalizer.SuitPennyPincher,
        'singularname': TTLocalizer.SuitPennyPincherS,
        'pluralname': TTLocalizer.SuitPennyPincherP,
        'level': 1,
        'attacks': (('BounceCheck',
                     (4, 5, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24),
                     (75, 75, 75, 75, 75, 75, 75, 75, 75, 75, 75, 75),
                     (45)), 
                    ('FreezeAssets',
                     (2, 3, 4, 6, 9, 11, 13, 15, 16, 18, 20, 22),
                     (75, 75, 75, 75, 75, 75, 75, 75, 75, 75, 75, 75), 
                     (20)), 
                    ('FingerWag',
                     (1, 2, 3, 4, 6, 7, 8, 9, 11, 12, 13, 14),
                     (90, 90, 90, 90, 90, 90, 90, 90, 90, 90, 90, 90),
                     (35)))},
 'tw': {'name': TTLocalizer.SuitTightwad,
        'singularname': TTLocalizer.SuitTightwadS,
        'pluralname': TTLocalizer.SuitTightwadP,
        'level': 2,
        'attacks': (('Fired',
                     (2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13),
                     (95, 95, 95, 95, 95, 95, 95, 95, 95, 95, 95, 95),
                     (30)),
                    ('GlowerPower',
                     (3, 4, 6, 7, 9, 10, 11, 13, 14, 15, 17, 18),
                     (85, 85, 85, 85, 85, 85, 85, 85, 85, 85, 85, 85),
                     (20)),
                    ('FingerWag',
                     (3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14),
                     (95, 95, 95, 95, 95, 95, 95, 95, 95, 95, 95, 95),
                     (15)),
                    ('FreezeAssets',
                     (3, 4, 6, 9, 11, 13, 16, 18, 21, 23, 25, 27),
                     (75, 75, 75, 75, 75, 75, 75, 75, 80, 80, 80, 80),
                     (15)),
                    ('BounceCheck',
                     (4, 6, 9, 11, 13, 15, 18, 20, 22, 25, 27, 29),
                     (75, 75, 75, 75, 75, 75, 75, 75, 75, 75, 75, 75),
                     (20)))},
 'bc': {'name': TTLocalizer.SuitBeanCounter,
        'singularname': TTLocalizer.SuitBeanCounterS,
        'pluralname': TTLocalizer.SuitBeanCounterP,
        'level': 3,
        'attacks': (('Audit',
                     (2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24),
                     (95, 95, 95, 95, 95, 95, 95, 95, 95, 95, 95, 95),
                     (20)),
                    ('Calculate',
                     (2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24),
                     (75, 75, 75, 75, 75, 75, 75, 75, 75, 75, 75, 75),
                     (25)),
                    ('Tabulate',
                     (2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24),
                     (75, 75, 75, 75, 75, 75, 75, 75, 75, 75, 75, 75),
                     (25)),
                    ('WriteOff',
                     (2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24),
                     (95, 95, 95, 95, 95, 95, 95, 95, 95, 95, 95, 95),
                     (30)))},
 'nc': {'name': TTLocalizer.SuitNumberCruncher,
        'singularname': TTLocalizer.SuitNumberCruncherS,
        'pluralname': TTLocalizer.SuitNumberCruncherP,
        'level': 4,
        'attacks': (('Audit',
                     (2, 3, 5, 7, 8, 9, 11, 13, 14, 15, 17, 19),
                     (95, 95, 95, 95, 95, 95, 95, 95, 95, 95, 95, 95),
                     (15)),
                    ('Calculate',
                     (3, 4, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20),
                     (95, 95, 95, 95, 95, 95, 95, 95, 95, 95, 95, 95),
                     (20)),
                    ('Crunch',
                     (3, 5, 7, 9, 11, 13, 15, 17, 19, 23, 26, 29),
                     (75, 75, 75, 75, 80, 80, 80, 80, 85, 85, 85, 85),
                     (30)),
                    ('Synergy',
                     (5, 6, 8, 10, 11, 12, 14, 16, 17, 18, 20, 22),
                     (80, 80, 80, 80, 85, 85, 85, 85, 90, 90, 95, 95),
                     (15)),
                    ('Tabulate',
                     (1, 2, 4, 6, 7, 8, 10, 12, 13, 14, 16, 18),
                     (95, 95, 95, 95, 95, 95, 95, 95, 95, 95, 95, 95),
                     (20)))},
 'mb': {'name': TTLocalizer.SuitMoneyBags,
        'singularname': TTLocalizer.SuitMoneyBagsS,
        'pluralname': TTLocalizer.SuitMoneyBagsP,
        'level': 5,
        'attacks': (('Liquidate',
                     (1, 3, 6, 9, 12, 14, 16, 19, 22, 24, 26, 29),
                     (60, 60, 65, 65, 70, 70, 75, 75, 80, 80, 85, 85),
                     (30)), 
                    ('MarketCrash',
                     (3, 5, 8, 11, 14, 16, 18, 21, 24, 26, 28, 31),
                     (60, 60, 65, 65, 70, 70, 75, 75, 80, 80, 85, 85),
                     (45)), 
                    ('PowerTie',
                     (2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13),
                     (95, 95, 95, 95, 95, 95, 95, 95, 95, 95, 95, 95),
                     (25)))},
 'ls': {'name': TTLocalizer.SuitLoanShark,
        'singularname': TTLocalizer.SuitLoanSharkS,
        'pluralname': TTLocalizer.SuitLoanSharkP,
        'level': 6,
        'attacks': (('Bite',
                     (1, 3, 5, 7, 10, 13, 16, 19, 21, 24, 26, 28),
                     (60, 75, 80, 85, 85, 85, 85, 85, 85, 85, 85, 85),
                     (30)),
                    ('Chomp',
                     (3, 5, 7, 9, 12, 15, 18, 21, 23, 26, 28, 30),
                     (60, 75, 80, 85, 85, 85, 85, 85, 85, 85, 85, 85),
                     (35)),
                    ('ParadigmShift',
                     (2, 4, 6, 8, 10, 12, 15, 17, 20, 22, 25, 27),
                     (70, 70, 75, 75, 80, 80, 85, 85, 90, 90, 90, 90),
                     (10)),
                    ('PlayHardball',
                     (1, 3, 5, 7, 9, 11, 12, 13, 15, 16, 17, 18),
                     (80, 80, 80, 80, 85, 85, 85, 85, 90, 95, 95, 95),
                     (15)),
                    ('WriteOff',
                     (3, 5, 7, 9, 11, 13, 14, 15, 17, 18, 19, 20),
                     (80, 80, 80, 80, 85, 85, 85, 85, 90, 95, 95, 95),
                     (10)))},
 'rb': {'name': TTLocalizer.SuitRobberBaron,
        'singularname': TTLocalizer.SuitRobberBaronS,
        'pluralname': TTLocalizer.SuitRobberBaronP,
        'level': 7,
        'attacks': (('Synergy',
                     (3, 5, 7, 11, 14, 16, 18, 21, 24, 26, 28, 30),
                     (60, 60, 65, 65, 70, 70, 75, 75, 80, 80, 85, 85),
                     (20)),
                    ('CigarSmoke',
                     (2, 4, 6, 8, 10, 12, 15, 18, 20, 21, 22, 23),
                     (55, 65, 75, 85, 85, 85, 85, 85, 90, 90, 90, 90),
                     (20)),
                    ('PickPocket', 
                     (5, 7, 10, 13, 17, 20, 22, 24, 26, 28, 30, 32),
                     (65, 65, 65, 65, 70, 70, 75, 75, 80, 80, 85, 85),
                     (20)),
                    ('EvilEye', 
                     (3, 5, 8, 11, 15, 18, 20, 22, 24, 26, 28, 30),
                     (70, 70, 70, 70, 80, 80, 80, 80, 90, 90, 90, 90),
                     (20)),
                    ('TeeOff',
                     (2, 4, 6, 8, 10, 12, 14, 16, 18, 19, 20, 21),
                     (80, 80, 80, 80, 90, 90, 90, 90, 95, 95, 95, 95),
                     (20)))},
 'bf': {'name': TTLocalizer.SuitBottomFeeder,
        'singularname': TTLocalizer.SuitBottomFeederS,
        'pluralname': TTLocalizer.SuitBottomFeederP,
        'level': 0,
        'attacks': (('RubberStamp',
                     (2, 3, 4, 5, 6, 7, 9, 10, 11, 12, 13, 14),
                     (80, 80, 80, 80, 85, 85, 85, 85, 90, 90, 90, 90),
                     (20)),
                    ('Shred',
                     (2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24),
                     (55, 55, 60, 60, 65, 65, 70, 70, 75, 75, 80, 80),
                     (20)),
                    ('Watercooler',
                     (3, 4, 5, 6, 7, 8, 10, 11, 12, 13, 14, 15),
                     (95, 95, 95, 95, 95, 95, 95, 95, 95, 95, 95, 95),
                     (10)),
                    ('PickPocket',
                     (2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13),
                     (75, 75, 75, 75, 80, 80, 80, 80, 85, 85, 85, 85),
                     (50)))},
 'b': {'name': TTLocalizer.SuitBloodsucker,
       'singularname': TTLocalizer.SuitBloodsuckerS,
       'pluralname': TTLocalizer.SuitBloodsuckerP,
       'level': 1,
       'attacks': (('EvictionNotice',
                    (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12),
                    (95, 95, 95, 95, 95, 95, 95, 95, 95, 95, 95, 95),
                    (25)),
                   ('RedTape',
                    (2, 3, 4, 6, 9, 10, 12, 13, 15, 16, 18, 19),
                    (75, 75, 75, 75, 80, 80, 80, 80, 80, 80, 80, 80),
                    (20)),
                   ('Withdrawal',
                    (4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26),
                    (75, 75, 75, 75, 75, 75, 75, 75, 80, 80, 85, 85),
                    (15)),
                   ('Liquidate',
                    (1, 3, 4, 6, 7, 9, 10, 12, 13, 15, 16, 18),
                    (70, 70, 70, 70, 70, 70, 75, 75, 75, 75, 75, 75),
                    (40)))},
 'dt': {'name': TTLocalizer.SuitDoubleTalker,
        'singularname': TTLocalizer.SuitDoubleTalkerS,
        'pluralname': TTLocalizer.SuitDoubleTalkerP,
        'level': 2,
        'attacks': (('RubberStamp',
                     (2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13),
                     (75, 75, 80, 80, 85, 85, 90, 90, 95, 95, 95, 95),
                     (10)),
                    ('BounceCheck',
                     (3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14),
                     (75, 75, 80, 80, 85, 85, 90, 90, 95, 95, 95, 95),
                     (10)),
                    ('BuzzWord',
                     (1, 2, 3, 5, 6, 7, 8, 10, 11, 12, 13, 15),
                     (75, 75, 80, 80, 85, 85, 90, 90, 95, 95, 95, 95),
                     (20)),
                    ('DoubleTalk',
                     (4, 5, 8, 11, 14, 16, 19, 21, 24, 26, 28, 30),
                     (55, 60, 60, 65, 65, 70, 70, 75, 75, 75, 75, 75),
                     (25)),
                    ('Jargon',
                     (3, 4, 6, 9, 12, 13, 14, 15, 16, 17, 18, 19),
                     (60, 65, 65, 70, 70, 70, 70, 75, 80, 80, 85, 85),
                     (20)),
                    ('MumboJumbo',
                     (3, 4, 6, 9, 12, 13, 14, 15, 16, 17, 18, 19),
                     (65, 65, 70, 70, 75, 75, 75, 80, 80, 85, 90, 90),
                     (15)))},
 'ac': {'name': TTLocalizer.SuitAmbulanceChaser,
        'singularname': TTLocalizer.SuitAmbulanceChaserS,
        'pluralname': TTLocalizer.SuitAmbulanceChaserP,
        'level': 3,
        'attacks': (('Shake',
                     (2, 4, 6, 8, 10, 13, 16, 18, 20, 23, 24, 26),
                     (75, 75, 75, 75, 75, 75, 75, 75, 75, 75, 75, 75), 
                     (15)),
                    ('CogUp',
                     (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
                     (100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100),
                     (10)),
                    ('RedTape',
                     (4, 6, 8, 12, 15, 18, 19, 20, 22, 24, 26, 28),
                     (75, 75, 75, 75, 75, 75, 75, 75, 75, 75, 75, 75),
                     (20)),
                    ('Rolodex',
                     (3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14),
                     (70, 70, 70, 75, 75, 75, 80, 80, 80, 80, 80, 80),
                     (20)),
                    ('HangUp',
                     (2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13),
                     (85, 85, 85, 85, 85, 85, 85, 85, 85, 85, 85, 85),
                     (35)))},
 'bs': {'name': TTLocalizer.SuitBackStabber,
        'singularname': TTLocalizer.SuitBackStabberS,
        'pluralname': TTLocalizer.SuitBackStabberP,
        'level': 4,
        'attacks': (('GuiltTrip',
                     (3, 5, 8, 10, 12, 15, 17, 18, 20, 22, 24, 26),
                     (60, 65, 70, 70, 75, 75, 80, 80, 80, 85, 85, 85),
                     (35)), 
                    ('RestrainingOrder',
                     (3, 5, 8, 10, 12, 15, 17, 18, 20, 22, 24, 26),
                     (60, 65, 70, 70, 75, 75, 80, 80, 80, 85, 85, 85),
                     (25)), 
                    ('CigarSmoke',
                     (2, 4, 5, 7, 8, 10, 11, 13, 14, 16, 17, 19),
                     (75, 75, 75, 75, 75, 75, 85, 85, 85, 85, 85, 90),
                     (15)), 
                    ('FingerWag',
                     (2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13),
                     (70, 70, 70, 70, 75, 75, 75, 75, 80, 85, 90, 95),
                     (25)))},
 'sd': {'name': TTLocalizer.SuitSpinDoctor,
        'singularname': TTLocalizer.SuitSpinDoctorS,
        'pluralname': TTLocalizer.SuitSpinDoctorP,
        'level': 5,
        'attacks': (('ParadigmShift',
                     (3, 5, 6, 9, 11, 14, 16, 18, 20, 23, 25, 27),
                     (65, 65, 65, 70, 70, 70, 75, 75, 75, 80, 80, 85),
                     (20)),
                    ('Quake',
                     (2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24),
                     (70, 70, 75, 75, 80, 80, 85, 85, 90, 90, 90, 90),
                     (20)),
                    ('CogUp',
                     (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
                     (100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100),
                     (10)),
                    ('Spin',
                     (5, 7, 8, 11, 13, 16, 18, 20, 22, 24, 27, 29),
                     (65, 65, 65, 70, 70, 70, 75, 75, 75, 80, 85, 90),
                     (20)),
                    ('ReOrg',
                     (2, 4, 5, 8, 11, 13, 15, 18, 20, 22, 24, 26),
                     (65, 65, 70, 70, 75, 75, 80, 80, 80, 85, 85, 85), 
                     (15)),
                    ('WriteOff',
                     (2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14),
                     (90, 90, 90, 90, 90, 90, 90, 90, 90, 90, 90, 90),
                     (15)))},
 'le': {'name': TTLocalizer.SuitLegalEagle,
        'singularname': TTLocalizer.SuitLegalEagleS,
        'pluralname': TTLocalizer.SuitLegalEagleP,
        'level': 6,
        'attacks': (('EvilEye',
                     (3, 4, 6, 8, 10, 11, 13, 15, 16, 17, 18, 19), 
                     (65, 65, 70, 70, 75, 75, 80, 80, 85, 85, 85, 85),
                     (20)),
                    ('Jargon',
                     (1, 3, 5, 7, 9, 12, 14, 16, 18, 20, 22, 24),
                     (70, 70, 70, 70, 80, 80, 80, 80, 90, 90, 90, 90),
                     (15)),
                    ('Legalese',
                     (2, 4, 6, 9, 11, 13, 16, 18, 20, 22, 24, 26),
                     (65, 65, 65, 65, 70, 70, 70, 70, 75, 75, 80, 80),
                     (35)),
                    ('PeckingOrder',
                     (4, 6, 8, 10, 12, 15, 17, 19, 22, 24, 26, 29),
                     (70, 70, 70, 75, 75, 75, 80, 80, 80, 85, 85, 85),
                     (30)))},
 'bw': {'name': TTLocalizer.SuitBigWig,
        'singularname': TTLocalizer.SuitBigWigS,
        'pluralname': TTLocalizer.SuitBigWigP,
        'level': 7,
        'attacks': (('PowerTrip',
                     (2, 4, 6, 8, 11, 14, 16, 19, 22, 24, 26, 28),
                     (75, 75, 75, 75, 80, 80, 85, 85, 90, 90, 95, 95),
                     (40)),
                    ('ThrowBook',
                     (4, 6, 8, 10, 13, 16, 18, 21, 24, 26, 28, 30),
                     (70, 70, 70, 70, 80, 80, 80, 80, 90, 90, 90, 90),
                     (30)),
                    ('FingerWag',
                     (2, 3, 5, 6, 8, 9, 12, 13, 16, 17, 20, 21),
                     (80, 80, 80, 80, 80, 80, 90, 90, 90, 90, 90, 90),
                     (30)))}}
ATK_TGT_UNKNOWN = 1
ATK_TGT_SINGLE = 2
ATK_TGT_GROUP = 3
SuitAttacks = {'Audit': ('phone', ATK_TGT_SINGLE),
 'Barrier': ('effort', ATK_TGT_GROUP),
 'Bite': ('throw-paper', ATK_TGT_SINGLE),
 'BounceCheck': ('throw-paper', ATK_TGT_SINGLE),
 'BrainStorm': ('effort', ATK_TGT_SINGLE),
 'BuzzWord': ('speak', ATK_TGT_SINGLE),
 'Calculate': ('phone', ATK_TGT_SINGLE),
 'Canned': ('throw-paper', ATK_TGT_SINGLE),
 'Chomp': ('throw-paper', ATK_TGT_SINGLE),
 'CigarSmoke': ('cigar-smoke', ATK_TGT_SINGLE),
 'ClipOnTie': ('throw-paper', ATK_TGT_SINGLE),
 'Crunch': ('throw-object', ATK_TGT_SINGLE),
 'CogUp': ('effort', ATK_TGT_GROUP),
 'Demotion': ('magic1', ATK_TGT_SINGLE),
 'DoubleTalk': ('speak', ATK_TGT_SINGLE),
 'Downsize': ('magic2', ATK_TGT_SINGLE),
 'DropAnvil': ('magic3', ATK_TGT_SINGLE),
 'EvictionNotice': ('throw-paper', ATK_TGT_SINGLE),
 'EvilEye': ('glower', ATK_TGT_SINGLE),
 'Filibuster': ('speak', ATK_TGT_SINGLE),
 'FillWithLead': ('pencil-sharpener', ATK_TGT_SINGLE),
 'FingerWag': ('finger-wag', ATK_TGT_SINGLE),
 'Fired': ('magic2', ATK_TGT_SINGLE),
 'FiveOClockShadow': ('glower', ATK_TGT_SINGLE),
 'FloodTheMarket': ('glower', ATK_TGT_SINGLE),
 'FountainPen': ('pen-squirt', ATK_TGT_SINGLE),
 'FreezeAssets': ('glower', ATK_TGT_SINGLE),
 'Gavel': ('gavel', ATK_TGT_SINGLE),
 'GlowerPower': ('glower', ATK_TGT_SINGLE),
 'GuiltTrip': ('magic1', ATK_TGT_GROUP),
 'HalfWindsor': ('throw-paper', ATK_TGT_SINGLE),
 'HangUp': ('phone', ATK_TGT_SINGLE),
 'HeadShrink': ('magic1', ATK_TGT_SINGLE),
 'HotAir': ('speak', ATK_TGT_SINGLE),
 'Jargon': ('speak', ATK_TGT_SINGLE),
 'Legalese': ('speak', ATK_TGT_SINGLE),
 'Liquidate': ('magic1', ATK_TGT_SINGLE),
 'MarketCrash': ('throw-paper', ATK_TGT_SINGLE),
 'MumboJumbo': ('speak', ATK_TGT_SINGLE),
 'ParadigmShift': ('magic2', ATK_TGT_GROUP),
 'PeckingOrder': ('throw-object', ATK_TGT_SINGLE),
 'PickPocket': ('pickpocket', ATK_TGT_SINGLE),
 'PinkSlip': ('throw-paper', ATK_TGT_SINGLE),
 'PlayHardball': ('throw-paper', ATK_TGT_SINGLE),
 'PoundKey': ('phone', ATK_TGT_SINGLE),
 'PowerTie': ('throw-paper', ATK_TGT_SINGLE),
 'PowerTrip': ('magic1', ATK_TGT_GROUP),
 'Quake': ('quick-jump', ATK_TGT_GROUP),
 'RazzleDazzle': ('smile', ATK_TGT_SINGLE),
 'RedTape': ('throw-object', ATK_TGT_SINGLE),
 'ReOrg': ('magic3', ATK_TGT_SINGLE),
 'RestrainingOrder': ('throw-paper', ATK_TGT_SINGLE),
 'Rolodex': ('roll-o-dex', ATK_TGT_SINGLE),
 'RubberStamp': ('rubber-stamp', ATK_TGT_SINGLE),
 'RubOut': ('hold-eraser', ATK_TGT_SINGLE),
 'Sacked': ('throw-paper', ATK_TGT_SINGLE),
 'SandTrap': ('golf-club-swing', ATK_TGT_SINGLE),
 'Schmooze': ('speak', ATK_TGT_SINGLE),
 'Shake': ('stomp', ATK_TGT_GROUP),
 'Shred': ('shredder', ATK_TGT_SINGLE),
 'SongAndDance': ('song-and-dance', ATK_TGT_GROUP),
 'Spin': ('magic3', ATK_TGT_SINGLE),
 'Synergy': ('magic3', ATK_TGT_GROUP),
 'Tabulate': ('phone', ATK_TGT_SINGLE),
 'TeeOff': ('golf-club-swing', ATK_TGT_SINGLE),
 'ThrowBook': ('throw-object', ATK_TGT_SINGLE),
 'Tremor': ('stomp', ATK_TGT_GROUP),
 'Watercooler': ('watercooler', ATK_TGT_SINGLE),
 'Withdrawal': ('magic1', ATK_TGT_SINGLE),
 'WriteOff': ('hold-pencil', ATK_TGT_SINGLE)}
AUDIT = SuitAttacks.keys().index('Audit')
BARRIER = SuitAttacks.keys().index('Barrier')
BITE = SuitAttacks.keys().index('Bite')
BOUNCE_CHECK = SuitAttacks.keys().index('BounceCheck')
BRAIN_STORM = SuitAttacks.keys().index('BrainStorm')
BUZZ_WORD = SuitAttacks.keys().index('BuzzWord')
CALCULATE = SuitAttacks.keys().index('Calculate')
CANNED = SuitAttacks.keys().index('Canned')
CHOMP = SuitAttacks.keys().index('Chomp')
CIGAR_SMOKE = SuitAttacks.keys().index('CigarSmoke')
CLIPON_TIE = SuitAttacks.keys().index('ClipOnTie')
COG_UP = SuitAttacks.keys().index('CogUp')
CRUNCH = SuitAttacks.keys().index('Crunch')
DEMOTION = SuitAttacks.keys().index('Demotion')
DOWNSIZE = SuitAttacks.keys().index('Downsize')
DOUBLE_TALK = SuitAttacks.keys().index('DoubleTalk')
DROP_ANVIL = SuitAttacks.keys().index('DropAnvil')
EVICTION_NOTICE = SuitAttacks.keys().index('EvictionNotice')
EVIL_EYE = SuitAttacks.keys().index('EvilEye')
FILIBUSTER = SuitAttacks.keys().index('Filibuster')
FILL_WITH_LEAD = SuitAttacks.keys().index('FillWithLead')
FINGER_WAG = SuitAttacks.keys().index('FingerWag')
FIRED = SuitAttacks.keys().index('Fired')
FIVE_O_CLOCK_SHADOW = SuitAttacks.keys().index('FiveOClockShadow')
FLOOD_THE_MARKET = SuitAttacks.keys().index('FloodTheMarket')
FOUNTAIN_PEN = SuitAttacks.keys().index('FountainPen')
FREEZE_ASSETS = SuitAttacks.keys().index('FreezeAssets')
GAVEL = SuitAttacks.keys().index('Gavel')
GLOWER_POWER = SuitAttacks.keys().index('GlowerPower')
GUILT_TRIP = SuitAttacks.keys().index('GuiltTrip')
HALF_WINDSOR = SuitAttacks.keys().index('HalfWindsor')
HANG_UP = SuitAttacks.keys().index('HangUp')
HEAD_SHRINK = SuitAttacks.keys().index('HeadShrink')
HOT_AIR = SuitAttacks.keys().index('HotAir')
JARGON = SuitAttacks.keys().index('Jargon')
LEGALESE = SuitAttacks.keys().index('Legalese')
LIQUIDATE = SuitAttacks.keys().index('Liquidate')
MARKET_CRASH = SuitAttacks.keys().index('MarketCrash')
MUMBO_JUMBO = SuitAttacks.keys().index('MumboJumbo')
PARADIGM_SHIFT = SuitAttacks.keys().index('ParadigmShift')
PECKING_ORDER = SuitAttacks.keys().index('PeckingOrder')
PICK_POCKET = SuitAttacks.keys().index('PickPocket')
PINK_SLIP = SuitAttacks.keys().index('PinkSlip')
PLAY_HARDBALL = SuitAttacks.keys().index('PlayHardball')
POUND_KEY = SuitAttacks.keys().index('PoundKey')
POWER_TIE = SuitAttacks.keys().index('PowerTie')
POWER_TRIP = SuitAttacks.keys().index('PowerTrip')
QUAKE = SuitAttacks.keys().index('Quake')
RAZZLE_DAZZLE = SuitAttacks.keys().index('RazzleDazzle')
RED_TAPE = SuitAttacks.keys().index('RedTape')
RE_ORG = SuitAttacks.keys().index('ReOrg')
RESTRAINING_ORDER = SuitAttacks.keys().index('RestrainingOrder')
ROLODEX = SuitAttacks.keys().index('Rolodex')
RUBBER_STAMP = SuitAttacks.keys().index('RubberStamp')
RUB_OUT = SuitAttacks.keys().index('RubOut')
SACKED = SuitAttacks.keys().index('Sacked')
SANDTRAP = SuitAttacks.keys().index('SandTrap')
SCHMOOZE = SuitAttacks.keys().index('Schmooze')
SHAKE = SuitAttacks.keys().index('Shake')
SHRED = SuitAttacks.keys().index('Shred')
SONG_AND_DANCE = SuitAttacks.keys().index('SongAndDance')
SPIN = SuitAttacks.keys().index('Spin')
SYNERGY = SuitAttacks.keys().index('Synergy')
TABULATE = SuitAttacks.keys().index('Tabulate')
TEE_OFF = SuitAttacks.keys().index('TeeOff')
THROW_BOOK = SuitAttacks.keys().index('ThrowBook')
TREMOR = SuitAttacks.keys().index('Tremor')
WATERCOOLER = SuitAttacks.keys().index('Watercooler')
WITHDRAWAL = SuitAttacks.keys().index('Withdrawal')
WRITE_OFF = SuitAttacks.keys().index('WriteOff')

def getFaceoffTaunt(suitName, doId):
    if suitName in SuitFaceoffTaunts:
        taunts = SuitFaceoffTaunts[suitName]
    else:
        taunts = TTLocalizer.SuitFaceoffDefaultTaunts
    return taunts[doId % len(taunts)]


SuitFaceoffTaunts = OTPLocalizer.SuitFaceoffTaunts

def getAttackTauntIndexFromIndex(suit, attackIndex):
    adict = getSuitAttack(suit.getStyleName(), suit.getLevel(), attackIndex)
    return getAttackTauntIndex(adict['name'])


def getAttackTauntIndex(attackName):
    if attackName in SuitAttackTaunts:
        taunts = SuitAttackTaunts[attackName]
        return random.randint(0, len(taunts) - 1)
    else:
        return 1


def getAttackTaunt(attackName, index = None):
    if attackName in SuitAttackTaunts:
        taunts = SuitAttackTaunts[attackName]
    else:
        taunts = TTLocalizer.SuitAttackDefaultTaunts
    if index != None:
        if index >= len(taunts):
            notify.warning('index exceeds length of taunts list in getAttackTaunt')
            return TTLocalizer.SuitAttackDefaultTaunts[0]
        return taunts[index]
    else:
        return random.choice(taunts)
    return


SuitAttackTaunts = TTLocalizer.SuitAttackTaunts
DisabledAttacks = ('Gavel', 'SandTrap', 'FloodTheMarket', 'FiveOClockShadow')

def getAttacksByType(attributes):
    groupAttacks = []
    singleAttacks = []

    for attack in sorted(attributes['attacks'], key=lambda x: x[0]):
        if attack[0] in DisabledAttacks:
            continue
        if SuitAttacks[attack[0]][1] == ATK_TGT_GROUP:
            groupAttacks.append(attack)
        else:
            singleAttacks.append(attack)
    
    return groupAttacks, singleAttacks