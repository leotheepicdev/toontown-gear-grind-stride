from panda3d.core import VBase4

DEPT_INDEX = 0 # The dept of the cog
BODY_TYPE_INDEX = 1 # The body type of the cog
SCALE_INDEX = 2 # The scale of the cog
HAND_COLOR_INDEX = 3 # The hand color
HEADS_INDEX = 4 # A list of heads
HEAD_TEXTURE_INDEX = 5 # The texture to use for the head
HEIGHT_INDEX = 6 # The height of the cog

aSize = 6.06 # Size of body type 'a'
bSize = 5.29 # Size of body type 'b'
cSize = 4.14 # Size of body type 'c'

bossbotHandColor = VBase4(0.95, 0.75, 0.75, 1.0) # Bossbot Hand Color
lawbotHandColor = VBase4(0.75, 0.75, 0.95, 1.0) # Lawbot Hand Color
cashbotHandColor = VBase4(0.65, 0.95, 0.85, 1.0) # Cashbot Hand Color
sellbotHandColor = VBase4(0.95, 0.75, 0.95, 1.0) # Sellbot Hand Color
ExecutiveHandColor = VBase4(0.4, 0.4, 0.4, 1) # Hand color used by Executive Cogs.

ColdCallerHead = VBase4(0.25, 0.35, 1.0, 1.0) # Head used by Cold Caller


unlistedSuits = [] # These cogs aren't apart of the 8 cog tiers.
unlistedAllowedToInvade = [] # These cogs are unlisted but can invade.

            # Bossbots
suitProperties = {'f': ('c', 'c', 4.0 / cSize, bossbotHandColor, ['flunky', 'glasses'], '', 4.88),
                  'p': ('c', 'b',  3.35 / bSize, bossbotHandColor, ['pencilpusher'], '', 5.0),
                  'ym': ('c', 'a', 4.125 / aSize, bossbotHandColor, ['yesman'], '', 5.28),
                  'mm': ('c', 'c', 2.5 / cSize, bossbotHandColor, ['micromanager'], '', 3.25),
                  'ds': ('c', 'b', 4.5 / bSize, bossbotHandColor, ['beancounter'], '', 6.08),
                  'hh': ('c', 'a', 6.5 / aSize, bossbotHandColor, ['headhunter'], '', 7.45),
                  'cr': ('c', 'c', 6.75 / cSize, VBase4(0.85, 0.55, 0.55, 1.0), ['flunky'], 'corporate-raider.jpg', 8.23),
                  'tbc': ('c', 'a', 7.0 / aSize, VBase4(0.75, 0.95, 0.75, 1.0), ['bigcheese'], 'tt_t_ene_hed_bigCheese.png', 9.34),
                  # Lawbots
                  'bf': ('l', 'c', 4.0 / cSize, lawbotHandColor, ['tightwad'], 'bottom-feeder.jpg', 4.81),
                  'b': ('l', 'b', 4.375 / bSize, VBase4(0.95, 0.95, 1.0, 1.0), ['movershaker'], 'blood-sucker.jpg', 6.17),
                  'dt': ('l', 'a', 4.25 / aSize, lawbotHandColor, ['twoface'], 'double-talker.jpg', 5.63),
                  'ac': ('l', 'b', 4.35 / bSize, lawbotHandColor, ['ambulancechaser'], '', 6.39),
                  'bs': ('l', 'a', 4.5 / aSize, lawbotHandColor, ['backstabber'], '', 6.71),
                  'sd': ('l', 'b', 5.65 / bSize, VBase4(0.5, 0.8, 0.75, 1.0), ['telemarketer'], 'spin-doctor.jpg', 7.9),
                  'le': ('l', 'a', 7.125 / aSize, VBase4(0.25, 0.25, 0.5, 1.0), ['legaleagle'], '', 8.27),
                  'bw': ('l', 'a', 7.0 / aSize, lawbotHandColor, ['bigwig'], '', 8.69),
                  # Cashbots
                  'sc': ('m', 'c', 3.6 / cSize, cashbotHandColor, ['coldcaller'], '', 4.77),
                  'pp': ('m', 'a', 3.55 / aSize, VBase4(1.0, 0.5, 0.6, 1.0), ['pennypincher'], '', 5.26),
                  'tw': ('m', 'c', 4.5 / cSize, cashbotHandColor, ['tightwad'], '', 5.41),
                  'bc': ('m', 'b', 4.4 / bSize, cashbotHandColor, ['beancounter'], '', 5.95),
                  'nc': ('m', 'a', 5.25 / aSize, cashbotHandColor, ['numbercruncher'], '', 7.22),
                  'mb': ('m', 'c', 5.3 / cSize, cashbotHandColor, ['moneybags'], '', 6.97),
                  'ls': ('m', 'b', 6.5 / bSize, VBase4(0.5, 0.85, 0.75, 1.0), ['loanshark'], '', 8.58),
                  'rb': ('m', 'a', 7.0 / aSize, cashbotHandColor, ['yesman'], 'robber-baron.jpg', 8.95),
                  # Sellbots
                  'cc': ('s', 'c', 3.5 / cSize, VBase4(0.55, 0.65, 1.0, 1.0), ['coldcaller'], '', 4.63),
                  'tm': ('s', 'b', 3.75 / bSize, sellbotHandColor, ['telemarketer'], '', 5.24),
                  'nd': ('s', 'a', 4.35 / aSize, sellbotHandColor, ['numbercruncher'], 'name-dropper.jpg', 5.98),
                  'gh': ('s', 'c', 4.75 / cSize, sellbotHandColor, ['gladhander'], '', 6.4),
                  'ms': ('s', 'b', 4.75 / bSize, sellbotHandColor, ['movershaker'], '', 6.7),
                  'tf': ('s', 'a', 5.25 / aSize, sellbotHandColor, ['twoface'], '', 6.95),
                  'm': ('s', 'a', 5.75 / aSize, sellbotHandColor, ['twoface'], 'mingler.jpg', 7.61),
                  'mh': ('s', 'a', 7.0 / aSize, sellbotHandColor, ['yesman'], '', 8.95),
                  # Unlisted Cogs 
                  # NONE YET
                  }
