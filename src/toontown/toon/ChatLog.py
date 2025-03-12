from direct.gui.DirectGui import *

class ChatLog(DirectFrame):
    VISIBLE_MSG_COUNT = 5

    def __init__(self):
        DirectFrame.__init__(self, parent=base.a2dTopLeft, relief=None, pos=(0.9, 0, -0.35))
        self.initialiseoptions(ChatLog)
        self.chatlog = DirectScrolledList(parent=self,
            decButton_relief = None,
            incButton_relief = None,
            itemFrame_geom =(loader.loadModel('phase_3.5/models/gui/speedChatGui').find('**/menuBG')),
            itemFrame_relief = None,
            itemFrame_geom_scale = (1, 1, 0.65),
            itemFrame_geom_color = (0, 0.35, 0.55, 0.8),
            items = [],
            numItemsVisible = self.VISIBLE_MSG_COUNT,
            forceHeight = 0.1)
			
    def show(self):
        DirectFrame.show(self)
        self.accept('wheel_up-up', self.scroll, [-1])
        self.accept('wheel_down-up', self.scroll, [1])
		
    def hide(self):
        DirectFrame.hide(self)
        self.ignore('wheel_up-up')
        self.ignore('wheel_down-up')
		
    def log(self, name, msg, color='amber'):
        msg = DirectLabel(relief=None, text='\n\x01%s\x01(%s): %s' % (color, name, msg), text_scale=0.035, text_pos=(0, 0.235), text_wordwrap=22)			
        self.chatlog.addItem(msg)
        self.chatlog.scrollTo(len(self.chatlog['items']) - 1)		
		
    def scroll(self, value):
        index = self.chatlog.getSelectedIndex()
        self.chatlog.scrollTo(index + value)