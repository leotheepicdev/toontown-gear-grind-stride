from direct.directnotify import DirectNotifyGlobal
from direct.distributed.DistributedObjectAI import DistributedObjectAI

from direct.distributed.ClockDelta import *
from direct.task import Task

from toontown.magicword.MagicWordGlobal import *

from toontown.base import ToontownGlobals
from toontown.parties import PartyGlobals

import FireworkShows
import random

class DistributedFireworkShowAI(DistributedObjectAI):
    notify = DirectNotifyGlobal.directNotify.newCategory("DistributedFireworkShowAI")

    def __init__(self, air):
        DistributedObjectAI.__init__(self, air)
        self.air = air

    def startShow(self, eventId, style, timeStamp):
        taskMgr.doMethodLater(FireworkShows.getShowDuration(eventId, style), self.requestDelete, 'delete%i' % self.doId, [])

    def d_startShow(self, eventId, style, timeStamp):
        self.sendUpdate('startShow', [eventId, style, random.randint(0,1), timeStamp])

    def b_startShow(self, eventId, style, timeStamp):
        self.startShow(eventId, style, timeStamp)
        self.d_startShow(eventId, style, timeStamp)

    def requestFirework(self, todo0, todo1, todo2, todo3, todo4, todo5):
        pass

    def shootFirework(self, todo0, todo1, todo2, todo3, todo4, todo5):
        pass


@magicWord(category=CATEGORY_SYSTEM_ADMINISTRATOR, types=[str])
def fireworks(showName='july4'):
    """
    Starts a fireworks show on the AI server.
    """
    showName = showName.lower()
    if showName == 'july4':
        showType = ToontownGlobals.SUMMER_FIREWORKS
    elif showName == 'newyears':
        showType = ToontownGlobals.NEW_YEAR_FIREWORKS
    elif showName == 'summer':
        showType = PartyGlobals.FireworkShows.Summer
    else:
        return 'Invalid fireworks show name!'
    numShows = len(FireworkShows.shows.get(showType, []))
    showIndex = random.randint(0, numShows - 1)
    for hood in simbase.air.hoods:
        if hood.zoneId == ToontownGlobals.GolfZone:
            continue
        fireworkShow = DistributedFireworkShowAI(simbase.air)
        fireworkShow.generateWithRequired(hood.zoneId)
        fireworkShow.b_startShow(showType, showIndex,
                                 globalClockDelta.getRealNetworkTime())
    return 'A %s fireworks show was started!' % showName
