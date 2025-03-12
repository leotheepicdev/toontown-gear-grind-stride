from panda3d.core import Lens, TextNode, Vec4
from direct.directnotify.DirectNotifyGlobal import directNotify
from direct.gui.DirectGui import *
from direct.showbase import PythonUtil
from direct.task import Task
import DisplaySettingsDialog
import ShtikerPage
from toontown.speedchat import SCColorScheme
from toontown.speedchat import SCStaticTextTerminal
from toontown.speedchat import SpeedChat
from toontown.base import TTLocalizer, ToontownGlobals
from toontown.toon import Toon
from toontown.gui import TTDialog
import KeybindDialog

speedChatStyles = (
    (
        2000,
        (200 / 255.0, 60 / 255.0, 229 / 255.0),
        (200 / 255.0, 135 / 255.0, 255 / 255.0),
        (220 / 255.0, 195 / 255.0, 229 / 255.0)
    ),
    (
        2012,
        (142 / 255.0, 151 / 255.0, 230 / 255.0),
        (173 / 255.0, 180 / 255.0, 237 / 255.0),
        (220 / 255.0, 195 / 255.0, 229 / 255.0)
    ),
    (
        2001,
        (0 / 255.0, 0 / 255.0, 255 / 255.0),
        (140 / 255.0, 150 / 255.0, 235 / 255.0),
        (201 / 255.0, 215 / 255.0, 255 / 255.0)
    ),
    (
        2010,
        (0 / 255.0, 119 / 255.0, 190 / 255.0),
        (53 / 255.0, 180 / 255.0, 255 / 255.0),
        (201 / 255.0, 215 / 255.0, 255 / 255.0)
    ),
    (
        2014,
        (0 / 255.0, 64 / 255.0, 128 / 255.0),
        (0 / 255.0, 64 / 255.0, 128 / 255.0),
        (201 / 255.0, 215 / 255.0, 255 / 255.0)
    ),
    (
        2002,
        (90 / 255.0, 175 / 255.0, 225 / 255.0),
        (120 / 255.0, 215 / 255.0, 255 / 255.0),
        (208 / 255.0, 230 / 255.0, 250 / 255.0)
    ),
    (
        2003,
        (130 / 255.0, 235 / 255.0, 235 / 255.0),
        (120 / 255.0, 225 / 255.0, 225 / 255.0),
        (234 / 255.0, 255 / 255.0, 255 / 255.0)
    ),
    (
        2004,
        (0 / 255.0, 200 / 255.0, 70 / 255.0),
        (0 / 255.0, 200 / 255.0, 80 / 255.0),
        (204 / 255.0, 255 / 255.0, 204 / 255.0)
    ),
    (
        2015,
        (13 / 255.0, 255 / 255.0, 100 / 255.0),
        (64 / 255.0, 255 / 255.0, 131 / 255.0),
        (204 / 255.0, 255 / 255.0, 204 / 255.0)
    ),
    (
        2005,
        (235 / 255.0, 230 / 255.0, 0 / 255.0),
        (255 / 255.0, 250 / 255.0, 100 / 255.0),
        (255 / 255.0, 250 / 255.0, 204 / 255.0)
    ),
    (
        2006,
        (255 / 255.0, 153 / 255.0, 0 / 255.0),
        (229 / 255.0, 147 / 255.0, 0 / 255.0),
        (255 / 255.0, 234 / 255.0, 204 / 255.0)
    ),
    (
        2011,
        (255 / 255.0, 177 / 255.0, 62 / 255.0),
        (255 / 255.0, 200 / 255.0, 117 / 255.0),
        (255 / 255.0, 234 / 255.0, 204 / 255.0)
    ),
    (
        2007,
        (255 / 255.0, 0 / 255.0, 50 / 255.0),
        (229 / 255.0, 0 / 255.0, 50 / 255.0),
        (255 / 255.0, 204 / 255.0, 204 / 255.0)
    ),
    (
        2013,
        (130 / 255.0, 0 / 255.0, 26 / 255.0),
        (179 / 255.0, 0 / 255.0, 50 / 255.0),
        (255 / 255.0, 204 / 255.0, 204 / 255.0)
    ),
    (
        2016,
        (176 / 255.0, 35 / 255.0, 0 / 255.0),
        (240 / 255.0, 48 / 255.0, 0 / 255.0),
        (255 / 255.0, 204 / 255.0, 204 / 255.0)
    ),
    (
        2008,
        (255 / 255.0, 153 / 255.0, 193 / 255.0),
        (240 / 255.0, 157 / 255.0, 192 / 255.0),
        (255 / 255.0, 215 / 255.0, 238 / 255.0)
    ),
    (
        2009,
        (170 / 255.0, 120 / 255.0, 20 / 255.0),
        (165 / 255.0, 120 / 255.0, 50 / 255.0),
        (210 / 255.0, 200 / 255.0, 180 / 255.0)
    )
)
PageMode = PythonUtil.Enum('Options, Extra')


class OptionsPage(ShtikerPage.ShtikerPage):
    notify = directNotify.newCategory('OptionsPage')

    def __init__(self):
        ShtikerPage.ShtikerPage.__init__(self)
        self.optionsTabPage = None
        self.extraOptionsTabPage = None
        self.title = None
        self.leftArrow = None
        self.rightArrow = None
        self.page = 0

    def load(self):
        ShtikerPage.ShtikerPage.load(self)

        self.optionsTabPage = OptionsTabPage(self)
        self.optionsTabPage.hide()
        self.extraOptionsTabPage = ExtraOptionsTabPage(self)
        self.extraOptionsTabPage.hide()

        self.title = DirectLabel(
            parent=self, relief=None, text=TTLocalizer.OptionsPageTitle,
            text_scale=0.12, pos=(0, 0, 0.61))

        gui = loader.loadModel('phase_3/models/props/arrow.bam')
        normalColor = (1, 0.98, 0.15, 1)
        clickColor = (0.8, 0.8, 0, 1)
        rolloverColor = (0.15, 0.82, 1.0, 1)
        disabledColor = (1, 0.98, 0.15, 0.4)
        imageScale = (0.2, 0.2, 0.2)
        leftArrowPos = (-0.35, 0, 0.625)
        rightArrowPos = (0.35, 0, 0.625)
        self.leftArrow = DirectButton(parent=self, relief=None, image_scale=imageScale, image=gui, image_color=normalColor, image1_color=clickColor, image2_color=rolloverColor, image3_color=disabledColor,
                                       command=self.setPage, extraArgs=[0], pos=leftArrowPos, hpr=(0, 0, -180))
        self.rightArrow = DirectButton(parent=self, relief=None, image_scale=imageScale, image=gui, image_color=normalColor, image1_color=clickColor, image2_color=rolloverColor, image3_color=disabledColor,
                                       command=self.setPage, extraArgs=[1], pos=rightArrowPos)
        gui.removeNode()

    def enter(self):
        self.setPage(-1)

        ShtikerPage.ShtikerPage.enter(self)

    def exit(self):
        self.optionsTabPage.exit()
        self.extraOptionsTabPage.exit()
        
        ShtikerPage.ShtikerPage.exit(self)

    def unload(self):
        if self.optionsTabPage is not None:
            self.optionsTabPage.unload()
            self.optionsTabPage = None

        if self.title is not None:
            self.title.destroy()
            self.title = None

        if self.leftArrow is not None:
            self.leftArrow.destroy()
            self.leftArrow = None
        
        if self.rightArrow is not None:
            self.rightArrow.destroy()
            self.rightArrow = None

        ShtikerPage.ShtikerPage.unload(self)

    def setPage(self, direction):
        messenger.send('wakeup')
        self.title['text'] = TTLocalizer.OptionsPageTitle
        if direction == -1:
            self.page = 0
        elif direction == 0:
            self.page -= 1
        elif direction == 1:
            self.page += 1
        if self.page == 0:
            self.leftArrow['state'] = DGG.DISABLED
            self.optionsTabPage.enter()
            self.rightArrow['state'] = DGG.NORMAL
            self.extraOptionsTabPage.exit()
        elif self.page == 1:
            self.title['text'] = TTLocalizer.OptionsPageTitle
            self.leftArrow['state'] = DGG.NORMAL
            self.optionsTabPage.exit()
            self.rightArrow['state'] = DGG.DISABLED
            self.extraOptionsTabPage.enter()
        else:
            self.notify.info('Got unknown option page number: %s' % self.page)		
                      
class OptionsTabPage(DirectFrame):
    notify = directNotify.newCategory('OptionsTabPage')
    DisplaySettingsTaskName = 'save-display-settings'
    DisplaySettingsDelay = 60
    ChangeDisplaySettings = base.config.GetBool('change-display-settings', 1)
    ChangeDisplayAPI = base.config.GetBool('change-display-api', 0)

    def __init__(self, parent = aspect2d):
        self.parent = parent
        self.currentSizeIndex = None

        DirectFrame.__init__(self, parent=self.parent, relief=None, pos=(0.0, 0.0, 0.0), scale=(1.0, 1.0, 1.0))

        self.load()

    def destroy(self):
        self.parent = None

        DirectFrame.destroy(self)

    def load(self):
        self.displaySettings = None
        self.displaySettingsChanged = 0
        self.displaySettingsSize = (None, None)
        self.displaySettingsFullscreen = None
        self.displaySettingsApi = None
        self.displaySettingsApiChanged = 0
        guiButton = loader.loadModel('phase_3/models/gui/quit_button')
        gui = loader.loadModel('phase_3.5/models/gui/friendslist_gui')
        circleModel = loader.loadModel('phase_3/models/gui/tt_m_gui_mat_nameShop')
        titleHeight = 0.61
        textStartHeight = 0.45
        textRowHeight = 0.145
        leftMargin = -0.72
        buttonbase_xcoord = 0.35
        buttonbase_ycoord = 0.45
        button_image_scale = (0.7, 1, 1)
        button_textpos = (0, -0.02)
        options_text_scale = 0.052
        disabled_arrow_color = Vec4(0.6, 0.6, 0.6, 1.0)
        self.speed_chat_scale = 0.055
        self.Music_Label = DirectLabel(parent=self, relief=None, text=TTLocalizer.OptionsPageMusic, text_align=TextNode.ALeft, text_scale=options_text_scale, pos=(leftMargin, 0, textStartHeight))
        self.SoundFX_Label = DirectLabel(parent=self, relief=None, text=TTLocalizer.OptionsPageSFX, text_align=TextNode.ALeft, text_scale=options_text_scale, text_wordwrap=16, pos=(leftMargin, 0, textStartHeight - textRowHeight))
        self.Friends_Label = DirectLabel(parent=self, relief=None, text='', text_align=TextNode.ALeft, text_scale=options_text_scale, text_wordwrap=16, pos=(leftMargin, 0, textStartHeight - 3 * textRowHeight))
        self.Whispers_Label = DirectLabel(parent=self, relief=None, text='', text_align=TextNode.ALeft, text_scale=options_text_scale, text_wordwrap=16, pos=(leftMargin, 0, textStartHeight - 4 * textRowHeight))
        self.DisplaySettings_Label = DirectLabel(parent=self, relief=None, text='', text_align=TextNode.ALeft, text_scale=options_text_scale, text_wordwrap=10, pos=(leftMargin, 0, textStartHeight - 5 * textRowHeight))
        self.SpeedChatStyle_Label = DirectLabel(parent=self, relief=None, text=TTLocalizer.OptionsPageSpeedChatStyleLabel, text_align=TextNode.ALeft, text_scale=options_text_scale, text_wordwrap=10, pos=(leftMargin, 0, textStartHeight - 6 * textRowHeight))
        self.ToonChatSounds_Label = DirectLabel(parent=self, relief=None, text='', text_align=TextNode.ALeft, text_scale=options_text_scale, text_wordwrap=15, pos=(leftMargin, 0, textStartHeight - 2 * textRowHeight + 0.025))
        self.ToonChatSounds_Label.setScale(0.9)
        self.Music_toggleSlider = DirectSlider(parent=self, pos=(buttonbase_xcoord, 0.0, buttonbase_ycoord),
                                               value=settings['musicVol']*100, pageSize=5, range=(0, 100), command=self.__doMusicLevel,
                                               thumb_geom=(circleModel.find('**/tt_t_gui_mat_namePanelCircle')), thumb_relief=None, thumb_geom_scale=2)
        self.Music_toggleSlider.setScale(0.25)
        self.SoundFX_toggleSlider = DirectSlider(parent=self, pos=(buttonbase_xcoord, 0.0, buttonbase_ycoord - textRowHeight),
                                               value=settings['sfxVol']*100, pageSize=5, range=(0, 100), command=self.__doSfxLevel,
                                               thumb_geom=(circleModel.find('**/tt_t_gui_mat_namePanelCircle')), thumb_relief=None, thumb_geom_scale=2)
        self.SoundFX_toggleSlider.setScale(0.25)
        self.Friends_toggleButton = DirectButton(parent=self, relief=None, image=(guiButton.find('**/QuitBtn_UP'), guiButton.find('**/QuitBtn_DN'), guiButton.find('**/QuitBtn_RLVR')), image_scale=button_image_scale, text='', text_scale=options_text_scale, text_pos=button_textpos, pos=(buttonbase_xcoord, 0.0, buttonbase_ycoord - textRowHeight * 3), command=self.__doToggleAcceptFriends)
        self.Whispers_toggleButton = DirectButton(parent=self, relief=None, image=(guiButton.find('**/QuitBtn_UP'), guiButton.find('**/QuitBtn_DN'), guiButton.find('**/QuitBtn_RLVR')), image_scale=button_image_scale, text='', text_scale=options_text_scale, text_pos=button_textpos, pos=(buttonbase_xcoord, 0.0, buttonbase_ycoord - textRowHeight * 4), command=self.__doToggleAcceptWhispers)
        self.DisplaySettingsButton = DirectButton(parent=self, relief=None, image=(guiButton.find('**/QuitBtn_UP'), guiButton.find('**/QuitBtn_DN'), guiButton.find('**/QuitBtn_RLVR')), image3_color=Vec4(0.5, 0.5, 0.5, 0.5), image_scale=button_image_scale, text=TTLocalizer.OptionsPageChange, text3_fg=(0.5, 0.5, 0.5, 0.75), text_scale=options_text_scale, text_pos=button_textpos, pos=(buttonbase_xcoord, 0.0, buttonbase_ycoord - textRowHeight * 5), command=self.__doDisplaySettings)
        self.speedChatStyleLeftArrow = DirectButton(parent=self, relief=None, image=(gui.find('**/Horiz_Arrow_UP'),
         gui.find('**/Horiz_Arrow_DN'),
         gui.find('**/Horiz_Arrow_Rllvr'),
         gui.find('**/Horiz_Arrow_UP')), image3_color=Vec4(1, 1, 1, 0.5), scale=(-1.0, 1.0, 1.0), pos=(0.25, 0, buttonbase_ycoord - textRowHeight * 6), command=self.__doSpeedChatStyleLeft)
        self.speedChatStyleRightArrow = DirectButton(parent=self, relief=None, image=(gui.find('**/Horiz_Arrow_UP'),
         gui.find('**/Horiz_Arrow_DN'),
         gui.find('**/Horiz_Arrow_Rllvr'),
         gui.find('**/Horiz_Arrow_UP')), image3_color=Vec4(1, 1, 1, 0.5), pos=(0.65, 0, buttonbase_ycoord - textRowHeight * 6), command=self.__doSpeedChatStyleRight)
        self.ToonChatSounds_toggleButton = DirectButton(parent=self, relief=None, image=(guiButton.find('**/QuitBtn_UP'),
         guiButton.find('**/QuitBtn_DN'),
         guiButton.find('**/QuitBtn_RLVR'),
         guiButton.find('**/QuitBtn_UP')), image3_color=Vec4(0.5, 0.5, 0.5, 0.5), image_scale=button_image_scale, text='', text3_fg=(0.5, 0.5, 0.5, 0.75), text_scale=options_text_scale, text_pos=button_textpos, pos=(buttonbase_xcoord, 0.0, buttonbase_ycoord - textRowHeight * 2 + 0.025), command=self.__doToggleToonChatSounds)
        self.ToonChatSounds_toggleButton.setScale(0.8)
        self.speedChatStyleText = SpeedChat.SpeedChat(name='OptionsPageStyleText', structure=[2000], backgroundModelName='phase_3/models/gui/ChatPanel', guiModelName='phase_3.5/models/gui/speedChatGui')
        self.speedChatStyleText.setScale(self.speed_chat_scale)
        self.speedChatStyleText.setPos(0.37, 0, buttonbase_ycoord - textRowHeight * 6 + 0.03)
        self.speedChatStyleText.reparentTo(self, DGG.FOREGROUND_SORT_INDEX)
        self.exitButton = DirectButton(parent=self, relief=None, image=(guiButton.find('**/QuitBtn_UP'), guiButton.find('**/QuitBtn_DN'), guiButton.find('**/QuitBtn_RLVR')), image_scale=1.15, text=TTLocalizer.OptionsPageExitToontown, text_scale=options_text_scale, text_pos=button_textpos, textMayChange=0, pos=(0.45, 0, -0.6), command=self.__handleExitShowWithConfirm)
        guiButton.removeNode()
        gui.removeNode()

    def enter(self):
        self.show()
        taskMgr.remove(self.DisplaySettingsTaskName)
        self.settingsChanged = 0
        self.__setAcceptFriendsButton()
        self.__setAcceptWhispersButton()
        self.__setDisplaySettings()
        self.__setToonChatSoundsButton()
        self.speedChatStyleText.enter()
        self.speedChatStyleIndex = base.localAvatar.getSpeedChatStyleIndex()
        self.updateSpeedChatStyle()
        if self.parent.book.safeMode:
            self.exitButton.hide()
        else:
            self.exitButton.show()

    def exit(self):
        self.ignore('confirmDone')
        self.hide()
        self.speedChatStyleText.exit()
        if self.displaySettingsChanged:
            taskMgr.doMethodLater(self.DisplaySettingsDelay, self.writeDisplaySettings, self.DisplaySettingsTaskName)

    def unload(self):
        self.writeDisplaySettings()
        taskMgr.remove(self.DisplaySettingsTaskName)
        if self.displaySettings != None:
            self.ignore(self.displaySettings.doneEvent)
            self.displaySettings.unload()
        self.displaySettings = None
        self.exitButton.destroy()
        self.Music_toggleSlider.destroy()
        self.SoundFX_toggleSlider.destroy()
        self.Friends_toggleButton.destroy()
        self.Whispers_toggleButton.destroy()
        self.DisplaySettingsButton.destroy()
        self.speedChatStyleLeftArrow.destroy()
        self.speedChatStyleRightArrow.destroy()
        del self.exitButton
        del self.SoundFX_Label
        del self.Music_Label
        del self.Friends_Label
        del self.Whispers_Label
        del self.SpeedChatStyle_Label
        del self.SoundFX_toggleSlider
        del self.Music_toggleSlider
        del self.Friends_toggleButton
        del self.Whispers_toggleButton
        del self.speedChatStyleLeftArrow
        del self.speedChatStyleRightArrow
        self.speedChatStyleText.exit()
        self.speedChatStyleText.destroy()
        del self.speedChatStyleText
        self.currentSizeIndex = None

    def __doMusicLevel(self):
        vol = self.Music_toggleSlider['value']
        vol = float(vol) / 100
        settings['musicVol'] = vol
        base.musicManager.setVolume(vol)
        base.musicActive = vol > 0.0

    def __doSfxLevel(self):
        vol = self.SoundFX_toggleSlider['value']
        vol = float(vol) / 100
        settings['sfxVol'] = vol
        for sfm in base.sfxManagerList:
            sfm.setVolume(vol)
        base.sfxActive = vol > 0.0
        self.__setToonChatSoundsButton()

    def __doToggleToonChatSounds(self):
        messenger.send('wakeup')
        if base.toonChatSounds:
            base.toonChatSounds = 0
            settings['toonChatSounds'] = False
        else:
            base.toonChatSounds = 1
            settings['toonChatSounds'] = True
        self.settingsChanged = 1
        self.__setToonChatSoundsButton()

    def __setToonChatSoundsButton(self):
        if base.toonChatSounds:
            self.ToonChatSounds_Label['text'] = TTLocalizer.OptionsPageToonChatSoundsOnLabel
            self.ToonChatSounds_toggleButton['text'] = TTLocalizer.OptionsPageToggleOff
        else:
            self.ToonChatSounds_Label['text'] = TTLocalizer.OptionsPageToonChatSoundsOffLabel
            self.ToonChatSounds_toggleButton['text'] = TTLocalizer.OptionsPageToggleOn
        if base.sfxActive:
            self.ToonChatSounds_Label.setColorScale(1.0, 1.0, 1.0, 1.0)
            self.ToonChatSounds_toggleButton['state'] = DGG.NORMAL
        else:
            self.ToonChatSounds_Label.setColorScale(0.5, 0.5, 0.5, 0.5)
            self.ToonChatSounds_toggleButton['state'] = DGG.DISABLED

    def __doToggleAcceptFriends(self):
        messenger.send('wakeup')
        acceptingNewFriends = settings.get('acceptingNewFriends', {})
        if base.localAvatar.acceptingNewFriends:
            base.localAvatar.acceptingNewFriends = 0
            acceptingNewFriends[str(base.localAvatar.doId)] = False
        else:
            base.localAvatar.acceptingNewFriends = 1
            acceptingNewFriends[str(base.localAvatar.doId)] = True
        settings['acceptingNewFriends'] = acceptingNewFriends
        self.settingsChanged = 1
        self.__setAcceptFriendsButton()

    def __doToggleAcceptWhispers(self):
        messenger.send('wakeup')
        acceptingNonFriendWhispers = settings.get('acceptingNonFriendWhispers', {})
        if base.localAvatar.acceptingNonFriendWhispers:
            base.localAvatar.acceptingNonFriendWhispers = 0
            acceptingNonFriendWhispers[str(base.localAvatar.doId)] = False
        else:
            base.localAvatar.acceptingNonFriendWhispers = 1
            acceptingNonFriendWhispers[str(base.localAvatar.doId)] = True
        settings['acceptingNonFriendWhispers'] = acceptingNonFriendWhispers
        self.settingsChanged = 1
        self.__setAcceptWhispersButton()

    def __setAcceptFriendsButton(self):
        if base.localAvatar.acceptingNewFriends:
            self.Friends_Label['text'] = TTLocalizer.OptionsPageFriendsEnabledLabel
            self.Friends_toggleButton['text'] = TTLocalizer.OptionsPageToggleOff
        else:
            self.Friends_Label['text'] = TTLocalizer.OptionsPageFriendsDisabledLabel
            self.Friends_toggleButton['text'] = TTLocalizer.OptionsPageToggleOn

    def __setAcceptWhispersButton(self):
        if base.localAvatar.acceptingNonFriendWhispers:
            self.Whispers_Label['text'] = TTLocalizer.OptionsPageWhisperEnabledLabel
            self.Whispers_toggleButton['text'] = TTLocalizer.OptionsPageToggleOff
        else:
            self.Whispers_Label['text'] = TTLocalizer.OptionsPageWhisperDisabledLabel
            self.Whispers_toggleButton['text'] = TTLocalizer.OptionsPageToggleOn

    def __doDisplaySettings(self):
        if self.displaySettings == None:
            self.displaySettings = DisplaySettingsDialog.DisplaySettingsDialog()
            self.displaySettings.load()
            self.accept(self.displaySettings.doneEvent, self.__doneDisplaySettings)
        self.displaySettings.enter(self.ChangeDisplaySettings, self.ChangeDisplayAPI)

    def __doneDisplaySettings(self, anyChanged, apiChanged):
        if anyChanged:
            self.__setDisplaySettings()
            properties = base.win.getProperties()
            self.displaySettingsChanged = 1
            self.displaySettingsSize = (properties.getXSize(), properties.getYSize())
            self.displaySettingsFullscreen = properties.getFullscreen()
            self.displaySettingsApi = base.pipe.getInterfaceName()
            self.displaySettingsApiChanged = apiChanged

    def __setDisplaySettings(self):
        properties = base.win.getProperties()
        if properties.getFullscreen():
            screensize = '%s x %s' % (properties.getXSize(), properties.getYSize())
        else:
            screensize = TTLocalizer.OptionsPageDisplayWindowed
        api = base.pipe.getInterfaceName()
        settings = {'screensize': screensize,
         'api': api}
        if self.ChangeDisplayAPI:
            OptionsPage.notify.debug('change display settings...')
            text = TTLocalizer.OptionsPageDisplaySettings % settings
        else:
            OptionsPage.notify.debug('no change display settings...')
            text = TTLocalizer.OptionsPageDisplaySettingsNoApi % settings
        self.DisplaySettings_Label['text'] = text

    def __doSpeedChatStyleLeft(self):
        if self.speedChatStyleIndex > 0:
            self.speedChatStyleIndex = self.speedChatStyleIndex - 1
            self.updateSpeedChatStyle()

    def __doSpeedChatStyleRight(self):
        if self.speedChatStyleIndex < len(speedChatStyles) - 1:
            self.speedChatStyleIndex = self.speedChatStyleIndex + 1
            self.updateSpeedChatStyle()

    def updateSpeedChatStyle(self):
        nameKey, arrowColor, rolloverColor, frameColor = speedChatStyles[self.speedChatStyleIndex]
        newSCColorScheme = SCColorScheme.SCColorScheme(arrowColor=arrowColor, rolloverColor=rolloverColor, frameColor=frameColor)
        self.speedChatStyleText.setColorScheme(newSCColorScheme)
        self.speedChatStyleText.clearMenu()
        colorName = SCStaticTextTerminal.SCStaticTextTerminal(nameKey)
        self.speedChatStyleText.append(colorName)
        self.speedChatStyleText.finalize()
        self.speedChatStyleText.setPos(0.445 - self.speedChatStyleText.getWidth() * self.speed_chat_scale / 2, 0, self.speedChatStyleText.getPos()[2])
        if self.speedChatStyleIndex > 0:
            self.speedChatStyleLeftArrow['state'] = DGG.NORMAL
        else:
            self.speedChatStyleLeftArrow['state'] = DGG.DISABLED
        if self.speedChatStyleIndex < len(speedChatStyles) - 1:
            self.speedChatStyleRightArrow['state'] = DGG.NORMAL
        else:
            self.speedChatStyleRightArrow['state'] = DGG.DISABLED
        base.localAvatar.b_setSpeedChatStyleIndex(self.speedChatStyleIndex)

    def writeDisplaySettings(self, task=None):
        if not self.displaySettingsChanged:
            return
        taskMgr.remove(self.DisplaySettingsTaskName)
        settings['res'] = (self.displaySettingsSize[0], self.displaySettingsSize[1])
        settings['fullscreen'] = self.displaySettingsFullscreen
        return Task.done

    def __handleExitShowWithConfirm(self):
        self.confirm = TTDialog.TTGlobalDialog(doneEvent='confirmDone', message=TTLocalizer.OptionsPageExitConfirm, style=TTDialog.TwoChoice)
        self.confirm.show()
        self.parent.doneStatus = {'mode': 'exit',
         'exitTo': 'closeShard'}
        self.accept('confirmDone', self.__handleConfirm)

    def __handleConfirm(self):
        status = self.confirm.doneStatus
        self.ignore('confirmDone')
        self.confirm.cleanup()
        del self.confirm
        if status == 'ok':
            base.cr._userLoggingOut = True
            messenger.send(self.parent.doneEvent)

class ExtraOptionsTabPage(DirectFrame):
    notify = directNotify.newCategory('ExtraOptionsTabPage')

    def __init__(self, parent = aspect2d):
        self.parent = parent
        self.currentSizeIndex = None
        self.keybindDialog = None
        DirectFrame.__init__(self, parent=self.parent, relief=None, pos=(0.0, 0.0, 0.0), scale=(1.0, 1.0, 1.0))

        self.load()

    def destroy(self):
        self.parent = None
        DirectFrame.destroy(self)

    def load(self):
        guiButton = loader.loadModel('phase_3/models/gui/quit_button')
        circleModel = loader.loadModel('phase_3/models/gui/tt_m_gui_mat_nameShop')
        titleHeight = 0.61
        textStartHeight = 0.45
        textRowHeight = 0.145
        leftMargin = -0.72
        buttonbase_xcoord = 0.35
        buttonbase_ycoord = 0.45
        button_image_scale = (0.7, 1, 1)
        button_textpos = (0, -0.02)
        options_text_scale = 0.052
        disabled_arrow_color = Vec4(0.6, 0.6, 0.6, 1.0)
        button_image = (guiButton.find('**/QuitBtn_UP'), guiButton.find('**/QuitBtn_DN'), guiButton.find('**/QuitBtn_RLVR'))
        self.speed_chat_scale = 0.055
        self.fov_label = DirectLabel(parent=self, relief=None, text=TTLocalizer.FieldOfViewLabel, text_align=TextNode.ALeft, text_scale=options_text_scale, text_wordwrap=16, pos=(leftMargin, 0, textStartHeight))
        self.cogInterface_label = DirectLabel(parent=self, relief=None, text='', text_align=TextNode.ALeft, text_scale=options_text_scale, text_wordwrap=16, pos=(leftMargin, 0, textStartHeight - textRowHeight))
        self.fpsMeter_label = DirectLabel(parent=self, relief=None, text='', text_align=TextNode.ALeft, text_scale=options_text_scale, text_wordwrap=16, pos=(leftMargin, 0, textStartHeight - 2 * textRowHeight))
        self.teleport_label = DirectLabel(parent=self, relief=None, text='', text_align=TextNode.ALeft, text_scale=options_text_scale, text_wordwrap=16, pos=(leftMargin, 0, textStartHeight - 3 * textRowHeight))
        self.ttoAspectRatio_label = DirectLabel(parent=self, relief=None, text=TTLocalizer.TTOAspectRatioLabel, text_align=TextNode.ALeft, text_scale=options_text_scale, text_wordwrap=16, pos=(leftMargin, 0, textStartHeight - 4 * textRowHeight))
        self.keybindLabel = DirectLabel(parent=self, relief=None, text=TTLocalizer.KeybindLabel, text_align=TextNode.ALeft, text_scale=options_text_scale, text_wordwrap=16, pos=(leftMargin, 0, textStartHeight - 5 * textRowHeight))
        self.discordPresence_label = DirectLabel(parent=self, relief=None, text=TTLocalizer.discordPresenceLabel, text_align=TextNode.ALeft, text_scale=options_text_scale, text_wordwrap=16, pos=(leftMargin, 0, textStartHeight - 6 * textRowHeight))
        self.trolleyPosition_label = self.discordPresence_label = DirectLabel(parent=self, relief=None, text=TTLocalizer.TrolleyPositionLabel, text_align=TextNode.ALeft, text_scale=options_text_scale, text_wordwrap=16, pos=(leftMargin, 0, textStartHeight - 7 * textRowHeight))
        self.fov_slider = DirectSlider(parent=self, pos=(buttonbase_xcoord, 0.0, buttonbase_ycoord),
                                               value=settings['fov'], pageSize=5, range=(ToontownGlobals.DefaultCameraFov, ToontownGlobals.MaxCameraFov), command=self.__doFov,
                                               thumb_geom=(circleModel.find('**/tt_t_gui_mat_namePanelCircle')), thumb_relief=None, thumb_geom_scale=2)
        self.fov_slider.setScale(0.25)
        self.cogInterface_toggleButton = DirectButton(parent=self, relief=None, image=button_image, image_scale=button_image_scale, text='', text_scale=options_text_scale, text_pos=button_textpos, pos=(buttonbase_xcoord, 0.0, buttonbase_ycoord - textRowHeight), command=self.__doToggleCogInterface)
        self.fpsMeter_toggleButton = DirectButton(parent=self, relief=None, image=button_image, image_scale=button_image_scale, text='', text_scale=options_text_scale, text_pos=button_textpos, pos=(buttonbase_xcoord, 0.0, buttonbase_ycoord - 2 * textRowHeight), command=self.__doToggleFpsMeter)
        self.teleport_toggleButton = DirectButton(parent=self, relief=None, image=button_image, image_scale=button_image_scale, text='', text_scale=options_text_scale, text_pos=button_textpos, pos=(buttonbase_xcoord, 0.0, buttonbase_ycoord - 3 * textRowHeight), command=self.__doToggleTeleport)
        self.ttoAspectRatio_toggleButton = DirectButton(parent=self, relief=None, image=button_image, image_scale=button_image_scale, text='', text_scale=options_text_scale, text_pos=button_textpos, pos=(buttonbase_xcoord, 0.0, buttonbase_ycoord - 4 * textRowHeight), command=self.__doToggleAspectRatio)
        self.keybind_updateButton = DirectButton(parent=self, relief=None, image=button_image, image_scale=button_image_scale, text=TTLocalizer.KeybindButton, text_scale=options_text_scale, text_pos=button_textpos, pos=(buttonbase_xcoord, 0.0, buttonbase_ycoord - 5 * textRowHeight), command=self.__doUpdateKeybinds)      
        self.discordPresence_toggleButton = DirectButton(parent=self, relief=None, image=button_image, image_scale=button_image_scale, text='', text_scale=options_text_scale, text_pos=button_textpos, pos=(buttonbase_xcoord, 0.0, buttonbase_ycoord - 6 * textRowHeight), command=self.__doToggleDiscordPresence)
        self.trolleyPosition_toggleButton = DirectButton(parent=self, relief=None, image=button_image, image_scale=button_image_scale, text='', text_scale=options_text_scale, text_pos=button_textpos, pos=(buttonbase_xcoord, 0.0, buttonbase_ycoord - 7 * textRowHeight), command=self.__doToggleTrolleyPosition)       
        guiButton.removeNode()
        circleModel.removeNode()

    def enter(self):
        self.show()
        self.settingsChanged = 0
        self.__setCogInterfaceButton()
        self.__setFpsMeterButton()
        self.__setTeleportButton()
        self.__setAspectRatioButton()
        self.__setDiscordPresenceButton()
        self.__setTrolleyPositionButton()

    def exit(self):
        self.ignoreAll()
        self.hide()

    def unload(self):
        self.fov_label.destroy()
        del self.fov_label
        self.fov_slider.destroy()
        del self.fov_slider
        self.cogInterface_label.destroy()
        del self.cogInterface_label
        self.cogInterface_toggleButton.destroy()
        del self.cogInterface_label
        self.fpsMeter_label.destroy()
        del self.fpsMeter_label
        self.fpsMeter_toggleButton.destroy()
        del self.fpsMeter_toggleButton
        self.teleport_label.destroy()
        del self.teleport_label
        self.teleport_toggleButton.destroy()
        del self.teleport_toggleButton
        self.ttoAspectRatio_label.destroy()
        del self.ttoAspectRatio_label
        self.ttoAspectRatio_toggleButton.destroy()
        del self.ttoAspectRatio_toggleButton
        self.discordPresence_label.destroy()
        del self.discordPresence_label
        self.discordPresence_toggleButton.destroy()
        del self.discordPresence_toggleButton
        self.trolleyPosition_label.destroy()
        del self.trolleyPosition_label
        self.trolleyPosition_toggleButton.destroy()
        del self.trolleyPosition_toggleButton
        self.keybindLabel.destroy()
        del self.keybindLabel
        self.keybind_updateButton.destroy()
        del self.keybind_updateButton

    def __doFov(self):
        fov = self.fov_slider['value']
        settings['fov'] = fov
        base.camLens.setMinFov(fov/(4./3.))

    def __doToggleCogInterface(self):
        messenger.send('wakeup')
        settings['cogInterface'] = not settings['cogInterface']
        self.settingsChanged = 1
        self.__setCogInterfaceButton()

    def __setCogInterfaceButton(self):
        self.cogInterface_label['text'] = TTLocalizer.CogInterfaceLabelOn if settings['cogInterface'] else TTLocalizer.CogInterfaceLabelOff
        self.cogInterface_toggleButton['text'] = TTLocalizer.OptionsPageToggleOff if settings['cogInterface'] else TTLocalizer.OptionsPageToggleOn

    def __doToggleFpsMeter(self):
        messenger.send('wakeup')
        settings['fpsMeter'] = not settings['fpsMeter']
        base.setFrameRateMeter(settings['fpsMeter'])
        self.settingsChanged = 1
        self.__setFpsMeterButton()

    def __setFpsMeterButton(self):
        self.fpsMeter_label['text'] = TTLocalizer.FpsMeterLabelOn if settings['fpsMeter'] else TTLocalizer.FpsMeterLabelOff
        self.fpsMeter_toggleButton['text'] = TTLocalizer.OptionsPageToggleOff if settings['fpsMeter'] else TTLocalizer.OptionsPageToggleOn
    
    def __doToggleTeleport(self):
        messenger.send('wakeup')
        acceptingTeleport = settings.get('acceptingTeleport', {})
        if base.localAvatar.acceptingTeleport:
            base.localAvatar.acceptingTeleport = 0
            acceptingTeleport[str(base.localAvatar.doId)] = False
        else:
            base.localAvatar.acceptingTeleport  = 1
            acceptingTeleport[str(base.localAvatar.doId)] = True
        settings['acceptingTeleport'] = acceptingTeleport
        self.settingsChanged = 1
        self.__setTeleportButton()
    
    def __setTeleportButton(self):
        self.teleport_label['text'] = TTLocalizer.TeleportLabelOn if base.localAvatar.acceptingTeleport else TTLocalizer.TeleportLabelOff
        self.teleport_toggleButton['text'] = TTLocalizer.OptionsPageToggleOff if base.localAvatar.acceptingTeleport else TTLocalizer.OptionsPageToggleOn

    def __doToggleAspectRatio(self):
        messenger.send('wakeup')
        if not settings['ttoAspectRatio']:
            base.setAspectRatio(ToontownGlobals.TTOAspectRatio)
            settings['ttoAspectRatio'] = True
        elif settings['ttoAspectRatio']:
            base.setAspectRatio(0)
            settings['ttoAspectRatio'] = False
        self.settingsChanged = 1
        self.__setAspectRatioButton()
     
    def __setAspectRatioButton(self):
        self.ttoAspectRatio_toggleButton['text'] = TTLocalizer.OptionsPageToggleOff if settings['ttoAspectRatio'] else TTLocalizer.OptionsPageToggleOn

    def __doUpdateKeybinds(self):
        if not self.keybindDialog:
            self.keybindDialog = KeybindDialog.KeybindDialog()
			
    def __setDiscordPresenceButton(self):
        self.discordPresence_toggleButton['text'] = TTLocalizer.OptionsPageToggleOff if settings['discordPresence'] else TTLocalizer.OptionsPageToggleOn

    def __doToggleDiscordPresence(self):
        if not settings['discordPresence']:
            base.cr.discordPresence.open()
            base.cr.discordPresence.send_general()
            settings['discordPresence'] = True
        elif settings['discordPresence']:
            base.cr.discordPresence.pop_activity()
            base.cr.discordPresence.close()
            settings['discordPresence'] = False
        self.__setDiscordPresenceButton()
        
    def __setTrolleyPositionButton(self):
        if base.localAvatar.getTrolleyPosition() == ToontownGlobals.TROLLEY_POSITION_SIT:  
            self.trolleyPosition_toggleButton['text'] = TTLocalizer.TrolleyPositionSit
        else:
            self.trolleyPosition_toggleButton['text'] = TTLocalizer.TrolleyPositionStand
            
    def __doToggleTrolleyPosition(self):
        messenger.send('wakeup')
        if base.localAvatar.getTrolleyPosition() == ToontownGlobals.TROLLEY_POSITION_SIT:
            base.localAvatar.updateTrolleyPosition(ToontownGlobals.TROLLEY_POSITION_STAND)
            self.trolleyPosition_toggleButton['text'] = TTLocalizer.TrolleyPositionStand
        else:
            base.localAvatar.updateTrolleyPosition(ToontownGlobals.TROLLEY_POSITION_SIT)
            self.trolleyPosition_toggleButton['text'] = TTLocalizer.TrolleyPositionSit
            
        
