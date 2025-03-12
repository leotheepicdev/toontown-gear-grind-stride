from panda3d.core import LVector3f

class PetLeash:

    def __init__(self, origin, length):
        self.origin = origin
        self.length = length

    def _process(self, dt):
        myPos = self.nodePath.getPos()
        myDist = LVector3f(myPos - self.origin.getPos()).length()
        if myDist > self.length:
            excess = myDist - self.length
            shove = LVector3f(myPos)
            shove.normalize()
            shove *= -excess
            self.mover.addShove(shove)
