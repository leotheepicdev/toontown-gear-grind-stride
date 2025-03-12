from panda3d.core import HTTPClient
from direct.directnotify import DirectNotifyGlobal
import os

class TTLauncher:
    notify = DirectNotifyGlobal.directNotify.newCategory('TTLauncher')

    def __init__(self):
        self.http = HTTPClient()

    def getPlayToken(self):
        return self.getValue('TT_PLAYCOOKIE')

    def getGameServer(self):
        return self.getValue('TT_GAMESERVER')

    def getValue(self, key, default = None):
        return os.environ.get(key, default)

    def setPandaErrorCode(self):
        pass

    def setDisconnectDetails(self, disconnectCode, disconnectMsg):
        self.disconnectCode = disconnectCode
        self.disconnectMsg = disconnectMsg

    def setDisconnectDetailsNormal(self):
        self.setDisconnectDetails(0, 'normal')
