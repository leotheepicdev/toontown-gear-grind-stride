from direct.distributed.DistributedObjectAI import DistributedObjectAI
from direct.directnotify.DirectNotifyGlobal import directNotify

class DistributedLeaderBoardAI(DistributedObjectAI):
    notify = directNotify.newCategory('DistributedLeaderBoardAI')
    
    def __init__(self, air):
        DistributedObjectAI.__init__(self, air)
        self.name = ''
        self.posHpr = (0, 0, 0, 0, 0, 0)
        self.records = {}
        self.subscriptions = []
        self.index = -1
        
    def announceGenerate(self):
        DistributedObjectAI.announceGenerate(self)
        self.accept('UpdateRaceRecord', self.updateRaceRecord)
        self.accept('GS_LeaderBoardSwap' + str(self.zoneId), self.setDisplay)
    
    def setName(self, name):
        self.name = name
        
    def getName(self):
        return self.name

    def setPosHpr(self, x, y, z, h, p, r):
        self.posHpr = (x, y, z, h, p, r)
        
    def getPosHpr(self):
        return self.posHpr
        
    def subscribeTo(self, subscription):
        _list = []
        for x in self.air.raceMgr.getRecords(subscription[0], subscription[1]):
            _list.append((x[0], x[3]))            
        self.records.setdefault(subscription[0], {})[subscription[1]] = _list
        self.subscriptions.append(subscription)
        
    def updateRaceRecord(self, record):
        trackId, period = record
        if trackId not in self.records:
            self.notify.warning('trackId {0} not in self.records!'.format(trackId))
            return
        _list = []
        for x in self.air.raceMgr.getRecords(trackId, period):
            _list.append((x[0], x[3]))
            self.records[trackId][period] = _list

    def setDisplay(self):
        self.index += 1
        if self.index >= len(self.subscriptions):
            self.index = 0
        trackId = self.subscriptions[self.index][0]
        recordId = self.subscriptions[self.index][1]
        results = self.records[self.subscriptions[self.index][0]][self.subscriptions[self.index][1]]
        self.sendUpdate('setDisplay', [trackId, recordId, results])