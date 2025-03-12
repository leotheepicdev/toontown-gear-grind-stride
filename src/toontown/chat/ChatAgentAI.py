from direct.distributed.DistributedObjectGlobalAI import DistributedObjectGlobalAI

class ChatAgentAI(DistributedObjectGlobalAI): # TODO: Finish Chat Mode that wasn't complete in Toontown Stride
    wantWhitelist = simbase.config.GetBool('want-whitelist', True)

    def announceGenerate(self):
        DistributedObjectGlobalAI.announceGenerate(self)

    def chatMessage(self, message, chatMode):
        sender = self.air.getAvatarIdFromSender()
        if sender == 0:
            self.air.writeServerEvent('suspicious', self.air.getAccountIdFromSender(), 'Account sent chat without an avatar', message)
            return
        av = self.air.doId2do.get(sender)
        if av is None:
            return
        if chatMode < 0:
            self.air.writeServerEvent('suspicious', sender, 'Tried to send chat below chat mode 0.')
            return
        if chatMode == 1:
           if av.getAdminAccess() < 300:
               self.air.writeServerEvent('suspicious', sender, 'Tried to send chat under chat mode 1, but is below 300 access level')
               return
        elif chatMode == 2:
           if av.getAdminAccess() < 500:
               self.air.writeServerEvent('suspicious', sender, 'Tried to send chat under chat mode 2, but is below 500 access level')
               return
        elif chatMode == 3:
           if av.getAdminAccess() < 600:
               self.air.writeServerEvent('suspicious', sender, 'Tried to send chat under chat mode 3, but is below 600 access level')
               return
        elif chatMode == 4:
           if av.getAdminAccess() < 700:
               self.air.writeServerEvent('suspicious', sender, 'Tried to send chat under chat mode 4, but is below 700 access level')
               return
        if simbase.config.GetString('accountdb-type', 'developer') == 'remote':
            self.sendMessageToWebsite(message)
        self.air.writeServerEvent('chat-said', sender, 'Zone ID: %s|Message: %s' % (av.zoneId, message))
        self.air.send(self.air.dclassesByName['DistributedAvatarAI'].aiFormatUpdate('setTalk', sender, sender, self.air.ourChannel, [message]))

    def sendMessageToWebsite(self, message):
        pass