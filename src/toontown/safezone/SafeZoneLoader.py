from panda3d.core import ModelPool, NodePath, Texture, TexturePool
from toontown.base.ToonBaseGlobal import *
from toontown.distributed.ToontownMsgTypes import *
from toontown.hood import ZoneUtil
from direct.directnotify import DirectNotifyGlobal
from toontown.hood import Place
from direct.showbase import DirectObject
from direct.fsm import StateData
from direct.fsm import ClassicFSM, State
from direct.fsm import State
from direct.task import Task
from toontown.toon import HealthForceAcknowledge
from toontown.toon.Toon import teleportDebug
from toontown.base.ToontownGlobals import *
from toontown.building import ToonInterior
from toontown.cogtower import CogTowerInterior
from toontown.hood import QuietZoneState
from toontown.dna.DNAParser import *
from direct.stdpy.file import *

class SafeZoneLoader(StateData.StateData):
    notify = DirectNotifyGlobal.directNotify.newCategory('SafeZoneLoader')

    def __init__(self, hood, parentFSMState, doneEvent):
        StateData.StateData.__init__(self, doneEvent)
        self.hood = hood
        self.parentFSMState = parentFSMState
        self.fsm = ClassicFSM.ClassicFSM('SafeZoneLoader', [State.State('start', self.enterStart, self.exitStart, ['quietZone', 'playground', 'toonInterior']),
         State.State('playground', self.enterPlayground, self.exitPlayground, ['quietZone']),
         State.State('toonInterior', self.enterToonInterior, self.exitToonInterior, ['quietZone', 'cogTowerInterior']),
         State.State('cogTowerInterior', self.enterCogTowerInterior, self.exitCogTowerInterior, ['quietZone', 'playground']),
         State.State('quietZone', self.enterQuietZone, self.exitQuietZone, ['playground', 'toonInterior', 'cogTowerInterior']),
         State.State('golfcourse', self.enterGolfcourse, self.exitGolfcourse, ['quietZone', 'playground']),
         State.State('final', self.enterFinal, self.exitFinal, ['start'])], 'start', 'final')
        self.placeDoneEvent = 'placeDone'
        self.place = None
        self.playgroundClass = None
        return

    def load(self):
        self.music = loader.loadMusic(self.musicFile)
        self.activityMusic = loader.loadMusic(self.activityMusicFile)
        self.createSafeZone(self.dnaFile)
        self.parentFSMState.addChild(self.fsm)

    def unload(self):
        self.parentFSMState.removeChild(self.fsm)
        del self.parentFSMState
        self.geom.removeNode()
        del self.geom
        del self.fsm
        del self.hood
        del self.nodeList
        del self.playgroundClass
        del self.music
        del self.activityMusic
        del self.holidayPropTransforms
        self.deleteAnimatedProps()
        self.ignoreAll()
        ModelPool.garbageCollect()
        TexturePool.garbageCollect()

    def enter(self, requestStatus):
        self.fsm.enterInitialState()
        messenger.send('enterSafeZone')
        self.setState(requestStatus['where'], requestStatus)
        if not base.config.GetBool('want-parties', True):
            partyGate = self.geom.find('**/prop_party_gate_DNARoot')
            if not partyGate.isEmpty():
                partyGate.removeNode()

    def exit(self):
        messenger.send('exitSafeZone')

    def setState(self, stateName, requestStatus):
        self.fsm.request(stateName, [requestStatus])

    def createSafeZone(self, dnaFile):
        if self.safeZoneStorageDNAFile:
            dnaBulk = DNABulkLoader(self.hood.dnaStore, (self.safeZoneStorageDNAFile,))
            dnaBulk.loadDNAFiles()
        node = loadDNAFile(self.hood.dnaStore, dnaFile)
        if node.getNumParents() == 1:
            self.geom = NodePath(node.getParent(0))
            self.geom.reparentTo(hidden)
        else:
            self.geom = hidden.attachNewNode(node)
        self.makeDictionaries(self.hood.dnaStore)
        self.createAnimatedProps(self.nodeList)
        self.holidayPropTransforms = {}
        npl = self.geom.findAllMatches('**/=DNARoot=holiday_prop')
        for i in xrange(npl.getNumPaths()):
            np = npl.getPath(i)
            np.setTag('transformIndex', `i`)
            self.holidayPropTransforms[i] = np.getNetTransform()
        gsg = base.win.getGsg()
        if gsg:
            self.geom.prepareScene(gsg)
        self.geom.flattenMedium()

    def makeDictionaries(self, dnaStore):
        self.nodeList = []
        for i in xrange(dnaStore.getNumDNAVisGroups()):
            groupFullName = dnaStore.getDNAVisGroupName(i)
            groupName = base.cr.hoodMgr.extractGroupName(groupFullName)
            groupNode = self.geom.find('**/' + groupFullName)
            if groupNode.isEmpty():
                self.notify.error('Could not find visgroup')
            groupNode.flattenMedium()
            self.nodeList.append(groupNode)

        self.removeLandmarkBlockNodes()
        self.hood.dnaStore.resetPlaceNodes()
        self.hood.dnaStore.resetDNAGroups()
        self.hood.dnaStore.resetDNAVisGroups()
        self.hood.dnaStore.resetDNAVisGroupsAI()

    def removeLandmarkBlockNodes(self):
        npc = self.geom.findAllMatches('**/suit_building_origin')
        for i in xrange(npc.getNumPaths()):
            npc.getPath(i).removeNode()

    def enterStart(self):
        pass

    def exitStart(self):
        pass

    def enterPlayground(self, requestStatus):
        self.acceptOnce(self.placeDoneEvent, self.handlePlaygroundDone)
        self.place = self.playgroundClass(self, self.fsm, self.placeDoneEvent)
        self.place.load()
        self.place.enter(requestStatus)
        base.cr.playGame.setPlace(self.place)

    def exitPlayground(self):
        self.ignore(self.placeDoneEvent)
        self.place.exit()
        self.place.unload()
        self.place = None
        base.cr.playGame.setPlace(self.place)
        return

    def handlePlaygroundDone(self):
        status = self.place.doneStatus
        teleportDebug(status, 'handlePlaygroundDone, doneStatus=%s' % (status,))
        if ZoneUtil.getBranchZone(status['zoneId']) == self.hood.hoodId and status['shardId'] == None:
            teleportDebug(status, 'same branch')
            self.fsm.request('quietZone', [status])
        else:
            self.doneStatus = status
            teleportDebug(status, 'different hood')
            messenger.send(self.doneEvent)
        return

    def enterToonInterior(self, requestStatus):
        self.acceptOnce(self.placeDoneEvent, self.handleToonInteriorDone)
        self.place = ToonInterior.ToonInterior(self, self.fsm.getStateNamed('toonInterior'), self.placeDoneEvent)
        base.cr.playGame.setPlace(self.place)
        self.place.load()
        self.place.enter(requestStatus)

    def exitToonInterior(self):
        self.ignore(self.placeDoneEvent)
        self.place.exit()
        self.place.unload()
        self.place = None
        base.cr.playGame.setPlace(self.place)
        return

    def handleToonInteriorDone(self):
        status = self.place.doneStatus
        if ZoneUtil.getBranchZone(status['zoneId']) == self.hood.hoodId and status['shardId'] == None:
            self.fsm.request('quietZone', [status])
        elif status['where'] == 'cogTowerInterior':
            self.fsm.request('quietZone', [status])
        else:
            self.doneStatus = status
            messenger.send(self.doneEvent)
        return
		
    def enterCogTowerInterior(self, requestStatus):
        self.acceptOnce(self.placeDoneEvent, self.handleCogTowerInteriorDone)
        self.place = CogTowerInterior.CogTowerInterior(self, self.fsm, self.placeDoneEvent)
        base.cr.playGame.setPlace(self.place)
        self.place.load()
        self.place.enter(requestStatus)
		
    def exitCogTowerInterior(self):
        self.ignore(self.placeDoneEvent)
        self.place.exit()
        self.place.unload()
        self.place = None
        base.cr.playGame.setPlace(self.place)
		
    def handleCogTowerInteriorDone(self):
        status = self.place.doneStatus
        if ZoneUtil.getBranchZone(status['zoneId']) == self.hood.hoodId and status['shardId'] == None:
            self.fsm.request('quietZone', [status])
        else:
            self.doneStatus = status
            messenger.send(self.doneEvent)

    def enterQuietZone(self, requestStatus):
        self.quietZoneDoneEvent = uniqueName('quietZoneDone')
        self.acceptOnce(self.quietZoneDoneEvent, self.handleQuietZoneDone)
        self.quietZoneStateData = QuietZoneState.QuietZoneState(self.quietZoneDoneEvent)
        self.quietZoneStateData.load()
        self.quietZoneStateData.enter(requestStatus)

    def exitQuietZone(self):
        self.ignore(self.quietZoneDoneEvent)
        del self.quietZoneDoneEvent
        self.quietZoneStateData.exit()
        self.quietZoneStateData.unload()
        self.quietZoneStateData = None
        return

    def handleQuietZoneDone(self):
        status = self.quietZoneStateData.getRequestStatus()
        if status['where'] == 'estate':
            self.doneStatus = status
            messenger.send(self.doneEvent)
        else:
            self.fsm.request(status['where'], [status])

    def enterFinal(self):
        pass

    def exitFinal(self):
        pass

    def createAnimatedProps(self, nodeList):
        self.animPropDict = {}
        for i in nodeList:
            animPropNodes = i.findAllMatches('**/animated_prop_*')
            numAnimPropNodes = animPropNodes.getNumPaths()
            for j in xrange(numAnimPropNodes):
                animPropNode = animPropNodes.getPath(j)
                if animPropNode.getName().startswith('animated_prop_generic'):
                    className = 'GenericAnimatedProp'
                else:
                    className = animPropNode.getName()[14:-8]
                symbols = {}
                base.cr.importModule(symbols, 'toontown.hood', [className])
                classObj = getattr(symbols[className], className)
                animPropObj = classObj(animPropNode)
                animPropList = self.animPropDict.setdefault(i, [])
                animPropList.append(animPropObj)

    def deleteAnimatedProps(self):
        for zoneNode, animPropList in self.animPropDict.items():
            for animProp in animPropList:
                animProp.delete()

        del self.animPropDict

    def enterAnimatedProps(self, zoneNode):
        for animProp in self.animPropDict.get(zoneNode, ()):
            animProp.enter()

    def exitAnimatedProps(self, zoneNode):
        for animProp in self.animPropDict.get(zoneNode, ()):
            animProp.exit()

    def enterGolfcourse(self, requestStatus):
        base.transitions.fadeOut(t=0)

    def exitGolfcourse(self):
        pass
