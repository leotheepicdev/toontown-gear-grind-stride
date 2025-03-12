from toontown.base import ToontownGlobals
import SellbotLegFactorySpecExtreme
import SellbotLegFactoryCogsExtreme

def getFactorySpecModule(factoryId):
    return FactorySpecModules[factoryId]


def getCogSpecModule(factoryId):
    return CogSpecModules[factoryId]


FactorySpecModules = {ToontownGlobals.SellbotFactoryInt: SellbotLegFactorySpecExtreme}
CogSpecModules = {ToontownGlobals.SellbotFactoryInt: SellbotLegFactoryCogsExtreme}

if config.GetBool('want-brutal-factory', True):
    from toontown.coghq import SellbotMegaCorpLegSpec
    from toontown.coghq import SellbotMegaCorpLegCogs
    FactorySpecModules[ToontownGlobals.SellbotMegaCorpInt] = SellbotMegaCorpLegSpec
    CogSpecModules[ToontownGlobals.SellbotMegaCorpInt] = SellbotMegaCorpLegCogs
