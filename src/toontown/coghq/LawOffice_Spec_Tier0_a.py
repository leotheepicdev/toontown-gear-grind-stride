from panda3d.core import Point3, Vec3


GlobalEntities = {
    1000: {
        'type': 'levelMgr',
        'name': 'LevelMgr',
        'comment': '',
        'parentEntId': 0,
        'cogLevel': 0,
        'farPlaneDistance': 1500,
        'modelFilename': 'phase_10/models/lawbotHQ/LawbotCourtroom3',
        'wantDoors': 1 },
    0: {
        'type': 'zone',
        'name': 'UberZone',
        'comment': '',
        'parentEntId': 0,
        'scale': 1,
        'description': '',
        'visibility': [] },
    100000: {
        'type': 'laserField',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 0,
        'pos': Point3(68.722499999999997, -27.415400000000002, 71),
        'hpr': Vec3(0, 0, 0),
        'scale': Vec3(1, 1, 1),
        'laserFactor': 3,
        'modelPath': 0 } }
Scenario0 = { }
levelSpec = {
    'globalEntities': GlobalEntities,
    'scenarios': [
        Scenario0] }
