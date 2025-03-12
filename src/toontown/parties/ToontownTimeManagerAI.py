from datetime import datetime
from toontown.parties.ToontownTimeZone import ToontownTimeZone

class ToontownTimeManagerAI:

    def __init__(self):
        self.serverTimeZone = ToontownTimeZone()

    def getCurServerDateTime(self):
        return datetime.now(self.serverTimeZone)