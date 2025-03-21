from direct.showbase import DirectObject
from direct.directnotify import DirectNotifyGlobal
from direct.distributed import DistributedObject
from direct.task import Task
from direct.distributed import DoInterestManager
from toontown.distributed.ToontownDoGlobals import *

_ToonTownDistrictStatInterest = None
_ToonTownDistrictStatInterestComplete = 0
_trashObject = DirectObject.DirectObject()

def EventName():
    return 'ShardPopulationSet'

def isOpen():
    global _ToonTownDistrictStatInterest
    return _ToonTownDistrictStatInterest is not None

def isComplete():
    global _ToonTownDistrictStatInterestComplete
    return _ToonTownDistrictStatInterestComplete

def open(event = None):
    global _trashObject
    global _ToonTownDistrictStatInterest
    if not isOpen():
        def _CompleteProc(event):
            global _ToonTownDistrictStatInterestComplete
            _ToonTownDistrictStatInterestComplete = 1
            if event is not None:
                messenger.send(event)
            return
        _trashObject.acceptOnce(EventName(), _CompleteProc)
        _ToonTownDistrictStatInterest = base.cr.addInterest(DO_ID_TOONTOWN, ZONE_ID_DISTRICTS_STATS, EventName(), EventName())
    elif isComplete():
        messenger.send(EventName())

def refresh(event = None):
    global _ToonTownDistrictStatInterest
    if isOpen():
        if isComplete():
            messenger.send(EventName())
            if event is not none:
                messenger.send(event)
    else:
        def _CompleteProc(event):
            global _ToonTownDistrictStatInterestComplete
            _ToonTownDistrictStatInterestComplete = 1
            if event is not None:
                messenger.send(event)
            close()
            return
        _trashObject.acceptOnce(EventName(), _CompleteProc, [event])
        _ToonTownDistrictStatInterest = base.cr.addInterest(DO_ID_TOONTOWN, ZONE_ID_DISTRICTS_STATS, EventName(), EventName())

def close():
    global _ToonTownDistrictStatInterest
    global _ToonTownDistrictStatInterestComplete
    if isOpen():
        _ToonTownDistrictStatInterestComplete = 0
        base.cr.removeInterest(_ToonTownDistrictStatInterest, None)
        _ToonTownDistrictStatInterest = None


class ToontownDistrictStats(DistributedObject.DistributedObject):
    neverDisable = 1

    def __init__(self, cr):
        DistributedObject.DistributedObject.__init__(self, cr)
        self.districtId = 0

    def setDistrictId(self, value):
        self.districtId = value
    
    def setGroupAvCount(self, groupAvCount):
        if self.districtId in self.cr.activeDistrictMap:
            self.cr.activeDistrictMap[self.districtId].groupAvCount = groupAvCount
            messenger.send('shardInfoUpdated')
