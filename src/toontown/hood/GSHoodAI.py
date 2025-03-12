from toontown.dna.DNAParser import DNAGroup, DNAVisGroup
from toontown.hood import HoodAI
from toontown.hood import ZoneUtil
from toontown.racing import RaceGlobals
from toontown.racing.DistributedRacePadAI import DistributedRacePadAI
from toontown.racing.DistributedStartingBlockAI import DistributedStartingBlockAI
from toontown.racing.DistributedViewPadAI import DistributedViewPadAI
from toontown.racing.DistributedStartingBlockAI import DistributedViewingBlockAI
from toontown.racing.DistributedLeaderBoardAI import DistributedLeaderBoardAI
from toontown.base import ToontownGlobals

class GSHoodAI(HoodAI.HoodAI):
    __slots__ = ('air', 'zoneId', 'canonicalHoodId', 'fishingPonds', 'partyGates', 'treasurePlanner', 'buildingManagers', 'suitPlanners', 'racingPads', 'viewingPads', 'viewingBlocks', 'startingBlocks', 'leaderBoards')

    def __init__(self, air):
        HoodAI.HoodAI.__init__(self, air,
                               ToontownGlobals.GoofySpeedway,
                               ToontownGlobals.GoofySpeedway)

        self.racingPads = []
        self.viewingPads = []
        self.viewingBlocks = []
        self.startingBlocks = []
        self.leaderBoards = []

        self.startup()

    def startup(self):
        HoodAI.HoodAI.startup(self)

        self.createStartingBlocks()
        self.cycleDuration = 10
        self.createLeaderBoards()
        self.__cycleLeaderBoards()

    def shutdown(self):
        HoodAI.HoodAI.shutdown(self)

        taskMgr.removeTasksMatching('leaderBoardSwitch')
        for board in self.leaderBoards:
            board.delete()
        del self.leaderBoards
        
    def __cycleLeaderBoards(self, task=None):
        messenger.send('GS_LeaderBoardSwap' + str(self.zoneId))
        taskMgr.doMethodLater(self.cycleDuration, self.__cycleLeaderBoards, str(self) + '_leaderBoardSwitch')

    def findRacingPads(self, dnaGroup, zoneId, area, padType='racing_pad'):
        racingPads = []
        racingPadGroups = []
        if isinstance(dnaGroup, DNAGroup) and (padType in dnaGroup.getName()):
            racingPadGroups.append(dnaGroup)

            if padType == 'racing_pad':
                nameInfo = dnaGroup.getName().split('_')
                racingPad = DistributedRacePadAI(simbase.air)
                racingPad.setArea(zoneId)
                racingPad.nameType = nameInfo[3]
                racingPad.index = int(nameInfo[2])
                nextRaceInfo = RaceGlobals.getNextRaceInfo(-1, racingPad.nameType, racingPad.index)
                racingPad.setTrackInfo([nextRaceInfo[0], nextRaceInfo[1]])
                racingPad.generateWithRequired(zoneId)
            elif padType == 'viewing_pad':
                racingPad = DistributedViewPadAI(simbase.air)
                racingPad.setArea(zoneId)
                racingPad.generateWithRequired(zoneId)
            else:
                self.notify.error('Invalid racing pad type: ' + padType)

            racingPads.append(racingPad)
        elif isinstance(dnaGroup, DNAVisGroup):
            zoneId = int(dnaGroup.getName().split(':')[0])
        for i in xrange(dnaGroup.getNumChildren()):
            (foundRacingPads, foundRacingPadGroups) = self.findRacingPads(dnaGroup.at(i), zoneId, area, padType=padType)
            racingPads.extend(foundRacingPads)
            racingPadGroups.extend(foundRacingPadGroups)
        return (racingPads, racingPadGroups)

    def findStartingBlocks(self, dnaGroup, racePad):
        startingBlocks = []
        if isinstance(dnaGroup, DNAGroup) and ('starting_block' in dnaGroup.getName()):
            x, y, z = dnaGroup.getPos()
            h, p, r = dnaGroup.getHpr()
            padLocationId = getattr(racePad, 'index', 0)
            if isinstance(racePad, DistributedRacePadAI):
                startingBlock = DistributedStartingBlockAI(simbase.air, racePad, x, y, z, h, p, r, padLocationId)
            elif isinstance(racePad, DistributedViewPadAI):
                startingBlock = DistributedViewingBlockAI(simbase.air, racePad, x, y, z, h, p, r, padLocationId)
            else:
                self.notify.error('Unknown starting block type.')
            startingBlock.generateWithRequired(racePad.zoneId)

            startingBlocks.append(startingBlock)
        for i in xrange(dnaGroup.getNumChildren()):
            foundStartingBlocks = self.findStartingBlocks(dnaGroup.at(i), racePad)
            startingBlocks.extend(foundStartingBlocks)
        return startingBlocks

    def createStartingBlocks(self):
        self.racingPads = []
        self.viewingPads = []
        racingPadGroups = []
        viewingPadGroups = []
        for zoneId in self.getZoneTable():
            dnaData = self.air.dnaDataMap.get(zoneId, None)
            if dnaData.getName() == 'root':
                area = ZoneUtil.getCanonicalZoneId(zoneId)
                (foundRacingPads, foundRacingPadGroups) = self.findRacingPads(dnaData, zoneId, area, padType='racing_pad')
                (foundViewingPads, foundViewingPadGroups) = self.findRacingPads(dnaData, zoneId, area, padType='viewing_pad')
                self.racingPads.extend(foundRacingPads)
                racingPadGroups.extend(foundRacingPadGroups)
                self.viewingPads.extend(foundViewingPads)
                viewingPadGroups.extend(foundViewingPadGroups)
        self.startingBlocks = []
        for (dnaGroup, racePad) in zip(racingPadGroups, self.racingPads):
            foundStartingBlocks = self.findStartingBlocks(dnaGroup, racePad)
            self.startingBlocks.extend(foundStartingBlocks)
            for startingBlock in foundStartingBlocks:
                racePad.addStartingBlock(startingBlock)
        self.viewingBlocks = []
        for (dnaGroup, viewPad) in zip(viewingPadGroups, self.viewingPads):
            foundViewingBlocks = self.findStartingBlocks(dnaGroup, viewPad)
            self.viewingBlocks.extend(foundViewingBlocks)
            for viewingBlock in foundViewingBlocks:
                viewPad.addStartingBlock(viewingBlock)

    def findLeaderBoards(self, dnaGroup, zoneId):
        if not self.air.wantKarts:
            return

        leaderBoards = []

        if isinstance(dnaGroup, DNAGroup) and ('leader_board' in dnaGroup.getName()):
            for i in xrange(dnaGroup.getNumChildren()):
                childDnaGroup = dnaGroup.at(i)

                if 'leaderBoard' in childDnaGroup.getName():
                    x, y, z = childDnaGroup.getPos()
                    h, p, r, = childDnaGroup.getHpr()
                    leaderBoard = DistributedLeaderBoardAI(simbase.air)
                    leaderBoard.setName(childDnaGroup.getName())
                    leaderBoard.setPosHpr(x, y, z, h, p, r)
                    leaderBoard.generateWithRequired(zoneId)
                    leaderBoards.append(leaderBoard)
        elif isinstance(dnaGroup, DNAVisGroup):
            zoneId = int(dnaGroup.getName().split(':')[0])

        for i in xrange(dnaGroup.getNumChildren()):
            foundLeaderBoards = self.findLeaderBoards(dnaGroup.at(i), zoneId)
            leaderBoards.extend(foundLeaderBoards)

        return leaderBoards

    def createLeaderBoards(self):
        self.leaderBoards = []
        dnaData = self.air.dnaDataMap[self.zoneId]
        if dnaData.getName() == 'root':
            self.leaderBoards = self.findLeaderBoards(dnaData, self.zoneId)
        for distObj in self.leaderBoards:
            if distObj:
                if distObj.getName().count('city'):
                    type = 'city'
                else:
                    if distObj.getName().count('stadium'):
                        type = 'stadium'
                    else:
                        if distObj.getName().count('country'):
                            type = 'country'
                for subscription in RaceGlobals.LBSubscription[type]:
                    distObj.subscribeTo(subscription)
