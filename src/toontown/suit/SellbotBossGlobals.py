from panda3d.core import Point3, Vec3

try:
    from toontown.coghq.DistributedHealBarrelAI import DistributedHealBarrelAI
    from toontown.coghq.DistributedGagBarrelAI import DistributedGagBarrelAI
except ImportError:
    DistributedHealBarrelAI = None
    DistributedGagBarrelAI = None

PieToonup = 1
PieToonupNerfed = 2
PieDamageMult = 1.0
PieDamageMultNerfed = 2.0
AttackMult = 1.0
AttackMultNerfed = 0.5
HitCountDamage = 35
HitCountDamageNerfed = 50
BarrelDefs = {
 8000: {'type': DistributedHealBarrelAI,
        'pos': Point3(15, 23, 0),
        'hpr': Vec3(-45, 0, 0),
        'rewardPerGrab': 50,
        'rewardPerGrabMax': 0},
 8001: {'type': DistributedGagBarrelAI,
        'pos': Point3(15, -23, 0),
        'hpr': Vec3(-135, 0, 0),
        'gagLevel': 3,
        'gagLevelMax': 0,
        'gagTrack': 3,
        'rewardPerGrab': 10,
        'rewardPerGrabMax': 0},
 8002: {'type': DistributedGagBarrelAI,
        'pos': Point3(21, 20, 0),
        'hpr': Vec3(-45, 0, 0),
        'gagLevel': 3,
        'gagLevelMax': 0,
        'gagTrack': 4,
        'rewardPerGrab': 10,
        'rewardPerGrabMax': 0},
 8003: {'type': DistributedGagBarrelAI,
        'pos': Point3(21, -20, 0),
        'hpr': Vec3(-135, 0, 0),
        'gagLevel': 3,
        'gagLevelMax': 0,
        'gagTrack': 5,
        'rewardPerGrab': 10,
        'rewardPerGrabMax': 0}
}

def setBarrelAttr(barrel, entId):
    for defAttr, defValue in BarrelDefs[entId].iteritems():
        setattr(barrel, defAttr, defValue)


BarrelsStartPos = (0, -36, -8)
BarrelsFinalPos = (0, -36, 0)
