from panda3d.core import GeomNode, Light, NodePath, VBase4
from direct.interval.IntervalGlobal import *
import random

from toontown.base import TTLocalizer
from toontown.base import ToontownBattleGlobals
from toontown.suit import SuitDNA


if process == 'client':
    from toontown.battle import BattleParticles


try:
    config = base.config
except:
    config = simbase.config

EFFECT_RADIUS = 30
RESISTANCE_TOONUP = 0
RESISTANCE_RESTOCK = 1
RESISTANCE_MONEY = 2
RESISTANCE_TICKETS = 3
RESISTANCE_MERITS = 4
resistanceMenu = [RESISTANCE_TOONUP, RESISTANCE_RESTOCK, RESISTANCE_MONEY, RESISTANCE_TICKETS, RESISTANCE_MERITS]
randomResistanceMenu = [RESISTANCE_TOONUP, RESISTANCE_RESTOCK, RESISTANCE_MONEY, RESISTANCE_TICKETS]
resistanceDict = {
    RESISTANCE_TOONUP: {
        'menuName': TTLocalizer.ResistanceToonupMenu,
        'itemText': TTLocalizer.ResistanceToonupItem,
        'chatText': TTLocalizer.ResistanceToonupChat,
        'values': [10, 20, 40, 80, -1],
        'items': [0, 1, 2, 3, 4]
    },
    RESISTANCE_MONEY: {
        'menuName': TTLocalizer.ResistanceMoneyMenu,
        'itemText': TTLocalizer.ResistanceMoneyItem,
        'chatText': TTLocalizer.ResistanceMoneyChat,
        'values': [100, 200, 350, 600, 1200, 2400],
        'items': [0, 1, 2, 3, 4, 5]
    },
    RESISTANCE_RESTOCK: {
        'menuName': TTLocalizer.ResistanceRestockMenu,
        'itemText': TTLocalizer.ResistanceRestockItem,
        'chatText': TTLocalizer.ResistanceRestockChat,
        'values': [
            ToontownBattleGlobals.HEAL_TRACK,
            ToontownBattleGlobals.TRAP_TRACK,
            ToontownBattleGlobals.LURE_TRACK,
            ToontownBattleGlobals.SOUND_TRACK,
            ToontownBattleGlobals.THROW_TRACK,
            ToontownBattleGlobals.SQUIRT_TRACK,
            ToontownBattleGlobals.DROP_TRACK,
            -1
        ],
        'extra': [
            TTLocalizer.MovieNPCSOSHeal,
            TTLocalizer.MovieNPCSOSTrap,
            TTLocalizer.MovieNPCSOSLure,
            TTLocalizer.MovieNPCSOSSound,
            TTLocalizer.MovieNPCSOSThrow,
            TTLocalizer.MovieNPCSOSSquirt,
            TTLocalizer.MovieNPCSOSDrop,
            TTLocalizer.MovieNPCSOSAll
        ],
        'items': [0, 1, 2, 3, 4, 5, 6, 7]
    },
    RESISTANCE_MERITS: {
        'menuName': TTLocalizer.ResistanceMeritsMenu,
        'itemText': TTLocalizer.ResistanceMeritsItem,
        'chatText': TTLocalizer.ResistanceMeritsChat,
        'values': range(len(SuitDNA.suitDepts)) + [-1],
        'extra': TTLocalizer.RewardPanelMeritBarLabels + [TTLocalizer.MovieNPCSOSAll],
        'items': range(len(SuitDNA.suitDepts) + 1)
    },
    RESISTANCE_TICKETS: {
        'menuName': TTLocalizer.ResistanceTicketsMenu,
        'itemText': TTLocalizer.ResistanceTicketsItem,
        'chatText': TTLocalizer.ResistanceTicketsChat,
        'values': [200, 400, 600, 800, 1200],
        'items': [0, 1, 2, 3, 4]
    }
}


def encodeId(menuIndex, itemIndex):
    textId = menuIndex * 100
    textId += resistanceDict[menuIndex]['items'][itemIndex]
    return textId


def decodeId(textId):
    menuIndex = int(textId / 100)
    itemIndex = textId % 100
    return (menuIndex, itemIndex)


def validateId(textId):
    if textId < 0:
        return 0
    menuIndex, itemIndex = decodeId(textId)
    if menuIndex not in resistanceDict:
        return 0
    if itemIndex >= len(resistanceDict[menuIndex]['values']):
        return 0
    return 1


def getItems(menuIndex):
    return resistanceDict[menuIndex]['items']


def getMenuName(textId):
    menuIndex, _ = decodeId(textId)
    return resistanceDict[menuIndex]['menuName']


def getItemText(textId):
    menuIndex, itemIndex = decodeId(textId)
    resistance = resistanceDict[menuIndex]
    value = resistance['values'][itemIndex]
    text = resistance['itemText']
    if menuIndex is RESISTANCE_TOONUP:
        if value is -1:
            value = TTLocalizer.ResistanceToonupItemMax
    elif 'extra' in resistance:
        value = resistance['extra'][itemIndex]
    return text % str(value)


def getChatText(textId):
    menuIndex, _ = decodeId(textId)
    return resistanceDict[menuIndex]['chatText']


def getItemValue(textId):
    menuIndex, itemIndex = decodeId(textId)
    return resistanceDict[menuIndex]['values'][itemIndex]


def getRandomId():
    menuIndex = random.choice(randomResistanceMenu)
    itemIndex = random.choice(getItems(menuIndex))
    return encodeId(menuIndex, itemIndex)


def doEffect(textId, speakingToon, nearbyToons):
    menuIndex, _ = decodeId(textId)
    itemValue = getItemValue(textId)
    if menuIndex == RESISTANCE_TOONUP:
        effect = BattleParticles.loadParticleFile('resistanceEffectSparkle.ptf')
        fadeColor = VBase4(1, 0.5, 1, 1)
    elif menuIndex == RESISTANCE_MONEY:
        effect = BattleParticles.loadParticleFile('resistanceEffectBean.ptf')
        bean = loader.loadModel('phase_4/models/props/jellybean4.bam')
        bean = bean.find('**/jellybean')
        colors = {
            'particles-1': (1, 1, 0, 1),
            'particles-2': (1, 0, 0, 1),
            'particles-3': (0, 1, 0, 1),
            'particles-4': (0, 0, 1, 1),
            'particles-5': (1, 0, 1, 1)
        }
        for name, color in colors.items():
            node = bean.copyTo(NodePath())
            node.setColorScale(*color)
            p = effect.getParticlesNamed(name)
            p.renderer.setGeomNode(node.node())
        fadeColor = VBase4(0, 1, 0, 1)
    elif menuIndex == RESISTANCE_RESTOCK:
        effect = BattleParticles.loadParticleFile('resistanceEffectSprite.ptf')
        invModel = loader.loadModel('phase_3.5/models/gui/inventory_icons')
        invModel.setScale(4)
        invModel.flattenLight()
        icons = []
        if itemValue != -1:
            for item in xrange(6):
                iconName = ToontownBattleGlobals.AvPropsNew[itemValue][item]
                icons.append(invModel.find('**/%s' % iconName))
        else:
            tracks = range(7)
            random.shuffle(tracks)
            for i in xrange(6):
                track = tracks[i]
                item = random.randint(0, 5)
                iconName = ToontownBattleGlobals.AvPropsNew[track][item]
                icons.append(invModel.find('**/%s' % iconName))
        iconDict = {
            'particles-1': icons[0],
            'particles-2': icons[1],
            'particles-3': icons[2],
            'particles-4': icons[3],
            'particles-5': icons[4],
            'particles-6': icons[5]
        }
        for name, icon in iconDict.items():
            p = effect.getParticlesNamed(name)
            p.renderer.setFromNode(icon)
        fadeColor = VBase4(0, 0, 1, 1)
    elif menuIndex == RESISTANCE_MERITS:
        effect = BattleParticles.loadParticleFile('resistanceEffectSprite.ptf')
        cogModel = loader.loadModel('phase_3/models/gui/cog_icons')
        cogModel.setScale(0.75)
        cogModel.flattenLight()

        if itemValue != -1:
            iconDict = {'particles-1': cogModel.find(SuitDNA.suitDeptModelPaths[itemValue])}
        else:
            iconDict = {}

            for i in xrange(len(SuitDNA.suitDepts)):
                iconDict['particles-%s' % (i + 1)] = cogModel.find(SuitDNA.suitDeptModelPaths[i])

        for name, icon in iconDict.items():
            p = effect.getParticlesNamed(name)
            p.renderer.setFromNode(icon)

        fadeColor = VBase4(0.7, 0.7, 0.7, 1.0)
        cogModel.removeNode()
    elif menuIndex == RESISTANCE_TICKETS:
        effect = BattleParticles.loadParticleFile('resistanceEffectSprite.ptf')
        model = loader.loadModel('phase_6/models/karting/tickets')
        model.flattenLight()
        iconDict = {'particles-1': model} 

        for name, icon in iconDict.items():
            p = effect.getParticlesNamed(name)
            p.renderer.setFromNode(icon)

        fadeColor = VBase4(1, 1, 0, 1)
    else:
        return
    recolorToons = Parallel()
    for toonId in nearbyToons:
        toon = base.cr.doId2do.get(toonId)
        if toon and not toon.ghostMode and not toon.isEmpty() and not toon.getGeomNode().isEmpty():
            i = Sequence(
                toon.doToonColorScale(fadeColor, 0.3),
                toon.doToonColorScale(toon.defaultColorScale, 0.3),
                Func(toon.restoreDefaultColorScale)
            )
            recolorToons.append(i)
    if speakingToon.carActive:
        # TODO: FIX KART INTERACTION WITH PARTICLEINTERVALS
        i = Sequence(Wait(0.2), recolorToons)
    else:
        i = Parallel(
            ParticleInterval(effect, speakingToon, worldRelative=0, duration=3, cleanup=True),
            Sequence(Wait(0.2), recolorToons),
            autoFinish=1
        )
    i.start()
