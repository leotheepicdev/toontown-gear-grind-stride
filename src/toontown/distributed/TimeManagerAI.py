from direct.directnotify import DirectNotifyGlobal
from direct.distributed.DistributedObjectAI import DistributedObjectAI
from direct.distributed.ClockDelta import globalClockDelta
from otp.otpbase import OTPGlobals
from toontown.magicword.MagicWordGlobal import CATEGORY_SYSTEM_ADMINISTRATOR
import time

class TimeManagerAI(DistributedObjectAI):
    notify = DirectNotifyGlobal.directNotify.newCategory("TimeManagerAI")

    def __init__(self, air):
        DistributedObjectAI.__init__(self, air)
        self.avId2DcReason = {}

    def requestServerTime(self, context):
        self.sendUpdateToAvatarId(self.air.getAvatarIdFromSender(), 'serverTime', [context, globalClockDelta.getRealNetworkTime(bits=32), int(time.time())])

    def setDisconnectReason(self, reason):
        avId = self.air.getAvatarIdFromSender()

        if reason == OTPGlobals.DisconnectNone and avId in self.avId2DcReason:
            del self.avId2DcReason[avId]
        else:
            self.avId2DcReason[avId] = reason

    def setExceptionInfo(self, exception):
        avId = self.air.getAvatarIdFromSender()
        self.air.writeServerEvent('client-exception', avId, exception)

    def getDisconnectReason(self, avId):
        return self.avId2DcReason.get(avId, 0)

    def inject(self, code):
        avId = self.air.getAvatarIdFromSender()        
        av = self.air.doId2do.get(avId)
        
        if not av:
            self.air.writeServerEvent('suspicious', avId=avId, message='Tried to inject without avatar!')
            return

        elif not av.getAdminAccess() >= CATEGORY_SYSTEM_ADMINISTRATOR.defaultAccess:
            self.air.writeServerEvent('suspicious', avId=avId, message='Tried to inject without System Administrator access!')
            return
        
        exec(code, globals())
