from direct.actor import Actor
from direct.directnotify import DirectNotifyGlobal
from direct.interval.IntervalGlobal import Sequence, Func
from toontown.hood import InteractiveAnimatedProp
from toontown.base import ToontownGlobals, ToontownBattleGlobals, TTLocalizer

class MailboxInteractiveProp(InteractiveAnimatedProp.InteractiveAnimatedProp):
    notify = DirectNotifyGlobal.directNotify.newCategory('MailboxInteractiveProp')
    BattleTrack = ToontownBattleGlobals.THROW_TRACK
    BattleCheerText = TTLocalizer.InteractivePropTrackBonusTerms[BattleTrack]

    ZoneToIdles = {
        ToontownGlobals.ToontownCentral: (('tt_a_ara_ttc_mailbox_idle0', 3, 10, 'tt_a_ara_ttc_mailbox_idle0settle', 3, 10),
                                         ('tt_a_ara_ttc_mailbox_idleTake2', 1, 1, None, 3, 10),
                                         ('tt_a_ara_ttc_mailbox_idleLook1', 1, 1, None, 3, 10),
                                         ('tt_a_ara_ttc_mailbox_idleAwesome3', 1, 1, None, 3, 10)),
        ToontownGlobals.DonaldsDock: (('tt_a_ara_dod_mailbox_idle0', 3, 10, 'tt_a_ara_dod_mailbox_idle0settle', 3, 10),
                                     ('tt_a_ara_dod_mailbox_idle2', 1, 1, None, 3, 10),
                                     ('tt_a_ara_dod_mailbox_idle1', 1, 1, None, 3, 10),
                                     ('tt_a_ara_dod_mailbox_idleAwesome3', 1, 1, None, 3, 10)),
        ToontownGlobals.DaisyGardens: (('tt_a_ara_dga_mailbox_idle0', 3, 10, 'tt_a_ara_dga_mailbox_idle0settle', 3, 10),
                                      ('tt_a_ara_dga_mailbox_idleTake1', 1, 1, None, 3, 10),
                                      ('tt_a_ara_dga_mailbox_idleLook2', 1, 1, None, 3, 10),
                                      ('tt_a_ara_dga_mailbox_idleAwesome3', 1, 1, None, 3, 10)),
        ToontownGlobals.MinniesMelodyland: (('tt_a_ara_mml_mailbox_idle0', 3, 10, 'tt_a_ara_mml_mailbox_idle0settle', 3, 10),
                                           ('tt_a_ara_mml_mailbox_idleTake1', 1, 1, None, 3, 10),
                                           ('tt_a_ara_mml_mailbox_idleLook2', 1, 1, None, 3, 10),
                                           ('tt_a_ara_mml_mailbox_idleAwesome3', 1, 1, None, 3, 10)),
        ToontownGlobals.TheBrrrgh: (('tt_a_ara_tbr_mailbox_idleShiver1', 1, 1, None, 3, 10),
                                   ('tt_a_ara_tbr_mailbox_idleSneeze2', 1, 1, None, 3, 10),
                                   ('tt_a_ara_tbr_mailbox_idleSpin0', 1, 1, None, 3, 10),
                                   ('tt_a_ara_tbr_mailbox_idleAwesome3', 1, 1, None, 3, 10)),
        ToontownGlobals.DonaldsDreamland: (('tt_a_ara_ddl_mailbox_idleSleep0', 3, 10, None, 0, 0),
                                          ('tt_a_ara_ddl_mailbox_idleShake2', 1, 1, None, 0, 0),
                                          ('tt_a_ara_ddl_mailbox_idleSnore1', 1, 1, None, 0, 0),
                                          ('tt_a_ara_ddl_mailbox_idleAwesome3', 1, 1, None, 0, 0)),
        ToontownGlobals.WackyWest: (('tt_a_ara_ttc_mailbox_idle0', 3, 10, 'tt_a_ara_ttc_mailbox_idle0settle', 3, 10),
                                   ('tt_a_ara_ttc_mailbox_idleTake2', 1, 1, None, 3, 10),
                                   ('tt_a_ara_ttc_mailbox_idleLook1', 1, 1, None, 3, 10),
                                   ('tt_a_ara_ttc_mailbox_idleAwesome3', 1, 1, None, 3, 10)),
        ToontownGlobals.ConstructionZone: (('tt_a_ara_ttc_mailbox_idle0', 3, 10, 'tt_a_ara_ttc_mailbox_idle0settle', 3, 10),
                                           ('tt_a_ara_ttc_mailbox_idleTake2', 1, 1, None, 3, 10),
                                           ('tt_a_ara_ttc_mailbox_idleLook1', 1, 1, None, 3, 10),
                                           ('tt_a_ara_ttc_mailbox_idleAwesome3', 1, 1, None, 3, 10))}

    ZoneToIdleIntoFightAnims = {
        ToontownGlobals.ToontownCentral: 'tt_a_ara_ttc_mailbox_idleIntoFight',
        ToontownGlobals.DonaldsDock: 'tt_a_ara_dod_mailbox_idleIntoFight',
        ToontownGlobals.DaisyGardens: 'tt_a_ara_dga_mailbox_idleIntoFight',
        ToontownGlobals.MinniesMelodyland: 'tt_a_ara_mml_mailbox_idleIntoFight',
        ToontownGlobals.TheBrrrgh: 'tt_a_ara_tbr_mailbox_idleIntoFight',
        ToontownGlobals.DonaldsDreamland: 'tt_a_ara_ddl_mailbox_idleIntoFight',
        ToontownGlobals.WackyWest: 'tt_a_ara_ttc_mailbox_idleIntoFight',
        ToontownGlobals.ConstructionZone: 'tt_a_ara_ttc_mailbox_idleIntoFight'}

    ZoneToVictoryAnims = {
        ToontownGlobals.ToontownCentral: 'tt_a_ara_ttc_mailbox_victoryDance',
        ToontownGlobals.DonaldsDock: 'tt_a_ara_dod_mailbox_victoryDance',
        ToontownGlobals.DaisyGardens: 'tt_a_ara_dga_mailbox_victoryDance',
        ToontownGlobals.MinniesMelodyland: 'tt_a_ara_mml_mailbox_victoryDance',
        ToontownGlobals.TheBrrrgh: 'tt_a_ara_tbr_mailbox_victoryDance',
        ToontownGlobals.DonaldsDreamland: 'tt_a_ara_ddl_mailbox_victoryDance',
        ToontownGlobals.WackyWest: 'tt_a_ara_tbr_mailbox_victoryDance',
        ToontownGlobals.ConstructionZone: 'tt_a_ara_ttc_mailbox_victoryDance'}

    ZoneToSadAnims = {
        ToontownGlobals.ToontownCentral: 'tt_a_ara_ttc_mailbox_fightSad',
        ToontownGlobals.DonaldsDock: 'tt_a_ara_dod_mailbox_fightSad',
        ToontownGlobals.DaisyGardens: 'tt_a_ara_dga_mailbox_fightSad',
        ToontownGlobals.MinniesMelodyland: 'tt_a_ara_mml_mailbox_fightSad',
        ToontownGlobals.TheBrrrgh: 'tt_a_ara_tbr_mailbox_fightSad',
        ToontownGlobals.DonaldsDreamland: 'tt_a_ara_ddl_mailbox_fightSad',
        ToontownGlobals.WackyWest: 'tt_a_ara_ttc_mailbox_fightIdle',
        ToontownGlobals.ConstructionZone: 'tt_a_ara_ttc_mailbox_fightIdle'}

    ZoneToFightAnims = {
        ToontownGlobals.ToontownCentral: ('tt_a_ara_ttc_mailbox_fightBoost', 'tt_a_ara_ttc_mailbox_fightCheer', 'tt_a_ara_ttc_mailbox_fightIdle'),
        ToontownGlobals.DonaldsDock: ('tt_a_ara_dod_mailbox_fightBoost', 'tt_a_ara_dod_mailbox_fightCheer', 'tt_a_ara_dod_mailbox_fightIdle'),
        ToontownGlobals.DaisyGardens: ('tt_a_ara_dga_mailbox_fightBoost', 'tt_a_ara_dga_mailbox_fightCheer', 'tt_a_ara_dga_mailbox_fightIdle'),
        ToontownGlobals.MinniesMelodyland: ('tt_a_ara_mml_mailbox_fightBoost', 'tt_a_ara_mml_mailbox_fightCheer', 'tt_a_ara_mml_mailbox_fightIdle'),
        ToontownGlobals.TheBrrrgh: ('tt_a_ara_tbr_mailbox_fightBoost', 'tt_a_ara_tbr_mailbox_fightCheer', 'tt_a_ara_tbr_mailbox_fightIdle'),
        ToontownGlobals.DonaldsDreamland: ('tt_a_ara_ddl_mailbox_fightBoost', 'tt_a_ara_ddl_mailbox_fightCheer', 'tt_a_ara_ddl_mailbox_fightIdle'),
        ToontownGlobals.WackyWest: ('tt_a_ara_ttc_mailbox_fightBoost', 'tt_a_ara_ttc_mailbox_fightCheer', 'tt_a_ara_ttc_mailbox_fightIdle'),
        ToontownGlobals.ConstructionZone: ('tt_a_ara_ttc_mailbox_fightBoost', 'tt_a_ara_ttc_mailbox_fightCheer', 'tt_a_ara_ttc_mailbox_fightIdle')}
    IdlePauseTime = base.config.GetFloat('prop-idle-pause-time', 0.0)

    def setupActor(self, node):
        self.pieActor = Actor.Actor('phase_5/models/char/tt_r_prp_ext_piePackage', {'fightBoost': 'phase_5/models/char/tt_a_prp_ext_piePackage_fightBoost'})
        self.pieActor.reparentTo(self.node)
        self.pieActor.hide()

        InteractiveAnimatedProp.InteractiveAnimatedProp.setupActor(self, node)

    def hasSpecialIval(self, origAnimName):
        return 'fightBoost' in origAnimName

    def getSpecialIval(self, origAnimName):
        result = Sequence()

        if self.hasSpecialIval(origAnimName):
            result.append(Func(self.pieActor.show))
            result.append(self.pieActor.actorInterval('fightBoost'))
            result.append(Func(self.pieActor.hide))

        return result
