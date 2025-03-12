import CatalogItem
from toontown.base import TTLocalizer
from direct.showbase import PythonUtil
from toontown.base import ToontownGlobals

class CatalogInvalidItem(CatalogItem.CatalogItem):

    def requestPurchase(self, phone, callback):
        self.notify.error('Attempt to purchase invalid item.')

    def acceptItem(self, mailbox, index, callback):
        self.notify.error('Attempt to accept invalid item.')

    def output(self, store = -1):
        return 'CatalogInvalidItem()'
