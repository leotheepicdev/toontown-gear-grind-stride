from toontown.toon import DistributedNPCToon

ChoiceTimeout = 20

class DistributedNPCHQ(DistributedNPCToon.DistributedNPCToon):
    
    def __init__(self, cr):
        DistributedNPCToon.DistributedNPCToon.__init__(self, cr)
        self.toonTag = 'HQ Officer'
        