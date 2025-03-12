from otp.otpgui.OTPDialog import *
from toontown.base.TTLocalizer import lOK, lCancel

class TTDialog(OTPDialog):

    def __init__(self, parent = None, style = NoButtons, **kw):
        self.path = 'phase_3/models/gui/dialog_box_buttons_gui'
        OTPDialog.__init__(self, parent, style, **kw)
        self.initialiseoptions(TTDialog)


class TTGlobalDialog(GlobalDialog):

    def __init__(self, message = '', doneEvent = None, style = NoButtons, okButtonText = lOK, cancelButtonText = lCancel, **kw):
        self.path = 'phase_3/models/gui/dialog_box_buttons_gui'
        GlobalDialog.__init__(self, message, doneEvent, style, okButtonText, cancelButtonText, **kw)
        self.initialiseoptions(TTGlobalDialog)
