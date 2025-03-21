from panda3d.core import Datagram
from direct.directnotify import DirectNotifyGlobal
from direct.distributed.PyDatagram import PyDatagram
import cPickle, zlib

class ToontownNetMessengerAI:
    """
    This works very much like the NetMessenger class except that
    this is much simpler and makes much more sense.
    """
    notify = DirectNotifyGlobal.directNotify.newCategory('ToontownNetMessengerAI')

    def __init__(self, air, msgChannel=40000, msgType=54321):
        self.air = air
        self.air.registerForChannel(msgChannel)
        self.msgChannel = msgChannel
        self.msgType = msgType
        
    def prepare(self, message, sentArgs=[], channels=None):
        dg = PyDatagram()
        if channels is None:
            channels = [self.msgChannel]
        dg.addInt8(len(channels))
        for channel in channels:
            dg.addChannel(channel)
        dg.addChannel(self.air.ourChannel)
        dg.addUint16(self.msgType)
        dg.addString(message)
        dg.addString(zlib.compress(cPickle.dumps(sentArgs)))
        return dg
        
    def send(self, message, sentArgs=[], channels=None):
        self.notify.debug('sendNetEvent: %s %r' % (message, sentArgs))
        dg = self.prepare(message, sentArgs, channels)
        self.air.send(dg)
        
    def handle(self, msgType, di):
        message = di.getString()
        data = zlib.decompress(di.getString())
        sentArgs = cPickle.loads(data)
        messenger.send(message, sentArgs)
