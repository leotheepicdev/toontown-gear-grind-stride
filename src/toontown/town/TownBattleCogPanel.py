from direct.gui.DirectGui import *
from toontown.battle import SuitBattleGlobals
from toontown.suit import Suit, SuitHealthBar
from toontown.base import TTLocalizer
from toontown.base.ToontownGlobals import EXECUTIVE_DAMAGE_BONUS, VIRTUAL_ATK
import math

class TownBattleCogPanel(DirectFrame):

    def __init__(self, battle):
        gui = loader.loadModel('phase_3.5/models/gui/battle_gui')
        DirectFrame.__init__(self, relief=None, image=gui.find('**/ToonBtl_Status_BG'), image_color=(0.86, 0.86, 0.86, 0.7), scale=0.8)
        self.initialiseoptions(TownBattleCogPanel)
        self.battle = battle
        self.levelText = DirectLabel(parent=self, text='', pos=(-0.06, 0, -0.075), text_scale=0.055)
        self.typeText = DirectLabel(parent=self, text='', pos=(0.12, 0, -0.075), text_scale=0.045)
        self.healthBar = SuitHealthBar.SuitHealthBar()
        self.generateHealthBar()
        self.hoverButton = DirectButton(parent=self, relief=None, image_scale=(0.07, 0, 0.06), pos=(0.105, 0, 0.05), image='phase_3/maps/invisible.png', pressEffect=0)
        self.hoverButton.setTransparency(True)
        self.hoverButton.bind(DGG.EXIT, self.battle.hideRolloverFrame)
        self.suit = None
        self.suitHead = None
        self.hide()
        gui.removeNode()
    
    def cleanup(self):
        self.cleanupHead()
        self.levelText.removeNode()
        self.typeText.removeNode()
        self.healthBar.delete()
        self.hoverButton.removeNode()
        del self.levelText
        del self.typeText
        del self.healthBar
        del self.hoverButton
        DirectFrame.destroy(self)
    
    def cleanupHead(self):
        if self.suitHead:
            self.suitHead.removeNode()
            del self.suitHead

    def setSuit(self, suit):
        if self.suit == suit:
            return

        self.cleanupHead()
        self.suit = suit
        self.generateSuitHead(suit.getStyleName())
        if self.suit.getExecutive():
            self['image_color'] = (0.56, 0.56, 0.56, 0.7)
        else:
            self['image_color'] = (0.86, 0.86, 0.86, 0.7)
        self.updateHealthBar()
        self.levelText['text'] = TTLocalizer.CogPanelLevel % suit.getActualLevel()
        self.typeText['text'] = suit.getTypeText()
        self.updateRolloverBind()
    
    def updateRolloverBind(self):
        if not self.suit:
            return

        attributes = SuitBattleGlobals.SuitAttributes[self.suit.getStyleName()]
        groupAttacks, singleAttacks = SuitBattleGlobals.getAttacksByType(attributes)
        level = self.suit.getActualLevel()
        info = TTLocalizer.BattleCogPopup % (self.suit.getHP(), self.suit.getMaxHP(), self.getAttackStrings(groupAttacks, level), self.getAttackStrings(singleAttacks, level))
        
        if TTLocalizer.BattleCogPopupDangerColor in info:
            info = TTLocalizer.BattleCogPopupDanger + info

        self.hoverButton.bind(DGG.ENTER, self.battle.showRolloverFrame, extraArgs=[self, TTLocalizer.BattleHoverCog, info])
        
    def getAttackStrings(self, attacks, level):
        attackStrings = []
        
        for attack in attacks:
            hp = SuitBattleGlobals.getAttackDamage(attack[1], level)
            if self.suit.getExecutive():
                hp = int(math.ceil(hp * EXECUTIVE_DAMAGE_BONUS))
            elif self.suit.getVirtual() == VIRTUAL_ATK:
                hp *= 2
            attackString = TTLocalizer.BattleCogPopupAttackDanger if self.battle.isAttackDangerous(hp) else TTLocalizer.BattleCogPopupAttack
            attackStrings.append(attackString % (TTLocalizer.SuitAttackNames[attack[0]], hp))

        return '\n'.join(attackStrings) if attackStrings else TTLocalizer.BattleCogNoAttacks

    def generateSuitHead(self, name):
        self.suitHead = Suit.attachSuitHead(self, name)
        self.suitHead.setScale(0.05)
        self.suitHead.setPos(0.1, 0, 0.01)
        
    def generateHealthBar(self):
        self.healthBar.generate()
        self.healthBar.geom.reparentTo(self)
        self.healthBar.geom.setScale(0.5)
        self.healthBar.geom.setPos(-0.065, 0, 0.05)
        self.healthBar.geom.show()

    def updateHealthBar(self):
        if not self.suit:
            return

        self.healthBar.update(float(self.suit.getHP()) / float(self.suit.getMaxHP()))