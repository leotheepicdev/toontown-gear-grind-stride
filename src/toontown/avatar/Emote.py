import types
from toontown.base.TTLocalizer import EmoteFuncDict

class Emote:
    EmoteClear = -1
    EmoteEnableStateChanged = 'EmoteEnableStateChanged'

    def __init__(self):
        self.emoteFunc = None

    def isEnabled(self, index):
        if isinstance(index, types.StringType):
            index = EmoteFuncDict[index]
        if self.emoteFunc == None:
            return 0
        elif self.emoteFunc[index][1] == 0:
            return 1
        return 0

globalEmote = None
