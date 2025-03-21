from toontown.base.ToontownGlobals import *
from direct.showbase import DirectObject
from direct.directnotify import DirectNotifyGlobal
from toontown.gui import TTDialog
from otp.otpbase import OTPLocalizer
from toontown.gui import ToonHeadDialog
from direct.gui.DirectGui import DGG

class FriendInvitee(ToonHeadDialog.ToonHeadDialog):
    notify = DirectNotifyGlobal.directNotify.newCategory('FriendInvitee')

    def __init__(self, avId, avName, avDNA, context, **kw):
        self.avId = avId
        self.avDNA = avDNA
        self.context = context
        self.avName = avName
        if len(base.localAvatar.friendsList) >= MaxFriends:
            base.cr.friendManager.up_inviteeFriendResponse(3, self.context)
            self.context = None
            text = OTPLocalizer.FriendInviteeTooManyFriends % self.avName
            style = TTDialog.Acknowledge
            buttonTextList = [OTPLocalizer.FriendInviteeOK]
            command = self.__handleOhWell
        else:
            text = OTPLocalizer.FriendInviteeInvitation % self.avName
            style = TTDialog.TwoChoice
            buttonTextList = [OTPLocalizer.FriendInviteeOK, OTPLocalizer.FriendInviteeNo]
            command = self.__handleButton
        optiondefs = (('dialogName', 'FriendInvitee', None),
         ('text', text, None),
         ('style', style, None),
         ('buttonTextList', buttonTextList, None),
         ('command', command, None),
         ('image_color', (1.0, 0.89, 0.77, 1.0), None),
         ('geom_scale', 0.2, None),
         ('geom_pos', (-0.1, 0, -0.025), None),
         ('pad', (0.075, 0.075), None),
         ('topPad', 0, None),
         ('midPad', 0, None),
         ('pos', (0.45, 0, 0.75), None),
         ('scale', 0.75, None))
        self.defineoptions(kw, optiondefs)
        ToonHeadDialog.ToonHeadDialog.__init__(self, self.avDNA)
        self.accept('cancelFriendInvitation', self.__handleCancelFromAbove)
        self.initialiseoptions(FriendInvitee)
        self.show()
        return

    def cleanup(self):
        ToonHeadDialog.ToonHeadDialog.cleanup(self)
        self.ignore('cancelFriendInvitation')
        if self.context != None:
            base.cr.friendManager.up_inviteeFriendResponse(2, self.context)
            self.context = None

    def __handleButton(self, value):
        base.cr.friendManager.up_inviteeFriendResponse(value == DGG.DIALOG_OK, self.context)
        self.context = None
        self.cleanup()
        return

    def __handleOhWell(self, value):
        self.cleanup()

    def __handleCancelFromAbove(self, context = None):
        if context == None or context == self.context:
            self.context = None
            self.cleanup()
        return
