import FriendsListPanel
import FriendInviter
import FriendInvitee
from direct.directnotify import DirectNotifyGlobal
from toontown.toon import ToonTeleportPanel
from toontown.friends import ToontownFriendSecret
from toontown.pets import PetAvatarPanel
from toontown.toon import ToonAvatarPanel
from toontown.suit import SuitAvatarPanel
from toontown.toon import ToonDNA
from toontown.toon import ToonAvatarDetailPanel
from toontown.base import ToontownGlobals
from toontown.toon import Toon
import FriendHandle
from lib.nametag import NametagGlobals

class FriendsListManager:
    notify = DirectNotifyGlobal.directNotify.newCategory('FriendsListManager')

    def __init__(self):
        self.avatarPanel = None
        self._preserveFriendsList = False
        self._entered = False
        self.friendsRequestQueue = []

    def load(self):
        pass

    def unload(self):
        self.exitFLM()
        if self.avatarPanel:
            del self.avatarPanel
        FriendInviter.unloadFriendInviter()
        ToonAvatarDetailPanel.unloadAvatarDetail()
        ToonTeleportPanel.unloadTeleportPanel()

    def enterFLM(self):
        self.notify.debug('FriendsListManager: enterFLM()')
        if self._preserveFriendsList:
            self._preserveFriendsList = 0
            return
        self._entered = True
        self.accept('openFriendsList', self.__openFriendsList)
        self.accept('clickedNametag', self.__handleClickedNametag)
        base.localAvatar.setFriendsListButtonActive(1)
        NametagGlobals.setMasterNametagsActive(1)
        self.accept('gotoAvatar', self.__handleGotoAvatar)
        self.accept('friendAvatar', self.__handleFriendAvatar)
        self.accept('avatarDetails', self.__handleAvatarDetails)
        self.accept('friendInvitation', self.__handleFriendInvitation)
        if base.cr.friendManager:
            base.cr.friendManager.setAvailable(1)

    def exitFLM(self):
        self.notify.debug('FriendsListManager: exitFLM()')
        if self._preserveFriendsList:
            return
        if not self._entered:
            return
        self._entered = False
        self.ignore('openFriendsList')
        self.ignore('clickedNametag')
        base.localAvatar.setFriendsListButtonActive(0)
        NametagGlobals.setMasterNametagsActive(0)
        if self.avatarPanel:
            self.avatarPanel.cleanup()
            self.avatarPanel = None
        self.ignore('gotoAvatar')
        self.ignore('friendAvatar')
        self.ignore('avatarDetails')
        FriendsListPanel.hideFriendsList()
        ToontownFriendSecret.hideFriendSecret()
        if base.cr.friendManager:
            base.cr.friendManager.setAvailable(0)
        self.ignore('friendInvitation')
        FriendInviter.hideFriendInviter()
        ToonAvatarDetailPanel.hideAvatarDetail()
        ToonTeleportPanel.hideTeleportPanel()

    def __openFriendsList(self):
        FriendsListPanel.showFriendsList()

    def __handleClickedNametag(self, avatar):
        base.hideFriendMargins()
        self.notify.debug('__handleClickedNametag. doId = %s' % avatar.doId)
        if avatar.isPet():
            self.avatarPanel = PetAvatarPanel.PetAvatarPanel(avatar)
        elif isinstance(avatar, Toon.Toon) or isinstance(avatar, FriendHandle.FriendHandle):
            if hasattr(self, 'avatarPanel'):
                if self.avatarPanel:
                    if not hasattr(self.avatarPanel, 'getAvId') or self.avatarPanel.getAvId() == avatar.doId:
                        if not self.avatarPanel.isHidden():
                            if self.avatarPanel.getType() == 'toon':
                                return
            self.avatarPanel = ToonAvatarPanel.ToonAvatarPanel(avatar)
        else:
            self.avatarPanel = SuitAvatarPanel.SuitAvatarPanel(avatar)

    def __handleGotoAvatar(self, avId, avName, avDisableName):
        ToonTeleportPanel.showTeleportPanel(avId, avName, avDisableName)

    def __handleFriendAvatar(self, avId, avName, avDisableName):
        FriendInviter.showFriendInviter(avId, avName, avDisableName)

    def __handleFriendInvitation(self, avId, avName, inviterDna, context):
        dna = ToonDNA.ToonDNA()
        dna.makeFromNetString(inviterDna)
        if not base.localAvatar.isIgnored(avId):
            FriendInvitee.FriendInvitee(avId, avName, dna, context)

    def processQueuedRequests(self):
        if len(self.friendsRequestQueue):
            request = self.friendsRequestQueue.pop(0)
            self.__processFriendRequest(request[0], request[1], request[2], request[3])

    def __processFriendRequest(self, avId, avName, inviterDna = None, context = None):
        self.notify.debug('__handleAvatarFriendInvitation')
        askerToon = base.cr.doId2do.get(avId)
        if askerToon:
            self.notify.debug('got toon')
            dna = askerToon.getStyle()
            if not base.localAvatar.isIgnored(avId):
                FriendInvitee.FriendInvitee(avId, avName, dna, context)
        else:
            self.notify.debug('no toon')

    def __handleAvatarDetails(self, avId, avName):
        ToonAvatarDetailPanel.showAvatarDetail(avId, avName)

    def preserveFriendsList(self):
        self.notify.debug('Preserving Friends List')
        self._preserveFriendsList = True
