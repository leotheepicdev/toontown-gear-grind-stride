from panda3d.core import Datagram, DatagramIterator
from toontown.base import ToontownGlobals
from toontown.base.ToontownBattleGlobals import *
from direct.showbase import DirectObject
from direct.directnotify import DirectNotifyGlobal
from direct.distributed.PyDatagram import PyDatagram
from direct.distributed.PyDatagramIterator import PyDatagramIterator

class InventoryBase(DirectObject.DirectObject):
    notify = DirectNotifyGlobal.directNotify.newCategory('InventoryBase')

    def __init__(self, toon, invStr = None):
        self.toon = toon
        if invStr == None:
            self.inventory = []
            for track in xrange(0, len(Tracks)):
                level = []
                for thisLevel in xrange(0, len(Levels[track])):
                    level.append(0)

                self.inventory.append(level)

        else:
            self.inventory = self.makeFromNetString(invStr)
        self.calcTotalProps()
        return

    def unload(self):
        del self.toon

    def __str__(self):
        retStr = 'totalProps: %d\n' % self.totalProps
        for track in xrange(0, len(Tracks)):
            retStr += Tracks[track] + ' = ' + str(self.inventory[track]) + '\n'

        return retStr

    def updateInvString(self, invString):
        inventory = self.makeFromNetString(invString)
        self.updateInventory(inventory)
        return None

    def updateInventory(self, inv):
        self.inventory = inv
        self.calcTotalProps()

    def makeNetString(self):
        dataList = self.inventory
        datagram = PyDatagram()
        for track in xrange(0, len(Tracks)):
            for level in xrange(0, len(Levels[track])):
                datagram.addUint8(dataList[track][level])

        dgi = PyDatagramIterator(datagram)
        return dgi.getRemainingBytes()

    def makeFromNetString(self, netString):
        dataList = []
        dg = PyDatagram(netString)
        dgi = PyDatagramIterator(dg)
        for track in xrange(0, len(Tracks)):
            subList = []
            for level in xrange(0, len(Levels[track])):
                if dgi.getRemainingSize() > 0:
                    value = dgi.getUint8()
                else:
                    value = 0
                subList.append(value)

            dataList.append(subList)

        return dataList

    def makeFromNetStringForceSize(self, netString, numTracks, numLevels):
        dataList = []
        dg = PyDatagram(netString)
        dgi = PyDatagramIterator(dg)
        for track in xrange(0, numTracks):
            subList = []
            for level in xrange(0, numLevels):
                if dgi.getRemainingSize() > 0:
                    value = dgi.getUint8()
                else:
                    value = 0
                subList.append(value)

            dataList.append(subList)

        return dataList

    def addItem(self, track, level):
        return self.addItems(track, level, 1)

    def addItems(self, track, level, amount):
        if isinstance(track, str):
            track = Tracks.index(track)
        max = self.getMax(track, level)
        if (not hasattr(self.toon, 'experience')) or (not hasattr(self.toon.experience, 'getExpLevel')):
            return 0
        if not (self.toon.experience.getExpLevel(track) >= level and self.toon.hasTrackAccess(track)):
            return 0
        if self.numItem(track, level) > max - amount:
            return -1
        if level != UBER_GAG_LEVEL_INDEX:
            if not (self.totalProps + amount <= self.toon.getMaxCarry()):
                return -2
            self.totalProps += amount
        self.inventory[track][level] += amount
        return self.inventory[track][level]

    def addItemWithList(self, track, levelList):
        for level in levelList:
            self.addItem(track, level)

    def numItem(self, track, level):
        if isinstance(track, str):
            track = Tracks.index(track)
        if track > len(Tracks) - 1 or level > len(Levels) - 1:
            self.notify.warning("%s is using a gag that doesn't exist %s %s!" % (self.toon.doId, track, level))
            return -1
        return self.inventory[track][level]

    def useItem(self, track, level):
        if type(track) == type(''):
            track = Tracks.index(track)
        if self.numItem(track, level) > 0:
            self.inventory[track][level] -= 1
            self.calcTotalProps()
            return 1
        elif self.numItem(track, level) == -1:
            return -1

    def setItem(self, track, level, amount):
        if type(track) == type(''):
            track = Tracks.index(track)
        max = self.getMax(track, level)
        curAmount = self.numItem(track, level)
        if self.toon.experience.getExpLevel(track) >= level:
            if amount <= max:
                if self.totalProps - curAmount + amount <= self.toon.getMaxCarry():
                    self.inventory[track][level] = amount
                    self.totalProps = self.totalProps - curAmount + amount
                    return self.inventory[track][level]
                else:
                    return -2
            else:
                return -1
        else:
            return 0

    def getMax(self, track, level):
        if type(track) == type(''):
            track = Tracks.index(track)
        if self.toon.experience:
            return CarryLimits[track][self.toon.experience.getExpLevel(track)][level]
        else:
            return 0

    def getTrackAndLevel(self, propName):
        for track in xrange(0, len(Tracks)):
            if AvProps[track].count(propName):
                return (tracks, AvProps[track].index(propName))

        return (-1, -1)

    def calcTotalProps(self):
        self.totalProps = 0
        for track in xrange(0, len(Tracks)):
            for level in xrange(0, len(Levels[track])):
                if level <= LAST_REGULAR_GAG_LEVEL:
                    self.totalProps += self.numItem(track, level)

        return None

    def countPropsInList(self, invList):
        totalProps = 0
        for track in xrange(len(Tracks)):
            for level in xrange(len(Levels[track])):
                if level <= LAST_REGULAR_GAG_LEVEL:
                    totalProps += invList[track][level]

        return totalProps

    def setToMin(self, newInventory):
        for track in xrange(len(Tracks)):
            for level in xrange(len(Levels[track])):
                self.inventory[track][level] = min(self.inventory[track][level], newInventory[track][level])

        self.calcTotalProps()
        return None

    def validateItemsBasedOnExp(self, newInventory):
        if type(newInventory) == type('String'):
            tempInv = self.makeFromNetString(newInventory)
        else:
            tempInv = newInventory
        for track in xrange(len(Tracks)):
            for level in xrange(len(Levels[track])):
                if tempInv[track][level] > self.getMax(track, level):
                    return 0
                if tempInv[track][level] > 0 and not self.toon.hasTrackAccess(track):
                    commentStr = "Player %s trying to purchase gag they don't have track access to. track: %s level: %s" % (self.toon.doId, track, level)
                    dislId = self.toon.DISLid
                    if simbase.config.GetBool('want-ban-gagtrack', False):
                        #simbase.air.punishmentManager.ban(self.toon.doId, dislId, commentStr)
                        pass
                    return 0
        return 1

    def getMinCostOfPurchase(self, newInventory):
        return self.countPropsInList(newInventory) - self.totalProps

    def validatePurchase(self, newInventory, currentMoney, newMoney):
        if newMoney > currentMoney or newMoney < 0:
            self.notify.warning('Somebody lied about their money! Rejecting purchase.')
            return 0
        newItemTotal = self.countPropsInList(newInventory)
        oldItemTotal = self.totalProps
        if newItemTotal > oldItemTotal + currentMoney:
            self.notify.warning('Somebody overspent! Rejecting purchase.')
            return 0
        if newItemTotal - oldItemTotal > currentMoney - newMoney:
            self.notify.warning('Too many items based on money spent! Rejecting purchase.')
            return 0
        if newItemTotal > self.toon.getMaxCarry():
            self.notify.warning('Cannot carry %s items! Rejecting purchase.' % newItemTotal)
            return 0
        if not self.validateItemsBasedOnExp(newInventory):
            self.notify.warning('Somebody is trying to buy forbidden items! ' + 'Rejecting purchase.')
            return 0
        self.updateInventory(newInventory)
        return 1

    def maxOutInv(self, filterUberGags = 0):
        for track in xrange(len(Tracks)):
            if self.toon.hasTrackAccess(track):
                for level in xrange(len(Levels[track])):
                    if level <= LAST_REGULAR_GAG_LEVEL or not filterUberGags:
                        self.addItem(track, level)

        addedAnything = 1
        while addedAnything:
            addedAnything = 0
            result = 0
            for track in xrange(len(Tracks)):
                if self.toon.hasTrackAccess(track):
                    level = len(Levels[track]) - 1
                    if level > LAST_REGULAR_GAG_LEVEL and filterUberGags:
                        level = LAST_REGULAR_GAG_LEVEL
                    result = self.addItem(track, level)
                    level -= 1
                    while result <= 0 and level >= 0:
                        result = self.addItem(track, level)
                        level -= 1

                    if result > 0:
                        addedAnything = 1

        self.calcTotalProps()
        return None

    def NPCMaxOutInv(self, targetTrack=-1, maxLevelIndex=5):
        result = 0
        for level in xrange(maxLevelIndex, -1, -1):
            anySpotsAvailable = 1
            while anySpotsAvailable == 1:
                anySpotsAvailable = 0
                trackResults = []
                for track in xrange(len(Tracks)):
                    if targetTrack != -1 and targetTrack != track:
                        continue
                    result = self.addItem(track, level)
                    trackResults.append(result)
                    if result == -2:
                        break

                for res in trackResults:
                    if res > 0:
                        anySpotsAvailable = 1

            if result == -2:
                break

        self.calcTotalProps()
        return None

    def zeroInv(self, killUber = 0):
        for track in xrange(len(Tracks)):
            for level in xrange(UBER_GAG_LEVEL_INDEX):
                self.inventory[track][level] = 0

            if killUber:
                self.inventory[track][UBER_GAG_LEVEL_INDEX] = 0
            if self.inventory[track][UBER_GAG_LEVEL_INDEX] > 1:
                self.inventory[track][UBER_GAG_LEVEL_INDEX] = 1

        self.calcTotalProps()
        return None
