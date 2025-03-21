from panda3d.core import Datagram
import CatalogItem
from toontown.base import ToontownGlobals
from toontown.base import TTLocalizer
from direct.interval.IntervalGlobal import *

class CatalogEmoteItem(CatalogItem.CatalogItem):
    sequenceNumber = 0
    pictureToon = None

    def makeNewItem(self, emoteIndex, isSpecial = False):
        self.emoteIndex = emoteIndex
        self.isSpecial = isSpecial
        CatalogItem.CatalogItem.makeNewItem(self)

    def getPurchaseLimit(self):
        return 1

    def reachedPurchaseLimit(self, avatar):
        if self in avatar.onOrder or self in avatar.mailboxContents or self in avatar.onGiftOrder:
            return 1
        if self.emoteIndex >= len(avatar.emoteAccess):
            return 0
        return avatar.emoteAccess[self.emoteIndex] != 0

    def getAcceptItemErrorText(self, retcode):
        if retcode == ToontownGlobals.P_ItemAvailable:
            return TTLocalizer.CatalogAcceptEmote
        return CatalogItem.CatalogItem.getAcceptItemErrorText(self, retcode)

    def saveHistory(self):
        return 1

    def getTypeName(self):
        return TTLocalizer.EmoteTypeName

    def getName(self):
        return TTLocalizer.EmoteList[self.emoteIndex]

    def recordPurchase(self, avatar, optional):
        if self.emoteIndex < 0 or self.emoteIndex > len(avatar.emoteAccess):
            self.notify.warning('Invalid emote access: %s for avatar %s' % (self.emoteIndex, avatar.doId))
            return ToontownGlobals.P_InvalidIndex
        avatar.emoteAccess[self.emoteIndex] = 1
        avatar.d_setEmoteAccess(avatar.emoteAccess)
        return ToontownGlobals.P_ItemAvailable

    def getPicture(self, avatar):
        from toontown.toon import Toon
        from toontown.toon import ToonHead
        from toontown.toon import TTEmote
        from toontown.avatar import Emote
        self.hasPicture = True
        if self.emoteIndex in Emote.globalEmote.getHeadEmotes():
            toon = ToonHead.ToonHead()
            toon.setupHead(avatar.style, forGui=1)
        else:
            toon = Toon.Toon()
            toon.setDNA(avatar.style)
            toon.loop('neutral')
        toon.setH(180)
        model, ival = self.makeFrameModel(toon, 0)
        track, duration = Emote.globalEmote.doEmote(toon, self.emoteIndex, volume=self.volume)
        if duration == None:
            duration = 0
        name = 'emote-item-%s' % self.sequenceNumber
        CatalogEmoteItem.sequenceNumber += 1
        if track != None:
            track = Sequence(Sequence(track, duration=0), Wait(duration + 2), name=name)
        else:
            track = Sequence(Func(Emote.globalEmote.doEmote, toon, self.emoteIndex), Wait(duration + 4), name=name)
        self.pictureToon = toon
        return (model, track)

    def changeIval(self, volume):
        from toontown.toon import Toon
        from toontown.toon import ToonHead
        from toontown.toon import TTEmote
        from toontown.avatar import Emote
        self.volume = volume
        if not hasattr(self, 'pictureToon'):
            return Sequence()
        track, duration = Emote.globalEmote.doEmote(self.pictureToon, self.emoteIndex, volume=self.volume)
        if duration == None:
            duration = 0
        name = 'emote-item-%s' % self.sequenceNumber
        CatalogEmoteItem.sequenceNumber += 1
        if track != None:
            track = Sequence(Sequence(track, duration=0), Wait(duration + 2), name=name)
        else:
            track = Sequence(Func(Emote.globalEmote.doEmote, toon, self.emoteIndex), Wait(duration + 4), name=name)
        return track

    def output(self, store = -1):
        return 'CatalogEmoteItem(%s%s)' % (self.emoteIndex, self.formatOptionalData(store))

    def compareTo(self, other):
        return self.emoteIndex - other.emoteIndex

    def getHashContents(self):
        return self.emoteIndex

    def getBasePrice(self):
        return 550

    def decodeDatagram(self, di, versionNumber, store):
        CatalogItem.CatalogItem.decodeDatagram(self, di, versionNumber, store)
        self.emoteIndex = di.getUint8()
        self.isSpecial = di.getBool()
        if self.emoteIndex > len(TTLocalizer.EmoteList):
            raise ValueError

    def encodeDatagram(self, dg, store):
        CatalogItem.CatalogItem.encodeDatagram(self, dg, store)
        dg.addUint8(self.emoteIndex)
        dg.addBool(self.isSpecial)

    def isGift(self):
        return not self.getEmblemPrices()
