from panda3d.core import NodePath, Texture
from direct.directnotify.DirectNotifyGlobal import *
from direct.showbase import Loader
from toontown.gui import ToontownLoadingScreen
from toontown.dna.DNAParser import *

class ToontownLoader(Loader.Loader):

    def __init__(self, base):
        Loader.Loader.__init__(self, base)
        self.inBulkBlock = None
        self.textureCache = {}
        self.fontCache = {}
        self.musicCache = {}
        self.sfxCache = {}
        self.modelCache = {}
        self.loadingScreen = ToontownLoadingScreen.ToontownLoadingScreen()

    def destroy(self):
        self.loadingScreen.destroy()
        del self.loadingScreen
        del self.textureCache
        del self.fontCache
        del self.sfxCache
        del self.musicCache
        del self.modelCache
        Loader.Loader.destroy(self)

    def loadDNAFile(self, dnastore, filename):
        return loadDNAFile(dnastore, filename)

    def beginBulkLoad(self, name, label, range, gui, tipCategory, zoneId):
        if self.inBulkBlock:
            return
        self.inBulkBlock = True
        self.loadingScreen.begin(label, gui, tipCategory, zoneId)

    def endBulkLoad(self, name):
        if not self.inBulkBlock:
            return
        self.inBulkBlock = False
        self.loadingScreen.end()

    def tick(self):
        if self.inBulkBlock:
            base.graphicsEngine.renderFrame()

    def loadModel(self, *args, **kw):
        modelName = args[0]
        self.tick()
        if modelName in self.modelCache:
            model = self.modelCache[modelName]
        else:
            kw['noCache'] = True
            model = Loader.Loader.loadModel(self, *args, **kw)
            if not model:
                return
            model = model.node()
            self.modelCache[modelName] = model
        return NodePath(model.copySubgraph())

    def loadFont(self, *args, **kw):
        fontId = (args[0], frozenset(kw.items()))
        if fontId not in self.fontCache:
            font = Loader.Loader.loadFont(self, *args, **kw)
            self.fontCache[fontId] = font
            return font
        else:
            return self.fontCache[fontId]

    def loadTexture(self, texturePath, alphaPath = None, okMissing = False):
        textureId = (texturePath, alphaPath)
        if textureId not in self.textureCache:
            texture = Loader.Loader.loadTexture(self, texturePath, alphaPath, okMissing=okMissing)
            self.textureCache[textureId] = texture
            return texture
        else:
            return self.textureCache[textureId]

    def loadSfx(self, soundPath):
        if soundPath not in self.sfxCache:
            sfx = Loader.Loader.loadSfx(self, soundPath)
            self.sfxCache[soundPath] = sfx
            return sfx
        else:
            return self.sfxCache[soundPath]
        
    def loadMusic(self, soundPath):
        if soundPath not in self.musicCache:
            sound = Loader.Loader.loadMusic(self, soundPath)
            self.musicCache[soundPath] = sound
            return sound
        else:
            return self.musicCache[soundPath]
