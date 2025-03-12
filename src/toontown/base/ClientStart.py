#!/usr/bin/env python2
from panda3d.core import ConfigVariable, ConfigVariableBool, ConfigVariableDouble, ConfigVariableList, ConfigVariableString, Filename, VirtualFile, VirtualFileSystem, loadPrcFile, loadPrcFileData, NodePath
import gc
import ToontownTitleScreen

gc.disable()

import __builtin__
__builtin__.process = 'client'

import ToontownLogger
__builtin__.logger = ToontownLogger.LogWriter()

import sys, os
sys.path.append(
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            "../../lib"
        )
    )
)

if __debug__:
    loadPrcFile('config/general.prc')
    loadPrcFile('config/release/dev.prc')

if not os.path.exists('user/'):
    os.mkdir('user/')
	
for dtool in ('children', 'parent', 'name'):
    del NodePath.DtoolClassDict[dtool]

from direct.directnotify.DirectNotifyGlobal import directNotify
notify = directNotify.newCategory('ClientStart')
notify.setInfo(True)

if __debug__:
    # The VirtualFileSystem, which has already initialized, doesn't see the mount
    # directives in the config(s) yet. We have to force it to load those manually:
    vfs = VirtualFileSystem.getGlobalPtr()
    mounts = ConfigVariableList('vfs-mount')
    for mount in mounts:
        mountfile, mountpoint = (mount.split(' ', 2) + [None, None, None])[:2]
        vfs.mount(Filename(mountfile), Filename(mountpoint), 0)

from toontown.base.Settings import Settings
from otp.otpbase import OTPGlobals

preferencesFilename = ConfigVariableString('preferences-filename', 'user/preferences.json').getValue()
notify.info('Reading %s...' % preferencesFilename)
__builtin__.settings = Settings(preferencesFilename)
defaultSettings = {'res': (1280, 720),
 'fullscreen': False,
 'musicVol': 1.0,
 'sfxVol': 1.0,
 'loadDisplay': 'pandagl',
 'toonChatSounds': True,
 'language': 'English',
 'cogInterface': True,
 'speedchatPlus': True,
 'trueFriends': True,
 'fov': OTPGlobals.DefaultCameraFov,
 'fpsMeter': False,
 'ttoAspectRatio': False,
 'keybindings': {},
 'discordPresence': False,
 'automaticErrorReporting': False}

for setting, value in defaultSettings.iteritems():
    if setting not in settings:
        settings[setting] = value
del defaultSettings

loadPrcFileData('Settings: res', 'win-size %d %d' % tuple(settings['res']))
loadPrcFileData('Settings: fullscreen', 'fullscreen %s' % settings['fullscreen'])
loadPrcFileData('Settings: loadDisplay', 'load-display %s' % settings['loadDisplay'])

from toontown.launcher.TTLauncher import TTLauncher

__builtin__.launcher = TTLauncher()

try:
    sys.argv[1] == "debug"
    debugInjector = True
except:
    debugInjector = False

if __debug__ and debugInjector:
    try:
        import wx
    except:
        notify.warning('Failed to start injector - wx module missing!')
    else:
        try:
            import psutil
        except:
            notify.warning('Failed to start injector - psutil module missing!')
        else:
            from toontown.base.ToontownInjector import ToontownInjector
            notify.info('Starting injector...')
            __builtin__.injector = ToontownInjector()

notify.info('Starting the game...')
from direct.gui import DirectGuiGlobals
from direct.gui.DirectGui import *
notify.info('Setting the default font...')
import ToontownGlobals
DirectGuiGlobals.setDefaultFontFunc(ToontownGlobals.getInterfaceFont)
import ToonBase
ToonBase.ToonBase()
if settings['ttoAspectRatio']:
    base.setAspectRatio(ToontownGlobals.TTOAspectRatio)
if base.win is None:
    notify.error('Unable to open window; aborting.')
ConfigVariableDouble('decompressor-step-time').setValue(0.01)
ConfigVariableDouble('extractor-step-time').setValue(0.01)

# TODO: possibly add a background here for those with slow pcs (START) 

DirectGuiGlobals.setDefaultRolloverSound(loader.loadSfx('phase_3/audio/sfx/GUI_rollover.ogg'))
DirectGuiGlobals.setDefaultClickSound(loader.loadSfx('phase_3/audio/sfx/GUI_create_toon_fwd.ogg'))
DirectGuiGlobals.setDefaultDialogGeom(loader.loadModel('phase_3/models/gui/dialog_box_gui'))
from . import TTLocalizer
if base.musicManagerIsValid:
    for manager in base.sfxManagerList:
        manager.setVolume(settings['sfxVol'])
    base.musicManager.setVolume(settings['musicVol'])
    notify.info('Loading the default GUI sounds...')
    DirectGuiGlobals.setDefaultRolloverSound(loader.loadSfx('phase_3/audio/sfx/GUI_rollover.ogg'))
    DirectGuiGlobals.setDefaultClickSound(loader.loadSfx('phase_3/audio/sfx/GUI_create_toon_fwd.ogg'))
from . import ToontownLoader
serverVersion = base.config.GetString('server-version', 'no_version_set')
from toontown.suit import Suit
Suit.loadModels()
from direct.showbase.MessengerGlobal import *
from toontown.distributed import ToontownClientRepository
base.cr = ToontownClientRepository.ToontownClientRepository(serverVersion)
base.initNametagGlobals()
base.setFrameRateMeter(settings['fpsMeter'])
from toontown.friends import FriendManager
from toontown.distributed.ToontownDoGlobals import DO_ID_FRIEND_MANAGER
base.cr.generateGlobalObject(DO_ID_FRIEND_MANAGER, 'FriendManager')

# TODO: possibly add a background here for those with slow pcs (END)
        
base.cr.toontownTitleScreen = ToontownTitleScreen.ToontownTitleScreen()
base.loader = base.loader
__builtin__.loader = base.loader

gc.enable()
gc.collect()

try:
    base.run()
except:
    pass
