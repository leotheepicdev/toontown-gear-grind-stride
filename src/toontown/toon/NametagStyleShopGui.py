from direct.gui.DirectGui import DirectButton, DirectLabel, DGG
from direct.task.Task import Task
from toontown.toon import ToonDNA
from toontown.base import ToontownGlobals, TTLocalizer
from lib.nametag import NametagConstants
from . import NametagNPCGlobals
import time

class NametagStyleShopGui:

    def __init__(self):
        self.index = 0
        self.id = time.time()
        self.lastNametagStyle = base.localAvatar.nametagStyle
        self.setupButtons()
        self.bindButtons()
        self.__updateIndex(3)

    def setupButtons(self):
        gui = loader.loadModel('phase_3/models/gui/tt_m_gui_mat_mainGui')
        arrowImage = (gui.find('**/tt_t_gui_mat_shuffleArrowUp'), gui.find('**/tt_t_gui_mat_shuffleArrowDown'))
        buttonImage = (gui.find('**/tt_t_gui_mat_shuffleUp'), gui.find('**/tt_t_gui_mat_shuffleDown'))

        self.title = DirectLabel(aspect2d, relief=None, text=TTLocalizer.NametagStyleGuiTitle,
                     text_fg=(0, 1, 0, 1), text_scale=0.15, text_font=ToontownGlobals.getSignFont(),
                     pos=(0, 0, -0.30), text_shadow=(1, 1, 1, 1))

        self.notice = DirectLabel(aspect2d, relief=None, text='', text_fg=(1, 0, 0, 1), text_scale=0.11,
                      text_font=ToontownGlobals.getSignFont(), pos=(0, 0, -0.45), text_shadow=(1, 1, 1, 1))

        self.style = DirectLabel(aspect2d, relief=None, text='', text_scale=0.11, pos=(0, 0, -0.70))

        self.buyButton = DirectButton(aspect2d, relief=None, image=buttonImage, text=TTLocalizer.NametagGuiBuy,
                         text_font=ToontownGlobals.getInterfaceFont(), text_scale=0.11, text_pos=(0, -0.02),
                         pos=(-0.60, 0, -0.90), text_fg=(1, 1, 1, 1), text_shadow=(0, 0, 0, 1), command=self.__exit, extraArgs=[NametagNPCGlobals.CHANGE])
                         
        self.backButton = DirectButton(aspect2d, relief=None, image=buttonImage, text=TTLocalizer.PartyPlannerPreviousButton,
                          text_font=ToontownGlobals.getInterfaceFont(), text_scale=0.11, text_pos=(0, -0.02),
                          pos=(0, 0, -0.90), text_fg=(1, 1, 1, 1), text_shadow=(0, 0, 0, 1), command=self.__back)

        self.cancelButton = DirectButton(aspect2d, relief=None, image=buttonImage, text=TTLocalizer.lCancel,
                            clickSound=loader.loadSfx('phase_3/audio/sfx/GUI_create_toon_back.ogg'),
                            text_font=ToontownGlobals.getInterfaceFont(), text_scale=0.11, text_pos=(0, -0.02),
                            pos=(0.60, 0, -0.90), text_fg=(1, 1, 1, 1), text_shadow=(0, 0, 0, 1), command=self.__exit, extraArgs=[NametagNPCGlobals.USER_CANCEL])

        self.downArrow = DirectButton(aspect2d, relief=None, image=arrowImage, pos=(-0.60, 0, -0.66))
        self.upArrow = DirectButton(aspect2d, relief=None, image=arrowImage, pos=(0.60, 0, -0.66), scale=-1)

        gui.removeNode()

    def bindButtons(self):
        self.downArrow.bind(DGG.B1PRESS, self.__taskUpdate, extraArgs=[-1])
        self.downArrow.bind(DGG.B1RELEASE, self.__taskDone)
        self.upArrow.bind(DGG.B1PRESS, self.__taskUpdate, extraArgs=[1])
        self.upArrow.bind(DGG.B1RELEASE, self.__taskDone)

    def destroy(self):
        if not hasattr(self, 'title'):
            return

        self.title.destroy()
        self.notice.destroy()
        self.style.destroy()
        self.buyButton.destroy()
        self.backButton.destroy()
        self.cancelButton.destroy()
        self.downArrow.destroy()
        self.upArrow.destroy()
        del self.title
        del self.notice
        del self.style
        del self.buyButton
        del self.cancelButton
        del self.downArrow
        del self.upArrow

        taskMgr.remove('runNametagStyleCounter-%s' % self.id)
        
    def setClientNametagStyle(self, nametagStyle):
        base.localAvatar.setNametagStyle(nametagStyle)

    def __exit(self, state):
        self.destroy()
        self.setClientNametagStyle(self.lastNametagStyle)
        messenger.send('nametagStyleShopDone', [state, self.index if state == NametagNPCGlobals.CHANGE else 0])
        
    def __back(self):
        self.destroy()
        self.setClientNametagStyle(self.lastNametagStyle)
        messenger.send('nametagShopBack')

    def __updateIndex(self, offset):
        self.index += offset
        hitLimit = 0

        if self.index <= 3:
            self.downArrow['state'] = DGG.DISABLED
            hitLimit = 1
        else:
            self.downArrow['state'] = DGG.NORMAL

        if (self.index + 1) >= len(TTLocalizer.NametagFontNames):
            self.upArrow['state'] = DGG.DISABLED
            hitLimit = 1
        else:
            self.upArrow['state'] = DGG.NORMAL
        
        if self.index in base.localAvatar.nametagStyles:
            self.buyButton['state'] = DGG.DISABLED
            self.notice['text'] = TTLocalizer.NametagStyleGuiSameStyle
        else:
            self.buyButton['state'] = DGG.NORMAL
            self.notice['text'] = TTLocalizer.NametagGuiNotice % ToontownGlobals.NametagStyleCost

        self.style['text_font'] = loader.loadFont(TTLocalizer.NametagFonts[self.index], lineHeight=1.0)
        self.style['text'] = TTLocalizer.NametagFontNames[self.index]
        self.style['text_fg'] = NametagConstants.TOON_COLORS[base.localAvatar.nametagColor][0][0]
        self.setClientNametagStyle(self.index)
        return hitLimit

    def __runTask(self, task):
        if task.time - task.prevTime < task.delayTime:
            return Task.cont
        else:
            task.delayTime = max(0.05, task.delayTime * 0.75)
            task.prevTime = task.time
            hitLimit = self.__updateIndex(task.delta)

            return Task.done if hitLimit else Task.cont

    def __taskDone(self, event):
        messenger.send('wakeup')
        taskMgr.remove('runNametagStyleCounter-%s' % self.id)

    def __taskUpdate(self, delta, event):
        messenger.send('wakeup')

        task = Task(self.__runTask)
        task.delayTime = 0.4
        task.prevTime = 0.0
        task.delta = delta
        hitLimit = self.__updateIndex(delta)

        if not hitLimit:
            taskMgr.add(task, 'runNametagStyleCounter-%s' % self.id)