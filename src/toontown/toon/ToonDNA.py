from panda3d.core import Datagram, DatagramIterator, VBase4
import random, colorsys
from direct.directnotify.DirectNotifyGlobal import *
from direct.distributed.PyDatagram import PyDatagram
from direct.distributed.PyDatagramIterator import PyDatagramIterator
from toontown.base import ToontownGlobals
notify = directNotify.newCategory('ToonDNA')
mergeMATTailor = config.GetBool('want-mat-all-tailors', 0)
toonSpeciesTypes = ['d',
 'c',
 'h',
 'm',
 'r',
 'f',
 'p',
 'b',
 's']
toonHeadTypes = ['dls',
 'dss',
 'dsl',
 'dll',
 'cls',
 'css',
 'csl',
 'cll',
 'hls',
 'hss',
 'hsl',
 'hll',
 'mls',
 'mss',
 'rls',
 'rss',
 'rsl',
 'rll',
 'fls',
 'fss',
 'fsl',
 'fll',
 'pls',
 'pss',
 'psl',
 'pll',
 'bls',
 'bss',
 'bsl',
 'bll',
 'sls',
 'sss',
 'ssl',
 'sll']

def getHeadList(species):
    headList = []
    for head in toonHeadTypes:
        if head[0] == species:
            headList.append(head)

    return headList


def getHeadStartIndex(species):
    for head in toonHeadTypes:
        if head[0] == species:
            return toonHeadTypes.index(head)


def getSpecies(head):
    for species in toonSpeciesTypes:
        if species == head[0]:
            return species


def getSpeciesName(head):
    species = getSpecies(head)
    if species == 'd':
        speciesName = 'dog'
    elif species == 'c':
        speciesName = 'cat'
    elif species == 'h':
        speciesName = 'horse'
    elif species == 'm':
        speciesName = 'mouse'
    elif species == 'r':
        speciesName = 'rabbit'
    elif species == 'f':
        speciesName = 'duck'
    elif species == 'p':
        speciesName = 'monkey'
    elif species == 'b':
        speciesName = 'bear'
    elif species == 's':
        speciesName = 'pig'
    return speciesName


toonHeadAnimalIndices = [0,
 4,
 8,
 12,
 14,
 18,
 22,
 26,
 30]
allToonHeadAnimalIndices = [0,
 1,
 2,
 3,
 4,
 5,
 6,
 7,
 8,
 9,
 10,
 11,
 12,
 13,
 14,
 15,
 16,
 17,
 18,
 19,
 20,
 21,
 22,
 23,
 24,
 25,
 26,
 27,
 28,
 29,
 30,
 31,
 32,
 33]
toonTorsoTypes = ['ss',
 'ms',
 'ls',
 'sd',
 'md',
 'ld',
 's',
 'm',
 'l']
toonLegTypes = ['s', 'm', 'l']
Shirts = ['phase_3/maps/desat_shirt_1.jpg', #0
 'phase_3/maps/desat_shirt_2.jpg',
 'phase_3/maps/desat_shirt_3.jpg',
 'phase_3/maps/desat_shirt_4.jpg',
 'phase_3/maps/desat_shirt_5.jpg',
 'phase_3/maps/desat_shirt_6.jpg',
 'phase_3/maps/desat_shirt_7.jpg',
 'phase_3/maps/desat_shirt_8.jpg',
 'phase_3/maps/desat_shirt_9.jpg',
 'phase_3/maps/desat_shirt_10.jpg',
 'phase_3/maps/desat_shirt_11.jpg',  #10
 'phase_3/maps/desat_shirt_12.jpg',
 'phase_3/maps/desat_shirt_13.jpg',
 'phase_3/maps/desat_shirt_14.jpg',
 'phase_3/maps/desat_shirt_15.jpg',
 'phase_3/maps/desat_shirt_16.jpg',  #15
 'phase_3/maps/desat_shirt_17.jpg',
 'phase_3/maps/desat_shirt_18.jpg',  #17
 'phase_3/maps/desat_shirt_19.jpg',  #18
 'phase_3/maps/desat_shirt_20.jpg',
 'phase_3/maps/desat_shirt_21.jpg',  #20
 'phase_3/maps/desat_shirt_22.jpg',
 'phase_3/maps/desat_shirt_23.jpg',
 'phase_4/maps/female_shirt1b.jpg',  #23
 'phase_4/maps/female_shirt2.jpg',   #24
 'phase_4/maps/female_shirt3.jpg',
 'phase_4/maps/male_shirt1.jpg',  #26
 'phase_4/maps/male_shirt2_palm.jpg', #27
 'phase_4/maps/male_shirt3c.jpg', #28
 'phase_4/maps/shirt_ghost.jpg',  #29
 'phase_4/maps/shirt_pumkin.jpg', #30
 'phase_4/maps/holiday_shirt1.jpg',#snowman 31  Brr
 'phase_4/maps/holiday_shirt2b.jpg',  #32 Brr
 'phase_4/maps/holidayShirt3b.jpg',   #33 Brr
 'phase_4/maps/holidayShirt4.jpg',    #34 Brr
 'phase_4/maps/female_shirt1b.jpg',
 'phase_4/maps/female_shirt5New.jpg', #36
 'phase_4/maps/shirtMale4B.jpg', #37
 'phase_4/maps/shirt6New.jpg',  #38
 'phase_4/maps/shirtMaleNew7.jpg',
 'phase_4/maps/femaleShirtNew6.jpg',#40
 'phase_4/maps/Vday1Shirt5.jpg',
 'phase_4/maps/Vday1Shirt6SHD.jpg',
 'phase_4/maps/Vday1Shirt4.jpg',
 'phase_4/maps/Vday_shirt2c.jpg',
 'phase_4/maps/shirtTieDyeNew.jpg',#45
 'phase_4/maps/male_shirtNew12.jpg', #46
 'phase_4/maps/StPats_shirt1.jpg', #47
 'phase_4/maps/StPats_shirt2.jpg', #48
 'phase_4/maps/ContestfishingVestShirt2.jpg', #49
 'phase_4/maps/ContestFishtankShirt1.jpg',#50
 'phase_4/maps/ContestPawShirt1.jpg',
 'phase_4/maps/CowboyShirt1.jpg',
 'phase_4/maps/CowboyShirt2.jpg',
 'phase_4/maps/CowboyShirt3.jpg',
 'phase_4/maps/CowboyShirt4.jpg',#55
 'phase_4/maps/CowboyShirt5.jpg',
 'phase_4/maps/CowboyShirt6.jpg',
 'phase_4/maps/4thJulyShirt1.jpg',#58
 'phase_4/maps/4thJulyShirt2.jpg',
 'phase_4/maps/shirt_Cat7_01.jpg',#60
 'phase_4/maps/shirt_Cat7_02.jpg',
 'phase_4/maps/contest_backpack3.jpg', #62
 'phase_4/maps/contest_leder.jpg',     #63
 'phase_4/maps/contest_mellon2.jpg',
 'phase_4/maps/contest_race2.jpg',#65
 'phase_4/maps/PJBlueBanana2.jpg',#66
 'phase_4/maps/PJRedHorn2.jpg',   #67
 'phase_4/maps/PJGlasses2.jpg',   #68
 'phase_4/maps/tt_t_chr_avt_shirt_valentine1.jpg',
 'phase_4/maps/tt_t_chr_avt_shirt_valentine2.jpg',  #70
 'phase_4/maps/tt_t_chr_avt_shirt_desat4.jpg',
 'phase_4/maps/tt_t_chr_avt_shirt_fishing1.jpg',
 'phase_4/maps/tt_t_chr_avt_shirt_fishing2.jpg',
 'phase_4/maps/tt_t_chr_avt_shirt_gardening1.jpg',
 'phase_4/maps/tt_t_chr_avt_shirt_gardening2.jpg',  #75
 'phase_4/maps/tt_t_chr_avt_shirt_party1.jpg',
 'phase_4/maps/tt_t_chr_avt_shirt_party2.jpg',
 'phase_4/maps/tt_t_chr_avt_shirt_racing1.jpg',
 'phase_4/maps/tt_t_chr_avt_shirt_racing2.jpg',
 'phase_4/maps/tt_t_chr_avt_shirt_summer1.jpg',  #80
 'phase_4/maps/tt_t_chr_avt_shirt_summer2.jpg',
 'phase_4/maps/tt_t_chr_avt_shirt_golf1.jpg',  #82DD
 'phase_4/maps/tt_t_chr_avt_shirt_golf2.jpg',  #83DD
 'phase_4/maps/tt_t_chr_avt_shirt_halloween1.jpg',
 'phase_4/maps/tt_t_chr_avt_shirt_halloween2.jpg', #85
 'phase_4/maps/tt_t_chr_avt_shirt_marathon1.jpg',  #86
 'phase_4/maps/tt_t_chr_avt_shirt_saveBuilding1.jpg',
 'phase_4/maps/tt_t_chr_avt_shirt_saveBuilding2.jpg',#88DonaldsDock
 'phase_4/maps/tt_t_chr_avt_shirt_toonTask1.jpg',
 'phase_4/maps/tt_t_chr_avt_shirt_toonTask2.jpg',  #90
 'phase_4/maps/tt_t_chr_avt_shirt_trolley1.jpg',
 'phase_4/maps/tt_t_chr_avt_shirt_trolley2.jpg',
 'phase_4/maps/tt_t_chr_avt_shirt_winter1.jpg',  #93Brr
 'phase_4/maps/tt_t_chr_avt_shirt_halloween3.jpg',
 'phase_4/maps/tt_t_chr_avt_shirt_halloween4.jpg',  #95
 'phase_4/maps/tt_t_chr_avt_shirt_valentine3.jpg',
 'phase_4/maps/tt_t_chr_shirt_scientistC.jpg',
 'phase_4/maps/tt_t_chr_shirt_scientistA.jpg',
 'phase_4/maps/tt_t_chr_shirt_scientistB.jpg',
 'phase_4/maps/tt_t_chr_avt_shirt_mailbox.jpg',  #100
 'phase_4/maps/tt_t_chr_avt_shirt_trashcan.jpg',
 'phase_4/maps/tt_t_chr_avt_shirt_loonyLabs.jpg',
 'phase_4/maps/tt_t_chr_avt_shirt_hydrant.jpg',
 'phase_4/maps/tt_t_chr_avt_shirt_whistle.jpg',
 'phase_4/maps/tt_t_chr_avt_shirt_cogbuster.jpg',#105
 'phase_4/maps/tt_t_chr_avt_shirt_mostCogsDefeated01.jpg',
 'phase_4/maps/tt_t_chr_avt_shirt_victoryParty01.jpg',
 'phase_4/maps/tt_t_chr_avt_shirt_victoryParty02.jpg',
 'phase_4/maps/tt_t_chr_avt_shirt_sellbotIcon.jpg',
 'phase_4/maps/tt_t_chr_avt_shirt_sellbotVPIcon.jpg',#110
 'phase_4/maps/tt_t_chr_avt_shirt_sellbotCrusher.jpg',
 'phase_4/maps/tt_t_chr_avt_shirt_jellyBeans.jpg',
 'phase_4/maps/tt_t_chr_avt_shirt_doodle.jpg',
 'phase_4/maps/tt_t_chr_avt_shirt_halloween5.jpg',
 'phase_4/maps/tt_t_chr_avt_shirt_halloweenTurtle.jpg',#115
 'phase_4/maps/tt_t_chr_avt_shirt_greentoon1.jpg',  #116
 'phase_4/maps/tt_t_chr_avt_shirt_getConnectedMoverShaker.jpg',#117
 'phase_4/maps/tt_t_chr_avt_shirt_racingGrandPrix.jpg',
 'phase_4/maps/tt_t_chr_avt_shirt_bee.jpg',
 'phase_4/maps/tt_t_chr_avt_shirt_pirate.jpg',  #120
 'phase_4/maps/tt_t_chr_avt_shirt_supertoon.jpg',
 'phase_4/maps/tt_t_chr_avt_shirt_vampire.jpg',
 'phase_4/maps/tt_t_chr_avt_shirt_dinosaur.jpg', #123
 'phase_4/maps/tt_t_chr_avt_shirt_fishing04.jpg',
 'phase_4/maps/tt_t_chr_avt_shirt_golf03.jpg', #125
 'phase_4/maps/tt_t_chr_avt_shirt_mostCogsDefeated02.jpg',
 'phase_4/maps/tt_t_chr_avt_shirt_racing03.jpg',
 'phase_4/maps/tt_t_chr_avt_shirt_saveBuilding3.jpg',
 'phase_4/maps/tt_t_chr_avt_shirt_trolley03.jpg',
 'phase_4/maps/tt_t_chr_avt_shirt_fishing05.jpg', #130
 'phase_4/maps/tt_t_chr_avt_shirt_golf04.jpg',
 'phase_4/maps/tt_t_chr_avt_shirt_halloween06.jpg',
 'phase_4/maps/tt_t_chr_avt_shirt_winter03.jpg',
 'phase_4/maps/tt_t_chr_avt_shirt_halloween07.jpg',
 'phase_4/maps/tt_t_chr_avt_shirt_winter02.jpg', #135
 'phase_4/maps/tt_t_chr_avt_shirt_fishing06.jpg',
 'phase_4/maps/tt_t_chr_avt_shirt_fishing07.jpg',
 'phase_4/maps/tt_t_chr_avt_shirt_golf05.jpg',
 'phase_4/maps/tt_t_chr_avt_shirt_racing04.jpg',
 'phase_4/maps/tt_t_chr_avt_shirt_racing05.jpg', #140
 'phase_4/maps/tt_t_chr_avt_shirt_mostCogsDefeated03.jpg',
 'phase_4/maps/tt_t_chr_avt_shirt_mostCogsDefeated04.jpg',
 'phase_4/maps/tt_t_chr_avt_shirt_trolley04.jpg',
 'phase_4/maps/tt_t_chr_avt_shirt_trolley05.jpg',
 'phase_4/maps/tt_t_chr_avt_shirt_saveBuilding4.jpg',#145
 'phase_4/maps/tt_t_chr_avt_shirt_saveBuilding05.jpg',
 'phase_4/maps/tt_t_chr_avt_shirt_anniversary.jpg',#147
 'phase_4/maps/flannelshirt_red.jpg',
 'phase_3/maps/mml_shirt.jpg',          #149
 'phase_4/maps/Big_Cheese_Shirt.jpg',   #150
 'phase_3/maps/mml_shirt2.jpg']         #151
BoyShirts = [(0, 0),
 (1, 1),
 (2, 2),
 (3, 3),
 (4, 4),
 (5, 5),
 (8, 8),
 (9, 9),
 (10, 0),
 (11, 0),
 (14, 10),
 (16, 0),
 (17, 0),
 (18, 12),
 (19, 13)]
GirlShirts = [(0, 0),
 (1, 1),
 (2, 2),
 (3, 3),
 (5, 5),
 (6, 6),
 (7, 7),
 (9, 9),
 (12, 0),
 (13, 11),
 (15, 11),
 (16, 0),
 (20, 0),
 (21, 0),
 (22, 0)]

def isValidBoyShirt(index):
    for pair in BoyShirts:
        if index == pair[0]:
            return 1

    return 0


def isValidGirlShirt(index):
    for pair in GirlShirts:
        if index == pair[0]:
            return 1

    return 0


Sleeves = ['phase_3/maps/desat_sleeve_1.jpg', #0
 'phase_3/maps/desat_sleeve_2.jpg',
 'phase_3/maps/desat_sleeve_3.jpg',
 'phase_3/maps/desat_sleeve_4.jpg',
 'phase_3/maps/desat_sleeve_5.jpg',
 'phase_3/maps/desat_sleeve_6.jpg', #5
 'phase_3/maps/desat_sleeve_7.jpg',
 'phase_3/maps/desat_sleeve_8.jpg',
 'phase_3/maps/desat_sleeve_9.jpg',
 'phase_3/maps/desat_sleeve_10.jpg',
 'phase_3/maps/desat_sleeve_15.jpg', #10
 'phase_3/maps/desat_sleeve_16.jpg',
 'phase_3/maps/desat_sleeve_19.jpg',
 'phase_3/maps/desat_sleeve_20.jpg',
 'phase_4/maps/female_sleeve1b.jpg', #14
 'phase_4/maps/female_sleeve2.jpg',  #15
 'phase_4/maps/female_sleeve3.jpg',
 'phase_4/maps/male_sleeve1.jpg',  #17
 'phase_4/maps/male_sleeve2_palm.jpg',
 'phase_4/maps/male_sleeve3c.jpg',
 'phase_4/maps/shirt_Sleeve_ghost.jpg', #20
 'phase_4/maps/shirt_Sleeve_pumkin.jpg',#21
 'phase_4/maps/holidaySleeve1.jpg', #goes with holidayshirt1,2 22
 'phase_4/maps/holidaySleeve3.jpg', #goes with holidayshirt3,4 23
 'phase_4/maps/female_sleeve1b.jpg',
 'phase_4/maps/female_sleeve5New.jpg',#25
 'phase_4/maps/male_sleeve4New.jpg',  #26
 'phase_4/maps/sleeve6New.jpg',
 'phase_4/maps/SleeveMaleNew7.jpg',    #28
 'phase_4/maps/female_sleeveNew6.jpg', #29
 'phase_4/maps/Vday5Sleeve.jpg',  #30
 'phase_4/maps/Vda6Sleeve.jpg',
 'phase_4/maps/Vday_shirt4sleeve.jpg',
 'phase_4/maps/Vday2cSleeve.jpg',
 'phase_4/maps/sleeveTieDye.jpg', #34
 'phase_4/maps/male_sleeveNew12.jpg',  #35
 'phase_4/maps/StPats_sleeve.jpg',   #36
 'phase_4/maps/StPats_sleeve2.jpg',  #37
 'phase_4/maps/ContestfishingVestSleeve1.jpg',  #38
 'phase_4/maps/ContestFishtankSleeve1.jpg',
 'phase_4/maps/ContestPawSleeve1.jpg',  #40
 'phase_4/maps/CowboySleeve1.jpg',
 'phase_4/maps/CowboySleeve2.jpg',
 'phase_4/maps/CowboySleeve3.jpg',
 'phase_4/maps/CowboySleeve4.jpg',
 'phase_4/maps/CowboySleeve5.jpg',  #45
 'phase_4/maps/CowboySleeve6.jpg',
 'phase_4/maps/4thJulySleeve1.jpg', #47
 'phase_4/maps/4thJulySleeve2.jpg', #48
 'phase_4/maps/shirt_sleeveCat7_01.jpg',
 'phase_4/maps/shirt_sleeveCat7_02.jpg',  #50
 'phase_4/maps/contest_backpack_sleeve.jpg',
 'phase_4/maps/Contest_leder_sleeve.jpg',  #52
 'phase_4/maps/contest_mellon_sleeve2.jpg',
 'phase_4/maps/contest_race_sleeve.jpg',#54
 'phase_4/maps/PJSleeveBlue.jpg',  #55
 'phase_4/maps/PJSleeveRed.jpg',   #56
 'phase_4/maps/PJSleevePurple.jpg',#57
 'phase_4/maps/tt_t_chr_avt_shirtSleeve_valentine1.jpg',
 'phase_4/maps/tt_t_chr_avt_shirtSleeve_valentine2.jpg',
 'phase_4/maps/tt_t_chr_avt_shirtSleeve_desat4.jpg',  #60
 'phase_4/maps/tt_t_chr_avt_shirtSleeve_fishing1.jpg',  #61
 'phase_4/maps/tt_t_chr_avt_shirtSleeve_fishing2.jpg',
 'phase_4/maps/tt_t_chr_avt_shirtSleeve_gardening1.jpg',
 'phase_4/maps/tt_t_chr_avt_shirtSleeve_gardening2.jpg',
 'phase_4/maps/tt_t_chr_avt_shirtSleeve_party1.jpg',  #65
 'phase_4/maps/tt_t_chr_avt_shirtSleeve_party2.jpg',
 'phase_4/maps/tt_t_chr_avt_shirtSleeve_racing1.jpg',
 'phase_4/maps/tt_t_chr_avt_shirtSleeve_racing2.jpg',
 'phase_4/maps/tt_t_chr_avt_shirtSleeve_summer1.jpg',
 'phase_4/maps/tt_t_chr_avt_shirtSleeve_summer2.jpg',  #70
 'phase_4/maps/tt_t_chr_avt_shirtSleeve_golf1.jpg',  #71DD
 'phase_4/maps/tt_t_chr_avt_shirtSleeve_golf2.jpg',  #72DD
 'phase_4/maps/tt_t_chr_avt_shirtSleeve_halloween1.jpg',
 'phase_4/maps/tt_t_chr_avt_shirtSleeve_halloween2.jpg',
 'phase_4/maps/tt_t_chr_avt_shirtSleeve_marathon1.jpg',  #75
 'phase_4/maps/tt_t_chr_avt_shirtSleeve_saveBuilding1.jpg',
 'phase_4/maps/tt_t_chr_avt_shirtSleeve_saveBuilding2.jpg', #77DonaldsDock
 'phase_4/maps/tt_t_chr_avt_shirtSleeve_toonTask1.jpg',
 'phase_4/maps/tt_t_chr_avt_shirtSleeve_toonTask2.jpg',
 'phase_4/maps/tt_t_chr_avt_shirtSleeve_trolley1.jpg',  #80
 'phase_4/maps/tt_t_chr_avt_shirtSleeve_trolley2.jpg',
 'phase_4/maps/tt_t_chr_avt_shirtSleeve_winter1.jpg',  #82
 'phase_4/maps/tt_t_chr_avt_shirtSleeve_halloween3.jpg',
 'phase_4/maps/tt_t_chr_avt_shirtSleeve_halloween4.jpg',
 'phase_4/maps/tt_t_chr_avt_shirtSleeve_valentine3.jpg',  #85
 'phase_4/maps/tt_t_chr_shirtSleeve_scientist.jpg',
 'phase_4/maps/tt_t_chr_avt_shirtSleeve_mailbox.jpg',   #87
 'phase_4/maps/tt_t_chr_avt_shirtSleeve_trashcan.jpg',
 'phase_4/maps/tt_t_chr_avt_shirtSleeve_loonyLabs.jpg', #89
 'phase_4/maps/tt_t_chr_avt_shirtSleeve_hydrant.jpg',   #90
 'phase_4/maps/tt_t_chr_avt_shirtSleeve_whistle.jpg',
 'phase_4/maps/tt_t_chr_avt_shirtSleeve_cogbuster.jpg', #92
 'phase_4/maps/tt_t_chr_avt_shirtSleeve_mostCogsDefeated01.jpg',
 'phase_4/maps/tt_t_chr_avt_shirtSleeve_victoryParty01.jpg',
 'phase_4/maps/tt_t_chr_avt_shirtSleeve_victoryParty02.jpg',  #95
 'phase_4/maps/tt_t_chr_avt_shirtSleeve_sellbotIcon.jpg',
 'phase_4/maps/tt_t_chr_avt_shirtSleeve_sellbotVPIcon.jpg',
 'phase_4/maps/tt_t_chr_avt_shirtSleeve_sellbotCrusher.jpg',
 'phase_4/maps/tt_t_chr_avt_shirtSleeve_jellyBeans.jpg',
 'phase_4/maps/tt_t_chr_avt_shirtSleeve_doodle.jpg',   #100
 'phase_4/maps/tt_t_chr_avt_shirtSleeve_halloween5.jpg',
 'phase_4/maps/tt_t_chr_avt_shirtSleeve_halloweenTurtle.jpg',
 'phase_4/maps/tt_t_chr_avt_shirtSleeve_greentoon1.jpg',  #103
 'phase_4/maps/tt_t_chr_avt_shirtSleeve_getConnectedMoverShaker.jpg',#104
 'phase_4/maps/tt_t_chr_avt_shirtSleeve_racingGrandPrix.jpg',  #105
 'phase_4/maps/tt_t_chr_avt_shirtSleeve_bee.jpg',
 'phase_4/maps/tt_t_chr_avt_shirtSleeve_pirate.jpg',
 'phase_4/maps/tt_t_chr_avt_shirtSleeve_supertoon.jpg',
 'phase_4/maps/tt_t_chr_avt_shirtSleeve_vampire.jpg',
 'phase_4/maps/tt_t_chr_avt_shirtSleeve_dinosaur.jpg',  #110
 'phase_4/maps/tt_t_chr_avt_shirtSleeve_fishing04.jpg',
 'phase_4/maps/tt_t_chr_avt_shirtSleeve_golf03.jpg',   #112
 'phase_4/maps/tt_t_chr_avt_shirtSleeve_mostCogsDefeated02.jpg',
 'phase_4/maps/tt_t_chr_avt_shirtSleeve_racing03.jpg',
 'phase_4/maps/tt_t_chr_avt_shirtSleeve_saveBuilding3.jpg',  #115
 'phase_4/maps/tt_t_chr_avt_shirtSleeve_trolley03.jpg',
 'phase_4/maps/tt_t_chr_avt_shirtSleeve_fishing05.jpg',
 'phase_4/maps/tt_t_chr_avt_shirtSleeve_golf04.jpg',
 'phase_4/maps/tt_t_chr_avt_shirtSleeve_halloween06.jpg',
 'phase_4/maps/tt_t_chr_avt_shirtSleeve_winter03.jpg',   #120
 'phase_4/maps/tt_t_chr_avt_shirtSleeve_halloween07.jpg',
 'phase_4/maps/tt_t_chr_avt_shirtSleeve_winter02.jpg',#122
 'phase_4/maps/tt_t_chr_avt_shirtSleeve_fishing06.jpg',
 'phase_4/maps/tt_t_chr_avt_shirtSleeve_fishing07.jpg',
 'phase_4/maps/tt_t_chr_avt_shirtSleeve_golf05.jpg',  #125
 'phase_4/maps/tt_t_chr_avt_shirtSleeve_racing04.jpg',
 'phase_4/maps/tt_t_chr_avt_shirtSleeve_racing05.jpg',
 'phase_4/maps/tt_t_chr_avt_shirtSleeve_mostCogsDefeated03.jpg',
 'phase_4/maps/tt_t_chr_avt_shirtSleeve_mostCogsDefeated04.jpg',
 'phase_4/maps/tt_t_chr_avt_shirtSleeve_trolley04.jpg',  #130
 'phase_4/maps/tt_t_chr_avt_shirtSleeve_trolley05.jpg',
 'phase_4/maps/tt_t_chr_avt_shirtSleeve_saveBuilding4.jpg',
 'phase_4/maps/tt_t_chr_avt_shirtSleeve_saveBuilding05.jpg',
 'phase_4/maps/tt_t_chr_avt_shirtSleeve_anniversary.jpg',  #134
 'phase_4/maps/flannelsleeve_red.jpg',
 'phase_3/maps/mml_sleeve.jpg',
 'phase_4/maps/Big_Cheese_Sleeve.jpg',     #137 
 'phase_3/maps/mml_sleeve2.jpg']   
BoyShorts = ['phase_3/maps/desat_shorts_1.jpg', #0
 'phase_3/maps/desat_shorts_2.jpg', #DonaldsDock
 'phase_3/maps/desat_shorts_4.jpg',
 'phase_3/maps/desat_shorts_6.jpg',
 'phase_3/maps/desat_shorts_7.jpg',
 'phase_3/maps/desat_shorts_8.jpg',  #5
 'phase_3/maps/desat_shorts_9.jpg',
 'phase_3/maps/desat_shorts_10.jpg',  #7 DonaldsDock
 'phase_4/maps/VdayShorts2.jpg',
 'phase_4/maps/shorts4.jpg', #9DDL
 'phase_4/maps/shorts1.jpg', #10brr
 'phase_4/maps/shorts5.jpg', #11BRR
 'phase_4/maps/CowboyShorts1.jpg',
 'phase_4/maps/CowboyShorts2.jpg',
 'phase_4/maps/4thJulyShorts1.jpg',#14
 'phase_4/maps/shortsCat7_01.jpg', #15DG
 'phase_4/maps/Blue_shorts_1.jpg', #16brr
 'phase_4/maps/Red_shorts_1.jpg',
 'phase_4/maps/Purple_shorts_1.jpg',
 'phase_4/maps/tt_t_chr_avt_shorts_winter1.jpg',#19
 'phase_4/maps/tt_t_chr_avt_shorts_winter2.jpg',#20
 'phase_4/maps/tt_t_chr_avt_shorts_winter3.jpg',#21
 'phase_4/maps/tt_t_chr_avt_shorts_winter4.jpg',#22
 'phase_4/maps/tt_t_chr_avt_shorts_valentine1.jpg',
 'phase_4/maps/tt_t_chr_avt_shorts_valentine2.jpg',
 'phase_4/maps/tt_t_chr_avt_shorts_fishing1.jpg',  #25
 'phase_4/maps/tt_t_chr_avt_shorts_gardening1.jpg',
 'phase_4/maps/tt_t_chr_avt_shorts_party1.jpg',    #27
 'phase_4/maps/tt_t_chr_avt_shorts_racing1.jpg',
 'phase_4/maps/tt_t_chr_avt_shorts_summer1.jpg',
 'phase_4/maps/tt_t_chr_avt_shorts_golf1.jpg',  #30
 'phase_4/maps/tt_t_chr_avt_shorts_halloween1.jpg',
 'phase_4/maps/tt_t_chr_avt_shorts_halloween2.jpg',
 'phase_4/maps/tt_t_chr_avt_shorts_saveBuilding1.jpg',
 'phase_4/maps/tt_t_chr_avt_shorts_trolley1.jpg',
 'phase_4/maps/tt_t_chr_avt_shorts_halloween4.jpg',  #35
 'phase_4/maps/tt_t_chr_avt_shorts_halloween3.jpg',
 'phase_4/maps/tt_t_chr_shorts_scientistA.jpg',
 'phase_4/maps/tt_t_chr_shorts_scientistB.jpg',
 'phase_4/maps/tt_t_chr_shorts_scientistC.jpg',
 'phase_4/maps/tt_t_chr_avt_shorts_cogbuster.jpg',  #40
 'phase_4/maps/tt_t_chr_avt_shorts_sellbotCrusher.jpg',
 'phase_4/maps/tt_t_chr_avt_shorts_halloween5.jpg',
 'phase_4/maps/tt_t_chr_avt_shorts_halloweenTurtle.jpg',
 'phase_4/maps/tt_t_chr_avt_shorts_greentoon1.jpg',  #44
 'phase_4/maps/tt_t_chr_avt_shorts_racingGrandPrix.jpg',  #45
 'phase_4/maps/tt_t_chr_avt_shorts_bee.jpg',
 'phase_4/maps/tt_t_chr_avt_shorts_pirate.jpg',  #47
 'phase_4/maps/tt_t_chr_avt_shorts_supertoon.jpg',
 'phase_4/maps/tt_t_chr_avt_shorts_vampire.jpg',
 'phase_4/maps/tt_t_chr_avt_shorts_dinosaur.jpg',  #50
 'phase_4/maps/tt_t_chr_avt_shorts_golf03.jpg',   #51
 'phase_4/maps/tt_t_chr_avt_shorts_racing03.jpg',
 'phase_4/maps/tt_t_chr_avt_shorts_golf04.jpg',    #53
 'phase_4/maps/tt_t_chr_avt_shorts_golf05.jpg',    #54
 'phase_4/maps/tt_t_chr_avt_shorts_racing04.jpg',  #55
 'phase_4/maps/tt_t_chr_avt_shorts_racing05.jpg',
 'phase_3/maps/desat_shorts_20.jpg',  #57
 'phase_3/maps/desat_shorts_80.jpg']  
SHORTS = 0
SKIRT = 1
GirlBottoms = [('phase_3/maps/desat_skirt_1.jpg', SKIRT),
 ('phase_3/maps/desat_skirt_2.jpg', SKIRT),#1
 ('phase_3/maps/desat_skirt_3.jpg', SKIRT),
 ('phase_3/maps/desat_skirt_4.jpg', SKIRT),
 ('phase_3/maps/desat_skirt_5.jpg', SKIRT),#4
 ('phase_3/maps/desat_shorts_1.jpg', SHORTS), #5
 ('phase_3/maps/desat_shorts_5.jpg', SHORTS),
 ('phase_3/maps/desat_skirt_6.jpg', SKIRT),
 ('phase_3/maps/desat_skirt_7.jpg', SKIRT),#8
 ('phase_3/maps/desat_shorts_10.jpg', SHORTS),
 ('phase_4/maps/female_skirt1.jpg', SKIRT),
 ('phase_4/maps/female_skirt2.jpg', SKIRT),
 ('phase_4/maps/female_skirt3.jpg', SKIRT),#12
 ('phase_4/maps/VdaySkirt1.jpg', SKIRT),
 ('phase_4/maps/skirtNew5.jpg', SKIRT),  #14TTC
 ('phase_4/maps/shorts5.jpg', SHORTS),
 ('phase_4/maps/CowboySkirt1.jpg', SKIRT),#16
 ('phase_4/maps/CowboySkirt2.jpg', SKIRT),
 ('phase_4/maps/4thJulySkirt1.jpg', SKIRT),
 ('phase_4/maps/skirtCat7_01.jpg', SKIRT),  #19DG
 ('phase_4/maps/Blue_shorts_1.jpg', SHORTS),#20brr
 ('phase_4/maps/Red_shorts_1.jpg', SHORTS),
 ('phase_4/maps/Purple_shorts_1.jpg', SHORTS),
 ('phase_4/maps/tt_t_chr_avt_skirt_winter1.jpg', SKIRT),#23
 ('phase_4/maps/tt_t_chr_avt_skirt_winter2.jpg', SKIRT),#24
 ('phase_4/maps/tt_t_chr_avt_skirt_winter3.jpg', SKIRT),#25 red
 ('phase_4/maps/tt_t_chr_avt_skirt_winter4.jpg', SKIRT),#26 red
 ('phase_4/maps/tt_t_chr_avt_skirt_valentine1.jpg', SKIRT),
 ('phase_4/maps/tt_t_chr_avt_skirt_valentine2.jpg', SKIRT),
 ('phase_4/maps/tt_t_chr_avt_skirt_fishing1.jpg', SKIRT),
 ('phase_4/maps/tt_t_chr_avt_skirt_gardening1.jpg', SKIRT), #30
 ('phase_4/maps/tt_t_chr_avt_skirt_party1.jpg', SKIRT),
 ('phase_4/maps/tt_t_chr_avt_skirt_racing1.jpg', SKIRT),
 ('phase_4/maps/tt_t_chr_avt_skirt_summer1.jpg', SKIRT),
 ('phase_4/maps/tt_t_chr_avt_skirt_golf1.jpg', SKIRT), #34
 ('phase_4/maps/tt_t_chr_avt_skirt_halloween1.jpg', SKIRT), #35
 ('phase_4/maps/tt_t_chr_avt_skirt_halloween2.jpg', SKIRT),
 ('phase_4/maps/tt_t_chr_avt_skirt_saveBuilding1.jpg', SKIRT),
 ('phase_4/maps/tt_t_chr_avt_skirt_trolley1.jpg', SKIRT),
 ('phase_4/maps/tt_t_chr_avt_skirt_halloween3.jpg', SKIRT),
 ('phase_4/maps/tt_t_chr_avt_skirt_halloween4.jpg', SKIRT), #40
 ('phase_4/maps/tt_t_chr_shorts_scientistA.jpg', SHORTS),
 ('phase_4/maps/tt_t_chr_shorts_scientistB.jpg', SHORTS),
 ('phase_4/maps/tt_t_chr_shorts_scientistC.jpg', SHORTS),
 ('phase_4/maps/tt_t_chr_avt_shorts_cogbuster.jpg', SHORTS),
 ('phase_4/maps/tt_t_chr_avt_shorts_sellbotCrusher.jpg', SHORTS), #45
 ('phase_4/maps/tt_t_chr_avt_shorts_halloween5.jpg', SHORTS),
 ('phase_4/maps/tt_t_chr_avt_shorts_halloweenTurtle.jpg', SHORTS),
 ('phase_4/maps/tt_t_chr_avt_skirt_greentoon1.jpg', SKIRT), #48
 ('phase_4/maps/tt_t_chr_avt_skirt_racingGrandPrix.jpg', SKIRT),
 ('phase_4/maps/tt_t_chr_avt_shorts_bee.jpg', SHORTS), #50
 ('phase_4/maps/tt_t_chr_avt_shorts_pirate.jpg', SHORTS),
 ('phase_4/maps/tt_t_chr_avt_skirt_pirate.jpg', SKIRT),
 ('phase_4/maps/tt_t_chr_avt_shorts_supertoon.jpg', SHORTS),
 ('phase_4/maps/tt_t_chr_avt_shorts_vampire.jpg', SHORTS),
 ('phase_4/maps/tt_t_chr_avt_shorts_dinosaur.jpg', SHORTS), #55
 ('phase_4/maps/tt_t_chr_avt_skirt_golf02.jpg', SKIRT),
 ('phase_4/maps/tt_t_chr_avt_skirt_racing03.jpg', SKIRT),
 ('phase_4/maps/tt_t_chr_avt_skirt_golf03.jpg', SKIRT),
 ('phase_4/maps/tt_t_chr_avt_skirt_golf04.jpg', SKIRT),   #59
 ('phase_4/maps/tt_t_chr_avt_skirt_racing04.jpg', SKIRT), #60
 ('phase_4/maps/tt_t_chr_avt_skirt_racing05.jpg', SKIRT), #61
 ('phase_3/maps/desat_skirt_40.jpg', SKIRT),  #62
 ('phase_3/maps/desat_skirt_70.jpg', SKIRT),  #63
 ('phase_3/maps/desat_shorts_20.jpg', SHORTS),  #64
 ('phase_4/maps/cash_skirt.jpg', SKIRT)]  #65
ClothesColors = [VBase4(0.933594, 0.265625, 0.28125, 1.0), #0Red
 VBase4(0.863281, 0.40625, 0.417969, 1.0),   #1LightRed
 VBase4(0.710938, 0.234375, 0.4375, 1.0),    #2DarkPink
 VBase4(0.992188, 0.480469, 0.167969, 1.0),  #3OrangeTTC
 VBase4(0.996094, 0.898438, 0.320312, 1.0),  #4Yellow
 VBase4(0.180781, 0.304219, 0.174219, 1.0),  #5DarkGreen
 VBase4(0.242188, 0.742188, 0.515625, 1.0),  #6BlueGreen
 VBase4(0.55, 0.138, 0.138, 1.0),            #7DarkRedDDL
 VBase4(0.347656, 0.820312, 0.953125, 1.0),  #8LightBlueBRR
 VBase4(0.191406, 0.5625, 0.773438, 1.0),    #9SlateBlueBRR
 VBase4(0.285156, 0.328125, 0.726562, 1.0),  #10Blue
 VBase4(0.37, 0.24, 0.41, 1.0),              #11DarkPurpleDDL
 VBase4(0.546875, 0.28125, 0.75, 1.0),       #12Purple
 VBase4(0.570312, 0.449219, 0.164062, 1.0),  #13LightBrown
 VBase4(0.47, 0.36, 0.23, 1.0),              #14BrownDDL
 VBase4(0.996094, 0.695312, 0.511719, 1.0),  #15PeachTan
 VBase4(0.832031, 0.5, 0.296875, 1.0),       #16OrangeBrown
 VBase4(0.196078, 0.803921, 0.196078, 1.0),  #17LimeGreenTTC
 VBase4(0.550781, 0.824219, 0.324219, 1.0),  #18LightGreen
 VBase4(0.3, 0.3, 0.35, 1.0),                #19Black
 VBase4(0.0, 0.2, 0.956862, 1.0),            #20BrightBlue
 VBase4(1.0, 0.43, 0.78, 1.0),               #21NeonPink
 VBase4(0.996094, 0.957031, 0.597656, 1.0),  #22LightYellow
 VBase4(0.972549, 0.094117, 0.094117, 1.0),  #23BrightRed
 VBase4(0.558594, 0.589844, 0.875, 1.0),     #24LightPurple
 VBase4(0.726562, 0.472656, 0.859375, 1.0),  #25Purple
 VBase4(0.898438, 0.617188, 0.90625, 1.0),   #26Pink
 VBase4(1.0, 1.0, 1.0, 1.0),                 #27White
 VBase4(0.0, 0.2, 0.956862, 1.0),            #28BrightBlue
 VBase4(0.972549, 0.094117, 0.094117, 1.0),  #29BrightRed
 VBase4(0.447058, 0.0, 0.90196, 1.0),        #30BrightPurple
 VBase4(0.3, 0.3, 0.35, 1.0),                #31Black
 VBase4(0.196078, 0.803921, 0.196078, 1.0),  #32LimeGreen
 VBase4(0.462745098039216, 0.0901960784313725, 0.0901960784313725, 1.0)]  #33DarkRed

ShirtStyles = {'bss1': [0, 0, [(0, 0),
           (3, 3),
           (4, 4),
           (6, 6),
           (10, 10),      #Makeatoon
           (11, 11),
           (13, 13),
           (15, 15),
           (16, 16),
           (18, 18),
           (19, 19),
           (20, 20),
           (22, 22),
           (27, 27)]],
 'bss2': [1, 1, [(0, 0),
           (3, 3),
           (4, 4),
           (6, 6),
           (10, 10),      #Makeatoon
           (11, 11),
           (13, 13),
           (15, 15),
           (16, 16),
           (18, 18),
           (19, 19),
           (22, 22),
           (27, 27)]],
 'bss29': [4, 4, [(0, 0),
           (3, 3),
           (4, 4),
           (6, 6),
           (10, 10),      #Makeatoon
           (11, 11),
           (13, 13),
           (15, 15),
           (16, 16),
           (18, 18),
           (19, 19),
           (22, 22),
           (27, 27)]],
 'bss30': [5, 12, [(0, 0),
           (3, 3),
           (4, 4),
           (6, 6),
           (10, 10),      #Makeatoon
           (11, 11),
           (13, 13),
           (15, 15),
           (16, 16),
           (18, 18),
           (19, 19),
           (22, 22),
           (27, 27)]],
 'bss3': [139, 126, [(27, 27)]],   #TTC
 'bss4': [140, 127, [(27, 27)]],   #TTC
 'bss5': [112, 99, [(27, 27)]],    #MML
 'bss6': [72, 61, [(27, 27)]],  #DonaldsDock
 'bss7': [73, 62, [(27, 27)]],  #DonaldsDock
 'bss8': [120, 107, [(27, 27)]],  #DonaldsDock
 'bss9': [88, 77, [(27, 27)]],  #DonaldsDock
 'bss10': [124, 111, [(27, 27)]],  #DonaldsDock
 'bss11': [137, 124, [(27, 27)]],  #DonaldsDock
 'bss12': [150, 137, [(27, 27)]],  #DDBigCheese
 'bss13': [149, 136, [(0, 0),      #MML
            (27, 27)]],
 'bss14': [113, 100, [(27, 27)]],   #MML
 'bss15': [74, 63, [(27, 27)]],    #DG
 'bss16': [75, 64, [(27, 27)]],    #DG
 'bss17': [93, 82, [(27, 27)]],    #Brr
 'bss18': [31, 22, [(27, 27)]],    #Brr
 'bss19': [32, 22, [(27, 27)]],    #Brr
 'bss20': [0, 0, [(8, 8),
           (9, 9),                 #Brr
           (27, 27)]],
 'bss21': [78, 67, [(27, 27)]],   #TTC
 'bss22': [79, 68, [(27, 27)]],   #TTC
 'bss23': [127, 114, [(27, 27)]], #TTC
 'bss24': [117, 104, [(27, 27)]], #DG
 'bss25': [80, 69, [(27, 27)]], #DG
 'bss26': [91, 80, [(27, 27)]], #DDL
 'bss27': [129, 116, [(27, 27)]], #DDL
 'bss28': [126, 113, [(27, 27)]], #DDL
 'bss31': [58, 47, [(27, 27)]],   #Holiday4th
 'bss32': [59, 48, [(27, 27)]],   #Holiday4th
 'bss33': [62, 51, [(27, 27)]],   #BackpackDG
 'bss34': [63, 52, [(27, 27)]],   #DDL
 'bss35': [65, 54, [(27, 27)]],   #TTC
 'bss36': [49, 38, [(27, 27)]], #DD
 'bss37': [50, 39, [(27, 27)]], #DD
 'bss38': [51, 40, [(27, 27)]],   #TTC
 'bss39': [52, 41, [(27, 27)]],   #Cowboynotaddedtotailorshop
 'bss40': [53, 42, [(27, 27)]],   #Cowboy
 'bss41': [54, 43, [(27, 27)]],   #Cowboy
 'bss42': [55, 44, [(27, 27)]],   #Cowboy
 'bss43': [56, 45, [(27, 27)]],   #Cowboy
 'bss44': [57, 46, [(27, 27)]],   #Cowboy
 'bss45': [33, 23, [(27, 27)]],   #BRR
 'bss46': [34, 23, [(27, 27)]],   #BRR
 'bss47': [26, 17, [(27, 27)]],   #BRR
 'bss48': [27, 18, [(27, 27)]],   #DD
 'bss49': [28, 19, [(27, 27)]],   #TTC
 'bss50': [46, 35, [(27, 27)]],   #DG
 'bss51': [66, 55, [(27, 27)]],   #BlueBRR
 'bss52': [67, 56, [(27, 27)]],   #RedDD
 'bss53': [68, 57, [(27, 27)]],   #PurpleDDL
 'bss54': [60, 49, [(27, 27)]],   #DG
 'bss55': [29, 20, [(27, 27)]],   #BRRghost
 'bss56': [30, 21, [(27, 27)]],   #BRRpumpkin
 'bss57': [45, 34, [(27, 27)]],   #TTC
 'bss58': [37, 26, [(27, 27)]],   #DG
 'bss59': [39, 28, [(27, 27)]],   #TTC
 'bss60': [47, 36, [(27, 27)]],   #BRR
 'bss61': [48, 37, [(27, 27)]],   #BRR
 'bss62': [147, 134, [(27, 27)]], #BRRanniversary
 'bss63': [119, 106, [(27, 27)]], #BRRbee
 'bss64': [105, 92, [(27, 27)]],  #BRRcogbuster
 'bss65': [123, 110, [(27, 27)]],  #BRRdinosaur
 'bss66': [82, 71, [(27, 27)]],  #DDgolf
 'bss67': [83, 72, [(27, 27)]],  #DDgolf
 'bss68': [125, 112, [(27, 27)]],  #DDgolf
 'bss69': [131, 118, [(27, 27)]],  #DDgolf
 'bss70': [138, 125, [(27, 27)]],  #DDgolf
 'bss71': [116, 103, [(27, 27)]],  #DDgreentoon
 'bss72': [115, 102, [(27, 27)]], #BRRturtle
 'bss73': [103, 90, [(27, 27)]],  #BRR
 'bss74': [85, 74, [(27, 27)]],   #BRRhalloween
 'bss75': [94, 83, [(27, 27)]],   #BRRhalloween
 'bss76': [95, 84, [(27, 27)]],   #BRRhalloween
 'bss77': [114, 101, [(27, 27)]], #BRRhalloween
 'bss78': [132, 119, [(27, 27)]], #BRRhalloween
 'bss79': [134, 121, [(27, 27)]], #BRRhalloween
 'bss80': [102, 89, [(27, 27)]],  #TTC
 'bss81': [100, 87, [(27, 27)]],  #TTC
 'bss82': [86, 75, [(27, 27)]],  #DDL
 'bss83': [106, 93, [(27, 27)]], #DDL
 'bss84': [141, 128, [(27, 27)]],#DDL
 'bss85': [142, 129, [(27, 27)]],#DDL
 'bss86': [76, 65, [(27, 27)]],  #DDLparty1
 'bss87': [77, 66, [(27, 27)]],  #DDLparty2
 'bss88': [118, 105, [(27, 27)]],#TTC
 'bss89': [87, 76, [(27, 27)]],   #MMLsavebuilding1
 'bss90': [128, 115, [(27, 27)]], #MMLsavebuilding3
 'bss91': [145, 132, [(27, 27)]], #DDLsavebuilding4
 'bss92': [146, 133, [(27, 27)]], #DDLsavebuilding5
 'bss93': [111, 98, [(27, 27)]], #DG
 'bss94': [110, 97, [(27, 27)]], #DG
 'bss95': [109, 96, [(27, 27)]], #DG
 'bss96': [81, 70, [(27, 27)]],  #DG
 'bss97': [92, 81, [(27, 27)]],   #MMLtrolley2
 'bss98': [122, 109, [(27, 27)]], #BRRvampire
 'bss99': [89, 78, [(27, 27)]],   #MML
 'bss100': [90, 79, [(27, 27)]],  #MML
 'bss101': [101, 88, [(27, 27)]], #DDL
 'bss102': [69, 58, [(27, 27)]],  #BRRvalentine
 'bss103': [70, 59, [(27, 27)]],  #BRRvalentine
 'bss104': [96, 85, [(27, 27)]],  #BRRvalentine
 'bss105': [107, 94, [(27, 27)]], #MML
 'bss106': [108, 95, [(27, 27)]], #BRR
 'bss107': [104, 91, [(27, 27)]], #MML
 'bss108': [133, 120, [(27, 27)]],#BRR
 'bss109': [148, 135, [(27, 27)]],#DDflannel
 'bss110': [97, 86, [(27, 27)]], #TTC
 'bss111': [98, 86, [(27, 27)]], #TTC
 'bss112': [99, 86, [(27, 27)]], #TTC
 'gss1': [0, 0, [(0, 0),
           (3, 3),
           (4, 4),
           (6, 6),
           (10, 10),      #Makeatoon
           (12, 12),
           (16, 16),
           (18, 18),
           (19, 19),
           (21, 21),
           (22, 22),
           (25, 25),
           (26, 26),
           (27, 27)]],
 'gss2': [1, 1, [(0, 0),
           (3, 3),
           (4, 4),
           (6, 6),
           (10, 10),      #Makeatoon
           (12, 12),
           (16, 16),
           (18, 18),
           (19, 19),
           (21, 21),
           (22, 22),
           (25, 25),
           (26, 26),
           (27, 27)]],
 'gss33': [2, 2, [(0, 0),
           (3, 3),
           (4, 4),
           (6, 6),
           (10, 10),      #Makeatoon
           (12, 12),
           (16, 16),
           (18, 18),
           (19, 19),
           (21, 21),
           (22, 22),
           (25, 25),
           (26, 26),
           (27, 27)]],
 'gss34': [20, 0, [(0, 0),
           (3, 3),
           (4, 4),
           (6, 6),
           (10, 10),      #Makeatoon
           (12, 12),
           (16, 16),
           (18, 18),
           (19, 19),
           (21, 21),
           (22, 22),
           (25, 25),
           (26, 26),
           (27, 27)]],
 'gss3': [31, 22, [(27, 27)]],#Snowman Shirt and sleeve    #Brr
 'gss4': [139, 126, [(27, 27)]],   #TTC
 'gss5': [140, 127, [(27, 27)]],   #TTC
 'gss6': [72, 61, [(27, 27)]],  #DonaldsDock
 'gss7': [73, 62, [(27, 27)]],  #DonaldsDock
 'gss8': [120, 107, [(27, 27)]],  #DonaldsDock
 'gss9': [88, 77, [(27, 27)]],  #DonaldsDock
 'gss10': [124, 111, [(27, 27)]],  #DonaldsDock
 'gss11': [137, 124, [(27, 27)]],  #DonaldsDock
 'gss12': [149, 136, [(22, 22),      #MML
            (25, 25)]],
 'gss13': [61, 50, [(27, 27)]],    #MML
 'gss14': [113, 100, [(27, 27)]],  #MML
 'gss15': [112, 99, [(27, 27)]],  #MML
 'gss16': [32, 22, [(27, 27)]],   #Brr
 'gss17': [135, 122, [(27, 27)]],  #Brr
 'gss18': [78, 67, [(27, 27)]],   #TTC
 'gss19': [79, 68, [(27, 27)]],   #TTC
 'gss20': [127, 114, [(27, 27)]], #TTC
 'gss21': [151, 138, [(15, 16), (22, 18), (26, 26)]], #MML
 'gss22': [74, 63, [(27, 27)]],   #DG
 'gss23': [75, 64, [(27, 27)]],   #DG
 'gss24': [117, 104, [(27, 27)]],   #DG
 'gss25': [80, 69, [(27, 27)]],   #DG
 'gss26': [64, 53, [(27, 27)]],   #DG
 'gss27': [91, 80, [(27, 27)]],   #DDL
 'gss28': [129, 116, [(27, 27)]],   #DDL
 'gss29': [150, 137, [(27, 27)]],  #DDBigCheese
 'gss30': [36, 25, [(27, 27)]],   #DDL
 'gss31': [38, 27, [(27, 27)]],   #DDL
 'gss32': [126, 113, [(27, 27)]], #DDL
 'gss35': [58, 47, [(27, 27)]],   #Holiday4th
 'gss36': [59, 48, [(27, 27)]],   #Holiday4th
 'gss37': [62, 51, [(27, 27)]],   #BackpackDG
 'gss38': [63, 52, [(27, 27)]],   #DDL
 'gss39': [65, 54, [(27, 27)]],   #TTC
 'gss40': [49, 38, [(27, 27)]], #DD
 'gss41': [50, 39, [(27, 27)]], #DD
 'gss42': [51, 40, [(27, 27)]],   #TTC
 'gss43': [52, 41, [(27, 27)]],   #Cowboynotaddedtotailorshop
 'gss44': [53, 42, [(27, 27)]],   #Cowboy
 'gss45': [54, 43, [(27, 27)]],   #Cowboy
 'gss46': [55, 44, [(27, 27)]],   #Cowboy
 'gss47': [56, 45, [(27, 27)]],   #Cowboy
 'gss48': [57, 46, [(27, 27)]],   #Cowboy
 'gss49': [23, 14, [(27, 27)]],   #DDL
 'gss50': [24, 15, [(27, 27)]],   #MML
 'gss51': [25, 16, [(27, 27)]],   #DDL
 'gss52': [40, 29, [(27, 27)]],   #DDL
 'gss53': [33, 23, [(27, 27)]],   #BRR
 'gss54': [34, 23, [(27, 27)]],   #BRR
 'gss55': [66, 55, [(27, 27)]],   #BlueBRR
 'gss56': [67, 56, [(27, 27)]],   #RedDD
 'gss57': [68, 57, [(27, 27)]],   #PurpleDDL
 'gss58': [60, 49, [(27, 27)]],   #DG
 'gss59': [29, 20, [(27, 27)]],   #BRRghost
 'gss60': [30, 21, [(27, 27)]],   #BRRpumpkin
 'gss61': [45, 34, [(27, 27)]],   #TTC
 'gss62': [47, 36, [(27, 27)]],   #BRR
 'gss63': [48, 37, [(27, 27)]],   #BRR
 'gss64': [147, 134, [(27, 27)]], #BRRanniversary
 'gss65': [119, 106, [(27, 27)]], #BRRbee
 'gss66': [105, 92, [(27, 27)]],  #BRRcogbuster
 'gss67': [123, 110, [(27, 27)]], #BRRdinosaur
 'gss68': [82, 71, [(27, 27)]],    #DDgolf
 'gss69': [83, 72, [(27, 27)]],    #DDgolf
 'gss70': [125, 112, [(27, 27)]],  #DDgolf
 'gss71': [131, 118, [(27, 27)]],  #DDgolf
 'gss72': [138, 125, [(27, 27)]],  #DDgolf
 'gss73': [116, 103, [(27, 27)]],  #DDgreentoon
 'gss74': [115, 102, [(27, 27)]], #BRRturtle
 'gss75': [103, 90, [(27, 27)]],  #BRR
 'gss76': [85, 74, [(27, 27)]],   #BRRhalloween
 'gss77': [94, 83, [(27, 27)]],   #BRRhalloween
 'gss78': [95, 84, [(27, 27)]],   #BRRhalloween
 'gss79': [114, 101, [(27, 27)]], #BRRhalloween
 'gss80': [132, 119, [(27, 27)]], #BRRhalloween
 'gss81': [134, 121, [(27, 27)]], #BRRhalloween
 'gss82': [102, 89, [(27, 27)]],  #TTC
 'gss83': [100, 87, [(27, 27)]],  #TTC
 'gss84': [86, 75, [(27, 27)]],  #DDL
 'gss85': [106, 93, [(27, 27)]], #DDL
 'gss86': [141, 128, [(27, 27)]],#DDL
 'gss87': [142, 129, [(27, 27)]],#DDL
 'gss88': [76, 65, [(27, 27)]],  #DDLparty1 
 'gss89': [77, 66, [(27, 27)]],  #DDLparty2
 'gss90': [118, 105, [(27, 27)]],#TTC
 'gss91': [87, 76, [(27, 27)]],   #MMLsavebuilding1
 'gss92': [128, 115, [(27, 27)]], #MMLsavebuilding3
 'gss93': [145, 132, [(27, 27)]], #DDLsavebuilding4
 'gss94': [146, 133, [(27, 27)]], #DDLsavebuilding5
 'gss95': [111, 98, [(27, 27)]], #DG
 'gss96': [110, 97, [(27, 27)]], #DG
 'gss97': [109, 96, [(27, 27)]], #DG
 'gss98': [81, 70, [(27, 27)]],  #DG
 'gss99': [92, 81, [(27, 27)]],   #MMLtrolley2
 'gss100': [122, 109, [(27, 27)]],#BRRvampire
 'gss101': [89, 78, [(27, 27)]],  #MML
 'gss102': [90, 79, [(27, 27)]],  #MML
 'gss103': [101, 88, [(27, 27)]], #DDL
 'gss104': [69, 58, [(27, 27)]],  #BRRvalentine
 'gss105': [70, 59, [(27, 27)]],  #BRRvalentine
 'gss106': [96, 85, [(27, 27)]],  #BRRvalentine
 'gss107': [107, 94, [(27, 27)]], #MML
 'gss108': [108, 95, [(27, 27)]], #BRR
 'gss109': [104, 91, [(27, 27)]], #MML
 'gss110': [133, 120, [(27, 27)]],#BRR
 'gss111': [97, 86, [(27, 27)]], #TTC
 'gss112': [98, 86, [(27, 27)]], #TTC
 'gss113': [99, 86, [(27, 27)]], #TTC
 'c_ss1': [25, 16, [(27, 27)]],
 'c_ss2': [27, 18, [(27, 27)]],
 'c_ss3': [38, 27, [(27, 27)]],
 'c_bss1': [26, 17, [(27, 27)]],
 'c_bss2': [28, 19, [(27, 27)]],
 'c_bss3': [37, 26, [(27, 27)]],
 'c_bss4': [39, 28, [(27, 27)]],
 'c_gss1': [23, 14, [(27, 27)]],
 'c_gss2': [24, 15, [(27, 27)]],
 'c_gss3': [35, 24, [(27, 27)]],
 'c_gss4': [36, 25, [(27, 27)]],
 'c_gss5': [40, 29, [(27, 27)]],
 'c_ss4': [45, 34, [(27, 27)]],
 'c_ss5': [46, 35, [(27, 27)]],
 'c_ss6': [52, 41, [(27, 27)]],
 'c_ss7': [53, 42, [(27, 27)]],
 'c_ss8': [54, 43, [(27, 27)]],
 'c_ss9': [55, 44, [(27, 27)]],
 'c_ss10': [56, 45, [(27, 27)]],
 'c_ss11': [57, 46, [(27, 27)]],
 'hw_ss1': [29, 20, [(27, 27)]],
 'hw_ss2': [30, 21, [(27, 27)]],
 'hw_ss3': [114, 101, [(27, 27)]],
 'hw_ss4': [115, 102, [(27, 27)]],
 'hw_ss5': [122, 109, [(27, 27)]],
 'hw_ss6': [123, 110, [(27, 27)]],
 'hw_ss7': [124, 111, [(27, 27)]],
 'hw_ss8': [125, 112, [(27, 27)]],
 'hw_ss9': [126, 113, [(27, 27)]],
 'wh_ss1': [31, 22, [(27, 27)]],
 'wh_ss2': [32, 22, [(27, 27)]],
 'wh_ss3': [33, 23, [(27, 27)]],
 'wh_ss4': [34, 23, [(27, 27)]],
 'vd_ss1': [41, 30, [(27, 27)]],
 'vd_ss2': [42, 31, [(27, 27)]],
 'vd_ss3': [43, 32, [(27, 27)]],
 'vd_ss4': [44, 33, [(27, 27)]],
 'vd_ss5': [69, 58, [(27, 27)]],
 'vd_ss6': [70, 59, [(27, 27)]],
 'vd_ss7': [96, 85, [(27, 27)]],
 'sd_ss1': [47, 36, [(27, 27)]],
 'sd_ss2': [48, 37, [(27, 27)]],
 'sd_ss3': [116, 103, [(27, 27)]],
 'tc_ss1': [49, 38, [(27, 27)]],
 'tc_ss2': [50, 39, [(27, 27)]],
 'tc_ss3': [51, 40, [(27, 27)]],
 'tc_ss4': [62, 51, [(27, 27)]],
 'tc_ss5': [63, 52, [(27, 27)]],
 'tc_ss6': [64, 53, [(27, 27)]],
 'tc_ss7': [65, 54, [(27, 27)]],
 'j4_ss1': [58, 47, [(27, 27)]],
 'j4_ss2': [59, 48, [(27, 27)]],
 'c_ss12': [60, 49, [(27, 27)]],
 'c_ss13': [61, 50, [(27, 27)]],
 'pj_ss1': [66, 55, [(27, 27)]],
 'pj_ss2': [67, 56, [(27, 27)]],
 'pj_ss3': [68, 57, [(27, 27)]],
 'sa_ss1': [71, 60, [(27, 27)]],
 'sa_ss2': [72, 61, [(27, 27)]],
 'sa_ss3': [73, 62, [(27, 27)]],
 'sa_ss4': [74, 63, [(27, 27)]],
 'sa_ss5': [75, 64, [(27, 27)]],
 'sa_ss6': [76, 65, [(27, 27)]],
 'sa_ss7': [77, 66, [(27, 27)]],
 'sa_ss8': [78, 67, [(27, 27)]],
 'sa_ss9': [79, 68, [(27, 27)]],
 'sa_ss10': [80, 69, [(27, 27)]],
 'sa_ss11': [81, 70, [(27, 27)]],
 'sa_ss12': [82, 71, [(27, 27)]],
 'sa_ss13': [83, 72, [(27, 27)]],
 'sa_ss14': [84, 73, [(27, 27)]],
 'sa_ss15': [85, 74, [(27, 27)]],
 'sa_ss16': [86, 75, [(27, 27)]],
 'sa_ss17': [87, 76, [(27, 27)]],
 'sa_ss18': [88, 77, [(27, 27)]],
 'sa_ss19': [89, 78, [(27, 27)]],
 'sa_ss20': [90, 79, [(27, 27)]],
 'sa_ss21': [91, 80, [(27, 27)]],
 'sa_ss22': [92, 81, [(27, 27)]],
 'sa_ss23': [93, 82, [(27, 27)]],
 'sa_ss24': [94, 83, [(27, 27)]],
 'sa_ss25': [95, 84, [(27, 27)]],
 'sa_ss26': [106, 93, [(27, 27)]],
 'sa_ss27': [110, 97, [(27, 27)]],
 'sa_ss28': [111, 98, [(27, 27)]],
 'sa_ss29': [120, 107, [(27, 27)]],
 'sa_ss30': [121, 108, [(27, 27)]],
 'sa_ss31': [118, 105, [(27, 27)]],
 'sa_ss32': [127, 114, [(27, 27)]],
 'sa_ss33': [128, 115, [(27, 27)]],
 'sa_ss34': [129, 116, [(27, 27)]],
 'sa_ss35': [130, 117, [(27, 27)]],
 'sa_ss36': [131, 118, [(27, 27)]],
 'sa_ss37': [132, 119, [(27, 27)]],
 'sa_ss38': [133, 120, [(27, 27)]],
 'sa_ss39': [134, 121, [(27, 27)]],
 'sa_ss40': [135, 122, [(27, 27)]],
 'sa_ss41': [136, 123, [(27, 27)]],
 'sa_ss42': [137, 124, [(27, 27)]],
 'sa_ss43': [138, 125, [(27, 27)]],
 'sa_ss44': [139, 126, [(27, 27)]],
 'sa_ss45': [140, 127, [(27, 27)]],
 'sa_ss46': [141, 128, [(27, 27)]],
 'sa_ss47': [142, 129, [(27, 27)]],
 'sa_ss48': [143, 130, [(27, 27)]],
 'sa_ss49': [144, 116, [(27, 27)]],
 'sa_ss50': [145, 131, [(27, 27)]],
 'sa_ss51': [146, 133, [(27, 27)]],
 'sa_ss52': [147, 134, [(27, 27)]],
 'sa_ss53': [148, 135, [(27, 27)]],
 'sa_ss54': [149, 136, [(27, 27)]],
 'sa_ss55': [150, 137, [(27, 27)]],
 'sc_1': [97, 86, [(27, 27)]],
 'sc_2': [98, 86, [(27, 27)]],
 'sc_3': [99, 86, [(27, 27)]],
 'sil_1': [100, 87, [(27, 27)]],
 'sil_2': [101, 88, [(27, 27)]],
 'sil_3': [102, 89, [(27, 27)]],
 'sil_4': [103, 90, [(27, 27)]],
 'sil_5': [104, 91, [(27, 27)]],
 'sil_6': [105, 92, [(27, 27)]],
 'sil_7': [107, 94, [(27, 27)]],
 'sil_8': [108, 95, [(27, 27)]],
 'emb_us1': [103, 90, [(27, 27)]],
 'emb_us2': [100, 87, [(27, 27)]],
 'emb_us3': [101, 88, [(27, 27)]],
 'sb_1': [109, 96, [(27, 27)]],
 'jb_1': [112, 99, [(27, 27)]],
 'jb_2': [113, 100, [(27, 27)]],
 'ugcms': [117, 104, [(27, 27)]],
 'lb_1': [119, 106, [(27, 27)]],
 'flannel': [148, 135, [(27, 27)]],
 'mml': [149, 136, [(27, 27)]],
 'big': [150, 137, [(27, 27)]],
 'mml': [151, 138, [(27, 27)]]}
BottomStyles = {'bbs1': [0, [0,
           3, 
           4,
           6,
           10,       #Makeatoon
           11,
           13, 
           15,
           16, 
           18, 
           19, 
           20, 
           22, 
           27]],
 'bbs2': [1, [0,
           3, 
           4,
           6,
           10,       #Makeatoon
           11,
           13, 
           15,
           16, 
           18, 
           19, 
           20, 
           22, 
           27]],
 'bbs3': [55, [27]], #TTC
 'bbs4': [56, [27]], #TTC
 'bbs5': [47, [27]],  #DonaldsDock
 'bbs6': [25, [27]],  #DonaldsDock
 'bbs7': [1, [4,           
           13,
           18,   #DonaldsDock
           27]],
 'bbs8': [7, [0,           
           4,      #DonaldsDock
           13,           
           15]],
 'bbs9': [19, [27]],   #Brr
 'bbs10': [20, [27]],  #Brr
 'bbs11': [0, [8,
           9,          #Brr
           27]],
 'bbs12': [16, [27]],  #Brr
 'bbs13': [28, [27]], #TTC
 'bbs14': [52, [27]], #TTC
 'bbs15': [0, [4]], #MML
 'bbs16': [34, [27]], #MML
 'bbs17': [57, [27]], #MML
 'bbs18': [26, [27]], #DG
 'bbs19': [30, [27]], #DD
 'bbs20': [58, [23,         
           27]], #DG
 'bbs21': [27, [27]], #DDL
 'bbs22': [14, [27]], #Holiday4th
 'bbs23': [12, [27]], #Cowboy
 'bbs24': [13, [27]], #Cowboy
 'bbs25': [21, [27]],  #Brrwinter3
 'bbs26': [22, [27]],  #Brr
 'bbs27': [1, [3, #TTC
           17,          
           27]],
 'bbs28': [17, [27]], #RedDD
 'bbs29': [18, [27]], #PurpleDDL
 'bbs30': [15, [27]], #DGCat7
 'bbs31': [9, [27]], #DDL
 'bbs32': [10, [27]], #BRR
 'bbs33': [11, [27]], #BRR
 'bbs34': [23, [27]], #BRRvalentine1
 'bbs35': [40, [27]], #BRRcogbuster
 'bbs36': [50, [27]], #BRRdinosaur
 'bbs37': [51, [27]], #DD
 'bbs38': [44, [27]], #DD
 'bbs39': [54, [27]], #DD
 'bbs40': [43, [27]], #BRRturtle
 'bbs41': [31, [27]], #BRRhalloween
 'bbs42': [32, [27]], #BRRhalloween
 'bbs43': [35, [27]], #BRRhalloween
 'bbs44': [36, [27]], #BRRhalloween
 'bbs45': [42, [27]], #BRRhalloween
 'bbs46': [45, [27]], #TTCgrandprix
 'bbs47': [33, [27]], #MMLsavebuilding1
 'bbs48': [41, [27]], #DG
 'bbs49': [29, [27]], #DG
 'bbs50': [24, [27]], #BRRvalentine2
 'bbs51': [48, [27]], #BRR
 'bbs52': [49, [27]], #BRR
 'bbs53': [37, [27]], #TTCscientist
 'bbs54': [38, [27]], #TTCscientist
 'bbs55': [39, [27]], #TTCscientist
 'vd_bs1': [8, [27]],
 'vd_bs2': [23, [27]],
 'vd_bs3': [24, [27]],
 'c_bs1': [9, [27]],
 'c_bs2': [10, [27]],
 'c_bs5': [15, [27]],
 'sd_bs1': [11, [27]],
 'sd_bs2': [44, [27]],
 'pj_bs1': [16, [27]],
 'pj_bs2': [17, [27]],
 'pj_bs3': [18, [27]],
 'wh_bs1': [19, [27]],
 'wh_bs2': [20, [27]],
 'wh_bs3': [21, [27]],
 'wh_bs4': [22, [27]],
 'hw_bs1': [47, [27]],
 'hw_bs2': [48, [27]],
 'hw_bs5': [49, [27]],
 'hw_bs6': [50, [27]],
 'hw_bs7': [51, [27]],
 'c_bs17': [57, [27]],
 'c_bs20': [58, [27]],
 'gsk1': [0, [0,
           3,
           4,
           6,
           10,      #Makeatoon
           12,
           16,
           18,
           19,
           21,
           22,
           25,
           26,
           27]],
 'gsk2': [60, [27]],  #TTC
 'gsk3': [29, [0,
           27]],     #DonaldsDock
 'gsk4': [3, [5,     #DonaldsDock          
           22,
           27]],
 'gsk5': [52, [27]], #DonaldsDock
 'gsk6': [38, [27]],    #MML
 'gsk7': [58, [27]],  #DDL
 'gsk8': [23, [27]],  #Brr
 'gsk9': [24, [27]],  #Brr
 'gsk10': [0, [27]],   #Brr
 'gsk11': [62, [27]],  #Brrdesatskirt40
 'gsk12': [61, [27]],  #TTC
 'gsk13': [32, [27]],  #TTC
 'gsk14': [57, [27]],  #TTC
 'gsk15': [63, [0,
           1,
           27]],  #MML
 'gsk16': [30, [27]],  #TTC
 'gsk17': [33, [27]],  #DG
 'gsk18': [56, [27]],  #DG
 'gsk19': [34, [27]],  #MML
 'gsk20': [19, [27]],  #DG
 'gsk21': [0, [4,
           7,
           11,
           14]],  #DDL
 'gsk22': [37, [27]],  #MML
 'gsk23': [18, [27]],  #Holiday4th
 'gsk24': [16, [27]],  #CowboynoCOWBOYaddedyettoanytailor
 'gsk25': [17, [27]],  #Cowboy
 'gsk26': [10, [27]],  #DDL
 'gsk27': [11, [27]],  #MML
 'gsk28': [12, [27]],  #DDL
 'gsk29': [0, [3,      #TTC          
           27]],
 'gsk30': [25, [27]],  #BRR
 'gsk31': [26, [27]],  #BRR
 'gsk32': [14, [27]],  #TTCskirtnew5
 'gsk33': [59, [27]],  #DDgolf04
 'gsk34': [48, [27]],  #DDgreentoon
 'gsk35': [35, [27]],  #BRRhalloween
 'gsk36': [36, [27]],  #BRRhalloween
 'gsk37': [39, [27]],  #BRRhalloween
 'gsk38': [40, [27]],  #BRRhalloween
 'gsk39': [49, [27]],  #TTCgrandprix
 'gsk40': [31, [27]],  #DDLparty1
 'gsk41': [27, [27]],  #BRR
 'gsk42': [28, [27]],  #BRR
 'gsh1': [5, [0,
           3,
           4,
           6,
           10,       #Makeatoon
           12, 
           16,
           18,
           19, 
           21, 
           22, 
           25, 
           26,
           27]],
 'gsh2': [5, [3, #TTC
           17,          
           27]],
 'gsh3': [9, [3,     #DonaldsDock
           6,           
           23]],
 'gsh4': [5, [8,
           9,      #Brr
           27]],
 'gsh5': [64, [8,
          12,
          21]],       #MML          
 'gsh6': [6, [4,
           18,       #DG
           27]],
 'gsh7': [5, [4,
            11,
            14]], #DDL
 'gsh8': [22, [27]], #PurpleDDL
 'gsh9': [20, [27]], #BlueBRR
 'gsh10': [21, [27]], #RedDD
 'gsh11': [50, [27]], #BRRbee
 'gsh12': [44, [27]], #BRRcogbuster
 'gsh13': [55, [27]], #BRRdinosaur
 'gsh14': [47, [27]], #BRRturtle
 'gsh15': [46, [27]], #BRRhalloween
 'gsh16': [45, [27]], #DG
 'gsh17': [53, [27]], #BRR
 'gsh18': [54, [27]], #BRR
 'gsh19': [41, [27]], #TTCscientist
 'gsh20': [42, [27]], #TTCscientist
 'gsh21': [43, [27]], #TTCscientist
 'c_gsk1': [10, [27]],
 'c_gsk2': [11, [27]],
 'c_gsk3': [12, [27]],
 'vd_gs1': [13, [27]],
 'vd_gs2': [27, [27]],
 'vd_gs3': [28, [27]],
 'c_gsk4': [14, [27]],
 'sd_gs1': [15, [27]],
 'sd_gs2': [48, [27]],
 'c_gsk5': [16, [27]],
 'c_gsk6': [17, [27]],
 'c_bs3': [12, [27]],
 'c_bs4': [13, [27]],
 'j4_bs1': [14, [27]],
 'j4_gs1': [18, [27]],
 'c_gsk7': [19, [27]],
 'pj_gs1': [20, [27]],
 'pj_gs2': [21, [27]],
 'pj_gs3': [22, [27]],
 'wh_gsk1': [23, [27]],
 'wh_gsk2': [24, [27]],
 'wh_gsk3': [25, [27]],
 'wh_gsk4': [26, [27]],
 'sa_bs1': [25, [27]],
 'sa_bs2': [26, [27]],
 'sa_bs3': [27, [27]],
 'sa_bs4': [28, [27]],
 'sa_bs5': [29, [27]],
 'sa_bs6': [30, [27]],
 'sa_bs7': [31, [27]],
 'sa_bs8': [32, [27]],
 'sa_bs9': [33, [27]],
 'sa_bs10': [34, [27]],
 'sa_bs11': [35, [27]],
 'sa_bs12': [36, [27]],
 'sa_bs13': [41, [27]],
 'sa_bs14': [46, [27]],
 'sa_bs15': [45, [27]],
 'sa_bs16': [52, [27]],
 'sa_bs17': [53, [27]],
 'sa_bs18': [54, [27]],
 'sa_bs19': [55, [27]],
 'sa_bs20': [56, [27]],
 'sa_bs21': [57, [27]],
 'sa_gs1': [29, [27]],
 'sa_gs2': [30, [27]],
 'sa_gs3': [31, [27]],
 'sa_gs4': [32, [27]],
 'sa_gs5': [33, [27]],
 'sa_gs6': [34, [27]],
 'sa_gs7': [35, [27]],
 'sa_gs8': [36, [27]],
 'sa_gs9': [37, [27]],
 'sa_gs10': [38, [27]],
 'sa_gs11': [39, [27]],
 'sa_gs12': [40, [27]],
 'sa_gs13': [45, [27]],
 'sa_gs14': [50, [27]],
 'sa_gs15': [49, [27]],
 'sa_gs16': [57, [27]],
 'sa_gs17': [58, [27]],
 'sa_gs18': [59, [27]],
 'sa_gs19': [60, [27]],
 'sa_gs20': [61, [27]],
 'sa_gs21': [62, [27]],
 'sc_bs1': [37, [27]],
 'sc_bs2': [38, [27]],
 'sc_bs3': [39, [27]],
 'sc_gs1': [41, [27]],
 'sc_gs2': [42, [27]],
 'sc_gs3': [43, [27]],
 'sil_bs1': [40, [27]],
 'sil_gs1': [44, [27]],
 'hw_bs3': [42, [27]],
 'hw_gs3': [46, [27]],
 'hw_bs4': [43, [27]],
 'hw_gs4': [47, [27]],
 'hw_gs1': [51, [27]],
 'hw_gs2': [52, [27]],
 'hw_gs5': [54, [27]],
 'hw_gs6': [55, [27]],
 'hw_gs7': [56, [27]],
 'hw_gsk1': [53, [27]],
 'nig2': [57, [27]],
 'c_gsk11': [62, [27]],
 'c_gsk15': [63, [27]],
 'c_gsh5': [64, [27]]}
MAKE_A_TOON = 1
TAMMY_TAILOR = 2004
LONGJOHN_LEROY = 1007
TAILOR_HARMONY = 4008
BONNIE_BLOSSOM = 5007
WARREN_BUNDLES = 3008
WORNOUT_WAYLON = 9010
TAILOR_BALER = 7029
TAILOR_SPURS = 14030
TAILOR_BOLT = 21003
TailorCollections = {MAKE_A_TOON: [['bss1', 'bss2', 'bss29', 'bss30', 'bss57'],
               ['gss1', 'gss2', 'gss33', 'gss34'],
               ['bbs1', 'bbs2'],
               ['gsk1', 'gsh1']],
 TAMMY_TAILOR: [['bss3', 'bss4', 'bss21', 'bss22', 'bss23', 'bss35', 'bss38', 'bss49', 'bss59', 'bss80', 'bss81', 'bss88', 'bss110', 'bss111', 'bss112'],
                ['gss4', 'gss5', 'gss18', 'gss19', 'gss20', 'gss39', 'gss42', 'gss61', 'gss82', 'gss83', 'gss90', 'gss111', 'gss112', 'gss113'],
                ['bbs3', 'bbs4', 'bbs13', 'bbs14', 'bbs27', 'bbs46', 'bbs53', 'bbs54', 'bbs55'],
                ['gsk2', 'gsk12', 'gsk13', 'gsk14', 'gsk29', 'gsk32', 'gsk39', 'gsh2', 'gsh19', 'gsh20', 'gsh21']],
 LONGJOHN_LEROY: [['bss6', 'bss7', 'bss8', 'bss9', 'bss10', 'bss11', 'bss12', 'bss36', 'bss37', 'bss48', 'bss52', 'bss66', 'bss67', 'bss68', 'bss69', 'bss70', 'bss71', 'bss109'],
                  ['gss6', 'gss7', 'gss8', 'gss9', 'gss10', 'gss11', 'gss29', 'gss40', 'gss41', 'gss56', 'gss68', 'gss69', 'gss70', 'gss71', 'gss72', 'gss73'],
                  ['bbs5', 'bbs6', 'bbs7', 'bbs8', 'bbs19', 'bbs28', 'bbs37', 'bbs38', 'bbs39'],
                  ['gsk3', 'gsk4', 'gsk5', 'gsk33', 'gsk34', 'gsh3', 'gsh10']],
 TAILOR_HARMONY: [['bss5', 'bss13', 'bss14', 'bss89', 'bss90', 'bss97', 'bss99', 'bss100', 'bss105', 'bss107'],
                  ['gss12', 'gss14', 'gss15', 'gss21', 'gss50', 'gss91', 'gss92', 'gss99', 'gss101', 'gss102', 'gss107', 'gss109'], 
                  ['bbs15', 'bbs16', 'bbs17', 'bbs47'],
                  ['gsk6', 'gsk15', 'gsk19', 'gsk22', 'gsk27', 'gsh5']],
 BONNIE_BLOSSOM: [['bss15', 'bss16', 'bss24', 'bss25', 'bss33', 'bss50', 'bss54', 'bss58', 'bss93', 'bss94', 'bss95', 'bss96'],
                  ['gss13', 'gss22', 'gss23', 'gss24', 'gss25', 'gss26', 'gss37', 'gss58', 'gss95', 'gss96', 'gss97', 'gss98'],
                  ['bbs18', 'bbs20', 'bbs30', 'bbs48', 'bbs49'],
                  ['gsk16', 'gsk17', 'gsk18', 'gsk20', 'gsh6', 'gsh16']],
 WARREN_BUNDLES: [['bss17', 'bss18', 'bss19', 'bss20', 'bss31', 'bss32', 'bss45', 'bss46', 'bss47', 'bss51', 'bss55', 'bss56', 'bss60', 'bss61', 'bss62', 'bss63', 'bss64', 'bss65', 'bss72', 'bss73', 'bss74', 'bss75', 'bss76', 'bss77', 'bss78', 'bss79', 'bss98', 'bss102', 'bss103', 'bss104', 'bss106', 'bss108'],
                  ['gss3', 'gss16', 'gss17', 'gss35', 'gss36', 'gss53', 'gss54', 'gss55', 'gss59', 'gss60', 'gss62', 'gss63', 'gss64', 'gss65', 'gss66', 'gss67', 'gss74', 'gss75', 'gss76', 'gss77', 'gss78', 'gss79', 'gss80', 'gss81', 'gss100', 'gss104', 'gss105', 'gss106', 'gss108', 'gss110'],
                  ['bbs9', 'bbs10', 'bbs11', 'bbs12', 'bbs22', 'bbs25', 'bbs26', 'bbs32', 'bbs33', 'bbs34', 'bbs35', 'bbs36', 'bbs40', 'bbs41', 'bbs42', 'bbs43', 'bbs44', 'bbs45', 'bbs50', 'bbs51', 'bbs52'],
                  ['gsk8', 'gsk9', 'gsk10', 'gsk11', 'gsk23', 'gsk30', 'gsk31', 'gsk35', 'gsk36', 'gsk37', 'gsk38', 'gsk41', 'gsk42', 'gsh4', 'gsh9', 'gsh11', 'gsh12', 'gsh13', 'gsh14', 'gsh15', 'gsh17', 'gsh18']],
 WORNOUT_WAYLON: [['bss26', 'bss27', 'bss28', 'bss34', 'bss53', 'bss82', 'bss83', 'bss84', 'bss85', 'bss86', 'bss87', 'bss91', 'bss92', 'bss101'],
                  ['gss27', 'gss28', 'gss30', 'gss31', 'gss32', 'gss38', 'gss49', 'gss51', 'gss52', 'gss57', 'gss84', 'gss85', 'gss86', 'gss87', 'gss88', 'gss89', 'gss93', 'gss94', 'gss103'],
                  ['bbs8', 'bbs21', 'bbs29', 'bbs31'],
                  ['gsk7', 'gsk21', 'gsk26', 'gsk28', 'gsk40', 'gsh7', 'gsh8']],
 TAILOR_BALER: [['bss26', 'bss27', 'bss28', 'bss34', 'bss53', 'bss82', 'bss83', 'bss84', 'bss85', 'bss86', 'bss87', 'bss91', 'bss92', 'bss101'],
                ['gss27', 'gss28', 'gss30', 'gss31', 'gss32', 'gss38', 'gss49', 'gss51', 'gss52', 'gss57', 'gss84', 'gss85', 'gss86', 'gss87', 'gss88', 'gss89', 'gss93', 'gss94', 'gss103'],
                ['bbs8', 'bbs21', 'bbs29', 'bbs31'],
                ['gsk7', 'gsk21', 'gsk26', 'gsk28', 'gsk40', 'gsh7', 'gsh8']],
 TAILOR_SPURS: [['bss26', 'bss27', 'bss28', 'bss34', 'bss53', 'bss82', 'bss83', 'bss84', 'bss85', 'bss86', 'bss87', 'bss91', 'bss92', 'bss101'],
                ['gss27', 'gss28', 'gss30', 'gss31', 'gss32', 'gss38', 'gss49', 'gss51', 'gss52', 'gss57', 'gss84', 'gss85', 'gss86', 'gss87', 'gss88', 'gss89', 'gss93', 'gss94', 'gss103'],
                ['bbs8', 'bbs21', 'bbs29', 'bbs31'],
                ['gsk7', 'gsk21', 'gsk26', 'gsk28', 'gsk40', 'gsh7', 'gsh8']],
 TAILOR_BOLT: [['bss26', 'bss27', 'bss28', 'bss34', 'bss53', 'bss82', 'bss83', 'bss84', 'bss85', 'bss86', 'bss87', 'bss91', 'bss92', 'bss101'],
               ['gss27', 'gss28', 'gss30', 'gss31', 'gss32', 'gss38', 'gss49', 'gss51', 'gss52', 'gss57', 'gss84', 'gss85', 'gss86', 'gss87', 'gss88', 'gss89', 'gss93', 'gss94', 'gss103'],
               ['bbs8', 'bbs21', 'bbs29', 'bbs31'],
               ['gsk7', 'gsk21', 'gsk26', 'gsk28', 'gsk40', 'gsh7', 'gsh8']]}

BOY_SHIRTS = 0
GIRL_SHIRTS = 1
BOY_SHORTS = 2
GIRL_BOTTOMS = 3
HAT = 1
GLASSES = 2
BACKPACK = 4
SHOES = 8
MakeAToonBoyBottoms = []
MakeAToonBoyShirts = []
MakeAToonGirlBottoms = []
MakeAToonGirlShirts = []
MakeAToonGirlSkirts = []
MakeAToonGirlShorts = []

#Combine all tailors into MAKE_A_TOON tailor.
if mergeMATTailor:
    pass

for style in TailorCollections[MAKE_A_TOON][BOY_SHORTS]:
    index = BottomStyles[style][0]
    MakeAToonBoyBottoms.append(index)

for style in TailorCollections[MAKE_A_TOON][BOY_SHIRTS]:
    index = ShirtStyles[style][0]
    MakeAToonBoyShirts.append(index)

for style in TailorCollections[MAKE_A_TOON][GIRL_BOTTOMS]:
    index = BottomStyles[style][0]
    MakeAToonGirlBottoms.append(index)

for style in TailorCollections[MAKE_A_TOON][GIRL_SHIRTS]:
    index = ShirtStyles[style][0]
    MakeAToonGirlShirts.append(index)

for index in MakeAToonGirlBottoms:
    flag = GirlBottoms[index][1]
    if flag == SKIRT:
        MakeAToonGirlSkirts.append(index)
    elif flag == SHORTS:
        MakeAToonGirlShorts.append(index)
    else:
        notify.error('Invalid flag')

def getRandomTop(gender, tailorId = MAKE_A_TOON, generator = None):
    if generator == None:
        generator = random
    collection = TailorCollections[tailorId]
    if gender == 'm':
        style = generator.choice(collection[BOY_SHIRTS])
    else:
        style = generator.choice(collection[GIRL_SHIRTS])
    styleList = ShirtStyles[style]
    colors = generator.choice(styleList[2])
    return (styleList[0],
     colors[0],
     styleList[1],
     colors[1])


def getRandomBottom(gender, tailorId = MAKE_A_TOON, generator = None, girlBottomType = None):
    if generator == None:
        generator = random
    collection = TailorCollections[tailorId]
    if gender == 'm':
        style = generator.choice(collection[BOY_SHORTS])
    elif girlBottomType is None:
        style = generator.choice(collection[GIRL_BOTTOMS])
    elif girlBottomType == SKIRT:
        skirtCollection = filter(lambda style: GirlBottoms[BottomStyles[style][0]][1] == SKIRT, collection[GIRL_BOTTOMS])
        style = generator.choice(skirtCollection)
    elif girlBottomType == SHORTS:
        shortsCollection = filter(lambda style: GirlBottoms[BottomStyles[style][0]][1] == SHORTS, collection[GIRL_BOTTOMS])
        style = generator.choice(shortsCollection)
    else:
        notify.error('Bad girlBottomType: %s' % girlBottomType)
    styleList = BottomStyles[style]
    color = generator.choice(styleList[1])
    return (styleList[0], color)


def getRandomGirlBottom(type):
    bottoms = []
    index = 0
    for bottom in GirlBottoms:
        if bottom[1] == type:
            bottoms.append(index)
        index += 1

    return random.choice(bottoms)


def getRandomGirlBottomAndColor(type):
    bottoms = []
    if type == SHORTS:
        typeStr = 'gsh'
    else:
        typeStr = 'gsk'
    for bottom in BottomStyles.keys():
        if bottom.find(typeStr) >= 0:
            bottoms.append(bottom)

    style = BottomStyles[random.choice(bottoms)]
    return (style[0], random.choice(style[1]))


def getRandomizedTops(gender, tailorId = MAKE_A_TOON, generator = None):
    if generator == None:
        generator = random
    collection = TailorCollections[tailorId]
    if gender == 'm':
        collection = collection[BOY_SHIRTS][:]
    else:
        collection = collection[GIRL_SHIRTS][:]
    tops = []
    random.shuffle(collection)
    for style in collection:
        colors = ShirtStyles[style][2][:]
        random.shuffle(colors)
        for color in colors:
            tops.append((ShirtStyles[style][0],
             color[0],
             ShirtStyles[style][1],
             color[1]))

    return tops


def getRandomizedBottoms(gender, tailorId = MAKE_A_TOON, generator = None):
    if generator == None:
        generator = random
    collection = TailorCollections[tailorId]
    if gender == 'm':
        collection = collection[BOY_SHORTS][:]
    else:
        collection = collection[GIRL_BOTTOMS][:]
    bottoms = []
    random.shuffle(collection)
    for style in collection:
        colors = BottomStyles[style][1][:]
        random.shuffle(colors)
        for color in colors:
            bottoms.append((BottomStyles[style][0], color))

    return bottoms


def getTops(gender, tailorId = MAKE_A_TOON):
    if gender == 'm':
        collection = TailorCollections[tailorId][BOY_SHIRTS]
    else:
        collection = TailorCollections[tailorId][GIRL_SHIRTS]
    tops = []
    for style in collection:
        for color in ShirtStyles[style][2]:
            tops.append((ShirtStyles[style][0],
             color[0],
             ShirtStyles[style][1],
             color[1]))

    return tops


def getAllTops(gender):
    tops = []
    for style in ShirtStyles.keys():
        if gender == 'm':
            if style[0] == 'g' or style[:3] == 'c_g':
                continue
        elif style[0] == 'b' or style[:3] == 'c_b':
            continue
        for color in ShirtStyles[style][2]:
            tops.append((ShirtStyles[style][0],
             color[0],
             ShirtStyles[style][1],
             color[1]))

    return tops


def getBottoms(gender, tailorId = MAKE_A_TOON):
    if gender == 'm':
        collection = TailorCollections[tailorId][BOY_SHORTS]
    else:
        collection = TailorCollections[tailorId][GIRL_BOTTOMS]
    bottoms = []
    for style in collection:
        for color in BottomStyles[style][1]:
            bottoms.append((BottomStyles[style][0], color))

    return bottoms


def getAllBottoms(gender, output = 'both'):
    bottoms = []
    for style in BottomStyles.keys():
        if gender == 'm':
            if style[0] == 'g' or style[:3] == 'c_g' or style[:4] == 'vd_g' or style[:4] == 'sd_g' or style[:4] == 'j4_g' or style[:4] == 'pj_g' or style[:4] == 'wh_g' or style[:4] == 'sa_g' or style[:4] == 'sc_g' or style[:5] == 'sil_g' or style[:4] == 'hw_g':
                continue
        elif style[0] == 'b' or style[:3] == 'c_b' or style[:4] == 'vd_b' or style[:4] == 'sd_b' or style[:4] == 'j4_b' or style[:4] == 'pj_b' or style[:4] == 'wh_b' or style[:4] == 'sa_b' or style[:4] == 'sc_b' or style[:5] == 'sil_b' or style[:4] == 'hw_b':
            continue
        bottomIdx = BottomStyles[style][0]
        if gender == 'f':
            textureType = GirlBottoms[bottomIdx][1]
        else:
            textureType = SHORTS
        if output == 'both' or output == 'skirts' and textureType == SKIRT or output == 'shorts' and textureType == SHORTS:
            for color in BottomStyles[style][1]:
                bottoms.append((bottomIdx, color))

    return bottoms


allColorsList = [(1.0, 1.0, 1.0, 1.0),
 (0.96, 0.69, 0.69, 1.0),
 (0.93, 0.26, 0.28, 1.0),
 (0.86, 0.40, 0.41, 1.0),
 (0.71, 0.23, 0.43, 1.0),
 (0.57, 0.44, 0.16, 1.0),
 (0.64, 0.35, 0.26, 1.0),
 (0.99, 0.69, 0.51, 1.0),
 (0.83, 0.5, 0.29, 1.0),
 (0.99, 0.48, 0.16, 1.0),
 (0.99, 0.89, 0.32, 1.0),
 (0.99, 0.95, 0.59, 1.0),
 (0.85, 0.93, 0.49, 1.0),
 (0.55, 0.82, 0.32, 1.0),
 (0.24, 0.74, 0.51, 1.0),
 (0.30, 0.96, 0.4, 1.0),
 (0.43, 0.9, 0.83, 1.0),
 (0.34, 0.82, 0.95, 1.0),
 (0.19, 0.56, 0.77, 1.0),
 (0.55, 0.58, 0.87, 1.0),
 (0.28, 0.32, 0.72, 1.0),
 (0.46, 0.37, 0.82, 1.0),
 (0.54, 0.28, 0.75, 1.0),
 (0.72, 0.47, 0.85, 1.0),
 (0.89, 0.61, 0.9, 1.0),
 (0.7, 0.7, 0.8, 1.0),
 (0.3, 0.3, 0.35, 1.0),
 (0.0, 0.63, 0.25, 1.0),
 (0.67, 0.92, 1.0, 1.0),
 (0.98, 0.89, 0.74, 1.0),
 (0.74, 1.0, 0.84, 1.0),
 (0.47, 0.44, 0.44, 1.0),
 (0.99, 0.25, 0.39, 1.0),
 (0.81, 0.7, 0.23, 1.0),
 (0.74, 0.75, 0.76, 1.0),
 (1.0, 0.63, 0.26, 1.0),
 (0.0, 0.4, 0.64, 1.0),
 (0.86, 0.07, 0.23, 1.0),
 (0.0, 0.63, 0.51, 1.0),
 (0.8, 0.49, 0.19, 1.0),
 (0.224, 1.0, 0.078, 1.0),
 (0.192, 0.353, 0.49, 1.0)]
defaultColorList = [0,
 1,
 32,
 2,
 3,
 4,
 5,
 6,
 7,
 29,
 8,
 37,
 35,
 9,
 10,
 33,
 11,
 12,
 30,
 13,
 14,
 15,
 39,
 27,
 28,
 16,
 17,
 18,
 19,
 20,
 21,
 38,
 40,
 41,
 36,
 22,
 23,
 24,
 25,
 34,
 31,
 26]
HatModels = [None,
 'phase_4/models/accessories/tt_m_chr_avt_acc_hat_baseball',
 'phase_4/models/accessories/tt_m_chr_avt_acc_hat_safari',
 'phase_4/models/accessories/tt_m_chr_avt_acc_hat_ribbon',
 'phase_4/models/accessories/tt_m_chr_avt_acc_hat_heart',
 'phase_4/models/accessories/tt_m_chr_avt_acc_hat_topHat',
 'phase_4/models/accessories/tt_m_chr_avt_acc_hat_anvil',
 'phase_4/models/accessories/tt_m_chr_avt_acc_hat_flowerPot',
 'phase_4/models/accessories/tt_m_chr_avt_acc_hat_sandbag',
 'phase_4/models/accessories/tt_m_chr_avt_acc_hat_weight',
 'phase_4/models/accessories/tt_m_chr_avt_acc_hat_fez',
 'phase_4/models/accessories/tt_m_chr_avt_acc_hat_golfHat',
 'phase_4/models/accessories/tt_m_chr_avt_acc_hat_partyHat',
 'phase_4/models/accessories/tt_m_chr_avt_acc_hat_pillBox',
 'phase_4/models/accessories/tt_m_chr_avt_acc_hat_crown',
 'phase_4/models/accessories/tt_m_chr_avt_acc_hat_cowboyHat',
 'phase_4/models/accessories/tt_m_chr_avt_acc_hat_pirateHat',
 'phase_4/models/accessories/tt_m_chr_avt_acc_hat_propellerHat',
 'phase_4/models/accessories/tt_m_chr_avt_acc_hat_fishingHat',
 'phase_4/models/accessories/tt_m_chr_avt_acc_hat_sombreroHat',
 'phase_4/models/accessories/tt_m_chr_avt_acc_hat_strawHat',
 'phase_4/models/accessories/tt_m_chr_avt_acc_hat_sunHat',
 'phase_4/models/accessories/tt_m_chr_avt_acc_hat_antenna',
 'phase_4/models/accessories/tt_m_chr_avt_acc_hat_beeHiveHairdo',
 'phase_4/models/accessories/tt_m_chr_avt_acc_hat_bowler',
 'phase_4/models/accessories/tt_m_chr_avt_acc_hat_chefsHat',
 'phase_4/models/accessories/tt_m_chr_avt_acc_hat_detective',
 'phase_4/models/accessories/tt_m_chr_avt_acc_hat_feathers',
 'phase_4/models/accessories/tt_m_chr_avt_acc_hat_fedora',
 'phase_4/models/accessories/tt_m_chr_avt_acc_hat_mickeysBandConductorHat',
 'phase_4/models/accessories/tt_m_chr_avt_acc_hat_nativeAmericanFeather',
 'phase_4/models/accessories/tt_m_chr_avt_acc_hat_pompadorHairdo',
 'phase_4/models/accessories/tt_m_chr_avt_acc_hat_princess',
 'phase_4/models/accessories/tt_m_chr_avt_acc_hat_robinHoodHat',
 'phase_4/models/accessories/tt_m_chr_avt_acc_hat_romanHelmet',
 'phase_4/models/accessories/tt_m_chr_avt_acc_hat_spiderAntennaThingy',
 'phase_4/models/accessories/tt_m_chr_avt_acc_hat_tiara',
 'phase_4/models/accessories/tt_m_chr_avt_acc_hat_vikingHelmet',
 'phase_4/models/accessories/tt_m_chr_avt_acc_hat_witch',
 'phase_4/models/accessories/tt_m_chr_avt_acc_hat_wizard',
 'phase_4/models/accessories/tt_m_chr_avt_acc_hat_conquistadorHelmet',
 'phase_4/models/accessories/tt_m_chr_avt_acc_hat_firefighterHelmet',
 'phase_4/models/accessories/tt_m_chr_avt_acc_hat_foilPyramid',
 'phase_4/models/accessories/tt_m_chr_avt_acc_hat_minersHardhatWithLight',
 'phase_4/models/accessories/tt_m_chr_avt_acc_hat_napoleonHat',
 'phase_4/models/accessories/tt_m_chr_avt_acc_hat_pilotsCap',
 'phase_4/models/accessories/tt_m_chr_avt_acc_hat_policeHat',
 'phase_4/models/accessories/tt_m_chr_avt_acc_hat_rainbowAfroWig',
 'phase_4/models/accessories/tt_m_chr_avt_acc_hat_sailorHat',
 'phase_4/models/accessories/tt_m_chr_avt_acc_hat_carmenMirandaFruitHat',
 'phase_4/models/accessories/tt_m_chr_avt_acc_hat_bobbyHat',
 'phase_4/models/accessories/tt_m_chr_avt_acc_hat_jugheadHat',
 'phase_4/models/accessories/tt_m_chr_avt_acc_hat_winter',
 'phase_4/models/accessories/tt_m_chr_avt_acc_hat_bandana',
 'phase_4/models/accessories/tt_m_chr_avt_acc_hat_dinosaur',
 'phase_4/models/accessories/tt_m_chr_avt_acc_hat_band',
 'phase_4/models/accessories/tt_m_chr_avt_acc_hat_birdNest',
 'phase_4/models/accessories/tt_m_chr_avt_acc_hat_mousekateer']
HatTextures = [None,
 'phase_4/maps/tt_t_chr_avt_acc_hat_ribbonRed.jpg',
 'phase_4/maps/tt_t_chr_avt_acc_hat_ribbonPurple.jpg',
 'phase_4/maps/tt_t_chr_avt_acc_hat_heartYellow.jpg',
 'phase_4/maps/tt_t_chr_avt_acc_hat_topHatBlue.jpg',
 'phase_4/maps/tt_t_chr_avt_acc_hat_safariBrown.jpg',
 'phase_4/maps/tt_t_chr_avt_acc_hat_safariGreen.jpg',
 'phase_4/maps/tt_t_chr_avt_acc_hat_baseballBlue.jpg',
 'phase_4/maps/tt_t_chr_avt_acc_hat_baseballOrange.jpg',
 'phase_4/maps/tt_t_chr_avt_acc_hat_ribbonYellow.jpg',
 'phase_4/maps/tt_t_chr_avt_acc_hat_ribbonChecker.jpg',
 'phase_4/maps/tt_t_chr_avt_acc_hat_ribbonLtRed.jpg',
 'phase_4/maps/tt_t_chr_avt_acc_hat_ribbonRainbow.jpg',
 'phase_4/maps/tt_t_chr_avt_acc_hat_baseballYellow.jpg',
 'phase_4/maps/tt_t_chr_avt_acc_hat_baseballRed.jpg',
 'phase_4/maps/tt_t_chr_avt_acc_hat_baseballTeal.jpg',
 'phase_4/maps/tt_t_chr_avt_acc_hat_ribbonPinkDots.jpg',
 'phase_4/maps/tt_t_chr_avt_acc_hat_baseballPurple.jpg',
 'phase_4/maps/tt_t_chr_avt_acc_hat_ribbonCheckerGreen.jpg',
 'phase_4/maps/tt_t_chr_avt_acc_hat_partyToon.jpg',
 'phase_4/maps/tt_t_chr_avt_acc_hat_bowlerRoger.jpg',
 'phase_4/maps/tt_m_chr_avt_acc_hat_mousekateer.jpg']
GlassesModels = [None,
 'phase_4/models/accessories/tt_m_chr_avt_acc_msk_roundGlasses',
 'phase_4/models/accessories/tt_m_chr_avt_acc_msk_miniblinds',
 'phase_4/models/accessories/tt_m_chr_avt_acc_msk_narrowGlasses',
 'phase_4/models/accessories/tt_m_chr_avt_acc_msk_starGlasses',
 'phase_4/models/accessories/tt_m_chr_avt_acc_msk_3dGlasses',
 'phase_4/models/accessories/tt_m_chr_avt_acc_msk_aviator',
 'phase_4/models/accessories/tt_m_chr_avt_acc_msk_catEyeGlasses',
 'phase_4/models/accessories/tt_m_chr_avt_acc_msk_dorkGlasses',
 'phase_4/models/accessories/tt_m_chr_avt_acc_msk_jackieOShades',
 'phase_4/models/accessories/tt_m_chr_avt_acc_msk_scubaMask',
 'phase_4/models/accessories/tt_m_chr_avt_acc_msk_goggles',
 'phase_4/models/accessories/tt_m_chr_avt_acc_msk_grouchoMarxEyebrow',
 'phase_4/models/accessories/tt_m_chr_avt_acc_msk_heartGlasses',
 'phase_4/models/accessories/tt_m_chr_avt_acc_msk_insectEyeGlasses',
 'phase_4/models/accessories/tt_m_chr_avt_acc_msk_masqueradeTypeMask',
 'phase_4/models/accessories/tt_m_chr_avt_acc_msk_masqueradeTypeMask3',
 'phase_4/models/accessories/tt_m_chr_avt_acc_msk_monocle',
 'phase_4/models/accessories/tt_m_chr_avt_acc_msk_mouthGlasses',
 'phase_4/models/accessories/tt_m_chr_avt_acc_msk_squareRims',
 'phase_4/models/accessories/tt_m_chr_avt_acc_msk_eyepatch',
 'phase_4/models/accessories/tt_m_chr_avt_acc_msk_alienGlasses',
 'phase_4/models/accessories/tt_m_chr_avt_acc_msk_hypno_goggles17']
GlassesTextures = [None,
 'phase_4/maps/tt_t_chr_avt_acc_msk_masqueradeTypeMask2.jpg',
 'phase_4/maps/tt_t_chr_avt_acc_msk_masqueradeTypeMask4.jpg',
 'phase_4/maps/tt_t_chr_avt_acc_msk_masqueradeTypeMask5.jpg',
 'phase_4/maps/tt_t_chr_avt_acc_msk_eyepatchGems.jpg']
BackpackModels = [None,
 'phase_4/models/accessories/tt_m_chr_avt_acc_pac_backpack',
 'phase_4/models/accessories/tt_m_chr_avt_acc_pac_batWings',
 'phase_4/models/accessories/tt_m_chr_avt_acc_pac_beeWings',
 'phase_4/models/accessories/tt_m_chr_avt_acc_pac_dragonFlyWings',
 'phase_4/models/accessories/tt_m_chr_avt_acc_pac_scubaTank',
 'phase_4/models/accessories/tt_m_chr_avt_acc_pac_sharkFin',
 'phase_4/models/accessories/tt_m_chr_avt_acc_pac_angelWings',
 'phase_4/models/accessories/tt_m_chr_avt_acc_pac_backpackWithToys',
 'phase_4/models/accessories/tt_m_chr_avt_acc_pac_butterflyWings',
 'phase_4/models/accessories/tt_m_chr_avt_acc_pac_dragonWing',
 'phase_4/models/accessories/tt_m_chr_avt_acc_pac_jetPack',
 'phase_4/models/accessories/tt_m_chr_avt_acc_pac_spiderLegs',
 'phase_4/models/accessories/tt_m_chr_avt_acc_pac_stuffedAnimalBackpackA',
 'phase_4/models/accessories/tt_m_chr_avt_acc_pac_birdWings',
 'phase_4/models/accessories/tt_m_chr_avt_acc_pac_stuffedAnimalBackpackCat',
 'phase_4/models/accessories/tt_m_chr_avt_acc_pac_stuffedAnimalBackpackDog',
 'phase_4/models/accessories/tt_m_chr_avt_acc_pac_airplane',
 'phase_4/models/accessories/tt_m_chr_avt_acc_pac_woodenSword',
 'phase_4/models/accessories/tt_m_chr_avt_acc_pac_supertoonCape',
 'phase_4/models/accessories/tt_m_chr_avt_acc_pac_vampireCape',
 'phase_4/models/accessories/tt_m_chr_avt_acc_pac_dinosaurTail',
 'phase_4/models/accessories/tt_m_chr_avt_acc_pac_band',
 'phase_4/models/accessories/tt_m_chr_avt_acc_pac_gags',
 'phase_4/models/accessories/tt_m_chr_avt_acc_pac_flunky']
BackpackTextures = [None,
 'phase_4/maps/tt_t_chr_avt_acc_pac_backpackOrange.jpg',
 'phase_4/maps/tt_t_chr_avt_acc_pac_backpackPurple.jpg',
 'phase_4/maps/tt_t_chr_avt_acc_pac_backpackPolkaDotRed.jpg',
 'phase_4/maps/tt_t_chr_avt_acc_pac_backpackPolkaDotYellow.jpg',
 'phase_4/maps/tt_t_chr_avt_acc_pac_angelWingsMultiColor.jpg',
 'phase_4/maps/tt_t_chr_avt_acc_pac_butterflyWingsStyle2.jpg']
ShoesModels = ['feet',
 'shoes',
 'boots_short',
 'boots_long']
ShoesTextures = ['phase_3/maps/tt_t_chr_avt_acc_sho_athleticGreen.jpg',
 'phase_4/maps/tt_t_chr_avt_acc_sho_athleticRed.jpg',
 'phase_3/maps/tt_t_chr_avt_acc_sho_docMartinBootsGreen.jpg',
 'phase_4/maps/tt_t_chr_avt_acc_sho_converseStyleGreen.jpg',
 'phase_4/maps/tt_t_chr_avt_acc_sho_wingtips.jpg',
 'phase_4/maps/tt_t_chr_avt_acc_sho_maryJaneShoes.jpg',
 'phase_4/maps/tt_t_chr_avt_acc_sho_deckShoes.jpg',
 'phase_4/maps/tt_t_chr_avt_acc_sho_athleticYellow.jpg',
 'phase_4/maps/tt_t_chr_avt_acc_sho_converseStyleBlack.jpg',
 'phase_4/maps/tt_t_chr_avt_acc_sho_converseStyleWhite.jpg',
 'phase_4/maps/tt_t_chr_avt_acc_sho_converseStylePink.jpg',
 'phase_4/maps/tt_t_chr_avt_acc_sho_cowboyBoots.jpg',
 'phase_4/maps/tt_t_chr_avt_acc_sho_fashionBootsPurple.jpg',
 'phase_4/maps/tt_t_chr_avt_acc_sho_hiTopSneakers.jpg',
 'phase_4/maps/tt_t_chr_avt_acc_sho_maryJaneShoesBrown.jpg',
 'phase_4/maps/tt_t_chr_avt_acc_sho_maryJaneShoesRed.jpg',
 'phase_4/maps/tt_t_chr_avt_acc_sho_superToonRedBoots.jpg',
 'phase_4/maps/tt_t_chr_avt_acc_sho_tennisShoesGreen.jpg',
 'phase_4/maps/tt_t_chr_avt_acc_sho_tennisShoesPink.jpg',
 'phase_4/maps/tt_t_chr_avt_acc_sho_converseStyleRed.jpg',
 'phase_4/maps/tt_t_chr_avt_acc_sho_docMartinBootsAqua.jpg',
 'phase_4/maps/tt_t_chr_avt_acc_sho_docMartinBootsBrown.jpg',
 'phase_4/maps/tt_t_chr_avt_acc_sho_docMartinBootsYellow.jpg',
 'phase_4/maps/tt_t_chr_avt_acc_sho_fashionBootsBlueSquares.jpg',
 'phase_4/maps/tt_t_chr_avt_acc_sho_fashionBootsGreenHearts.jpg',
 'phase_4/maps/tt_t_chr_avt_acc_sho_fashionBootsGreyDots.jpg',
 'phase_4/maps/tt_t_chr_avt_acc_sho_fashionBootsOrangeStars.jpg',
 'phase_4/maps/tt_t_chr_avt_acc_sho_fashionBootsPinkStars.jpg',
 'phase_4/maps/tt_t_chr_avt_acc_sho_loafers.jpg',
 'phase_4/maps/tt_t_chr_avt_acc_sho_maryJaneShoesPurple.jpg',
 'phase_4/maps/tt_t_chr_avt_acc_sho_motorcycleBoots.jpg',
 'phase_4/maps/tt_t_chr_avt_acc_sho_oxfords.jpg',
 'phase_4/maps/tt_t_chr_avt_acc_sho_rainBootsPink.jpg',
 'phase_4/maps/tt_t_chr_avt_acc_sho_santaBoots.jpg',
 'phase_4/maps/tt_t_chr_avt_acc_sho_winterBootsBeige.jpg',
 'phase_4/maps/tt_t_chr_avt_acc_sho_winterBootsPink.jpg',
 'phase_4/maps/tt_t_chr_avt_acc_sho_workBoots.jpg',
 'phase_4/maps/tt_t_chr_avt_acc_sho_converseStyleYellow.jpg',
 'phase_4/maps/tt_t_chr_avt_acc_sho_docMartinBootsPink.jpg',
 'phase_4/maps/tt_t_chr_avt_acc_sho_hiTopSneakersPink.jpg',
 'phase_4/maps/tt_t_chr_avt_acc_sho_rainBootsRedDots.jpg',
 'phase_4/maps/tt_t_chr_avt_acc_sho_tennisShoesPurple.jpg',
 'phase_4/maps/tt_t_chr_avt_acc_sho_tennisShoesViolet.jpg',
 'phase_4/maps/tt_t_chr_avt_acc_sho_tennisShoesYellow.jpg',
 'phase_4/maps/tt_t_chr_avt_acc_sho_rainBootsBlue.jpg',
 'phase_4/maps/tt_t_chr_avt_acc_sho_rainBootsYellow.jpg',
 'phase_4/maps/tt_t_chr_avt_acc_sho_athleticBlack.jpg',
 'phase_4/maps/tt_t_chr_avt_acc_sho_pirate.jpg',
 'phase_4/maps/tt_t_chr_avt_acc_sho_dinosaur.jpg']
HatStyles = {'none': [0, 0, 0],
 'hbb1': [1, 0, 0],
 'hsf1': [2, 0, 0],
 'hsf2': [2, 5, 0],
 'hsf3': [2, 6, 0],
 'hht1': [4, 0, 0],
 'hht2': [4, 3, 0],
 'htp1': [5, 0, 0],
 'htp2': [5, 4, 0],
 'hav1': [6, 0, 0],
 'hfp1': [7, 0, 0],
 'hsg1': [8, 0, 0],
 'hwt1': [9, 0, 0],
 'hfz1': [10, 0, 0],
 'hgf1': [11, 0, 0],
 'hpt1': [12, 0, 0],
 'hpt2': [12, 19, 0],
 'hpb1': [13, 0, 0],
 'hcr1': [14, 0, 0],
 'hbb2': [1, 7, 0],
 'hbb3': [1, 8, 0],
 'hcw1': [15, 0, 0],
 'hpr1': [16, 0, 0],
 'hpp1': [17, 0, 0],
 'hfs1': [18, 0, 0],
 'hsb1': [19, 0, 0],
 'hst1': [20, 0, 0],
 'hat1': [22, 0, 0],
 'hhd1': [23, 0, 0],
 'hbw1': [24, 0, 0],
 'hch1': [25, 0, 0],
 'hdt1': [26, 0, 0],
 'hft1': [27, 0, 0],
 'hfd1': [28, 0, 0],
 'hmk1': [29, 0, 0],
 'hft2': [30, 0, 0],
 'hhd2': [31, 0, 0],
 'hrh1': [33, 0, 0],
 'hhm1': [34, 0, 0],
 'hat2': [35, 0, 0],
 'htr1': [36, 0, 0],
 'hhm2': [37, 0, 0],
 'hwz1': [38, 0, 0],
 'hwz2': [39, 0, 0],
 'hhm3': [40, 0, 0],
 'hhm4': [41, 0, 0],
 'hfp2': [42, 0, 0],
 'hhm5': [43, 0, 0],
 'hnp1': [44, 0, 0],
 'hpc2': [45, 0, 0],
 'hph1': [46, 0, 0],
 'hwg1': [47, 0, 0],
 'hbb4': [1, 13, 0],
 'hbb5': [1, 14, 0],
 'hbb6': [1, 15, 0],
 'hsl1': [48, 0, 0],
 'hfr1': [49, 0, 0],
 'hby1': [50, 0, 0],
 'hjh1': [51, 0, 0],
 'hbb7': [1, 17, 0],
 'hwt2': [52, 0, 0],
 'hhw2': [54, 0, 0],
 'hob1': [55, 0, 0],
 'hbn1': [56, 0, 0],
 'hrb1': [3, 0, 0],
 'hrb2': [3, 1, 0],
 'hrb3': [3, 2, 0],
 'hsu1': [21, 0, 0],
 'hrb4': [3, 9, 0],
 'hrb5': [3, 10, 0],
 'hrb6': [3, 11, 0],
 'hrb7': [3, 12, 0],
 'hpc1': [32, 0, 0],
 'hrb8': [3, 16, 0],
 'hrb9': [3, 18, 0],
 'hhw1': [53, 0, 0],
 'kmh1': [57, 0, 0]}
GlassesStyles = {'none': [0, 0, 0],
 'grd1': [1, 0, 0],
 'gmb1': [2, 0, 0],
 'gnr1': [3, 0, 0],
 'gst1': [4, 0, 0],
 'g3d1': [5, 0, 0],
 'gav1': [6, 0, 0],
 'gjo1': [9, 0, 0],
 'gsb1': [10, 0, 0],
 'ggl1': [11, 0, 0],
 'ggm1': [12, 0, 0],
 'ghg1': [13, 0, 0],
 'gie1': [14, 0, 0],
 'gmt1': [15, 0, 0],
 'gmt2': [15, 1, 0],
 'gmt3': [16, 0, 0],
 'gmt4': [16, 2, 0],
 'gmt5': [16, 3, 0],
 'gmn1': [17, 0, 0],
 'gmo1': [18, 0, 0],
 'gsr1': [19, 0, 0],
 'gce1': [7, 0, 0],
 'gdk1': [8, 0, 0],
 'gag1': [21, 0, 0],
 'ghy1': [22, 0, 0],
 'ghw1': [20, 0, 0],
 'ghw2': [20, 4, 0]}
BackpackStyles = {'none': [0, 0, 0],
 'bpb1': [1, 0, 0],
 'bpb2': [1, 1, 0],
 'bpb3': [1, 2, 0],
 'bpd1': [1, 3, 0],
 'bpd2': [1, 4, 0],
 'bwg1': [2, 0, 0],
 'bwg2': [3, 0, 0],
 'bwg3': [4, 0, 0],
 'bst1': [5, 0, 0],
 'bfn1': [6, 0, 0],
 'baw1': [7, 0, 0],
 'baw2': [7, 5, 0],
 'bwt1': [8, 0, 0],
 'bwg4': [9, 0, 0],
 'bwg5': [9, 6, 0],
 'bwg6': [10, 0, 0],
 'bjp1': [11, 0, 0],
 'blg1': [12, 0, 0],
 'bsa1': [13, 0, 0],
 'bwg7': [14, 0, 0],
 'bsa2': [15, 0, 0],
 'bsa3': [16, 0, 0],
 'bap1': [17, 0, 0],
 'bhw1': [18, 0, 0],
 'bhw2': [19, 0, 0],
 'bhw3': [20, 0, 0],
 'bhw4': [21, 0, 0],
 'bob1': [22, 0, 0],
 'bfg1': [23, 0, 0],
 'bfl1': [24, 0, 0]}
ShoesStyles = {'none': [0, 0, 0],
 'sat1': [1, 0, 0],
 'sat2': [1, 1, 0],
 'smb1': [3, 2, 0],
 'scs1': [2, 3, 0],
 'sdk1': [1, 6, 0],
 'sat3': [1, 7, 0],
 'scs2': [2, 8, 0],
 'scs3': [2, 9, 0],
 'scs4': [2, 10, 0],
 'scb1': [3, 11, 0],
 'sht1': [2, 13, 0],
 'ssb1': [3, 16, 0],
 'sts1': [1, 17, 0],
 'sts2': [1, 18, 0],
 'scs5': [2, 19, 0],
 'smb2': [3, 20, 0],
 'smb3': [3, 21, 0],
 'smb4': [3, 22, 0],
 'slf1': [1, 28, 0],
 'smt1': [3, 30, 0],
 'sox1': [1, 31, 0],
 'srb1': [3, 32, 0],
 'sst1': [3, 33, 0],
 'swb1': [3, 34, 0],
 'swb2': [3, 35, 0],
 'swk1': [2, 36, 0],
 'scs6': [2, 37, 0],
 'smb5': [3, 38, 0],
 'sht2': [2, 39, 0],
 'srb2': [3, 40, 0],
 'sts3': [1, 41, 0],
 'sts4': [1, 42, 0],
 'sts5': [1, 43, 0],
 'srb3': [3, 44, 0],
 'srb4': [3, 45, 0],
 'sat4': [1, 46, 0],
 'shw1': [3, 47, 0],
 'shw2': [3, 48, 0],
 'swt1': [1, 4, 0],
 'smj1': [2, 5, 0],
 'sfb1': [3, 12, 0],
 'smj2': [2, 14, 0],
 'smj3': [2, 15, 0],
 'sfb2': [3, 23, 0],
 'sfb3': [3, 24, 0],
 'sfb4': [3, 25, 0],
 'sfb5': [3, 26, 0],
 'sfb6': [3, 27, 0],
 'smj4': [2, 29, 0]}

def isValidHat(itemIdx, textureIdx, colorIdx):
    for style in HatStyles.values():
        if itemIdx == style[0] and textureIdx == style[1] and colorIdx == style[2]:
            return True

    return False


def isValidGlasses(itemIdx, textureIdx, colorIdx):
    for style in GlassesStyles.values():
        if itemIdx == style[0] and textureIdx == style[1] and colorIdx == style[2]:
            return True

    return False


def isValidBackpack(itemIdx, textureIdx, colorIdx):
    for style in BackpackStyles.values():
        if itemIdx == style[0] and textureIdx == style[1] and colorIdx == style[2]:
            return True

    return False


def isValidShoes(itemIdx, textureIdx, colorIdx):
    for style in ShoesStyles.values():
        if itemIdx == style[0] and textureIdx == style[1] and colorIdx == style[2]:
            return True

    return False


def isValidAccessory(itemIdx, textureIdx, colorIdx, which):
    if which == HAT:
        return isValidHat(itemIdx, textureIdx, colorIdx)
    elif which == GLASSES:
        return isValidGlasses(itemIdx, textureIdx, colorIdx)
    elif which == BACKPACK:
        return isValidBackpack(itemIdx, textureIdx, colorIdx)
    elif which == SHOES:
        return isValidShoes(itemIdx, textureIdx, colorIdx)
    else:
        return False


class ToonDNA:

    def __init__(self, str = None, type = None, dna = None, r = None, b = None, g = None):
        if str != None:
            self.makeFromNetString(str)
        elif type != None:
            if type == 't':
                if dna == None:
                    self.newToonRandom(r, g, b)
                else:
                    self.newToonFromProperties(*dna.asTuple())
        else:
            self.type = 'u'

    def __str__(self):
        string = 'type = toon\n'
        string = string + 'gender = %s\n' % self.gender
        string = string + 'head = %s, torso = %s, legs = %s\n' % (self.head, self.torso, self.legs)
        string = string + 'arm color = %s\n' % (self.armColor,)
        string = string + 'glove color = %s\n' % (self.gloveColor,)
        string = string + 'leg color = %s\n' % (self.legColor,)
        string = string + 'head color = %s\n' % (self.headColor,)
        string = string + 'top texture = %d\n' % self.topTex
        string = string + 'top texture color = %d\n' % self.topTexColor
        string = string + 'sleeve texture = %d\n' % self.sleeveTex
        string = string + 'sleeve texture color = %d\n' % self.sleeveTexColor
        string = string + 'bottom texture = %d\n' % self.botTex
        string = string + 'bottom texture color = %d\n' % self.botTexColor
        return string

    def clone(self):
        d = ToonDNA()
        d.makeFromNetString(self.makeNetString())
        return d

    def makeNetString(self):
        dg = PyDatagram()
        dg.addFixedString(self.type, 1)
        if self.type == 't':
            headIndex = toonHeadTypes.index(self.head)
            torsoIndex = toonTorsoTypes.index(self.torso)
            legsIndex = toonLegTypes.index(self.legs)
            dg.addUint8(headIndex)
            dg.addUint8(torsoIndex)
            dg.addUint8(legsIndex)
            if self.gender == 'm':
                dg.addUint8(1)
            else:
                dg.addUint8(0)
            dg.addUint8(self.topTex)
            dg.addUint8(self.topTexColor)
            dg.addUint8(self.sleeveTex)
            dg.addUint8(self.sleeveTexColor)
            dg.addUint8(self.botTex)
            dg.addUint8(self.botTexColor)
            self.armColor = self.migrateColor(self.armColor)
            self.gloveColor = self.migrateColor(self.gloveColor)
            self.legColor = self.migrateColor(self.legColor)
            self.headColor = self.migrateColor(self.headColor)
            for colors in (self.armColor, self.gloveColor, self.legColor, self.headColor):
                for color in colors[:-1]:
                    dg.addFloat64(color)
        elif self.type == 'u':
            notify.error('undefined avatar')
        else:
            notify.error('unknown avatar type: ', self.type)
        return dg.getMessage()

    def isValidNetString(self, string):
        dg = PyDatagram(string)
        dgi = PyDatagramIterator(dg)
        type = dgi.getFixedString(1)
        if type not in ('t',):
            return False
        headIndex = dgi.getUint8()
        torsoIndex = dgi.getUint8()
        legsIndex = dgi.getUint8()
        if headIndex >= len(toonHeadTypes):
            return False
        if torsoIndex >= len(toonTorsoTypes):
            return False
        if legsIndex >= len(toonLegTypes):
            return False
        gender = dgi.getUint8()
        if gender == 1:
            gender = 'm'
        else:
            gender = 'f'
        topTex = dgi.getUint8()
        topTexColor = dgi.getUint8()
        sleeveTex = dgi.getUint8()
        sleeveTexColor = dgi.getUint8()
        botTex = dgi.getUint8()
        botTexColor = dgi.getUint8()
        armColor = (dgi.getFloat64(), dgi.getFloat64(), dgi.getFloat64(), 1.0)
        gloveColor = (dgi.getFloat64(), dgi.getFloat64(), dgi.getFloat64(), 1.0)
        legColor = (dgi.getFloat64(), dgi.getFloat64(), dgi.getFloat64(), 1.0)
        headColor = (dgi.getFloat64(), dgi.getFloat64(), dgi.getFloat64(), 1.0)
        if topTex >= len(Shirts):
            return False
        if topTexColor >= len(ClothesColors):
            return False
        if sleeveTex >= len(Sleeves):		
            return False
        if sleeveTexColor >= len(ClothesColors):	
            return False
        if gender == 'm':
            if botTex >= len(BoyShorts):
                return False
        else:
            if botTex >= len(GirlBottoms):
                return False
        if botTexColor >= len(ClothesColors):
            return False
        if not self.isValid(armColor):
            return False
        if not self.isValid(gloveColor):
            return False
        if not self.isValid(legColor):
            return False
        if not self.isValid(headColor):
            return False
        return True
    
    def isValid(self, color):
        if color in allColorsList:
            return True
        
        hsv = colorsys.rgb_to_hsv(*color[:-1])
        return ToontownGlobals.COLOR_SATURATION_MIN <= hsv[1] <= ToontownGlobals.COLOR_SATURATION_MAX and ToontownGlobals.COLOR_VALUE_MIN <= hsv[2] <= ToontownGlobals.COLOR_VALUE_MAX

    def makeFromNetString(self, string):
        dg = PyDatagram(string)
        dgi = PyDatagramIterator(dg)
        self.type = dgi.getFixedString(1)
        if self.type == 't':
            headIndex = dgi.getUint8()
            torsoIndex = dgi.getUint8()
            legsIndex = dgi.getUint8()
            self.head = toonHeadTypes[headIndex]
            self.torso = toonTorsoTypes[torsoIndex]
            self.legs = toonLegTypes[legsIndex]
            gender = dgi.getUint8()
            if gender == 1:
                self.gender = 'm'
            else:
                self.gender = 'f'
            self.topTex = dgi.getUint8()
            self.topTexColor = dgi.getUint8()
            self.sleeveTex = dgi.getUint8()
            self.sleeveTexColor = dgi.getUint8()
            self.botTex = dgi.getUint8()
            self.botTexColor = dgi.getUint8()
            self.armColor = (dgi.getFloat64(), dgi.getFloat64(), dgi.getFloat64(), 1.0)
            self.gloveColor = (dgi.getFloat64(), dgi.getFloat64(), dgi.getFloat64(), 1.0)
            self.legColor = (dgi.getFloat64(), dgi.getFloat64(), dgi.getFloat64(), 1.0)
            self.headColor = (dgi.getFloat64(), dgi.getFloat64(), dgi.getFloat64(), 1.0)
        else:
            notify.error('unknown avatar type: ', self.type)

    def defaultColor(self):
        return 25

    def newToon(self, dna, color = None):
        if len(dna) == 4:
            self.type = 't'
            self.head = dna[0]
            self.torso = dna[1]
            self.legs = dna[2]
            self.gender = dna[3]
            self.topTex = 0
            self.topTexColor = 0
            self.sleeveTex = 0
            self.sleeveTexColor = 0
            self.botTex = 0
            self.botTexColor = 0
            if color == None:
                color = 25
            color = self.migrateColor(color)
            self.armColor = color
            self.legColor = color
            self.headColor = color
            self.gloveColor = 0
        else:
            notify.error("tuple must be in format ('%s', '%s', '%s', '%s')")
    
    def migrateColor(self, color):
        return allColorsList[color] if isinstance(color, int) else color

    def newToonFromProperties(self, head, torso, legs, gender, armColor, gloveColor, legColor, headColor, topTexture, topTextureColor, sleeveTexture, sleeveTextureColor, bottomTexture, bottomTextureColor):
        self.type = 't'
        self.head = head
        self.torso = torso
        self.legs = legs
        self.gender = gender
        self.armColor = self.migrateColor(armColor)
        self.gloveColor = self.migrateColor(gloveColor)
        self.legColor = self.migrateColor(legColor)
        self.headColor = self.migrateColor(headColor)
        self.topTex = topTexture
        self.topTexColor = topTextureColor
        self.sleeveTex = sleeveTexture
        self.sleeveTexColor = sleeveTextureColor
        self.botTex = bottomTexture
        self.botTexColor = bottomTextureColor

    def updateToonProperties(self, head = None, torso = None, legs = None, gender = None, armColor = None, gloveColor = None, legColor = None, headColor = None, topTexture = None, topTextureColor = None, sleeveTexture = None, sleeveTextureColor = None, bottomTexture = None, bottomTextureColor = None, shirt = None, bottom = None):
        if head:
            self.head = head
        if torso:
            self.torso = torso
        if legs:
            self.legs = legs
        if gender:
            self.gender = gender
        if armColor:
            self.armColor = self.migrateColor(armColor)
        if gloveColor:
            self.gloveColor = self.migrateColor(gloveColor)
        if legColor:
            self.legColor = self.migrateColor(legColor)
        if headColor:
            self.headColor = self.migrateColor(headColor)
        if topTexture:
            self.topTex = topTexture
        if topTextureColor:
            self.topTexColor = topTextureColor
        if sleeveTexture:
            self.sleeveTex = sleeveTexture
        if sleeveTextureColor:
            self.sleeveTexColor = sleeveTextureColor
        if bottomTexture:
            self.botTex = bottomTexture
        if bottomTextureColor:
            self.botTexColor = bottomTextureColor
        if shirt:
            str, colorIndex = shirt
            defn = ShirtStyles[str]
            self.topTex = defn[0]
            self.topTexColor = defn[2][colorIndex][0]
            self.sleeveTex = defn[1]
            self.sleeveTexColor = defn[2][colorIndex][1]
        if bottom:
            str, colorIndex = bottom
            defn = BottomStyles[str]
            self.botTex = defn[0]
            self.botTexColor = defn[1][colorIndex]

    def newToonRandom(self, seed = None, gender = 'm', npc = 0, stage = None):
        if seed:
            generator = random.Random()
            generator.seed(seed)
        else:
            generator = random
        self.type = 't'
        self.legs = generator.choice(toonLegTypes + ['m',
         'l',
         'l',
         'l'])
        self.gender = gender
        if not npc:
            if stage == MAKE_A_TOON:
                animal = generator.choice(allToonHeadAnimalIndices)
                self.head = toonHeadTypes[animal]
            else:
                self.head = generator.choice(toonHeadTypes)
        else:
            self.head = generator.choice(toonHeadTypes[:22])
        top, topColor, sleeve, sleeveColor = getRandomTop(gender, generator=generator)
        bottom, bottomColor = getRandomBottom(gender, generator=generator)
        color = generator.choice(allColorsList)
        if gender == 'm':
            self.torso = generator.choice(toonTorsoTypes[:3])
            self.topTex = top
            self.topTexColor = topColor
            self.sleeveTex = sleeve
            self.sleeveTexColor = sleeveColor
            self.botTex = bottom
            self.botTexColor = bottomColor
        else:
            self.torso = generator.choice(toonTorsoTypes[:6])
            self.topTex = top
            self.topTexColor = topColor
            self.sleeveTex = sleeve
            self.sleeveTexColor = sleeveColor
            if self.torso[1] == 'd':
                bottom, bottomColor = getRandomBottom(gender, generator=generator, girlBottomType=SKIRT)
            else:
                bottom, bottomColor = getRandomBottom(gender, generator=generator, girlBottomType=SHORTS)
            self.botTex = bottom
            self.botTexColor = bottomColor
        self.armColor = color
        self.legColor = color
        self.headColor = color
        self.gloveColor = self.migrateColor(0)

    def asTuple(self):
        return (self.head,
         self.torso,
         self.legs,
         self.gender,
         self.armColor,
         self.gloveColor,
         self.legColor,
         self.headColor,
         self.topTex,
         self.topTexColor,
         self.sleeveTex,
         self.sleeveTexColor,
         self.botTex,
         self.botTexColor)
    
    def asNpcTuple(self):
        return (self.head,
         self.torso,
         self.legs,
         self.gender,
         allColorsList.index(self.armColor),
         allColorsList.index(self.gloveColor),
         allColorsList.index(self.legColor),
         allColorsList.index(self.headColor),
         self.topTex,
         self.topTexColor,
         self.sleeveTex,
         self.sleeveTexColor,
         self.botTex,
         self.botTexColor)

    def getType(self):
        if self.type == 't':
            type = self.getAnimal()
        else:
            notify.error('Invalid DNA type: ', self.type)
        return type

    def getAnimal(self):
        if self.head[0] == 'd':
            return 'dog'
        elif self.head[0] == 'c':
            return 'cat'
        elif self.head[0] == 'm':
            return 'mouse'
        elif self.head[0] == 'h':
            return 'horse'
        elif self.head[0] == 'r':
            return 'rabbit'
        elif self.head[0] == 'f':
            return 'duck'
        elif self.head[0] == 'p':
            return 'monkey'
        elif self.head[0] == 'b':
            return 'bear'
        elif self.head[0] == 's':
            return 'pig'
        else:
            notify.error('unknown headStyle: ', self.head[0])

    def getHeadSize(self):
        if self.head[1] == 'l':
            return 'long'
        elif self.head[1] == 's':
            return 'short'
        else:
            notify.error('unknown head size: ', self.head[1])

    def getMuzzleSize(self):
        if self.head[2] == 'l':
            return 'long'
        elif self.head[2] == 's':
            return 'short'
        else:
            notify.error('unknown muzzle size: ', self.head[2])

    def getTorsoSize(self):
        if self.torso[0] == 'l':
            return 'long'
        elif self.torso[0] == 'm':
            return 'medium'
        elif self.torso[0] == 's':
            return 'short'
        else:
            notify.error('unknown torso size: ', self.torso[0])

    def getLegSize(self):
        if self.legs == 'l':
            return 'long'
        elif self.legs == 'm':
            return 'medium'
        elif self.legs == 's':
            return 'short'
        else:
            notify.error('unknown leg size: ', self.legs)

    def getGender(self):
        return self.gender

    def getClothes(self):
        if len(self.torso) == 1:
            return 'naked'
        elif self.torso[1] == 's':
            return 'shorts'
        elif self.torso[1] == 'd':
            return 'dress'
        else:
            notify.error('unknown clothing type: ', self.torso[1])

    def getArmColor(self):
        return self.armColor

    def getLegColor(self):
        return self.legColor

    def getHeadColor(self):
        return self.headColor

    def getGloveColor(self):
        return self.gloveColor

    def getBlackColor(self):
        try:
            return allColorsList[26]
        except:
            return allColorsList[0]

    def getWhiteColor(self):
        return allColorsList[0]