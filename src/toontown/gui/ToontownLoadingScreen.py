from panda3d.core import TransparencyAttrib, Vec3
from direct.gui.DirectGui import *
from direct.gui.DirectGuiGlobals import NO_FADE_SORT_INDEX
from toontown.base import ToontownGlobals
from toontown.base import TTLocalizer
from toontown.hood import ZoneUtil
import random

class ToontownLoadingScreen:
    zone2picturePath = 'phase_3.5/maps/loading/'
    zone2picture = {
        ToontownGlobals.ToontownCentral : 'ttc.jpg',
        ToontownGlobals.SillyStreet: 'ttc_ss.jpg',
        ToontownGlobals.LoopyLane: 'ttc_ll.jpg',
        ToontownGlobals.PunchlinePlace: 'ttc_pp.jpg',
        ToontownGlobals.DonaldsDock : 'dd.jpg',
        ToontownGlobals.BarnacleBoulevard: 'dd_bb.jpg',
        ToontownGlobals.SeaweedStreet: 'dd_ss.jpg',
        ToontownGlobals.LighthouseLane: 'dd_ll.jpg',
        ToontownGlobals.DaisyGardens: 'dg.jpg',
        ToontownGlobals.ElmStreet: 'dg_es.jpg',
        ToontownGlobals.MapleStreet: 'dg_ms.jpg',
        ToontownGlobals.OakStreet: 'dg_os.jpg',
        ToontownGlobals.WalnutWay: 'oz_fww.jpg',
        ToontownGlobals.MinniesMelodyland : 'mml.jpg',
        ToontownGlobals.AltoAvenue: 'mml_aa.jpg',
        ToontownGlobals.BaritoneBoulevard: 'mml_bb.jpg',
        ToontownGlobals.TenorTerrace: 'mml_tt.jpg',
        ToontownGlobals.TheBrrrgh: 'tb.jpg',
        ToontownGlobals.WalrusWay: 'tb_ww.jpg',
        ToontownGlobals.SleetStreet: 'tb_ss.jpg',
        ToontownGlobals.PolarPlace: 'tb_pp.jpg',
        ToontownGlobals.DonaldsDreamland: 'ddl.jpg',
        ToontownGlobals.LullabyLane: 'ddl_ll.jpg',
        ToontownGlobals.PajamaPlace: 'ddl_pp.jpg',
        ToontownGlobals.GoofySpeedway: 'gs.jpg',
        ToontownGlobals.OutdoorZone: 'oz.jpg',
        ToontownGlobals.GolfZone: 'gz.jpg',
        ToontownGlobals.SellbotHQ: 'sbhq.jpg',
        ToontownGlobals.SellbotFactoryInt: 'sbhq_fact.jpg',
        ToontownGlobals.SellbotMegaCorpInt: 'sbhq_fact.jpg',
        ToontownGlobals.CashbotHQ: 'cbhq.jpg',
        ToontownGlobals.LawbotHQ: 'lbhq.jpg',
        ToontownGlobals.BossbotHQ: 'bbhq.jpg'
    }

    def __init__(self):
        self.gui = None
        self.title = DirectLabel(parent=base.a2dpBottomCenter, relief=None, pos=(0, 0, 0.5), text='', 
                                 textMayChange=1, text_scale=0.08, text_fg=(1, 1, 1, 1), text_shadow=(0, 0, 0, 1), text_font=ToontownGlobals.getMinnieFont())
        self.title.hide()
        self.tip = DirectLabel(parent=base.a2dpBottomCenter, relief=None, pos=(0, 0, 0.4), text='', 
                               textMayChange=1, text_wordwrap=40, text_scale=0.05, text_fg=(1, 1, 1, 1), text_shadow=(0, 0, 0, 1), text_font=ToontownGlobals.getMinnieFont())
        self.tip.hide()
        logoScale = 0.7
        self.logo = OnscreenImage(image='phase_3/maps/toontown-logo.png', scale=(((16.0 / 9.0)*logoScale) / (4.0/3.0), 1, logoScale / (4.0/3.0)))
        self.logo.reparentTo(hidden)
        self.logo.setTransparency(TransparencyAttrib.MAlpha)
        scale = self.logo.getScale()
        self.logo.setPos(0, 0, -0.8)

    def destroy(self):
        if self.title:
            self.title.destroy()
            self.title = None
        if self.gui:
            self.gui.destroy()
            self.gui = None
        if self.tip:
            self.tip.destroy()
            self.tip = None
        self.logo.removeNode()

    def getTip(self, tipCategory):
        return TTLocalizer.TipTitle + '\n' + random.choice(TTLocalizer.TipDict.get(tipCategory))

    def getGuiBackground(self, zoneId):
        zone = ZoneUtil.getBranchZone(zoneId)
        if zone in self.zone2picture:
            texture = self.zone2picturePath + self.zone2picture[zone]
        else:
            texture = 'phase_3.5/maps/loading/default.jpg'
        return texture

    def begin(self, label, gui, tipCategory, zoneId):
        self.title['text'] = label
        if gui == 1:
            self.title.show()
            self.gui = OnscreenImage(parent=render2d, image=self.getGuiBackground(zoneId))
            self.gui.setBin('gui-popup', 0)
            self.tip['text'] = self.getTip(tipCategory)
            self.tip.show()
            self.logo.reparentTo(base.a2dpTopCenter, NO_FADE_SORT_INDEX)  # base.a2dpTopLeft
        elif gui == 0:
            self.title.show()
            self.gui = OnscreenImage(parent=render2d, image='phase_3.5/maps/loading/default.jpg')
            self.gui.setBin('gui-popup', 0)
            self.tip['text'] = self.getTip(tipCategory)
            self.tip.show()
            self.logo.reparentTo(base.a2dpTopCenter, NO_FADE_SORT_INDEX)

    def end(self):
        if self.title:
            self.title.hide()
        if self.gui:
            self.gui.hide()
        if self.tip:
            self.tip.hide()
        self.logo.reparentTo(hidden)

