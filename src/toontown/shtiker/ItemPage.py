import ShtikerPage
from direct.gui.DirectGui import *
from toontown.base import ToontownGlobals
from toontown.base import TTLocalizer
import OptionChooser
from lib.nametag import NametagConstants

class ItemPage(ShtikerPage.ShtikerPage):

    def __init__(self):
        ShtikerPage.ShtikerPage.__init__(self)
        self.optionChoosers = {}
        
    def load(self):
        self.title = DirectLabel(parent=self, relief=None, text=TTLocalizer.ItemPageTitle, text_scale=0.12, textMayChange=0, pos=(0, 0, 0.6))
        self.optionChoosers['pole'] = OptionChooser.OptionChooser(self, TTLocalizer.FishingPoleLabel, 0, self.__updateFishingPole, [False], self.__applyFishingPole)
        self.optionChoosers['nametag_style'] = OptionChooser.OptionChooser(self, TTLocalizer.NametagStyleLabel, 1, self.__updateNametagStyle, [False], self.__applyNametagStyle)
        self.optionChoosers['nametag_color'] = OptionChooser.OptionChooser(self, TTLocalizer.NametagColorLabel, 2, self.__updateNametagColor, [False], self.__applyNametagColor)
        self.optionChoosers['nametag_panel'] = OptionChooser.OptionChooser(self, TTLocalizer.NametagPanelLabel, 3, self.__updateNametagPanel, [False], self.__applyNametagPanel)
        self.optionChoosers['cheesy_effect'] = OptionChooser.OptionChooser(self, TTLocalizer.CheesyEffectLabel, 4, self.__updateCheesyEffect, [False], self.__applyCheesyEffect)
        ShtikerPage.ShtikerPage.load(self)

    def unload(self):
        del self.title
        for chooser in self.optionChoosers.values():
            chooser.unload()
        ShtikerPage.ShtikerPage.unload(self)

    def enter(self):
        self.__updateNametagStyle()
        self.__updateNametagColor()
        self.__updateNametagPanel()
        self.__updateFishingPole()
        self.__updateCheesyEffect()
        self.accept('refreshNametagStyle', self.__updateNametagStyle)
        self.accept('refreshNametagColor', self.__updateNametagColor)
        self.accept('refreshNametagPanel', self.__updateNametagPanel)
        self.accept('refreshFishingRod', self.__updateFishingPole)
        self.accept('refreshCheesyEffect', self.__updateCheesyEffect)
        ShtikerPage.ShtikerPage.enter(self)

    def exit(self):
        self.ignore('refreshNametagStyle')
        self.ignore('refreshNametagColor')
        self.ignore('refreshNametagPanel')
        self.ignore('refreshFishingRod')
        self.ignore('refreshCheesyEffect')
        for chooser in self.optionChoosers.values():
            chooser.exit(chooser.index)
        ShtikerPage.ShtikerPage.exit(self)

    def __updateNametagStyle(self, resetIndex=True):
        chooser = self.optionChoosers['nametag_style']
        if resetIndex:
            chooser.setIndex(base.localAvatar.nametagStyles.index(base.localAvatar.getNametagStyle()))
        nametagId = base.localAvatar.nametagStyles[chooser.index]
        chooser.setDisplayText('%s\n%s' % (base.localAvatar.getName(), TTLocalizer.NametagFontNames[nametagId]))
        chooser.setDisplayFont(ToontownGlobals.getNametagFont(nametagId))
        chooser.decideButtons(0, len(base.localAvatar.nametagStyles) - 1)

    def __applyNametagStyle(self, index):
        if index != -1 and index != base.localAvatar.nametagStyles.index(base.localAvatar.getNametagStyle()):
            base.localAvatar.requestNametagStyle(base.localAvatar.nametagStyles[index])
			
    def __updateNametagColor(self, resetIndex=True):
        chooser = self.optionChoosers['nametag_color']
        if resetIndex:
            chooser.setIndex(base.localAvatar.nametagColors.index(base.localAvatar.getNametagColor()))
        nametagColorId = base.localAvatar.nametagColors[chooser.index]
        color = NametagConstants.TOON_COLORS[nametagColorId][0][0]
        chooser.setDisplayText('%s' % TTLocalizer.NametagColorNames[nametagColorId])
        chooser.setDisplayFont(ToontownGlobals.getToonFont())
        chooser.setDisplayTextFG(color)       
        chooser.decideButtons(0, len(base.localAvatar.nametagColors) - 1)

    def __applyNametagColor(self, index):
        if index != -1 and index != base.localAvatar.nametagColors.index(base.localAvatar.getNametagColor()):
            base.localAvatar.requestNametagColor(base.localAvatar.nametagColors[index])
            
    def __updateNametagPanel(self, resetIndex=True):
        chooser = self.optionChoosers['nametag_panel']
        if resetIndex:
            chooser.setIndex(base.localAvatar.getNametagPanel())
        chooser.setDisplayText('%s' % TTLocalizer.NametagPanelNames[chooser.index])
        chooser.setDisplayFont(ToontownGlobals.getToonFont())
        chooser.decideButtons(0, NametagConstants.MaxPanel)

    def __applyNametagPanel(self, index):
        if index != -1 and index != base.localAvatar.getNametagPanel():
            base.localAvatar.requestNametagPanel(index)

    def __updateFishingPole(self, resetIndex=True):
        chooser = self.optionChoosers['pole']
        if resetIndex:
            chooser.setIndex(base.localAvatar.getFishingRod())
        chooser.setDisplayText(TTLocalizer.FishingRodNameDict[chooser.index])
        chooser.decideButtons(0, base.localAvatar.maxFishingRod)
    
    def __applyFishingPole(self, index):
        if index != -1 and index != base.localAvatar.getFishingRod():
            base.localAvatar.requestFishingRod(index)

    def __updateCheesyEffect(self, resetIndex=True):
        chooser = self.optionChoosers['cheesy_effect']
        if resetIndex:
            chooser.setIndex(base.localAvatar.cheesyEffects.index(base.localAvatar.getCheesyEffect()))
        cheesyEffect = base.localAvatar.cheesyEffects[chooser.index]
        chooser.setDisplayText(TTLocalizer.CheesyEffectNames[cheesyEffect])
        chooser.decideButtons(0, len(base.localAvatar.cheesyEffects) - 1)

    def __applyCheesyEffect(self, index):
        if index != -1 and index != base.localAvatar.cheesyEffects.index(base.localAvatar.getCheesyEffect()):
            base.localAvatar.requestCheesyEffect(base.localAvatar.cheesyEffects[index])
