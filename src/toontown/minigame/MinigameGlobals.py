from direct.showbase import PythonUtil
from toontown.base import ToontownGlobals
from toontown.hood import ZoneUtil
latencyTolerance = 10.0
MaxLoadTime = 40.0
rulesDuration = 21
JellybeanTrolleyHolidayScoreMultiplier = 3
DifficultyOverrideMult = int(1 << 16)

def QuantizeDifficultyOverride(diffOverride):
    return int(round(diffOverride * DifficultyOverrideMult)) / float(DifficultyOverrideMult)


NoDifficultyOverride = 2147483647
NoTrolleyZoneOverride = -1
SafeZones = [ToontownGlobals.ToontownCentral,
 ToontownGlobals.DonaldsDock,
 ToontownGlobals.DaisyGardens,
 ToontownGlobals.MinniesMelodyland,
 ToontownGlobals.TheBrrrgh,
 ToontownGlobals.DonaldsDreamland,
 ToontownGlobals.WackyWest,
 ToontownGlobals.ConstructionZone]

def getDifficulty(trolleyZone):
    hoodZone = getSafezoneId(trolleyZone)
    return float(SafeZones.index(hoodZone)) / (len(SafeZones) - 1)


def getSafezoneId(trolleyZone):
    return ZoneUtil.getCanonicalHoodId(trolleyZone)

def getScoreMult(trolleyZone):
    szId = getSafezoneId(trolleyZone)
    multiplier = PythonUtil.lerp(1.0, 1.5, float(SafeZones.index(szId)) / (len(SafeZones) - 1) + 2)
    return multiplier
