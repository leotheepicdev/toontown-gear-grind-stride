from DistributedTreasureAI import DistributedTreasureAI
import TreasureGlobals

class DistributedBeanBagTreasureAI(DistributedTreasureAI):

    def __init__(self, air, treasurePlanner, x, y, z, treasureType=TreasureGlobals.TreasureJellybeanBag):
        DistributedTreasureAI.__init__(self, air, treasurePlanner, treasureType, x, y, z)
        self.value = 0    
        
    def setValue(self, value):
        self.value = value
        
    def d_setValue(self, value):
        self.sendUpdate('setValue', [value])
        
    def b_setValue(self, value):
        self.setValue(value)
        self.d_setValue(value)
        
    def getValue(self):
        return self.value
      
    def validAvatar(self, av):
        return 1
        