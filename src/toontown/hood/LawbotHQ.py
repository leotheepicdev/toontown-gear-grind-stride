from panda3d.core import Lens
from toontown.coghq.LawbotCogHQLoader import LawbotCogHQLoader
from toontown.base import ToontownGlobals
from toontown.hood.CogHood import CogHood


class LawbotHQ(CogHood):
    notify = directNotify.newCategory('LawbotHQ')

    ID = ToontownGlobals.LawbotHQ
    LOADER_CLASS = LawbotCogHQLoader

    def load(self):
        CogHood.load(self)

        self.sky.hide()

    def enter(self, requestStatus):
        CogHood.enter(self, requestStatus)

        base.localAvatar.setCameraFov(ToontownGlobals.CogHQCameraFov)
        base.camLens.setNearFar(ToontownGlobals.LawbotHQCameraNear, ToontownGlobals.LawbotHQCameraFar)
