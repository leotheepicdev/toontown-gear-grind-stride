from direct.distributed.PyDatagram import *
from toontown.distributed.ToontownDoGlobals import DO_ID_CLIENT_SERVICES_MANAGER, DO_ID_TT_FRIENDS_MANAGER, DO_ID_GLOBAL_PARTY_MANAGER
from toontown.distributed.DistributedRootObjectAI import DistributedRootObjectAI
from toontown.distributed.ToontownInternalRepository import ToontownInternalRepository

class ToontownUberRepository(ToontownInternalRepository):
    def __init__(self, baseChannel, serverId):
        ToontownInternalRepository.__init__(self, baseChannel, serverId, dcSuffix='UD')
        self.notify.setInfo(True)

    def handleConnected(self):
        ToontownInternalRepository.handleConnected(self)
        rootObj = DistributedRootObjectAI(self)
        rootObj.generateWithRequiredAndId(self.getGameDoId(), 0, 0)
        self.createGlobals()
        self.notify.info('Done.')

    def createGlobals(self):
        self.notify.info('Creating globals...')
        self.csm = simbase.air.generateGlobalObject(DO_ID_CLIENT_SERVICES_MANAGER, 'ClientServicesManager')
        self.friendsManager = simbase.air.generateGlobalObject(DO_ID_TT_FRIENDS_MANAGER, 'TTFriendsManager')
        self.globalPartyMgr = simbase.air.generateGlobalObject(DO_ID_GLOBAL_PARTY_MANAGER, 'GlobalPartyManager')

