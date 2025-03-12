import hashlib, hmac
from direct.directnotify.DirectNotifyGlobal import directNotify
from direct.distributed.DistributedObjectGlobal import DistributedObjectGlobal
from lib.nametag.NametagConstants import WTSystem
from lib.margins.WhisperPopup import WhisperPopup
from toontown.distributed.PotentialAvatar import PotentialAvatar
from toontown.base import ToontownGlobals

FIXED_KEY = 'd;j;676yhjghygfytuafjpd32343er0347980&DlP(TIGKG(*^*%90yhjhytuygyyhtyt4yoerhfj*h^#@dfY@lkflssidfdkdj93874*&*^**%$*23232sadf'

class ClientServicesManager(DistributedObjectGlobal):
    notify = directNotify.newCategory('ClientServicesManager')
    systemMessageSfx = None
    avIdList = []

    def requestChallenge(self, doneEvent):
        self.doneEvent = doneEvent
        playToken = self.cr.playToken
        key = FIXED_KEY + base.config.GetString('server-version', 'version_not_set')
        key = hashlib.sha512(key).digest()
        clientKey = hmac.new(key, playToken, digestmod=hashlib.sha512).digest()
        self.sendUpdate('challengeSender', [clientKey, playToken])       

    def challengeWon(self, timestamp):
        messenger.send(self.doneEvent, [{'mode': 'success', 'timestamp': timestamp}])

    # --- AVATARS LIST ---
    def requestAvatars(self):
        self.sendUpdate('requestAvatars')

    def setAvatars(self, chatSettings, avatars):
        avList = []
        for avNum, avName, avDNA, avPosition, nameState in avatars:
            nameOpen = int(nameState == 1)
            names = [avName, '', '', '']
            if nameState == 2: # PENDING
                names[1] = avName
            elif nameState == 3: # APPROVED
                names[2] = avName
            elif nameState == 4: # REJECTED
                names[3] = avName
            self.avIdList = []
            self.avIdList.append(avNum)
            avList.append(PotentialAvatar(avNum, names, avDNA, avPosition, nameOpen))

        self.cr.handleChatSettings(chatSettings)
        self.cr.handleAvatarsList(avList)

    # --- AVATAR CREATION/DELETION ---
    def sendCreateAvatar(self, avDNA, _, index, track1Type, track2Type):
        self.sendUpdate('createAvatar', [avDNA.makeNetString(), index, track1Type, track2Type])

    def createAvatarResp(self, avId):
        messenger.send('nameShopCreateAvatarDone', [avId])

    def sendDeleteAvatar(self, avId):
        self.sendUpdate('deleteAvatar', [avId])

    # No deleteAvatarResp; it just sends a setAvatars when the deed is done.

    # --- AVATAR NAMING ---
    def sendSetNameTyped(self, avId, name, callback):
        self._callback = callback
        self.sendUpdate('setNameTyped', [avId, name])

    def setNameTypedResp(self, avId, status):
        self._callback(avId, status)

    def sendSetNamePattern(self, avId, p1, f1, p2, f2, p3, f3, p4, f4, callback):
        self._callback = callback
        self.sendUpdate('setNamePattern', [avId, p1, f1, p2, f2, p3, f3, p4, f4])

    def setNamePatternResp(self, avId, status):
        self._callback(avId, status)

    def sendAcknowledgeAvatarName(self, avId, callback):
        self._callback = callback
        self.sendUpdate('acknowledgeAvatarName', [avId])

    def acknowledgeAvatarNameResp(self):
        self._callback()

    # --- AVATAR CHOICE ---
    def sendChooseAvatar(self, avId):
        self.sendUpdate('chooseAvatar', [avId])

    def systemMessage(self, message):
        whisper = WhisperPopup(message, ToontownGlobals.getInterfaceFont(), WTSystem)
        whisper.manage(base.marginManager)

        if hasattr(base, 'localAvatar'):
            if hasattr(base.localAvatar, 'chatLog'):
                base.localAvatar.chatLog.log('System Message', message, color='amaranth')      
		
        if self.systemMessageSfx is None:
            self.systemMessageSfx = loader.loadSfx('phase_4/audio/sfx/clock03.ogg')

        base.playSfx(self.systemMessageSfx)
