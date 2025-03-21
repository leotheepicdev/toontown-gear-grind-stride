import FactorySpecs
from toontown.level import LevelSpec
from toontown.base import ToontownGlobals

class LawOfficeBase:

    def __init__(self):
        pass

    def setLawOfficeId(self, factoryId):
        self.lawOfficeId = factoryId
        self.factoryType = ToontownGlobals.factoryId2factoryType[factoryId]
        self.cogTrack = ToontownGlobals.cogHQZoneId2dept(factoryId)

    def getCogTrack(self):
        return self.cogTrack

    def getFactoryType(self):
        return self.factoryType
