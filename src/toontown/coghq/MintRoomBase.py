from toontown.base import ToontownGlobals

class MintRoomBase:

    def __init__(self):
        pass

    def setMintId(self, mintId):
        self.mintId = mintId
        self.cogTrack = ToontownGlobals.cogHQZoneId2dept(mintId)

    def setRoomId(self, roomId):
        self.roomId = roomId

    def getCogTrack(self):
        return self.cogTrack
