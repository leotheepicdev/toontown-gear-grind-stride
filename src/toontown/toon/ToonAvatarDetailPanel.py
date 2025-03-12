from panda3d.core import TextEncoder, TextNode, Vec4
from toontown.base.ToontownGlobals import *
from direct.gui.DirectGui import *
from direct.interval.IntervalGlobal import *
from direct.showbase import DirectObject
from direct.fsm import ClassicFSM, State
from direct.directnotify import DirectNotifyGlobal
from direct.task.Task import Task
import DistributedToon
from toontown.friends import FriendInviter
import ToonTeleportPanel
from toontown.base import TTLocalizer, ToontownGlobals
from toontown.hood import ZoneUtil
from toontown.base.ToontownBattleGlobals import Tracks, Levels, getAvPropDamage
import Toon, NPCFriendPanel
globalAvatarDetail = None

def showAvatarDetail(avId, avName):
    global globalAvatarDetail
    if globalAvatarDetail:
        if globalAvatarDetail.avId == avId:
            return
    if globalAvatarDetail != None:
        globalAvatarDetail.cleanup()
        globalAvatarDetail = None
    globalAvatarDetail = ToonAvatarDetailPanel(avId, avName)


def hideAvatarDetail():
    global globalAvatarDetail
    if globalAvatarDetail != None:
        globalAvatarDetail.cleanup()
        globalAvatarDetail = None
    return


def unloadAvatarDetail():
    global globalAvatarDetail
    if globalAvatarDetail != None:
        globalAvatarDetail.cleanup()
        globalAvatarDetail = None
    return


class ToonAvatarDetailPanel(DirectFrame):
    notify = DirectNotifyGlobal.directNotify.newCategory('ToonAvatarDetailPanel')

    def __init__(self, avId, avName, parent = base.a2dTopRight, **kw):
        buttons = loader.loadModel('phase_3/models/gui/dialog_box_buttons_gui')
        gui = loader.loadModel('phase_3.5/models/gui/avatar_panel_gui')
        jarGui = loader.loadModel('phase_3.5/models/gui/jar_gui')
        nameBalloon = loader.loadModel('phase_3/models/props/chatbox_input')
        detailPanel = gui.find('**/avatarInfoPanel')
        textScale = 0.095
        textWrap = 16.4
        optiondefs = (('pos', (-0.79, 0.0, -0.47), None),
         ('scale', 0.5, None),
         ('relief', None, None),
         ('image', detailPanel, None),
         ('image_color', GlobalDialogColor, None),
         ('text', '', None),
         ('text_wordwrap', textWrap, None),
         ('text_scale', textScale, None),
         ('text_pos', (-0.125, 0.775), None))
        self.defineoptions(kw, optiondefs)
        DirectFrame.__init__(self, parent)
        self.dataText = DirectLabel(self, text='', text_scale=0.09, text_align=TextNode.ALeft, text_wordwrap=15, relief=None, pos=(-0.85, 0.0, 0.645))
        self.avId = avId
        self.avName = avName
        self.avatar = None
        self.createdAvatar = None
        self.fsm = ClassicFSM.ClassicFSM('ToonAvatarDetailPanel', [State.State('off', self.enterOff, self.exitOff, ['begin']),
         State.State('begin', self.enterBegin, self.exitBegin, ['query', 'data', 'off']),
         State.State('query', self.enterQuery, self.exitQuery, ['data', 'invalid', 'off']),
         State.State('data', self.enterData, self.exitData, ['off']),
         State.State('invalid', self.enterInvalid, self.exitInvalid, ['off'])], 'off', 'off')
        ToonTeleportPanel.hideTeleportPanel()
        FriendInviter.hideFriendInviter()
        self.bCancel = DirectButton(self, image=(buttons.find('**/CloseBtn_UP'), buttons.find('**/CloseBtn_DN'), buttons.find('**/CloseBtn_Rllvr')), image_scale=1.1, relief=None, text=TTLocalizer.AvatarDetailPanelCancel, text_scale=TTLocalizer.TADPbCancel, text_pos=(0.12, -0.01), pos=TTLocalizer.TADPbCancelPos, scale=2.0, command=self.__handleCancel)
        self.bCancel.hide()
        self.jellybeanButton = DirectButton(self, relief=None, image=jarGui.find('**/Jar'), scale=0.3, pos=(0.4, 0, -0.76), text=('', TTLocalizer.GiftJellybeanTitle, TTLocalizer.GiftJellybeanTitle, ''), text_fg=(1, 1, 0.5, 1), text_shadow=(0, 0, 0, 1), text_scale=0.18, text_pos=(0, -0.4), text_align=TextNode.ACenter, state=DGG.NORMAL, command=self.__toggleJellybeanGui)
        self.jellybeanButton.hide()
        self.jellybeanFrame = DirectFrame(self, relief=None, image=DGG.getDefaultDialogGeom(), image_scale=(1.36, 1, 0.67), image_color=ToontownGlobals.GlobalDialogColor, pos=(0, 0, -1.28))
        self.jellybeanFrame.hide()
        self.amountFrame = DirectFrame(pos=(-0.3, 0, 0), parent=self.jellybeanFrame, relief=None, image=nameBalloon, image_scale=(0.07, 0, 0.05))      
        self.enterText = DirectLabel(parent=self.jellybeanFrame, relief=None, pos=(0, 0, 0.15), text=TTLocalizer.GiftJellybeanEnter, text_fg=(0.44, 0.18, 0.65, 1), text_font=ToontownGlobals.getMinnieFont(), scale=0.06)
        self.amountEntry = DirectEntry(parent=self.amountFrame, relief=None, pos=(0, 0, 0), scale=0.06, width=6, focus=1, cursorKeys=1, command=self.requestGiftToon)
        self.amountJar = DirectLabel(parent=self.jellybeanFrame, relief=None, pos=(-0.58, 0, -0.225), scale=0.4, text=str(base.localAvatar.getTotalMoney()), 
                                     text_scale=0.2, text_fg=(0.95, 0.95, 0, 1), text_shadow=(0, 0, 0, 1), text_pos=(0, -0.1, 0), image=jarGui.find('**/Jar'), text_font=ToontownGlobals.getSignFont())
        self.callback = DirectLabel(parent=self.jellybeanFrame, relief=None, pos=(0, 0, -0.2), text='', text_fg=(0, 0, 0, 0), text_font=ToontownGlobals.getSignFont(), scale=0.08)
        self.callbackSeq = None
        self.initialiseoptions(ToonAvatarDetailPanel)
        self.fsm.enterInitialState()
        self.fsm.request('begin')
        buttons.removeNode()
        gui.removeNode()
        jarGui.removeNode()
        nameBalloon.removeNode()

    def cleanup(self):
        if self.fsm:
            self.fsm.request('off')
            self.fsm = None
            base.cr.cancelAvatarDetailsRequest(self.avatar)
        if self.createdAvatar:
            self.avatar.delete()
            self.createdAvatar = None
        self.destroy()

    def enterOff(self):
        pass

    def exitOff(self):
        pass

    def enterBegin(self):
        myId = base.localAvatar.doId
        self['text'] = self.avName
        if self.avId == myId:
            self.avatar = base.localAvatar
            self.createdAvatar = 0
            self.fsm.request('data')
        else:
            self.fsm.request('query')

    def exitBegin(self):
        pass

    def enterQuery(self):
        self.dataText['text'] = TTLocalizer.AvatarDetailPanelLookup % self.avName
        self.jellybeanButton.hide()
        self.bCancel.show()
        self.avatar = base.cr.doId2do.get(self.avId)
        if self.avatar != None and not self.avatar.ghostMode:
            self.createdAvatar = 0
        else:
            self.avatar = DistributedToon.DistributedToon(base.cr)
            self.createdAvatar = 1
            self.avatar.doId = self.avId
            self.avatar.forceAllowDelayDelete()
        base.cr.getAvatarDetails(self.avatar, self.__handleAvatarDetails, 'DistributedToon')
        return

    def exitQuery(self):
        self.bCancel.hide()

    def enterData(self):
        self.bCancel['text'] = TTLocalizer.AvatarDetailPanelClose
        self.bCancel.show()
        self.__showData()

    def exitData(self):
        self.bCancel.hide()

    def enterInvalid(self):
        self.dataText['text'] = TTLocalizer.AvatarDetailPanelFailedLookup % self.avName

    def exitInvalid(self):
        self.bCancel.hide()

    def __handleCancel(self):
        unloadAvatarDetail()

    def __handleAvatarDetails(self, gotData, avatar, dclass):
        if not self.fsm or avatar != self.avatar:
            self.notify.warning('Ignoring unexpected request for avatar %s' % avatar.doId)
            return
        if gotData:
            self.fsm.request('data')
        else:
            self.fsm.request('invalid')

    def __showData(self):
        av = self.avatar
        online = 1
        if base.cr.isFriend(self.avId):
            online = base.cr.isFriendOnline(self.avId)
        identifier = int(str(self.avId)[1:])

        if online:
            shardName = base.cr.getShardName(av.defaultShard)
            hoodName = base.cr.hoodMgr.getFullnameFromId(av.lastHood)
            text = TTLocalizer.AvatarDetailPanelOnline % {'district': shardName, 'location': hoodName, 'identifier': identifier}
        else:
            text = TTLocalizer.AvatarDetailPanelOffline % {'identifier': identifier}
        self.dataText['text'] = text
        self.jellybeanButton.show()
        self.__addToonModel()
        self.__updateTrackInfo()
        self.__updateTrophyInfo()
        self.__updateLaffInfo()

    def __addToonModel(self):
        toon = Toon.Toon()
        toon.setDNA(self.avatar.style)
        toon.reparentTo(self)
        toon.setPos(0.45, 0, 0.3)
        toon.setH(180)
        toon.setScale(0.11)
        toon.loop('neutral')
        toon.setDepthWrite(True)
        toon.setDepthTest(True)
    
    def __updateLaffInfo(self):
        avatar = self.avatar
        messenger.send('updateLaffMeter', [avatar, avatar.hp, avatar.maxHp])

    def __updateTrackInfo(self):
        xOffset = -0.501814
        xSpacing = 0.1835
        yOffset = 0.1
        ySpacing = -0.115
        inventory = self.avatar.inventory
        self.inventoryFrame = DirectFrame(parent=self, relief=None)
        inventoryModels = loader.loadModel('phase_3.5/models/gui/inventory_gui')
        rolloverFrame = DirectFrame(parent=self.inventoryFrame, relief=None, geom=DGG.getDefaultDialogGeom(), geom_color=(0, 0.5, 1, 1), geom_scale=(0.5, 0.3, 0.2), text_scale=0.05, text_pos=(0, 0.0125), text='', text_fg=(1, 1, 1, 1))
        rolloverFrame.setBin('gui-popup', 0)
        rolloverFrame.hide()
        buttonModel = inventoryModels.find('**/InventoryButtonUp')
        for track in xrange(0, len(Tracks)):
            DirectLabel(parent=self.inventoryFrame, relief=None, text=TextEncoder.upper(TTLocalizer.BattleGlobalTracks[track]), text_scale=TTLocalizer.TADPtrackLabel, text_align=TextNode.ALeft, pos=(-0.9, 0, TTLocalizer.TADtrackLabelPosZ + track * ySpacing))
            if self.avatar.hasTrackAccess(track):
                curExp, nextExp = inventory.getCurAndNextExpValues(track)
                for item in xrange(0, len(Levels[track])):
                    level = Levels[track][item]
                    if curExp >= level:
                        numItems = inventory.numItem(track, item)
                        organic = self.avatar.checkGagBonus(track, item)
                        if numItems == 0:
                            image_color = Vec4(0.5, 0.5, 0.5, 1)
                            geom_color = Vec4(0.2, 0.2, 0.2, 0.5)
                        elif organic:
                            image_color = Vec4(0, 0.8, 0.4, 1)
                            geom_color = None
                        else:
                            image_color = Vec4(0, 0.6, 1, 1)
                            geom_color = None
                        pos = (xOffset + item * xSpacing, 0, yOffset + track * ySpacing)
                        label = DirectLabel(parent=self.inventoryFrame, image=buttonModel, image_scale=(0.92, 1, 1), image_color=image_color, geom=inventory.invModels[track][item], geom_color=geom_color, geom_scale=0.6, relief=None, pos=pos, state=DGG.NORMAL)
                        label.bind(DGG.ENTER, self.showInfo, extraArgs=[rolloverFrame, track, int(getAvPropDamage(track, item, curExp, organic)), numItems, (pos[0] + 0.37, pos[1], pos[2])])
                        label.bind(DGG.EXIT, self.hideInfo, extraArgs=[rolloverFrame])
                    else:
                        break
    
    def showInfo(self, frame, track, damage, numItems, pos, extra):
        frame.setPos(*pos)
        frame.show()
        frame['text'] = TTLocalizer.GagPopup % (self.avatar.inventory.getToonupDmgStr(track, 0), damage, numItems)

    def hideInfo(self, frame, extra):
        frame.hide()

    def __updateTrophyInfo(self):
        if self.createdAvatar:
            return
        if self.avatar.trophyScore >= TrophyStarLevels[2]:
            color = TrophyStarColors[2]
        elif self.avatar.trophyScore >= TrophyStarLevels[1]:
            color = TrophyStarColors[1]
        elif self.avatar.trophyScore >= TrophyStarLevels[0]:
            color = TrophyStarColors[0]
        else:
            color = None
        if color:
            gui = loader.loadModel('phase_3.5/models/gui/avatar_panel_gui')
            star = gui.find('**/avatarStar')
            self.star = DirectLabel(parent=self, image=star, image_color=color, pos=(0.610165, 0, -0.760678), scale=0.9, relief=None)
            gui.removeNode()
    
    def __updateSOSPage(self):
        pass
    
    def __toggleJellybeanGui(self):
        self.jellybeanButton['state'] = DGG.DISABLED
        if self.jellybeanFrame.isHidden():
            if self.callback['text'] != '':
                self.callback['text'] = ''
            self.accept('giftJellybeansResult', self.requestGiftToonResults)
            self.accept(localAvatar.uniqueName('moneyChange'), self.__moneyChange)
            self.accept(localAvatar.uniqueName('bankMoneyChange'), self.__moneyChange)
            self.jellybeanFrame.show()
        else:
            self.ignore('giftJellybeansResult')
            self.ignore(localAvatar.uniqueName('moneyChange'))
            self.ignore(localAvatar.uniqueName('bankMoneyChange'))
            self.jellybeanFrame.hide()
        self.jellybeanButton['state'] = DGG.NORMAL
        
    def requestGiftToon(self, input=None):
        if input == '':
            return
        try:
            amount = int(input)
        except ValueError:
            amount = 0
            
        if amount <= 0 or amount > base.localAvatar.getTotalMoney():
            self.callback['text_fg'] = (1, 0, 0, 1)
            self.callback['text'] = TTLocalizer.GiftJellybeanInvalidJellybeans
            if self.callbackSeq:
                self.callbackSeq.finish()
                self.callbackSeq = None
            self.callbackSeq = Sequence(LerpColorScaleInterval(self.callback, 1.33, Vec4(1, 1, 1, 0), startColorScale=Vec4(1, 1, 1, 1), blendType='easeIn'), 
                                    LerpColorScaleInterval(self.callback, 1.33, Vec4(1, 1, 1, 1), startColorScale=Vec4(1, 1, 1, 0), blendType='easeIn'),
                                    LerpColorScaleInterval(self.callback, 1.33, Vec4(1, 1, 1, 0), startColorScale=Vec4(1, 1, 1, 1), blendType='easeIn'),
                                    Func(self.finishCallback))
            self.callbackSeq.start()
        else:
            self.callback['text_fg'] = (1, 0.5, 0, 1)
            self.callback['text'] = TTLocalizer.GiftJellybeanGifting
            base.localAvatar.giftJellybeans(self.avId, amount)
            
            
    def requestGiftToonResults(self, callback):
        if callback == 0:
            self.callback['text_fg'] = (0, 1, 0, 1)
            self.callback['text'] = TTLocalizer.GiftJellybeanSuccess
        elif callback == 1:
            self.callback['text_fg'] = (1, 0, 0, 1)
            self.callback['text'] = TTLocalizer.GiftJellybeanFullMailbox
        if self.callbackSeq:
            self.callbackSeq.finish()
            self.callbackSeq = None
        self.callbackSeq = Sequence(LerpColorScaleInterval(self.callback, 1.33, Vec4(1, 1, 1, 0), startColorScale=Vec4(1, 1, 1, 1), blendType='easeIn'), 
                                    LerpColorScaleInterval(self.callback, 1.33, Vec4(1, 1, 1, 1), startColorScale=Vec4(1, 1, 1, 0), blendType='easeIn'),
                                    LerpColorScaleInterval(self.callback, 1.33, Vec4(1, 1, 1, 0), startColorScale=Vec4(1, 1, 1, 1), blendType='easeIn'),
                                    Func(self.finishCallback))
        self.callbackSeq.start()
                                        
    def finishCallback(self):
        if self.callback:
            self.callback['text_fg'] = (0, 0, 0, 0)
        
    def __moneyChange(self, money):
        self.amountJar['text'] = str(base.localAvatar.getTotalMoney())
         
        