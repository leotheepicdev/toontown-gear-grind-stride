from panda3d.core import Vec4
from otp.otpbase import OTPGlobals
from direct.gui.DirectGui import *
from direct.fsm import FSM
from otp.chat import ChatUtil
from otp.otpbase import OTPLocalizer
from toontown.base import ToontownGlobals
from direct.directnotify import DirectNotifyGlobal

class TTChatInputWhiteList(FSM.FSM, DirectFrame):
    notify = DirectNotifyGlobal.directNotify.newCategory('TTChatInputWhiteList')
    TFToggleKey = base.config.GetString('true-friend-toggle-key', 'alt')
    TFToggleKeyUp = TFToggleKey + '-up'

    def __init__(self, parent = None, **kw):
        FSM.FSM.__init__(self, 'TTChatInputWhiteListFrame')
        DirectFrame.__init__(self, parent=aspect2dp, pos=(0, 0, 0.3), relief=None, image=DGG.getDefaultDialogGeom(), image_scale=(1.6, 1, 1.4), image_pos=(0, 0, -0.05), image_color=OTPGlobals.GlobalDialogColor, borderWidth=(0.01, 0.01))
        optiondefs = {'parent': self,
         'relief': DGG.SUNKEN,
         'scale': 0.05,
         'frameColor': (0.9, 0.9, 0.85, 0.0),
         'pos': (-0.2, 0, 0.11),
         'entryFont': ToontownGlobals.getInterfaceFont(),
         'width': 8.6,
         'numLines': 3,
         'cursorKeys': 0,
         'backgroundFocus': 0,
         'suppressKeys': 0,
         'suppressMouse': 1,
         'command': self.sendChat,
         'focus': 0,
         'text': '',
         'sortOrder': DGG.FOREGROUND_SORT_INDEX}
        self.chatEntry = DirectEntry(**optiondefs)
        self.receiverId = None
        self.whisperId = None
        self.active = 0
        base.ttwl = self
        self.autoOff = 1
        self.prefilter = 0
        self.promoteWhiteList = 1
        self.typeGrabbed = 0
        self.deactivate()
        gui = loader.loadModel('phase_3.5/models/gui/chat_input_gui')
        self.chatFrame = DirectFrame(parent=self, image=gui.find('**/Chat_Bx_FNL'), relief=None, pos=(0.0, 0, 0.0), state=DGG.NORMAL)
        self.chatButton = DirectButton(parent=self.chatFrame, image=(gui.find('**/ChtBx_ChtBtn_UP'), gui.find('**/ChtBx_ChtBtn_DN'), gui.find('**/ChtBx_ChtBtn_RLVR')), pos=(0.182, 0, -0.088), relief=None, text=('', OTPLocalizer.ChatInputNormalSayIt, OTPLocalizer.ChatInputNormalSayIt), text_scale=0.06, text_fg=Vec4(1, 1, 1, 1), text_shadow=Vec4(0, 0, 0, 1), text_pos=(0, -0.09), textMayChange=0, command=self.chatButtonPressed)
        self.cancelButton = DirectButton(parent=self.chatFrame, image=(gui.find('**/CloseBtn_UP'), gui.find('**/CloseBtn_DN'), gui.find('**/CloseBtn_Rllvr')), pos=(-0.151, 0, -0.088), relief=None, text=('', OTPLocalizer.ChatInputNormalCancel, OTPLocalizer.ChatInputNormalCancel), text_scale=0.06, text_fg=Vec4(1, 1, 1, 1), text_shadow=Vec4(0, 0, 0, 1), text_pos=(0, -0.09), textMayChange=0, command=self.cancelButtonPressed)
        self.whisperLabel = DirectLabel(parent=self.chatFrame, pos=(0.02, 0, 0.23), relief=DGG.FLAT, frameColor=(1, 1, 0.5, 1), frameSize=(-0.23,
         0.23,
         -0.07,
         0.05), text=OTPLocalizer.ChatInputNormalWhisper, text_scale=0.04, text_fg=Vec4(0, 0, 0, 1), text_wordwrap=9.5, textMayChange=1)
        self.chatEntry.bind(DGG.TYPE, self.typeCallback)
        self.chatEntry.bind(DGG.ERASE, self.applyFilter)
        self.trueFriendChat = 0
        if base.config.GetBool('whisper-to-nearby-true-friends', 1):
            self.accept(self.TFToggleKey, self.shiftPressed)

    def requestMode(self, mode, *args):
        return self.request(mode, *args)

    def enterOff(self):
        self.deactivate()
        localAvatar.chatMgr.fsm.request('mainMenu')

    def exitOff(self):
        self.activate()

    def activateByData(self, receiverId = None):
        self.receiverId = receiverId
        result = None
        if not self.receiverId:
            result = self.requestMode('AllChat')
        elif self.receiverId:
            self.whisperId = receiverId
            result = self.requestMode('AvatarWhisper')
        return result

    def activate(self):
        self.chatEntry['focus'] = 1
        self.show()
        self.active = 1
        self.chatEntry.guiItem.setAcceptEnabled(True)

    def deactivate(self):
        self.chatEntry.set('')
        self.chatEntry['focus'] = 0
        self.hide()
        self.active = 0

    def isActive(self):
        return self.active

    def sendChat(self, text):
        if self.typeGrabbed:
            return
        if not (len(text) > 0 and text[0] in ['~', '>']):
            text = self.chatEntry.get(plain=True)
        if text:
            self.chatEntry.set('')
            if not base.cr.chatAgent.verifyMessage(text):
                self.hideChatInput()
                return
            if len(text) > 0 and text[0] == '~':
                base.talkAssistant.sendOpenTalk(text)
            else:
                self.sendChatByData(text)
        self.hideChatInput()

    def hideChatInput(self):
        self.hide()
        if self.autoOff:
            self.requestMode('Off')		
        
    def shiftPressed(self):
        self.ignore(self.TFToggleKey)
        self.trueFriendChat = 1
        self.accept(self.TFToggleKeyUp, self.shiftReleased)

    def shiftReleased(self):
        self.ignore(self.TFToggleKeyUp)
        self.trueFriendChat = 0
        self.accept(self.TFToggleKey, self.shiftPressed)

    def handleTypeGrab(self):
        self.ignore('typeEntryGrab')
        self.accept('typeEntryRelease', self.handleTypeRelease)
        self.typeGrabbed = 1

    def handleTypeRelease(self):
        self.ignore('typeEntryRelease')
        self.accept('typeEntryGrab', self.handleTypeGrab)
        self.typeGrabbed = 0

    def typeCallback(self, extraArgs):
        if self.typeGrabbed:
            return
        self.applyFilter(extraArgs)
        if self.isActive():
            return
        messenger.send('wakeup')

    def destroy(self):
        self.chatEntry.destroy()
        self.chatFrame.destroy()
        self.ignoreAll()
        self.chatEntry.unbind(DGG.TYPE)
        self.chatEntry.unbind(DGG.ERASE)
        self.chatEntry.ignoreAll()
        DirectFrame.destroy(self)

    def delete(self):
        self.ignore('arrow_up-up')
        self.ignore('arrow_down-up')

    def sendChatByData(self, text):
        if self.trueFriendChat:
            for friendId in base.localAvatar.friendsList:
                if base.localAvatar.isTrueFriends(friendId):
                    self.sendWhisperByFriend(friendId, text)
        elif self.receiverId:
            base.talkAssistant.sendWhisperTalk(text, self.receiverId)
        else:
            base.talkAssistant.sendOpenTalk(text)

    def sendWhisperByFriend(self, avatarId, text):
        online = 0
        if avatarId in base.cr.doId2do:
            online = 1
        avatarUnderstandable = 0
        av = None
        if avatarId:
            av = base.cr.identifyAvatar(avatarId)
        if av != None:
            avatarUnderstandable = av.isUnderstandable()
        if avatarUnderstandable and online:
            base.talkAssistant.sendWhisperTalk(text, avatarId)

    def chatButtonPressed(self):
        self.sendChat(self.chatEntry.get())

    def cancelButtonPressed(self):
        self.requestMode('Off')
        localAvatar.chatMgr.fsm.request('mainMenu')

    def enterAllChat(self):
        self.chatEntry['focus'] = 1
        self.show()
        self.whisperLabel.hide()

    def exitAllChat(self):
        pass

    def enterAvatarWhisper(self):
        self.tempText = self.chatEntry.get()
        self.activate()
        self.labelWhisper()

    def exitAvatarWhisper(self):
        self.chatEntry.set(self.tempText)
        self.whisperId = None
        self.whisperLabel.hide()

    def labelWhisper(self):
        if self.receiverId:
            self.whisperName = ChatUtil.findAvatarName(self.receiverId)
            self.whisperLabel['text'] = OTPLocalizer.ChatInputWhisperLabel % self.whisperName
            self.whisperLabel.show()
        else:
            self.whisperLabel.hide()

    def applyFilter(self, keyArgs):
        if base.whiteList:
            self.chatEntry.set(base.whiteList.processThroughAll(self.chatEntry.get(plain=True)))
