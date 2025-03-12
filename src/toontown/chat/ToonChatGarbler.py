import random
from toontown.base import TTLocalizer
		 
class ToonChatGarbler:

    def __init__(self):
        self.messages = {'default': TTLocalizer.ChatGarblerDefault,
         'dog': TTLocalizer.ChatGarblerDog,
         'cat': TTLocalizer.ChatGarblerCat,
         'mouse': TTLocalizer.ChatGarblerMouse,
         'horse': TTLocalizer.ChatGarblerHorse,
         'rabbit': TTLocalizer.ChatGarblerRabbit,
         'duck': TTLocalizer.ChatGarblerDuck,
         'monkey': TTLocalizer.ChatGarblerMonkey,
         'bear': TTLocalizer.ChatGarblerBear,
         'pig': TTLocalizer.ChatGarblerPig,
         'default': TTLocalizer.ChatGarblerDefault}
	
    def garble(self, avatar, numWords):
        newMessage = ''
        if avatar.style:
            avatarType = avatar.style.getType()
            wordList = self.messages[avatarType if avatarType in self.messages else 'default']
        for i in xrange(1, numWords + 1):
            wordIndex = random.randint(0, len(wordList) - 1)
            newMessage = newMessage + wordList[wordIndex]
            if i < numWords:
                newMessage = newMessage + ' '
        return '\x01WLDisplay\x01%s\x02' % newMessage