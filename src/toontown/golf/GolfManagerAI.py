from direct.directnotify.DirectNotifyGlobal import *
from toontown.golf import DistributedGolfCourseAI

class GolfManagerAI:
    notify = directNotify.newCategory('GolfManagerAI')

    def __init__(self):
        self.courseList = []
        self.requestHole = {}

    def readyGolfCourse(self, avIds, courseId = 0):
        self.notify.debug('readyGolfCourse avIds=%s courseId=%d' % (avIds, courseId))
        golfZone = simbase.air.allocateZone()
        preferredHoleId = None
        for avId in avIds:
            if avId in self.requestHole:
                preferredHoleId = self.requestHole[avId][0]
        newCourse = DistributedGolfCourseAI.DistributedGolfCourseAI(
            golfZone, avIds, courseId, preferredHoleId)
        newCourse.generateWithRequired(golfZone)
        self.courseList.append(newCourse)
        return golfZone

    def removeCourse(self, course):
        if course in self.courseList:
            for avId in course.avIdList:
                if avId in self.requestHole:
                    if not self.requestHole[avId][1]:
                        del self.requestHole[avId]
            self.courseList.remove(course)
