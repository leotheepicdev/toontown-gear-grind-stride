from toontown.toon import DistributedNPCToonAI

class DistributedNPCHQAI(DistributedNPCToonAI.DistributedNPCToonAI):
    
    def __init__(self, air, npcId, questCallback, hq):
        DistributedNPCToonAI.DistributedNPCToonAI.__init__(self, air, npcId, questCallback, hq)
        