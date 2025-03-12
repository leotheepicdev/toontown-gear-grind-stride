from ElevatorConstants import *
from toontown.base import ToontownGlobals
import random

try:
    config = base.config
except:
    config = simbase.config
    
# TODO: add more cog difficulties for higher cogs.    
# TODO: we need to make separate difficulties for field offices.
    
def determineDifficulty(suitLevel):
    if suitLevel >= 0 and suitLevel <= 2:
        possibleDifficulies = [0, 1, 2]
    elif suitLevel >= 3 and suitLevel <= 5:
        possibleDifficulies = [2, 3, 4]
    elif suitLevel >= 6 and suitLevel <= 8:
        possibleDifficulies = [5, 6, 7]
    elif suitLevel >= 9 and suitLevel <= 11:
        possibleDifficulies = [8, 9, 10]
    else:
        possibleDifficulies = [11, 12, 13, 14]
    chosenDifficulty = random.choice(possibleDifficulies)
    return chosenDifficulty
    
def determineFloors(difficulty):
    floors = CogBuildings[difficulty][0]
    minFloor = floors[0]
    maxFloor = floors[1]
    return random.randint(minFloor, maxFloor)
    
CogBuildings = {
 0: ((1, 1), # Possible floors that can be spawned.
     (1, 5), # Non-boss level range
     (6, 7), # Boss level
     (11, 13), # Number of Cogs
     (1,)),
 1: ((1, 2),
     (2, 6),
     (7, 8),
     (12, 14),
     (1, 1.2)),
 2: ((1, 3), 
     (3, 7),
     (8, 9),
     (13, 15),
     (1, 1.3, 1.6)),
 3: ((2, 3),
     (4, 8),
     (9, 10),
     (14, 16),
     (1, 1.4, 1.8)),
 4: ((2, 4),
     (5, 9),
     (10, 11),
     (15, 17),
     (1, 1.6, 1.8, 2)),
 5: ((3, 4),
     (6, 10),
     (11, 12),
     (17, 19),
     (1, 1.6, 2, 2.4)),
 6: ((3, 5),
     (7, 11),
     (12, 12),
     (19, 23),
     (1, 1.6, 1.8, 2.2, 2.4)),
 7: ((4, 5),
     (8, 11),
     (12, 12),
     (21, 27),
     (1, 1.8, 2.4, 3, 3.2)),
 8: ((4, 6), #Building created by Level 9 Cog
     (9, 12),
     (12, 12),
     (23, 31),
     (1.4, 1.8, 2.2, 3, 3.4, 4.2)),
 9: ((5, 5),
     (11, 12),
     (12, 12),
     (25, 35),
     (1.5, 1.9, 2.7, 3.5, 4.1)),
 10: ((5, 6),
      (9, 12),
      (13, 13),
      (29, 38),
      (1.7, 2.1, 2.9, 3.7, 4.3, 4.9)),
 11: ((5, 7),
      (10, 13),
      (13, 13),
      (34, 45),
      (2, 2.4, 3.2, 4, 4.6, 5.2, 6)),
 12: ((6, 6),
      (9, 13),
      (14, 14),
      (38, 50),
      (2.4, 2.8, 3.6, 4.4, 5, 5.6)),
 13: ((6, 7),
      (11, 14),
      (14, 14),
      (43, 56),
      (2.9, 3.2, 4.1, 4.9, 5.5, 6.1, 6.9)),
 14: ((7, 7),
      (12, 14),
      (15, 15),
      (50, 65),
      (3.5, 3.8, 4.7, 5.5, 6.1, 6.7, 7.5))
}
CogBosses = {
 0: ((1, 1),  #VP Round1
     (3, 10),
     (10, 10),
     (60, 60),
     (1, 1, 1, 1, 1)),
 1: ((1, 1),  #VP Round2
     (8, 12),
     (12, 12),
     (100, 100),
     (1, 1, 1, 1, 1)),
 2: ((1, 1),  #CFO
     (4, 12),
     (12, 12),
     (90, 90),
     (1, 1, 1, 1, 1)),
 3: ((1, 1),  #CFO Skelecogs
     (8, 13),
     (13, 13),
     (125, 125),
     (1, 1, 1, 1, 1)),
 4: ((1, 1),   #CJ
     (8, 14),
     (14, 14),
     (250, 250),
     (1, 1, 1, 1, 1)),
 5: ((1, 1),  #CEO Round1
     (9, 15),
     (15, 15),
     (180, 180),
     (1, 1, 1, 1, 1)),
 6: ((1, 1),
     (1, 5),
     (5, 5),
     (33, 33),
     (1, 1, 1, 1, 1)),
 7: ((1, 1),
     (4, 5),
     (5, 5),
     (50, 50),
     (1, 1, 1, 1, 1)),
 8: ((1, 1),   #CEO Round2
     (11, 12),
     (12, 12),
     (180, 180),
     (1, 1, 1, 1, 1), 
     (1,))
}
SUIT_BLDG_INFO_FLOORS = 0
SUIT_BLDG_INFO_SUIT_LVLS = 1
SUIT_BLDG_INFO_BOSS_LVLS = 2
SUIT_BLDG_INFO_LVL_POOL = 3
SUIT_BLDG_INFO_LVL_POOL_MULTS = 4
SUIT_BLDG_INFO_REVIVES = 5
VICTORY_RUN_TIME = ElevatorData[ELEVATOR_NORMAL]['openTime'] + TOON_VICTORY_EXIT_TIME
TO_TOON_BLDG_TIME = 8
VICTORY_SEQUENCE_TIME = VICTORY_RUN_TIME + TO_TOON_BLDG_TIME
CLEAR_OUT_TOON_BLDG_TIME = 4
TO_SUIT_BLDG_TIME = 8

buildingMinMax = {
    ToontownGlobals.SillyStreet: [config.GetInt('silly-street-building-min', 0),
                                  config.GetInt('silly-street-building-max', 3)],
    ToontownGlobals.LoopyLane: [config.GetInt('loopy-lane-building-min', 0),
                                config.GetInt('loopy-lane-building-max', 3)],
    ToontownGlobals.PunchlinePlace: [config.GetInt('punchline-place-building-min', 0),
                                     config.GetInt('punchline-place-building-max', 3)],
    ToontownGlobals.BarnacleBoulevard: [config.GetInt('barnacle-boulevard-building-min', 1),
                                        config.GetInt('barnacle-boulevard-building-max', 5)],
    ToontownGlobals.SeaweedStreet: [config.GetInt('seaweed-street-building-min', 1),
                                    config.GetInt('seaweed-street-building-max', 5)],
    ToontownGlobals.LighthouseLane: [config.GetInt('lighthouse-lane-building-min', 1),
                                     config.GetInt('lighthouse-lane-building-max', 5)],
    ToontownGlobals.ElmStreet: [config.GetInt('elm-street-building-min', 2),
                                config.GetInt('elm-street-building-max', 6)],
    ToontownGlobals.MapleStreet: [config.GetInt('maple-street-building-min', 2),
                                  config.GetInt('maple-street-building-max', 6)],
    ToontownGlobals.OakStreet: [config.GetInt('oak-street-building-min', 2),
                                config.GetInt('oak-street-building-max', 6)],
    ToontownGlobals.WalnutWay: [config.GetInt('walnut-way-building-min', 0),
                                config.GetInt('walnut-way-building-max', 0)],
    ToontownGlobals.AltoAvenue: [config.GetInt('alto-avenue-building-min', 3),
                                 config.GetInt('alto-avenue-building-max', 7)],
    ToontownGlobals.BaritoneBoulevard: [config.GetInt('baritone-boulevard-building-min', 3),
                                        config.GetInt('baritone-boulevard-building-max', 7)],
    ToontownGlobals.TenorTerrace: [config.GetInt('tenor-terrace-building-min', 3),
                                   config.GetInt('tenor-terrace-building-max', 7)],
    ToontownGlobals.WalrusWay: [config.GetInt('walrus-way-building-min', 5),
                                config.GetInt('walrus-way-building-max', 10)],
    ToontownGlobals.SleetStreet: [config.GetInt('sleet-street-building-min', 5),
                                  config.GetInt('sleet-street-building-max', 10)],
    ToontownGlobals.PolarPlace: [config.GetInt('polar-place-building-min', 5),
                                 config.GetInt('polar-place-building-max', 10)],
    ToontownGlobals.BlizzardBypass: [config.GetInt('blizzard-bypass-building-min', 4),
                                     config.GetInt('blizzard-bypass-building-max', 8)],
    ToontownGlobals.LullabyLane: [config.GetInt('lullaby-lane-building-min', 6),
                                  config.GetInt('lullaby-lane-building-max', 12)],
    ToontownGlobals.PajamaPlace: [config.GetInt('pajama-place-building-min', 6),
                                  config.GetInt('pajama-place-building-max', 12)],
    ToontownGlobals.SlumberStreet: [config.GetInt('slumber-street-building-min', 6),
                                    config.GetInt('slumber-street-building-max', 12)],
    ToontownGlobals.RodeoRoad: [config.GetInt('rodeo-road-building-min', 6),
                                  config.GetInt('rodeo-road-building-max', 12)],
    ToontownGlobals.CactusCourt: [config.GetInt('cactus-court-building-min', 6),
                                  config.GetInt('cactus-court-building-max', 12)],
    ToontownGlobals.HighNoonNook: [config.GetInt('high-noon-nook-building-min', 6),
                                    config.GetInt('high-noon-nook-building-max', 12)],
    ToontownGlobals.PitchforkPath: [config.GetInt('pitchfork-path-building-min', 4),
                                    config.GetInt('pitchfork-path-building-max', 8)],
    ToontownGlobals.HaybaleHighway: [config.GetInt('haybale-highway-building-min', 4),
                                     config.GetInt('haybale-highway-building-max', 8)],
    ToontownGlobals.RoosterRoad: [config.GetInt('rooster-road-building-min', 2),
                                  config.GetInt('rooster-road-building-max', 4)],
    ToontownGlobals.PavementPath: [config.GetInt('pavement-path-building-min', 10),
                                   config.GetInt('pavement-path-building-max', 16)],
    ToontownGlobals.BedrockBoulevard: [config.GetInt('bedrock-boulevard-building-min', 5),
                                       config.GetInt('bedrock-boulevard-building-max', 8)],
    ToontownGlobals.SawmillStreet: [config.GetInt('sawmill-street-building-min', 10),
                                    config.GetInt('sawmill-street-building-max', 16)],
    ToontownGlobals.SellbotHQ: [0, 0],
    ToontownGlobals.SellbotFactoryExt: [0, 0],
    ToontownGlobals.CashbotHQ: [0, 0],
    ToontownGlobals.LawbotHQ: [0, 0],
    ToontownGlobals.LawbotOfficeExt: [0, 0],
    ToontownGlobals.BossbotHQ: [0, 0]
}

buildingChance = {
    ToontownGlobals.SillyStreet: config.GetFloat('silly-street-building-chance', 2.0),
    ToontownGlobals.LoopyLane: config.GetFloat('loopy-lane-building-chance', 2.0),
    ToontownGlobals.PunchlinePlace: config.GetFloat('punchline-place-building-chance', 2.0),
    ToontownGlobals.BarnacleBoulevard: config.GetFloat('barnacle-boulevard-building-chance', 75.0),
    ToontownGlobals.SeaweedStreet: config.GetFloat('seaweed-street-building-chance', 75.0),
    ToontownGlobals.LighthouseLane: config.GetFloat('lighthouse-lane-building-chance', 75.0),
    ToontownGlobals.ElmStreet: config.GetFloat('elm-street-building-chance', 90.0),
    ToontownGlobals.MapleStreet: config.GetFloat('maple-street-building-chance', 90.0),
    ToontownGlobals.OakStreet: config.GetFloat('oak-street-building-chance', 90.0),
    ToontownGlobals.AltoAvenue: config.GetFloat('alto-avenue-building-chance', 95.0),
    ToontownGlobals.BaritoneBoulevard: config.GetFloat('baritone-boulevard-building-chance', 95.0),
    ToontownGlobals.TenorTerrace: config.GetFloat('tenor-terrace-building-chance', 95.0),
    ToontownGlobals.WalrusWay: config.GetFloat('walrus-way-building-chance', 100.0),
    ToontownGlobals.SleetStreet: config.GetFloat('sleet-street-building-chance', 100.0),
    ToontownGlobals.PolarPlace: config.GetFloat('polar-place-building-chance', 100.0),
    ToontownGlobals.BlizzardBypass: config.GetFloat('blizzard-bypass-building-chance', 80.0),
    ToontownGlobals.LullabyLane: config.GetFloat('lullaby-lane-building-chance', 100.0),
    ToontownGlobals.PajamaPlace: config.GetFloat('pajama-place-building-chance', 100.0),
    ToontownGlobals.SlumberStreet: config.GetFloat('slumber-street-building-chance', 100.0),
    ToontownGlobals.RodeoRoad: config.GetFloat('rodeo-road-building-chance', 100.0),
    ToontownGlobals.CactusCourt: config.GetFloat('cactus-court-building-chance', 100.0),
    ToontownGlobals.HighNoonNook: config.GetFloat('high-noon-nook-building-chance', 100.0),
    ToontownGlobals.PitchforkPath: config.GetFloat('pitchfork-path-building-chance', 60.0),
    ToontownGlobals.HaybaleHighway: config.GetFloat('haybale-highway-building-chance', 60.0),
    ToontownGlobals.RoosterRoad: config.GetFloat('rooster-road-building-chance', 60.0),
    ToontownGlobals.PavementPath: config.GetFloat('pavement-path-building-chance', 90.0),
    ToontownGlobals.BedrockBoulevard: config.GetFloat('bedrock-boulevard-building-chance', 90.0),
    ToontownGlobals.SawmillStreet: config.GetFloat('sawmill-street-building-chance', 90.0),
    ToontownGlobals.SellbotHQ: 0.0,
    ToontownGlobals.SellbotFactoryExt: 0.0,
    ToontownGlobals.CashbotHQ: 0.0,
    ToontownGlobals.LawbotHQ: 0.0,
    ToontownGlobals.LawbotOfficeExt: 0.0,
    ToontownGlobals.BossbotHQ: 0.0
}
