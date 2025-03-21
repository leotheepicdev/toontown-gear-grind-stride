from toontown.base.ToontownGlobals import *
from direct.directnotify.DirectNotifyGlobal import directNotify

zoneUtilNotify = directNotify.newCategory('ZoneUtil')


def isGoofySpeedwayZone(zoneId):
    return zoneId == 8000


def isCogHQZone(zoneId):
    return zoneId >= 10000 and zoneId < 14000


def isMintInteriorZone(zoneId):
    return zoneId in (CashbotMintIntA, CashbotMintIntB, CashbotMintIntC)


def isDynamicZone(zoneId):
    return zoneId >= DynamicZonesBegin and zoneId < DynamicZonesEnd


def getStreetName(branchId):
    return StreetNames[branchId][-1]


def getLoaderName(zoneId):
    suffix = zoneId % 1000
    if suffix >= 500:
        suffix -= 500
    if isCogHQZone(zoneId):
        loaderName = 'cogHQLoader'
    elif suffix < 100:
        loaderName = 'safeZoneLoader'
    else:
        loaderName = 'townLoader'
    return loaderName


def getBranchLoaderName(zoneId):
    return getLoaderName(getBranchZone(zoneId))


def getSuitWhereName(zoneId):
    where = getWhereName(zoneId, 0)
    return where


def getToonWhereName(zoneId):
    where = getWhereName(zoneId, 1)
    return where


def isPlayground(zoneId):
    whereName = getWhereName(zoneId, False)
    if whereName == 'cogHQExterior':
        return True
    else:
        return zoneId % 1000 == 0 and zoneId < DynamicZonesBegin


def isHQ(zoneId):
    if zoneId == 2520 or zoneId == 1507 or zoneId == 3508 or zoneId == 4504 or zoneId == 5502 or zoneId == 7503 or zoneId == 9505:
        return True
    return False

def isPetshop(zoneId):
    if zoneId == 2522 or zoneId == 1510 or zoneId == 3511 or zoneId == 4508 or zoneId == 5505 or zoneId == 7504 or zoneId == 9508:
        return True
    return False


def getWhereName(zoneId, isToon):
    suffix = zoneId % 1000
    suffix = suffix - suffix % 100
    if isCogHQZone(zoneId):
        if suffix == 0:
            where = 'cogHQExterior'
        elif suffix == 100:
            where = 'cogHQLobby'
        elif suffix == 200:
            where = 'factoryExterior'
        elif getHoodId(zoneId) == LawbotHQ and suffix in (300, 400, 500, 600):
            where = 'stageInterior'
        elif getHoodId(zoneId) == BossbotHQ and suffix in (500, 600, 700):
            where = 'countryClubInterior'
        elif suffix >= 500:
            if getHoodId(zoneId) == SellbotHQ:
                if suffix == 600:
                    where = 'megaCorpInterior'
                else:
                    where = 'factoryInterior'
            elif getHoodId(zoneId) == CashbotHQ:
                where = 'mintInterior'
            else:
                zoneUtilNotify.error('unknown cogHQ interior for hood: ' + str(getHoodId(zoneId)))
        else:
            zoneUtilNotify.error('unknown cogHQ where: ' + str(zoneId))
    elif suffix == 0:
        where = 'playground'
    elif suffix >= 500:
        if isToon:
            where = 'toonInterior'
        else:
            where = 'suitInterior'
    else:
        where = 'street'
    return where


def getBranchZone(zoneId):
    branchId = zoneId - zoneId % 100
    if not isCogHQZone(zoneId):
        if zoneId % 1000 >= 500:
            branchId -= 500
    return branchId


def getCanonicalBranchZone(zoneId):
    return getBranchZone(getCanonicalZoneId(zoneId))


def getCanonicalZoneId(zoneId):
    return zoneId


def getHoodId(zoneId):
    hoodId = zoneId - zoneId % 1000
    return hoodId


def getSafeZoneId(zoneId):
    hoodId = getHoodId(zoneId)
    if hoodId in HQToSafezone:
        hoodId = HQToSafezone[hoodId]
    return hoodId


def getCanonicalHoodId(zoneId):
    return getHoodId(getCanonicalZoneId(zoneId))

def getCanonicalSafeZoneId(zoneId):
    return getSafeZoneId(getCanonicalZoneId(zoneId))

def isInterior(zoneId):
    r = zoneId % 1000 >= 500
    return r

def getWakeInfo(hoodId = None, zoneId = None):
    wakeWaterHeight = 0
    showWake = 0
    try:
        if hoodId is None:
            hoodId = base.cr.playGame.getPlaceId()
        if zoneId is None:
            zoneId = base.cr.playGame.getPlace().getZoneId()
        canonicalZoneId = getCanonicalZoneId(zoneId)
        if canonicalZoneId == DonaldsDock:
            wakeWaterHeight = DDWakeWaterHeight
            showWake = 1
        elif canonicalZoneId == ToontownCentral:
            wakeWaterHeight = TTWakeWaterHeight
            showWake = 1
        elif canonicalZoneId == OutdoorZone:
            wakeWaterHeight = OZWakeWaterHeight
            showWake = 1
        elif hoodId == MyEstate:
            wakeWaterHeight = EstateWakeWaterHeight
            showWake = 1
    except AttributeError:
        pass

    return (showWake, wakeWaterHeight)

def canWearSuit(zoneId):
    zoneId = getCanonicalHoodId(zoneId)

    return zoneId >= DynamicZonesBegin or zoneId in [LawbotHQ, CashbotHQ, SellbotHQ, BossbotHQ]
