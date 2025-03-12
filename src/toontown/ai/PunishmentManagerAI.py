from panda3d.core import Datagram
from direct.directnotify import DirectNotifyGlobal
import time
from direct.fsm.FSM import FSM
from direct.distributed.PyDatagram import PyDatagram
from direct.distributed.MsgTypes import *
from toontown.magicword.MagicWordGlobal import *
from direct.showbase.DirectObject import DirectObject


class BanFSM(FSM):

    def __init__(self, air, avId, comment, duration, banner):
        FSM.__init__(self, 'banFSM-%s' % avId)
        self.air = air
        self.avId = avId

        # Needed variables for the actual banning.
        self.comment = comment
        self.duration = duration
        self.DISLid = None
        self.accountId = None
        self.avName = None
        self.banner = banner

    def performBan(self, duration):
        print("TODO: Rewrite banning system.")

    def ejectPlayer(self):
        av = self.air.doId2do.get(self.avId)
        if not av:
            return

        # Send the client a 'CLIENTAGENT_EJECT' with the players name.
        datagram = PyDatagram()
        datagram.addServerHeader(
                av.GetPuppetConnectionChannel(self.avId),
                self.air.ourChannel, CLIENTAGENT_EJECT)
        datagram.addUint16(152)
        datagram.addString(self.avName)
        simbase.air.send(datagram)

    def dbCallback(self, dclass, fields):
        if dclass != simbase.air.dclassesByName['AccountAI']:
            return

        self.accountId = fields.get('ACCOUNT_ID')

        if not self.accountId:
            return

        if simbase.config.GetBool('want-bans', True):
            self.performBan(self.duration)
            self.duration = None

    def getAvatarDetails(self):
        av = self.air.doId2do.get(self.avId)
        if not av:
            return

        self.DISLid = av.getDISLid()
        self.avName = av.getName()

    def log(self):
        simbase.air.writeServerEvent('ban', self.accountId, self.comment)

    def cleanup(self):
        self.air = None
        self.avId = None

        self.DISLid = None
        self.avName = None
        self.accountId = None
        self.comment = None
        self.duration = None
        self = None

    def enterStart(self):
        self.getAvatarDetails()
        self.air.dbInterface.queryObject(self.air.dbId, self.DISLid,
                                         self.dbCallback)
        self.ejectPlayer()

    def exitStart(self):
        self.log()
        self.cleanup()

    def enterOff(self):
        pass

    def exitOff(self):
        pass


class PunishmentManagerAI(DirectObject):
    notify = DirectNotifyGlobal.directNotify.newCategory('PunishmentManagerAI')

    def __init__(self, air):
        self.air = air
        self.banFSMs = {}

    def ban(self, avId, duration, comment, banner):
        self.banFSMs[avId] = BanFSM(self.air, avId, comment, duration, banner)
        self.banFSMs[avId].request('Start')

        self.acceptOnce(self.air.getAvatarExitEvent(avId), self.banDone, [avId])

    def banDone(self, avId):
        self.banFSMs[avId].request('Off')
        self.banFSMs[avId] = None
		
    def kick(self, avId, reason, reasonString):
        av = self.air.doId2do.get(avId)
        if not av:
            return
        if av.avBeingEjected:
            # The av is already being ejected. No need to send multiple messages
            return
        datagram = PyDatagram()
        datagram.addServerHeader(av.GetPuppetConnectionChannel(avId), self.air.ourChannel, CLIENTAGENT_EJECT)
        datagram.addUint16(reason)
        datagram.addString(reasonString)
        simbase.air.send(datagram)
        if av:
            av.avBeingEjected = True
			
    def warn(self, avId, reason):
        av = self.air.doId2do.get(avId)
        if not av:
            return
        av.sendUpdate('warnToon', [reason])

@magicWord(category=CATEGORY_MODERATOR, types=[str])
def kick(reason='No reason specified'):
    """
    Kick the target from the game server.
    """
    target = spellbook.getTarget()
    simbase.air.punishmentManager.kick(target.doId, 155, 'You were kicked by a moderator for the following reason: %s' % reason)
    return "Kicked %s from the game server!" % target.getName()

@magicWord(category=CATEGORY_MODERATOR, types=[str, int])
def ban(reason, duration):
    """
    Ban the target from the game server.
    """
    target = spellbook.getTarget()
    if target == spellbook.getInvoker():
        return "You can't ban yourself!"
    banner = spellbook.getInvoker().DISLid
    simbase.air.punishmentManager.ban(target.doId, duration, reason, banner)
    return "Banned %s from the game server!" % target.getName()
	
@magicWord(category=CATEGORY_MODERATOR, types=[str])
def warn(reason='No reason specified'):
    """
    Warn target. We would rather do this than annoy people with kicks.
    """
    target = spellbook.getTarget()
    simbase.air.punishmentManager.warn(target.doId, reason)
    return "%s has been warned for %s!" % (target.getName(), reason)
