from panda3d.core import Point3, Vec3, Vec4
GlobalEntities = {1000: {'type': 'levelMgr',
        'name': 'LevelMgr',
        'comment': '',
        'parentEntId': 0,
        'cogLevel': 0,
        'farPlaneDistance': 1500,
        'modelFilename': 'phase_12/models/bossbotHQ/BossbotGreenRoom_A',
        'wantDoors': 1},
 0: {'type': 'zone',
     'name': 'UberZone',
     'comment': '',
     'parentEntId': 0,
     'scale': 1,
     'description': '',
     'visibility': []},
 110301: {'type': 'door',
          'name': '<unnamed>',
          'comment': '',
          'parentEntId': 110303,
          'pos': Point3(0, 0, 0),
          'hpr': Vec3(0, 0, 0),
          'scale': 1,
          'color': Vec4(1, 1, 1, 1),
          'isLock0Unlocked': 1,
          'isLock1Unlocked': 0,
          'isLock2Unlocked': 1,
          'isLock3Unlocked': 1,
          'isOpen': 0,
          'isOpenEvent': 0,
          'isVisBlocker': 0,
          'secondsOpen': 1,
          'unlock0Event': 0,
          'unlock1Event': 110302,
          'unlock2Event': 0,
          'unlock3Event': 0},
 110302: {'type': 'golfGreenGame',
          'name': '<unnamed>',
          'comment': '',
          'parentEntId': 0,
          'pos': Point3(0, 0, 0),
          'hpr': Vec3(0, 0, 0),
          'scale': 1,
          'puzzleBase': 3,
          'puzzlePerPlayer': 2,
          'timeToPlay': 140,
          'cellId': 0,
          'switchId': 0},
 10002: {'type': 'nodepath',
         'name': 'props',
         'comment': '',
         'parentEntId': 0,
         'pos': Point3(0, 0, 0),
         'hpr': Vec3(0, 0, 0),
         'scale': 1},
 110303: {'type': 'nodepath',
          'name': '<unnamed>',
          'comment': '',
          'parentEntId': 0,
          'pos': Point3(40.9635, 2, 0),
          'hpr': Vec3(270, 0, 0),
          'scale': Vec3(1, 1, 1)}}
Scenario0 = {}
levelSpec = {'globalEntities': GlobalEntities,
 'scenarios': [Scenario0]}
