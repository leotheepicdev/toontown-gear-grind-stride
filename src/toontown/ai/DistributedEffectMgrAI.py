from direct.distributed.DistributedObjectAI import DistributedObjectAI
import HolidayGlobals

class DistributedEffectMgrAI(DistributedObjectAI):

    def __init__(self, air, holiday, effectId):
        DistributedObjectAI.__init__(self, air)
        self.holiday = holiday
        self.effectId = effectId

    def getHoliday(self):
        return self.holiday

    def requestEffect(self):
        if not self.air.newsManager.isHolidayRunning(self.holiday):
            return
        avId = self.air.getAvatarIdFromSender()
        av = self.air.doId2do.get(avId)
        if not av:
            return
        holidayInfo = HolidayGlobals.getHoliday(self.holiday)
        if 'scavengerHunt' in holidayInfo:
            scavengerHunt = av.getScavengerHunt()
            if self.zoneId in scavengerHunt:
                self.sendUpdateToAvatarId(avId, 'effectDone', [0])
            else:
                scavengerHunt.append(self.zoneId)
                av.b_setScavengerHunt(scavengerHunt)
                av.addMoney(HolidayGlobals.CAROLING_REWARD)
                self.sendUpdateToAvatarId(avId, 'effectDone', [HolidayGlobals.CAROLING_REWARD])
            if len(scavengerHunt) == HolidayGlobals.SCAVENGER_HUNT_LOCATIONS:
                av.addCheesyEffect(self.effectId)
        else:
            av.addCheesyEffect(self.effectId)
            self.sendUpdateToAvatarId(avId, 'effectDone', [0])
