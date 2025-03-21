from direct.actor import Actor
from direct.directnotify import DirectNotifyGlobal
from direct.interval.IntervalGlobal import Sequence, Func
from toontown.hood import InteractiveAnimatedProp
from toontown.base import ToontownGlobals, ToontownBattleGlobals, TTLocalizer

class HydrantInteractiveProp(InteractiveAnimatedProp.InteractiveAnimatedProp):
    notify = DirectNotifyGlobal.directNotify.newCategory('HydrantInteractiveProp')
    BattleTrack = ToontownBattleGlobals.SQUIRT_TRACK
    BattleCheerText = TTLocalizer.InteractivePropTrackBonusTerms[BattleTrack]

    ZoneToIdles = {
        ToontownGlobals.ToontownCentral: (('tt_a_ara_ttc_hydrant_idle0', 1, 1, None, 3, 10),
                                         ('tt_a_ara_ttc_hydrant_idle2', 1, 1, None, 3, 10),
                                         ('tt_a_ara_ttc_hydrant_idle1', 1, 1, None, 3, 10),
                                         ('tt_a_ara_ttc_hydrant_idleAwesome3', 1, 1, None, 3, 10)),
        ToontownGlobals.DonaldsDock: (('tt_a_ara_ttc_hydrant_idle0', 1, 1, None, 3, 10),
                                     ('tt_a_ara_ttc_hydrant_idle2', 1, 1, None, 3, 10),
                                     ('tt_a_ara_ttc_hydrant_idle1', 1, 1, None, 3, 10),
                                     ('tt_a_ara_ttc_hydrant_idleAwesome3', 1, 1, None, 3, 10)),
        ToontownGlobals.DaisyGardens: (('tt_a_ara_dga_hydrant_idle0', 3, 10, 'tt_a_ara_dga_hydrant_idle0settle', 3, 10),
                                      ('tt_a_ara_dga_hydrant_idleLook1', 1, 1, None, 3, 10),
                                      ('tt_a_ara_dga_hydrant_idleSneeze2', 1, 1, None, 3, 10),
                                      ('tt_a_ara_dga_hydrant_idleAwesome3', 1, 1, None, 3, 10)),
        ToontownGlobals.MinniesMelodyland: (('tt_a_ara_mml_hydrant_idle0', 3, 10, 'tt_a_ara_mml_hydrant_idle0settle', 3, 10),
                                           ('tt_a_ara_mml_hydrant_idle2', 3, 10, 'tt_a_ara_mml_hydrant_idle2settle', 3, 10),
                                           ('tt_a_ara_mml_hydrant_idle1', 3, 10, 'tt_a_ara_mml_hydrant_idle1settle', 3, 10),
                                           ('tt_a_ara_mml_hydrant_idleAwesome3', 1, 1, None, 3, 10)),
        ToontownGlobals.TheBrrrgh: (('tt_a_ara_tbr_hydrant_idleShiver1', 1, 1, None, 3, 10),
                                   ('tt_a_ara_tbr_hydrant_idleRubNose0', 1, 1, None, 3, 10),
                                   ('tt_a_ara_tbr_hydrant_idleSneeze2', 1, 1, None, 3, 10),
                                   ('tt_a_ara_tbr_hydrant_idleAwesome3', 1, 1, None, 3, 10)),
        ToontownGlobals.DonaldsDreamland: (('tt_a_ara_ddl_hydrant_idle0', 3, 10, None, 0, 0),
                                          ('tt_a_ara_ddl_hydrant_idle1', 1, 1, None, 0, 0),
                                          ('tt_a_ara_ddl_hydrant_idle2', 1, 1, None, 0, 0),
                                          ('tt_a_ara_ddl_hydrant_idleAwesome3', 1, 1, None, 0, 0)),
        ToontownGlobals.WackyWest: (('tt_a_ara_ttc_hydrant_idle0', 1, 1, None, 3, 10),
                                         ('tt_a_ara_ttc_hydrant_idle2', 1, 1, None, 3, 10),
                                         ('tt_a_ara_ttc_hydrant_idle1', 1, 1, None, 3, 10),
                                         ('tt_a_ara_ttc_hydrant_idleAwesome3', 1, 1, None, 3, 10)),
        ToontownGlobals.ConstructionZone: (('tt_a_ara_ttc_hydrant_idle0', 1, 1, None, 3, 10),
                                           ('tt_a_ara_ttc_hydrant_idle2', 1, 1, None, 3, 10),
                                           ('tt_a_ara_ttc_hydrant_idle1', 1, 1, None, 3, 10),
                                           ('tt_a_ara_ttc_hydrant_idleAwesome3', 1, 1, None, 3, 10))}

    ZoneToIdleIntoFightAnims = {
        ToontownGlobals.ToontownCentral: 'tt_a_ara_ttc_hydrant_idleIntoFight',
        ToontownGlobals.DonaldsDock: 'tt_a_ara_ttc_hydrant_idleIntoFight',
        ToontownGlobals.DaisyGardens: 'tt_a_ara_dga_hydrant_idleIntoFight',
        ToontownGlobals.MinniesMelodyland: 'tt_a_ara_mml_hydrant_idleIntoFight',
        ToontownGlobals.TheBrrrgh: 'tt_a_ara_tbr_hydrant_idleIntoFight',
        ToontownGlobals.DonaldsDreamland: 'tt_a_ara_ddl_hydrant_idleIntoFight',
        ToontownGlobals.WackyWest: 'tt_a_ara_ttc_hydrant_idleIntoFight',
        ToontownGlobals.ConstructionZone: 'tt_a_ara_ttc_hydrant_idleIntoFight'}

    ZoneToVictoryAnims = {
        ToontownGlobals.ToontownCentral: 'tt_a_ara_ttc_hydrant_victoryDance',
        ToontownGlobals.DonaldsDock: 'tt_a_ara_ttc_hydrant_victoryDance',
        ToontownGlobals.DaisyGardens: 'tt_a_ara_dga_hydrant_victoryDance',
        ToontownGlobals.MinniesMelodyland: 'tt_a_ara_mml_hydrant_victoryDance',
        ToontownGlobals.TheBrrrgh: 'tt_a_ara_tbr_hydrant_victoryDance',
        ToontownGlobals.DonaldsDreamland: 'tt_a_ara_ddl_hydrant_victoryDance',
        ToontownGlobals.WackyWest: 'tt_a_ara_tbr_hydrant_victoryDance',
        ToontownGlobals.ConstructionZone: 'tt_a_ara_ttc_hydrant_victoryDance'}


    ZoneToSadAnims = {
        ToontownGlobals.ToontownCentral: 'tt_a_ara_ttc_hydrant_fightSad',
        ToontownGlobals.DonaldsDock: 'tt_a_ara_ttc_hydrant_fightSad',
        ToontownGlobals.DaisyGardens: 'tt_a_ara_dga_hydrant_fightSad',
        ToontownGlobals.MinniesMelodyland: 'tt_a_ara_mml_hydrant_fightSad',
        ToontownGlobals.TheBrrrgh: 'tt_a_ara_tbr_hydrant_fightSad',
        ToontownGlobals.DonaldsDreamland: 'tt_a_ara_ddl_hydrant_fightSad',
        ToontownGlobals.WackyWest: 'tt_a_ara_ddl_hydrant_fightSad',
        ToontownGlobals.ConstructionZone: 'tt_a_ara_ttc_hydrant_fightSad'}


    ZoneToFightAnims = {
        ToontownGlobals.ToontownCentral: ('tt_a_ara_ttc_hydrant_fightBoost', 'tt_a_ara_ttc_hydrant_fightCheer', 'tt_a_ara_ttc_hydrant_fightIdle'),
        ToontownGlobals.DonaldsDock: ('tt_a_ara_ttc_hydrant_fightBoost', 'tt_a_ara_ttc_hydrant_fightCheer', 'tt_a_ara_ttc_hydrant_fightIdle'),
        ToontownGlobals.DaisyGardens: ('tt_a_ara_dga_hydrant_fightBoost', 'tt_a_ara_dga_hydrant_fightCheer', 'tt_a_ara_dga_hydrant_fightIdle'),
        ToontownGlobals.MinniesMelodyland: ('tt_a_ara_mml_hydrant_fightBoost', 'tt_a_ara_mml_hydrant_fightCheer', 'tt_a_ara_mml_hydrant_fightIdle'),
        ToontownGlobals.TheBrrrgh: ('tt_a_ara_tbr_hydrant_fightBoost', 'tt_a_ara_tbr_hydrant_fightCheer', 'tt_a_ara_tbr_hydrant_fightIdle'),
        ToontownGlobals.DonaldsDreamland: ('tt_a_ara_ddl_hydrant_fightBoost', 'tt_a_ara_ddl_hydrant_fightCheer', 'tt_a_ara_ddl_hydrant_fightIdle'),
        ToontownGlobals.WackyWest: ('tt_a_ara_ttc_hydrant_fightBoost', 'tt_a_ara_ttc_hydrant_fightCheer', 'tt_a_ara_ttc_hydrant_fightIdle'),
        ToontownGlobals.ConstructionZone: ('tt_a_ara_ttc_hydrant_fightBoost', 'tt_a_ara_ttc_hydrant_fightCheer', 'tt_a_ara_ttc_hydrant_fightIdle')}

    IdlePauseTime = base.config.GetFloat('prop-idle-pause-time', 0.0)

    def __init__(self, node):
        self.leftWater = None
        self.rightWater = None
        InteractiveAnimatedProp.InteractiveAnimatedProp.__init__(self, node)

    def setupActor(self, node):
        InteractiveAnimatedProp.InteractiveAnimatedProp.setupActor(self, node)

        if not self.hoodId == ToontownGlobals.TheBrrrgh:
            water = loader.loadModel('phase_5/models/char/tt_m_efx_hydrantSquirt')
            self.leftWater = water.find('**/efx_hydrantSquirtLeft')
            self.rightWater = water.find('**/efx_hydrantSquirtRight')

            if self.leftWater:
                self.leftWater.reparentTo(self.node.find('**/dx_left_water'))
                base.leftWater = self.leftWater
                self.leftWater.hide()

            if self.rightWater:
                self.rightWater.reparentTo(self.node.find('**/dx_right_water'))
                self.rightWater.hide()

    def hideWater(self):
        if self.leftWater:
            self.leftWater.hide()
        if self.rightWater:
            self.rightWater.hide()

    def showWater(self):
        if self.leftWater:
            self.leftWater.show()
        if self.rightWater:
            self.rightWater.show()

    def hasOverrideIval(self, origAnimName):
        return ('fightBoost' in origAnimName or 'fightCheer' in origAnimName) and not self.hoodId == ToontownGlobals.TheBrrrgh

    def getOverrideIval(self, origAnimName):
        result = Sequence()

        if self.hasOverrideIval(origAnimName):
            result.append(Func(self.showWater))
            animAndSound = self.createAnimAndSoundIval('fight0' if 'fightBoost' in origAnimName else 'fight1')
            result.append(animAndSound)
            result.append(Func(self.hideWater))

        return result
