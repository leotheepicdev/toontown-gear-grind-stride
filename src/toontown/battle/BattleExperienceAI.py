from direct.directnotify import DirectNotifyGlobal
from toontown.base import ToontownBattleGlobals
from toontown.suit import SuitDNA, SuitGlobals
BattleExperienceAINotify = DirectNotifyGlobal.directNotify.newCategory('BattleExperienceAI')

def getSkillGained(toonSkillPtsGained, toonId, track):
    exp = 0
    expList = toonSkillPtsGained.get(toonId, None)
    if expList != None:
        exp = expList[track]
    return int(exp + 0.5)

def getBattleExperience(numToons, activeToons, toonExp, toonSkillPtsGained, toonOrigQuests, toonItems, toonOrigMerits, toonMerits, toonParts, suitsKilled, helpfulToonsList = None):
    if helpfulToonsList == None:
        BattleExperienceAINotify.warning('=============\nERROR ERROR helpfulToons=None in assignRewards , tell Red')
    p = []
    for k in xrange(numToons):
        toon = None
        if k < len(activeToons):
            toonId = activeToons[k]
            toon = simbase.air.doId2do.get(toonId)
        if toon == None:
            p.append(-1)
            p.append([0,
             0,
             0,
             0,
             0,
             0,
             0])
            p.append([0,
             0,
             0,
             0,
             0,
             0,
             0])
            p.append([])
            p.append([])
            p.append([])
            p.append([0,
             0,
             0,
             0])
            p.append([0,
             0,
             0,
             0])
            p.append([0,
             0,
             0,
             0])
        else:
            p.append(toonId)
            origExp = toonExp[toonId]
            earnedExp = []
            for i in xrange(len(ToontownBattleGlobals.Tracks)):
                earnedExp.append(getSkillGained(toonSkillPtsGained, toonId, i))

            p.append(origExp)
            p.append(earnedExp)
            origQuests = toonOrigQuests.get(toonId, [])
            p.append(origQuests)
            items = toonItems.get(toonId, ([], []))
            p.append(items[0])
            p.append(items[1])
            origMerits = toonOrigMerits.get(toonId, [])
            p.append(origMerits)
            merits = toonMerits.get(toonId, [0,
             0,
             0,
             0])
            p.append(merits)
            parts = toonParts.get(toonId, [0,
             0,
             0,
             0])
            p.append(parts)

    deathList = []
    toonIndices = {}
    for i in xrange(len(activeToons)):
        toonIndices[activeToons[i]] = i

    for deathRecord in suitsKilled:
        level = deathRecord['level']
        type = deathRecord['type']
        unlisted = 0
        if deathRecord['isBoss'] > 0:
            level = 0
            typeNum = SuitDNA.suitDepts.index(deathRecord['track'])
        elif type in SuitGlobals.unlistedSuits:
            unlisted = 1
            typeNum = SuitGlobals.unlistedSuits.index(type)
        else:
            typeNum = SuitDNA.suitHeadTypes.index(type)
        involvedToonIds = deathRecord['activeToons']
        toonBits = 0
        for toonId in involvedToonIds:
            if toonId in toonIndices:
                toonBits |= 1 << toonIndices[toonId]

        flags = 0
        if deathRecord['isSkelecog']:
            flags |= ToontownBattleGlobals.DLF_SKELECOG
        if deathRecord['isForeman']:
            flags |= ToontownBattleGlobals.DLF_FOREMAN
        if deathRecord['isBoss'] > 0:
            flags |= ToontownBattleGlobals.DLF_BOSS
        if deathRecord['isSupervisor']:
            flags |= ToontownBattleGlobals.DLF_SUPERVISOR
        if deathRecord['isVirtual']:
            flags |= ToontownBattleGlobals.DLF_VIRTUAL
        if 'hasRevives' in deathRecord and deathRecord['hasRevives']:
            flags |= ToontownBattleGlobals.DLF_REVIVES
        if deathRecord['isExecutive']:
            flags |= ToontownBattleGlobals.DLF_EXECUTIVE
        deathList.extend([typeNum, level, toonBits, flags, unlisted])

    p.append(deathList)
    if helpfulToonsList == None:
        helpfulToonsList = []
    p.append(helpfulToonsList)
    return p

def assignRewards(activeToons, toonSkillPtsGained, suitsKilled, zoneId, helpfulToons = None):
    if helpfulToons == None:
        BattleExperienceAINotify.warning('=============\nERROR ERROR helpfulToons=None in assignRewards , tell Red')
    activeToonList = []
    for t in activeToons:
        toon = simbase.air.doId2do.get(t)
        if toon != None:
            activeToonList.append(toon)

    for toon in activeToonList:
        for i in xrange(len(ToontownBattleGlobals.Tracks)):
            exp = getSkillGained(toonSkillPtsGained, toon.doId, i)
            totalExp = exp + toon.experience.getExp(i)
            if toon.experience.getExp(i) == ToontownBattleGlobals.MaxSkill:
                continue
            if totalExp >= ToontownBattleGlobals.MaxSkill:
                toon.experience.setExp(i, ToontownBattleGlobals.MaxSkill)
                toon.inventory.addItem(i, ToontownBattleGlobals.UBER_GAG_LEVEL_INDEX)
                continue
            if exp > 0:
                newGagList = toon.experience.getNewGagIndexList(i, exp)
                toon.experience.addExp(i, amount=exp)
                toon.inventory.addItemWithList(i, newGagList)
        toon.b_setExperience(toon.experience.makeNetString())
        toon.d_setInventory(toon.inventory.makeNetString())
        toon.b_setAnimState('victory', 1)

        if simbase.air.config.GetBool('battle-passing-no-credit', True):
            if helpfulToons and toon.doId in helpfulToons:
                simbase.air.questManager.toonKilledCogs(toon, suitsKilled, zoneId)
                simbase.air.cogPageManager.toonKilledCogs(toon, suitsKilled, zoneId)
            else:
                BattleExperienceAINotify.debug('toon=%d unhelpful not getting killed cog quest credit' % toon.doId)
        else:
            simbase.air.questManager.toonKilledCogs(toon, suitsKilled, zoneId)
            simbase.air.cogPageManager.toonKilledCogs(toon, suitsKilled, zoneId)