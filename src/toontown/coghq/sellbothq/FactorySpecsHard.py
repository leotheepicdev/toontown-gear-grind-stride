from toontown.base import ToontownGlobals
import SellbotLegFactorySpecHard
import SellbotLegFactoryCogsHard

def getFactorySpecModule(factoryId):
    return FactorySpecModules[factoryId]


def getCogSpecModule(factoryId):
    return CogSpecModules[factoryId]


FactorySpecModules = {ToontownGlobals.SellbotFactoryInt: SellbotLegFactorySpecHard}
CogSpecModules = {ToontownGlobals.SellbotFactoryInt: SellbotLegFactoryCogsHard}

if config.GetBool('want-brutal-factory', True):
    from toontown.coghq import SellbotMegaCorpLegSpec
    from toontown.coghq import SellbotMegaCorpLegCogs
    FactorySpecModules[ToontownGlobals.SellbotMegaCorpInt] = SellbotMegaCorpLegSpec
    CogSpecModules[ToontownGlobals.SellbotMegaCorpInt] = SellbotMegaCorpLegCogs
