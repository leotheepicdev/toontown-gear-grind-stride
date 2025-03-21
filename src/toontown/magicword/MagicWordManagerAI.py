from panda3d.core import Datagram
from direct.directnotify import DirectNotifyGlobal
from direct.distributed.DistributedObjectAI import DistributedObjectAI
from toontown.magicword.MagicWordGlobal import *
from direct.distributed.PyDatagram import PyDatagram
from direct.distributed.MsgTypes import *
from toontown.toon.DistributedToonAI import DistributedToonAI
import time

class MagicWordManagerAI(DistributedObjectAI):
    notify = DirectNotifyGlobal.directNotify.newCategory("MagicWordManagerAI")
    notify.setInfo(True)

    def sendMagicWord(self, word, targetId):
        invokerId = self.air.getAvatarIdFromSender()
        invoker = self.air.doId2do.get(invokerId)

        if not isinstance(self.air.doId2do.get(targetId), DistributedToonAI):
            self.sendUpdateToAvatarId(invokerId, 'sendMagicWordResponse', ['Target is not a toon object!'])
            return

        if not invoker:
            self.sendUpdateToAvatarId(invokerId, 'sendMagicWordResponse', ['missing invoker'])
            return

        if not invoker.isAdmin():
            self.air.writeServerEvent('suspicious', invokerId, 'Attempted to issue magic word: %s' % word)
            dg = PyDatagram()
            dg.addServerHeader(self.GetPuppetConnectionChannel(invokerId), self.air.ourChannel, CLIENTAGENT_EJECT)
            dg.addUint16(102)
            dg.addString('Magic Words are reserved for administrators only!')
            self.air.send(dg)
            return

        target = self.air.doId2do.get(targetId)
        if not target:
            self.sendUpdateToAvatarId(invokerId, 'sendMagicWordResponse', ['missing target'])
            return

        response = spellbook.process(invoker, target, word)
        if response:
            self.sendUpdateToAvatarId(invokerId, 'sendMagicWordResponse', [response])

        now = time.strftime("%c")
        with open('data/magic-words.txt', 'a') as f:
            msg = ('[{0}]: invokerId=({1}, {2}), targetId=({3}, {4}), word={5}').format(now, invokerId, invoker.getAdminAccess(), targetId, target.getAdminAccess(), word)
            self.notify.info(msg)
            f.write(msg + '\n')

@magicWord(category=CATEGORY_COMMUNITY_MANAGER, types=[str])
def help(wordName=None):
    if not wordName:
        return "What were you interested getting help for?"
    word = spellbook.words.get(wordName.lower())
    if not word:
        accessLevel = spellbook.getInvoker().getAdminAccess()
        wname = wordName.lower()
        for key in spellbook.words:
            if spellbook.words.get(key).access <= accessLevel:
                if wname in key:
                    return 'Did you mean %s' % (spellbook.words.get(key).name)
        return 'I have no clue what %s is referring to' % (wordName)
    return word.doc

@magicWord(category=CATEGORY_COMMUNITY_MANAGER, types=[])
def words():
    accessLevel = spellbook.getInvoker().getAdminAccess()
    wordString = None
    for key in spellbook.words:
        word = spellbook.words.get(key)
        if word.access <= accessLevel:
            if wordString is None:
                wordString = key
            else:
                wordString += ", ";
                wordString += key;
    if wordString is None:
        return "You are chopped liver"
    else:
        return wordString
            

