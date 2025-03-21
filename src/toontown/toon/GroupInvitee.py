from toontown.base.ToontownGlobals import *
from direct.showbase import DirectObject
from direct.directnotify import DirectNotifyGlobal
from toontown.gui import TTDialog
from otp.otpbase import OTPLocalizer
from toontown.gui import ToonHeadDialog
from direct.gui.DirectGui import DGG
from toontown.base import TTLocalizer

class GroupInvitee(ToonHeadDialog.ToonHeadDialog):
    notify = DirectNotifyGlobal.directNotify.newCategory('GroupInvitee')

    def __init__(self):
        pass

    def make(self, party, toon, leaderId, merger, **kw):
        self.leaderId = leaderId
        self.avName = toon.getName()
        self.av = toon
        self.avId = toon.doId
        self.avDNA = toon.getStyle()
        self.party = party
        if merger:
            text = TTLocalizer.BoardingInviteeMergeMessage % self.avName
        else:
            text = TTLocalizer.BoardingInviteeMessage % self.avName
        style = TTDialog.TwoChoice
        buttonTextList = [OTPLocalizer.FriendInviteeOK, OTPLocalizer.FriendInviteeNo]
        command = self.__handleButton
        optiondefs = (('dialogName', 'GroupInvitee', None),
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
         ('scale', 0.75, None))
        self.defineoptions(kw, optiondefs)
        ToonHeadDialog.ToonHeadDialog.__init__(self, self.avDNA)
        self.initialiseoptions(GroupInvitee)
        self.show()

    def cleanup(self):
        ToonHeadDialog.ToonHeadDialog.cleanup(self)

    def forceCleanup(self):
        self.party.requestRejectInvite(self.leaderId, self.avId)
        self.cleanup()

    def __handleButton(self, value):
        place = base.cr.playGame.getPlace()
        if value == DGG.DIALOG_OK and place and not place.getState() == 'elevator':
            self.party.requestAcceptInvite(self.leaderId, self.avId)
        else:
            self.party.requestRejectInvite(self.leaderId, self.avId)
        self.cleanup()
