from toontown.safezone import SafeZoneLoader
from toontown.safezone import CZPlayground
from direct.gui import DirectGui
from panda3d.core import *
from direct.distributed.DistributedObjectAI import DistributedObjectAI
from toontown.base import TTLocalizer
from toontown.base import ToontownGlobals
from direct.distributed.ClockDelta import *
from direct.interval.IntervalGlobal import *
import random
from toontown.hood import ZoneUtil
from direct.fsm import ClassicFSM, State
from direct.fsm import State
from direct.directnotify import DirectNotifyGlobal
from pandac.PandaModules import NodePath
from toontown.toon import NPCToons, Toon
from toontown.pets import Pet
from direct.task.Task import Task
from direct.actor.Actor import Actor


class CZSafeZoneLoader(SafeZoneLoader.SafeZoneLoader):

    def __init__(self, hood, parentFSM, doneEvent):
        SafeZoneLoader.SafeZoneLoader.__init__(self, hood, parentFSM, doneEvent)
        self.playgroundClass = CZPlayground.CZPlayground
        self.musicFile = 'phase_14/audio/bgm/CZ_nbrhood.ogg'
        self.activityMusicFile = 'phase_14/audio/bgm/CZ_SZ_activity.ogg'
        self.dnaFile = 'phase_14/dna/construction_zone_sz.pdna'
        self.safeZoneStorageDNAFile = 'phase_14/dna/storage_CZ_sz.pdna'


    def load(self):
        SafeZoneLoader.SafeZoneLoader.load(self)
       
        self.underwaterSound = base.loader.loadSfx('phase_4/audio/sfx/AV_ambient_water.ogg')
        self.swimSound = base.loader.loadSfx('phase_4/audio/sfx/AV_swim_single_stroke.ogg')
        self.submergeSound = base.loader.loadSfx('phase_5.5/audio/sfx/AV_jump_in_water.ogg')

        water = self.geom.find('**/water')

        self.birdSound = map(base.loader.loadSfx, ['phase_4/audio/sfx/SZ_TC_bird1.ogg',
                                            'phase_4/audio/sfx/SZ_TC_bird2.ogg',
                                            'phase_4/audio/sfx/SZ_TC_bird3.ogg'])

    
    def unload(self):
        SafeZoneLoader.SafeZoneLoader.unload(self)
  
        del self.underwaterSound
        del self.swimSound
        del self.submergeSound
        del self.birdSound       
       