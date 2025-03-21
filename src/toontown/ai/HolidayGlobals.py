from toontown.base import ToontownGlobals, TTLocalizer
from toontown.parties import ToontownTimeZone
import calendar, datetime

TIME_ZONE = ToontownTimeZone.ToontownTimeZone()
TRICK_OR_TREAT = 0
WINTER_CAROLING = 1
CAROLING_REWARD = 100
SCAVENGER_HUNT_LOCATIONS = 6

Holidays = {
    ToontownGlobals.GRAND_PRIX: {
        'weekDay': 0,
        'startMessage': TTLocalizer.CircuitRaceStart,
        'ongoingMessage': TTLocalizer.CircuitRaceOngoing,
        'endMessage': TTLocalizer.CircuitRaceEnd
    },
    ToontownGlobals.MORE_MERITS_HOLIDAY: {
        'weekDay': 0,
        'startMessage': TTLocalizer.MoreMeritsHolidayStart,
        'ongoingMessage': TTLocalizer.MoreMeritsHolidayOngoing,
        'endMessage': TTLocalizer.MoreMeritsHolidayOngoing
    },
    ToontownGlobals.FISH_BINGO: {
        'weekDay': 2,
        'startMessage': TTLocalizer.FishBingoStart,
        'ongoingMessage': TTLocalizer.FishBingoOngoing,
        'endMessage': TTLocalizer.FishBingoEnd
    },
    ToontownGlobals.MORE_XP_HOLIDAY: {
        'weekDay': 4,
        'startMessage': TTLocalizer.MoreXpHolidayStart,
        'ongoingMessage': TTLocalizer.MoreXpHolidayOngoing,
        'endMessage': TTLocalizer.MoreXpHolidayEnd
    },
    ToontownGlobals.SILLY_SATURDAY: {
        'weekDay': 5,
        'startMessage': TTLocalizer.SillySaturdayStart,
        'ongoingMessage': TTLocalizer.SillySaturdayOngoing,
        'endMessage': TTLocalizer.SillySaturdayEnd
    },
    ToontownGlobals.BLACK_TOON_DAY: {
        'startMonth': 10,
        'startDay': 31,
        'endMonth': 11,
        'endDay': 1,
        'startMessage': TTLocalizer.BlackToonHolidayStart,
        'ongoingMessage': TTLocalizer.BlackToonHolidayStart,
        'endMessage': TTLocalizer.BlackToonHolidayEnd
    },
    ToontownGlobals.APRIL_TOONS_WEEK: {
        'startMonth': 4,
        'startDay': 1,
        'endMonth': 4,
        'endDay': 7,
        'startMessage': TTLocalizer.AprilToonsWeekStart,
        'ongoingMessage': TTLocalizer.AprilToonsWeekStart,
        'endMessage': TTLocalizer.AprilToonsWeekEnd
    },
    ToontownGlobals.IDES_OF_MARCH: {
        'startMonth': 3,
        'startDay': 14,
        'endMonth': 3,
        'endDay': 20,
        'startMessage': TTLocalizer.IdesOfMarchStart,
        'ongoingMessage': TTLocalizer.IdesOfMarchStart,
        'endMessage': TTLocalizer.IdesOfMarchEnd,
        'speedchatIndexes': [30450], # It's easy to be green!
        'effectMessage': TTLocalizer.GreenToonEffectMsg,
        'effectDelay': 10
    },
    ToontownGlobals.TAX_DAY_INVASION: {
        'startMonth': 4,
        'startDay': 15,
        'endMonth': 4,
        'endDay': 16,
        'startMessage': TTLocalizer.TaxDayHolidayStart,
        'ongoingMessage': TTLocalizer.TaxDayHolidayOngoing,
        'endMessage': TTLocalizer.TaxDayHolidayEnd
    },
    ToontownGlobals.CHRISTMAS: {
        'startMonth': 12,
        'startDay': 14,
        'endMonth': 1,
        'endDay': 4,
        'startMessage': TTLocalizer.WinterCarolingStart,
        'ongoingMessage': TTLocalizer.WinterCarolingStart,
        'endMessage': TTLocalizer.WinterCarolingEnd,
        'speedchatIndexes': range(30200, 30206),
        'effectDelay': 15,
        'scavengerHunt': WINTER_CAROLING
    },
    ToontownGlobals.HALLOWEEN: {
        'startMonth': 10,
        'startDay': 13,
        'endMonth': 11,
        'endDay': 1,
        'startMessage': TTLocalizer.TrickOrTreatStart,
        'ongoingMessage': TTLocalizer.TrickOrTreatStart,
        'endMessage': TTLocalizer.TrickOrTreatEnd,
        'speedchatIndexes': [10003],
        'effectDelay': 15,
        'scavengerHunt': TRICK_OR_TREAT
    },
    ToontownGlobals.SUMMER_FIREWORKS: {
        'startMonth': 6,
        'startDay': 30,
        'endMonth': 7,
        'endDay': 15,
        'startMessage': TTLocalizer.SummerFireworksStart,
        'ongoingMessage': TTLocalizer.SummerFireworksStart,
        'endMessage': TTLocalizer.SummerFireworksEnd
    },
    ToontownGlobals.NEW_YEAR_FIREWORKS: {
        'startMonth': 12,
        'startDay': 31,
        'endMonth': 1,
        'endDay': 7,
        'startMessage': TTLocalizer.NewYearFireworksStart,
        'ongoingMessage': TTLocalizer.NewYearFireworksStart,
        'endMessage': TTLocalizer.NewYearFireworksEnd
    },
    ToontownGlobals.VALENTOONS_DAY: {
        'startMonth': 2,
        'startDay': 9,
        'endMonth': 2,
        'endDay': 16,
        'startMessage': TTLocalizer.ValentinesDayStart,
        'ongoingMessage': TTLocalizer.ValentinesDayStart,
        'endMessage': TTLocalizer.ValentinesDayEnd
    }
}

# Dept, Rank
# Dept: 0-3 = Bossbot-Lawbot-Cashbot-Sellbot
# Suit Rank: 0-7 = Rank 1 to 8
Holidays2Cog = {
 ToontownGlobals.BLACK_TOON_DAY: (1, 1), # Bloodsucker
 ToontownGlobals.IDES_OF_MARCH: (1, 4), # Back Stabber
 ToontownGlobals.TAX_DAY_INVASION: (2, 4), # Number Cruncher
 ToontownGlobals.VALENTOONS_DAY: (3, 6) # The Mingler
}

def getHoliday(id):
    return Holidays.get(id, {})

def getServerTime(date):
    epoch = datetime.datetime.fromtimestamp(0, TIME_ZONE)
    delta = date - epoch

    return delta.total_seconds()

def getStartDate(holiday, rightNow=None):
    if not rightNow:
        rightNow = datetime.datetime.now()

    startMonth = holiday['startMonth'] if 'startMonth' in holiday else rightNow.month
    startDay = holiday['startDay'] if 'startDay' in holiday else (rightNow.day if 'weekDay' in holiday else calendar.monthrange(rightNow.year, startMonth)[0])
    startDate = datetime.datetime(rightNow.year, startMonth, startDay, tzinfo=TIME_ZONE)

    return startDate

def getEndDate(holiday, rightNow=None):
    if not rightNow:
        rightNow = datetime.datetime.now()

    endMonth = holiday['endMonth'] if 'endMonth' in holiday else rightNow.month
    endDay = holiday['endDay'] if 'endDay' in holiday else (rightNow.day if 'weekDay' in holiday else calendar.monthrange(rightNow.year, endMonth)[1])
    endYear = rightNow.year

    if 'startMonth' in holiday and holiday['startMonth'] > endMonth:
        endYear += 1

    endDate = datetime.datetime(endYear, endMonth, endDay, tzinfo=TIME_ZONE)

    return endDate
