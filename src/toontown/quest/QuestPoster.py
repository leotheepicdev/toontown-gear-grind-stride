from panda3d.core import NodePath, Point3, TextNode, Vec3, Vec4
from direct.gui.DirectGui import *
import Quests
from toontown.toon import NPCToons
from toontown.toon import ToonHead
from toontown.toon import ToonDNA
from toontown.suit import SuitDNA
from toontown.suit import Suit
from toontown.hood import ZoneUtil
from toontown.base import ToontownGlobals
from toontown.base import TTLocalizer
import random
import string
from toontown.toon import LaffMeter
from toontown.base.ToontownBattleGlobals import AvPropsNew
from direct.directnotify import DirectNotifyGlobal
from toontown.gui import TTDialog
from toontown.building import DistributedBuildingQueryMgr

IMAGE_SCALE_LARGE = 0.2
IMAGE_SCALE_SMALL = 0.15
POSTER_WIDTH = 0.7
TEXT_SCALE = TTLocalizer.QPtextScale
TEXT_WORDWRAP = TTLocalizer.QPtextWordwrap

class QuestPoster(DirectFrame):
    notify = DirectNotifyGlobal.directNotify.newCategory('QuestPoster')
    colors = {
              'white':(1,1,1,1),
              'blue':(0.45,0.45,0.8,1),
              'lightBlue':(0.42,0.671,1.0,1.0),
              'green':(0.45,0.8,0.45,1),
              'lightGreen':(0.784,1,0.863,1),
              'red':(0.8,0.45,0.45,1),
              'rewardRed':(0.8,0.3,0.3,1),
              'brightRed':(1.0,0.16,0.16,1.0),
              'brown':(0.52,0.42,0.22,1)
              }
    normalTextColor=(0.3, 0.25, 0.2, 1)
    confirmDeleteButtonEvent = 'confirmDeleteButtonEvent'

    def __init__(self, parent = aspect2d, **kw):
        bookModel = loader.loadModel('phase_3.5/models/gui/stickerbook_gui')
        circleModel = loader.loadModel('phase_3/models/gui/tt_m_gui_mat_nameShop').find('**/tt_t_gui_mat_namePanelCircle')
        questCard = bookModel.find('**/questCard')
        optiondefs = (('relief', None, None),
         ('image', questCard, None),
         ('image_scale', (0.8, 1.0, 0.58), None),
         ('state', DGG.NORMAL, None))
        self.defineoptions(kw, optiondefs)
        DirectFrame.__init__(self, relief=None)
        self.initialiseoptions(QuestPoster)
        self._deleteCallback = None
        self.questFrame = DirectFrame(parent=self, relief=None)
        self.headline = DirectLabel(parent=self.questFrame, relief=None, text='', text_font=ToontownGlobals.getMinnieFont(), text_fg=self.normalTextColor, text_scale=0.05, text_align=TextNode.ACenter, text_wordwrap=12.0, textMayChange=1, pos=(0, 0, 0.23))
        self.questInfo = DirectLabel(parent=self.questFrame, relief=None, text='', text_fg=self.normalTextColor, text_scale=TEXT_SCALE, text_align=TextNode.ACenter, text_wordwrap=TEXT_WORDWRAP, textMayChange=1, pos=(0, 0, -0.0625))
        self.rewardText = DirectLabel(parent=self.questFrame, relief=None, text='', text_fg=self.colors['rewardRed'], text_scale=0.0425, text_align=TextNode.ALeft, text_wordwrap=17.0, textMayChange=1, pos=(-0.36, 0, -0.26))
        self.rewardText.hide()
        self.lPictureFrame = DirectFrame(parent=self.questFrame, relief=None, image=bookModel.find('**/questPictureFrame'), image_scale=IMAGE_SCALE_SMALL, text='', text_pos=(0, -0.11), text_fg=self.normalTextColor, text_scale=TEXT_SCALE, text_align=TextNode.ACenter, text_wordwrap=11.0, textMayChange=1)
        self.lPictureFrame.hide()
        self.rPictureFrame = DirectFrame(parent=self.questFrame, relief=None, image=bookModel.find('**/questPictureFrame'), image_scale=IMAGE_SCALE_SMALL, text='', text_pos=(0, -0.11), text_fg=self.normalTextColor, text_scale=TEXT_SCALE, text_align=TextNode.ACenter, text_wordwrap=11.0, textMayChange=1, pos=(0.18, 0, 0.13))
        self.rPictureFrame.hide()
        self.lQuestIcon = DirectFrame(parent=self.lPictureFrame, relief=None, text=' ', text_font=ToontownGlobals.getSuitFont(), text_pos=(0, -0.03), text_fg=self.normalTextColor, text_scale=0.13, text_align=TextNode.ACenter, text_wordwrap=13.0, textMayChange=1)
        self.lQuestIcon.setColorOff(-1)
        self.rQuestIcon = DirectFrame(parent=self.rPictureFrame, relief=None, text=' ', text_font=ToontownGlobals.getSuitFont(), text_pos=(0, -0.03), text_fg=self.normalTextColor, text_scale=0.13, text_align=TextNode.ACenter, text_wordwrap=13.0, textMayChange=1)
        self.rQuestIcon.setColorOff(-1)
        self.auxText = DirectLabel(parent=self.questFrame, relief=None, text='', text_scale=TTLocalizer.QPauxText, text_fg=self.normalTextColor, text_align=TextNode.ACenter, textMayChange=1)
        self.auxText.hide()
        self.questProgress = DirectWaitBar(parent=self.questFrame, relief=DGG.SUNKEN, frameSize=(-0.95, 0.95, -0.1, 0.12), borderWidth=(0.025, 0.025), scale=0.2, frameColor=(0.945, 0.875, 0.706, 1.0), barColor=(0.5, 0.7, 0.5, 1), text='0/0', text_scale=0.19, text_fg=(0.05, 0.14, 0.4, 1), text_align=TextNode.ACenter, text_pos=(0, -0.04), pos=(0, 0, -0.195))
        self.questProgress.hide()
        self.teleportButton = DirectButton(parent=self.questFrame, relief=None, image=circleModel, text=TTLocalizer.TeleportButton, text_scale=0.035, text_pos=(-0.0025, -0.015), pos=(0.175, 0, 0.125), scale=0.75)  #, text_bg=(0, 0.75, 1, 1)
        self.teleportButton.hide()
        self.laffMeter = None
        self.dialog = None

    def destroy(self):
        self._deleteGeoms()
        self.destroyDialog()
        DirectFrame.destroy(self)
    
    def destroyDialog(self, extra=None):
        if self.dialog:
            self.dialog.destroy()
            self.dialog = None
            base.cr.playGame.getPlace().setState('walk')

    def _deleteGeoms(self):
        for icon in (self.lQuestIcon, self.rQuestIcon):
            geom = icon['geom']
            if geom:
                if hasattr(geom, 'delete'):
                    geom.delete()

    def mouseEnterPoster(self, event):
        self.reparentTo(self.getParent())
        sc = Vec3(self.initImageScale)
        sc.setZ(sc[2] + 0.07)
        self['image_scale'] = sc
        self.questFrame.setZ(0.03)
        self.headline.setZ(0.23 + 0.03)
        self.lPictureFrame.setZ(0.13 + 0.03)
        self.rPictureFrame.setZ(0.13 + 0.03)
        self.questInfo.setZ(-0.0625 + 0.03)
        self.questProgress.setZ(-0.195 + 0.03)
        self.auxText.setZ(0.12 + 0.03)
        self.rewardText.setZ(-0.26 + 0.03)
        self.rewardText.show()

    def mouseExitPoster(self, event):
        self['image_scale'] = self.initImageScale
        self.questFrame.setZ(0)
        self.headline.setZ(0.23)
        self.lPictureFrame.setZ(0.13)
        self.rPictureFrame.setZ(0.13)
        self.questInfo.setZ(-0.0625)
        self.questProgress.setZ(-0.195)
        self.auxText.setZ(0.12)
        self.rewardText.setZ(-0.26)
        self.rewardText.hide()

    def createNpcToonHead(self, toNpcId):
        npcInfo = NPCToons.NPCToonDict[toNpcId]
        dnaList = npcInfo[2]
        gender = npcInfo[3]
        if dnaList == 'r':
            dnaList = NPCToons.getRandomDNA(toNpcId, gender)
        dna = ToonDNA.ToonDNA()
        dna.newToonFromProperties(*dnaList)
        head = ToonHead.ToonHead()
        head.setupHead(dna, forGui=1)
        self.fitGeometry(head, fFlip=1)
        return head

    def createLaffMeter(self, hp):
        lm = LaffMeter.LaffMeter(base.localAvatar.style, hp, hp)
        lm.adjustText()
        return lm

    def createSuitHead(self, suitName):
        suitDNA = SuitDNA.SuitDNA()
        suitDNA.newSuit(suitName)
        suit = Suit.Suit()
        suit.setDNA(suitDNA)
        headParts = suit.getHeadParts()
        head = hidden.attachNewNode('head')
        for part in headParts:
            copyPart = part.copyTo(head)
            copyPart.setDepthTest(1)
            copyPart.setDepthWrite(1)

        self.fitGeometry(head, fFlip=1)
        suit.delete()
        suit = None
        return head

    def loadElevator(self, building, numFloors):
        elevatorNodePath = hidden.attachNewNode('elevatorNodePath')
        elevatorModel = loader.loadModel('phase_4/models/modules/elevator')
        floorIndicator = [None] * 5
        npc = elevatorModel.findAllMatches('**/floor_light_?;+s')
        for i in xrange(npc.getNumPaths()):
            np = npc.getPath(i)
            floor = int(np.getName()[-1:]) - 1
            floorIndicator[floor] = np
            if floor < numFloors:
                np.setColor(Vec4(0.5, 0.5, 0.5, 1.0))
            else:
                np.hide()

        elevatorModel.reparentTo(elevatorNodePath)
        suitDoorOrigin = building.find('**/*_door_origin')
        elevatorNodePath.reparentTo(suitDoorOrigin)
        elevatorNodePath.setPosHpr(0, 0, 0, 0, 0, 0)

    def teleportToShop(self, npcId):
        if base.cr.playGame.getPlace().getState() != 'walk':
            return

        npcZone = NPCToons.getNPCZone(npcId)
        npcHood = ZoneUtil.getCanonicalHoodId(npcZone)
        hqZone = {2000:2520, 1000:1507, 3000:3508, 4000:4504, 5000:5502, 7000:7503, 9000:9505}

        if npcZone in (-1, 0, None):
            zoneId = base.localAvatar.getZoneId()
            if ZoneUtil.isDynamicZone(zoneId) or ZoneUtil.isCogHQZone(zoneId):
                zoneId = 2000 
            npcHood = ZoneUtil.getCanonicalHoodId(zoneId)
            npcZone = hqZone.get(npcHood, 2520)
        
        cost = ToontownGlobals.getTeleportButtonCost(npcHood)
        self.destroyDialog()
        base.cr.playGame.getPlace().setState('stopped')
        
        if base.localAvatar.getTotalMoney() < cost:
            self.dialog = TTDialog.TTDialog(style=TTDialog.Acknowledge, text=TTLocalizer.TeleportButtonNoMoney % cost, command=self.destroyDialog)
        else:
            self.dialog = TTDialog.TTDialog(style=TTDialog.YesNo, text=TTLocalizer.TeleportButtonConfirm % cost, command=lambda value: self.teleportToShopConfirm(npcZone, npcHood, cost, value))

        self.dialog.show()
    
    def teleportToShopConfirm(self, npcZone, npcHood, cost, value):
        self.destroyDialog()

        if value > 0:
            base.cr.buildingQueryMgr.d_isSuit(npcZone, lambda isSuit: self.teleportToShopCallback(npcZone, npcHood, cost, isSuit))
    
    def teleportToShopCallback(self, npcZone, npcHood, cost, flag):
        if flag:
            base.cr.playGame.getPlace().setState('stopped')
            self.dialog = TTDialog.TTDialog(style=TTDialog.Acknowledge, text=TTLocalizer.TeleportButtonTakenOver, command=self.destroyDialog)
            self.dialog.show()
            return
        
        base.localAvatar.takeMoney(cost)
        base.cr.playGame.getPlace().requestTeleport(npcHood, npcZone, base.localAvatar.defaultShard, -1)

    def fitGeometry(self, geom, fFlip = 0, dimension = 0.8):
        p1 = Point3()
        p2 = Point3()
        geom.calcTightBounds(p1, p2)
        if fFlip:
            t = p1[0]
            p1.setX(-p2[0])
            p2.setX(-t)
        d = p2 - p1
        biggest = max(d[0], d[2])
        s = dimension / biggest
        mid = (p1 + d / 2.0) * s
        geomXform = hidden.attachNewNode('geomXform')
        for child in geom.getChildren():
            child.reparentTo(geomXform)

        geomXform.setPosHprScale(-mid[0], -mid[1] + 1, -mid[2], 180, 0, 0, s, s, s)
        geomXform.reparentTo(geom)

    def clear(self):
        self['image_color'] = Vec4(*self.colors['white'])
        self.headline['text'] = ''
        self.headline['text_fg'] = self.normalTextColor
        self.questInfo['text'] = ''
        self.questInfo['text_fg'] = self.normalTextColor
        self.rewardText['text'] = ''
        self.auxText['text'] = ''
        self.auxText['text_fg'] = self.normalTextColor
        self.lPictureFrame.hide()
        self.rPictureFrame.hide()
        self.questProgress.hide()
        self.teleportButton.hide()
        self.destroyDialog()
        if hasattr(self, 'chooseButton'):
            self.chooseButton.destroy()
            del self.chooseButton
        if hasattr(self, 'deleteButton'):
            self.deleteButton.destroy()
            del self.deleteButton
        self.ignore(self.confirmDeleteButtonEvent)
        if hasattr(self, 'confirmDeleteButton'):
            self.confirmDeleteButton.cleanup()
            del self.confirmDeleteButton
        if self.laffMeter != None:
            self.laffMeter.reparentTo(hidden)
            self.laffMeter.destroy()
            self.laffMeter = None
        return

    def showChoicePoster(self, questId, fromNpcId, toNpcId, rewardId, callback):
        self.update((questId,
         fromNpcId,
         toNpcId,
         rewardId,
         0))
        quest = Quests.getQuest(questId)
        self.rewardText.show()
        self.rewardText.setZ(-0.205)
        self.questProgress.hide()
        if not hasattr(self, 'chooseButton'):
            guiButton = loader.loadModel('phase_3/models/gui/quit_button')
            self.chooseButton = DirectButton(parent=self.questFrame, relief=None, image=(guiButton.find('**/QuitBtn_UP'), guiButton.find('**/QuitBtn_DN'), guiButton.find('**/QuitBtn_RLVR')), image_scale=(0.7, 1, 1), text=TTLocalizer.QuestPageChoose, text_scale=0.06, text_pos=(0, -0.02), pos=(0.273, 0, 0.185), scale=0.65)
            guiButton.removeNode()
        npcZone = NPCToons.getNPCZone(toNpcId)
        hoodId = ZoneUtil.getCanonicalHoodId(npcZone)
        self.chooseButton['command'] = callback
        self.chooseButton['extraArgs'] = [questId]
        self.unbind(DGG.WITHIN)
        self.unbind(DGG.WITHOUT)
        if not quest.getType() == Quests.TrackChoiceQuest:
            self.questInfo.setZ(-0.0625)
        return

    def update(self, questDesc):
        questId, fromNpcId, toNpcId, rewardId, toonProgress = questDesc
        quest = Quests.getQuest(questId)
        self.teleportButton['command'] = self.teleportToShop
        self.teleportButton['extraArgs'] = [toNpcId]
        if quest == None:
            self.notify.warning('Tried to display poster for unknown quest %s' % questId)
            return
        if rewardId == Quests.NA:
            finalReward = Quests.getFinalRewardId(questId, fAll=1)
            transformedReward = Quests.transformReward(finalReward, base.localAvatar)
            reward = Quests.getReward(transformedReward)
        else:
            reward = Quests.getReward(rewardId)
        if reward and questId not in Quests.NoRewardTierZeroQuests:
            rewardString = reward.getPosterString()
        else:
            rewardString = ''
        self.rewardText['text'] = rewardString
        self.fitLabel(self.rewardText)
        if self._deleteCallback:
            self.showDeleteButton(questDesc)
        else:
            self.hideDeleteButton()
        if self.laffMeter:
            self.laffMeter.destroy()
        fComplete = quest.getCompletionStatus(base.localAvatar, questDesc) == Quests.COMPLETE

        if toNpcId == Quests.ToonHQ:
            toNpcName = TTLocalizer.QuestPosterHQOfficer
            toNpcBuildingName = TTLocalizer.QuestPosterHQBuildingName
            toNpcStreetName = TTLocalizer.QuestPosterHQStreetName
            toNpcLocationName = TTLocalizer.QuestPosterHQLocationName
        elif toNpcId == Quests.ToonTailor:
            toNpcName = TTLocalizer.QuestPosterTailor
            toNpcBuildingName = TTLocalizer.QuestPosterTailorBuildingName
            toNpcStreetName = TTLocalizer.QuestPosterTailorStreetName
            toNpcLocationName = TTLocalizer.QuestPosterTailorLocationName
        else:
            toNpcName = NPCToons.getNPCName(toNpcId)
            toNpcZone = NPCToons.getNPCZone(toNpcId)
            toNpcHoodId = ZoneUtil.getCanonicalHoodId(toNpcZone)
            toNpcLocationName = base.cr.hoodMgr.getFullnameFromId(toNpcHoodId)
            toNpcBuildingName = NPCToons.getBuildingTitle(toNpcZone)
            toNpcBranchId = ZoneUtil.getBranchZone(toNpcZone)
            toNpcStreetName = ZoneUtil.getStreetName(toNpcBranchId)
        lPos = Vec3(0, 0, 0.13)
        lIconGeom = None
        lIconGeomScale = 1
        rIconGeom = None
        rIconGeomScale = 1
        infoText = ''
        infoZ = TTLocalizer.QPinfoZ
        auxText = None
        auxTextPos = Vec3(0, 0, 0.12)
        headlineString = quest.getHeadlineString()
        objectiveStrings = quest.getObjectiveStrings()
        captions = map(string.capwords, quest.getObjectiveStrings())
        imageColor = Vec4(*self.colors['white'])
        self.teleportButton.hide()
        
        if (fComplete or quest.getType() in (Quests.DeliverGagQuest, Quests.DeliverItemQuest, Quests.VisitQuest, Quests.TrackChoiceQuest)):
            self.teleportButton.show()
            self.teleportButton.setPos(0.3, 0, -0.15)
        
        if isinstance(quest, Quests.TexturedQuest) and quest.hasFrame():
            frame = quest.getFrame()
            frameBgColor = frame[1]
            lIconGeom = frame[0]
            lIconGeomScale = 0.13
            if not fComplete:
                infoText = quest.getLocationName()
                if infoText == '':
                    infoText = TTLocalizer.QuestPosterAnywhere
        elif quest.getType() == Quests.DeliverGagQuest or quest.getType() == Quests.DeliverItemQuest:
            frameBgColor = 'red'
            if quest.getType() == Quests.DeliverGagQuest:
                invModel = loader.loadModel('phase_3.5/models/gui/inventory_icons')
                track, item = quest.getGagType()
                lIconGeom = invModel.find('**/' + AvPropsNew[track][item])
                invModel.removeNode()
            else:
                bookModel = loader.loadModel('phase_3.5/models/gui/stickerbook_gui')
                lIconGeom = bookModel.find('**/package')
                lIconGeomScale = 0.12
                bookModel.removeNode()
            if not fComplete:
                captions.append(toNpcName)
                auxText = TTLocalizer.QuestPosterAuxTo
                auxTextPos.setZ(0.12)
                lPos.setX(-0.18)
                infoText = TTLocalizer.QuestPageDestination % (toNpcBuildingName, toNpcStreetName, toNpcLocationName)
                rIconGeom = self.createNpcToonHead(toNpcId)
                rIconGeomScale = IMAGE_SCALE_SMALL
        elif quest.getType() == Quests.RecoverItemQuest:
            frameBgColor = 'green'
            bookModel = loader.loadModel('phase_3.5/models/gui/stickerbook_gui')
            lIconGeom = bookModel.find('**/package')
            lIconGeomScale = 0.12
            bookModel.removeNode()
            if not fComplete:
                rIconGeomScale = IMAGE_SCALE_SMALL
                holder = quest.getHolder()
                holderType = quest.getHolderType()
                if holder == Quests.Any:
                    cogIcons = loader.loadModel('phase_3/models/gui/cog_icons')
                    rIconGeom = cogIcons.find('**/cog')
                    cogIcons.removeNode()
                    lPos.setX(-0.18)
                    auxText = TTLocalizer.QuestPosterAuxFrom
                elif holder == Quests.AnyFish:
                    headlineString = TTLocalizer.QuestPosterFishing
                    auxText = TTLocalizer.QuestPosterAuxFor
                    auxTextPos.setX(-0.18)
                    captions = captions[:1]
                else:
                    if holderType == 'track':
                        cogIcons = loader.loadModel('phase_3/models/gui/cog_icons')
                        if holder in SuitDNA.suitDeptModelPaths:
                            icon = cogIcons.find(SuitDNA.suitDeptModelPaths[holder])
                        rIconGeom = icon.copyTo(hidden)
                        rIconGeom.setColor(Suit.Suit.medallionColors[holder])
                        rIconGeomScale = 0.12
                        cogIcons.removeNode()
                    elif holderType == 'level':
                        cogIcons = loader.loadModel('phase_3/models/gui/cog_icons')
                        rIconGeom = cogIcons.find('**/cog')
                        rIconGeomScale = IMAGE_SCALE_SMALL
                        cogIcons.removeNode()
                    else:
                        rIconGeom = self.createSuitHead(holder)
                    lPos.setX(-0.18)
                    auxText = TTLocalizer.QuestPosterAuxFrom
                infoText = quest.getLocationName()
                if infoText == '':
                    infoText = TTLocalizer.QuestPosterAnywhere
        elif quest.getType() == Quests.VisitQuest:
            frameBgColor = 'brown'
            captions[0] = '%s' % toNpcName
            lIconGeom = self.createNpcToonHead(toNpcId)
            lIconGeomScale = IMAGE_SCALE_SMALL
            if not fComplete:
                infoText = TTLocalizer.QuestPageDestination % (toNpcBuildingName, toNpcStreetName, toNpcLocationName)
        elif quest.getType() == Quests.TrackChoiceQuest:
            frameBgColor = 'green'
            invModel = loader.loadModel('phase_3.5/models/gui/inventory_icons')

            track1, track2 = quest.getChoices()
            lIconGeom = invModel.find('**/' + AvPropsNew[track1][1])

            if not fComplete:
                auxText = TTLocalizer.QuestPosterAuxOr
                lPos.setX(-0.18)
                rIconGeom = invModel.find('**/' + AvPropsNew[track2][1])

                infoText = TTLocalizer.QuestPageNameAndDestination % (toNpcName,
                 toNpcBuildingName,
                 toNpcStreetName,
                 toNpcLocationName)
                infoZ = -0.02
            invModel.removeNode()
        elif quest.getType() == Quests.BuildingQuest:
            frameBgColor = 'blue'
            track = quest.getBuildingTrack()
            numFloors = quest.getNumFloors()
            if track == 'c':
                lIconGeom = loader.loadModel('phase_4/models/modules/suit_landmark_corp')
            elif track == 'l':
                lIconGeom = loader.loadModel('phase_4/models/modules/suit_landmark_legal')
            elif track == 'm':
                lIconGeom = loader.loadModel('phase_4/models/modules/suit_landmark_money')
            elif track == 's':
                lIconGeom = loader.loadModel('phase_4/models/modules/suit_landmark_sales')
            else:
                bookModel = loader.loadModel('phase_3.5/models/gui/stickerbook_gui')
                lIconGeom = bookModel.find('**/COG_building')
                bookModel.removeNode()
            if lIconGeom and track != Quests.Any:
                self.loadElevator(lIconGeom, numFloors)
                lIconGeom.setH(180)
                self.fitGeometry(lIconGeom, fFlip=0)
                lIconGeomScale = IMAGE_SCALE_SMALL
            else:
                lIconGeomScale = 0.13
            if not fComplete:
                infoText = quest.getLocationName()
                if infoText == '':
                    infoText = TTLocalizer.QuestPosterAnywhere
        elif quest.getType() == Quests.FactoryQuest:
            frameBgColor = 'blue'
            bookModel = loader.loadModel('phase_3.5/models/gui/stickerbook_gui')
            lIconGeom = bookModel.find('**/factoryIcon2')
            bookModel.removeNode()
            lIconGeomScale = 0.13
            if not fComplete:
                infoText = quest.getLocationName()
                if infoText == '':
                    infoText = TTLocalizer.QuestPosterAnywhere
        elif quest.getType() == Quests.MintQuest:
            frameBgColor = 'blue'
            bookModel = loader.loadModel('phase_3.5/models/gui/stickerbook_gui')
            lIconGeom = bookModel.find('**/CashBotMint')
            bookModel.removeNode()
            lIconGeomScale = 0.13
            if not fComplete:
                infoText = quest.getLocationName()
                if infoText == '':
                    infoText = TTLocalizer.QuestPosterAnywhere
        elif quest.getType() == Quests.CogPartQuest:
            frameBgColor = 'green'
            bookModel = loader.loadModel('phase_3.5/models/gui/stickerbook_gui')
            lIconGeom = bookModel.find('**/CogArmIcon2')
            bookModel.removeNode()
            lIconGeomScale = 0.13
            if not fComplete:
                infoText = quest.getLocationName()
                if infoText == '':
                    infoText = TTLocalizer.QuestPosterAnywhere
        elif quest.getType() == Quests.ForemanQuest or quest.getType() == Quests.SupervisorQuest:
            frameBgColor = 'blue'
            bookModel = loader.loadModel('phase_3.5/models/gui/stickerbook_gui')
            lIconGeom = bookModel.find('**/skelecog5')
            bookModel.removeNode()
            lIconGeomScale = 0.13
            if not fComplete:
                infoText = quest.getLocationName()
                if infoText == '':
                    infoText = TTLocalizer.QuestPosterAnywhere
        elif quest.getType() == Quests.RescueQuest:
            frameBgColor = 'blue'
            lIconGeom = self.createNpcToonHead(random.choice(NPCToons.HQnpcFriends.keys()))
            lIconGeomScale = 0.13
            infoText = quest.getLocationName().strip()
        elif quest.getType() == Quests.FriendQuest:
            frameBgColor = 'brown'
            gui = loader.loadModel('phase_3.5/models/gui/friendslist_gui')
            lIconGeom = gui.find('**/FriendsBox_Closed')
            lIconGeomScale = 0.45
            gui.removeNode()
            infoText = TTLocalizer.QuestPosterAnywhere
        elif quest.getType() == Quests.TrolleyQuest:
            frameBgColor = 'lightBlue'
            gui = loader.loadModel('phase_3.5/models/gui/stickerbook_gui')
            lIconGeom = gui.find('**/trolley')
            lIconGeomScale = 0.13
            gui.removeNode()
            infoText = TTLocalizer.QuestPosterPlayground
        elif quest.getType() == Quests.MailboxQuest:
            frameBgColor = 'lightBlue'
            bookModel = loader.loadModel('phase_3.5/models/gui/stickerbook_gui')
            lIconGeom = bookModel.find('**/package')
            lIconGeomScale = 0.12
            bookModel.removeNode()
            infoText = TTLocalizer.QuestPosterAtHome
        elif quest.getType() == Quests.PhoneQuest:
            frameBgColor = 'lightBlue'
            bookModel = loader.loadModel('phase_3.5/models/gui/stickerbook_gui')
            lIconGeom = bookModel.find('**/clarabelleCow')
            lIconGeomScale = 0.12
            bookModel.removeNode()
            infoText = TTLocalizer.QuestPosterOnPhone
        else:
            frameBgColor = 'blue'
            if quest.getType() == Quests.CogTrackQuest:
                dept = quest.getCogTrack()
                cogIcons = loader.loadModel('phase_3/models/gui/cog_icons')
                lIconGeomScale = 0.13
                if dept in SuitDNA.suitDeptModelPaths:
                    icon = cogIcons.find(SuitDNA.suitDeptModelPaths[dept])
                lIconGeom = icon.copyTo(hidden)
                lIconGeom.setColor(Suit.Suit.medallionColors[dept])
                cogIcons.removeNode()
            elif quest.getType() == Quests.CogQuest:
                if quest.getCogType() != Quests.Any:
                    lIconGeom = self.createSuitHead(quest.getCogType())
                    lIconGeomScale = IMAGE_SCALE_SMALL
                else:
                    cogIcons = loader.loadModel('phase_3/models/gui/cog_icons')
                    lIconGeom = cogIcons.find('**/cog')
                    lIconGeomScale = IMAGE_SCALE_SMALL
                    cogIcons.removeNode()
            elif quest.getType() == Quests.CogLevelQuest:
                cogIcons = loader.loadModel('phase_3/models/gui/cog_icons')
                lIconGeom = cogIcons.find('**/cog')
                lIconGeomScale = IMAGE_SCALE_SMALL
                cogIcons.removeNode()
            elif quest.getType() == Quests.SkelecogTrackQuest:
                dept = quest.getCogTrack()
                cogIcons = loader.loadModel('phase_3/models/gui/cog_icons')
                lIconGeomScale = 0.13
                if dept in SuitDNA.suitDeptModelPaths:
                    icon = cogIcons.find(SuitDNA.suitDeptModelPaths[dept])
                lIconGeom = icon.copyTo(hidden)
                lIconGeom.setColor(Suit.Suit.medallionColors[dept])
                cogIcons.removeNode()
            elif quest.getType() == Quests.SkelecogQuest:
                cogIcons = loader.loadModel('phase_3.5/models/gui/stickerbook_gui')
                lIconGeom = cogIcons.find('**/skelecog5')
                lIconGeomScale = IMAGE_SCALE_SMALL
                cogIcons.removeNode()
            elif quest.getType() == Quests.SkelecogLevelQuest:
                cogIcons = loader.loadModel('phase_3.5/models/gui/stickerbook_gui')
                lIconGeom = cogIcons.find('**/skelecog5')
                lIconGeomScale = IMAGE_SCALE_SMALL
                cogIcons.removeNode()
            elif quest.getType() == Quests.SkeleReviveQuest:
                cogIcons = loader.loadModel('phase_3.5/models/gui/stickerbook_gui')
                lIconGeom = cogIcons.find('**/skelecog5')
                lIconGeomScale = IMAGE_SCALE_SMALL
                cogIcons.removeNode()
            if not fComplete:
                infoText = quest.getLocationName()
                if infoText == '':
                    infoText = TTLocalizer.QuestPosterAnywhere
        if fComplete:
            textColor = (0, 0.3, 0, 1)
            imageColor = Vec4(*self.colors['lightGreen'])
            lPos.setX(-0.18)
            rIconGeom = self.createNpcToonHead(toNpcId)
            rIconGeomScale = IMAGE_SCALE_SMALL
            captions = captions[:1]
            captions.append(toNpcName)
            auxText = TTLocalizer.QuestPosterAuxReturnTo
            headlineString = TTLocalizer.QuestPosterComplete
            infoText = TTLocalizer.QuestPageDestination % (toNpcBuildingName, toNpcStreetName, toNpcLocationName)
            if self.laffMeter != None:
                self.laffMeter.reparentTo(hidden)
                self.laffMeter.destroy()
                self.laffMeter = None
        else:
            textColor = self.normalTextColor
        self.show()
        self['image_color'] = imageColor
        self.headline['text_fg'] = textColor
        self.headline['text'] = headlineString
        self.fitLabel(self.headline)
        self.lPictureFrame.show()
        self.lPictureFrame.setPos(lPos)
        self.lPictureFrame['text_scale'] = TEXT_SCALE
        if lPos[0] != 0:
            self.lPictureFrame['text_scale'] = 0.0325
        self.lPictureFrame['text'] = captions[0]
        self.lPictureFrame['image_color'] = Vec4(*self.colors[frameBgColor])
        if len(captions) > 1:
            self.rPictureFrame.show()
            self.rPictureFrame['text'] = captions[1]
            self.rPictureFrame['text_scale'] = 0.0325
            self.rPictureFrame['image_color'] = Vec4(*self.colors[frameBgColor])
        else:
            self.rPictureFrame.hide()
        self._deleteGeoms()
        self.lQuestIcon['geom'] = lIconGeom
        self.lQuestIcon['geom_pos'] = (0, 10, 0)
        if lIconGeom:
            try:
                self.lQuestIcon['geom_scale'] = lIconGeomScale
            except: pass
            try:
                self.lQuestIcon['geom_pos'] = Point3(lIconGeomPos[0], lIconGeomPos[1], lIconGeomPos[2])
            except: pass
            try:
                self.lQuestIcon['geom_hpr'] = Point3(lIconGeomHpr[0], lIconGeomHpr[1], lIconGeomHpr[2])
            except: pass
        if self.laffMeter != None:
            self.laffMeter.reparentTo(self.lQuestIcon)
        self.rQuestIcon['geom'] = rIconGeom
        self.rQuestIcon['geom_pos'] = (0, 10, 0)
        if rIconGeom:
            self.rQuestIcon['geom_scale'] = rIconGeomScale
        if auxText:
            self.auxText.show()
            self.auxText['text'] = auxText
            self.auxText.setPos(auxTextPos)
        else:
            self.auxText.hide()
        self.bind(DGG.WITHIN, self.mouseEnterPoster)
        self.bind(DGG.WITHOUT, self.mouseExitPoster)
        numQuestItems = quest.getNumQuestItems()
        if fComplete or numQuestItems <= 1:
            self.questProgress.hide()
            if not quest.getType() == Quests.TrackChoiceQuest:
                infoZ = -0.075
        else:
            self.questProgress.show()
            self.questProgress['value'] = toonProgress & pow(2, 16) - 1
            self.questProgress['range'] = numQuestItems
            self.questProgress['text'] = quest.getProgressString(base.localAvatar, questDesc)
        self.questInfo['text'] = infoText
        self.questInfo.setZ(infoZ)
        self.fitLabel(self.questInfo)
        return

    def unbindMouseEnter(self):
        self.unbind(DGG.WITHIN)

    def showDeleteButton(self, questDesc):
        self.hideDeleteButton()
        trashcanGui = loader.loadModel('phase_3/models/gui/trashcan_gui')
        self.deleteButton = DirectButton(parent=self.questFrame, image=(trashcanGui.find('**/TrashCan_CLSD'), trashcanGui.find('**/TrashCan_OPEN'), trashcanGui.find('**/TrashCan_RLVR')), text=('', TTLocalizer.QuestPosterDeleteBtn, TTLocalizer.QuestPosterDeleteBtn), text_fg=(1, 1, 1, 1), text_shadow=(0, 0, 0, 1), text_scale=0.18, text_pos=(0, -0.12), relief=None, pos=(0.3, 0, 0.145), scale=0.3, command=self.onPressedDeleteButton, extraArgs=[questDesc])
        trashcanGui.removeNode()
        return

    def hideDeleteButton(self):
        if hasattr(self, 'deleteButton'):
            self.deleteButton.destroy()
            del self.deleteButton

    def setDeleteCallback(self, callback):
        self._deleteCallback = callback

    def onPressedDeleteButton(self, questDesc):
        self.deleteButton['state'] = DGG.DISABLED
        self.accept(self.confirmDeleteButtonEvent, self.confirmedDeleteButton)
        self.confirmDeleteButton = TTDialog.TTGlobalDialog(doneEvent=self.confirmDeleteButtonEvent, message=TTLocalizer.QuestPosterConfirmDelete, style=TTDialog.YesNo, okButtonText=TTLocalizer.QuestPosterDialogYes, cancelButtonText=TTLocalizer.QuestPosterDialogNo)
        self.confirmDeleteButton.quest = questDesc
        self.confirmDeleteButton.doneStatus = ''
        self.confirmDeleteButton.show()

    def confirmedDeleteButton(self):
        questDesc = self.confirmDeleteButton.quest
        self.ignore(self.confirmDeleteButtonEvent)
        if self.confirmDeleteButton.doneStatus == 'ok':
            if self._deleteCallback:
                self._deleteCallback(questDesc)
        else:
            self.deleteButton['state'] = DGG.NORMAL
        self.confirmDeleteButton.cleanup()
        del self.confirmDeleteButton

    def fitLabel(self, label, lineNo = 0):
        text = label['text']
        label['text_scale'] = TEXT_SCALE
        label['text_wordwrap'] = TEXT_WORDWRAP
        if len(text) > 0:
            lines = text.split('\n')
            lineWidth = label.component('text0').textNode.calcWidth(lines[lineNo])
            if lineWidth > 0:
                textScale = POSTER_WIDTH / lineWidth
                label['text_scale'] = min(TEXT_SCALE, textScale)
                label['text_wordwrap'] = max(TEXT_WORDWRAP, lineWidth + 0.05)
