from toontown.pets import PetDNA, PetTraits, PetConstants
from direct.showbase import PythonUtil
from toontown.base import TTLocalizer
import random

def getPetInfoFromSeed(seed, safezoneId):
    S = random.getstate()
    random.seed(seed)
    dnaArray = PetDNA.getRandomPetDNA(safezoneId)
    gender = PetDNA.getGender(dnaArray)
    nameString = TTLocalizer.getRandomPetName(gender=gender, seed=seed)
    traitSeed = PythonUtil.randUint31()
    random.setstate(S)
    return (nameString, dnaArray, traitSeed)

def getPetCostFromSeed(seed, safezoneId):
    name, dna, traitSeed = getPetInfoFromSeed(seed, safezoneId)
    traits = PetTraits.PetTraits(traitSeed, safezoneId)
    traitValue = traits.getOverallValue()
    traitValue -= 0.3
    traitValue = max(0, traitValue)
    rarity = PetDNA.getRarity(dna)
    rarity *= 1.0 - traitValue
    rarity = pow(0.001, rarity) - 0.001
    minCost, maxCost = PetConstants.ZoneToCostRange[safezoneId]
    cost = rarity * (maxCost - minCost) + minCost
    cost = int(cost)
    return cost
