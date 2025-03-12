from toontown.safezone import Playground

class WWPlayground(Playground.Playground):
    def enter(self, requestStatus):
        Playground.Playground.enter(self, requestStatus)

    def exit(self):
        Playground.Playground.exit(self)
