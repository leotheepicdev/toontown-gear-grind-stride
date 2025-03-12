from panda3d.core import TextNode
from toontown.base.TTLocalizerEnglishProperty import *
from toontown.catalog import CatalogAccessoryItemGlobals
from otp.otpbase import OTPLocalizer as OL
import random
OL.SpeedChatStaticText = OL.SpeedChatStaticTextToontown.copy()
for key in OL.SpeedChatStaticTextCommon.iterkeys():
    OL.SpeedChatStaticText[key] = OL.SpeedChatStaticTextCommon[key]

InterfaceFont = 'phase_3/models/fonts/ImpressBT.ttf'
ToonFont = 'phase_3/models/fonts/ImpressBT.ttf'
SuitFont = 'phase_3/models/fonts/vtRemingtonPortable.ttf'
SignFont = 'phase_3/models/fonts/MickeyFont'
MinnieFont = 'phase_3/models/fonts/MinnieFont'
ChalkFont = 'phase_3/models/fonts/Chawp.ttf'
BuildingNametagFont = 'phase_3/models/fonts/MickeyFont'
BuildingNametagShadow = None
NametagFonts = (
    'phase_3/models/fonts/ImpressBT.ttf',
    'phase_3/models/fonts/MickeyFont.bam',
    'phase_3/models/fonts/MinnieFont.bam',
    'phase_3/models/fonts/Aftershock.bam',
    'phase_3/models/fonts/JiggeryPokery.bam',
    'phase_3/models/fonts/Ironwork.bam',
    'phase_3/models/fonts/HastyPudding.bam',
    'phase_3/models/fonts/Comedy.bam',
    'phase_3/models/fonts/Humanist.bam',
    'phase_3/models/fonts/Portago.bam',
    'phase_3/models/fonts/Musicals.bam',
    'phase_3/models/fonts/Scurlock.bam',
    'phase_3/models/fonts/Danger.bam',
    'phase_3/models/fonts/Alie.bam',
    'phase_3/models/fonts/OysterBar.bam',
    'phase_3/models/fonts/RedDogSaloon.bam',
    'phase_3/models/fonts/PBN.ttf',
    'phase_3/models/fonts/SomethingStrange.ttf',
    'phase_3/models/fonts/DinosaursAreAlive.ttf',
    'phase_3/models/fonts/SuperMario256.ttf',
    'phase_3/models/fonts/Triforce.ttf',
    'phase_3/models/fonts/SerpentineDBol.ttf',
    'phase_3/models/fonts/ComicSansMS.ttf'
)
NametagFontNames = (
    'Basic',
    'Sign',
    'Minnie',
    'Shivering',
    'Wonky',
    'Fancy',
    'Silly',
    'Zany',
    'Practical',
    'Nautical',
    'Whimsical',
    'Spooky',
    'Action',
    'Poetic',
    'Boardwalk',
    'Western',
    'Pixelated',
    'Metal',
    'Dinosaurs',
    'Mario',
    'Triforce',
    'Prime',
    'Comic Sans'
)
NametagColorNames = ['Default', 'Red', 'Pink', 'Purple', 'Orange', 'Green', 'Yellow', 'Black', 'White', 'Brown', 'Gray', 
                     'Icy Blue', 'Slate Blue', 'High Blue', 'Light Blue', 'Aqua', 'Blue', 'Maroon', 'Lavender', 'Hot Pink', 'Ruby',
                     'Marigold', 'Vanilla', 'Milk Chocolate']
NametagPanelNames = ['Normal', 'None', 'Miner']
NametagLabel = ' Nametag'
ScreenshotPath = 'user/screenshots/'
Flippy = 'Flippy'
lTheBrrrgh = 'The Brrrgh'
lDaisyGardens = 'Daisy Gardens'
lDonaldsDock = "Drifter's Dock"
lDonaldsDreamland = "Daunting Dreamland"
lWackyWest = "Wacky West"
lMinniesMelodyland = "Musical Melodyland"
lToontownCentral = 'Toontown Central'
lToonHQ = 'Toon HQ'
lSellbotHQ = 'Sellbot HQ'
lGoofySpeedway = 'Toontown Speedway'
lOutdoorZone = "Acorn Acres"
lFunnyFarm = "Funny Farm"
lConstructionZone = "Construction Zone"
lGolfZone = "Toontown MiniGolf"
lPartyHood = 'Party Grounds'
GlobalStreetNames = {1000: ('to the', 'in the', 'Playground'),
 1100: ('to', 'on', 'Barnacle Boulevard'),
 1200: ('to', 'on', 'Seaweed Street'),
 1300: ('to', 'on', 'Lighthouse Lane'),
 2000: ('to the', 'in the', 'Playground'),
 2100: ('to', 'on', 'Silly Street'),
 2200: ('to', 'on', 'Loopy Lane'),
 2300: ('to', 'on', 'Punchline Place'),
 2400: ('to', 'on', 'Funny Freeway'),
 3000: ('to the', 'in the', 'Playground'),
 3100: ('to', 'on', 'Walrus Way'),
 3200: ('to', 'on', 'Sleet Street'),
 3300: ('to', 'on', 'Polar Place'),
 3400: ('to', 'on', 'Blizzard Bypass'),
 4000: ('to the', 'in the', 'Playground'),
 4100: ('to', 'on', 'Alto Avenue'),
 4200: ('to', 'on', 'Baritone Boulevard'),
 4300: ('to', 'on', 'Tenor Terrace'),
 5000: ('to the', 'in the', 'Playground'),
 5100: ('to', 'on', 'Elm Street'),
 5200: ('to', 'on', 'Maple Street'),
 5300: ('to', 'on', 'Oak Street'),
 6000: ('to the', 'in the', 'Playground'),
 6100: ('to', 'on', 'Fallen Walnut Way'),
 7000: ('to the', 'in the', 'Playground'),
 7100: ('to', 'on', 'Pitchfork Path'),
 7200: ('to', 'on', 'Haybale Highway'),
 7300: ('to', 'on', 'Rooster Road'),
 9000: ('to the', 'in the', 'Playground'),
 9100: ('to', 'on', 'Lullaby Lane'),
 9200: ('to', 'on', 'Pajama Place'),
 9300: ('to', 'on', 'Slumber Street'),
 14000: ('to the', 'in the', 'Playground'),
 14100: ('to', 'on', 'Rodeo Road'),
 14200: ('to', 'on', 'Cactus Court'),
 14300: ('to', 'on', 'High Noon Nook'),
 21000: ('to the', 'in the', 'Playground'),
 21100: ('to', 'on', 'Pavement Path'),
 21200: ('to', 'on', 'Bedrock Boulevard'),
 21300: ('to', 'on', 'Sawmill Street'),
 10000: ('to the', 'in the', 'Bossbot HQ Country Club'),
 10100: ('to the', 'in the', 'Bossbot HQ Lobby'),
 10200: ('to', 'in', 'The Clubhouse'),
 10500: ('to', 'in', 'The Front Two'),
 10600: ('to', 'in', 'The Middle Four'),
 10700: ('to', 'in', 'The Back Six'),
 11000: ('to the', 'in the', 'Sellbot HQ Courtyard'),
 11100: ('to the', 'in the', 'Sellbot HQ Lobby'),
 11200: ('to the', 'in the', 'Sellbot Factory'),
 11500: ('to the', 'in the', 'Sellbot Factory'),
 11600: ('to the', 'in the', 'Sellbot Extreme'),
 12000: ('to the', 'in the', 'Cashbot Train Yard'),
 12100: ('to the', 'in the', 'Cashbot HQ Lobby'),
 12500: ('to the', 'in the', 'Cashbot Coin Mint'),
 12600: ('to the', 'in the', 'Cashbot Dollar Mint'),
 12700: ('to the', 'in the', 'Cashbot Bullion Mint'),
 13000: ('to the', 'in the', 'Lawbot HQ Courtyard'),
 13100: ('to the', 'in the', 'Courthouse Lobby'),
 13200: ('to the', 'in the', "DA's Office Lobby"),
 13300: ('to the', 'in the', 'Lawbot A Office'),
 13400: ('to the', 'in the', 'Lawbot B Office'),
 13500: ('to the', 'in the', 'Lawbot C Office'),
 13600: ('to the', 'in the', 'Lawbot D Office')}
DonaldsDock = ('to', 'in', lDonaldsDock)
ToontownCentral = ('to', 'in', lToontownCentral)
TheBrrrgh = ('to', 'in', lTheBrrrgh)
MinniesMelodyland = ('to', 'in', lMinniesMelodyland)
DaisyGardens = ('to', 'in', lDaisyGardens)
OutdoorZone = ('to', 'in', lOutdoorZone)
FunnyFarm = ('to the', 'in the', lFunnyFarm)
GoofySpeedway = ('to', 'in', lGoofySpeedway)
DonaldsDreamland = ('to', 'in', lDonaldsDreamland)
ConstructionZone = ('to', 'in', lConstructionZone)
WackyWest = ('to', 'in', lWackyWest)
BossbotHQ = ('to', 'in', 'Bossbot HQ')
SellbotHQ = ('to', 'in', 'Sellbot HQ')
CashbotHQ = ('to', 'in', 'Cashbot HQ')
LawbotHQ = ('to', 'in', 'Lawbot HQ')
MyEstate = ('to', 'in', 'your house')
GolfZone = ('to', 'in', lGolfZone)
PartyHood = ('to the', 'in the', lPartyHood)
Factory = 'Factory'
Headquarters = 'Headquarters'
SellbotFrontEntrance = 'Front Entrance'
SellbotSideEntrance = 'Side Entrance'
Office = 'Office'
FactoryNames = {11500: 'Sellbot Cog Factory',
 11600: 'Sellbot Cog Extreme',
 13300: 'Lawbot Cog Office'}
FactoryTypeLeg = 'Leg'
FactoryTypeArm = 'Arm'
FactoryTypeTorso = 'Torso'
DefaultFloorTitle = 'Floor %s'
CountryClubFloorTitle = 'Hole %s'
lCancel = 'Cancel'
lClose = 'Close'
lOK = 'OK'
lNext = 'Next'
lQuit = 'Quit'
lYes = 'Yes'
lNo = 'No'
SleepAutoReply = '%s is sleeping right now.'
lHQOfficerF = 'HQ Officer'
lHQOfficerM = 'HQ Officer'
Cog = 'Cog'
Cogs = 'Cogs'
ACog = 'a Cog'
TheCogs = 'The Cogs'
ASkeleton = 'a Skelecog'
Skeleton = 'Skelecog'
SkeletonP = 'Skelecogs'
Av2Cog = 'a Version 2.0 Cog'
v2Cog = 'Version 2.0 Cog'
v2CogP = 'Version 2.0 Cogs'
ASkeleton = 'a Skelecog'
Foreman = 'Factory Foreman'
ForemanP = 'Factory Foremen'
AForeman = 'a Factory Foreman'
CogVP = Cog + ' V.P.'
CogVPs = "Cog V.P.'s"
ACogVP = ACog + ' V.P.'
Supervisor = 'Mint Supervisor'
SupervisorP = 'Mint Supervisors'
ASupervisor = 'a Mint Supervisor'
CogCFO = Cog + ' C.F.O.'
CogCFOs = "Cog C.F.O.'s"
ACogCFO = ACog + ' C.F.O.'
CogCJs = "Cog C.J.'s"
ACogCJ = ACog + ' C.J.'
CogCEOs = "Cog C.E.O.'s"
ACogCEO = ACog + ' C.E.O.'
CogBosses = 'Cog Bosses'
ACogBoss = ACog + ' Boss'
TheFish = 'the Fish'
AFish = 'a fish'
Level = 'Level'
QuestsCompleteString = 'Complete'
QuestsNotChosenString = 'Not chosen'
Period = '.'
Laff = 'Laff'
QuestInLocationString = ' %(inPhrase)s %(location)s'
QuestsDefaultGreeting = ('Hello, _avName_!',
 'Hi, _avName_!',
 'Hey there, _avName_!',
 'Say there, _avName_!',
 'Welcome, _avName_!',
 'Howdy, _avName_!',
 'How are you, _avName_?',
 'Greetings _avName_!')
QuestsDefaultIncomplete = ("How's that task coming, _avName_?",
 'Looks like you still have more work to do on that task!',
 'Keep up the good work, _avName_!',
 'Keep trying to finish that task.  I know you can do it!',
 'Keep trying to complete that task, we are counting on you!',
 'Keep working on that ToonTask!')
QuestsDefaultIncompleteProgress = ('You came to the right place, but you need to finish your ToonTask first.', 'When you are finished with that ToonTask, come back here.', 'Come back when you are finished with your ToonTask.')
QuestsDefaultIncompleteWrongNPC = ('Nice work on that ToonTask. You should go visit _toNpcName_._where_', 'Looks like you are ready to finish your ToonTask. Go see _toNpcName_._where_.', 'Go see _toNpcName_ to finish your ToonTask._where_')
QuestsDefaultComplete = ('Nice work! Here is your reward...', 'Great job, _avName_! Take this reward...', 'Wonderful job, _avName_! Here is your reward...')
QuestsDefaultLeaving = ('Bye!',
 'Goodbye!',
 'So long, _avName_.',
 'See ya, _avName_!',
 'Good luck!',
 'Have fun in Toontown!',
 'See you later!')
QuestsDefaultReject = ('Heya, _avName_!',
 'Whatcha need?',
 'Hello! How are you doing?',
 'Hi there.',
 "Sorry _avName_, I'm a bit busy right now.",
 'Yes?',
 'Howdy, _avName_!',
 'Welcome, _avName_!',
 "Hey, _avName_! How's it hanging?",
 "Need any help?",
 "Hi _avName_, what brings you here?")
QuestsDefaultTierNotDone = ('Hello, _avName_! You must finish your current ToonTasks before getting a new one.', 'Hi there! You need to finish the ToonTasks you are working on in order to get a new one.', 'Hi, _avName_! Before I can give you a new ToonTask, you need to finish the ones you have.')
QuestsDefaultQuest = None
QuestsDefaultVisitQuestDialog = ('I heard _toNpcName_ is looking for you._where_',
 'Stop by and see _toNpcName_ when you get a chance._where_',
 'Pay a visit to _toNpcName_ next time you are over that way._where_',
 'If you get a chance, stop in and say hi to _toNpcName_._where_',
 '_toNpcName_ will give you your next ToonTask._where_')
QuestsLocationArticle = ''

def getLocalNum(num):
    return str(num)


QuestsItemNameAndNum = '%(num)s %(name)s'
QuestsCogQuestProgress = '%(progress)s of %(numCogs)s defeated'
QuestsCogQuestSCStringS = 'I need to defeat %(cogName)s%(cogLoc)s.'
QuestsCogQuestSCStringP = 'I need to defeat some %(cogName)s%(cogLoc)s.'
QuestsCogQuestDefeat = 'Defeat %s'
QuestsCogQuestDefeatDesc = '%(numCogs)s %(cogName)s'
QuestsCogTrackQuestProgress = '%(progress)s of %(numCogs)s defeated'
QuestsCogTrackQuestSCStringS = 'I need to defeat %(cogText)s%(cogLoc)s.'
QuestsCogTrackQuestSCStringP = 'I need to defeat some %(cogText)s%(cogLoc)s.'
QuestsCogTrackQuestDefeat = 'Defeat %s'
QuestsCogTrackDefeatDesc = '%(numCogs)s %(trackName)s'
QuestsCogLevelQuestProgress = '%(progress)s of %(numCogs)s defeated'
QuestsCogLevelQuestDefeat = 'Defeat %s'
QuestsCogLevelQuestDesc = 'a Level %(level)s+ %(name)s'
QuestsCogLevelQuestDescC = '%(count)s Level %(level)s+ %(name)s'
QuestsCogLevelQuestDescI = 'some Level %(level)s+ %(name)s'
QuestsCogLevelQuestSCString = 'I need to defeat %(objective)s%(location)s.'
QuestsBuildingQuestFloorNumbers = ('',
 'two+',
 'three+',
 'four+',
 'five+',
 'six+',
 'seven+')
QuestsBuildingQuestHeadline = 'DEFEAT'
QuestsBuildingQuestProgressString = '%(progress)s of %(num)s defeated'
QuestsBuildingQuestString = 'Defeat %s'
QuestsBuildingQuestSCString = 'I need to defeat %(objective)s%(location)s.'
QuestsBuildingQuestDesc = 'a %(type)s Building'
QuestsBuildingQuestDescF = 'a %(floors)s story %(type)s Building'
QuestsBuildingQuestDescC = '%(count)s %(type)s Buildings'
QuestsBuildingQuestDescCF = '%(count)s %(floors)s story %(type)s Buildings'
QuestsBuildingQuestDescI = 'some %(type)s Buildings'
QuestsBuildingQuestDescIF = 'some %(floors)s story %(type)s Buildings'
QuestsCogdoQuestDesc = 'a %(type)s Field Office'
QuestsCogdoQuestDescM = '%(count)s %(type)s Field Offices'
QuestsCogdoQuestDescMUI = 'some %(type)s Field Offices'
QuestsCogdoQuestDescU = 'a Field Office'
QuestsCogdoQuestDescUM = '%(count)s Field Offices'
QuestsCogdoQuestDescMI = 'some Field Offices'
QuestFactoryQuestFactory = 'Factory'
QuestsFactoryQuestFactories = 'Factories'
QuestsFactoryQuestHeadline = 'DEFEAT'
QuestsFactoryQuestProgressString = '%(progress)s of %(num)s defeated'
QuestsFactoryQuestString = 'Defeat %s'
QuestsFactoryQuestSCString = 'I need to defeat %(objective)s%(location)s.'
QuestsFactoryQuestDesc = 'a %(type)s Factory'
QuestsFactoryQuestDescC = '%(count)s %(type)s Factories'
QuestsFactoryQuestDescI = 'some %(type)s Factories'
QuestMintQuestMint = 'Mint'
QuestsMintQuestMints = 'Mints'
QuestsMintQuestHeadline = 'DEFEAT'
QuestsMintQuestProgressString = '%(progress)s of %(num)s defeated'
QuestsMintQuestString = 'Defeat %s'
QuestsMintQuestSCString = 'I need to defeat %(objective)s%(location)s.'
QuestsMintQuestDesc = 'a Cog Mint'
QuestsMintQuestDescC = '%(count)s Cog Mints'
QuestsMintQuestDescI = 'some Cog Mints'
QuestsRescueQuestProgress = '%(progress)s of %(numToons)s rescued'
QuestsRescueQuestHeadline = 'RESCUE'
QuestsRescueQuestSCStringS = 'I need to rescue a Toon %(toonLoc)s.'
QuestsRescueQuestSCStringP = 'I need to rescue some Toons %(toonLoc)s.'
QuestsRescueQuestRescue = 'Rescue %s'
QuestsRescueQuestRescueDesc = '%(numToons)s Toons'
QuestsRescueQuestToonS = 'a Toon'
QuestsRescueQuestToonP = 'Toons'
QuestsRescueQuestAux = 'Rescue:'
QuestCogPartQuestCogPart = 'Cog Suit Part'
QuestsCogPartQuestFactories = 'Factories'
QuestsCogPartQuestHeadline = 'RETRIEVE'
QuestsCogPartQuestProgressString = '%(progress)s of %(num)s retrieved'
QuestsCogPartQuestString = 'Retrieve %s'
QuestsCogPartQuestSCString = 'I need to retrieve %(objective)s%(location)s.'
QuestsCogPartQuestAux = 'Retrieve:'
QuestsCogPartQuestDesc = 'a Cog Suit Part'
QuestsCogPartQuestDescC = '%(count)s Cog Suit Parts'
QuestsCogPartQuestDescI = 'some Cog Suit Parts'
QuestsDeliverGagQuestProgress = '%(progress)s of %(numGags)s delivered'
QuestsDeliverGagQuestHeadline = 'DELIVER'
QuestsDeliverGagQuestToSCStringS = 'I need to deliver %(gagName)s.'
QuestsDeliverGagQuestToSCStringP = 'I need to deliver some %(gagName)s.'
QuestsDeliverGagQuestSCString = 'I need to make a delivery.'
QuestsDeliverGagQuestString = 'Deliver %s'
QuestsDeliverGagQuestStringLong = 'Deliver %s to _toNpcName_.'
QuestsDeliverGagQuestInstructions = 'You can buy this gag in the Gag Shop once you earn access to it.'
QuestsDeliverItemQuestProgress = ''
QuestsDeliverItemQuestHeadline = 'DELIVER'
QuestsDeliverItemQuestSCString = 'I need to deliver %(article)s%(itemName)s.'
QuestsDeliverItemQuestString = 'Deliver %s'
QuestsDeliverItemQuestStringLong = 'Deliver %s to _toNpcName_.'
QuestsTrackChoiceQuestHeadline = 'CHOOSE'
QuestsTrackChoiceQuestSCString = 'I need to choose a new Gag Track.'
QuestsTrackChoiceQuestString = 'Choose a new Gag Track.'
QuestsVisitQuestProgress = ''
QuestsVisitQuestHeadline = 'VISIT'
QuestsVisitQuestStringShort = 'Visit'
QuestsVisitQuestStringLong = 'Visit _toNpcName_'
QuestsVisitQuestSeeSCString = 'I need to see %s.'
QuestsRecoverItemQuestProgress = '%(progress)s of %(numItems)s recovered'
QuestsRecoverItemQuestHeadline = 'RECOVER'
QuestsRecoverItemQuestSeeHQSCString = 'I need to see an ' + lHQOfficerM + '.'
QuestsRecoverItemQuestReturnToHQSCString = 'I need to return %s to an ' + lHQOfficerM + '.'
QuestsRecoverItemQuestReturnToSCString = 'I need to return %(item)s to %(npcName)s.'
QuestsRecoverItemQuestGoToHQSCString = 'I need to go to a Toon HQ.'
QuestsRecoverItemQuestGoToPlaygroundSCString = 'I need to go to %s Playground.'
QuestsRecoverItemQuestGoToStreetSCString = 'I need to go %(to)s %(street)s in %(hood)s.'
QuestsRecoverItemQuestVisitBuildingSCString = 'I need to visit %s%s.'
QuestsRecoverItemQuestWhereIsBuildingSCString = 'Where is %s%s?'
QuestsRecoverItemQuestRecoverFromSCString = 'I need to recover %(item)s from %(holder)s%(loc)s.'
QuestsRecoverItemQuestString = 'Recover %(item)s from %(holder)s'
QuestsRecoverItemQuestHolderString = '%(level)s %(holder)d+ %(cogs)s'
QuestsFriendQuestHeadline = 'FRIEND'
QuestsFriendQuestSCString = 'I need to make a friend.'
QuestsFriendQuestString = 'Make a friend'
QuestsMailboxQuestHeadline = 'MAIL'
QuestsMailboxQuestSCString = 'I need to check my mail.'
QuestsMailboxQuestString = 'Check your mail'
QuestsPhoneQuestHeadline = 'CLARABELLE'
QuestsPhoneQuestSCString = 'I need to call Clarabelle.'
QuestsPhoneQuestString = 'Call Clarabelle'
QuestsTrolleyQuestHeadline = 'TROLLEY'
QuestsTrolleyQuestSCString = 'I need to ride the trolley.'
QuestsTrolleyQuestString = 'Ride on the trolley'
QuestsTrolleyQuestStringShort = 'Ride the trolley'
QuestsMaxHpReward = 'Your Laff limit has been increased by %s.'
QuestsMaxHpRewardPoster = 'Reward: %s point Laff boost'
QuestsMoneyRewardSingular = 'You get 1 Jellybean.'
QuestsMoneyRewardPlural = 'You get %s Jellybeans.'
QuestsMoneyRewardPosterSingular = 'Reward: 1 Jellybean'
QuestsMoneyRewardPosterPlural = 'Reward: %s Jellybeans'
QuestsMaxGagCarryReward = 'You get a %(name)s. You can now carry %(num)s gags.'
QuestsMaxGagCarryRewardPoster = 'Reward: %(name)s (%(num)s)'
QuestsMaxQuestCarryReward = 'You can now have %s ToonTasks.'
QuestsMaxQuestCarryRewardPoster = 'Reward: Carry %s ToonTasks'
QuestsCogMeritReward = 'Your %s have increased by 20%%.'
QuestsTrackTrainingReward = 'You can now train for "%s" gags.'
QuestsTrackTrainingRewardPoster = 'Reward: Gag training'
QuestsTrackProgressReward = 'You now have frame %(frameNum)s of the %(trackName)s track animation.'
QuestsTrackProgressRewardPoster = 'Reward: "%(trackName)s" track animation frame %(frameNum)s'
QuestsTrackCompleteReward = 'You may now carry and use "%s" gags.'
QuestsTrackCompleteRewardPoster = 'Reward: Final %s track training'
QuestsCogMeritRewardPoster = 'Reward: 20%% Increased %s'
QuestsStreetLocationThisPlayground = 'in this playground'
QuestsStreetLocationThisStreet = 'on this street'
QuestsStreetLocationNamedPlayground = 'in the %s playground'
QuestsStreetLocationNamedStreet = 'on %(toStreetName)s in %(toHoodName)s'
QuestsLocationString = '%(string)s%(location)s'
QuestsLocationBuilding = "%s's building is called"
QuestsLocationBuildingVerb = 'which is'
QuestsLocationParagraph = '\x07%(building)s "%(buildingName)s"...\x07...%(buildingVerb)s %(street)s.'
QuestsGenericFinishSCString = 'I need to finish a ToonTask.'
QuestsMediumPouch = 'Medium Pouch'
QuestsLargePouch = 'Large Pouch'
QuestsSmallBag = 'Small Bag'
QuestsMediumBag = 'Medium Bag'
QuestsLargeBag = 'Large Bag'
QuestsSmallBackpack = 'Small Backpack'
QuestsMediumBackpack = 'Medium Backpack'
QuestsLargeBackpack = 'Large Backpack'
QuestsItemDict = {}
QuestsGenericCogHeadline = 'COG CLASH!'
CogTrack2Headline = {'c': 'BESIEGE BOSSBOT!',
 'l': 'LAWBOTS LOSE!',
 'm': 'CASHBOT CHAOS!',
 's': 'STORM SELLBOT!'}
CogName2Headline = {'f': 'REAL SPUNKY!',
 'p': 'WE ARE NO.2!',
 'ym': 'ALWAYS YES!',
 'mm': 'NEVER TOO SMALL!',
 'ds': 'GOING DOWN!',
 'hh': 'HEADS UP!',
 'cr': 'RAID!',
 'tbc': 'WHAT A BRIEEZE!',
 'bf': 'BOTTOMS UP!',
 'b': 'GETTING DIZZY!',
 'dt': 'DOUBLE TROUBLE!',
 'ac': "CHASING OUTTA TOWN",
 'bs': 'BACKSTAB!',
 'sd': 'OUT OF CONTROL!',
 'le': 'SOAR AND SCORE',
 'bw': 'BIG TROUBLE!',
 'sc': 'MONEY TROUBLE!',
 'pp': 'PRESSING LUCK!',
 'tw': 'THINGS ARE TIGHT!',
 'bc': 'COUNTING BEANS!',
 'nc': 'TIME FOR CRUNCH!',
 'mb': 'NEVER TOO RICH!',
 'ls': 'TIME TO PAY UP!',
 'rb': "STICK 'EM UP",
 'cc': 'WHAT A SURPRISE!',
 'tm': "CAN'T GO AWAY!",
 'nd': 'NEVER FORGOTTEN',
 'gh': 'BUSINESS AT HAND',
 'ms': 'SHAKE DOWN!',
 'tf': 'FACE OFF!',
 'm': "LET'S MINGLE",
 'mh': 'ACTION!'}

QuestsHQOfficerFillin = lHQOfficerM
QuestsHQWhereFillin = ''
QuestsHQBuildingNameFillin = lToonHQ
QuestsHQLocationNameFillin = 'in any neighborhood'
QuestsTailorFillin = 'Tailor'
QuestsTailorWhereFillin = ''
QuestsTailorBuildingNameFillin = 'Clothing Store'
QuestsTailorLocationNameFillin = 'in any neighborhood'
QuestsTailorQuestSCString = 'I need to see a Tailor.'
QuestMovieQuestChoiceCancel = 'Come back later if you need a ToonTask! Bye!'
QuestMovieTrackChoiceCancel = 'Come back when you are ready to decide! Bye!'
QuestMovieQuestChoice = 'Choose a ToonTask.'
QuestMovieTrackChoice = 'Ready to decide? Choose a track, or come back later.'
GREETING = 0
QUEST = 1
INCOMPLETE = 2
INCOMPLETE_PROGRESS = 3
INCOMPLETE_WRONG_NPC = 4
COMPLETE = 5
LEAVING = 6
TheBrrrghTrackQuestDict = {GREETING: '',
 QUEST: 'Now you are ready.\x07Go out and walk the earth until you know which track you would like to choose.\x07Choose wisely, because this is your final track.\x07When you are certain, return to me.',
 INCOMPLETE_PROGRESS: 'Choose wisely.',
 INCOMPLETE_WRONG_NPC: 'Choose wisely.',
 COMPLETE: 'Very wise choice!',
 LEAVING: 'Good luck.  Return to me when you have mastered your new skill.'}
QuestDialog_3225 = {QUEST: "Oh, thanks for coming, _avName_!\x07The Cogs in the neighborhood frightened away my delivery person.\x07I don't have anyone to deliver this salad to _toNpcName_!\x07Can you do it for me? Thanks so much!_where_"}
QuestDialog_2910 = {QUEST: 'Back so soon?\x07Great job on the spring.\x07The final item is a counter weight.\x07Stop by and see _toNpcName_ and bring back whatever you can get._where_'}
QuestDialogDict = {}
ChatGarblerDog = ['woof', 'arf', 'rruff']
ChatGarblerCat = ['meow', 'mew']
ChatGarblerMouse = ['squeak', 'squeaky', 'squeakity']
ChatGarblerHorse = ['neigh', 'brrr']
ChatGarblerRabbit = ['eek', 'eepr', 'eepy', 'eeky']
ChatGarblerDuck = ['quack', 'quackity', 'quacky']
ChatGarblerMonkey = ['ooh', 'ooo', 'ahh']
ChatGarblerBear = ['growl', 'grrr']
ChatGarblerPig = ['oink', 'oik', 'snort']
ChatGarblerFox = ['ring', 'ding', 'pow']
ChatGarblerHedgehog = ['snuff', 'huff', 'puff', 'sss']
ChatGarblerDefault = ['blah']
Bossbot = 'Bossbot'
Lawbot = 'Lawbot'
Cashbot = 'Cashbot'
Sellbot = 'Sellbot'
Scibot = 'Scibot'
BossbotS = 'a Bossbot'
LawbotS = 'a Lawbot'
CashbotS = 'a Cashbot'
SellbotS = 'a Sellbot'
ScibotS = 'a Scibot'
BossbotP = 'Bossbots'
LawbotP = 'Lawbots'
CashbotP = 'Cashbots'
SellbotP = 'Sellbots'
ScibotP = 'Scibots'
BossbotSkelS = 'a Bossbot Skelecog'
LawbotSkelS = 'a Lawbot Skelecog'
CashbotSkelS = 'a Cashbot Skelecog'
SellbotSkelS = 'a Sellbot Skelecog'
ScibotSkelS = 'a Scibot Skelecog'
BossbotSkelP = 'Bossbot Skelecogs'
LawbotSkelP = 'Lawbot Skelecogs'
CashbotSkelP = 'Cashbot Skelecogs'
SellbotSkelP = 'Sellbot Skelecogs'
ScibotSkelP = 'Scibot Skelecogs'
SkeleRevivePostFix = "\x01shadow\x01\x01WLRed\x01 V%s.0\x02\x02"
WaiterPostFix = "\x01shadow\x01\x01white\x01 Waiter\x02\x02"
ExecutivePostFix = ' Executive'
AvatarDetailPanelOK = lOK
AvatarDetailPanelCancel = lCancel
AvatarDetailPanelClose = lClose
AvatarDetailPanelLookup = 'Looking up details for %s.'
AvatarDetailPanelFailedLookup = 'Unable to get details for %s.'
AvatarDetailPanelOnline = 'District: %(district)s\nLocation: %(location)s\nIdentifier: %(identifier)s'
AvatarDetailPanelOffline = 'District: offline\nLocation: offline\nIdentifier: %(identifier)s'
OfflineLocation = 'Offline'
AvatarPanelFriends = 'Friends'
AvatarPanelWhisper = 'Whisper'
AvatarPanelTrueFriends = 'True Friends'
AvatarPanelGoTo = 'Go To'
AvatarPanelPet = 'Show Doodle'
AvatarPanelIgnore = 'Ignore'
AvatarPanelIgnoreCant = 'Okay'
AvatarPanelStopIgnoring = 'Stop Ignoring'
AvatarPanelReport = 'Report'
AvatarPanelCogLevel = 'Level: %s'
AvatarPanelCogDetailClose = lClose
AvatarPanelDetail = 'Toon Details'
AvatarPanelGroupInvite = 'Invite'
AvatarPanelGroupMerge = 'Resulting in'
AvatarPanelGroupRetract = 'Retract Invitation'
AvatarPanelGroupMember = 'Already In Group'
AvatarPanelGroupMemberKick = 'Remove'
AvatarPanelCast = 'Cast Member'
AvatarPanelCastInfo = '%s is a Toontown: Gear Grind Cast Member.'
ReportPanelTitle = 'Report A Toon'
ReportPanelBody = 'This feature will send a complete report to a Moderator. Instead of sending a report, you might choose to do one of the following:\n\n  - Teleport to another district\n  - Use "Ignore" on the toon\'s panel\n\nDo you really want to report %s to a Moderator?'
ReportPanelBodyFriends = 'This feature will send a complete report to a Moderator. Instead of sending a report, you might choose to do one of the following:\n\n  - Teleport to another district\n  - Break your friendship\n\nDo you really want to report %s to a Moderator?\n\n(This will also break your friendship)'
ReportPanelCategoryBody = 'You are about to report %s. A Moderator will be alerted to your complaint and will take appropriate action for anyone breaking our rules. Please choose the reason you are reporting %s:'
ReportPanelCategoryLanguage = 'Inappropriate Language'
ReportPanelCategoryRude = 'Rude or Mean Behavior'
ReportPanelCategoryName = 'Bad Name'
ReportPanelCategoryHacking = 'Hacking'
ReportPanelCategoryGreening = 'Greening'
ReportPanelConfirmations = ('You are about to report that %s has used obscene, bigoted or sexually explicit language.',
 'You are about to report that %s has disrupted your experience by intentionally causing your toon to go sad.',
 'You are about to report that %s is bullying, harassing, or using extreme behavior to disrupt the game.',
 "You are about to report that %s has created a name that does not follow the rules.",
 'You are about to report that %s has hacked/tampered with the game or used third party software.')
ReportPanelWarning = "We take reporting very seriously. Your report will be viewed by a Moderator who will take appropriate action for anyone breaking our rules. If your account is found to have participated in breaking the rules, or if you make false reports or abuse the 'Report a Toon' system, a Moderator may take action against your account. Are you absolutely sure you want to report this toon?"
ReportPanelThanks = 'Thank you! Your report has been sent to a Moderator for review. There is no need to contact us again about the issue. The moderation team will take appropriate action for a toon found breaking our rules.'
ReportPanelRemovedFriend = 'We have automatically removed %s from your Toon Friends List.'
ReportPanelAlreadyReported = 'You have already reported %s during this session. A Moderator will review your previous report.'
IgnorePanelTitle = 'Ignore A Toon'
IgnorePanelAddIgnore = 'Would you like to ignore %s?'
IgnorePanelIgnore = 'You are now ignoring %s.'
IgnorePanelRemoveIgnore = 'Would you like to stop ignoring %s?'
IgnorePanelEndIgnore = 'You are no longer ignoring %s.'
IgnorePanelAddFriendAvatar = '%s is your friend, you cannot ignore them while you are friends.'
PetPanelFeed = 'Feed'
PetPanelCall = 'Call'
PetPanelGoTo = 'Go To'
PetPanelOwner = 'Show Owner'
PetPanelDetail = 'Pet Details'
PetPanelScratch = 'Scratch'
PetDetailPanelTitle = 'Trick Training'
PetTrickStrings = {0: 'Jump',
 1: 'Beg',
 2: 'Play dead',
 3: 'Rollover',
 4: 'Backflip',
 5: 'Dance',
 6: 'Speak'}
PetMoodAdjectives = {'neutral': 'neutral',
 'hunger': 'hungry',
 'boredom': 'bored',
 'excitement': 'excited',
 'sadness': 'sad',
 'restlessness': 'restless',
 'playfulness': 'playful',
 'loneliness': 'lonely',
 'fatigue': 'tired',
 'confusion': 'confused',
 'anger': 'angry',
 'surprise': 'surprised',
 'affection': 'affectionate'}
SpokenMoods = {'neutral': 'neutral',
 'hunger': ["I'm tired of Jellybeans! How'bout giving me a slice of pie?",
            "How'bout a Red Jellybean? I'm tired of the Green ones!",
            "Oh, those Jellybeans were for planting?!! But I'm hungry!"],
 'boredom': ["I'm dying of boredom over here!",
             "You didn't think I understood you, huh?",
             'Could we, like, DO something already?'],
 'excitement': ["Wow, it's you, it's you, it's you!",
                'mmm, Jellybeans, mmm!',
                'Does it GET any better than this?',
                "Happy April Toons' Week!"],
 'sadness': ["Don't go, Don't go, Don't go, Don't go, Don't go, Don't go, Don't go, Don't go, Don't go, Don't go, Don't go...",
             "I'll be good, I promise!",
             "I don't know WHY I'm sad, I just am!!!"],
 'restlessness': ["I'm sooo restless!!!"],
 'playfulness': ["Let's play, Let's play, Let's play, Let's play, Let's play, Let's play, Let's play, Let's play, Let's play...",
                 'Play with me or I dig up some flowers!',
                 'Lets run around and  around and around and around and around and around...'],
 'loneliness': ['Where have you been?',
                'Wanna cuddle?',
                'I want to go with you when you fight Cogs!'],
 'fatigue': ['That swim in the pond really tired me out!',
             'Being a Doodle is exhausting!',
             'I gotta get to Dreamland!'],
 'confusion': ['Where am I? Who are you again?',
               "What's a Toon-up again?",
               "Whoa, I'm standing between you and the Cogs! Run away!"],
 'anger': ['... and you wonder why I never give you a Toon-up?!!!',
           'You always leave me behind!',
           'You love your gags more than you love me!'],
 'surprise': ['Of course Doodles can talk!',
              'Toons can talk?!!',
              'Whoa, where did you come from?'],
 'affection': ["You're the best Toon EVER!!!!!!!!!!",
               'Do you even KNOW how great you are?!?',
               'I am SO lucky to be with you!!!']}
DialogQuestion = '?'
FriendsListLabel = 'Friends'
TeleportPanelOK = lOK
TeleportPanelCancel = lCancel
TeleportPanelYes = lYes
TeleportPanelNo = lNo
TeleportPanelCheckAvailability = 'Trying to go to %s.'
TeleportPanelNotAvailable = '%s is busy right now; try again later.'
TeleportPanelIgnored = '%s is ignoring you.'
TeleportPanelNotOnline = "%s isn't online right now."
TeleportPanelWentAway = '%s went away.'
TeleportPanelDenySelf = "You can't go to yourself!"
TeleportPanelOtherShard = "%(avName)s is in district %(shardName)s, and you're in district %(myShardName)s.  Do you want to switch to %(shardName)s?"
TeleportPanelBusyShard = '%(avName)s is in a full District.'
BattleBldgBossTaunt = "I'm the boss."
CogdoBattleBldgBossTaunt = "I don't take meetings with Toons."
FactoryBossTaunt = "I'm the Foreman."
FactoryBossBattleTaunt = 'Let me introduce you to the Foreman.'
MintBossTaunt = "I'm the Supervisor."
MintBossBattleTaunt = 'You need to talk to the Supervisor.'
StageBossTaunt = "My Justice isn't Blind."
StageBossBattleTaunt = 'I am above the Law.'
CountryClubBossTaunt = "I'm the Club President."
CountryClubBossBattleTaunt = 'You need to talk to the Club President.'
ForcedLeaveCountryClubAckMsg = 'The Club President was defeated before you could reach him. You did not recover any Stock Options.'
ToonHealJokes = [['What goes TICK-TICK-TICK-WOOF?', 'A watchdog! '],
 ['Why do male deer need braces?', "Because they have 'buck teeth'!"],
 ['Why is it hard for a ghost to tell a lie?', 'Because you can see right through him.'],
 ['What did the ballerina do when she hurt her foot?', 'She called the toe truck!'],
 ['What has one horn and gives milk?', 'A milk truck!'],
 ["Why don't witches ride their brooms when they're angry?", "They don't want to fly off the handle!"],
 ['Why did the dolphin cross the ocean?', 'To get to the other tide.'],
 ['What kind of mistakes do spooks make?', 'Boo boos.'],
 ['Why did the chicken cross the playground?', 'To get to the other slide!'],
 ['Where does a peacock go when he loses his tail?', 'A retail store.'],
 ["Why didn't the skeleton cross the road?", "He didn't have the guts."],
 ["Why wouldn't they let the butterfly into the dance?", 'Because it was a moth ball.'],
 ["What's gray and squirts jam at you?", 'A mouse eating a doughnut.'],
 ['What happened when 500 hares got loose on the main street?', 'The police had to comb the area.'],
 ["What's the difference between a fish and a piano?", "You can tune a piano, but you can't tuna fish!"],
 ['What do people do in clock factories?', 'They make faces all day.'],
 ['What do you call a blind dinosaur?', "An I-don't-think-he-saurus."],
 ['If you drop a white hat into the Red Sea, what does it become?', 'Wet.'],
 ["What two things can't you have for breakfast?", 'Lunch and dinner.'],
 ['What do you give an elephant with big feet?', 'Big shoes.'],
 ['Where do baby ghosts go during the day?', 'Day-scare centers.'],
 ['What did Snow White say to the photographer?', 'Some day my prints will come.'],
 ["What's Tarzan's favorite song?", 'Jungle bells.'],
 ["What's green and loud?", 'A froghorn.'],
 ["What's worse than raining cats and dogs?", 'Hailing taxis.'],
 ['When is the vet busiest?', "When it's raining cats and dogs."],
 ['What do you call a gorilla wearing ear-muffs?', "Anything you want, he can't hear you."],
 ['Where would you weigh a whale?', 'At a whale-weigh station.'],
 ['What travels around the world but stays in the corner?', 'A stamp.'],
 ['What do you give a pig with a sore throat?', 'Oinkment.'],
 ['What did the hat say to the scarf?', 'You hang around while I go on a head.'],
 ["What's the best parting gift?", 'A comb.'],
 ['What kind of cats like to go bowling?', 'Alley cats.'],
 ['What did one eye say to the other?', 'Between you and me, something smells.'],
 ["What's round, white and giggles?", 'A tickled onion.'],
 ['What do you get when you cross Bambi with a ghost?', 'Bamboo.'],
 ['Why do golfers take an extra pair of socks?', 'In case they get a hole in one.'],
 ['What do you call a fly with no wings?', 'A walk.'],
 ['Who did Frankenstein take to the prom?', 'His ghoul friend.'],
 ['What lies on its back, one hundred feet in the air?', 'A sleeping centipede.'],
 ['How do you keep a bull from charging?', 'Take away his credit card.'],
 ['What do you call a chicken at the North Pole?', 'Lost.'],
 ['What do you get if you cross a cat with a dog?', 'An animal that chases itself.'],
 ['What did the digital watch say to the grandfather clock?', 'Look dad, no hands.'],
 ['Where does Ariel the mermaid go to see movies?', 'The dive-in.'],
 ['What do you call a mosquito with a tin suit?', 'A bite in shining armor.'],
 ['What do giraffes have that no other animal has?', 'Baby giraffes.'],
 ['Why did the man hit the clock?', 'Because the clock struck first.'],
 ['Why did the apple go out with a fig?', "Because it couldn't find a date."],
 ['What do you get when you cross a parrot with a monster?', 'A creature that gets a cracker whenever it asks for one.'],
 ["Why didn't the monster make the football team?", 'Because he threw like a ghoul!'],
 ['What do you get if you cross a Cocker Spaniel with a Poodle and a rooster?', 'A cockapoodledoo!'],
 ['What goes dot-dot-dash-dash-squeak?', 'Mouse code.'],
 ["Why aren't elephants allowed on beaches?", "They can't keep their trunks up."],
 ['What is at the end of everything?', 'The letter G.'],
 ['How do trains hear?', 'Through the engineers.'],
 ['What does the winner of a marathon lose?', 'His breath.'],
 ['Why did the pelican refuse to pay for his meal?', 'His bill was too big.'],
 ['What has six eyes but cannot see?', 'Three blind mice.'],
 ["What works only when it's fired?", 'A rocket.'],
 ["Why wasn't there any food left after the monster party?", 'Because everyone was a goblin!'],
 ['What bird can be heard at mealtimes?', 'A swallow.'],
 ['What goes Oh, Oh, Oh?', 'Santa walking backwards.'],
 ['What has green hair and runs through the forest?', 'Moldy locks.'],
 ['Where do ghosts pick up their mail?', 'At the ghost office.'],
 ['Why do dinosaurs have long necks?', 'Because their feet smell.'],
 ['What do mermaids have on toast?', 'Mermarlade.'],
 ['Why do elephants never forget?', 'Because nobody ever tells them anything.'],
 ["What's in the middle of a jellyfish?", 'A jellybutton.'],
 ['What do you call a very popular perfume?', 'A best-smeller.'],
 ["Why can't you play jokes on snakes?", 'Because you can never pull their legs.'],
 ['Why did the baker stop making donuts?', 'He got sick of the hole business.'],
 ['Why do mummies make excellent spies?', "They're good at keeping things under wraps."],
 ['How do you stop an elephant from going through the eye of a needle?', 'Tie a knot in its tail.'],
 ["What goes 'Ha Ha Ha Thud'?", 'Someone laughing his head off.'],
 ["My friend thinks he's a rubber band.", 'I told him to snap out of it.'],
 ["My sister thinks she's a pair of curtains.", 'I told her to pull herself together!'],
 ['Did you hear about the dentist that married the manicurist?', 'Within a month they were fighting tooth and nail.'],
 ['Why do hummingbirds hum?', "Because they don't know the words."],
 ['Why did the baby turkey bolt down his food?', 'Because he was a little gobbler.'],
 ['Where did the whale go when it was bankrupt?', 'To the loan shark.'],
 ['How does a sick sheep feel?', 'Baah-aahd.'],
 ["What's gray, weighs 10 pounds and squeaks?", 'A mouse that needs to go on a diet.'],
 ['Why did the dog chase his tail?', 'To make ends meet.'],
 ['Why do elephants wear running shoes?', 'For jogging of course.'],
 ['Why are elephants big and gray?', "Because if they were small and yellow they'd be canaries."],
 ['If athletes get tennis elbow what do astronauts get?', 'Missile toe.'],
 ['Did you hear about the man who hated Santa?', 'He suffered from Claustrophobia.'],
 ['Why did Joey sprinkle sugar on his pillow?', 'Because he wanted to have sweet dreams.'],
 ['Why did Goshi take his comb to the dentist?', 'Because it had lost all its teeth.'],
 ['Why did Denial wear his shirt in the bath?', 'Because the label said wash and wear.'],
 ['Why did the dirty chicken cross the road?', 'For some fowl purpose.'],
 ["Why didn't the skeleton go to the party?", 'He had no body to go with.'],
 ['Why did the burglar take a shower?', 'To make a clean getaway.'],
 ['Why does a sheep have a woolly coat?', "Because he'd look silly in a plastic one."],
 ['Why do potatoes argue all the time?', "They can't see eye to eye."],
 ['Why did Quackity sleep with a banana peel?', 'So he could slip out of bed in the morning.'],
 ['Why did the mouse wear brown sneakers?', 'His white ones were in the wash.'],
 ['Why are false teeth like stars?', 'They come out at night.'],
 ['Why are Saturday and Sunday so strong?', 'Because the others are weekdays.'],
 ['Why did the archaeologist go bankrupt?', 'Because his career was in ruins.'],
 ['What do you get if you cross the Atlantic on the Titanic?', 'Very wet.'],
 ['What do you get if you cross a chicken with cement?', 'A brick-layer.'],
 ['What do you get if you cross a dog with a phone?', 'A golden receiver.'],
 ['What do you get if you cross an elephant with a shark?', 'Swimming trunks with sharp teeth.'],
 ['What did the tablecloth say to the table?', "Don't move, I've got you covered."],
 ['Did you hear about the time Nick ate a candle?', 'He wanted a light snack.'],
 ['What did the balloon say to the pin?', 'Hi Buster.'],
 ['What did the big chimney say to the little chimney?', "You're too young to smoke."],
 ['What did the carpet say to the floor?', 'I got you covered.'],
 ['What did the necklace say to the hat?', "You go ahead, I'll hang around."],
 ['What goes zzub-zzub?', 'A bee flying backwards.'],
 ['How do you communicate with a fish?', 'Drop him a line.'],
 ["What do you call a dinosaur that's never late?", 'A prontosaurus.'],
 ['What do you get if you cross a bear and a skunk?', 'Winnie-the-phew.'],
 ['How do you clean a tuba?', 'With a tuba toothpaste.'],
 ['What do frogs like to sit on?', 'Toadstools.'],
 ['Why was the math book unhappy?', 'It had too many problems.'],
 ['Why was the school clock punished?', 'It tocked too much.'],
 ["What's a polygon?", 'A dead parrot.'],
 ['What needs a bath and keeps crossing the street?', 'A dirty double crosser.'],
 ['What do you get if you cross a camera with a crocodile?', 'A snap shot.'],
 ['What do you get if you cross an elephant with a canary?', 'A very messy cage.'],
 ['What do you get if you cross a jeweler with a plumber?', 'A ring around the bathtub.'],
 ['What do you get if you cross an elephant with a crow?', 'Lots of broken telephone poles.'],
 ['What do you get if you cross a plum with a tiger?', 'A purple people eater.'],
 ["What's the best way to save water?", 'Dilute it.'],
 ["What's a lazy shoe called?", 'A loafer.'],
 ["What's green, noisy and dangerous?", 'A thundering herd of cucumbers.'],
 ['What color is a shout?', 'Yellow!'],
 ['What do you call a sick duck?', 'A mallardy.'],
 ["What's worse then a giraffe with a sore throat?", "A centipede with athlete's foot."],
 ['What goes ABC...slurp...DEF...slurp?', 'Someone eating alphabet soup.'],
 ["What's green and jumps up and down?", 'Lettuce at a dance.'],
 ["What's a cow after she gives birth?", 'De-calf-inated.'],
 ['What do you get if you cross a cow and a camel?', 'Lumpy milk shakes.'],
 ["What's white with black and red spots?", 'A Dalmatian with measles.'],
 ["What's brown has four legs and a trunk?", 'A mouse coming back from vacation.'],
 ["What does a skunk do when it's angry?", 'It raises a stink.'],
 ["What's gray, weighs 200 pounds and says, Here Kitty, kitty?", 'A 200 pound mouse.'],
 ["What's the best way to catch a squirrel?", 'Climb a tree and act like a nut.'],
 ["What's the best way to catch a rabbit?", 'Hide in a bush and make a noise like lettuce.'],
 ['What do you call a spider that just got married?', 'A newly web.'],
 ['What do you call a duck that robs banks?', 'A safe quacker.'],
 ["What's furry, meows and chases mice underwater?", 'A catfish.'],
 ["What's a funny egg called?", 'A practical yolker.'],
 ["What's green on the outside and yellow inside?", 'A banana disguised as a cucumber.'],
 ['What did the elephant say to the lemon?', "Let's play squash."],
 ['What weighs 4 tons, has a trunk and is bright red?', 'An embarrassed elephant.'],
 ["What's gray, weighs 4 tons, and wears glass slippers?", 'Cinderelephant.'],
 ["What's an elephant in a fridge called?", 'A very tight squeeze.'],
 ['What did the elephant say to her naughty child?', 'Tusk!  Tusk!'],
 ['What did the peanut say to the elephant?', "Nothing -- Peanuts can't talk."],
 ['What do elephants say when they bump into each other?', "Small world, isn't it?"],
 ['What did the cashier say to the register?', "I'm counting on you."],
 ['What did the flea say to the other flea?', 'Shall we walk or take the cat?'],
 ['What did the big hand say to the little hand?', 'Got a minute.'],
 ['What does the sea say to the sand?', 'Not much.  It usually waves.'],
 ['What did the stocking say to the shoe?', 'See you later, I gotta run.'],
 ['What did one tonsil say to the other tonsil?', 'It must be spring, here comes a swallow.'],
 ['What did the soil say to the rain?', 'Stop, or my name is mud.'],
 ['What did the puddle say to the rain?', 'Drop in sometime.'],
 ['What did the bee say to the rose?', 'Hi, bud.'],
 ['What did the appendix say to the kidney?', "The doctor's taking me out tonight."],
 ['What did the window say to the venetian blinds?', "If it wasn't for you it'd be curtains for me."],
 ['What did the doctor say to the sick orange?', 'Are you peeling well?'],
 ['What do you get if you cross a chicken with a banjo?', 'A self-plucking chicken.'],
 ['What do you get if you cross a hyena with a bouillon cube?', 'An animal that makes a laughing stock of itself.'],
 ['What do you get if you cross a rabbit with a spider?', 'A hare net.'],
 ['What do you get if you cross a germ with a comedian?', 'Sick jokes.'],
 ['What do you get if you cross a hyena with a mynah bird?', 'An animal that laughs at its own jokes.'],
 ['What do you get if you cross a railway engine with a stick of gum?', 'A chew-chew train.'],
 ['What would you get if you crossed an elephant with a computer?', 'A big know-it-all.'],
 ['What would you get if you crossed an elephant with a skunk?', 'A big stinker.']]
MovieHealLaughterMisses = ('hmm',
 'heh',
 'ha',
 'harr harr')
MovieHealLaughterHits1 = ('Ha Ha Ha',
 'Hee Hee',
 'Tee Hee',
 'Ha Ha')
MovieHealLaughterHits2 = ('BWAH HAH HAH!', 'HO HO HO!', 'HA HA HA!')
MovieSOSCallHelp = '%s HELP!'
MovieSOSWhisperHelp = '%s needs help in battle!'
MovieSOSObserverHelp = 'HELP!'
MovieNPCSOSGreeting = 'Hi %s! Glad to help!'
MovieNPCSOSGreetingLeo = ['By the power of magic, Leo is here to help!', 'Having trouble with these Cogs? Leo is here to help!', 'Did someone call for Leo?', "I don't get paid enough for this job. Whatever."]
MovieNPCSOSGoodbye = 'See you later!'
MovieNPCSOSGoodbyeLeo = "I have to leave now. Don't tell Flippy that I implemented the Cogs!"
MovieNPCSOSToonsHit = 'Toons Always Hit!'
MovieNPCSOSCogsMiss = 'Cogs Always Miss!'
MovieNPCSOSGagsOrganicP = 'All Gags Organic For %s Rounds!'
MovieNPCSOSGagsOrganicS = 'All Gags Organic For 1 Round!'
MovieNPCSOSDoodlesPowerP = 'Doodles Always Hit and Heal 3x For %s Rounds!'
MovieNPCSOSDoodlesPowerS = 'Doodles Always Hit and Heal 3x For 1 Round!'
MovieNPCSOSBonusPowerUp = 'Bonus Power Up!'
MovieNPCSOSRestockGags = 'Restocking %s gags!'
MovieNPCSOSHeal = 'Toon-up'
MovieNPCSOSTrap = 'Trap'
MovieNPCSOSLure = 'Lure'
MovieNPCSOSSound = 'Sound'
MovieNPCSOSThrow = 'Throw'
MovieNPCSOSSquirt = 'Squirt'
MovieNPCSOSDrop = 'Drop'
MovieNPCSOSAll = 'All'
MoviePetSOSTrickFail = 'Sigh...'
MoviePetSOSTrickSucceedBoy = 'Good boy!'
MoviePetSOSTrickSucceedGirl = 'Good girl!'
MovieSuitCancelled = 'CANCELLED\nCANCELLED\nCANCELLED'
RewardPanelToonTasks = 'ToonTasks'
RewardPanelItems = 'Items Recovered'
RewardPanelMissedItems = 'Items Not Recovered'
RewardPanelQuestLabel = 'Quest %s'
RewardPanelCongratsStrings = ['Yeah!',
 'Congratulations!',
 'Wow!',
 'Cool!',
 'Awesome!',
 'Toon-tastic!']
RewardPanelNewGag = 'New %(gagName)s gag for %(avName)s!'
RewardPanelEndTrack = 'Yay! %(avName)s has reached the end of the %(gagName)s Gag Track!'
RewardPanelMeritsMaxed = 'Maxed'
RewardPanelMeritBarLabels = ['Stock Options',
 'Jury Notices',
 'Cogbucks',
 'Merits']
RewardPanelMeritAlert = 'Ready for promotion!'
RewardPanelCogPart = 'You gained a Cog disguise part!'
RewardPanelPromotion = 'Ready for promotion in %s  track!'
RewardPanelSkip = 'Skip'
SuitFlunky = 'Flunky'
SuitPencilPusher = 'Pencil Pusher'
SuitYesman = 'Yesman'
SuitMicromanager = 'Micro\x03manager'
SuitDownsizer = 'Downsizer'
SuitHeadHunter = 'Head Hunter'
SuitCorporateRaider = 'Corporate Raider'
SuitTheBigCheese = 'The Big Cheese'
SuitColdCaller = 'Cold Caller'
SuitTelemarketer = 'Tele\x03marketer'
SuitNameDropper = 'Name Dropper'
SuitGladHander = 'Glad Hander'
SuitMoverShaker = 'Mover & Shaker'
SuitTwoFace = 'Two-Face'
SuitTheMingler = 'The Mingler'
SuitMrHollywood = 'Mr. Hollywood'
SuitShortChange = 'Short Change'
SuitPennyPincher = 'Penny Pincher'
SuitTightwad = 'Tightwad'
SuitBeanCounter = 'Bean Counter'
SuitNumberCruncher = 'Number Cruncher'
SuitMoneyBags = 'Money Bags'
SuitLoanShark = 'Loan Shark'
SuitRobberBaron = 'Robber Baron'
SuitBottomFeeder = 'Bottom Feeder'
SuitBloodsucker = 'Blood\x03sucker'
SuitDoubleTalker = 'Double Talker'
SuitAmbulanceChaser = 'Ambulance Chaser'
SuitBackStabber = 'Back Stabber'
SuitSpinDoctor = 'Spin Doctor'
SuitLegalEagle = 'Legal Eagle'
SuitBigWig = 'Big Wig'
SuitTestTubeBaby = 'Test Tube Baby'
SuitLabRat = 'Lab Rat'
SuitHeadshrinker = 'Headshrinker'
SuitPathogrind = 'Pathogrind'
SuitWitchDoctor = 'Witch Doctor'
SuitTheBioHazard = 'The Bio-Hazard'
SuitSteveNHawk = 'Steve N. Hawk'
SuitFrankNStine = 'Frank N. Stine'
SuitFlunkyS = 'a Flunky'
SuitPencilPusherS = 'a Pencil Pusher'
SuitYesmanS = 'a Yesman'
SuitMicromanagerS = 'a Micromanager'
SuitDownsizerS = 'a Downsizer'
SuitHeadHunterS = 'a Head Hunter'
SuitCorporateRaiderS = 'a Corporate Raider'
SuitTheBigCheeseS = 'a The Big Cheese'
SuitColdCallerS = 'a Cold Caller'
SuitTelemarketerS = 'a Telemarketer'
SuitNameDropperS = 'a Name Dropper'
SuitGladHanderS = 'a Glad Hander'
SuitMoverShakerS = 'a Mover & Shaker'
SuitTwoFaceS = 'a Two-Face'
SuitTheMinglerS = 'a Mingler'
SuitMrHollywoodS = 'a Mr. Hollywood'
SuitShortChangeS = 'a Short Change'
SuitPennyPincherS = 'a Penny Pincher'
SuitTightwadS = 'a Tightwad'
SuitBeanCounterS = 'a Bean Counter'
SuitNumberCruncherS = 'a Number Cruncher'
SuitMoneyBagsS = 'a Money Bags'
SuitLoanSharkS = 'a Loan Shark'
SuitRobberBaronS = 'a Robber Baron'
SuitBottomFeederS = 'a Bottom Feeder'
SuitBloodsuckerS = 'a Bloodsucker'
SuitDoubleTalkerS = 'a Double Talker'
SuitAmbulanceChaserS = 'an Ambulance Chaser'
SuitBackStabberS = 'a Back Stabber'
SuitSpinDoctorS = 'a Spin Doctor'
SuitLegalEagleS = 'a Legal Eagle'
SuitBigWigS = 'a Big Wig'
SuitTestTubeBabyS = 'a Test Tube Baby'
SuitLabRatS = 'a Lab Rat'
SuitHeadshrinkerS = 'a Headshrinker'
SuitPathogrindS = 'a Pathogrind'
SuitWitchDoctorS = 'a Witch Doctor'
SuitTheBioHazardS = 'a Bio-Hazard'
SuitSteveNHawkS = 'a Steve N. Hawk'
SuitFrankNStineS = 'a Frank N. Stine'
SuitFlunkyP = 'Flunkies'
SuitPencilPusherP = 'Pencil Pushers'
SuitYesmanP = 'Yesmen'
SuitMicromanagerP = 'Micromanagers'
SuitDownsizerP = 'Downsizers'
SuitHeadHunterP = 'Head Hunters'
SuitCorporateRaiderP = 'Corporate Raiders'
SuitTheBigCheeseP = 'The Big Cheeses'
SuitColdCallerP = 'Cold Callers'
SuitTelemarketerP = 'Telemarketers'
SuitNameDropperP = 'Name Droppers'
SuitGladHanderP = 'Glad Handers'
SuitMoverShakerP = 'Movers & Shakers'
SuitTwoFaceP = 'Two-Faces'
SuitTheMinglerP = 'Minglers'
SuitMrHollywoodP = 'Mr. Hollywoods'
SuitShortChangeP = 'Short Changes'
SuitPennyPincherP = 'Penny Pinchers'
SuitTightwadP = 'Tightwads'
SuitBeanCounterP = 'Bean Counters'
SuitNumberCruncherP = 'Number Crunchers'
SuitMoneyBagsP = 'Money Bags'
SuitLoanSharkP = 'Loan Sharks'
SuitRobberBaronP = 'Robber Barons'
SuitBottomFeederP = 'Bottom Feeders'
SuitBloodsuckerP = 'Bloodsuckers'
SuitDoubleTalkerP = 'Double Talkers'
SuitAmbulanceChaserP = 'Ambulance Chasers'
SuitBackStabberP = 'Back Stabbers'
SuitSpinDoctorP = 'Spin Doctors'
SuitLegalEagleP = 'Legal Eagles'
SuitBigWigP = 'Big Wigs'
SuitTestTubeBabyP = 'Test Tube Babies'
SuitLabRatP = 'Lab Rats'
SuitHeadshrinkerP = 'Headshrinkers'
SuitPathogrindP = 'Pathogrinds'
SuitWitchDoctorP = 'Witch Doctors'
SuitTheBioHazardP = 'Bio-Hazards'
SuitSteveNHawkP = 'Steve N. Hawks'
SuitFrankNStineP = 'Frank N. Stines'
SuitFaceoffDefaultTaunts = ['Boo!']
SuitAttackDefaultTaunts = ['Take that!', 'Take a memo on this!']
SuitAttackNames = {'Audit': 'Audit!',
 'Barrier': 'Barrier!',
 'Bite': 'Bite!',
 'BounceCheck': 'Bounce Check!',
 'BrainStorm': 'Brain Storm!',
 'BuzzWord': 'Buzz Word!',
 'Calculate': 'Calculate!',
 'Canned': 'Canned!',
 'Chomp': 'Chomp!',
 'CigarSmoke': 'Cigar Smoke!',
 'ClipOnTie': 'Clip On Tie!',
 'CogUp': 'Cog-Up!',
 'Crunch': 'Crunch!',
 'Demotion': 'Demotion!',
 'Downsize': 'Downsize!',
 'DoubleTalk': 'Double Talk!',
 'DropAnvil': 'Drop Anvil!',
 'EvictionNotice': 'Eviction Notice!',
 'EvilEye': 'Evil Eye!',
 'Filibuster': 'Filibuster!',
 'FillWithLead': 'Fill With Lead!',
 'FiveOClockShadow': "Five O'Clock Shadow!",
 'FingerWag': 'Finger Wag!',
 'Fired': 'Fired!',
 'FloodTheMarket': 'Flood The Market!',
 'FountainPen': 'Fountain Pen!',
 'FreezeAssets': 'Freeze Assets!',
 'Gavel': 'Gavel!',
 'GlowerPower': 'Glower Power!',
 'GuiltTrip': 'Guilt Trip!',
 'HalfWindsor': 'Half Windsor!',
 'HangUp': 'Hang Up!',
 'HeadShrink': 'Head Shrink!',
 'HotAir': 'Hot Air!',
 'Jargon': 'Jargon!',
 'Legalese': 'Legalese!',
 'Liquidate': 'Liquidate!',
 'MarketCrash': 'Market Crash!',
 'MumboJumbo': 'Mumbo Jumbo!',
 'ParadigmShift': 'Paradigm Shift!',
 'PeckingOrder': 'Pecking Order!',
 'PickPocket': 'Pick Pocket!',
 'PinkSlip': 'Pink Slip!',
 'PlayHardball': 'Play Hardball!',
 'PoundKey': 'Pound Key!',
 'PowerTie': 'Power Tie!',
 'PowerTrip': 'Power Trip!',
 'Quake': 'Quake!',
 'RazzleDazzle': 'Razzle Dazzle!',
 'RedTape': 'Red Tape!',
 'ReOrg': 'Re-Org!',
 'RestrainingOrder': 'Restraining Order!',
 'Rolodex': 'Rolodex!',
 'RubberStamp': 'Rubber Stamp!',
 'RubOut': 'Rub Out!',
 'Sacked': 'Sacked!',
 'SandTrap': 'Sand Trap!',
 'Schmooze': 'Schmooze!',
 'Shake': 'Shake!',
 'Shred': 'Shred!',
 'SongAndDance': 'Song And Dance!',
 'Spin': 'Spin!',
 'Synergy': 'Synergy!',
 'Tabulate': 'Tabulate!',
 'TeeOff': 'Tee Off!',
 'ThrowBook': 'Throw Book!',
 'Tremor': 'Tremor!',
 'Watercooler': 'Watercooler!',
 'Withdrawal': 'Withdrawal!',
 'WriteOff': 'Write Off!'}
SuitAttackTaunts = {'Audit': ["I believe your books don't balance.",
           "Looks like you're in the red.",
           'Let me help you with your books.',
           'Your debit column is much too high.',
           "Let's check your assets.",
           'This will put you in debt.',
           "Let's take a close look at what you owe.",
           'This should drain your account.',
           'Time for you to account for your expenses.',
           "I've found an error in your books."],
 'Barrier': ["We need to build a wall, and I'll have the Toons pay for that wall.", # TODO: make quotes for me!
             "I shall shut you down until my wall is fully built!",
             "We need to build a wall, and I'm not giving up on that wall!",
             'Building the complete wall will only take a small loan of five billion jellybeans!'],
 'Bite': ['Would you like a bite?',
          'Try a bite of this!',
          "You're biting off more than you can chew.",
          'My bite is bigger than my bark.',
          'Bite down on this!',
          'Watch out, I may bite.',
          "I don't just bite when I'm cornered.",
          "I'm just gonna grab a quick bite.",
          "I haven't had a bite all day.",
          'I just want a bite.  Is that too much to ask?'],
 'BounceCheck': ["Ah, too bad, you're funless.",
                 'You have a payment due.',
                 'I believe this check is yours.',
                 'You owed me for this.',
                 "I'm collecting on this debt.",
                 "This check isn't going to be tender.",
                 "You're going to be charged for this.",
                 'Check this out.',
                 'This is going to cost you.',
                 "I'd like to cash this in.",
                 "I'm just going to kick this back to you.",
                 'This is one sour note.',
                 "I'm deducting a service charge."],
 'BrainStorm': ['I forecast rain.',
                'Hope you packed your umbrella.',
                'I want to enlighten you.',
                'How about a few rain DROPS?',
                'Not so sunny now, are you Toon?',
                'Ready for a down pour?',
                "I'm going to take you by storm.",
                'I call this a lightning attack.',
                'I love to be a wet blanket.'],
 'BuzzWord': ['Pardon me if I drone on.',
              'Have you heard the latest?',
              'Can you catch on to this?',
              'See if you can hum this Toon.',
              'Let me put in a good word for you.',
              'I\'ll "B" perfectly clear.',
              'You should "B" more careful.',
              'See if you can dodge this swarm.',
              "Careful, you're about to get stung.",
              'Looks like you have a bad case of hives.'],
 'Calculate': ['These numbers do add up!',
               'Did you count on this?',
               "Add it up, you're going down.",
               'Let me help you add this up.',
               'Did you register all your expenses?',
               "According to my calculations, you won't be around much longer.",
               "Here's the grand total.",
               'Wow, your bill is adding up.',
               'Try fiddling with these numbers!',
               Cogs + ': 1 Toons: 0'],
 'Canned': ['Do you like it out of the can?',
            '"Can" you handle this?',
            "This one's fresh out of the can!",
            'Ever been attacked by canned goods before?',
            "I'd like to donate this canned good to you!",
            'Get ready to "Kick the can"!',
            'You think you "can", you think you "can".',
            "I'll throw you in the can!",
            "I'm making me a can o' toon-a!",
            "You don't taste so good out of the can."],
 'Chomp': ['Take a look at these chompers!',
           'Chomp, chomp, chomp!',
           "Here's something to chomp on.",
           'Looking for something to chomp on?',
           "Why don't you chomp on this?",
           "I'm going to have you for dinner.",
           'I love to feed on Toons!'],
 'CigarSmoke': ['Gentlemen.',
                "It's a good day to have a smoke.",
                'Take a breath of this.',
                "It's tradition you know.",
                'Another day another dollar.',
                'I always have the occasional cigar.',
                'I need a good smoke.',
                'Smoking is a dirty habit.'],
 'ClipOnTie': ['Better dress for our meeting.',
               "You can't go OUT without your tie.",
               'The best dressed ' + Cogs + ' wear them.',
               'Try this on for size.',
               'You should dress for success.',
               'No tie, no service.',
               'Do you need help putting this on?',
               'Nothing says powerful like a good tie.',
               "Let's see if this fits.",
               'This is going to choke you up.',
               "You'll want to dress up before you go OUT.",
               "I think I'll tie you up."],
 'CogUp': ['Like a good neighbor, Medic is there!',
           "Fallen and can't get up? Not in my presence.",
           'Toon-Up? What a bad joke.',
           "Don't mind me. I do this on a regular basis."],
 'Crunch': ["Looks like you're in a crunch.",
            "It's crunch time!",
            "I'll give you something to crunch on!",
            'Crunch on this!',
            'I pack quite a crunch.',
            'Which do you prefer, smooth or crunchy?',
            "I hope you're ready for crunch time.",
            "It sounds like you're getting crunched!",
            "I'll crunch you like a can."],
 'Demotion': ["You're moving down the corporate ladder.",
              "I'm sending you back to the Mail Room.",
              'Time to turn in your nameplate.',
              "You're going down, clown.",
              "Looks like you're stuck.",
              "You're going nowhere fast.",
              "You're in a dead end position.",
              "You won't be moving anytime soon.",
              "You're not going anywhere.",
              'This will go on your permanent record.'],
 'Downsize': ['Come on down!',
              'Do you know how to get down?',
              "Let's get down to business.",
              "What's wrong? You look down.",
              'Going down?',
              "What's goin' down? You!",
              'Why pick on people my own size?',
              "Why don't I size you up, or should I say, down?",
              'Would you like a smaller size for just a quarter more?',
              'Try this on for size!',
              'You can get this in a smaller size.',
              'This attack is one size fits all!'],
 'DropAnvil': ['Drop another anvil!',
               "Did someone say 'drop'?",
               "Watch out, Toon. You don't know what's dropping at you.",
               "What's dropping? Your Laff points!",
               "It's time to drop!",
               'Stop, drop, and roll!'],
 'EvictionNotice': ["It's moving time.",
                    'Pack your bags, Toon.',
                    'Time to make some new living arrangements.',
                    'Consider yourself served.',
                    "You're behind on your lease.",
                    'This will be extremely unsettling.',
                    "You're about to be uprooted.",
                    "I'm going to send you packing.",
                    "You're out of place.",
                    'Prepare to be relocated.',
                    "You're in a hostel position."],
 'EvilEye': ["I'm giving you the evil eye.",
             'Could you eye-ball this for me?',
             "Wait.  I've got something in my eye.",
             "I've got my eye on you!",
             'Could you keep an eye on this for me?',
             "I've got a real eye for evil.",
             "I'll poke you in the eye!",
             '"Eye" am as evil as they come!',
             "I'll put you in the eye of the storm!",
             "I'm rolling my eye at you."],
 'Filibuster': ["Shall I fill 'er up?",
                'This is going to take awhile.',
                'I could do this all day.',
                "I don't even need to take a breath.",
                'I keep going and going and going.',
                'I never get tired of this one.',
                'I can talk a blue streak.',
                'Mind if I bend your ear?',
                "I think I'll shoot the breeze.",
                'I can always get a word in edgewise.'],
 'FingerWag': ['I have told you a thousand times.',
               'Now see here Toon.',
               "Don't make me laugh.",
               "Don't make me come over there.",
               "I'm tired of repeating myself.",
               "I believe we've been over this.",
               'You have no respect for us ' + Cogs + '.',
               "I think it's time you pay attention.",
               'Blah, Blah, Blah, Blah, Blah.',
               "Don't make me stop this meeting.",
               'Am I going to have to separate you?',
               "We've been through this before."],
 'Fired': ['I hope you brought some marshmallows.',
           "It's going to get rather warm around here.",
           'This should take the chill out of the air.',
           "I hope you're cold blooded.",
           'Hot, hot and hotter.',
           'You better stop, drop, and roll!',
           "You're outta here.",
           'How does "well-done" sound?',
           'Can you say ouch?',
           'Hope you wore sunscreen.',
           'Do you feel a little toasty?',
           "You're going down in flames.",
           "You'll go out in a blaze.",
           "You're a flash in the pan.",
           'I think I have a bit of a flare about me.',
           "I just sparkle, don't I?",
           'Oh look, a crispy critter.',
           "You shouldn't run around half baked."],
 'FountainPen': ['This is going to leave a stain.',
                 "Let's ink this deal.",
                 'Be prepared for some permanent damage.',
                 "You're going to need a good dry cleaner.",
                 'You should change.',
                 'This fountain pen has such a nice font.',
                 "Here, I'll use my pen.",
                 'Can you read my writing?',
                 'I call this the plume of doom.',
                 "There's a blot on your performance.",
                 "Don't you hate when this happens?"],
 'FreezeAssets': ['Your assets are mine.',
                  'Do you feel a draft?',
                  "Hope you don't have plans.",
                  'This should keep you on ice.',
                  "There's a chill in the air.",
                  'Winter is coming early this year.',
                  'Are you feeling a little blue?',
                  'Let me crystallize my plan.',
                  "You're going to take this hard.",
                  'This should cause freezer burn.',
                  'I hope you like cold cuts.',
                  "I'm very cold blooded."],
 'Gavel': ['Order in the court!',
            'Judging for the Cogs in the amount of 5,000 Cogbucks.',
            'Objection sustained.',
            'You have been convicted of attacks against the Cogs.',
            "Your opening statement?"],
 'GlowerPower': ['You looking at me?',
                 "I'm told I have very piercing eyes.",
                 'I like to stay on the cutting edge.',
                 "Jeepers, Creepers, don't you love my peepers?",
                 "Here's looking at you kid.",
                 "How's this for expressive eyes?",
                 'My eyes are my strongest feature.',
                 'The eyes have it.',
                 'Peeka-boo, I see you.',
                 'Look into my eyes...',
                 'Shall we take a peek at your future?'],
 'GuiltTrip': ["I'll lay a real guilt trip on you!",
               'Feeling guilty?',
               "It's all your fault!",
               'I always blame everything on you.',
               'Wallow in your own guilt!',
               'Did you have a nice trip?',
               "You had better say you're sorry.",
               "I  wouldn't forgive you in a million years!",
               'See you next fall.',
               'Call me when you get back from your trip.',
               'When do you get back from your trip?'],
 'HalfWindsor': ["This is the fanciest tie you'll ever see!",
                 'Try not to get too winded.',
                 "This isn't even half the trouble you're in.",
                 "You're lucky I don't have a whole windsor.",
                 "You can't afford this tie.",
                 "I bet you've never even SEEN a half windsor!",
                 'This tie is out of your league.',
                 "I shouldn't even waste this tie on you.",
                 "You're not even worth half of this tie!"],
 'HangUp': ["You've been disconnected.",
            'Good bye!',
            "It's time I end our connection.",
            "...and don't call back!",
            'Click!',
            'This conversation is over.',
            "I'm severing this link.",
            'I think you have a few hang ups.',
            "It appears you've got a weak link.",
            'Your time is up.',
            'I hope you receive this loud and clear.',
            'You got the wrong number.'],
 'HeadShrink': ["Looks like you're seeing a shrink.",
                'Honey, I shrunk the toon.',
                "Hope this doesn't shrink your pride.",
                'Do you shrink in the wash?',
                'I shrink therefore I am.',
                "It's nothing to lose your head over.",
                'Are you going out of your head?',
                'Heads up! Or should I say, down.',
                'Objects may be larger than they appear.',
                'Good Toons come in small packages.'],
 'HotAir': ["We're having a heated discussion.",
            "You're experiencing a heat wave.",
            "I've reached my boiling point.",
            'This should cause some wind burn.',
            'I hate to grill you, but...',
            "Always remember, where there's smoke, there's fire.",
            "You're looking a little burned out.",
            'Another meeting up in smoke.',
            "Guess it's time to add fuel to the fire.",
            'Let me kindle a working relationship.',
            'I have some glowing remarks for you.',
            'Air Raid!!!'],
 'Jargon': ['What nonsense.',
            'See if you can make sense of this.',
            'I hope you get this loud and clear.',
            "Looks like I'm going to have to raise my voice.",
            'I insist on having my say.',
            "I'm very outspoken.",
            'I must pontificate on this subject.',
            'See, words can hurt you.',
            'Did you catch my meaning?',
            'Words, words, words, words, words.'],
 'Legalese': ['You must cease and desist.',
              'You will be defeated, legally speaking.',
              'Are you aware of the legal ramifications?',
              "You aren't above the law!",
              'There should be a law against you.',
              "There's no ex post facto with me!",
              "The opinions expressed in this attack are not those of Toontown.",
              'We cannot be held responsible for damages suffered in this attack.',
              'Your results for this attack may vary.',
              'This attack is void where prohibited.',
              "You don't fit into my legal system!",
              "You can't handle the legal matters."],
 'Liquidate': ['I like to keep things fluid.',
               'Are you having some cash flow problems?',
               "I'll have to purge your assets.",
               'Time for you to go with the flow.',
               "Remember it's slippery when wet.",
               'Your numbers are running.',
               'You seem to be slipping.',
               "It's all crashing down on you.",
               "I think you're diluted.",
               "You're all washed up."],
 'MarketCrash': ["I'm going to crash your party.",
                 "You won't survive the crash.",
                 "I'm more than the market can bear.",
                 "I've got a real crash course for you!",
                 "Now I'll come crashing down.",
                 "I'm a real bull in the market.",
                 'Looks like the market is going down.',
                 'You had better get out quick!',
                 'Sell! Sell! Sell!',
                 'Shall I lead the recession?',
                 "Everybody's getting out, shouldn't you?"],
 'MumboJumbo': ['Let me make this perfectly clear.',
                "It's as simple as this.",
                "This is how we're going to do this.",
                'Let me supersize this for you.',
                'You might call this technobabble.',
                'Here are my five-dollar words.',
                'Boy, this is a mouth full.',
                'Some call me bombastic.',
                'Let me just interject this.',
                'I believe these are the right words.'],
 'ParadigmShift': ["Watch out! I'm rather shifty.",
                   'Prepare to have your paradigm shifted!',
                   "Isn't this an interesting paradigm.",
                   "You'll get shifted out of place.",
                   "I guess it's your shift now.",
                   'Your shift is up!',
                   "You've never shifted this much in your life.",
                   "I'm giving you the bad shift!",
                   'Look into my shifty eyes!'],
 'PeckingOrder': ["This one's for the birds.",
                  'Get ready for a bird bath.',
                  "Looks like you're going to hit a birdie.",
                  'Some think this attack is fowl.',
                  "You're on the bottom of the pecking order.",
                  'A bird in my hand is worth ten on your head!',
                  'Your order is up; the pecking order!',
                  "Why don't I peck on someone my own size? Nah.",
                  'Birds of a feather strike together.'],
 'PickPocket': ['Let me check your valuables.',
                "Hey, what's that over there?",
                'Like taking candy from a baby.',
                'What a steal.',
                "I'll hold this for you.",
                'Watch my hands at all times.',
                'The hand is quicker than the eye.',
                "There's nothing up my sleeve.",
                'The management is not responsible for lost items.',
                "Finder's keepers.",
                "You'll never see it coming.",
                'One for me, none for you.',
                "Don't mind if I do.",
                "You won't be needing this..."],
 'PinkSlip': ['Try not to slip up.',
              "Are you frightened? You've turned pink!",
              'This one will surely slip you up.',
              'Oops, I guess you slipped there, huh?',
              "Watch yourself, wouldn't want to slip!",
              "This one's slippery when wet.",
              "I'll just slip this one in.",
              "Don't mind if you slip by, do you?",
              "Pink isn't really your color.",
              "Here's your pink slip, you're outta here!"],
 'PlayHardball': ['So you wanna play hardball?',
                  "You don't wanna play hardball with me.",
                  'Batter up!',
                  'Hey batter, batter!',
                  "And here's the pitch...",
                  "You're going to need a relief pitcher.",
                  "I'm going to knock you out of the park.",
                  "Once you get hit, you'll run home.",
                  'This is your final inning!',
                  "You can't play with me!",
                  "I'll strike you out.",
                  "I'm throwing you a real curve ball!"],
 'PoundKey': ['Time to return some calls.',
              "I'd like to make a collect call.",
              "Ring-a-ling - it's for you!",
              "I've been wanting to drop a pound or two.",
              'I have a lot of clout.',
              'This may cause a slight pounding sensation.',
              "I'll just punch in this number.",
              'Let me call up a little surprise.',
              "I'll ring you up.",
              "O.K. Toon, it's the pound for you."],
 'PowerTie': ["I'll call later, you looked tied up.",
              'Are you ready to tie die?',
              "Ladies and gentlemen, it's a tie!",
              'You had better learn how to tie.',
              "I'll have you tongue-tied!",
              "This is the worst tie you'll ever get!",
              'Can you feel the power?',
              'My powers are far too great for you!',
              "I've got the power!",
              "By the powers vested in me, I'll tie you up."],
 'PowerTrip': ["Pack your bags, we're taking a little trip.",
               'Did you have a nice trip?',
               "Nice trip, I guess I'll see you next fall.",
               'How was your trip?',
               'Sorry to trip you up there!',
               'You look a little tripped up.',
               "Now you see who's in power!",
               'I am much more powerful than you.',
               "Who's got the power now?",
               "You can't fight the power.",
               'Power corrupts, especially in my hands!'],
 'Quake': ["Let's quake, rattle, and roll.",
           "I've got a whole lot of quakin' goin' on!",
           "I see you quakin' in your shoes.",
           "Here it comes, it's the big one!",
           "This one's off the Richter scale.",
           'Now the earth will quake!',
           "Hey, what's shakin'? You!",
           'Ever been in an earthquake?',
           "You're on shaky ground now!"],
 'RazzleDazzle': ['Read my lips.',
                  'How about these choppers?',
                  "Aren't I charming?",
                  "I'm going to wow you.",
                  'My dentist does excellent work.',
                  "Blinding aren't they?",
                  "Hard to believe these aren't real.",
                  "Shocking, aren't they?",
                  "I'm going to cap this off.",
                  'I floss after every meal.',
                  'Say Cheese!'],
 'RedTape': ['This should wrap things up.',
             "I'm going to tie you up for awhile.",
             "You're on a roll.",
             'See if you can cut through this.',
             'This will get sticky.',
             "Hope you're claustrophobic.",
             "I'll make sure you stick around.",
             'Let me keep you busy.',
             'Just try to unravel this.',
             'I want this meeting to stick with you.'],
 'ReOrg': ["You don't like the way I reorganized things!",
           'Perhaps a little reorganization is in order.',
           "You're not that bad, you just need to be reorganized.",
           'Do you like my organizational skills.',
           "I just thought I'd give things a new look.",
           'You need to get organized!',
           "You're looking a little disorganized.",
           'Hold on while I reorganize your thoughts.',
           "I'll just wait for you to get a little organized.",
           "You don't mind if I just reorganize a bit?"],
 'RestrainingOrder': ['You should show a little restraint.',
                      "I'm slapping you with a restraining order!",
                      "You can't come within five feet of me.",
                      'Perhaps you better keep your distance.',
                      'You should be restrained.',
                      Cogs + '!  Restrain that Toon!',
                      'Try and restrain yourself.',
                      "I hope I'm being too much of a restraint on you.",
                      'See if you can lift these restraints!',
                      "I'm ordering you to restrain!",
                      "Why don't we start with basic restraining?"],
 'Rolodex': ["Your card's in here somewhere.",
             "Here's the number for a pest exterminator.",
             'I want to give you my card.',
             "I've got your number right here.",
             "I've got you covered from a-z.",
             "You'll flip over this.",
             'Take this for a spin.',
             'Watch out for paper cuts.',
             "I'll let my fingers do the knocking.",
             'Is this how I can contact you?',
             'I want to make sure we stay in touch.'],
 'RubberStamp': ['I always make a good impression.',
                 "It's important to apply firm and even pressure.",
                 'A perfect imprint every time.',
                 'I want to stamp you out.',
                 'You must be RETURNED TO SENDER.',
                 "You've been CANCELLED.",
                 'You have a PRIORITY delivery.',
                 "I'll make sure you RECEIVED my message.",
                 "You're not going anywhere - you have POSTAGE DUE.",
                 "I'll need a response ASAP."],
 'RubOut': ['And now for my disappearing act.',
            "I sense I've lost you somewhere.",
            'I decided to leave you out.',
            'I always rub out all obstacles.',
            "I'll just erase this error.",
            'I can make any nuisance disappear.',
            'I like things neat and tidy.',
            'Please try and stay animated.',
            "Now I see you...  now I don't.",
            'This will cause some fading.',
            "I'm going to eliminate the problem.",
            'Let me take care of your problem areas.'],
 'Sacked': ["Looks like you're getting sacked.",
            "This one's in the bag.",
            "You've been bagged.",
            'Paper or plastic?',
            'My enemies shall be sacked!',
            'I hold the Toontown record in sacks per game.',
            "You're no longer wanted around here.",
            "Your time is up around here, you're being sacked!",
            'Let me bag that for you.',
            'No defense can match my sack attack!'],
 'Schmooze': ["You'll never see this coming.",
              'This will look good on you.',
              "You've earned this.",
              "I don't mean to gush.",
              'Flattery will get me everywhere.',
              "I'm going to pile it on now.",
              'Time to lay it on thick.',
              "I'm going to get on your good side.",
              'That deserves a good slap on the back.',
              "I'm going to ring your praises.",
              'I hate to knock you off your pedestal, but...'],
 'Shake': ["You're right on the epicenter.",
           "You're standing on a fault line.",
           "It's going to be a bumpy ride.",
           'I think of this as a natural disaster.',
           "It's a disaster of seismic proportions.",
           "This one's off the Richter scale.",
           'Time to duck and cover.',
           'You seem disturbed.',
           'Ready for a jolt?',
           "I'll have you shaken, not stirred.",
           'This will shake you up.',
           'I suggest a good escape plan.'],
 'Shred': ['I need to get rid of some hazardous waste.',
           "I'm increasing my throughput.",
           "I think I'll dispose of you right now.",
           'This will get rid of the evidence.',
           "There's no way to prove it now.",
           'See if you can put this back together.',
           'This should cut you down to size.',
           "I'm going to rip that idea to shreds.",
           "We don't want this to fall into the wrong hands.",
           'Easy come, easy go.',
           "Isn't this your last shred of hope?"],
 'SongAndDance': ['Baby, baby, baby oh!',
                  'Let it go, let it go.',
                  'When you feel sad, dance!',
                  'Never miss a chance to dance!',
                  "Just shout whenever, and I'll be there",
                  'You know you love me, I know you care.'],
 'Spin': ['What do you say we go for a little spin?',
          'Do you use the spin cycle?',
          "This'll really make your head spin!",
          "Here's my spin on things.",
          "I'll take you for a spin.",
          'How do you like to "spin" your time?',
          "Watch it.  Wouldn't want to spin out of control!",
          "Oh what a spin you're in!",
          'My attacks will make your head spin!'],
 'Synergy': ["I'm taking this to committee.",
             "Your project's been cancelled.",
             "Your budget's been cut.",
             "We're restructuring your division.",
             'I put it to a vote, and you lose.',
             'I just received the final approval.',
             'A good team can get rid of any problem.',
             "I'll get back to you on this.",
             "Let's get right to business.",
             'Consider this a Synergy crisis.'],
 'Tabulate': ["This doesn't add up.",
              'By my count, you lose.',
              "You're racking up quite a tab.",
              "I'll have you totaled in a moment.",
              'Are you ready for these numbers?',
              'Your bill is now due and payable.',
              'Time for the reckoning.',
              'I like to put things in order.',
              'And the tally is...',
              'These numbers should prove to be quite powerful.'],
 'TeeOff': ["You're not up to par.",
            'Fore!',
            "I'm getting teed off.",
            "Caddie, I'll need my driver!",
            'Just try and avoid this hazard.',
            'Swing!',
            'This is a sure hole in one.',
            "You're in my fairway.",
            'Notice my grip.',
            'Watch the birdie!',
            'Keep your eye on the ball!',
            'Mind if I play through?'],
 'ThrowBook': ['My book from Law School should help.',
               'You better have a good lawyer.',
               "I'll have to take legal action.",
               'Legal Eagle will be pleased to see this.',
               'Objection!',
               'Under article 14 subsection C...',
               'I see you have broken the law!',
               "It seems you don't understand the authority of law.",
               "I'll see you in court, Toon."],
 'Tremor': ['Did you feel that?',
            'Not afraid of a little tremor are you?',
            'A tremor is only the beginning.',
            'You look jittery.',
            "I'll shake things up a bit!",
            'Are you ready to rumble?',
            "What's wrong? You look shaken.",
            'Tremor with fear!',
            'Why are you tremoring with fear?'],
 'Watercooler': ['This ought to cool you off.',
                 "Isn't this refreshing?",
                 'I deliver.',
                 'Straight from the tap - into your lap.',
                 "What's the matter, it's just spring water.",
                 "Don't worry, it's purified.",
                 'Ah, another satisfied customer.',
                 "It's time for your daily delivery.",
                 "Hope your colors don't run.",
                 'Care for a drink?',
                 'It all comes out in the wash.',
                 "The drink's on you."],
 'Withdrawal': ["I believe you're overdrawn.",
                'I hope your balance is high enough for this.',
                'Take that, with interest.',
                'Your balance is dropping.',
                "You're going to need to make a deposit soon.",
                "You've suffered an economic collapse.",
                "I think you're in a slump.",
                'Your finances have taken a decline.',
                'I foresee a definite downturn.',
                "It's a reversal of fortune."],
 'WriteOff': ['Let me increase your losses.',
              "Let's make the best of a bad deal.",
              'Time to balance the books.',
              "This won't look good on your books.",
              "I'm looking for some dividends.",
              'You must account for your losses.',
              'You can forget about a bonus.',
              "I'll shuffle your accounts around.",
              "You're about to suffer some losses.",
              'This is going to hurt your bottom line.']}
WaitingForOtherToons = 'Waiting for other toons...'
WaitingForOtherToonsDots = 'Waiting for other toons%s'
ElevatorHopOff = 'Hop off'
ElevatorLeaderOff = 'Only your leader can decide when to hop off.'
ElevatorHopOK = 'Okay'
ElevatorGroupMember = 'Only your group leader can\n decide when to board.'
CogsIncExt = ', Inc.'
CogsIncModifier = '%s' + CogsIncExt
CogsInc = Cogs.upper() + CogsIncExt
CogdominiumsExt = ' Field Office'
Cogdominiums = Cog.upper() + CogdominiumsExt
DoorKnockKnock = 'Knock, knock.'
DoorWhosThere = "Who's there?"
DoorWhoAppendix = ' who?'
DoorNametag = 'Door'
FADoorCodes_UNLOCKED = None
FADoorCodes_SUIT_APPROACHING = None
FADoorCodes_BUILDING_TAKEOVER = "Watch out! There's a Cog in there!"
FADoorCodes_SB_DISGUISE_INCOMPLETE = "You'll get caught going in there as a Toon! You need to complete your Sellbot Disguise first!\n\nBuild your Sellbot Disguise out of parts from the Factory."
FADoorCodes_CB_DISGUISE_INCOMPLETE = "You'll get caught going in there as a Toon! You need to complete your Cashbot Disguise first!\n\nBuild your Cashbot Disguise by doing ToonTasks in Daunting Dreamland."
FADoorCodes_LB_DISGUISE_INCOMPLETE = "You'll get caught going in there as a Toon! You need to complete your Lawbot Disguise first!\n\nBuild your Lawbot Disguise by doing the ToonTasks after Daunting Dreamland."
FADoorCodes_BB_DISGUISE_INCOMPLETE = "You'll get caught going in there as a Toon! You need to complete your Bossbot Disguise first!\n\nBuild your Bossbot Disguise by doing the ToonTasks after Daunting Dreamland."
KnockKnockJokes = [['Who', "Bad echo in here, isn't there?"],
 ['Dozen', 'Dozen anybody want to let me in?'],
 ['Freddie', 'Freddie or not, here I come.'],
 ['Dishes', 'Dishes your friend, let me in.'],
 ['Wooden shoe', 'Wooden shoe like to know.'],
 ['Betty', "Betty doesn't know who I am."],
 ['Kent', 'Kent you tell?'],
 ['Noah', "Noah don't know who either."],
 ["I don't know", 'Neither do I, I keep telling you that.'],
 ['Howard', 'Howard I know?'],
 ['Emma', 'Emma so glad you asked me that.'],
 ['Auto', "Auto know, but I've forgotten."],
 ['Jess', 'Jess me and my shadow.'],
 ['One', 'One-der why you keep asking that?'],
 ['Alma', 'Alma not going to tell you!'],
 ['Zoom', 'Zoom do you expect?'],
 ['Amy', "Amy fraid I've forgotten."],
 ['Arfur', 'Arfur got.'],
 ['Ewan', 'No, just me'],
 ['Cozy', "Cozy who's knocking will you?"],
 ['Sam', 'Sam person who knocked on the door last time.'],
 ['Fozzie', 'Fozzie hundredth time, my name is ' + Flippy + '.'],
 ['Deduct', 'Donald Deduct.'],
 ['Max', 'Max no difference, just open the door.'],
 ['N.E.', 'N.E. body you like, let me in.'],
 ['Amos', 'Amos-quito bit me.'],
 ['Alma', "Alma candy's gone."],
 ['Bruce', "I Bruce very easily, don't hit me."],
 ['Colleen', "Colleen up your room, it's filthy."],
 ['Elsie', 'Elsie you later.'],
 ['Hugh', 'Hugh is going to let me in?'],
 ['Hugo', "Hugo first - I'm scared."],
 ['Ida', 'Ida know.  Sorry!'],
 ['Isabel', 'Isabel on a bike really necessary?'],
 ['Joan', "Joan call us, we'll call you."],
 ['Kay', 'Kay, L, M, N, O, P.'],
 ['Justin', 'Justin time for dinner.'],
 ['Liza', 'Liza wrong to tell.'],
 ['Luke', 'Luke and see who it is.'],
 ['Mandy', "Mandy the lifeboats, we're sinking."],
 ['Max', 'Max no difference - just open the door!'],
 ['Nettie', 'Nettie as a fruitcake.'],
 ['Olivia', 'Olivia me alone!'],
 ['Oscar', 'Oscar stupid question, you get a stupid answer.'],
 ['Patsy', 'Patsy dog on the head, he likes it.'],
 ['Paul', "Paul hard, the door's stuck again."],
 ['Thea', 'Thea later, alligator.'],
 ['Tyrone', "Tyrone shoelaces, you're old enough."],
 ['Stella', 'Stella no answer at the door.'],
 ['Uriah', 'Keep Uriah on the ball.'],
 ['Dwayne', "Dwayne the bathtub.  I'm drowning."],
 ['Dismay', "Dismay be a joke, but it didn't make me laugh."],
 ['Ocelot', "Ocelot of questions, don't you?"],
 ['Thermos', 'Thermos be a better knock knock joke than this.'],
 ['Sultan', 'Sultan Pepper.'],
 ['Vaughan', 'Vaughan day my prince will come.'],
 ['Donald', 'Donald come baby, cradle and all.'],
 ['Lettuce', "Lettuce in, won't you?"],
 ['Ivor', 'Ivor sore hand from knocking on your door!'],
 ['Isabel', 'Isabel broken, because I had to knock.'],
 ['Heywood, Hugh, Harry', 'Heywood Hugh Harry up and open this door.'],
 ['Juan', "Juan of this days you'll find out."],
 ['Earl', 'Earl be glad to tell you if you open this door.'],
 ['Abbot', 'Abbot time you opened this door!'],
 ['Ferdie', 'Ferdie last time, open the door!'],
 ['Don', 'Don mess around, just open the door.'],
 ['Sis', 'Sis any way to treat a friend?'],
 ['Isadore', 'Isadore open or locked?'],
 ['Harry', 'Harry up and let me in!'],
 ['Theodore', "Theodore wasn't open so I knocked-knocked."],
 ['Ken', 'Ken I come in?'],
 ['Boo', "There's no need to cry about it."],
 ['You', 'You who!  Is there anybody there?'],
 ['Ice cream', "Ice cream if you don't let me in."],
 ['Sarah', "Sarah 'nother way into this building?"],
 ['Mikey', 'Mikey dropped down the drain.'],
 ['Doris', 'Doris jammed again.'],
 ['Yelp', 'Yelp me, the door is stuck.'],
 ['Scold', 'Scold outside.'],
 ['Diana', 'Diana third, can I have a drink please?'],
 ['Doris', 'Doris slammed on my finger, open it quick!'],
 ['Lettuce', 'Lettuce tell you some knock knock jokes.'],
 ['Izzy', 'Izzy come, izzy go.'],
 ['Omar', 'Omar goodness gracious - wrong door!'],
 ['Says', "Says me, that's who!"],
 ['Duck', "Just duck, they're throwing things at us."],
 ['Tank', "You're welcome."],
 ['Eyes', 'Eyes got loads more knock knock jokes for you.'],
 ['Pizza', 'Pizza cake would be great right now.'],
 ['Closure', 'Closure mouth when you eat.'],
 ['Harriet', "Harriet all my lunch, I'm starving."],
 ['Wooden', 'Wooden you like to know?'],
 ['Punch', 'Not me, please.'],
 ['Gorilla', 'Gorilla me a hamburger.'],
 ['Jupiter', "Jupiter hurry, or you'll miss the trolley."],
 ['Bertha', 'Happy Bertha to you!'],
 ['Cows', 'Cows go "moo" not "who."'],
 ['Tuna fish', "You can tune a piano, but you can't tuna fish."],
 ['Consumption', 'Consumption be done about all these knock knock jokes?'],
 ['Banana', 'Banana spilt so ice creamed.'],
 ['X', 'X-tremely pleased to meet you.'],
 ['Haydn', 'Haydn seek is fun to play.'],
 ['Rhoda', 'Rhoda boat as fast as you can.'],
 ['Quacker', "Quacker 'nother bad joke and I'm off!"],
 ['Nana', 'Nana your business.'],
 ['Ether', 'Ether bunny.'],
 ['Little old lady', "My, you're good at yodelling!"],
 ['Beets', 'Beets me, I forgot the joke.'],
 ['Hal', 'Halloo to you too!'],
 ['Sarah', 'Sarah doctor in the house?'],
 ['Aileen', 'Aileen Dover and fell down.'],
 ['Atomic', 'Atomic ache'],
 ['Agatha', 'Agatha headache.  Got an aspirin?'],
 ['Stan', "Stan back, I'm going to sneeze."],
 ['Hatch', 'Bless you.'],
 ['Ida', "It's not Ida who, it's Idaho."],
 ['Zippy', 'Mrs. Zippy.'],
 ['Yukon', 'Yukon go away and come back another time.']]
ScientistPhase1Dialogue = ['Fellow Toons, this is the Silly Meter!',
                           "It is tracking Toontown's rising silly levels...",
                           'Which are causing objects on the street to animate!',
                           'And YOU can help push these levels higher!',
                           'Battle Cogs to cause Silly Surges...',
                           'Make Toontown sillier than ever...',
                           "And let's watch the world come alive!",
                           "Now I'll repeat what I said, but only once more."]
ScientistPhase2Dialogue = ['Good Gag work, Toons!',
                           "You're keeping those silly levels rising...",
                           'And Toontown is getting sillier every day!',
                           'Fire hydrants, trash cans, and mailboxes are springing to life...',
                           'Making the world more animated than ever!',
                           "You know the Cogs aren't happy about this...",
                           'But Toons sure are!']
ScientistPhase3Dialogue = ['Gadzooks! The Silly Meter is even crazier than expected!',
                           'Your Silly Surges are working wonders...',
                           'And Toontown is getting more animated every day!',
                           'Keep up the good Gag work...',
                           'And lets see how silly we can make Toontown!',
                           "You know the Cogs aren't happy about what's going on...",
                           'But Toons sure are!']
ScientistPhase4Dialogue = ['YOU DID IT TOONS!',
                           'You brought the streets of Toontown to life!']
ScientistPhase5Dialogue = ['Attention all Toons!',
                           'The Cog invasions have been an unhappy event.',
                           'As a result, silly levels have rapidly fallen...',
                           'And no new objects are coming to life.',
                           'But those that have are very thankful...',
                           'And are showing their appreciation by helping in battle!',
                           'We may hold off the Cogs yet, so keep up the fight!']
ScientistPhase6Dialogue = ['Congratulations Toons!',
                          'You all succesfully held off the Cog Invasions...',
                          'With a little help from our newly animated friends...',
                          'And brought Toontown back to its usual silly self!',
                          'We hope to get the Silly Meter rising again soon...',
                          'So in the meantime, keep up the Cog fight...',
                          'And enjoy the silliest place ever, Toontown!']
FriendsListPanelNewFriend = 'New Friend'
FriendsListPanelOnlineFriends = 'ONLINE TOON\nFRIENDS'
FriendsListPanelAllFriends = 'ALL TOON\nFRIENDS'
FriendsListPanelPets = 'NEARBY\nPETS'
FriendsListPanelTrueFriends = 'True Friends'
FriendsListPanelAccountToons = 'YOUR TOONS'
FriendInviterClickToon = 'Click on the toon you would like to make friends with.\n\n(You have %s friends)'
FriendInviterThatToon = 'That toon'
FriendInviterToonTooMany = 'You have too many toon friends to add another one now. You will have to remove some toon friends if you want to make friends with %s.'
FriendInviterToonAlready = '%s is already your toon friend.'
FriendInviterStopBeingToonFriends = 'Stop being toon friends'
FriendInviterEndFriendshipToon = 'Are you sure you want to stop being toon friends with %s?'
FriendInviterRemainToon = '\n(You will still be toon friends with %s)'
ToontownTitleScreenClickToStart = 'Click To Start!'
ToontownTitleScreenRandomText = ['No Cogs allowed in here!',
 'Are you Toon enough?',
 "This is an injustice!",
 'Toontown lasts forever!',
 "A FREAKING BIKE HORN!",
 "May contain Cogs!",
 "Let's raid Cog Nation!",
 'Fore!',
 "Ooo!",
 'Glue!',
 'Silver stars only!',
 'Deliver a Cream Pie to Cleff.',
 'A gag to surpass the Chairman!',
 'PLEASE BE QUIET FOR THE FREAKING ANNOUNCEMENTS!',
 'Please stay off the gazebo!',
 'I love the smell of pie in the morning!',
 'Power Trip!',
 "Try a new Nametag Color!",
 'Defeat 20 4+ Story Buildings.',
 'Cogs everywhere!',
 'Powered with Panda3D!']
AvatarChoiceMakeAToon = 'Make A\nToon'
AvatarChoicePlayThisToon = 'Play\nThis Toon'
AvatarChoiceDelete = 'Delete'
AvatarChoiceDeleteConfirm = 'This will delete %s forever.'
AvatarChoiceNameRejected = 'Name\nRejected'
AvatarChoiceNameApproved = 'Name\nApproved!'
AvatarChoiceNameReview = 'Under\nReview'
AvatarChoiceNameYourToon = 'Name\nYour Toon!'
AvatarChoiceDeleteConfirmText = 'Careful! This will delete %(name)s forever.  If you are sure you want to do this, type "%(confirm)s" and click OK.'
AvatarChoiceDeleteConfirmUserTypes = 'delete'
AvatarChoiceDeletePasswordTitle = 'Delete Toon?'
AvatarChoiceDeletePasswordOK = lOK
AvatarChoiceDeletePasswordCancel = lCancel
AvatarChoiceDeleteWrongConfirm = 'You didn\'t type the right thing.  To delete %(name)s, type "%(confirm)s" and click OK.  Do not type the quotation marks.  Click Cancel if you have changed your mind.'
AvatarChooserPickAToon = 'Pick  A  Toon  To  Play'
AvatarChooserQuit = lQuit
DateOfBirthEntryMonths = ['Jan',
 'Feb',
 'Mar',
 'Apr',
 'May',
 'Jun',
 'Jul',
 'Aug',
 'Sep',
 'Oct',
 'Nov',
 'Dec']
PhotoPageTitle = 'Snapshots'
PhotoPageNoName = 'Unnamed'
PhotoPageUnknownName = 'Unknown'
PhotoPageAddName = 'Add Caption'
PhotoPageAddNamePanel = 'Add a Caption to this Snapshot:'
PhotoPageDelete = 'Are you sure you want to delete'
PhotoPageConfirm = 'Yep!'
PhotoPageCancel = lCancel
PhotoPageClose = lClose
PhotoPageDirectory = 'Open Folder'
PhotoPageTutorial = 'You haven\'t taken any snapshots yet! Press TAB to change your camera angle, and press F9 to take a snapshot.\n\n Once you\'ve made a snapshot, come here to manage and name them.'
BuildingPageTitle = 'Buildings\n(Coming Soon)'
InventoryPageTitle = 'Gags'
InventoryPageTrackFull = 'You have all the gags in the %s track.'
InventoryPagePluralPoints = 'You will get a new\n%(trackName)s gag when you\nget %(numPoints)s more %(trackName)s points.'
InventoryPageSinglePoint = 'You will get a new\n%(trackName)s gag when you\nget %(numPoints)s more %(trackName)s point.'
InventoryPageNoAccess = 'You do not have access to the %s track yet.'
NPCFriendPageTitle = 'SOS Toons'
PartyDateFormat = '%(mm)s %(dd)d, %(yyyy).4d'
PartyTimeFormat = '%d:%.2d %s'
PartyTimeFormatMeridiemAM = 'am'
PartyTimeFormatMeridiemPM = 'pm'
PartyCanStart = "It's Party Time, click Start Party in your Shticker Book Hosting page!"
PartyHasStartedAcceptedInvite = '%s party has started! Teleport to the host!'
PartyHasStartedNotAcceptedInvite = '%s party has started! You can still go to it by teleporting to the host.'
EventsPageName = 'Events'
EventsPageCalendarTabName = 'Calendar'
EventsPageCalendarTabParty = 'Party'
EventsPageToontownTimeIs = 'TOONTOWN TIME IS'
EventsPageConfirmCancel = 'If you cancel, you will get a %d%% refund. Are you sure you want to cancel your party?'
EventsPageCancelPartyResultOk = 'Your party was cancelled and you got %d Jellybeans back!'
EventsPageCancelPartyResultError = 'Sorry, your party was not cancelled.'
EventsPageCancelPartyAlreadyRefunded = 'Your party was never started. Check your mailbox for your refund!'
EventsPageTooLateToStart = 'Sorry, it is too late to start your party. You can cancel it and plan another one.'
EventsPagePublicPrivateChange = "Changing your party's privacy setting..."
EventsPagePublicPrivateNoGo = "Sorry, you can't change your party's privacy setting right now."
EventsPagePublicPrivateAlreadyStarted = "Sorry, your party has already started, so you can't change your party's privacy setting."
EventsPageHostTabName = 'Hosting'
EventsPageHostTabTitle = 'My Next Party'
EventsPageHostTabTitleNoParties = 'No Parties'
EventsPageHostTabDateTimeLabel = 'You are having a party on %s at %s Toontown Time.'
EventsPageHostingTabNoParty = 'Go to a playground\nParty Gate to plan\nyour own party!'
EventsPageHostTabPublicPrivateLabel = 'This party is:'
EventsPageHostTabToggleToPrivate = 'Private'
EventsPageHostTabToggleToPublic = 'Public'
EventsPageHostingTabGuestListTitle = 'Guests'
EventsPageHostingTabActivityListTitle = 'Activities'
EventsPageHostingTabDecorationsListTitle = 'Decorations'
EventsPageHostingTabPartiesListTitle = 'Hosts'
EventsPageHostTabCancelButton = 'Cancel Party'
EventsPageGoButton = 'Start\nParty!'
EventsPageGoBackButton = 'Party\nNow!'
EventsPageInviteGoButton = 'Go to\nParty!'
EventsPageUnknownToon = 'Unknown Toon'
EventsPageInvitedTabName = 'Invitations'
EventsPageInvitedTabTitle = 'Party Invitations'
EventsPageInvitedTabInvitationListTitle = 'Invitations'
EventsPageInvitedTabActivityListTitle = 'Activities'
EventsPageInvitedTabTime = '%s %s Toontown Time'
SelectedInvitationInformation = '%s is having a party on %s at %s Toontown Time.'
PartyPlannerNextButton = 'Continue'
PartyPlannerPreviousButton = 'Back'
PartyPlannerWelcomeTitle = 'Toontown Party Planner'
PartyPlannerInstructions = 'Hosting your own party is a lot of fun!\nStart planning with the arrows at the bottom!'
PartyPlannerDateTitle = 'Pick A Day For Your Party'
PartyPlannerTimeTitle = 'Pick A Time For Your Party'
PartyPlannerGuestTitle = 'Choose Your Guests'
PartyPlannerEditorTitle = 'Design Your Party\nPlace Activities and Decorations'
PartyPlannerConfirmTitle = 'Choose Invitations To Send'
PartyPlannerConfirmTitleNoFriends = 'Double Check Your Party'
PartyPlannerTimeToontown = 'Toontown'
PartyPlannerTimeTime = 'Time'
PartyPlannerTimeRecap = 'Party Date and Time'
PartyPlannerPartyNow = 'As Soon As Possible'
PartyPlannerTimeToontownTime = 'Toontown Time:'
PartyPlannerTimeLocalTime = 'Party Local Time : '
PartyPlannerPublicPrivateLabel = 'This party will be:'
PartyPlannerPublicDescription = 'Any Toon\ncan come!'
PartyPlannerPrivateDescription = 'Only\nInvited Toons\ncan come!'
PartyPlannerPublic = 'Public'
PartyPlannerPrivate = 'Private'
PartyPlannerCheckAll = 'Check\nAll'
PartyPlannerUncheckAll = 'Uncheck\nAll'
PartyPlannerDateText = 'Date'
PartyPlannerTimeText = 'Time'
PartyPlannerTTTimeText = 'Toontown Time'
PartyPlannerEditorInstructionsIdle = 'Click on the Party Activity or Decoration you would like to purchase.'
PartyPlannerEditorInstructionsClickedElementActivity = 'Click Buy or Drag the Activity Icon onto the Party Grounds Map'
PartyPlannerEditorInstructionsClickedElementDecoration = 'Click Buy or Drag the Decoration onto the Party Grounds Map'
PartyPlannerEditorInstructionsDraggingActivity = 'Drag the Activity onto the Party Grounds Map.'
PartyPlannerEditorInstructionsDraggingDecoration = 'Drag the Activity onto the Party Grounds Map.'
PartyPlannerEditorInstructionsPartyGrounds = 'Click and Drag items to move them around the Party Grounds Map'
PartyPlannerEditorInstructionsTrash = 'Drag an Activity or Decoration here to remove it.'
PartyPlannerEditorInstructionsNoRoom = 'There is no room to place that activity.'
PartyPlannerEditorInstructionsRemoved = '%(removed)s removed since %(added)s was added.'
PartyPlannerBeans = 'beans'
PartyPlannerTotalCost = 'Total Cost:\n%d beans'
PartyPlannerSoldOut = 'SOLD OUT'
PartyPlannerBuy = 'BUY'
PartyPlannerPartyGrounds = 'PARTY GROUNDS MAP'
PartyPlannerOkWithGroundsLayout = 'Are you done moving your Party Activities and Decorations around the Party Grounds Map?'
PartyPlannerChooseFutureTime = 'Please choose a time in the future.'
PartyPlannerInviteButton = 'Send Invites'
PartyPlannerInviteButtonNoFriends = 'Plan Party'
PartyPlannerBirthdayTheme = 'Birthday'
PartyPlannerGenericMaleTheme = 'Star'
PartyPlannerGenericFemaleTheme = 'Flower'
PartyPlannerRacingTheme = 'Racing'
PartyPlannerValentoonsTheme = 'ValenToons'
PartyPlannerVictoryPartyTheme = 'Victory'
PartyPlannerWinterPartyTheme = 'Winter'
PartyPlannerGuestName = 'Guest Name'
PartyPlannerClosePlanner = 'Close Planner'
PartyPlannerConfirmationAllOkTitle = 'Congratulations!'
PartyPlannerConfirmationAllOkText = 'Your party has been created and your invitations sent out.\nThanks!'
PartyPlannerConfirmationAllOkTextNoFriends = 'Your party has been created!\nThanks!'
PartyPlannerConfirmationErrorTitle = 'Oops.'
PartyPlannerConfirmationValidationErrorText = 'Sorry, there seems to be a problem\nwith that party.\nPlease go back and try again.'
PartyPlannerConfirmationDatabaseErrorText = "Sorry, I couldn't record all your information.\nPlease try again later.\nDon't worry, no beans were lost."
PartyPlannerConfirmationTooManyText = 'Sorry, you are already hosting a party.\nIf you want to plan another party, please\ncancel your current party.'
PartyPlannerInvitationThemeWhatSentence = 'You are invited to my %s party! %s!'
PartyPlannerInvitationThemeWhatSentenceNoFriends = 'I am hosting a %s party! %s!'
PartyPlannerInvitationThemeWhatActivitiesBeginning = 'It will have '
PartyPlannerInvitationWhoseSentence = '%s Party'
PartyPlannerInvitationTheme = 'Theme'
PartyPlannerInvitationWhenSentence = 'It will be on %s,\nat %s Toontown Time.\nHope you can make it!'
PartyPlannerInvitationWhenSentenceNoFriends = 'It will be on %s,\nat %s Toontown Time.\nToontastic!'
PartyPlannerGenericName = 'Party Planner'
PartyJukeboxOccupied = 'Someone else is using the jukebox. Try again later.'
PartyJukeboxNowPlaying = 'The song you chose is now playing on the jukebox!'
MusicEncntrGeneralBg = 'Encounter With Cogs'
MusicTcSz = 'Strolling Along'
MusicCreateAToon = 'The New Toon in Town'
MusicTtTheme = 'The Toontown Theme'
MusicMinigameRace = 'Slow and Steady'
MusicTcNbrhood = 'Toontown Central'
MusicMgDiving = 'Treasure Lullaby'
MusicMgCannonGame = 'Fire the Cannons!'
MusicMgTwodgame = 'Running Toon'
MusicMgCogthief = 'Catch That Cog!'
MusicMgTugOWar = 'Tug-of-War'
MusicMgVine = 'The Jungle Swing'
MusicMgIcegame = 'Slippery Situation'
MusicMgToontag = 'Minigame Medley'
MusicMMatchBg2 = 'Jazzy Mouse'
MusicMgTarget = "Soarin' Over Toontown"
MusicFfSafezone = 'The Funny Farm'
MusicDdSz = 'Waddling Way'
MusicMmNbrhood = "Musical Melodyland"
MusicGzPlaygolf = "Let's Play Golf!"
MusicGsSz = 'Toontown Speedway'
MusicOzSz = "Acorn Acres"
MusicGsRaceCc = 'Downtown Driving'
MusicGsRaceSs = 'Ready, Set, Go!'
MusicGsRaceRr = 'Route 66'
MusicGzSz = 'The Putt-Putt Polka'
MusicMmSz = 'Dancing in the Streets'
MusicMmSzActivity = 'Here Comes Treble'
MusicDdNbrhood = "Drifter's Dock"
MusicGsKartshop = 'Mr. Rustywrench'
MusicDdSzActivity = 'Sea Shanty'
MusicEncntrGeneralBgIndoor = 'Building Excitement'
MusicTtElevator = 'Going Up?'
MusicEncntrToonWinningIndoor = 'Toons Unite!'
MusicEncntrGeneralSuitWinningIndoor = 'Cog-tastrophe!'
MusicTbNbrhood = 'The Brrrgh'
MusicDlNbrhood = "Daunting Dreamland"
MusicDlSzActivity = 'Counting Sheep'
MusicDgSz = 'Waltz of the Flowers'
MusicDlSz = 'Sleepwalking'
MusicTbSzActivity = 'Snow Problem'
MusicTbSz = 'Shiver and Shimmy'
MusicDgNbrhood = "Daisy's Garden"
MusicEncntrHallOfFame = 'The Hall of Fame'
MusicEncntrSuitHqNbrhood = 'Dollars and Cents'
MusicChqFactBg = 'Cog Factory'
MusicCoghqFinale = 'Triumph of the Toons'
MusicEncntrToonWinning = 'Cashing In!'
MusicEncntrSuitWinning = 'Selling You Short'
MusicEncntrHeadSuitTheme = 'The Big Boss'
MusicLbJurybg = 'Court is in Session'
MusicLbCourtyard = 'Balancing Act'
MusicBossbotCeoV2 = 'Head Honcho'
MusicBossbotFactoryV1 = 'Cog Waltz'
MusicBossbotCeoV1 = 'Bossing You Around'
MusicPartyOriginalTheme = 'Party Time'
MusicPartyPolkaDance = 'Party Polka'
MusicPartySwingDance = 'Party Swing'
MusicPartyWaltzDance = 'Party Waltz'
MusicPartyGenericThemeJazzy = 'Party Jazz'
MusicPartyGenericTheme = 'Party Jingle'
JukeboxAddSong = 'Add\nSong'
JukeboxReplaceSong = 'Replace\nSong'
JukeboxQueueLabel = 'Playing Next:'
JukeboxSongsLabel = 'Pick a Song:'
JukeboxClose = 'Done'
JukeboxCurrentlyPlaying = 'Currently Playing'
JukeboxCurrentlyPlayingNothing = 'Jukebox is paused.'
JukeboxCurrentSongNothing = 'Add a song to the playlist!'
PartyOverWarningNoName = 'The party has ended! Thanks for coming!'
PartyOverWarningWithName = '%s party has ended! Thanks for coming!'
PartyCountdownClockText = 'Time\n\nLeft'
PartyTitleText = '%s Party'
PartyActivityConjunction = ', and'
PartyActivityNameDict = {0: {'generic': 'Jukebox',
     'invite': 'a Jukebox',
     'editor': 'Jukebox',
     'description': 'Listen to music with your own jukebox!'},
 1: {'generic': 'Party Cannons',
     'invite': 'Party Cannons',
     'editor': 'Cannons',
     'description': 'Fire yourself out of the cannons and into fun!'},
 2: {'generic': 'Trampoline',
     'invite': 'Trampoline',
     'editor': 'Trampoline',
     'description': 'Collect Jellybeans and bounce the highest!'},
 3: {'generic': 'Party Catch',
     'invite': 'Party Catch',
     'editor': 'Party Catch',
     'description': 'Catch fruit to win beans! Dodge those anvils!'},
 4: {'generic': 'Dance Floor\n10 moves',
     'invite': 'a 10 move Dance Floor',
     'editor': 'Dance Floor - 10',
     'description': 'Show off all 10 of your moves, toon style!'},
 5: {'generic': 'Party Tug-of-War',
     'invite': 'Party Tug-of-War',
     'editor': 'Tug-of-War',
     'description': 'Up to 4 on 4 toon tugging craziness!'},
 6: {'generic': 'Party Fireworks',
     'invite': 'Party Fireworks',
     'editor': 'Fireworks',
     'description': 'Launch your very own fireworks show!'},
 7: {'generic': 'Party Clock',
     'invite': 'a Party Clock',
     'editor': 'Party Clock',
     'description': 'Counts down the time left in your party.'},
 8: {'generic': 'Deluxe Jukebox',
     'invite': 'a deluxe jukebox',
     'editor': 'Deluxe Jukebox',
     'description': 'Your own deluxe jukebox with double the tunes for double the deal!'},
 9: {'generic': 'Dance Floor\n20 moves',
     'invite': 'a 20 move Dance Floor',
     'editor': 'Dance Floor - 20',
     'description': 'Show off all 20 of your moves, toon style!'},
 10: {'generic': 'Cog-O-War',
      'invite': 'Cog-O-War',
      'editor': 'Cog-O-War',
      'description': 'The team vs. team game of Cog splatting!'},
 11: {'generic': 'Cog Trampoline',
      'invite': 'Cog Trampoline',
      'editor': 'Cog Trampoline',
      'description': "Jump on a Cog's face!"},
 12: {'generic': 'Present Catch',
      'invite': 'Present Catch',
      'editor': 'Present Catch',
      'description': 'Catch presents to win beans! Dodge those anvils!'},
 13: {'generic': 'Holiday Trampoline',
      'invite': 'Holiday Trampoline',
      'editor': 'Holiday Trampoline',
      'description': 'Jump if you love Winter Holidays!'},
 14: {'generic': 'Holiday Cog-O-War',
      'invite': 'Holiday Cog-O-War',
      'editor': 'Holiday Cog-O-War',
      'description': 'The team vs. team game of Cog splattering!'},
 15: {'generic': 'Dance Floor\n10 moves',
      'invite': 'a 10 move ValenToons Dance Floor',
      'editor': 'Dance Floor - 10',
      'description': 'Get your ValenToon Groove On!'},
 16: {'generic': 'Dance Floor\n20 moves',
      'invite': 'a 20 move ValenToons Dance Floor',
      'editor': 'Dance Floor - 20',
      'description': 'Get your ValenToon Groove On!'},
 17: {'generic': 'Jukebox\n20 songs',
      'invite': 'a 20 song Valentoons Jukebox',
      'editor': 'Jukebox - 20',
      'description': 'Nothing sets the mood like music!'},
 18: {'generic': 'Jukebox\n40 songs',
      'invite': 'a 40 song Valentoons jukebox',
      'editor': 'Jukebox - 40',
      'description': 'Nothing sets the mood like music!'},
 19: {'generic': 'Trampoline',
      'invite': 'ValenToons Trampoline',
      'editor': 'Trampoline',
      'description': "Jump to your heart's content!"}}
PartyDecorationNameDict = {0: {'editor': 'Balloon Anvil',
     'description': 'Try to keep the fun from floating away!'},
 1: {'editor': 'Party Stage',
     'description': 'Balloons, stars, what else could you want?'},
 2: {'editor': 'Party Bow',
     'description': 'Wrap up the fun!'},
 3: {'editor': 'Cake',
     'description': 'Delicious.'},
 4: {'editor': 'Party Castle',
     'description': "A Toon's home is his castle."},
 5: {'editor': 'Gift Pile',
     'description': 'Gifts for every Toon!'},
 6: {'editor': 'Streamer Horn',
     'description': 'This horn is a hoot! Streamers!'},
 7: {'editor': 'Party Gate',
     'description': 'Multi-colored and crazy!'},
 8: {'editor': 'Noise Makers',
     'description': 'Tweeeeet!'},
 9: {'editor': 'Pinwheel',
     'description': 'Colorful twirling for everyone!'},
 10: {'editor': 'Gag Globe',
      'description': 'Gag and star globe designed by Olivea'},
 11: {'editor': 'Bean Banner',
      'description': 'A Jellybean banner designed by Cassidy'},
 12: {'editor': 'Gag Cake',
      'description': 'A Topsy Turvy gag cake designed by Felicia'},
 13: {'editor': "Cupid's Heart",
      'description': 'Ready...Aim...\nValenToons!'},
 14: {'editor': 'Candy Hearts\n Banner',
      'description': "Who doesn't love candy hearts?"},
 15: {'editor': 'Flying Heart',
      'description': 'This heart is getting carried away!'},
 16: {'editor': 'Victory Bandstand',
      'description': 'All our new friends are ready to dance!'},
 17: {'editor': 'Victory Banner',
      'description': 'Not just a normal banner!'},
 18: {'editor': 'Confetti Cannons',
      'description': 'BOOM! Confetti! Fun!'},
 19: {'editor': 'Cog & Doodle',
      'description': "Ouch! That's gotta hurt."},
 20: {'editor': 'Cog Flappy Man',
      'description': 'A Cog full of hot air, what a shock!'},
 21: {'editor': 'Cog Ice Cream',
      'description': 'A Cog looking his best.'},
 22: {'editor': 'CogCicle',
      'description': 'A Cog looking his holiday best.'},
 23: {'editor': 'Holiday Bandstand',
      'description': 'Everyone loves a Holiday Party!'},
 24: {'editor': 'Chilly Cog',
      'description': "Ouch! That's gotta hurt."},
 25: {'editor': 'Snowman',
      'description': "So cool, he's hot!"},
 26: {'editor': 'SnowDoodle',
      'description': 'His only trick is being cold!'},
 27: {'editor': 'ValenToons Anvil',
      'description': "We've got your heart on a string!"}}
ActivityLabel = 'Cost - Activity Name'
PartyDoYouWantToPlan = 'Would you like to plan a new party right now?'
PartyPlannerComingSoon = 'Coming Soon!'
PartyPlannerCantBuy = "CAN'T BUY"
PartyPlannerOnYourWay = 'Have fun planning your party!'
PartyPlannerMaybeNextTime = 'Maybe next time.  Have a good day!'
PartyPlannerHostingTooMany = 'You can only host one party at a time, sorry.'
PartyPlannerNpcMinCost = 'It costs a minimum of %d Jellybeans to plan a party.'
PartyHatPublicPartyChoose = 'Do you want to go to the 1st available public party?'
PartyGateTitle = 'Public Parties'
PartyGateGoToParty = 'Go to\nParty!'
PartyGatePartiesListTitle = 'Hosts'
PartyGatesPartiesListToons = 'Toons'
PartyGatesPartiesListActivities = 'Activities'
PartyGatesPartiesListMinLeft = 'Minutes Left'
PartyGateLeftSign = 'Come On In!'
PartyGateRightSign = 'Public Parties Here!'
PartyGatePartyUnavailable = 'Sorry. That party is no longer available.'
PartyGatePartyFull = 'Sorry. That party is full.'
PartyGateInstructions = 'Click on a host, then click on "Go to Party"'
PartyActivityWaitingForOtherPlayers = 'Waiting for other toons to join the party game...'
PartyActivityPleaseWait = 'Please wait...'
DefaultPartyActivityTitle = 'Party Game Title'
DefaultPartyActivityInstructions = 'PartyGame Instructions'
PartyOnlyHostLeverPull = 'Only the host can start this activity. Sorry.'
PartyActivityDefaultJoinDeny = 'You cannot join this activity right now. Sorry.'
PartyActivityDefaultExitDeny = 'You cannot leave this activity right now. Sorry.'
PartyJellybeanRewardOK = 'OK'
PartyCatchActivityTitle = 'Party Catch Activity'
PartyCatchActivityInstructions = "Catch as many pieces of fruit as you can. Try not to 'catch' any %(badThing)s!"
PartyCatchActivityFinishPerfect = 'PERFECT GAME!'
PartyCatchActivityFinish = 'Good Game!'
PartyCatchActivityExit = 'EXIT'
PartyCatchActivityApples = 'apples'
PartyCatchActivityOranges = 'oranges'
PartyCatchActivityPears = 'pears'
PartyCatchActivityCoconuts = 'coconuts'
PartyCatchActivityWatermelons = 'watermelons'
PartyCatchActivityPineapples = 'pineapples'
PartyCatchActivityAnvils = 'anvils'
PartyCatchStarted = 'The game has started. Go play it.'
PartyCatchCannotStart = 'The game could not start right now.'
PartyCatchRewardMessage = 'Pieces of fruit caught: %s\n\nJellybeans earned: %d'
WinterPartyCatchActivityInstructions = "Catch as many presents as you can. Try not to 'catch' any %(badThing)s!"
WinterPartyCatchRewardMessage = 'Presents caught: %s\n\nJellybeans earned: %s'
PartyDanceActivityTitle = 'Party Dance Floor'
PartyDanceActivityInstructions = 'Combine 3 or more ARROW KEY patterns to do dance moves! There are 10 dance moves available. Can you find them all?'
PartyDanceActivity20Title = 'Party Dance Floor'
PartyDanceActivity20Instructions = 'Combine 3 or more ARROW KEY patterns to do dance moves! There are 20 dance moves available. Can you find them all?'
DanceAnimRight = 'Right'
DanceAnimReelNeutral = 'The Fishertoon'
DanceAnimConked = 'The Headbob'
DanceAnimHappyDance = 'The Happy Dance'
DanceAnimConfused = 'Very Dizzy'
DanceAnimWalk = 'Walking on the Moon'
DanceAnimJump = 'The Jump!'
DanceAnimFirehose = 'The Firetoon'
DanceAnimShrug = 'Who Knows?'
DanceAnimSlipForward = 'The Fall'
DanceAnimSadWalk = 'Tired'
DanceAnimWave = 'Hello Goodbye'
DanceAnimStruggle = 'The Shuffle Hop'
DanceAnimRunningJump = 'The Running Toon'
DanceAnimSlipBackward = 'The Backfall'
DanceAnimDown = 'Down'
DanceAnimUp = 'Up'
DanceAnimGoodPutt = 'The Putt'
DanceAnimVictory = 'The Victory Dance'
DanceAnimPush = 'The Mimetoon'
DanceAnimAngry = "Rock n' Roll"
DanceAnimLeft = 'Left'
PartyCannonActivityTitle = 'Party Cannons'
PartyCannonActivityInstructions = 'Hit the clouds to change their color and bounce in the air! While IN THE AIR, you can USE THE ARROW KEYS to GLIDE.'
PartyCannonResults = 'You collected %d jelly beans!\n\nNumber of Clouds Hit: %d'
FireworksActivityInstructions = 'Look up using the "Page Up" key to see better.'
FireworksActivityBeginning = 'Party fireworks are about to start! Enjoy the show!'
FireworksActivityEnding = 'Hope you enjoyed the show!'
PartyFireworksAlreadyActive = 'The fireworks show has already started.'
PartyFireworksAlreadyDone = 'The fireworks show is over.'
PartyTrampolineJellyBeanTitle = 'Jelly Beans Trampoline'
PartyTrampolineTricksTitle = 'Tricks Trampoline'
PartyTrampolineActivityInstructions = 'Use the Control key to jump.\n\nJump when your Toon is at its lowest point on the trampoline to jump higher.'
PartyTrampolineActivityOccupied = 'Trampoline in use.'
PartyTrampolineQuitEarlyButton = 'Hop Off'
PartyTrampolineBeanResults = 'You collected %d jelly beans.'
PartyTrampolineBonusBeanResults = 'You collected %d jelly beans, plus %d more for getting the Big Bean. '
PartyTrampolineTopHeightResults = 'Your top height was %d ft.'
PartyTrampolineTimesUp = "Time's Up"
PartyTrampolineReady = 'Ready...'
PartyTrampolineGo = 'Go!'
PartyTrampolineBestHeight = 'Best Height So Far:\n%s\n%d ft'
PartyTrampolineNoHeightYet = 'How high\ncan you jump?'
PartyTrampolineGetHeight = '%d ft'
PartyTeamActivityForMorePlural = 's'
PartyTeamActivityForMore = 'Waiting  for  %d  toon%s\non  each  side...'
PartyTeamActivityForMoreWithBalance = 'Waiting  for  %d  more  toon%s...'
PartyTeamActivityWaitingForOtherPlayers = 'Waiting  for  other  toons...'
PartyTeamActivityWaitingToStart = 'Starting  in...'
PartyTeamActivityExitButton = 'Hop Off'
PartyTeamActivitySwitchTeamsButton = 'Switch\nTeams'
PartyTeamActivityWins = '%s team wins!'
PartyTeamActivityLocalAvatarTeamWins = 'Your team won!'
PartyTeamActivityGameTie = "It's a tie!"
PartyTeamActivityJoinDenied = "Sorry, you can't join %s at this time."
PartyTeamActivityExitDenied = 'Sorry, you are unable to leave %s at this time.'
PartyTeamActivitySwitchDenied = "Sorry, you cant's switch teams at this time."
PartyTeamActivityTeamFull = 'Sorry, that team is already full!'
PartyTeamActivityRewardMessage = 'You got %d Jellybeans. Good job!'
PartyCogTeams = ('Blue', 'Orange')
PartyCogRewardMessage = 'Your Score: %d\n'
PartyCogRewardBonus = '\nYou got %d additional Jellybean%s because your team won!'
PartyCogJellybeanPlural = 's'
PartyCogSignNote = 'HI-SCORE\n%s\n%d'
PartyCogTitle = 'Cog-O-War'
PartyCogInstructions = 'Throw pies at cogs to push them away from your team. ' + "When time's up, the team with most cogs on the other side wins!" + '\n\nThrow with the CONTROL KEY. Move with the ARROW KEYS.'
PartyCogDistance = '%d ft'
PartyCogTimeUp = "Time's up!"
PartyCogGuiScoreLabel = 'SCORE'
PartyCogGuiPowerLabel = 'POWER'
PartyCogGuiSpamWarning = 'Hold CONTROL for more power!'
PartyCogBalanceBar = 'BALANCE'
PartyTugOfWarReady = 'Ready...'
PartyTugOfWarGo = 'GO!'
PartyTugOfWarGameEnd = 'Good  game!'
PartyTugOfWarTitle = 'Party Tug-of-War'
CalendarShowAll = 'Show All'
CalendarShowOnlyHolidays = 'Show Only Holidays'
CalendarShowOnlyParties = 'Show Only Parties'
CalendarEndsAt = 'Ends on'
CalendarStartedOn = 'Started on'
CalendarEndOf = 'End of'
CalendarPartyGetReady = 'Get ready!'
CalendarPartyGo = 'Go party!'
CalendarPartyFinished = "It's over..."
CalendarPartyCancelled = 'Cancelled.'
CalendarPartyNeverStarted = 'Never Started.'
NPCFriendPanelRemaining = '%d Remaining'
MapPageTitle = 'Map'
MapPageBackToPlayground = 'Back to Playground'
MapPageBackToCogHQ = 'Back to Cog HQ'
MapPageGoHome = 'Go Home'
MapPageYouAreHere = 'You are in: %s\n%s'
MapPageYouAreAtHome = 'You are at\nyour estate'
MapPageYouAreAtSomeonesHome = 'You are at %s estate'
MapPageGoTo = 'Go To\n%s'
OptionsPageTitle = 'Options'
OptionsTabTitle = 'Options'
OptionsPageExitToontown = 'Exit Toontown'
OptionsPageMusic = 'Music Volume:'
OptionsPageSFX = 'SFX Volume:'
OptionsPageSFXOnLabel = 'Sound Effects are on.'
OptionsPageSFXOffLabel = 'Sound Effects are off.'
OptionsPageToonChatSoundsOnLabel = '   Type Chat Sounds are on.'
OptionsPageToonChatSoundsOffLabel = '   Type Chat Sounds are off.'
OptionsPageFriendsEnabledLabel = 'Accepting new friend requests.'
OptionsPageFriendsDisabledLabel = 'Not accepting friend requests.'
OptionsPageWhisperEnabledLabel = 'Allowing whispers from anyone.'
OptionsPageWhisperDisabledLabel = 'Allowing whispers from friends only.'
OptionsPageSpeedChatStyleLabel = 'SpeedChat Color'
OptionsPageDisplayWindowed = 'windowed'
OptionsPageSelect = 'Select'
OptionsPageToggleOn = 'Turn On'
OptionsPageToggleOff = 'Turn Off'
OptionsPageChange = 'Change'
OptionsPageDisplaySettings = 'Display: %(screensize)s, %(api)s'
OptionsPageDisplaySettingsNoApi = 'Display: %(screensize)s'
OptionsPageExitConfirm = 'Exit Toontown?'
TrolleyPositionLabel = 'Trolley Position:'
TrolleyPositionSit = 'Sit'
TrolleyPositionStand = 'Stand'
DisplaySettingsTitle = 'Display Settings'
DisplaySettingsIntro = 'The following settings are used to configure the way Toontown is displayed on your computer.  It is usually unnecessary to adjust these unless you are experiencing a problem.'
DisplaySettingsIntroSimple = 'You may adjust the screen resolution to a higher value to improve the clarity of text and graphics in Toontown, but depending on your graphics card, some higher values may make the game run less smoothly or may not work at all.'
DisplaySettingsApi = 'Graphics API:'
DisplaySettingsResolution = 'Resolution:'
DisplaySettingsWindowed = 'In a window'
DisplaySettingsFullscreen = 'Full screen'
DisplaySettingsApply = 'Apply'
DisplaySettingsCancel = lCancel
DisplaySettingsApplyWarning = 'When you press OK, the display settings will change.  If the new configuration does not display properly on your computer, the display will automatically return to its original configuration after %s seconds.'
DisplaySettingsAccept = 'Press OK to keep the new settings, or Cancel to revert.  If you do not press anything, the settings will automatically revert back in %s seconds.'
DisplaySettingsRevertUser = 'Your previous display settings have been restored.'
DisplaySettingsRevertFailed = 'The selected display settings do not work on your computer.  Your previous display settings have been restored.'
TrackPageTitle = 'Gag Track Training'
TrackPageShortTitle = 'Gag Training'
TrackPageSubtitle = 'Complete ToonTasks to learn how to use new gags!'
TrackPageTraining = 'You are training to use %s gags.\nWhen you complete all 16 tasks you\nwill be able to use %s gags in battle.'
TrackPageClear = 'You are not training any Gag Tracks now.'
TrackPageFilmTitle = '%s\nTraining\nFilm'
TrackPageDone = 'FIN'
QuestPageToonTasks = 'ToonTasks'
QuestPageChoose = 'Choose'
QuestPageLocked = 'Locked'
QuestPageDestination = '%s\n%s\n%s'
QuestPageNameAndDestination = '%s\n%s\n%s\n%s'
QuestPosterHQOfficer = lHQOfficerM
QuestPosterHQBuildingName = lToonHQ
QuestPosterHQStreetName = 'Any Street'
QuestPosterHQLocationName = 'Any Neighborhood'
QuestPosterTailor = 'Tailor'
QuestPosterTailorBuildingName = 'Clothing Store'
QuestPosterTailorStreetName = 'Any Playground'
QuestPosterTailorLocationName = 'Any Neighborhood'
QuestPosterPlayground = 'In the playground'
QuestPosterAtHome = 'At your home'
QuestPosterInHome = 'In your home'
QuestPosterOnPhone = 'On your phone'
QuestPosterEstate = 'At your estate'
QuestPosterAnywhere = 'Anywhere'
QuestPosterAuxTo = 'to:'
QuestPosterAuxFrom = 'from:'
QuestPosterAuxFor = 'for:'
QuestPosterAuxOr = 'or:'
QuestPosterAuxReturnTo = 'Return to:'
QuestPosterLocationIn = ' in '
QuestPosterLocationOn = ' in '
QuestPosterFishing = 'GO FISHING'
QuestPosterComplete = 'COMPLETE'
QuestPosterConfirmDelete = 'Are you sure you want to delete this ToonTask?'
QuestPosterDeleteBtn = 'Delete'
QuestPosterDialogYes = 'Delete'
QuestPosterDialogNo = 'Cancel'
ShardPageTitle = 'Districts'
ShardPageHelpIntro = 'Each District is a copy of the Toontown world.'
ShardPageHelpWhere = '  You are currently in the "%s" District.'
ShardPageHelpMove = '  To move to a new District, click on its name.'
ShardPagePopulationTotal = 'Total Toontown Population:\n%d'
ShardPageScrollTitle = 'Name            Population'
ShardPageLow = 'Quiet'
ShardPageMed = 'Ideal'
ShardPageHigh = 'Full'
ShardPageChoiceReject = 'Sorry, that district is full. Please try another one.'
SuitPageTitle = 'Cog Gallery'
SuitPageMystery = DialogQuestion + DialogQuestion + DialogQuestion
SuitPageQuota = '%s of %s'
SuitPageCogRadar = '%s present'
SuitPageBuildingRadarS = '%s building'
SuitPageBuildingRadarP = '%s buildings'
DisguisePageTitle = Cog + ' Disguise'
DisguisePageMeritAlert = 'Ready for\npromotion!'
DisguisePageCogLevel = 'Level %s'
DisguisePageMeritFull = 'Full'
ItemPageTitle = 'Items'
FishPageTitle = 'Fishing'
FishPageTitleTank = 'Fish Bucket'
FishPageTitleCollection = 'Fish Album'
FishPageTitleTrophy = 'Fishing Trophies'
FishPageWeightStr = 'Weight: '
FishPageWeightLargeS = '%d lb. '
FishPageWeightLargeP = '%d lbs. '
FishPageWeightSmallS = '%d oz.'
FishPageWeightSmallP = '%d oz.'
FishPageWeightConversion = 16
FishPageValueS = 'Value: %d Jellybean'
FishPageValueP = 'Value: %d Jellybeans'
FishPageCollectedTotal = 'Fish Species Collected: %d of %d'
FishPageRodInfo = '%s Rod\n%d - %d Pounds'
FishPageTankTab = 'Bucket'
FishPageCollectionTab = 'Album'
FishPageTrophyTab = 'Trophies'
FishPickerTotalValue = 'Bucket: %s / %s\nValue: %d Jellybeans'
UnknownFish = '???'
FishingRod = '%s Rod'
FishingRodNameDict = {0: 'Twig',
 1: 'Bamboo',
 2: 'Hardwood',
 3: 'Steel',
 4: 'Gold'}
FishTrophyNameDict = {0: 'Guppy',
 1: 'Minnow',
 2: 'Fish',
 3: 'Flying Fish',
 4: 'Shark',
 5: 'Swordfish',
 6: 'Killer Whale',
 7: 'Great White',
 8: 'Kraken',
 9: 'Legendary'}
GardenPageTitle = 'Gardening'
GardenPageTitleBasket = 'Flower Basket'
GardenPageTitleCollection = 'Flower Album'
GardenPageTitleTrophy = 'Gardening Trophies'
GardenPageTitleSpecials = 'Gardening Specials'
GardenPageBasketTab = 'Basket'
GardenPageCollectionTab = 'Album'
GardenPageTrophyTab = 'Trophies'
GardenPageSpecialsTab = 'Specials'
GardenPageCollectedTotal = 'Flower Varieties Collected: %d of %d'
GardenPageValueS = 'Value: %d Jellybean'
GardenPageValueP = 'Value: %d Jellybeans'
FlowerPickerTotalValue = 'Basket: %s / %s\nValue: %d Jellybeans'
GardenPageShovelInfo = '%s Shovel: %d / %d\n'
GardenPageWateringCanInfo = '%s Watering Can: %d / %d'
FlowerPageWeightConversion = 1
FlowerPageWeightLargeP = 'Large P'
FlowerPageWeightLargeS = 'LargeS '
FlowerPageWeightSmallP = 'SmallP '
FlowerPageWeightSmallS = 'SmallS '
FlowerPageWeightStr = 'Weight: %s'
KartPageTitle = 'Karts'
KartPageTitleCustomize = 'Kart Customizer'
KartPageTitleRecords = 'Personal Best Records'
KartPageTitleTrophy = 'Racing Trophies'
KartPageCustomizeTab = 'Customize'
KartPageRecordsTab = 'Records'
KartPageTrophyTab = 'Trophy'
KartPageTrophyDetail = 'Trophy %s : %s'
KartPageTickets = 'Tickets : '
KartPageConfirmDelete = 'Delete Accessory?'
KartShtikerDelete = 'Delete'
KartShtikerSelect = 'Select a Category'
KartShtikerNoAccessories = 'No Accessories Owned'
KartShtikerBodyColors = 'Kart Colors'
KartShtikerAccColors = 'Accessory Colors'
KartShtikerEngineBlocks = 'Hood Accessories'
KartShtikerSpoilers = 'Trunk Accessories'
KartShtikerFrontWheelWells = 'Front Wheel Accessories'
KartShtikerBackWheelWells = 'Back Wheel Accessories'
KartShtikerRims = 'Rim Accessories'
KartShtikerDecals = 'Decal Accessories'
KartShtikerBodyColor = 'Kart Color'
KartShtikerAccColor = 'Accessory Color'
KartShtikerEngineBlock = 'Hood'
KartShtikerSpoiler = 'Trunk'
KartShtikerFrontWheelWell = 'Front Wheel'
KartShtikerBackWheelWell = 'Back Wheel'
KartShtikerRim = 'Rim'
KartShtikerDecal = 'Decal'
KartShtikerDefault = 'Default %s'
KartShtikerNo = 'No %s Accessory'
QuestChoiceGuiCancel = lCancel
TrackChoiceGuiChoose = 'Choose'
TrackChoiceGuiCancel = lCancel
TrackChoiceGuiHEAL = 'Toonup lets you heal other Toons in battle.'
TrackChoiceGuiTRAP = 'Traps are powerful gags that must be used with Lure.'
TrackChoiceGuiLURE = 'Use Lure to stun Cogs or draw them into traps.'
TrackChoiceGuiSOUND = 'Sound gags affect all Cogs, but are not very powerful.'
TrackChoiceGuiTHROW = 'Throw gags have lots of raw power, but are very accurate.'
TrackChoiceGuiSQUIRT = 'Squirt gags have a little raw power, but are highly accurate.'
TrackChoiceGuiDROP = 'Drop gags do lots of damage, but are not very accurate.'
EmotePageTitle = 'Expressions / Emotions'
EmotePageDance = 'You have built the following dance sequence:'
EmoteJump = 'Jump'
EmoteDance = 'Dance'
EmoteHappy = 'Happy'
EmoteSad = 'Sad'
EmoteAnnoyed = 'Annoyed'
EmoteSleep = 'Sleepy'
EmoteFuncDict = {'Wave': 0,
 'Happy': 1,
 'Sad': 2,
 'Angry': 3,
 'Sleepy': 4,
 'Shrug': 5,
 'Dance': 6,
 'Think': 7,
 'Bored': 8,
 'Applause': 9,
 'Cringe': 10,
 'Confused': 11,
 'Belly Flop': 12,
 'Bow': 13,
 'Banana Peel': 14,
 'Resistance Salute': 15,
 'Laugh': 16,
 lYes: 17,
 lNo: 18,
 'Happy Dance': 19,
 'Surprise': 20,
 'Cry': 21,
 'Delighted': 22,
 'Furious': 23,
 'Laugh': 24,
 'Rage': 25,
 'Hypnotize': 26,
 'T-Pose': 27,
 'Taunt': 28}
EmoteList = ['Wave',
 'Happy',
 'Sad',
 'Angry',
 'Sleepy',
 'Shrug',
 'Dance',
 'Think',
 'Bored',
 'Applause',
 'Cringe',
 'Confused',
 'Belly Flop',
 'Bow',
 'Banana Peel',
 'Resistance Salute',
 'Laugh',
 lYes,
 lNo,
 'Happy Dance',
 'Surprise',
 'Cry',
 'Delighted',
 'Furious',
 'Laugh',
 'Rage',
 'Hypnotize',
 'T-Pose',
 'Taunt']
EmoteWhispers = ['%s waves.',
 '%s is happy.',
 '%s is sad.',
 '%s is angry.',
 '%s is sleepy.',
 '%s shrugs.',
 '%s dances.',
 '%s thinks.',
 '%s is bored.',
 '%s applauds.',
 '%s cringes.',
 '%s is confused.',
 '%s does a belly flop.',
 '%s bows to you.',
 '%s slips on a banana peel.',
 '%s gives the resistance salute.',
 '%s laughs.',
 "%s says '" + lYes + "'.",
 "%s says '" + lNo + "'.",
 "%s does a happy dance.",
 '%s is surprised.',
 '%s is crying.',
 '%s is delighted.',
 '%s is furious.',
 '%s is laughing.',
 '%s is raging.',
 '%s tries to hypnotize you.',
 '%s is asserting their dominance.',
 '%s taunts you.']
SuitBaseNameWithLevel = '%(name)s\n%(dept)s\nLevel %(level)s'
SuitBaseNameVirtual = 'Virtual %s'
virtualType2Name = {1: 'ATK', 2: 'HP', 3: 'DEF', 4: 'ACC', 5: 'LUCK'}
HealthForceAcknowledgeMessage = 'You cannot leave the playground until your Laff meter is smiling!'
InventoryTotalGags = 'Total gags\n%d / %d'
InventoryPinkSlips = '%s Pink Slips'
InventoryPinkSlip = '1 Pink Slip'
InventoryDelete = 'DELETE'
InventoryDone = 'DONE'
InventoryDeleteHelp = 'Click on a gag to DELETE it.'
InventorySkillCredit = 'Skill credit: %s'
InventorySkillCreditNone = 'Skill credit: None'
InventoryDetailAmount = '%(numItems)s / %(maxItems)s'
InventoryDetailData = 'Accuracy: %(accuracy)s\n%(damageString)s: %(damage)d%(bonus)s\n%(singleOrGroup)s'
InventoryTrackExp = '%(curExp)s / %(nextExp)s'
InventoryUberTrackExp = '%(nextExp)s to Go!'
InventoryAffectsOneCog = 'Affects: One ' + Cog
InventoryAffectsOneToon = 'Affects: One Toon'
InventoryAffectsAllToons = 'Affects: All Toons'
InventoryAffectsAllCogs = 'Affects: All ' + Cogs
InventoryHealString = 'Toon-up'
InventoryDamageString = 'Damage'
InventoryLureString = 'Rounds effective'
InventoryBattleMenu = 'BATTLE MENU'
InventoryRun = 'RUN'
InventorySOS = 'SOS'
InventoryPass = 'PASS'
InventoryFire = 'FIRE'
InventoryClickToAttack = 'Click a\ngag to\nattack'
InventoryDamageBonus = '(+%d)'
NPCForceAcknowledgeMessage = "You must ride the trolley before leaving.\n\n\n\n\n\n\n\n\nYou can find the trolley next to Goofy's Gag Shop."
NPCForceAcknowledgeMessage2 = 'You must return to Toon Headquarters before leaving.\n\n\n\n\n\n\n\n\n\nToon Headquarters is located near the center of the playground.'
NPCForceAcknowledgeMessage3 = "Remember to ride the trolley.\n\n\n\n\n\n\n\nYou can find the trolley next to Goofy's Gag Shop."
NPCForceAcknowledgeMessage4 = 'Congratulations!  You found and rode the trolley!\n\n\n\n\n\n\n\n\n\nNow report back to Toon Headquarters.'
NPCForceAcknowledgeMessage5 = "Don't forget your ToonTask!\n\n\n\n\n\n\n\n\n\n\nYou can find Cogs to defeat on the other side of tunnels like this."
NPCForceAcknowledgeMessage6 = 'Great job defeating those Cogs!\n\n\n\n\n\n\n\n\nHead back to Toon Headquarters as soon as possible.'
NPCForceAcknowledgeMessage7 = "Don't forget to make a friend!\n\n\n\n\n\n\nClick on another toon and use the New Friend button."
NPCForceAcknowledgeMessage8 = 'Great! You made a new friend!\n\n\n\n\n\n\n\n\nYou should go back at Toon Headquarters now.'
NPCForceAcknowledgeMessage9 = 'Good job using the phone!\n\n\n\n\n\n\n\n\nReturn to Toon Headquarters to claim your reward.'
ToonSleepString = '. . . ZZZ . . .'
BattleGlobalTracks = ['toon-up',
 'trap',
 'lure',
 'sound',
 'throw',
 'squirt',
 'drop']
BattleGlobalNPCTracks = ['restock', 'toons hit', 'cogs miss', 'gags organic', 'doodles power up', 'bonus power up']
BattleGlobalAvPropStrings = (('Feather',
  'Megaphone',
  'Lipstick',
  'Bamboo Cane',
  'Pixie Dust',
  'Juggling Balls',
  'High Dive'),
 ('Banana Peel',
  'Rake',
  'Marbles',
  'Quicksand',
  'Trapdoor',
  'TNT',
  'Railroad'),
 ('$1 bill',
  'Small Magnet',
  '$5 bill',
  'Big Magnet',
  '$10 bill',
  'Hypno-goggles',
  'Presentation'),
 ('Bike Horn',
  'Whistle',
  'Bugle',
  'Aoogah',
  'Elephant Trunk',
  'Foghorn',
  'Opera Singer'),
 ('Cupcake',
  'Fruit Pie Slice',
  'Cream Pie Slice',
  'Whole Fruit Pie',
  'Whole Cream Pie',
  'Birthday Cake',
  'Wedding Cake'),
 ('Squirting Flower',
  'Glass of Water',
  'Squirt Gun',
  'Seltzer Bottle',
  'Fire Hose',
  'Storm Cloud',
  'Geyser'),
 ('Flower Pot',
  'Sandbag',
  'Anvil',
  'Big Weight',
  'Safe',
  'Grand Piano',
  'Toontanic'))
BattleGlobalAvPropStringsSingular = (('a Feather',
  'a Megaphone',
  'a Lipstick',
  'a Bamboo Cane',
  'a Pixie Dust',
  'a set of Juggling Balls',
  'a High Dive'),
 ('a Banana Peel',
  'a Rake',
  'a set of Marbles',
  'a patch of Quicksand',
  'a Trapdoor',
  'a TNT',
  'a Railroad'),
 ('a $1 bill',
  'a Small Magnet',
  'a $5 bill',
  'a Big Magnet',
  'a $10 bill',
  'a pair of Hypno-goggles',
  'a Presentation'),
 ('a Bike Horn',
  'a Whistle',
  'a Bugle',
  'an Aoogah',
  'an Elephant Trunk',
  'a Foghorn',
  'an Opera Singer'),
 ('a Cupcake',
  'a Fruit Pie Slice',
  'a Cream Pie Slice',
  'a Whole Fruit Pie',
  'a Whole Cream Pie',
  'a Birthday Cake',
  'a Wedding Cake'),
 ('a Squirting Flower',
  'a Glass of Water',
  'a Squirt Gun',
  'a Seltzer Bottle',
  'a Fire Hose',
  'a Storm Cloud',
  'a Geyser'),
 ('a Flower Pot',
  'a Sandbag',
  'an Anvil',
  'a Big Weight',
  'a Safe',
  'a Grand Piano',
  'the Toontanic'))
BattleGlobalAvPropStringsPlural = (('Feathers',
  'Megaphones',
  'Lipsticks',
  'Bamboo Canes',
  'Pixie Dusts',
  'sets of Juggling Balls',
  'High Dives'),
 ('Banana Peels',
  'Rakes',
  'sets of Marbles',
  'patches of Quicksand',
  'Trapdoors',
  'TNTs',
  'Railroads'),
 ('$1 bills',
  'Small Magnets',
  '$5 bills',
  'Big Magnets',
  '$10 bills',
  'pairs of Hypno-goggles',
  'Presentations'),
 ('Bike Horns',
  'Whistles',
  'Bugles',
  'Aoogahs',
  'Elephant Trunks',
  'Foghorns',
  'Opera Singers'),
 ('Cupcakes',
  'Fruit Pie Slices',
  'Cream Pie Slices',
  'Whole Fruit Pies',
  'Whole Cream Pies',
  'Birthday Cakes',
  'Wedding cakes'),
 ('Squirting Flowers',
  'Glasses of Water',
  'Squirt Guns',
  'Seltzer Bottles',
  'Fire Hoses',
  'Storm Clouds',
  'Geysers'),
 ('Flower Pots',
  'Sandbags',
  'Anvils',
  'Big Weights',
  'Safes',
  'Grand Pianos',
  'Oceanliners'))
AttackMissed = 'MISSED'
CriticalStrike = 'CRITICAL STRIKE!'
DefenseRisen = '+%s PERCENT DEFENSE!'
NPCCallButtonLabel = 'CALL'
LoaderLabel = 'Loading...'
StarringIn = 'Starring In...'
HeadingToHood = 'Heading %(to)s %(hood)s...'
HeadingToYourEstate = 'Heading to your estate...'
HeadingToEstate = "Heading to %s's estate..."
HeadingToFriend = "Heading to %s's friend's estate..."
HeadingToPlayground = 'Heading to the Playground...'
HeadingToStreet = 'Heading %(to)s %(street)s...'
TownBattleRun = 'Run all the way back to the playground?'
TownBattleChooseAvatarToonTitle = 'WHICH TOON?'
TownBattleChooseAvatarCogTitle = 'WHICH ' + Cog.upper() + '?'
TownBattleChooseAvatarBack = 'BACK'
FireCogTitle = 'PINK SLIPS LEFT:%s\nFIRE WHICH COG?'
FireCogLowTitle = 'PINK SLIPS LEFT:%s\nNOT ENOUGH SLIPS!'
TownBattleSOSNoFriends = 'No friends to call!'
TownBattleSOSWhichFriend = 'Call which friend?'
TownBattleSOSNPCFriends = 'Rescued Toons'
TownBattleSOSBack = 'BACK'
TownBattleToonSOS = 'SOS'
TownBattleToonFire = 'Fire'
TownBattleUndecided = '?'
TownBattleHealthText = '%(hitPoints)s/%(maxHit)s'
TownBattleWaitTitle = 'Waiting for\nother toons...'
TownSoloBattleWaitTitle = 'Please wait...'
TownBattleWaitBack = 'BACK'
TownBattleSOSPetSearchTitle = 'Searching for doodle\n%s...'
TownBattleSOSPetInfoTitle = '%s is %s'
TownBattleSOSPetInfoOK = lOK
TrolleyHFAMessage = 'You may not board the trolley until your Laff meter is smiling.'
TrolleyTFAMessage = 'You may not board the trolley until Joey says so.'
TrolleyHopOff = 'Hop off'
FishingExit = 'Exit'
FishingCast = 'Cast'
FishingAutoReel = 'Auto Reel'
FishingItemFound = 'You caught:'
FishingCrankTooSlow = 'Too\nslow'
FishingCrankTooFast = 'Too\nfast'
FishingFailure = "You didn't catch anything!"
FishingFailureTooSoon = "Don't start to reel in the line until you see a nibble.  Wait for your float to bob up and down rapidly!"
FishingFailureTooLate = 'Be sure to reel in the line while the fish is still nibbling!'
FishingFailureAutoReel = "The auto-reel didn't work this time.  Turn the crank by hand, at just the right speed, for your best chance to catch something!"
FishingFailureTooSlow = 'You turned the crank too slowly.  Some fish are faster than others.  Try to keep the speed bar centered!'
FishingFailureTooFast = 'You turned the crank too quickly.  Some fish are slower than others.  Try to keep the speed bar centered!'
FishingOverTankLimit = 'Your fish bucket is full. Go sell your fish to the Pet Shop Clerk and come back.'
FishingBroke = 'You do not have any more Jellybeans for bait! Ride the trolley or sell fish to the Pet Shop Clerks to earn more Jellybeans.'
FishingHowToFirstTime = 'Click and drag down from the Cast button. The farther down you drag, the stronger your cast will be. Adjust your angle to hit the fish targets.\n\nTry it now!'
FishingHowToFailed = 'Click and drag down from the Cast button. The farther down you drag, the stronger your cast will be. Adjust your angle to hit the fish targets.\n\nTry it again now!'
FishingJellybeanItem = '%s Jellybeans'
FishingNewEntry = 'New Species!'
FishingNewRecord = 'New Record!'
FishPokerCashIn = 'Cash In\n%s\n%s'
FishPokerLock = 'Lock'
FishPokerUnlock = 'Unlock'
FishPoker5OfKind = '5 of a Kind'
FishPoker4OfKind = '4 of a Kind'
FishPokerFullHouse = 'Full House'
FishPoker3OfKind = '3 of a Kind'
FishPoker2Pair = '2 Pair'
FishPokerPair = 'Pair'
PetTutorialTitle1 = 'The Doodle Panel'
PetTutorialTitle2 = 'Doodle SpeedChat'
PetTutorialTitle3 = 'Doodle Cattlelog'
PetTutorialNext = 'Next Page'
PetTutorialPrev = 'Previous Page'
PetTutorialDone = 'Done'
PetTutorialPage1 = 'Click on a Doodle to display the Doodle panel.  From here you can feed, scratch, and call the Doodle.'
PetTutorialPage2 = "Use the new 'Pets' area in the SpeedChat menu to get a Doodle to do a trick.  If he does it, reward him and he'll get better!"
PetTutorialPage3 = "Purchase new Doodle tricks from Clarabelle's Cattlelog.  Better tricks give better Toon-Ups!"

def getPetGuiAlign():
    return TextNode.ACenter


GardenTutorialTitle1 = 'Gardening'
GardenTutorialTitle2 = 'Flowers'
GardenTutorialTitle3 = 'Trees'
GardenTutorialTitle4 = 'How-to'
GardenTutorialTitle5 = 'Statues'
GardenTutorialNext = 'Next Page'
GardenTutorialPrev = 'Previous Page'
GardenTutorialDone = 'Done'
GardenTutorialPage1 = 'Toon up your Estate with a garden!  You can plant flowers, grow trees, harvest super-powerful gags, and decorate with statues!'
GardenTutorialPage2 = 'Flowers are finicky and require unique Jellybean recipes. Once grown, put them in the wheelbarrow to sell them and work toward Laff boosts!'
GardenTutorialPage3 = 'Use a gag from your inventory to plant a tree.  After a few days, that gag will do more damage!  Remember to keep it healthy or the damage boost will go away.'
GardenTutorialPage4 = 'Walk up to these spots to plant, water, dig up or harvest your garden.'
GardenTutorialPage5 = "Statues can be purchased in Clarabelle's Cattlelog. Increase your skill to unlock the more extravagant statues!"
EstatePlaneReturn = "Cog invasion!!!"
EstatePlaneHoliday = "Happy halloween!!!"
PlaygroundDeathAckMessage = TheCogs + ' took all your gags!\n\nYou are sad. You may not leave the playground until you are happy.'
DeathAck_1 = "IT APPEARS THE COGS\nHAVE STOLEN YOUR GAGS!"
DeathAck_2 = "YOU MAY NOT LEAVE UNTIL YOU'RE HAPPY."
DeathAck_3 = "CONTINUE"
ForcedLeaveFactoryAckMsg = 'The ' + Foreman + ' was defeated before you could reach him. You did not recover any Cog parts.'
ForcedLeaveMintAckMsg = 'The Mint Floor Supervisor was defeated before you could reach him. You did not recover any Cogbucks.'
HeadingToFactoryTitle = '%s'
ForemanConfrontedMsg = '%s is battling the ' + Foreman + '!'
MintBossConfrontedMsg = '%s is battling the Supervisor!'
StageBossConfrontedMsg = '%s is battling the District Attorney!'
StageToonEnterElevator = '%s\nhas entered the elevator!'
ForcedLeaveStageAckMsg = 'The Law Clerk was defeated before you could reach him. You did not recover any Jury Notices.'
MinigameWaitingForOtherToons = 'Waiting for other toons to join...'
MinigamePleaseWait = 'Please wait...'
DefaultMinigameTitle = 'Minigame Title'
DefaultMinigameInstructions = 'Minigame Instructions'
HeadingToMinigameTitle = '%s'
MinigamePowerMeterLabel = 'Power Meter'
MinigamePowerMeterTooSlow = 'Too\nslow'
MinigamePowerMeterTooFast = 'Too\nfast'
MinigameTemplateTitle = 'Minigame Template'
MinigameTemplateInstructions = 'This is a template minigame. Use it to create new minigames.'
CannonGameTitle = 'Cannon Game'
CannonGameInstructions = 'Shoot your toon into the water tower as quickly as you can. Use the mouse or the arrow keys to aim the cannon. Be quick and win a big reward for everyone!'
CannonGameReward = 'REWARD'
TwoDGameTitle = 'Toon Escape'
TwoDGameInstructions = 'Escape from the ' + Cog + ' den as soon as you can. Use arrow keys to run/jump and Ctrl to squirt a ' + Cog + '. Collect ' + Cog + ' treasures to gain even more points.'
TwoDGameElevatorExit = 'EXIT'
TugOfWarGameTitle = 'Tug-of-War'
TugOfWarInstructions = "Alternately tap the left and right arrow keys just fast enough to line up the green bar with the red line. Don't tap them too slow or too fast, or you'll end up in the water!"
TugOfWarGameGo = 'GO!'
TugOfWarGameReady = 'Ready...'
TugOfWarGameEnd = 'Good game!'
TugOfWarGameTie = 'You tied!'
TugOfWarPowerMeter = 'Power meter'
PatternGameTitle = 'Match Jaymo'
PatternGameInstructions = 'Jaymo will show you a dance sequence. ' + "Try to repeat Jaymo's dance just the way you see it using the arrow keys!"
PatternGameWatch = 'Watch these dance steps...'
PatternGameGo = 'GO!'
PatternGameRight = 'Good, %s!'
PatternGameWrong = 'Oops!'
PatternGamePerfect = 'That was perfect, %s!'
PatternGameBye = 'Thanks for playing!'
PatternGamePleaseWait = 'Please wait...'
PatternGameFaster = 'You were\nfaster!'
PatternGameFastest = 'You were\nthe fastest!'
PatternGameYouCanDoIt = 'Come on!\nYou can do it!'
PatternGameOtherFaster = '\nwas faster!'
PatternGameOtherFastest = '\nwas the fastest!'
PatternGameGreatJob = 'Great Job!'
PatternGameRound = 'Round %s!'
PatternGameImprov = 'You did great!  Now Improv!'
RaceGameTitle = 'Race Game'
RaceGameInstructions = 'Click a number. Choose wisely! You only advance if no one else picked the same number.'
RaceGameWaitingChoices = 'Waiting for other toons to choose...'
RaceGameCardText = '%(name)s draws: %(reward)s'
RaceGameCardTextBeans = '%(name)s receives: %(reward)s'
RaceGameCardTextHi1 = '%(name)s is one Fabulous Toon!'
RaceGameForwardOneSpace = ' forward 1 space'
RaceGameForwardTwoSpaces = ' forward 2 spaces'
RaceGameForwardThreeSpaces = ' forward 3 spaces'
RaceGameBackOneSpace = ' back 1 space'
RaceGameBackTwoSpaces = ' back 2 spaces'
RaceGameBackThreeSpaces = ' back 3 spaces'
RaceGameOthersForwardThree = ' all others forward \n3 spaces'
RaceGameOthersBackThree = 'all others back \n3 spaces'
RaceGameInstantWinner = 'Instant Winner!'
RaceGameJellybeans2 = '2 Jellybeans'
RaceGameJellybeans4 = '4 Jellybeans'
RaceGameJellybeans10 = '10 Jellybeans!'
RingGameTitle = 'Ring Game'
RingGameInstructionsSinglePlayer = 'Try to swim through as many of the %s rings as you can.  Use the arrow keys to swim.'
RingGameInstructionsMultiPlayer = 'Try to swim through the %s rings.  Other toons will try for the other colored rings.  Use the arrow keys to swim.'
RingGameMissed = 'MISSED'
RingGameGroupPerfect = 'GROUP\nPERFECT!!'
RingGamePerfect = 'PERFECT!'
RingGameGroupBonus = 'GROUP BONUS'
ColorRed = 'red'
ColorGreen = 'green'
ColorOrange = 'orange'
ColorPurple = 'purple'
ColorWhite = 'white'
ColorBlack = 'black'
ColorYellow = 'yellow'
DivingGameTitle = 'Treasure Dive'
DivingInstructionsSinglePlayer = 'Treasures will appear at the bottom of the lake.  Use the arrow keys to swim.  Avoid the fish and get the treasures up to the boat!'
DivingInstructionsMultiPlayer = 'Treasures will appear at the bottom of the lake.  Use the arrow keys to swim.  Work together to get the treasures up to the boat!'
DivingGameTreasuresRetrieved = 'Treasures Retrieved'
TargetGameTitle = 'Toon Slingshot'
TargetGameInstructionsSinglePlayer = 'Use your umbrella to land on the targets. The smaller the target, the more Jellybeans you get!'
TargetGameInstructionsMultiPlayer = 'Use your umbrella to land on the targets. The smaller the target, the more Jellybeans you get!'
TargetGameBoard = 'Round %s - Keeping Best Score'
TargetGameCountdown = 'Forced launch in %s seconds'
TargetGameCountHelp = 'Pound left and right arrows for power, stop to launch'
TargetGameFlyHelp = 'Press down to open umbrella'
TargetGameFallHelp = 'Use the arrow keys to land on target'
TargetGameBounceHelp = ' Bouncing can knock you off target'
TagGameTitle = 'Tag Game'
TagGameInstructions = 'Collect the treasures. You cannot collect treasure when you are IT!'
TagGameYouAreIt = 'You Are IT!'
TagGameSomeoneElseIsIt = '%s is IT!'
MazeGameTitle = 'Maze Game'
MazeGameInstructions = 'Collect the treasures. Try to get them all, but look out for the ' + Cogs + '!'
CatchGameTitle = 'Catching Game'
CatchGameInstructions = 'Catch as many %(fruit)s as you can. Watch out for the ' + Cogs + ", and try not to 'catch' any %(badThing)s!"
CatchGamePerfect = 'PERFECT!'
CatchGameApples = 'apples'
CatchGameOranges = 'oranges'
CatchGamePears = 'pears'
CatchGameCoconuts = 'coconuts'
CatchGameWatermelons = 'watermelons'
CatchGamePineapples = 'pineapples'
CatchGameAnvils = 'anvils'
PieTossGameTitle = 'Pie Toss Game'
PieTossGameInstructions = 'Toss pies at the targets.'
CogThiefGameTitle = 'Cog Thief'
CogThiefGameInstructions = 'Stop these Cogs from stealing our Gags! Press the Control key to throw pies. But be careful... they have a tendancy to explode!'
CogThiefBarrelsSaved = '%(num)d Barrels\nSaved!'
CogThiefBarrelSaved = '%(num)d Barrel\nSaved!'
CogThiefNoBarrelsSaved = 'No Barrels\nSaved'
CogThiefPerfect = 'PERFECT!'
MinigameRulesPanelPlay = 'PLAY'
MinigameRulesPanelSkip = 'SKIP\n%s/%s'
GagShopName = "Toontown Gag Shop"
GagShopPlayAgain = 'PLAY\nAGAIN'
GagShopBackToPlayground = 'EXIT BACK TO\nPLAYGROUND'
GagShopYouHave = 'You have %s Jellybeans to spend'
GagShopYouHaveOne = 'You have 1 Jellybean to spend'
GagShopTooManyProps = 'Sorry, you have too many props'
GagShopDoneShopping = 'DONE\nSHOPPING'
GagShopTooManyOfThatGag = 'Sorry, you have enough %s already'
GagShopInsufficientSkill = 'You do not have enough skill for that yet'
GagShopNotEnoughJellybeans = 'You do not have enough Jellybeans for that gag'
GagShopYouPurchased = 'You purchased %s'
GagShopOutOfJellybeans = 'Sorry, you are all out of Jellybeans!'
GagShopPlayerDisconnected = '%s has disconnected'
GagShopPlayerExited = '%s has exited'
GagShopPlayerPlayAgain = 'Play Again'
GagShopPlayerBuying = 'Buying'
GenderShopFollow = 'Follow me!'
GenderShopSeeYou = 'See you later!'
GenderShopBoyButtonText = 'Boy'
GenderShopGirlButtonText = 'Girl'
BodyShopHead = 'Head'
BodyShopBody = 'Body'
BodyShopLegs = 'Legs'
ColorShopToon = 'Toon Color'
ColorShopHead = 'Head'
ColorShopBody = 'Body'
ColorShopLegs = 'Legs'
ColorShopGloves = 'Gloves'
ColorShopParts = 'Multi Color'
ColorShopAll = 'Single Color'
ClothesShopShorts = 'Shorts'
ClothesShopShirt = 'Shirts'
ClothesShopBottoms = 'Bottoms'
TrackShopFirstTrack = 'First Track:'
TrackShopSecondTrack = 'Second Track:'
MakeAToonDone = 'Done'
MakeAToonCancel = lCancel
MakeAToonNext = lNext
MakeAToonLast = 'Back'
CreateYourToon = 'Click the arrows to create your toon.'
CreateYourToonTitle = 'Choose  Boy  or  Girl'
ShapeYourToonTitle = 'Choose  Your  Type'
PaintYourToonTitle = 'Choose  Your  Color'
PickClothesTitle = 'Choose  Your  Clothes'
PickTracksTitle = 'Choose  Your  Tracks'
NameToonTitle = 'Choose  Your  Name'
CreateYourToonHead = "Click the 'head' arrows to pick different animals."
MakeAToonClickForNextScreen = 'Click the arrow below to go to the next screen.'
PickClothes = 'Click the arrows to pick clothes!'
PaintYourToon = 'Click the arrows to paint your toon!'
MakeAToonYouCanGoBack = 'You can go back to change your body too!'
MakeAFunnyName = 'Choose a funny name for your toon with my Pick-A-Name game!'
MustHaveAFirstOrLast1 = "Your toon should have a first or last name, don't you think?"
MustHaveAFirstOrLast2 = "Don't you want your toon to have a first or last name?"
ApprovalForName1 = "That's it, your toon deserves a great name!"
ApprovalForName2 = 'Toon names are the best kind of names!'
MakeAToonLastStep = 'Last step before going to Toontown!'
PickANameYouLike = 'Pick a name you like!'
TitleCheckBox = 'Title'
FirstCheckBox = 'First'
LastCheckBox = 'Last'
RandomButton = 'Random'
ShuffleButton = 'Shuffle'
NameShopSubmitButton = 'Submit'
TypeANameButton = 'Type-A-Name'
TypeAName = "Don't like these names?\nClick here -->"
PickAName = 'Try the PickAName game!\nClick here -->'
PickANameButton = 'Pick-A-Name'
RejectNameText = 'That name is not allowed. Please try again.'
WaitingForNameSubmission = 'Submitting your name...'
PetshopUnknownName = 'Name: ???'
PetshopDescGender = 'Gender:\t%s'
PetshopDescCost = 'Cost:\t%s Jellybeans'
PetshopDescTrait = 'Traits:\t%s'
PetshopDescStandard = 'Standard'
PetshopCancel = lCancel
PetshopSell = 'Sell Fish'
PetshopAdoptAPet = 'Adopt a Doodle'
PetshopReturnPet = 'Return your Doodle'
PetshopAdoptConfirm = 'Adopt %s for %d Jellybeans?'
PetshopGoBack = 'Go Back'
PetshopAdopt = 'Adopt'
PetshopReturnConfirm = 'Return %s?'
PetshopReturn = 'Return'
PetshopChooserTitle = "TODAY'S DOODLES"
PetshopGoHomeText = 'Would you like to go to your estate to play with your new Doodle?'
NameShopContinueSubmission = 'Continue Submission'
NameShopChooseAnother = 'Choose Another Name'
NameShopToonCouncil = 'The Toon Council\nwill review your\nname.  ' + 'Review may\ntake a few days.\nWhile you wait\nyour name will be\n '
PleaseTypeName = 'Please type your name:'
AllNewNames = 'All new names must be\napproved by the Toon Council.'
NameMessages = 'Be creative, and remember:\nno NPC names, please.'
NameShopNameRejected = 'The name you\nsubmitted has\nbeen rejected.'
NumToColor = ['White',
 'Peach',
 'Bright Red',
 'Red',
 'Maroon',
 'Sienna',
 'Brown',
 'Tan',
 'Coral',
 'Orange',
 'Yellow',
 'Cream',
 'Citrine',
 'Lime',
 'Sea Green',
 'Green',
 'Light Blue',
 'Aqua',
 'Blue',
 'Periwinkle',
 'Royal Blue',
 'Slate Blue',
 'Purple',
 'Lavender',
 'Pink',
 'Plum',
 'Black',
 'Mountain Green',
 'Icy Blue',
 'Desert Sand',
 'Mint',
 'Charcoal',
 'Hot Pink',
 'Honey Mustard',
 'Gray',
 'Neon Orange',
 'Sapphire',
 'Crimson',
 'Emerald',
 'Bronze',
 'Neon Green',
 'Steel Blue']
AnimalToSpecies = {'dog': 'Dog',
 'cat': 'Cat',
 'mouse': 'Mouse',
 'horse': 'Horse',
 'rabbit': 'Rabbit',
 'duck': 'Duck',
 'monkey': 'Monkey',
 'bear': 'Bear',
 'pig': 'Pig'}
 #'fox': 'Fox',
 #'hedgehog': 'Hedgehog'
NameTooLong = 'That name is too long. Please try again.'
ToonAlreadyExists = 'You already have a toon named %s!'
NameAlreadyInUse = 'That name is already used!'
EmptyNameError = 'You must enter a name first.'
NameError = 'Sorry.  That name will not work.'
NCTooShort = 'That name is too short.'
NCNoDigits = 'Your name cannot contain numbers.'
NCNeedLetters = 'Each word in your name must contain some letters.'
NCNeedVowels = 'Each word in your name must contain some vowels.'
NCAllCaps = 'Your name cannot be all capital letters.'
NCMixedCase = 'That name has too many capital letters.'
NCBadCharacter = "Your name cannot contain the character '%s'"
NCGeneric = 'Sorry, that name will not work.'
NCTooManyWords = 'Your name cannot be more than four words long.'
NCDashUsage = "Dashes may only be used to connect two words together (like in 'Boo-Boo')."
NCCommaEdge = 'Your name may not begin or end with a comma.'
NCCommaAfterWord = 'You may not begin a word with a comma.'
NCCommaUsage = 'That name does not use commas properly. Commas must join two words together, like in the name "Dr. Quack, MD". Commas must also be followed by a space.'
NCPeriodUsage = 'That name does not use periods properly. Periods are only allowed in words like "Mr.", "Mrs.", "J.T.", etc.'
NCApostrophes = 'That name has too many apostrophes.'
RemoveTrophy = lToonHQ + ': ' + TheCogs + ' took over one of the buildings you rescued!'
STOREOWNER_TOOKTOOLONG = 'Need more time to think?'
STOREOWNER_GOODBYE = 'See you later!'
STOREOWNER_NEEDJELLYBEANS = 'You need to ride the Trolley to get some Jellybeans.'
STOREOWNER_GREETING = 'Choose what you want to buy.'
STOREOWNER_GREETING1 = 'Choose what you want to buy for 500 Jellybeans.'
STOREOWNER_BROWSING_JBS = 'You can browse, but you need at least 500 Jellybeans to buy.'
STOREOWNER_NOFISH = 'Come back here to sell fish to the Pet Shop for Jellybeans.'
STOREOWNER_THANKSFISH = 'Thanks! The Pet Shop will love these. Bye!'
STOREOWNER_THANKSFISH_PETSHOP = 'These are some fine specimens! Thanks.'
STOREOWNER_PETRETURNED = "Don't worry.  We'll find a good home for your Doodle."
STOREOWNER_PETADOPTED = 'Congratulations on purchasing a Doodle! You can play with your new friend at your estate.'
STOREOWNER_PETCANCELED = 'Remember, if you see a Doodle you like, make sure to adopt him before someone else does!'
STOREOWNER_NOROOM = 'Hmm...you might want to make room in your closet before you buy new clothes.\n'
STOREOWNER_CONFIRM_LOSS = 'Your closet is full.  You will lose the clothes you were wearing.'
STOREOWNER_OK = lOK
STOREOWNER_CANCEL = lCancel
STOREOWNER_TROPHY = 'Wow! You collected %s of %s fish. That deserves a trophy and a Laff boost!'
SuitInvasionPrefix = '%s: ' % lToonHQ
SuitInvasionBegin = [
 'A Cog invasion has begun!!!',
 '%(plural)s have taken over Toontown!!!'
]
SuitInvasionEnd = [
 'The %(singular)s invasion has ended!!!',
 'The Toons have saved the day once again!!!'
]
SuitInvasionUpdate = [
 'Keep it up, Toons!!!',
 "The Cogs are beginning to explode in laughter!!!"
]
SuitInvasionBulletin = [
 'There is a Cog invasion in progress!!!',
 '%(plural)s have taken over Toontown!!!'
]
SkelecogInvasionBegin = [
 "This just in, Sellbot HQ's factory is going bonkers!",
 "Sellbot HQ's factory is pushing out incomplete cogs!",
 '%(singular)s Skelecogs have taken over Toontown!!!'
]
SkelecogInvasionEnd = [
 'The %(singular)s Skelecog invasion has ended!!!',
 'The Toons have saved the day once again!!!'
]
SkelecogInvasionBulletin = [
 'There is a Cog invasion in progress!!!',
 "Sellbot HQ's factory has pushed out incomplete Cogs!",
 '%(singular)s Skelecogs have taken over Toontown!!!'
]
WaiterInvasionBegin = [
 'Uh oh, it appears that the Cogs banquet has been rescheduled!',
 'The Waiter %(singular)s are invading Toontown!!!'
]
WaiterInvasionEnd = [
 'The Waiter %(singular)s waiters have been defeated!!!',
 'The Toons have saved the day once again!!!'
]
WaiterInvasionBulletin = [
 'There is a Cog invasion in progress!!!',
 'The Cogs banquet has been rescheduled!!!',
 'The Waiter %(singular)s are invading Toontown!!!'
]
V2InvasionBegin = [
 "Oh my, stock up on gags toons!",
 'The Toon HQ has spotted a Version 2.0 Cog Invasion!',
 'The V2 %(plural)s have taken over Toontown!!!'
]
V2InvasionEnd = [
 'The V2 %(singular)s invasion has ended!!!',
 'The Toons have saved the day once again!!!'
]
V2InvasionBulletin = [
 "There is a Cog invasion in progress!!!",
 'The Toon HQ has spotted a storm of Version 2.0 Cogs!',
 'The V2 %(plural)s have taken over Toontown!!!'
]
ExecutiveInvasionBegin = [
 "This just in, Sellbot HQ's factory is going bonkers!",
 "Sellbot HQ's factory has pushed out powerful Cogs!",
 'The Executive %(plural)s have taken over Toontown!!!'
]
ExecutiveInvasionEnd = [
 'The Executive %(singular)s invasion has ended!!!',
 'The Toons have saved the day once again!!!'
]
ExecutiveInvasionBulletin = [
 "There is a Cog invasion in progress!!!",
 "Sellbot HQ's factory has pushed out powerful Cogs!",
 'The Executive %(plural)s have taken over Toontown!!!'
]
VirtualInvasionBegin = [
 'A Cog invasion has begun!!!',
 'Virtual %(plural)s have taken over Toontown!!!'
]
VirtualInvasionEnd = [
 'The Virtual %(singular)s invasion has ended!!!',
 'The Toons have saved the day once again!!!'
]
VirtualInvasionBulletin = [
 "There is a Cog invasion in progress!!!",
 'Virtual %(plural)s have taken over Toontown!!!'
]
LeaderboardTitle = 'Toon Platoon'
QuestScript101_0 = 'Come here! Use the arrow keys to move.'
QuestScript101_1 = 'These are Cogs. They are robots that are trying to take over Toontown.'
QuestScript101_2 = 'There are many different kinds of Cogs and...'
QuestScript101_3 = '...they turn happy Toon buildings...'
QuestScript101_4 = '...into ugly Cog buildings!'
QuestScript101_5 = "But Cogs can't take a joke!"
QuestScript101_6 = 'A good gag will stop them.'
QuestScript101_8 = 'You also need a Laff meter.'
QuestScript101_9 = "If your Laff meter gets too low, you'll be sad!"
QuestScript101_10 = 'A happy Toon is a healthy Toon!'
QuestScript101_11 = "OH NO! There's a Cog outside my shop!"
QuestScript101_12 = 'HELP ME, PLEASE! Defeat that Cog!'
QuestScript101_13 = 'Here is your first ToonTask!'
QuestScript101_14 = 'Hurry up! Go defeat that Flunky!'
QuestScript110_1 = 'Good work defeating that Flunky. Let me give you a Shticker Book...'
QuestScript110_2 = 'The book is full of good stuff.'
QuestScript110_3 = "Open it, and I'll show you."
QuestScript110_4 = "The map shows where you've been."
QuestScript110_5 = 'Turn the page to see your gags...'
QuestScript110_6 = 'You can see your gags here.'
QuestScript110_7 = 'Turn the page to see your tasks.'
QuestScript110_8 = 'Take a ride on the trolley, and earn jelly beans to buy gags!'
QuestScript110_9 = 'To get to the trolley, go out the door behind me and head for the playground.'
QuestScript110_10 = 'Now, close the book and find the trolley!'
QuestScript110_11 = 'Return to Toon HQ when you are done. Bye!'
QuestScript145_1 = 'I see you had no problem with the trolley!\x07Listen, the Cogs have stolen our blackboard eraser.\x07Go into the streets and fight Cogs until you recover the eraser.\x07To reach the streets go through one of the tunnels like this:'
QuestScript145_2 = "When you find our eraser, bring it back here.\x07Don't forget, if you need gags, ride the trolley.\x07Also, if you need to recover Laff points, collect ice cream cones in the Playground."
QuestScript150_1 = 'Great work!\x07Toontown is more fun when you have friends!'
QuestScript150_2 = 'To make friends, find another toon, and use the New Friend button.'
QuestScript150_3 = 'Once you have made a friend, come back here.'
QuestScript150_4 = 'Some tasks are too difficult to do alone!'
MissingKeySanityCheck = 'Ignore me'
SellbotBossName = 'Senior V. P.'
CashbotBossName = 'C. F. O.'
LawbotBossName = 'Chief Justice'
BossbotBossName = 'C. E. O.'
BossCogNameWithDept = '%(name)s\n%(dept)s'
BossCogPromoteDoobers = 'You are hereby promoted to full-fledged %s.  Congratulations!'
BossCogDoobersAway = {'s': 'Go! And make that sale!'}
BossCogWelcomeToons = 'Welcome, new Cogs!'
BossCogPromoteToons = 'You are hereby promoted to full-fledged %s.  Congratu--'
CagedToonInterruptBoss = 'Hey! Hiya! Hey over there!'
CagedToonRescueQuery = 'So, did you Toons come to rescue me?'
BossCogDiscoverToons = 'Huh?  Toons!  In disguise!'
BossCogAttackToons = 'Attack!!'
CagedToonDrop = ["Great job!  You're wearing him down!",
 "Keep after him!  He's on the run!",
 'You guys are doing great!',
 "Fantastic!  You've almost got him now!"]
CagedToonPrepareBattleTwo = "Look out, he's trying to get away!\x07Help me, everyone--get up here and stop him!"
CagedToonPrepareBattleThree = "Hooray, I'm almost free!\x07Now you need to attack the V.P. Cog directly.\x07I've got a whole bunch of pies you can use!\x07Jump up and touch the bottom of my cage and I'll give you some pies.\x07Press the Delete key to throw pies once you've got them!"
BossBattleNeedMorePies = 'You need to get more pies!'
BossBattleHowToGetPies = 'Jump up to touch the cage to get pies.'
BossBattleHowToThrowPies = 'Press the Delete key to throw pies!'
CagedToonYippee = 'Yippee!'
CagedToonThankYou = "It's great to be free!\x07Thanks for all your help!\x07I am in your debt.\x07Here's my card. If you ever need a hand in battle, give a shout!\x07Just click on your SOS button."
CagedToonMVP = "\x07Oh!\x07It seems like you contributed the most to defeating the V.P!\x07The Toon Council has rewarded you %s jellybeans!"
CagedToonPromotion = "\x07Say--that V.P. Cog left behind your promotion papers.\x07I'll file them for you on the way out, so you'll get your promotion!"
CagedToonLastPromotion = "\x07Wow, you've reached level %s on your Cog suit!\x07Cogs don't get promoted higher than that.\x07You can't upgrade your Cog suit anymore, but you can certainly keep rescuing Toons!"
CagedToonHPBoost = "\x07You've rescued a lot of Toons from this HQ.\x07The Toon Council has decided to give you another Laff point. Congratulations!"
CagedToonMaxed = '\x07I see that you have a level %s Cog suit. Very impressive!\x07On behalf of the Toon Council, thank you for coming back to rescue more Toons!'
CagedToonGoodbye = 'See ya!'
CagedToonBattleThree = {10: 'Nice jump, %(toon)s.  Here are some pies!',
 11: 'Hi, %(toon)s!  Have some pies!',
 12: "Hey there, %(toon)s!  You've got some pies now!",
 20: 'Hey, %(toon)s!  Jump up to my cage and get some pies to throw!',
 21: 'Hi, %(toon)s!  Use the Ctrl key to jump up and touch my cage!',
 100: 'Press the Delete key to throw a pie.',
 101: 'The blue power meter shows how high your pie will go.',
 102: 'First try to lob a pie inside his undercarriage to gum up his works.',
 103: 'Wait for the door to open, and throw a pie straight inside.',
 104: "When he's dizzy, hit him in the face or chest to knock him back!",
 105: "You'll know you've got a good hit when you see the splat in color.",
 106: 'If you hit a Toon with a pie, it gives that Toon a Laff point!'}
CagedToonBattleThreeMaxGivePies = 12
CagedToonBattleThreeMaxTouchCage = 21
CagedToonBattleThreeMaxAdvice = 106
CashbotBossHadEnough = "That's it.  I've had enough of these pesky Toons!"
CashbotBossOuttaHere = "I've got a train to catch!"
ResistanceToonCongratulations = "You did it!  Congratulations!\x07You're an asset to the Resistance!\x07Here's a special phrase you can use in a tight spot:\x07%s\x07When you say it, %s.\x07But you can only use it once, so choose that time well!"
ResistanceToonToonupInstructions = 'all the Toons near you will gain %s Laff points'
ResistanceToonToonupAllInstructions = 'all the Toons near you will gain full Laff points'
ResistanceToonMoneyInstructions = 'all the Toons near you will gain %s jellybeans'
ResistanceToonMoneyAllInstructions = 'all the Toons near you will fill their jellybean jars'
ResistanceToonTicketsInstructions = 'all the Toons near you will gain %s tickets'
ResistanceToonRestockInstructions = 'all the Toons near you will restock their "%s" gags'
ResistanceToonRestockAllInstructions = 'all the Toons near you will restock all their gags'
ResistanceToonMeritsInstructions = 'all the Toons near you will fill part of their %s'
ResistanceToonMeritsAllInstructions = 'all the Toons near you will fill part of all their promotion papers'
ResistanceToonLastPromotion = "\x07Wow, you've reached level %s on your Cog suit!\x07Cogs don't get promoted higher than that.\x07You can't upgrade your Cog suit anymore, but you can certainly keep working for the Resistance!"
ResistanceToonHPBoost = "\x07You've done a lot of work for the Resistance.\x07The Toon Council has decided to give you another Laff point. Congratulations!"
ResistanceToonMaxed = '\x07I see that you have a level %s Cog suit. Very impressive!\x07On behalf of the Toon Council, thank you for coming back to rescue more Toons!'
CashbotBossCogAttack = 'Get them!!!'
ResistanceToonWelcome = 'Hey, you made it!  Follow me to the main vault before the C.F.O. finds us!'
ResistanceToonTooLate = "Blast it!  We're too late!"
CashbotBossDiscoverToons1 = 'Ah-HAH!'
CashbotBossDiscoverToons2 = 'I thought I smelled something a little toony in here!  Imposters!'
ResistanceToonKeepHimBusy = "Keep him busy!  I'm going to set a trap!"
ResistanceToonWatchThis = 'Watch this!'
CashbotBossGetAwayFromThat = 'Hey!  Get away from that!'
ResistanceToonCraneInstructions1 = 'Control a magnet by stepping up to a podium.'
ResistanceToonCraneInstructions2 = 'Use the arrow keys to move the crane, and press the Ctrl key to grab an object.'
ResistanceToonCraneInstructions3 = "Grab a safe with a magnet and knock the C.F.O.'s safe-ty helmet off."
ResistanceToonCraneInstructions4 = 'Once his helmet is gone, grab a disabled goon and hit him in the head!'
ResistanceToonGetaway = 'Eek!  Gotta run!'
CashbotCraneLeave = 'Leave Crane'
CashbotCraneAdvice = 'Use the arrow keys to move the overhead crane.'
CashbotMagnetAdvice = 'Hold down the control key to pick things up.'
CashbotCraneLeaving = 'Leaving crane'
MintElevatorRejectMessage = 'You cannot enter the Mints until you have completed your %s Cog Suit.'
BossElevatorRejectMessage = 'You cannot board this elevator until you have earned a promotion.'
SellbotRentalSuitMessage = "Wear this Rental Suit so you can get close enough to the VP to attack.\n\nYou won't earn Merits or promotions, but you can rescue a Toon for an SOS reward!"
SellbotCogSuitNoMeritsMessage = "Your Sellbot Disguise will get you in, but since you don't have enough Merits, you won't earn a promotion.\n\nIf you rescue the trapped Toon, you will earn an SOS Toon reward!"
SellbotCogSuitHasMeritsMessage = "It's Operation: Storm Sellbot!\n\nBring 5 or more Rental Suit Toons with you to defeat the VP and earn credit towards a reward!"
LawbotRentalSuitMessage = "Wear this Rental Suit so you can get close enough to the CJ to attack.\n\nYou won't earn Jury Notices or promotions, but you can pass the bar exam for a Cog Summon!"
LawbotCogSuitNoNoticesMessage = "Your Lawbot Disguise will get you in, but since you don't have enough Jury Notices, you won't earn a promotion.\n\nIf you pass the bar exam, you will earn a Cog Summon!"
LawbotCogSuitHasNoticesMessage = "It's Operation: Lawbots Lose!\n\nBring 7 or more Rental Suit Toons with you to defeat the CJ and earn credit towards a summon!"
CashbotRentalSuitMessage = "Wear this Rental Suit so you can get close enough to the CFO to attack.\n\nYou wont earn Cogbucks or promotions, but you can delay the CFO for a Toon Unite!"
CashbotCogSuitNoCogbucksMessage = "Your Cashbot Disguise will get you in, but since you don't have enough Cogbucks, you won't earn a promotion.\n\n If you delay the CFO, you will earn a Toon Unite!"
CashbotCogSuitHasCogbucksMessage = "It's Operation: Cashbot Chaos!\n\n Bring 6 or more Rental Suit Toons with you to defeat the CFO and earn credit towards a unite!"
BossbotRentalSuitMessage = "Wear this Rental Suit so you can get close enough to the CEO to attack.\n\bYou wont earn Stock Options or promotions, but you can soak the CEO for a Fire!"
BossbotCogSuitNoOptionsMessage = "Your Bossbot Disguise will get you in, but since you don't have enough Stock Options you won't warn a promotion.\n\n If you soak the CEO, you will earn a Fire!"
BossbotCogSuitHasOptionsMessage = "It's Operation: Besiege Bossbot!\n\n Bring in 8 Rental Suit Toons with you to defeat the CEO and earn credit towards a Fire!"
FurnitureTypeName = 'Furniture'
PaintingTypeName = 'Painting'
ClothingTypeName = 'Clothing'
ChatTypeName = 'SpeedChat Phrase'
EmoteTypeName = 'Acting Lessons'
BeanTypeName = 'Jellybeans'
PoleTypeName = 'Fishing Pole'
WindowViewTypeName = 'Window View'
PetTrickTypeName = 'Doodle Training'
GardenTypeName = 'Garden Supplies'
RentalTypeName = 'Rental Item'
GardenStarterTypeName = 'Gardening Kit'
NametagTypeName = 'Nametag'
AccessoryTypeName = 'Accessory'
HatStylesDescriptions = {'hbb1': 'Green Baseball Cap',
 'kmh1': 'Mouskateer',
 'hbb2': 'Blue Baseball Cap',
 'hbb3': 'Orange Baseball Cap',
 'hsf1': 'Beige Safari Hat',
 'hsf2': 'Brown Safari Hat',
 'hsf3': 'Green Safari Hat',
 'hrb1': 'Pink Bow',
 'hrb2': 'Red Bow',
 'hrb3': 'Purple Bow',
 'hht1': 'Pink Heart',
 'hht2': 'Yellow Heart',
 'htp1': 'Black Top Hat',
 'htp2': 'Blue Top Hat',
 'hav1': 'Anvil Hat',
 'hfp1': 'Flower Hat',
 'hsg1': 'Sandbag Hat',
 'hwt1': 'Weight Hat',
 'hfz1': 'Fez Hat',
 'hgf1': 'Golf Hat',
 'hpt1': 'Party Hat',
 'hpt2': 'Toon Party Hat',
 'hpb1': 'Fancy Hat',
 'hcr1': 'Crown',
 'hcw1': 'Cowboy Hat',
 'hpr1': 'Pirate Hat',
 'hpp1': 'Propeller Hat',
 'hfs1': 'Fishing Hat',
 'hsb1': 'Sombrero Hat',
 'hst1': 'Straw Hat',
 'hsu1': 'Sun Hat',
 'hrb4': 'Yellow Bow',
 'hrb5': 'Checker Bow',
 'hrb6': 'Light Red Bow',
 'hrb7': 'Rainbow Bow',
 'hat1': 'Antenna Thingy',
 'hhd1': 'Beehive Hairdo',
 'hbw1': 'Bowler Hat',
 'hch1': 'Chef Hat',
 'hdt1': 'Detective Hat',
 'hft1': 'Fancy Feathers Hat',
 'hfd1': 'Fedora',
 'hmk1': "Mickey's Band Hat",
 'hft2': 'Feather Headband',
 'hhd2': 'Pompadour Hairdo',
 'hpc1': 'Princess Hat',
 'hrh1': 'Archer Hat',
 'hhm1': 'Roman Helmet',
 'hat2': 'Spider Antenna Thingy',
 'htr1': 'Tiara',
 'hhm2': 'Viking Helmet',
 'hwz1': 'Witch Hat',
 'hwz2': 'Wizard Hat',
 'hhm3': 'Conquistador Helmet',
 'hhm4': 'Firefighter Helmet',
 'hfp2': 'Anti-Cog Control Hat',
 'hhm5': 'Miner Hat',
 'hnp1': 'Napoleon Hat',
 'hpc2': 'Pilot Cap',
 'hph1': 'Cop Hat',
 'hwg1': 'Rainbow Wacky Wig',
 'hbb4': 'Yellow Baseball Cap',
 'hbb5': 'Red Baseball Cap',
 'hbb6': 'Aqua Baseball Cap',
 'hsl1': 'Sailor Hat',
 'hfr1': 'Samba Hat',
 'hby1': 'Bobby Hat',
 'hrb8': 'Pink Dots Bow',
 'hjh1': 'Jester Hat',
 'hbb7': 'Purple Baseball Cap',
 'hrb9': 'Green Checker Bow',
 'hwt2': 'Winter Hat',
 'hhw1': 'Bandana',
 'hhw2': 'Toonosaur Hat',
 'hob1': 'Jamboree Hat',
 'hbn1': 'Bird Hat'}
GlassesStylesDescriptions = {'grd1': 'Round Glasses',
 'gmb1': 'White Mini Blinds',
 'gnr1': 'Purple Narrow Glasses',
 'gst1': 'Yellow Star Glasses',
 'g3d1': 'Movie Glasses',
 'gav1': 'Aviator',
 'gce1': 'Cateye Glasses',
 'gdk1': 'Nerd Glasses',
 'gjo1': 'Celebrity Shades',
 'gsb1': 'Scuba Mask',
 'ggl1': 'Goggles',
 'ggm1': 'Groucho Glasses',
 'ghg1': 'Heart Glasses',
 'gie1': 'Bug Eye Glasses',
 'gmt1': 'Black Secret ID Mask',
 'gmt2': 'Blue Secret ID Mask',
 'gmt3': 'Blue Carnivale Mask',
 'gmt4': 'Purple Carnivale Mask',
 'gmt5': 'Aqua Carnivale Mask',
 'gmn1': 'Monocle',
 'gmo1': 'Smooch Glasses',
 'gsr1': 'Square Frame Glasses',
 'ghw1': 'Skull Eyepatch',
 'ghw2': 'Gem Eyepatch',
 'gag1': 'Alien Eyes',
 'ghy1': 'Hypno Lure Look'}
BackpackStylesDescriptions = {'bpb1': 'Blue Backpack',
 'bpb2': 'Orange Backpack',
 'bpb3': 'Purple BackPack',
 'bpd1': 'Red Dot Backpack',
 'bpd2': 'Yellow Dot Backpack',
 'bwg1': 'Bat Wings',
 'bwg2': 'Bee Wings',
 'bwg3': 'DragonFly Wings',
 'bst1': 'Scuba Tank',
 'bfn1': 'Shark Fin',
 'baw1': 'White Angel Wings',
 'baw2': 'Rainbow Angel Wings',
 'bwt1': 'Toys Backpack',
 'bwg4': 'Butterfly Wings',
 'bwg5': 'Pixie Wings',
 'bwg6': 'Dragon Wings',
 'bjp1': 'Jet Pack',
 'blg1': 'Bug Backpack',
 'bsa1': 'Plush Bear Pack',
 'bwg7': 'Bird wings',
 'bsa2': 'Plush Cat Pack',
 'bsa3': 'Plush Dog Pack',
 'bap1': 'Airplane Wings',
 'bhw1': 'Pirate Sword',
 'bhw2': 'Super Toon Cape',
 'bhw3': 'Vampire Cape',
 'bhw4': 'Toonosaur Backpack',
 'bob1': 'Jamboree Pack',
 'bfg1': 'Gag Attack Pack',
 'bfl1': 'Cog Pack'}
ShoesStylesDescriptions = {'sat1': 'Green Athletic Shoes',
 'sat2': 'Red Athletic Shoes',
 'smb1': 'Green Toon Boots',
 'scs1': 'Green Sneakers',
 'swt1': 'Wingtips',
 'smj1': 'Black Fancy Shoes',
 'sdk1': 'Boat Shoes',
 'sat3': 'Yellow Athletic Shoes',
 'scs2': 'Black Sneakers',
 'scs3': 'White Sneakers',
 'scs4': 'Pink Sneakers',
 'scb1': 'Cowboy Boots',
 'sfb1': 'Purple Boots',
 'sht1': 'Green Hi Top Sneakers',
 'smj2': 'Brown Fancy Shoes',
 'smj3': 'Red Fancy Shoes',
 'ssb1': 'Red Super Toon Boots',
 'sts1': 'Green Tennis Shoes',
 'sts2': 'Pink Tennis Shoes',
 'scs5': 'Red Sneakers',
 'smb2': 'Aqua Toon Boots',
 'smb3': 'Brown Toon Boots',
 'smb4': 'Yellow Toon Boots',
 'sfb2': 'Blue Square Boots',
 'sfb3': 'Green Hearts Boots',
 'sfb4': 'Grey Dots Boots',
 'sfb5': 'Orange Stars Boots',
 'sfb6': 'Pink Stars Boots',
 'slf1': 'Loafers',
 'smj4': 'Purple Fancy Shoes',
 'smt1': 'Motorcycle Boots',
 'sox1': 'Oxfords',
 'srb1': 'Pink Rain Boots',
 'sst1': 'Jolly Boots',
 'swb1': 'Beige Winter Boots',
 'swb2': 'Pink Winter Boots',
 'swk1': 'Work Boots',
 'scs6': 'Yellow Sneakers',
 'smb5': 'Pink Toon Boots',
 'sht2': 'Pink Hi Top Sneakers',
 'srb2': 'Red Dots Rain Boots',
 'sts3': 'Purple Tennis Shoes',
 'sts4': 'Violet Tennis Shoes',
 'sts5': 'Yellow Tennis Shoes',
 'srb3': 'Blue Rain Boots',
 'srb4': 'Yellow Rain Boots',
 'sat4': 'Black Athletic Shoes',
 'shw1': 'Pirate Shoes',
 'shw2': 'Toonosaur Feet'}
AccessoryNamePrefix = {0: 'hat unisex ',
 1: 'glasses unisex ',
 2: 'backpack unisex ',
 3: 'shoes unisex ',
 4: 'hat boy ',
 5: 'glasses boy ',
 6: 'backpack boy ',
 7: 'shoes boy ',
 8: 'hat girl ',
 9: 'glasses girl ',
 10: 'backpack girl ',
 11: 'shoes girl '}
AccessoryTypeNames = {}
for accessoryId in CatalogAccessoryItemGlobals.AccessoryTypes.keys():
    accessoryInfo = CatalogAccessoryItemGlobals.AccessoryTypes[accessoryId]
    if accessoryInfo[0] % 4 == 0:
        accessoryStyleDescription = HatStylesDescriptions
    elif accessoryInfo[0] % 4 == 1:
        accessoryStyleDescription = GlassesStylesDescriptions
    elif accessoryInfo[0] % 4 == 2:
        accessoryStyleDescription = BackpackStylesDescriptions
    else:
        accessoryStyleDescription = ShoesStylesDescriptions
    AccessoryTypeNames[accessoryId] = accessoryStyleDescription[accessoryInfo[1]]

SpecialEventMailboxStrings = {1: 'A special item from the Toon Council just for you!',
 2: "Here is your Melville's Fishing Tournament prize! Congratulations!",
 3: "Here is your Billy Budd's Fishing Tournament prize! Congratulations!",
 4: 'Here is your Acorn Acres April Invitational prize! Congratulations!',
 5: 'Here is your Acorn Acres C.U.P. Championship prize! Congratulations!',
 6: 'Here is your Gift-Giving Extravaganza prize! Congratulations!',
 7: "Here is your Top Toons New Year's Day Marathon prize! Congratulations!",
 8: 'Here is your Perfect Trolley Games Weekend prize! Congratulations!',
 9: 'Here is your Trolley Games Madness prize! Congratulations!',
 10: 'Here is your Grand Prix Weekend prize! Congratulations!',
 11: 'Here is your ToonTask Derby prize! Congratulations!',
 12: 'Here is your Save a Building Marathon prize! Congratulations!',
 13: 'Here is your Most Cogs Defeated Tournament prize! Congratulations!',
 14: 'Here is your Most V.P.s Defeated Tournament prize! Congratulations!',
 15: 'Here is your Operation: Storm Sellbot prize! Congratulations!',
 16: 'Here is your Most C.J.s Defeated Tournament prize! Congratulations!',
 17: 'Here is your Operation: Lawbots Lose prize! Congratulations!',
 18: 'Here is your Most C.F.O.s Defeated Tournament prize! Congratulations!',
 19: 'Here is your Operation: Cashbot Chaos prize! Congratulations!',
 20: 'Here is your Most C.E.O.s Defeated Tournament prize! Congratulations!',
 21: 'Here is your Operation: Besiege Bossbot prize! Congratulations!'}
RentalHours = 'Hours'
RentalOf = 'Of'
RentalCannon = 'Cannons!'
RentalGameTable = 'Game Table!'
EstateCannonGameEnd = 'The Cannon Game rental is over.'
GameTableRentalEnd = 'The Game Table rental is over.'
MessageConfirmRent = 'Begin rental? Cancel to save the rental for later'
MessageConfirmGarden = 'Are you sure you want to start a garden?'
FurnitureYourOldCloset = 'your old wardrobe'
FurnitureYourOldBank = 'your old bank'
TrunkHatGUI = 'Hats'
TrunkGlassesGUI = 'Glasses'
TrunkBackpackGUI = 'Backpacks'
TrunkShoesGUI = 'Shoes'
ChatItemQuotes = '"%s"'
FurnitureNames = {100: 'Armchair',
 105: 'Armchair',
 110: 'Chair',
 120: 'Desk Chair',
 130: 'Log Chair',
 140: 'Lobster Chair',
 145: 'Lifejacket Chair',
 150: 'Saddle Stool',
 160: 'Native Chair',
 170: 'Cupcake Chair',
 200: 'Bed',
 205: 'Bed',
 210: 'Bed',
 220: 'Bathtub Bed',
 230: 'Leaf Bed',
 240: 'Boat Bed',
 250: 'Cactus Hammock',
 260: 'Ice Cream Bed',
 270: "Olivia Erin & Cat's Bed",
 300: 'Player Piano',
 310: 'Pipe Organ',
 400: 'Fireplace',
 410: 'Fireplace',
 420: 'Round Fireplace',
 430: 'Fireplace',
 440: 'Apple Fireplace',
 450: "Erin's Fireplace",
 460: "Erin's Lit Fireplace",
 470: 'Lit Fireplace',
 480: 'Round Lit Fireplace',
 490: 'Lit Fireplace',
 491: 'Lit Fireplace',
 492: 'Apple Lit Fireplace',
 500: 'Wardrobe',
 502: '15 item Wardrobe',
 504: '20 item Wardrobe',
 506: '25 item Wardrobe',
 508: '50 item Wardrobe',
 510: 'Wardrobe',
 512: '15 item Wardrobe',
 514: '20 item Wardrobe',
 516: '25 item Wardrobe',
 518: '50 item Wardrobe',
 600: 'Short Lamp',
 610: 'Tall Lamp',
 620: 'Table Lamp',
 625: 'Table Lamp',
 630: 'Daisy Lamp',
 640: 'Daisy Lamp',
 650: 'Jellyfish Lamp',
 660: 'Jellyfish Lamp',
 670: 'Cowboy Lamp',
 680: 'Candle',
 681: 'Lit Candle',
 700: 'Cushioned Chair',
 705: 'Cushioned Chair',
 710: 'Couch',
 715: 'Couch',
 720: 'Hay Couch',
 730: 'Shortcake Couch',
 800: 'Desk',
 810: 'Log Desk',
 900: 'Umbrella Stand',
 910: 'Coat Rack',
 920: 'Trash Can',
 930: 'Red Mushroom',
 940: 'Yellow Mushroom',
 950: 'Coat Rack',
 960: 'Barrel Stand',
 970: 'Cactus Plant',
 980: 'Teepee',
 990: "Juliette's Fan",
 1000: 'Large Rug',
 1010: 'Round Rug',
 1015: 'Round Rug',
 1020: 'Small Rug',
 1030: 'Leaf Mat',
 1040: 'Presents',
 1050: 'Sled',
 1100: 'Display Cabinet',
 1110: 'Display Cabinet',
 1120: 'Tall Bookcase',
 1130: 'Low Bookcase',
 1140: 'Sundae Chest',
 1200: 'End Table',
 1210: 'Small Table',
 1215: 'Small Table',
 1220: 'Coffee Table',
 1230: 'Coffee Table',
 1240: "Snorkeler's Table",
 1250: 'Cookie Table',
 1260: 'Bedroom Table',
 1300: 'Bean Bank',
 1310: '15000 Bean Bank',
 1320: '20000 Bean Bank',
 1330: '25000 Bean Bank',
 1340: '30000 Bean Bank',
 1399: 'Telephone',
 1400: 'Cezanne Toon',
 1410: 'Flowers',
 1420: 'Modern Mickey',
 1430: 'Rembrandt Toon',
 1440: 'Toonscape',
 1441: "Whistler's Horse",
 1442: 'Toon Star',
 1443: 'Not a Pie',
 1450: 'Mickey and Minnie',
 1500: 'Radio',
 1510: 'Radio',
 1520: 'Radio',
 1530: 'Television',
 1600: 'Short Vase',
 1610: 'Tall Vase',
 1620: 'Short Vase',
 1630: 'Tall Vase',
 1640: 'Short Vase',
 1650: 'Short Vase',
 1660: 'Coral Vase',
 1661: 'Shell Vase',
 1670: 'Rose Vase',
 1680: 'Rose Watercan',
 1700: 'Popcorn Cart',
 1710: 'Ladybug',
 1720: 'Fountain',
 1725: 'Washing Machine',
 1800: 'Fish Bowl',
 1810: 'Fish Bowl',
 1900: 'Swordfish',
 1910: 'Hammerhead',
 1920: 'Hanging Horns',
 1930: 'Simple Sombrero',
 1940: 'Fancy Sombrero',
 1950: 'Dream Catcher',
 1960: 'Horseshoe',
 1970: 'Bison Portrait',
 2000: 'Candy Swing Set',
 2010: 'Cake Slide',
 3000: 'Banana Split Tub',
 4000: 'Boy Trunk',
 4010: 'Girl Trunk',
 10000: 'Short Pumpkin',
 10010: 'Tall Pumpkin',
 10020: 'Winter Tree',
 10030: 'Winter Wreath'}
ClothingArticleNames = ('Shirt',
 'Shirt',
 'Shirt',
 'Shorts',
 'Shorts',
 'Skirt',
 'Shorts')
ClothingTypeNames = {1001: 'Ghost Shirt',
 1002: 'Pumpkin Shirt',
 1112: 'Bee Shirt',
 1113: 'Pirate Shirt',
 1114: 'Super Toon Shirt',
 1115: 'Vampire Shirt',
 1116: 'Toonosaur Shirt',
 1117: 'Bee Shorts',
 1118: 'Pirate Shorts',
 1119: 'Super Toon Shorts',
 1120: 'Vampire Shorts',
 1121: 'Toonosaur Shorts',
 1122: 'Bee Shorts',
 1123: 'Pirate Shorts',
 1124: 'Super Toon Shorts',
 1125: 'Vampire Shorts',
 1126: 'Toonosaur Shorts',
 1127: 'Pirate Skirt',
 1304: "O'Shirt",
 1305: "O'Shorts",
 1306: "O'Skirt",
 1400: "Matthew's Shirt",
 1401: "Jessica's Shirt",
 1402: "Marissa's Shirt",
 1600: 'Trap Outfit',
 1601: 'Sound Outfit',
 1602: 'Lure Outfit',
 1603: 'Trap Outfit',
 1604: 'Sound Outfit',
 1605: 'Lure Outfit',
 1606: 'Trap Outfit',
 1607: 'Sound Outfit',
 1608: 'Lure Outfit',
 1723: 'Bee Shirt',
 1724: 'SuperToon Shirt',
 1734: 'Bee Shorts',
 1735: 'SuperToon Shorts',
 1739: 'Bee Skirt',
 1740: 'SuperToon Skirt',
 1743: 'Skeleton Shirt',
 1744: 'Spider Shirt',
 1745: 'Spider Shorts',
 1746: 'Skeleton Shorts',
 1747: 'Skeleton Skirt',
 1748: 'Spider Skirt',
 1749: 'Silly Mailbox Shirt',
 1750: 'Silly Trash Can Shirt',
 1751: 'Loony Labs Shirt',
 1752: 'Silly Hydrant Shirt',
 1753: 'Silly Meter Shirt',
 1754: 'Cog-Crusher Shirt',
 1755: 'Cog-Crusher Shorts',
 1756: 'Cog-Crusher Shorts',
 1757: 'Victory Party Shirt',
 1758: 'Relaxed Victory Shirt',
 1763: 'Smashed Sellbot Shirt',
 1764: 'Most V.P.s Defeated Shirt',
 1765: 'Sellbot Smasher Shirt',
 1766: 'Sellbot Smasher Shorts',
 1767: 'Sellbot Smasher Shorts',
 1768: 'Jellybean Bank Shirt',
 1769: 'Doodle Shirt',
 1770: 'Vampire Shirt',
 1771: 'Turtle Shirt',
 1772: 'Vampire Shorts',
 1773: 'Vampire Shorts',
 1774: 'Turtle Shorts',
 1775: 'Turtle Shorts',
 1776: 'Get Connected Mover & Shaker Shirt',
 1777: 'Smashed Lawbot Shirt',
 1778: 'Most C.J.s Defeated Shirt',
 1779: 'Lawbot Smasher Shirt',
 1780: 'Lawbot Smasher Shorts',
 1781: 'Lawbot Smasher Shorts',
 1782: 'Racing Shirt 3',
 1783: 'Racing Shorts 1',
 1784: 'Racing Skirt 1',
 1801: 'Batty Moon Shirt',
 1802: 'Mittens Shirt',
 1821: 'Plaid Punk Shirt'}
AccessoryArticleNames = ('Hat',
 'Glasses',
 'Backpack',
 'Shoes',
 'Hat',
 'Glasses',
 'Backpack',
 'Shoes',
 'Hat',
 'Glasses',
 'Backpack',
 'Shoes')
SurfaceNames = ('Wallpaper',
 'Moulding',
 'Flooring',
 'Wainscoting',
 'Border')
WallpaperNames = {1000: 'Parchment',
 1100: 'Milan',
 1200: 'Dover',
 1300: 'Victoria',
 1400: 'Newport',
 1500: 'Pastoral',
 1600: 'Harlequin',
 1700: 'Moon',
 1800: 'Stars',
 1900: 'Flowers',
 2000: 'Spring Garden',
 2100: 'Formal Garden',
 2200: 'Race Day',
 2300: 'Touchdown!',
 2400: 'Cloud 9',
 2500: 'Climbing Vine',
 2600: 'Springtime',
 2700: 'Kokeshi',
 2800: 'Posies',
 2900: 'Angel Fish',
 3000: 'Bubbles',
 3100: 'Bubbles',
 3200: 'Go Fish',
 3300: 'Stop Fish',
 3400: 'Sea Horse',
 3500: 'Sea Shells',
 3600: 'Underwater',
 3700: 'Boots',
 3800: 'Cactus',
 3900: 'Cowboy Hat',
 10100: 'Cats',
 10200: 'Bats',
 11000: 'Snowflakes',
 11100: 'Hollyleaf',
 11200: 'Snowman',
 12000: 'ValenToons',
 12100: 'ValenToons',
 12200: 'ValenToons',
 12300: 'ValenToons',
 13000: 'Shamrock',
 13100: 'Shamrock',
 13200: 'Rainbow',
 13300: 'Shamrock'}
FlooringNames = {1000: 'Hardwood Floor',
 1010: 'Carpet',
 1020: 'Diamond Tile',
 1030: 'Diamond Tile',
 1040: 'Grass',
 1050: 'Beige Bricks',
 1060: 'Red Bricks',
 1070: 'Square Tile',
 1080: 'Stone',
 1090: 'Boardwalk',
 1100: 'Dirt',
 1110: 'Wood Tile',
 1120: 'Tile',
 1130: 'Honeycomb',
 1140: 'Water',
 1150: 'Beach Tile',
 1160: 'Beach Tile',
 1170: 'Beach Tile',
 1180: 'Beach Tile',
 1190: 'Sand',
 10000: 'Ice Cube',
 10010: 'Igloo',
 11000: 'Shamrock',
 11010: 'Shamrock'}
MouldingNames = {1000: 'Knotty',
 1010: 'Painted',
 1020: 'Dental',
 1030: 'Flowers',
 1040: 'Flowers',
 1050: 'Ladybug',
 1060: 'ValenToons',
 1070: 'Beach',
 1080: 'Winter Lights 1',
 1085: 'Winter Lights 2',
 1090: 'Winter Lights 3',
 1100: "ValenToon's Cupid",
 1110: "ValenToon's Heart 1",
 1120: "ValenToon's Heart 2"}
WainscotingNames = {1000: 'Painted',
 1010: 'Wood Panel',
 1020: 'Wood',
 1030: 'ValenToons',
 1040: 'Underwater'}
WindowViewNames = {10: 'Large Garden',
 20: 'Wild Garden',
 30: 'Greek Garden',
 40: 'Cityscape',
 50: 'Wild West',
 60: 'Under the Sea',
 70: 'Tropical Island',
 80: 'Starry Night',
 90: 'Tiki Pool',
 100: 'Frozen Frontier',
 110: 'Farm Country',
 120: 'Native Camp',
 130: 'Main Street'}
SpecialEventNames = {1: 'Generic Award',
 2: "Melville's Fishing Tournament",
 3: "Billy Budd's Fishing Tournament",
 4: 'Acorn Acres April Invitational',
 5: 'Acorn Acres C.U.P. Championship',
 6: 'Gift-Giving Extravaganza',
 7: "Top Toons New Year's Day Marathon",
 8: 'Perfect Trolley Games Weekend',
 9: 'Trolley Games Madness',
 10: 'Grand Prix Weekend',
 11: 'ToonTask Derby',
 12: 'Save a Building Marathon',
 13: 'Most Cogs Defeated',
 14: 'Most V.P.s Defeated',
 15: 'Operation Storm Sellbot Event',
 16: 'Most C.J.s Defeated',
 17: 'Operation Lawbots Lose Event',
 18: 'Most C.F.O.s Defeated',
 19: 'Operation Cashbot Chaos Event',
 20: 'Most C.E.O.s Defeated',
 21: 'Operation Besiege Bossbot Event'}
NewCatalogNotify = 'There are new items available to order at your phone!'
NewDeliveryNotify = 'A new delivery has just arrived at your mailbox!'
CatalogNotifyFirstCatalog = 'Your first cattlelog has arrived!  You may use this to order new items for yourself or for your house.'
CatalogNotifyNewCatalog = 'Your cattlelog #%s has arrived!  You can go to your phone to order items from this cattlelog.'
CatalogNotifyNewCatalogNewDelivery = 'A new delivery has arrived at your mailbox!  Also, your cattlelog #%s has arrived!'
CatalogNotifyNewDelivery = 'A new delivery has arrived at your mailbox!'
CatalogNotifyNewCatalogOldDelivery = 'Your cattlelog #%s has arrived, and there are still items waiting in your mailbox!'
CatalogNotifyOldDelivery = 'There are still items waiting in your mailbox for you to pick up!'
CatalogNotifyInstructions = 'Click the "Go home" button on the map page in your Shticker Book, then walk up to the phone inside your house.'
CatalogNewDeliveryButton = 'New\nDelivery!'
CatalogNewCatalogButton = 'New\nCattlelog'
CatalogSaleItem = 'Sale!  '
DistributedMailboxEmpty = 'Your mailbox is empty right now.  Come back here to look for deliveries after you place an order from your phone!'
DistributedMailboxWaiting = 'Your mailbox is empty right now, but the package you ordered is on its way.  Check back later!'
DistributedMailboxReady = 'Your order has arrived!'
DistributedMailboxNotOwner = 'Sorry, this is not your mailbox.'
Clarabelle = 'Clarabelle'
MailboxExitButton = 'Close Mailbox'
MailboxAcceptButton = 'Take this item'
MailBoxDiscard = 'Discard this item'
MailboxAcceptInvite = 'Accept this invite'
MailBoxRejectInvite = 'Reject this invite'
MailBoxDiscardVerify = 'Are you sure you want to Discard %s?'
MailBoxRejectVerify = 'Are you sure you want to Reject %s?'
MailboxOneItem = 'Your mailbox contains 1 item.'
MailboxNumberOfItems = 'Your mailbox contains %s items.'
MailboxGettingItem = 'Taking %s from mailbox.'
MailboxGiftTag = 'Gift From: %s'
MailboxGiftTagAnonymous = 'Anonymous'
MailboxItemNext = 'Next\nItem'
MailboxItemPrev = 'Previous\nItem'
MailboxDiscard = 'Discard'
MailboxReject = 'Reject'
MailboxLeave = 'Keep'
CatalogCurrency = 'beans'
CatalogHangUp = 'Hang Up'
CatalogNew = 'NEW'
CatalogBackorder = 'BACKORDER'
CatalogSpecial = 'SPECIAL'
CatalogEmblem = 'COINS'
CatalogPagePrefix = 'Page'
CatalogGreeting = "Hello! Thanks for calling Clarabelle's Cattlelog. Can I help you?"
CatalogGoodbyeList = ['Bye now!',
 'Call back soon!',
 'Thanks for calling!',
 'Ok, bye now!',
 'Bye!']
CatalogHelpText1 = 'Turn the page to see items for sale.'
CatalogSeriesLabel = 'Series %s'
CatalogGiftError = 'Error'
CatalogGiftFor = 'Buy Gift for:'
CatalogGiftTo = 'To: %s'
CatalogGiftToggleOn = 'Stop Gifting'
CatalogGiftToggleOff = 'Buy Gifts'
CatalogGiftUpdating = 'Updating...'
CatalogGiftChoose = 'Choose a friend!'
CatalogPurchaseItemAvailable = 'Congratulations on your new purchase!  You can start using it right away.'
CatalogPurchaseGiftItemAvailable = 'Excellent!  %s can start using your gift right away.'
CatalogPurchaseItemOnOrder = 'Congratulations! Your purchase will be delivered to your mailbox soon.'
CatalogPurchaseGiftItemOnOrder = 'Excellent! Your gift to %s will be delivered to their mailbox.'
CatalogAnythingElse = 'Anything else I can get you today?'
CatalogPurchaseClosetFull = 'Your closet is full.  You may purchase this item anyway, but if you do you will need to delete something from your closet to make room for it when it arrives.\n\nDo you still want to purchase this item?'
CatalogPurchaseTrunkFull = 'Your trunk is full. If you purchase this item, you\xe2\x80\x99ll need to delete another item from your trunk to make more room.\n\nDo you still want to purchase this item?'
CatalogAcceptClosetFull = 'Your closet is full.  You must go inside and delete something from your closet to make room for this item before you can take it out of your mailbox.'
CatalogAcceptTrunkFull = 'Your trunk is full.  You must delete something from your trunk before you can take this item out of your mailbox.'
CatalogAcceptShirt = 'You are now wearing your new hat.  The hat you were wearing before has been moved to your trunk.'
CatalogAcceptShorts = 'You are now wearing your new shorts.  What you were wearing before has been moved to your closet.'
CatalogAcceptSkirt = 'You are now wearing your new skirt.  What you were wearing before has been moved to your closet.'
CatalogAcceptHat = 'You are now wearing your new hat.  The hat you were wearing before has been moved to your trunk.'
CatalogAcceptGlasses = 'You are now wearing your new glasses.  The glasses you were wearing before have been moved to your trunk.'
CatalogAcceptBackpack = 'You are now wearing your new backpack.  The backpack you were wearing before has been moved to your trunk.'
CatalogAcceptShoes = 'You are now wearing your new shoes.  The shoes you were wearing before have been moved to your trunk.'
CatalogAcceptPole = "You're now ready to go catch some bigger fish with your new pole!"
CatalogAcceptPoleUnneeded = 'You already have a better pole than this one!'
CatalogAcceptChat = 'You now have a new SpeedChat!'
CatalogAcceptEmote = 'You now have a new Emotion!'
CatalogAcceptBeans = 'You received some jelly beans!'
CatalogAcceptRATBeans = 'Your Toon recruit reward has arrived!'
CatalogAcceptPartyRefund = "Your party was never started. Here's your refund!"
CatalogAcceptNametag = 'Your new nametag has arrived!'
CatalogAcceptGarden = 'Your garden supplies have arrived!'
CatalogAcceptPet = 'You now have a new Pet Trick!'
CatalogPurchaseHouseFull = 'Your house is full.  You may purchase this item anyway, but if you do you will need to delete something from your house to make room for it when it arrives.\n\nDo you still want to purchase this item?'
CatalogAcceptHouseFull = 'Your house is full. You can not accept this item until you free up some room. Would you like to discard this item now?'
CatalogAcceptInAttic = 'Your new item is now in your attic.  You can put it in your house by going inside and clicking on the "Move Furniture" button.'
CatalogAcceptInAtticP = 'Your new items are now in your attic.  You can put them in your house by going inside and clicking on the "Move Furniture" button.'
CatalogPurchaseMailboxFull = "Your mailbox is full!  You can't purchase this item until you take some items out of your mailbox to make room."
CatalogPurchaseGiftMailboxFull = "%s's mailbox is full!  You can't purchase this item."
CatalogPurchaseOnOrderListFull = "You have too many items currently on order.  You can't order any more items until some of the ones you have already ordered arrive."
CatalogPurchaseGiftOnOrderListFull = '%s has too many items currently on order.'
CatalogPurchaseGeneralError = 'The item could not be purchased because of some internal game error: error code %s.'
CatalogPurchaseGiftGeneralError = 'The item could not be gifted to %(friend)s because of some internal game error: error code %(error)s.'
CatalogPurchaseGiftNotAGift = 'This item could not be sent to %s because it would be an unfair advantage.'
CatalogPurchaseGiftWillNotFit = "This item could not be sent to %s because it doesn't fit them."
CatalogPurchaseGiftLimitReached = "This item could not be sent to %s because they already have it."
CatalogPurchaseGiftNotEnoughMoney = "This item could not be sent to %s because you can't afford it."
CatalogPurchaseGiftTooFast = "This item could not be sent to %s because you are sending gifts too fast."
CatalogAcceptGeneralError = 'The item could not be removed from your mailbox because of some internal game error: error code %s.'
CatalogAcceptRoomError = "You don't have any place to put this. You'll have to get rid of something."
CatalogAcceptLimitError = "You already have as many of these as you can handle. You'll have to get rid of something."
CatalogAcceptFitError = "This won't fit you!"
CatalogAcceptInvalidError = 'This item has gone out of style!'
CatalogAcceptClosetError = 'You already have a bigger closet!'
MailboxOverflowButtonDicard = 'Discard'
MailboxOverflowButtonLeave = 'Leave'
HDMoveFurnitureButton = 'Move\nFurniture'
HDStopMoveFurnitureButton = 'Done\nMoving'
HDAtticPickerLabel = 'In the attic'
HDInRoomPickerLabel = 'In the room'
HDInTrashPickerLabel = 'In the trash'
HDDeletePickerLabel = 'Delete?'
HDInAtticLabel = 'Attic'
HDInRoomLabel = 'Room'
HDInTrashLabel = 'Trash'
HDToAtticLabel = 'Send\nto attic'
HDMoveLabel = 'Move'
HDRotateCWLabel = 'Rotate Right'
HDRotateCCWLabel = 'Rotate Left'
HDReturnVerify = 'Return this item to the attic?'
HDReturnFromTrashVerify = 'Return this item to the attic from the trash?'
HDDeleteItem = 'Click OK to send this item to the trash, or Cancel to keep it.'
HDNonDeletableItem = "You can't delete items of this type!"
HDNonDeletableBank = "You can't delete your bank!"
HDNonDeletableCloset = "You can't delete your wardrobe!"
HDNonDeletablePhone = "You can't delete your phone!"
HDNonDeletableTrunk = "You can't delete your trunk!"
HDNonDeletableNotOwner = "You can't delete %s's things!"
HDHouseFull = 'Your house is full.  You have to delete something else from your house or attic before you can return this item from the trash.'
HDHelpDict = {'DoneMoving': 'Finish room decorating.',
 'Attic': 'Show list of items in attic. The attic stores items that are not in your room.',
 'Room': 'Show list of items in room. Useful for finding lost items.',
 'Trash': 'Show items in trash. Oldest items are deleted after a while or when trash overflows.',
 'ZoomIn': 'Get a closer view of room.',
 'ZoomOut': 'Get a farther view of room.',
 'SendToAttic': 'Send the current furniture item to attic for storage.',
 'RotateLeft': 'Turn left.',
 'RotateRight': 'Turn right.',
 'DeleteEnter': 'Change to delete mode.',
 'DeleteExit': 'Exit delete mode.',
 'FurnitureItemPanelDelete': 'Send %s to trash.',
 'FurnitureItemPanelAttic': 'Place %s in room.',
 'FurnitureItemPanelRoom': 'Return %s to attic.',
 'FurnitureItemPanelTrash': 'Return %s to attic.'}
MessagePickerTitle = 'You have too many phrases. In order to purchase\n"%s"\n you must choose one to remove:'
MessagePickerCancel = lCancel
MessageConfirmDelete = 'Are you sure you want to remove "%s" from your SpeedChat menu?'
CatalogBuyText = 'Buy'
CatalogRentText = 'Rent'
CatalogGiftText = 'Gift'
CatalogOnOrderText = 'On Order'
CatalogPurchasedText = 'Already\nPurchased'
CatalogGiftedText = 'Gifted\nTo You'
CatalogPurchasedGiftText = 'Already\nOwned'
CatalogMailboxFull = 'No Room'
CatalogNotAGift = 'Not a Gift'
CatalogNoFit = "Doesn't\nFit"
CatalogSndOnText = 'Snd On'
CatalogSndOffText = 'Snd Off'
CatalogPurchasedMaxText = 'Already\nPurchased Max'
CatalogVerifyPurchase = 'Purchase %(item)s for %(price)s Jellybeans?'
CatalogVerifyPurchaseBeanSilverGold = 'Purchase %(item)s for %(price)s Jellybeans, %(silver)s silver coins and %(gold)s gold coins?'
CatalogVerifyPurchaseBeanGold = 'Purchase %(item)s for %(price)s Jellybeans and %(gold)s gold coins?'
CatalogVerifyPurchaseBeanSilver = 'Purchase %(item)s for %(price)s Jellybeans and %(silver)s silver coins?'
CatalogVerifyPurchaseSilverGold = 'Purchase %(item)s for %(silver)s silver coins and %(gold)s gold coins?'
CatalogVerifyPurchaseSilver = 'Purchase %(item)s for %(silver)s silver coins?'
CatalogVerifyPurchaseGold = 'Purchase %(item)s for %(gold)s gold coins?'
CatalogVerifyRent = 'Rent %(item)s for %(price)s Jellybeans?'
CatalogVerifyGift = 'Purchase %(item)s for %(price)s Jellybeans as a gift for %(friend)s?'
CatalogOnlyOnePurchase = 'You may only have one of these items at a time.  If you purchase this one, it will replace %(old)s.\n\nAre you sure you want to purchase %(item)s for %(price)s Jellybeans?'
CatalogExitButtonText = 'Hang Up'
CatalogPastButtonText = 'To Past Items'
NPCToonNames = {999: 'Toon Tailor',
 1000: lToonHQ,
 20001: Flippy,
 2001: Flippy,
 2002: 'Banker Bob',
 2003: 'Professor Pete',
 2004: 'Tammy the Tailor',
 2005: 'Librarian Larry',
 2006: 'Crazy Clark',
 2011: 'Clara Snowskirt',
 2007: 'HQ Harry',
 2008: 'Ranger Randy',
 2009: 'Mischievous Midknight',
 2010: 'Talkative Tom',
 2012: 'Fuzzy Freddy',
 2013: 'Poppy',
 2014: 'Peppy',
 2015: 'Pappy',
 2016: 'Pumpkin',
 2017: 'Polly',
 2018: 'Doctor Surlee',
 2019: 'Doctor Dimm',
 2020: 'Professor Prepostera',
 2021: 'Painter Eddy',
 2022: 'Cheesy Charlie',
 2023: 'Natalie',
 2024: 'Kate Kakery',
 2025: 'Chef Batter',
 2026: 'Tom Torrent',
 2027: 'Mindy Monsoon',
 2101: 'Dentist Daniel',
 2102: 'Sheriff Sherry',
 2103: 'Sneezy Kitty',
 2104: lHQOfficerM,
 2105: lHQOfficerM,
 2106: lHQOfficerF,
 2107: lHQOfficerF,
 2108: 'Canary Coalmine',
 2109: 'Sir Babbles A Lot',
 2110: 'Bill Board',
 2111: 'Dancing Diego',
 2112: 'Dr. Tom',
 2113: 'Rollo The Amazing',
 2114: 'Roz Berry',
 2115: 'Patty Papercut',
 2116: 'Bruiser McDougal',
 2117: 'Ma Putrid',
 2118: 'Jesse Jester',
 2119: 'Honey Haha',
 2120: 'Professor Binky',
 2121: 'Madam Chuckle',
 2122: 'Harry Ape',
 2123: 'Spamonia Biggles',
 2124: 'T.P. Rolle',
 2125: 'Lazy Hal',
 2126: 'Professor Guffaw',
 2127: 'Woody Nickel',
 2128: 'Loony Louis',
 2129: 'Frank Furter',
 2130: 'Joy Buzzer',
 2131: 'Feather Duster',
 2132: 'Daffy Don',
 2133: 'Dr. Euphoric',
 2134: 'Silent Simone',
 2135: 'Mary',
 2136: 'Sal Snicker',
 2137: 'Happy Heikyung',
 2138: 'Muldoon',
 2139: 'Dan Dribbles',
 2140: 'Billy Bonka',
 2201: 'Postmaster Pete',
 2202: 'Shirley U. Jest',
 2203: lHQOfficerM,
 2204: lHQOfficerM,
 2205: lHQOfficerF,
 2206: lHQOfficerF,
 2207: 'Will Wiseacre',
 2208: 'Sticky Lou',
 2209: 'Charlie Chortle',
 2210: 'Tee Hee',
 2211: 'Sally Spittake',
 2212: 'Weird Warren',
 2213: 'Lucy Tires',
 2214: 'Sam Stain',
 2215: 'Sid Seltzer',
 2216: 'Nona Seeya',
 2217: 'Sharky Jones',
 2218: 'Fanny Pages',
 2219: 'Chef Knucklehead',
 2220: 'Rick Rockhead',
 2221: 'Clovinia Cling',
 2222: 'Shorty Fuse',
 2223: 'Sasha Sidesplitter',
 2224: 'Smokey Joe',
 2225: 'Droopy',
 2301: 'Dr. Pulyurleg',
 2302: 'Professor Wiggle',
 2303: 'Nurse Nancy',
 2304: lHQOfficerM,
 2305: lHQOfficerM,
 2306: lHQOfficerF,
 2307: lHQOfficerF,
 2308: 'Nancy Gas',
 2309: 'Big Bruce',
 2311: 'Franz Neckvein',
 2312: 'Dr. Sensitive',
 2313: 'Lucy Shirtspot',
 2314: 'Ned Slinger',
 2315: 'Chewy Morsel',
 2316: 'Cindy Sprinkles',
 2318: 'Tony Maroni',
 2319: 'Zippy',
 2320: 'Crunchy Alfredo',
 2321: 'Punchy',
 2401: 'Hal Haggle',
 2402: 'Bo Bonkers',
 2403: 'Teddy Troop',
 2404: 'Patti Prank', 
 2405: 'Coco Creme',
 2406: 'Dr. Patrick',
 2407: 'Yancy Gas',
 2408: 'Moka Duck',
 2409: lHQOfficerM,
 2410: lHQOfficerM,
 2411: lHQOfficerF,
 2412: lHQOfficerF,
 2413: 'Tony',
 2414: 'Yellow',
 2415: 'Astro',
 2416: 'Fisherman Grins',
 1001: 'Wacky Will',
 1002: 'Bill Jobs',
 1003: lHQOfficerM,
 1004: lHQOfficerF,
 1005: lHQOfficerM,
 1006: lHQOfficerF,
 1007: 'Longjohn Leroy',
 1008: 'Furball',
 1009: 'Barky',
 1010: 'Purr',
 1011: 'Bloop',
 1012: 'Pickles',
 1013: 'Patty',
 1101: 'Billy Budd',
 1102: 'Captain Carl',
 1103: 'Fishy Frank',
 1104: 'Doctor Squall',
 1105: 'Admiral Hook',
 1106: 'Mrs. Starch',
 1107: 'Cal Estenicks',
 1108: lHQOfficerM,
 1109: lHQOfficerF,
 1110: lHQOfficerM,
 1111: lHQOfficerF,
 1112: 'Gary Glubglub',
 1113: 'Lisa Luff',
 1114: 'Charlie Chum',
 1115: 'Sheila Squid, Atty',
 1116: 'Barnacle Bessie',
 1117: 'Captain Yucks',
 1118: 'Choppy McDougal',
 1121: 'Linda Landlubber',
 1122: 'Salty Stan',
 1123: 'Electra Eel',
 1124: 'Flappy Docksplinter',
 1125: 'Eileen Overboard',
 1126: 'Bonkers Barney',
 1201: 'Barnacle Barbara',
 1202: 'Art',
 1203: 'Ahab',
 1204: 'Rocky Shores',
 1205: lHQOfficerM,
 1206: lHQOfficerF,
 1207: lHQOfficerM,
 1208: lHQOfficerF,
 1209: 'Professor Plank',
 1210: 'Gang Wei',
 1211: 'Wynn Bag',
 1212: 'Toby Tonguestinger',
 1213: 'Dante Dolphin',
 1214: 'Gusty Kate',
 1215: 'Dinah Down',
 1216: 'Rod Reel',
 1217: 'CC Weed',
 1218: 'Pacific Tim',
 1219: 'Brian Beachead',
 1220: 'Carla Canal',
 1221: 'Blisters McKee',
 1222: 'Shep Ahoy',
 1223: 'Sid Squid',
 1224: 'Emily Eel',
 1225: 'Bonzo Bilgepump',
 1226: 'Heave Ho',
 1227: 'Coral Reef',
 1228: 'Reed',
 1301: 'Alice',
 1302: 'Melville',
 1303: 'Claggart',
 1304: 'Svetlana',
 1305: lHQOfficerM,
 1306: lHQOfficerF,
 1307: lHQOfficerM,
 1308: lHQOfficerF,
 1309: 'Seafoam',
 1310: 'Ted Tackle',
 1311: 'Topsy Turvey',
 1312: 'Ethan Keel',
 1313: 'William Wake',
 1314: 'Rusty Ralph',
 1315: 'Doctor Drift',
 1316: 'Wilma Wobble',
 1317: 'Paula Pylon',
 1318: 'Dinghy Dan',
 1319: 'Davey Drydock',
 1320: 'Ted Calm',
 1321: 'Dinah Docker',
 1322: 'Whoopie Cushion',
 1323: 'Stinky Ned',
 1324: 'Pearl Diver',
 1325: 'Ned Setter',
 1326: 'Felicia Chips',
 1327: 'Cindy Splat',
 1328: 'Fred Flounder',
 1329: 'Shelly Seaweed',
 1330: 'Porter Hole',
 1331: 'Rudy Rudder',
 1332: 'Shane',
 3001: 'Betty Freezes',
 3002: lHQOfficerM,
 3003: lHQOfficerF,
 3004: lHQOfficerM,
 3005: lHQOfficerM,
 3006: 'Loud Lenny',
 3007: 'Peaceful Penny',
 3008: 'Warren Bundles',
 3009: 'Frizzy',
 3010: 'Skip',
 3011: 'Dip',
 3012: 'Kipp',
 3013: 'Pete',
 3014: 'Penny',
 3101: 'Mr. Cow',
 3102: 'Auntie Freeze',
 3103: 'Fred',
 3104: 'Bonnie',
 3105: 'Frosty Freddy',
 3106: 'Gus Gooseburger',
 3107: 'Patty Passport',
 3108: 'Toboggan Ted',
 3109: 'Kate',
 3110: 'Chicken Boy',
 3111: 'Snooty Sinjin',
 3112: 'Lil Oldman',
 3113: 'Hysterical Harry',
 3114: 'Henry the Hazard',
 3115: lHQOfficerM,
 3116: lHQOfficerF,
 3117: lHQOfficerM,
 3118: lHQOfficerM,
 3119: 'Creepy Carl',
 3120: 'Mike Mittens',
 3121: 'Joe Shockit',
 3122: 'Lucy Luge',
 3123: 'Frank Lloyd Ice',
 3124: 'Lance Iceberg',
 3125: 'Colonel Crunchmouth',
 3126: 'Colestra Awl',
 3127: 'Ifalla Yufalla',
 3128: 'Sticky George',
 3129: 'Baker Bridget',
 3130: 'Sandy',
 3131: 'Lazy Lorenzo',
 3132: 'Ashy',
 3133: 'Dr. Friezeframe',
 3134: 'Lounge Lassard',
 3135: 'Soggy Nell',
 3136: 'Happy Sue',
 3137: 'Mr. Freeze',
 3138: 'Chef Bumblesoup',
 3139: 'Granny Icestockings',
 3140: 'Lucille',
 3201: 'Aunt Arctic',
 3202: 'Shakey',
 3203: 'Walt',
 3204: 'Dr. Ivanna Cee',
 3205: 'Bumpy Noggin',
 3206: 'Vidalia VaVoom',
 3207: 'Dr. Mumbleface',
 3208: 'Grumpy Phil',
 3209: 'Giggles McGhee',
 3210: 'Simian Sam',
 3211: 'Fanny Freezes',
 3212: 'Frosty Fred',
 3213: lHQOfficerM,
 3214: lHQOfficerF,
 3215: lHQOfficerM,
 3216: lHQOfficerM,
 3217: 'Sweaty Pete',
 3218: 'Blue Lou',
 3219: 'Tom Tandemfrost',
 3220: 'Mr. Sneeze',
 3221: 'Nelly Snow',
 3222: 'Mindy Windburn',
 3223: 'Chappy',
 3224: 'Freida Frostbite',
 3225: 'Blake Ice',
 3226: 'Santa Paws',
 3227: 'Solar Ray',
 3228: 'Wynne Chill',
 3229: 'Hernia Belt',
 3230: 'Balding Benjy',
 3231: 'Choppy',
 3232: 'Albert Earstein',
 3301: 'Paisley Patches',
 3302: 'Bjorn Bord',
 3303: 'Dr. Peepers',
 3304: 'Eddie the Yeti',
 3305: 'Mack Ramay',
 3306: 'Paula Behr',
 3307: 'Fredrica',
 3308: 'Fred Frump',
 3309: 'Bootsy',
 3310: 'Professor Flake',
 3311: 'Connie Ferris',
 3312: 'March Harry',
 3313: lHQOfficerM,
 3314: lHQOfficerF,
 3315: lHQOfficerM,
 3316: lHQOfficerF,
 3317: 'Kissy Krissy',
 3318: 'Johnny Cashmere',
 3319: 'Sam Stetson',
 3320: 'Fizzy Lizzy',
 3321: 'Pickaxe Paul',
 3322: 'Flue Lou',
 3323: 'Dallas Borealis',
 3324: 'Snaggletooth Stu',
 3325: 'Groovy Garland',
 3326: 'Blanche',
 3327: 'Chuck Roast',
 3328: 'Shady Sadie',
 3329: 'Treading Ed',
 4001: 'Molly Molloy',
 4002: lHQOfficerM,
 4003: lHQOfficerF,
 4004: lHQOfficerF,
 4005: lHQOfficerF,
 4006: 'Doe',
 4007: 'Ray',
 4008: 'Tailor Harmony',
 4009: 'Fanny',
 4010: 'Cranky Chris',
 4011: 'Neil Legstrong',
 4012: 'Westin Girl',
 4013: 'Preston',
 4014: 'Penelope',
 4101: 'Tom',
 4102: 'Fifi',
 4103: 'Dr. Fret',
 4104: lHQOfficerM,
 4105: lHQOfficerF,
 4106: lHQOfficerF,
 4107: lHQOfficerF,
 4108: 'Cleff',
 4109: 'Carlos',
 4110: 'Metra Gnome',
 4111: 'Tom Hum',
 4112: 'Fa',
 4113: 'Madam Manners',
 4114: 'Offkey Eric',
 4115: 'Barbara Seville',
 4116: 'Piccolo',
 4117: 'Mandy Lynn',
 4118: 'Attendant Abe',
 4119: 'Moe Zart',
 4120: 'Viola Padding',
 4121: 'Gee Minor',
 4122: 'Minty Bass',
 4123: 'Lightning Ted',
 4124: 'Riff Raff',
 4125: 'Melody Wavers',
 4126: 'Mel Canto',
 4127: 'Happy Feet',
 4128: 'Luciano Scoop',
 4129: 'Tootie Twostep',
 4130: 'Metal Mike',
 4131: 'Abraham Armoire',
 4132: 'Lowdown Sally',
 4133: 'Scott Poplin',
 4134: 'Disco Dave',
 4135: 'Sluggo Songbird',
 4136: 'Patty Pause',
 4137: 'Tony Deff',
 4138: 'Cliff Cleff',
 4139: 'Harmony Swell',
 4140: 'Clumsy Ned',
 4141: 'Lousy Jed',
 4201: 'Tina',
 4202: 'Barry',
 4203: 'Lumber Jack',
 4204: lHQOfficerM,
 4205: lHQOfficerF,
 4206: lHQOfficerF,
 4207: lHQOfficerF,
 4208: 'Hedy',
 4209: 'Corny Canter',
 4211: 'Carl Concerto',
 4212: 'Detective Dirge',
 4213: 'Fran Foley',
 4214: 'Tina Toehooks',
 4215: 'Tim Tailgater',
 4216: 'Gummy Whistle',
 4217: 'Handsome Anton',
 4218: 'Wilma Wind',
 4219: 'Sid Sonata',
 4220: 'Curtis Finger',
 4221: 'Moe Madrigal',
 4222: 'John Doe',
 4223: 'Penny Prompter',
 4224: 'Jungle Jim',
 4225: 'Holly Hiss',
 4226: 'Thelma Throatreacher',
 4227: 'Quiet Francesca',
 4228: 'August Winds',
 4229: 'June Loon',
 4230: 'Julius Wheezer',
 4231: 'Steffi Squeezebox',
 4232: 'Hedly Hymn',
 4233: 'Charlie Carp',
 4234: 'Leed Guitar',
 4235: 'Larry',
 4301: 'Yuki',
 4302: 'Anna',
 4303: 'Leo',
 4304: lHQOfficerM,
 4305: lHQOfficerF,
 4306: lHQOfficerF,
 4307: lHQOfficerF,
 4308: 'Tabitha',
 4309: 'Marshall',
 4310: 'Martha Mopp',
 4311: 'Sea Shanty',
 4312: 'Moe Saj',
 4313: 'Dumb Dolph',
 4314: 'Dana Dander',
 4315: 'Karen Clockwork',
 4316: 'Tim Tango',
 4317: 'Stubby Toe',
 4318: 'Bob Marlin',
 4319: 'Rinky Dink',
 4320: 'Cammy Coda',
 4321: 'Luke Lute',
 4322: 'Randy Rythm',
 4323: 'Hanna Hogg',
 4324: 'Ellie',
 4325: 'Banker Bran',
 4326: 'Fran Fret',
 4327: 'Flim Flam',
 4328: 'Wagner',
 4329: 'Telly Prompter',
 4330: 'Quentin',
 4331: 'Mellow Costello',
 4332: 'Ziggy',
 4333: 'Harry',
 4334: 'Fast Freddie',
 4335: 'Walden',
 5001: lHQOfficerM,
 5002: lHQOfficerM,
 5003: lHQOfficerF,
 5004: lHQOfficerF,
 5005: 'Pretty Peaches',
 5006: 'Hearty Herb',
 5007: 'Bonnie Blossom',
 5008: 'Flora',
 5009: 'Bo Tanny',
 5010: 'Tom A. Dough',
 5011: 'Doug Wood',
 5012: 'Pierce',
 5013: 'Peggy',
 5101: 'Artie',
 5102: 'Susan',
 5103: 'Bud',
 5104: 'Flutterby',
 5105: 'Jack',
 5106: 'Barber Bjorn',
 5107: 'Postman Felipe',
 5108: 'Innkeeper Janet',
 5109: lHQOfficerM,
 5110: lHQOfficerM,
 5111: lHQOfficerF,
 5112: lHQOfficerF,
 5113: 'Dr. Spud',
 5114: 'Wilt',
 5115: 'Honey Dew',
 5116: 'Vegetable Vern',
 5117: 'Petal',
 5118: 'Pop Corn',
 5119: 'Barry Medly',
 5120: 'Gopher',
 5121: 'Paula Peapod',
 5122: 'Leif Pyle',
 5123: 'Diane Vine',
 5124: 'Soggy Bottom',
 5125: 'Sanjay Splash',
 5126: 'Madam Mum',
 5127: 'Polly Pollen',
 5128: 'Shoshanna Sap',
 5129: 'Silly Sally',
 5201: 'Jake',
 5202: 'Cynthia',
 5203: 'Lisa',
 5204: 'Bert',
 5205: 'Dan D. Lion',
 5206: 'Vine Green',
 5207: 'Sofie Squirt',
 5208: 'Samantha Spade',
 5209: lHQOfficerM,
 5210: lHQOfficerM,
 5211: lHQOfficerF,
 5212: lHQOfficerF,
 5213: 'Big Galoot',
 5214: 'Itchie Bumps',
 5215: 'Tammy Tuber',
 5216: 'Stinky Jim',
 5217: 'Greg Greenethumb',
 5218: 'Rocky Raspberry',
 5219: 'Lars Bicep',
 5220: 'Lacy Underalls',
 5221: 'Pink Flamingo',
 5222: 'Whiny Wilma',
 5223: 'Wet Will',
 5224: 'Uncle Bumpkin',
 5225: 'Pamela Puddle',
 5226: 'Pete Moss',
 5227: 'Begonia Biddlesmore',
 5228: 'Digger Mudhands',
 5229: 'Lily Pea Choo',
 5301: lHQOfficerM,
 5302: lHQOfficerM,
 5303: lHQOfficerM,
 5304: lHQOfficerM,
 5305: 'Crystal',
 5306: 'S. Cargo',
 5307: 'Fun Gus',
 5308: 'Naggy Nell',
 5309: 'Ro Maine',
 5310: 'Timothy',
 5311: 'Judge McIntosh',
 5312: 'Eugene',
 5313: 'Coach Zucchini',
 5314: 'Aunt Hill',
 5315: 'Uncle Mud',
 5316: 'Uncle Spud',
 5317: 'Detective Lima',
 5318: 'Caesar',
 5319: 'Rose',
 5320: 'April',
 5321: 'Professor Ivy',
 5322: 'Rose',
 6000: 'Melville',
 8001: 'Graham Pree',
 8002: 'Ivona Race',
 8003: 'Anita Winn',
 8004: 'Phil Errup',
 9001: "Snoozin' Susan",
 9002: 'Sleeping Tom',
 9003: 'Drowsy Dennis',
 9004: lHQOfficerF,
 9005: lHQOfficerF,
 9006: lHQOfficerM,
 9007: lHQOfficerM,
 9008: 'Jittery Jill',
 9009: 'Pleasant Phil',
 9010: 'Worn Out Waylon',
 9011: 'Freud',
 9012: 'Sarah Snuze',
 9013: 'Kat Knap',
 9014: 'R. V. Winkle',
 9015: 'Pebbles',
 9016: 'Pearl',
 9101: 'Ed',
 9102: 'Big Mama',
 9103: 'P.J.',
 9104: 'Sweet Slumber',
 9105: 'Professor Yawn',
 9106: 'Max',
 9107: 'Snuggles',
 9108: 'Winky Wilbur',
 9109: 'Dreamy Daphne',
 9110: 'Kathy Nip',
 9111: 'Powers Erge',
 9112: 'Lullaby Lou',
 9113: 'Jacques Clock',
 9114: 'Smudgy Mascara',
 9115: 'Babyface MacDougal',
 9116: 'Dances with Sheep',
 9117: 'Afta Hours',
 9118: 'Starry Knight',
 9119: 'Rocco',
 9120: 'Sarah Slumber',
 9121: 'Serena Shortsheeter',
 9122: 'Puffy Ayes',
 9123: 'Teddy Blair',
 9124: 'Nina Nitelight',
 9125: 'Dr. Bleary',
 9126: 'Wyda Wake',
 9127: 'Tabby Tucker',
 9128: "Hardy O'Toole",
 9129: 'Bertha Bedhog',
 9130: 'Charlie Chamberpot',
 9131: 'Susan Siesta',
 9132: lHQOfficerF,
 9133: lHQOfficerF,
 9134: lHQOfficerF,
 9135: lHQOfficerF,
 9136: 'Swifty Taylor',
 9201: 'Bernie',
 9202: 'Orville',
 9203: 'Nat',
 9204: 'Claire de Loon',
 9205: 'Zen Glen',
 9206: 'Skinny Ginny',
 9207: 'Jane Drain',
 9208: 'Drowsy Dave',
 9209: 'Dr. Floss',
 9210: 'Master Mike',
 9211: 'Dawn',
 9212: 'Moonbeam',
 9213: 'Rooster Rick',
 9214: 'Dr. Blinky',
 9215: 'Rip',
 9216: 'Cat',
 9217: 'Lawful Linda',
 9218: 'Waltzing Matilda',
 9219: 'The Countess',
 9220: 'Grumpy Gordon',
 9221: 'Zari',
 9222: 'Cowboy George',
 9223: 'Mark the Lark',
 9224: 'Sandy Sandman',
 9225: 'Fidgety Bridget',
 9226: 'William Teller',
 9227: 'Bed Head Ted',
 9228: 'Whispering Willow',
 9229: 'Rose Petals',
 9230: 'Tex',
 9231: 'Harry Hammock',
 9232: 'Honey Moon',
 9233: lHQOfficerM,
 9234: lHQOfficerM,
 9235: lHQOfficerM,
 9236: lHQOfficerM,
 9237: 'Kim Jung',
 9301: 'Midnight',
 9302: 'Dazy Day',
 9303: "Tim S. Leap",
 9304: 'Doc Bean',
 9305: 'Koo Koo',
 9306: 'Misty Clowder',
 9307: 'Skippy',
 9308: 'Fluffy',
 9309: 'Dancin Darrin',
 9310: 'Sally',
 9312: 'Sparky',
 9313: 'Rev',
 9314: 'Scala Ton',
 9315: 'Ole Flim',
 9316: 'Baker Knead',
 9317: 'Morton',
 9318: lHQOfficerM,
 9319: lHQOfficerM,
 9320: lHQOfficerF,
 9321: lHQOfficerF,
 9322: 'Dan Tyred',
 9323: 'Sleepy Sid',
 9324: 'Fisherman Slumber',

 14030: 'Tailor Spurs',

 21002: 'Fisherman Fernando',
 21003: 'Tailor Bolt',
 21004: 'Durta',
 21005: 'Marla',
 21006: 'Digg',
 21007: 'Plann',
 21008: 'Clerk Lilly',
 21009: 'Clerk Billy',
 21010: 'Clerk Growl',
 21011: 'Clerk Fluffy',
 21012: 'Clerk Rover',
 21015: 'Doc Brown',
 21101: 'Dentist Daniel',
 21102: 'Sheriff Sherry',
 21103: 'Tiger Mighty', 
 21104: lHQOfficerM,
 21105: lHQOfficerM,
 21106: lHQOfficerF,
 21107: lHQOfficerF,
 21108: 'Master',
 21109: 'Sir Babbles A Lot',
 21110: 'Bill Board',
 21111: 'Dancing Diego',
 21112: 'Dr. Tom',
 21113: 'Rollo The Amazing',
 21114: 'Roz Berry',
 21115: 'Patty Papercut',
 21116: 'Bruiser McDougal',
 21117: 'Ma Putrid',
 21118: 'Jesse Jester',
 21119: 'Honey Haha',
 21120: 'Professor Binky',
 21121: 'Madam Chuckle',
 21122: 'Magic',
 14123: 'Spamonia Biggles',
 21124: 'T.P. Rolle',
 21125: 'Lazy Hal',
 21126: 'Professor Guffaw',
 21127: 'Woody Nickel',
 21128: 'Loony Louis',
 21129: 'Frank Furter',
 21130: 'Joy Buzzer',
 21131: 'Feather Duster',
 21132: 'Daffy Don',
 21133: 'Dr. Euphoric',
 21134: 'Silent Simone',
 21135: 'Mary',
 21136: 'Sal Snicker',
 21137: 'Happy Heikyung',
 21138: 'Muldoon',
 21139: 'Dan Dribbles',
 21140: 'Fisherman Billy',
 21141: 'Clerk Whale',
 21142: 'Clerk Barrow',

 14201: 'Ed',
 14202: 'Dottie Draw',
 14203: lHQOfficerM,
 14204: lHQOfficerM,
 14205: lHQOfficerF,
 14206: lHQOfficerF,
 14207: 'Sammy Steps',
 14208: 'Jig Saw',
 14209: 'Molly Miller',
 14210: 'Cole Crane',
 14211: 'Rusty',
 14212: 'Hattie',
 14213: 'Lou Ash',
 14214: 'Earl Enge',
 14215: 'Rick Mason',
 14216: 'Cam Cutter', 
 14217: 'Bud Bolter',
 14218: 'Juleo',
 14219: 'Bulldog',
 14220: 'Frank',
 14221: 'Don Drill',
 14222: 'Susan Slab',
 14223: 'Jo Teller',
 14224: 'Mocha Duck',
 14225: 'Painter Vincent',
 14226: 'Chef Cobble',
 14227: 'Pebbles',
 14228: 'Wally',
 14229: 'Sam Doore',
 14230: 'Bill Miter',
 14231: 'Pam Pane',
 14232: 'Fisherman Plann',
 14301: 'Dr. Pulyurleg',
 14302: 'Mister BD McSwirl',
 14303: 'Nurse Nancy',
 14304: lHQOfficerM,
 14305: lHQOfficerM,
 14306: lHQOfficerF,
 14307: lHQOfficerF,
 14308: 'Nancy Gas',
 14309: 'Authentic',
 14311: 'Franz Neckvein',
 14312: 'Dr. Sensitive',
 14313: 'Lucy Shirtspot',
 14314: 'Ned Slinger',
 14315: 'Ozzie',
 14316: 'Brick Ward',
 14318: 'Tony Maroni',
 14319: 'Zippy',
 14320: 'Crunchy Alfredo',
 21321: 'Fisherman Punchy',

 7001: 'N. Prisoned',
 7002: 'R.E. Leaseme',
 7003: 'Lemmy Owte',
 7004: 'T. Rapped',
 7005: 'Little Helphere',
 7006: 'Gimmy Ahand',
 7007: 'Dewin Tymme',
 7008: 'Ima Cagedtoon',
 7009: 'Jimmy Thelock',
 7010: 'Jaymo',
 7011: 'Captain Bligh',
 7012: 'Phil Bettur',
 7013: 'Emma Phatic',
 7014: 'GiggleMesh',
 7015: 'Anne Ville',
 7016: 'Bud Erfingerz',
 7017: 'J.S. Bark',
 7018: 'Bea Sharpe',
 7019: 'Otto Toon',
 7020: 'Al Capella',
 7021: 'Des Traction',
 7022: 'Dee Version',
 7023: 'Bo Nanapeel',
 7024: 'Joe Drizzle',
 7025: 'Regina Reign',
 7026: 'Shay Showers',

 10002: "Good ol' Gil Giggles",
 12002: 'Mata Hairy',
 13001: 'Healer Clover',
 13002: 'Bumpy Bumblebehr',
 16001: 'Lonely Louis',
 90001: 'Programmer Leo'}
zone2TitleDict = {2513: ('Toon Hall', ''),
 2514: ('Toontown Bank', ''),
 2516: ('Toontown School House', ''),
 2518: ('Toontown Library', ''),
 2519: ('Gag Shop', ''),
 2520: (lToonHQ, ''),
 2521: ('Clothing Shop', ''),
 2522: ('Pet Shop', ''),
 2601: ('All Smiles Tooth Repair', ''),
 2602: ('', ''),
 2603: ('One-Liner Miners', ''),
 2604: ('Hogwash & Dry', ''),
 2605: ('Toontown Sign Factory', ''),
 2606: ('', ''),
 2607: ('Jumping Beans', ''),
 2610: ('Dr. Tom Foolery', ''),
 2611: ('', ''),
 2616: ("Weird Beard's Disguise Shop", ''),
 2617: ('Silly Stunts', ''),
 2618: ('All That Razz', ''),
 2621: ('Paper Airplanes', ''),
 2624: ('Happy Hooligans', ''),
 2625: ('House of Bad Pies', ''),
 2626: ("Jesse's Joke Repair", ''),
 2629: ("The Laughin' Place", ''),
 2632: ('Clown Class', ''),
 2633: ('Tee-Hee Tea Shop', ''),
 2638: ('Toontown Playhouse', ''),
 2639: ('Monkey Tricks', ''),
 2643: ('Canned Bottles', ''),
 2644: ('Impractical Jokes', ''),
 2649: ('All Fun and Games Shop', ''),
 2652: ('', ''),
 2653: ('', ''),
 2654: ('Laughing Lessons', ''),
 2655: ('Funny Money Savings & Loan', ''),
 2656: ('Used Clown Cars', ''),
 2657: ("Frank's Pranks", ''),
 2659: ('Joy Buzzers to the World', ''),
 2660: ('Tickle Machines', ''),
 2661: ('Daffy Taffy', ''),
 2662: ('Dr. I.M. Euphoric', ''),
 2663: ('Toontown Cinerama', ''),
 2664: ('The Merry Mimes', ''),
 2665: ("Mary's Go Around Travel Company", ''),
 2666: ('Laughing Gas Station', ''),
 2667: ('Happy Times', ''),
 2669: ("Muldoon's Maroon Balloons", ''),
 2670: ('Soup Forks', ''),
 2671: ('', ''),
 2701: ('', ''),
 2704: ('Movie Multiplex', ''),
 2705: ("Wiseacre's Noisemakers", ''),
 2708: ('Blue Glue', ''),
 2711: ('Toontown Post Office', ''),
 2712: ('Chortle Cafe', ''),
 2713: ('Laughter Hours Cafe', ''),
 2714: ('Kooky CinePlex', ''),
 2716: ('Soup and Crack Ups', ''),
 2717: ('Bottled Cans', ''),
 2720: ('Crack Up Auto Repair', ''),
 2725: ('', ''),
 2727: ('Seltzer Bottles and Cans', ''),
 2728: ('Vanishing Cream', ''),
 2729: ('14 Karat Goldfish', ''),
 2730: ('News for the Amused', ''),
 2731: ('', ''),
 2732: ('Spaghetti and Goofballs', ''),
 2733: ('Cast Iron Kites', ''),
 2734: ('Suction Cups and Saucers', ''),
 2735: ('The Kaboomery', ''),
 2739: ("Sidesplitter's Mending", ''),
 2740: ('Used Firecrackers', ''),
 2741: ('', ''),
 2742: ('', ''),
 2743: ('Ragtime Dry Cleaners', ''),
 2744: ('', ''),
 2747: ('Visible Ink', ''),
 2748: ('Jest for Laughs', ''),
 2801: ('Sofa Whoopee Cushions', ''),
 2802: ('Inflatable Wrecking Balls', ''),
 2803: ('The Karnival Kid', ''),
 2804: ('Dr. Pulyurleg, Chiropractor', ''),
 2805: ('', ''),
 2809: ('The Punch Line Gym', ''),
 2814: ('Toontown Theatre', ''),
 2818: ('The Flying Pie', ''),
 2821: ('', ''),
 2822: ('Rubber Chicken Sandwiches', ''),
 2823: ('Sundae Funnies Ice Cream', ''),
 2824: ('Punchline Movie Palace', ''),
 2829: ('Phony Baloney', ''),
 2830: ("Zippy's Zingers", ''),
 2831: ("Professor Wiggle's House of Giggles", ''),
 2832: ('', ''),
 2833: ('', ''),
 2834: ('Funny Bone Emergency Room', ''),
 2836: ('', ''),
 2837: ('Hardy Harr Seminars', ''),
 2839: ('Barely Palatable Pasta', ''),
 2841: ('', ''),
 2901: ('Gold & Silver Pawn Shop', ''),
 2902: ('Krazy Kafe', ''),
 2903: ('Marvelous Monkey Clubhouse', ''),
 2904: ('Joke Repair Shop', ''),
 2905: ('Five Dollar Cream Pies', ''),
 2906: ("Dr. Patrick's Office", ''),
 2907: ('TTC Gas Station', ''),
 2908: ("Starduck's Cafe", ''),
 2909: ('Toon HQ', ''),
 2910: ("Tony's Toy Store", ''),
 2912: ('Banana Cream Memes', ''),
 2913: ('Astron Headquarters', ''),
 1506: ('Gag Shop', ''),
 1507: ('Toon Headquarters', ''),
 1508: ('Clothing Shop', ''),
 1510: ('', ''),
 1602: ('Used Life Preservers', ''),
 1604: ('Wet Suit Dry Cleaners', ''),
 1606: ("Hook's Clock Repair", ''),
 1608: ("Luff 'N Stuff", ''),
 1609: ('Every Little Bait', ''),
 1612: ('Dime & Quarterdeck Bank', ''),
 1613: ('Squid Pro Quo, Attorneys at Law', ''),
 1614: ('Trim the Nail Boutique', ''),
 1615: ("Yacht's All, Folks!", ''),
 1616: ("Blackbeard's Beauty Parlor", ''),
 1617: ('Out to See Optics', ''),
 1619: ('Disembark! Tree Surgeons', ''),
 1620: ('From Fore to Aft', ''),
 1621: ('Poop Deck Gym', ''),
 1622: ('Bait and Switches Electrical Shop', ''),
 1624: ('Soles Repaired While U Wait', ''),
 1626: ('Salmon Chanted Evening Formal Wear', ''),
 1627: ("Billy Budd's Big Bargain Binnacle Barn", ''),
 1628: ('Piano Tuna', ''),
 1629: ('', ''),
 1701: ('Buoys and Gulls Nursery School', ''),
 1703: ('Wok the Plank Chinese Food', ''),
 1705: ('Sails for Sale', ''),
 1706: ('Peanut Butter and Jellyfish', ''),
 1707: ('Gifts With a Porpoise', ''),
 1709: ('Windjammers and Jellies', ''),
 1710: ('Barnacle Bargains', ''),
 1711: ('Deep Sea Diner', ''),
 1712: ('Able-Bodied Gym', ''),
 1713: ("Art's Smart Chart Mart", ''),
 1714: ("Reel 'Em Inn", ''),
 1716: ('Mermaid Swimwear', ''),
 1717: ('Be More Pacific Ocean Notions', ''),
 1718: ('Run Aground Taxi Service', ''),
 1719: ("Duck's Back Water Company", ''),
 1720: ('The Reel Deal', ''),
 1721: ('All For Nautical', ''),
 1723: ("Squid's Seaweed", ''),
 1724: ("That's  a Moray!", ''),
 1725: ("Ahab's Prefab Sea Crab Center", ''),
 1726: ('Root Beer Afloats', ''),
 1727: ('This Oar That', ''),
 1728: ('Good Luck Horseshoe Crabs', ''),
 1729: ('', ''),
 1802: ('Nautical But Nice', ''),
 1804: ('Mussel Beach Gymnasium', ''),
 1805: ('Tackle Box Lunches', ''),
 1806: ('Cap Size Hat Store', ''),
 1807: ('Keel Deals', ''),
 1808: ('Knots So Fast', ''),
 1809: ('Rusty Buckets', ''),
 1810: ('Anchor Management', ''),
 1811: ("What's Canoe With You?", ''),
 1813: ('Pier Pressure Plumbing', ''),
 1814: ('The Yo Ho Stop and Go', ''),
 1815: ("What's Up, Dock?", ''),
 1818: ('Seven Seas Cafe', ''),
 1819: ("Docker's Diner", ''),
 1820: ('Hook, Line, and Sinker Prank Shop', ''),
 1821: ("King Neptoon's Cannery", ''),
 1823: ('The Clam Bake Diner', ''),
 1824: ('Dog Paddles', ''),
 1825: ('Wholly Mackerel! Fish Market', ''),
 1826: ("Claggart's Clever Clovis Closet", ''),
 1828: ("Alice's Ballast Palace", ''),
 1829: ('Seagull Statue Store', ''),
 1830: ('Lost and Flounder', ''),
 1831: ('Kelp Around the House', ''),
 1832: ("Melville's Massive Mizzenmast Mart", ''),
 1833: ('This Transom Man Custom Tailored Suits', ''),
 1834: ('Rudderly Ridiculous!', ''),
 1835: ('', ''),
 4503: ('Gag Shop', ''),
 4504: ('Toon Headquarters', ''),
 4506: ('Clothing Shop', ''),
 4508: ('', ''),
 4603: ("Tom-Tom's Drums", ''),
 4604: ('In Four-Four Time', ''),
 4605: ("Fifi's Fiddles", ''),
 4606: ('Casa De Castanets', ''),
 4607: ('Catchy Toon Apparel', ''),
 4609: ('Do, Rae, Me Piano Keys', ''),
 4610: ('Please Refrain', ''),
 4611: ('Tuning Forks and Spoons', ''),
 4612: ("Dr. Fret's Dentistry", ''),
 4614: ('Shave and a Haircut for a Song', ''),
 4615: ("Piccolo's Pizza", ''),
 4617: ('Happy Mandolins', ''),
 4618: ('Rests Rooms', ''),
 4619: ('More Scores', ''),
 4622: ('Chin Rest Pillows', ''),
 4623: ('Flats Sharpened', ''),
 4625: ('Tuba Toothpaste', ''),
 4626: ('Notations', ''),
 4628: ('Accidental Insurance', ''),
 4629: ("Riff's Paper Plates", ''),
 4630: ('Music Is Our Forte', ''),
 4631: ('Canto Help You', ''),
 4632: ('Dance Around the Clock Shop', ''),
 4635: ('Tenor Times', ''),
 4637: ('For Good Measure', ''),
 4638: ('Hard Rock Shop', ''),
 4639: ('Four Score Antiques', ''),
 4641: ('Blues News', ''),
 4642: ('Ragtime Dry Cleaners', ''),
 4645: ('Club 88', ''),
 4646: ('', ''),
 4648: ('Carry a Toon Movers', ''),
 4649: ('', ''),
 4652: ('Full Stop Shop', ''),
 4653: ('', ''),
 4654: ('Pitch Perfect Roofing', ''),
 4655: ("The Treble Chef's Cooking School", ''),
 4656: ('', ''),
 4657: ('Barbershop Quartet', ''),
 4658: ('Plummeting Pianos', ''),
 4659: ('', ''),
 4701: ('The Schmaltzy Waltz School of Dance', ''),
 4702: ('Timbre! Equipment for the Singing Lumberjack', ''),
 4703: ('I Can Handel It!', ''),
 4704: ("Tina's Concertina Concerts", ''),
 4705: ('Zither Here Nor There', ''),
 4707: ("Doppler's Sound Effects Studio", ''),
 4709: ('On Ballet! Climbing Supplies', ''),
 4710: ('Hurry Up, Slow Polka! School of Driving', ''),
 4712: ('C-Flat Tire Repair', ''),
 4713: ('B-Sharp Fine Menswear', ''),
 4716: ('Four-Part Harmonicas', ''),
 4717: ('Sonata Your Fault! Discount Auto Insurance', ''),
 4718: ('Chopin Blocks and Other Kitchen Supplies', ''),
 4719: ('Madrigal Motor Homes', ''),
 4720: ('Name That Toon', ''),
 4722: ('Overture Understudies', ''),
 4723: ('Haydn Go Seek Playground Supplies', ''),
 4724: ('White Noise for Girls and Boys', ''),
 4725: ('The Baritone Barber', ''),
 4727: ('Vocal Chords Braided', ''),
 4728: ("Sing Solo We Can't Hear You", ''),
 4729: ('Double Reed Bookstore', ''),
 4730: ('Lousy Lyrics', ''),
 4731: ('Toon Tunes', ''),
 4732: ('Etude Brute? Theatre Company', ''),
 4733: ('', ''),
 4734: ('', ''),
 4735: ('Accordions, If You Want In, Just Bellow!', ''),
 4736: ('Her and Hymn Wedding Planners', ''),
 4737: ('Harp Tarps', ''),
 4738: ('Canticle Your Fancy Gift Shop', ''),
 4739: ('', ''),
 4801: ("Marshall's Stacks", ''),
 4803: ('What a Mezzo! Maid Service', ''),
 4804: ('Mixolydian Scales', ''),
 4807: ('Relax the Bach', ''),
 4809: ("I Can't Understanza!", ''),
 4812: ('', ''),
 4817: ('The Ternary Pet Shop', ''),
 4819: ("Yuki's Ukeleles", ''),
 4820: ('', ''),
 4821: ("Anna's Cruises", ''),
 4827: ('Common Time Watches', ''),
 4828: ("Schumann's Shoes for Men", ''),
 4829: ("Pachelbel's Canonballs", ''),
 4835: ('Ursatz for Kool Katz', ''),
 4836: ('Reggae Regalia', ''),
 4838: ('Kazoology School of Music', ''),
 4840: ('Coda Pop Musical Beverages', ''),
 4841: ('Lyre, Lyre, Pants on Fire!', ''),
 4842: ('The Syncopation Corporation', ''),
 4843: ('', ''),
 4844: ('Con Moto Cycles', ''),
 4845: ("Ellie's Elegant Elegies", ''),
 4848: ('Lotsa Lute Savings & Loan', ''),
 4849: ('', ''),
 4850: ('The Borrowed Chord Pawn Shop', ''),
 4852: ('Flowery Flute Fleeces', ''),
 4853: ("Leo's Fenders", ''),
 4854: ("Wagner's Vocational Violin Videos", ''),
 4855: ('The Teli-Caster Network', ''),
 4856: ('', ''),
 4862: ("Quentin's Quintessen\x03tial Quadrilles", ''),
 4867: ("Mr. Costello's Yellow Cellos", ''),
 4868: ('', ''),
 4870: ("Ziggy's Zoo of Zigeuner\x03musik", ''),
 4871: ("Harry's House of Harmonious Humbuckers", ''),
 4872: ("Fast Freddie's Fretless Fingerboards", ''),
 4873: ('', ''),
 5501: ('Gag Shop', ''),
 5502: (lToonHQ, ''),
 5503: ('Clothing Shop', ''),
 5505: ('', ''),
 5601: ('Eye of the Potato Optometry', ''),
 5602: ("Artie Choke's Neckties", ''),
 5603: ('Lettuce Alone', ''),
 5604: ('Cantaloupe Bridal Shop', ''),
 5605: ('Vege-tables and Chairs', ''),
 5606: ('Petals', ''),
 5607: ('Compost Office', ''),
 5608: ('Mom and Pop Corn', ''),
 5609: ('Berried Treasure', ''),
 5610: ("Black-eyed Susan's Boxing Lessons", ''),
 5611: ("Gopher's Gags", ''),
 5613: ('Crop Top Barbers', ''),
 5615: ("Bud's Bird Seed", ''),
 5616: ('Dew Drop Inn', ''),
 5617: ("Flutterby's Butterflies", ''),
 5618: ("Peas and Q's", ''),
 5619: ("Jack's Beanstalks", ''),
 5620: ('Rake It Inn', ''),
 5621: ('Grape Expectations', ''),
 5622: ('Petal Pusher Bicycles', ''),
 5623: ('Bubble Bird Baths', ''),
 5624: ("Mum's the Word", ''),
 5625: ('Leaf It Bees', ''),
 5626: ('Pine Needle Crafts', ''),
 5627: ('', ''),
 5701: ('From Start to Spinach', ''),
 5702: ("Jake's Rakes", ''),
 5703: ("Photo Cynthia's Camera Shop", ''),
 5704: ('Lisa Lemon Used Cars', ''),
 5705: ('Poison Oak Furniture', ''),
 5706: ('14 Carrot Jewelers', ''),
 5707: ('Musical Fruit', ''),
 5708: ("We'd Be Gone Travel Agency", ''),
 5709: ('Astroturf Mowers', ''),
 5710: ('Tuft Guy Gym', ''),
 5711: ('Garden Hosiery', ''),
 5712: ('Silly Statues', ''),
 5713: ('Trowels and Tribulations', ''),
 5714: ('Spring Rain Seltzer Bottles', ''),
 5715: ('Hayseed News', ''),
 5716: ('Take It or Leaf It Pawn Shop', ''),
 5717: ('The Squirting Flower', ''),
 5718: ('The Dandy Lion Exotic Pets', ''),
 5719: ('Trellis the Truth! Private Investi\x03gators', ''),
 5720: ('Vine and Dandy Menswear', ''),
 5721: ('Root 66 Diner', ''),
 5725: ('Barley, Hops, and Malt Shop', ''),
 5726: ("Bert's Dirt", ''),
 5727: ('Gopher Broke Savings & Loan', ''),
 5728: ('', ''),
 5802: (lToonHQ, ''),
 5804: ('Just Vase It', ''),
 5805: ('Snail Mail', ''),
 5809: ('Fungi Clown School', ''),
 5810: ('Honeydew This', ''),
 5811: ('Lettuce Inn', ''),
 5815: ('Grass Roots', ''),
 5817: ('Apples and Oranges', ''),
 5819: ('Green Bean Jeans', ''),
 5821: ('Squash and Stretch Gym', ''),
 5826: ('Ant Farming Supplies', ''),
 5827: ('Dirt. Cheap.', ''),
 5828: ('Couch Potato Furniture', ''),
 5830: ('Spill the Beans', ''),
 5833: ('The Salad Bar', ''),
 5835: ('Flower Bed and Breakfast', ''),
 5836: ("April's Showers and Tubs", ''),
 5837: ('School of Vine Arts', ''),
 7601: ('All Smiles Tooth Repair', ''),
 7602: ('', ''),
 7603: ('Masters Miners', ''),
 7604: ('Hogwash & Dry', ''),
 7605: ('Toontown Sign Factory', ''),
 7606: ('', ''),
 7607: ('Jumping Beans', ''),
 7610: ('Dr. Tom Foolery', ''),
 7611: ('', ''),
 7616: ("Tiger Mighty Disguise Shop", ''),
 7617: ('Silly Stunts', ''),
 7618: ('All That Razz', ''),
 7621: ('Paper Airplanes', ''),
 7624: ('Happy Hooligans', ''),
 7625: ('House of Bad Pies', ''),
 7626: ("Jesse's Joke Repair", ''),
 7629: ("The Laughin' Place", ''),
 7632: ('Clown Class', ''),
 7633: ('Tee-Hee Tea Shop', ''),
 7638: ('Toontown Playhouse', ''),
 7639: ("Magic's Tricks", ''),
 7643: ('Canned Bottles', ''),
 7644: ('Impractical Jokes', ''),
 7649: ('All Fun and Games Shop', ''),
 7652: ('', ''),
 7653: ('', ''),
 7654: ('Laughing Lessons', ''),
 7655: ('Funny Money Savings & Loan', ''),
 7656: ('Used Clown Cars', ''),
 7657: ("Frank's Pranks", ''),
 7659: ('Joy Buzzers to the World', ''),
 7660: ('Tickle Machines', ''),
 7661: ("Don's Baits", ''),
 7662: ('Dr. I.M. Euphoric', ''),
 7663: ('Toontown Cinerama', ''),
 7664: ('The Merry Mimes', ''),
 7665: ("Mary's Go Around Travel Company", ''),
 7666: ('Laughing Gas Station', ''),
 7667: ('Happy Times', ''),
 7669: ("Muldoon's Maroon Balloons", ''),
 7670: ('Soup Forks', ''),
 7671: ('', ''),
 9501: ('Lullaby Library', ''),
 9503: ('The Snooze Bar', ''),
 9504: ('Gag Shop', ''),
 9505: (lToonHQ, ''),
 9506: ('Clothing Shop', ''),
 9508: ('', ''),
 9601: ('Snuggle Inn', ''),
 9602: ('Forty Winks for the Price of Twenty', ''),
 9604: ("Ed's Red Bed Spreads", ''),
 9605: ('Cloud Nine Design', ''),
 9607: ("Big Mama's Bahama Pajamas", ''),
 9608: ('Cat Nip for Cat Naps', ''),
 9609: ('Deep Sleep for Cheap', ''),
 9613: ('Clock Cleaners', ''),
 9616: ('Lights Out Electric Co.', ''),
 9617: ('Crib Notes - Music to Sleep By', ''),
 9619: ('Relax to the Max', ''),
 9620: ("PJ's Taxi Service", ''),
 9622: ('Sleepy Time Pieces', ''),
 9625: ('Curl Up Beauty Parlor', ''),
 9626: ('Bed Time Stories', ''),
 9627: ('The Sleepy Teepee', ''),
 9628: ('Call It a Day Calendars', ''),
 9629: ('Silver Lining Jewelers', ''),
 9630: ('Rock to Sleep Quarry', ''),
 9631: ('Down Time Watch Repair', ''),
 9633: ('The Dreamland Screening Room', ''),
 9634: ('Mind Over Mattress', ''),
 9636: ('Insomniac Insurance', ''),
 9639: ('House of Hibernation', ''),
 9640: ('Nightstand Furniture Company', ''),
 9642: ('Sawing Wood Slumber Lumber', ''),
 9643: ('Shut-Eye Optometry', ''),
 9644: ('Pillow Fights Nightly', ''),
 9645: ('The All Tucked Inn', ''),
 9647: ('Make Your Bed! Hardware Store', ''),
 9649: ('Snore or Less', ''),
 9650: ('Crack of Dawn Repairs', ''),
 9651: ('For Richer or Snorer', ''),
 9652: ('', ''),
 9703: ('Fly By Night Travel Agency', ''),
 9704: ('Night Owl Pet Shop', ''),
 9705: ('Asleep At The Wheel Car Repair', ''),
 9706: ('Tooth Fairy Dentistry', ''),
 9707: ("Dawn's Yawn & Garden Center", ''),
 9708: ('Bed Of Roses Florist', ''),
 9709: ('Pipe Dream Plumbers', ''),
 9710: ('REM Optometry', ''),
 9711: ('Wake-Up Call Phone Company', ''),
 9712: ("Counting Sheep - So You Don't Have To!", ''),
 9713: ('Wynken, Blynken & Nod, Attorneys at Law', ''),
 9714: ('Dreamboat Marine Supply', ''),
 9715: ('First Security Blanket Bank', ''),
 9716: ('Wet Blanket Party Planners', ''),
 9717: ("Baker's Dozin' Doughnuts", ''),
 9718: ("Sandman's Sandwiches", ''),
 9719: ('Armadillo Pillow Company', ''),
 9720: ('Talking In Your Sleep Voice Training', ''),
 9721: ('Snug As A Bug Rug Dealer', ''),
 9722: ('Dream On Talent Agency', ''),
 9725: ("Cat's Pajamas", ''),
 9727: ('You Snooze, You Lose', ''),
 9736: ('Dream Jobs Employment Agency', ''),
 9737: ("Waltzing Matilda's Dance School", ''),
 9738: ('House of Zzzzzs', ''),
 9740: ('Hit The Sack Fencing School', ''),
 9741: ("Don't Let The Bed Bugs Bite Exterminators", ''),
 9744: ("Rip Van Winkle's Wrinkle Cream", ''),
 9752: ('Midnight Oil & Gas Company', ''),
 9753: ("Moonbeam's Ice Creams", ''),
 9754: ('Sleepless in the Saddle All Night Pony Rides', ''),
 9755: ('Bedknobs & Broomsticks Movie House', ''),
 9756: ('', ''),
 9759: ('Sleeping Beauty Parlor', ''),
 3507: ('Gag Shop', ''),
 3508: (lToonHQ, ''),
 3509: ('Clothing Shop', ''),
 3511: ('', ''),
 3601: ('Northern Lights Electric Company', ''),
 3602: ("Nor'easter Bonnets", ''),
 3605: ('', ''),
 3607: ('The Blizzard Wizard', ''),
 3608: ('Nothing to Luge', ''),
 3610: ("Mike's Massive Mukluk Mart", ''),
 3611: ("Mr. Cow's Snow Plows", ''),
 3612: ('Igloo Design', ''),
 3613: ('Ice Cycle Bikes', ''),
 3614: ('Snowflakes Cereal Company', ''),
 3615: ('Fried Baked Alaskas', ''),
 3617: ('Cold Air Balloon Rides', ''),
 3618: ('Snow Big Deal! Crisis Management', ''),
 3620: ('Skiing Clinic', ''),
 3621: ('The Melting Ice Cream Bar', ''),
 3622: ('', ''),
 3623: ('The Mostly Toasty Bread Company', ''),
 3624: ('Subzero Sandwich Shop', ''),
 3625: ("Auntie Freeze's Radiator Supply", ''),
 3627: ('St. Bernard Kennel Club', ''),
 3629: ('Pea Soup Cafe', ''),
 3630: ('Icy London, Icy France Travel Agency', ''),
 3634: ('Easy Chair Lifts', ''),
 3635: ('Used Firewood', ''),
 3636: ('Affordable Goosebumps', ''),
 3637: ("Kate's Skates", ''),
 3638: ('Toboggan or Not Toboggan', ''),
 3641: ("Fred's Red Sled Beds", ''),
 3642: ('Eye of the Storm Optics', ''),
 3643: ('Snowball Hall', ''),
 3644: ('Melted Ice Cubes', ''),
 3647: ('The Sanguine Penguin Tuxedo Shop', ''),
 3648: ('Instant Ice', ''),
 3649: ('Hambrrrgers', ''),
 3650: ('Antarctic Antiques', ''),
 3651: ("Frosty Freddy's Frozen Frankfurters", ''),
 3653: ('Ice House Jewelry', ''),
 3654: ('', ''),
 3702: ('Winter Storage', ''),
 3703: ('', ''),
 3705: ('Icicles Built for Two', ''),
 3706: ("Shiverin' Shakes Malt Shop", ''),
 3707: ('Snowplace Like Home', ''),
 3708: ("Pluto's Place", ''),
 3710: ('Dropping Degrees Diner', ''),
 3711: ('', ''),
 3712: ('Go With the Floe', ''),
 3713: ('Chattering Teeth, Subzero Dentist', ''),
 3715: ("Aunt Arctic's Soup Shop", ''),
 3716: ('Road Salt and Pepper', ''),
 3717: ('Juneau What I Mean?', ''),
 3718: ('Designer Inner Tubes', ''),
 3719: ('Ice Cube on a Stick', ''),
 3721: ("Noggin's Toboggan Bargains", ''),
 3722: ('Snow Bunny Ski Shop', ''),
 3723: ("Shakey's Snow Globes", ''),
 3724: ('The Chattering Chronicle', ''),
 3725: ('You Sleigh Me', ''),
 3726: ('Solar Powered Blankets', ''),
 3728: ('Lowbrow Snowplows', ''),
 3729: ('', ''),
 3730: ('Snowmen Bought & Sold', ''),
 3731: ('Portable Fireplaces', ''),
 3732: ('The Frozen Nose', ''),
 3734: ('Icy Fine, Do You? Optometry', ''),
 3735: ('Polar Ice Caps', ''),
 3736: ('Diced Ice at a Nice Price', ''),
 3737: ('Downhill Diner', ''),
 3738: ("Heat-Get It While It's Hot", ''),
 3739: ('', ''),
 3801: ('Toon HQ', ''),
 3806: ('Alpine Chow Line', ''),
 3807: ('Used Groundhog Shadows', ''),
 3808: ('The Sweater Lodge', ''),
 3809: ('Ice Saw It Too', ''),
 3810: ('A Better Built Quilt', ''),
 3811: ('Your Snow Angel', ''),
 3812: ('Mittens for Kittens', ''),
 3813: ("Snowshoes You Can't Refuse", ''),
 3814: ('Malt in Your Mouth Soda Fountain', ''),
 3815: ('The Toupee Chalet', ''),
 3816: ('Just So Mistletoe', ''),
 3817: ('Winter Wonderland Walking Club', ''),
 3818: ('The Shovel Hovel', ''),
 3819: ('Clean Sweep Chimney Service', ''),
 3820: ('Snow Whitening', ''),
 3821: ('Hibernation Vacations', ''),
 3823: ('Precipitation Foundation', ''),
 3824: ('Open Fire Chestnut Roasting', ''),
 3825: ('Cool Cat Hats', ''),
 3826: ('Oh My Galoshes!', ''),
 3827: ('Choral Wreaths', ''),
 3828: ("Snowman's Land", ''),
 3829: ('Pinecone Zone', ''),
 3830: ('Wait and See Goggle Defogging', ''),
 9801: ("Midnight Snack Shop", ''),
 9802: ("Tick Tock, Clocks On You!", ''),
 9803: ("Sleepy's", ''),
 9804: ("Drowsy Jellybean Pharmacy", ''),
 9805: ('Koo Koo Cafe', ''),
 9806: ('Midnight Cat Clan', ''),
 9807: ('Whispurr Down The Lane', ''),
 9808: ("My Little Pillow", ''),
 9809: ("Club Dreamland", ''),
 9810: ('Sleepy Sallys.', ''),
 9812: ('Twinkle Twinkle Little Toon', ''),
 9813: ("Gasoline! All For Your Needs!", ''),
 9814: ("Spooky Scary Skelecogs", ''),
 9815: ("Fallen And Can't Get Up", ''),
 9816: ("Rest In Pies", ''),
 9817: ("Dreamland Funeral House", ''),
 9818: ("Toon HQ", ''),
 9819: ("Drowsy Diner", ''),
 9820: ("Sleepy Sid's Sleeping Beds", ''),
}
ClosetTimeoutMessage = 'Sorry, you ran out\n of time.'
ClosetNotOwnerMessage = "This isn't your closet, but you may try on the clothes."
ClosetPopupOK = lOK
ClosetPopupCancel = lCancel
ClosetDiscardButton = 'Remove'
ClosetAreYouSureMessage = 'You have deleted some clothes.  Do you really want to delete them?'
ClosetYes = lYes
ClosetNo = lNo
ClosetVerifyDelete = 'Really delete %s?'
ClosetShirt = 'this shirt'
ClosetShorts = 'these shorts'
ClosetSkirt = 'this skirt'
ClosetDeleteShirt = 'Delete\nshirt'
ClosetDeleteShorts = 'Delete\nshorts'
ClosetDeleteSkirt = 'Delete\nskirt'
TrunkNotOwnerMessage = "This isn't your trunk, but you may try on the accessories."
TrunkAreYouSureMessage = 'You have deleted some accessories.  Do you really want to delete them?'
TrunkHat = 'this hat'
TrunkGlasses = 'these glasses'
TrunkBackpack = 'this backpack'
TrunkShoes = 'these shoes'
TrunkDeleteHat = 'Delete\nhat'
TrunkDeleteGlasses = 'Delete\nglasses'
TrunkDeleteBackpack = 'Delete\nbackpack'
TrunkDeleteShoes = 'Delete\nshoes'
EstateOwnerLeftMessage = "Sorry, the owner of this estate left.  You'll be sent to the playground in %s seconds"
EstatePopupOK = lOK
EstateTeleportFailed = "Couldn't go home. Try again!"
EstateTeleportFailedNotFriends = "Sorry, %s is in a toon's estate that you are not friends with."
EstateTargetGameStart = 'The Toon-up Target game has started!'
EstateTargetGameInst = "The more you hit the red target, the more you'll get Tooned up."
EstateTargetGameEnd = 'The Toon-up Target game is now over...'
AvatarsHouse = '%s\n House'
BankGuiCancel = lCancel
BankGuiOk = lOK
BankGuiWithdrawAll = 'Withdraw All'
DistributedBankNoOwner = 'Sorry, this is not your bank.'
DistributedBankNotOwner = 'Sorry, this is not your bank.'
FishGuiCancel = lCancel
FishGuiOk = 'Sell All'
FishTankValue = 'Hi, %(name)s! You have %(num)s fish in your bucket worth a total of %(value)s Jellybeans. Do you want to sell them all?'
FlowerGuiCancel = lCancel
FlowerGuiOk = 'Sell All'
FlowerBasketValue = '%(name)s, you have %(num)s flowers in your basket worth a total of %(value)s Jellybeans. Do you want to sell them all?'

def GetPossesive(name):
    if name[-1:] == 's':
        possesive = name + "'"
    else:
        possesive = name + "'s"
    return possesive


PetTrait2descriptions = {'hungerThreshold': ('Always Hungry',
                     'Often Hungry',
                     'Sometimes Hungry',
                     'Rarely Hungry'),
 'boredomThreshold': ('Always Bored',
                      'Often Bored',
                      'Sometimes Bored',
                      'Rarely Bored'),
 'angerThreshold': ('Always Grumpy',
                    'Often Grumpy',
                    'Sometimes Grumpy',
                    'Rarely Grumpy'),
 'forgetfulness': ('Always Forgets',
                   'Often Forgets',
                   'Sometimes Forgets',
                   'Rarely Forgets'),
 'excitementThreshold': ('Very Calm',
                         'Pretty Calm',
                         'Pretty Excitable',
                         'Very Excitable'),
 'sadnessThreshold': ('Always Sad',
                      'Often Sad',
                      'Sometimes Sad',
                      'Rarely Sad'),
 'restlessnessThreshold': ('Always Restless',
                           'Often Restless',
                           'Sometimes Restless',
                           'Rarely Restless'),
 'playfulnessThreshold': ('Rarely Playful',
                          'Sometimes Playful',
                          'Often Playful',
                          'Always Playful'),
 'lonelinessThreshold': ('Always Lonely',
                         'Often Lonely',
                         'Sometimes Lonely',
                         'Rarely Lonely'),
 'fatigueThreshold': ('Always Tired',
                      'Often Tired',
                      'Sometimes Tired',
                      'Rarely Tired'),
 'confusionThreshold': ('Always Confused',
                        'Often Confused',
                        'Sometimes Confused',
                        'Rarely Confused'),
 'surpriseThreshold': ('Always Surprised',
                       'Often Surprised',
                       'Sometimes Surprised',
                       'Rarely Surprised'),
 'affectionThreshold': ('Rarely Affectionate',
                        'Sometimes Affectionate',
                        'Often Affectionate',
                        'Always Affectionate')}
FireworksInstructions = lToonHQ + ': Hit the "Page Up" key to see the show!'
FireworksJuly4Beginning = lToonHQ + ': Welcome to summer fireworks! Enjoy the show!'
FireworksJuly4Ending = lToonHQ + ': Hope you enjoyed the show! Have a great summer!'
FireworksNewYearsEveBeginning = lToonHQ + ': Happy New Year! Enjoy the fireworks show, sponsored by Flippy!'
FireworksNewYearsEveEnding = lToonHQ + ': Hope you enjoyed the show! Have a Toontastic New Year!'
FireworksComboBeginning = lToonHQ + ': Enjoy lots of Laffs with Toon fireworks!'
FireworksComboEnding = lToonHQ + ': Thank you, Toons! Hope you enjoyed the show!'
TIP_NONE = 0
TIP_GENERAL = 1
TIP_STREET = 2
TIP_MINIGAME = 3
TIP_COGHQ = 4
TIP_ESTATE = 5
TIP_KARTING = 6
TIP_GOLF = 7
TipTitle = 'TOON TIP:'
TipDict = {TIP_NONE: ('',),
 TIP_GENERAL: ('Quickly check your ToonTask progress by holding down the "End" key.',
               'Quickly check your Gag page by holding down the "Home" key.',
               'Open your Friends List by pressing the "F7" key.',
               'Open or close your Shticker Book by pressing the "F8" key.',
               'You can look up by pressing the "Page Up" key and look down by pressing the "Page Down" key.',
               'Press the "Control" key to jump.',
               'Press the "F9" key to take a screenshot, which will be saved in your Toontown: Gear Grind folder on your computer.',
               'You can change your screen resolution, adjust audio, and control other options on the Options Page in the Shticker Book.',
               "Try on your friend's clothing at the closet in their house.",
               'You can go to your house using the "Go Home" button on your map.',
               'Every time you turn in a completed ToonTask your Laff points are automatically refilled.',
               'You can browse the selection at Clothing Stores even without jellybeans.',
               'Rewards for some ToonTasks allow you to carry more gags and Jellybeans.',
               'You can have up to 100 friends on your Friends List.',
               'Some ToonTask rewards let you teleport to playgrounds in Toontown by using the Map Page in the Shticker Book.',
               'Increase your Laff points in the Playgrounds by collecting treasures like stars and ice cream cones.',
               'To heal quickly after a battle, go to your estate and play with your Doodle.',
               'Change to different views of your Toon by pressing the Tab Key.',
               'Sometimes you can find several different ToonTasks offered for the same reward. Shop around!',
               'Finding friends with similar ToonTasks is a fun way to progress through the game.',
               'You never need to save your Toontown progress. The servers are continuously saving your progress.',
               'You can whisper to other Toons either by clicking on them or by selecting them from your Friends List.',
               'Some SpeedChat phrases play emotion animations on your Toon.',
               'If the area you are in is crowded, try changing Districts. Go to the District Page in the Shticker Book and select a different one.',
               'If you actively rescue buildings you will get a bronze, silver, or gold star above your Toon.',
               'If you rescue enough buildings to get a star above your head you may find your name on the blackboard in a Toon HQ.',
               'Rescued buildings are sometimes recaptured by the Cogs. The only way to keep your star is to go out and rescue more buildings!',
               'The names of your True Friends will appear in Blue.',
               'See if you can collect all the fish in Toontown!',
               'Different ponds hold different fish. Try them all!',
               'When your fishing bucket is full sell your fish to the Fishermen in the Playgrounds.',
               'You can sell your fish to the Fishermen or inside Pet Shops.',
               'Stronger fishing rods catch heavier fish but cost more Jellybeans to use.',
               'You can purchase stronger fishing rods in the Cattlelog.',
               'Heavier fish are worth more Jellybeans to the Pet Shop.',
               'Rare fish are worth more Jellybeans to the Pet Shop.',
               'You can sometimes find bags of Jellybeans while fishing.',
               'Some ToonTasks require fishing items out of the ponds.',
               'Fishing ponds in the Playgrounds have different fish than ponds on the streets.',
               'Some fish are really rare. Keep fishing until you collect them all!',
               'The pond at your estate has fish that can only be found there.',
               'For every 10 species you catch, you will get a fishing trophy!',
               'You can see what fish you have collected in your Shticker Book.',
               'Some fishing trophies reward you with a Laff boost.',
               'Fishing is a good way to earn more Jellybeans.',
               'Adopt a Doodle at the Pet Shop!',
               'Pet Shops get new Doodles to sell every day.',
               'Visit the Pet Shops every day to see what new Doodles they have.',
               'Different neighborhoods have different Doodles offered for adoption.',
               "Show off your stylin' ride and turbo-boost your Laff limit at Goofy Speedway.",
               'Enter Goofy Speedway through the tire-shaped tunnel in Toontown Central Playground.',
               'Earn Laff points at Goofy Speedway.',
               'Goofy Speedway has six different race tracks. '),
 TIP_STREET: ('There are four types of Cogs: Lawbots, Cashbots, Sellbots, and Bossbots.',
              'Each Gag Track has different amounts of accuracy and damage.',
              'Sound gags will affect all Cogs but will wake up any lured Cogs.',
              'Defeating Cogs in strategic order can greatly increase your chances of winning battles.',
              'The Toon-Up Gag Track lets you heal other Toons in battle.',
              'Gag experience points are doubled during a Cog Invasion!',
              'Multiple Toons can team up and use the same Gag Track in battle to get bonus Cog damage.',
              'In battle, gags are used in order from top to bottom as displayed on the Gag Menu.',
              'The row of circular lights over Cog Building elevators show how many floors will be inside.',
              'Click on a Cog to see more details.',
              'Using high level gags against low level Cogs will not earn any experience points.',
              'A gag that will earn experience has a blue background on the Gag Menu in battle.',
              'Gag experience is multiplied when used inside Cog Buildings. Higher floors have higher multipliers.',
              'When a Cog is defeated, each Toon in that round will get credit for the Cog when the battle is over.',
              'Each street in Toontown has different Cog levels and types.',
              'Sidewalks are safe from Cogs.',
              'On the streets, side doors tell knock-knock jokes when approached.',
              'Some ToonTasks train you for new Gag Tracks.',
              'Traps are only useful if you or your friends coordinate using Lure in battle.',
              'Higher level Lures are less likely to miss.',
              'Lower level gags have a lower accuracy against high level Cogs.',
              'Cogs cannot attack once they have been lured in battle.',
              'When you and your friends defeat a Cog building you are rewarded with portraits inside the rescued Toon Building.',
              'Using a Toon-Up gag on a Toon with a full Laff meter will not earn Toon-Up experience.',
              'Cogs will be briefly stunned when hit by any gag. This increases the chance that other gags in the same round will hit.',
              'Drop gags have low chance of hitting, but accuracy is increased when Cogs are first hit by another gag in the same round.',
              'When you\'ve defeated enough Cogs, use the "Cog Radar" by clicking the Cog icons on the Cog Gallery page in your Shticker Book.',
              'During a battle, you can tell which Cog your teammates are attacking by looking at the dashes (-) and Xs.',
              'During a battle, Cogs have a light on them that displays their health; green is healthy, red is nearly destroyed.',
              'A maximum of four Toons can battle at once.',
              'On the street, Cogs are more likely to join a fight against multiple Toons than just one Toon.',
              'The two most difficult Cogs of each type are only found in buildings.',
              'Drop gags never work against lured Cogs.',
              'Cogs tend to attack the Toon that has done them the most damage.',
              'Sound gags do not get bonus damage against lured Cogs.',
              'If you wait too long to attack a lured Cog, it will wake up. Higher level lures last longer.',
              'There are fishing ponds on every street in Toontown. Some streets have unique fish.'),
 TIP_MINIGAME: ('After you fill up your Jellybean jar, any Jellybeans you get from Trolley Games automatically spill over into your bank.',
                'You can use the arrow keys instead of the mouse in the "Match Jaymo" Trolley Game.',
                'In the Cannon Game you can use the arrow keys to move your cannon and press the "Control" key to fire.',
                'In the Ring Game, bonus points are awarded when the entire group successfully swims through its rings.',
                'A perfect game of Match Jaymo will double your points.',
                'In the Tug-of-War you are awarded more Jellybeans if you play against a tougher Cog.',
                'Trolley Game difficulty varies by neighborhood; ' + lToontownCentral + ' has the easiest and ' + lDonaldsDreamland + ' has the hardest.',
                'Certain Trolley Games can only be played in a group.'),
 TIP_COGHQ: ('You must complete your Sellbot Disguise before visiting the V.P.',
             'You must complete your Cashbot Disguise before visiting the C.F.O.',
             'You must complete your Lawbot Disguise before visiting the Chief Justice.',
             'You can jump on Cog Goons to temporarily disable them.',
             'Collect Cog Merits by defeating Sellbot Cogs in battle.',
             'Collect Cogbucks by defeating Cashbot Cogs in battle.',
             'Collect Jury Notices by defeating Lawbot Cogs in battle.',
             'Collect Stock Options by defeating Bossbot Cogs in battle.',
             'You get more Merits, Cogbucks, Jury Notices, or Stock Options from higher level Cogs.',
             'When you collect enough Cog Merits to earn a promotion, go see the Sellbot V.P.!',
             'When you collect enough Cogbucks to earn a promotion, go see the Cashbot C.F.O.!',
             'When you collect enough Jury Notices to earn a promotion, go see the Lawbot Chief Justice!',
             'When you collect enough Stock Options to earn a promotion, go see the Bossbot C.E.O.!',
             'You can talk like a Cog when you are wearing your Cog Disguise.',
             'Up to eight Toons can join together to fight the Sellbot V.P.',
             'Up to eight Toons can join together to fight the Cashbot C.F.O.',
             'Up to eight Toons can join together to fight the Lawbot Chief Justice.',
             'Up to eight Toons can join together to fight the Bossbot C.E.O.',
             'Inside Cog Headquarters follow stairs leading up to find your way.',
             'Each time you battle through a Sellbot HQ factory, you will gain one part of your Sellbot Cog Disguise.',
             'You can check the progress of your Cog Disguise in your Shticker Book.',
             'You can check your promotion progress on your Disguise Page in your Shticker Book.',
             'Make sure you have full gags and a full Laff Meter before going to Cog Headquarters.',
             'As you get promoted, your Cog disguise updates.',
             'You must defeat the ' + Foreman + ' to recover a Sellbot Cog Disguise part.',
             "Earn Cashbot disguise suit parts as rewards for completing ToonTasks in Daunting Dreamland.",
             'Cashbots manufacture and distribute their currency, Cogbucks, in three Mints - Coin, Dollar and Bullion.',
             'Wait until the C.F.O. is dizzy to throw a safe, or he will use it as a helmet! Hit the helmet with another safe to knock it off.',
             'Earn Lawbot disguise suit parts as rewards for completing ToonTasks for Professor Flake.',
             "It pays to be puzzled: the virtual Cogs in Lawbot HQ won't reward you with Jury Notices."),
 TIP_ESTATE: ('Doodles can understand some SpeedChat phrases. Try them!',
              'Use the "Pet" SpeedChat menu to ask your Doodle to do tricks.',
              "You can teach Doodles tricks with training lessons from Clarabelle's Cattlelog.",
              'Reward your Doodle for doing tricks.',
              "If you visit a friend's estate, your Doodle will come too.",
              'Feed your Doodle a Jellybean when it is hungry.',
              'Click on a Doodle to get a menu where you can Feed, Scratch, and Call him.',
              'Doodles love company. Invite your friends over to play!',
              'All Doodles have unique personalities.',
              'You can return your Doodle and adopt a new one at the Pet Shops.',
              'When a Doodle performs a trick, the Toons around it heal.',
              'Doodles become better at tricks with practice. Keep at it!',
              'More advanced Doodle tricks heal Toons faster.',
              'Experienced Doodles can perform more tricks before getting tired.',
              'You can see a list of nearby Doodles in your Friends List.',
              "Purchase furniture from Clarabelle's Cattlelog to decorate your house.",
              'The bank inside your house holds extra Jellybeans.',
              'The closet inside your house holds extra clothes.',
              "Go to your friend's house and try on his clothes.",
              "Purchase better fishing rods from Clarabelle's Cattlelog.",
              'Call Clarabelle using the phone inside your house.',
              'Clarabelle sells a larger closet that holds more clothing.',
              'Clarabelle sells everything you need to decorate your house.',
              'Check your mailbox for deliveries after ordering from Clarabelle.',
              "Clothing from Clarabelle's Cattlelog takes one hour to be delivered.",
              "Wallpaper and flooring from Clarabelle's Cattlelog take one hour to be delivered.",
              "Furniture from Clarabelle's Cattlelog takes a full day to be delivered.",
              'Store extra furniture in your attic.',
              'You will get a notice from Clarabelle when a new Cattlelog is ready.',
              'You will get a notice from Clarabelle when a Cattlelog delivery arrives.',
              'New Cattlelogs are delivered each week.',
              'Look for limited-edition holiday items in the Cattlelog.',
              'Move unwanted furniture to the trash can.',
              'Some fish, like the Holey Mackerel, are more commonly found in Toon Estates.',
              'You can invite your friends to your Estate using SpeedChat.',
              'Did you know the color of your house matches the color of your Pick-A-Toon panel?'),
 TIP_KARTING: ("Buy a Roadster, TUV, or Cruiser kart in Goofy's Auto Shop.",
               "Customize your kart with decals, rims and more in Goofy's Auto Shop.",
               'Earn tickets by kart racing at Goofy Speedway.',
               "Tickets are the only currency accepted at Goofy's Auto Shop.",
               'Tickets are required as deposits to race.',
               'A special page in the Shticker Book allows you to customize your kart.',
               'A special page in the Shticker Book allows you to view records on each track.',
               'A special page in the Shticker Book allows you to display trophies.',
               'Screwball Stadium is the easiest track at Goofy Speedway.',
               'Airborne Acres has the most hills and jumps of any track at Goofy Speedway.',
               'Blizzard Boulevard is the most challenging track at Goofy Speedway.'),
 TIP_GOLF: ('Press the Tab key to see a top view of the golf course.', 'Press the Up Arrow key to point yourself towards the golf hole.', 'Swinging the club is just like throwing a pie.')}
FishGenusNames = {0: 'Balloon Fish',
 2: 'Cat Fish',
 4: 'Clown Fish',
 6: 'Frozen Fish',
 8: 'Star Fish',
 10: 'Holey Mackerel',
 12: 'Dog Fish',
 14: 'Amore Eel',
 16: 'Nurse Shark',
 18: 'King Crab',
 20: 'Moon Fish',
 22: 'Doll Fin',
 24: 'Sea Horse',
 26: 'Pool Shark',
 28: 'Bear Acuda',
 30: 'Cutthroat Trout',
 32: 'Piano Tuna',
 34: 'Whale Shark',
 36: 'Peanut Butter & Jellyfish',
 38: 'Devil Ray'}
FishSpeciesNames = {0: ('Balloon Fish',
     'Hot Air Balloon Fish',
     'Weather Balloon Fish',
     'Water Balloon Fish',
     'Red Balloon Fish',
     'Birthday Balloon Fish'),
 2: ('Cat Fish',
     'Siamese Cat Fish',
     'Alley Cat Fish',
     'Tabby Cat Fish',
     'Tom Cat Fish',
     'Kitty Cat Fish'),
 4: ('Clown Fish',
     'Sad Clown Fish',
     'Party Clown Fish',
     'Circus Clown Fish',
     'Class Clown Fish'),
 6: ('Frozen Fish', 'Unfrozen Fish', 'Dry Frozen Fish', 'Flying Frozen Fish', 'Big Frozen Fish'),
 8: ('Star Fish',
     'Five Star Fish',
     'Rock Star Fish',
     'Pop Star Fish',
     'Shining Star Fish',
     'All Star Fish'),
 10: ('Holey Mackerel',),
 12: ('Dog Fish',
      'Bull Dog Fish',
      'Hot Dog Fish',
      'Dalmatian Dog Fish',
      'Puppy Dog Fish'),
 14: ('Amore Eel', 'Electric Amore Eel', 'Moray Amore Eel', 'Anguillidae Amore Eel', 'Moninguidae Amore Eel'),
 16: ('Nurse Shark', 'Clara Nurse Shark', 'Florence Nurse Shark', 'Hammerhead Nurse Shark', 'Whale Nurse Shark'),
 18: ('King Crab', 'Alaskan King Crab', 'Old King Crab', 'Three King Crab', 'Spider King Crab'),
 20: ('Moon Fish',
      'Full Moon Fish',
      'Half Moon Fish',
      'Quarter Moon Fish',
      'New Moon Fish',
      'Crescent Moon Fish',
      'Harvest Moon Fish'),
 22: ('Doll Fin',
      'Spinner Doll Fin',
      'River Doll Fin',
      'Rough Toothed Doll Fin'),
 24: ('Sea Horse',
      'Rocking Sea Horse',
      'Clydesdale Sea Horse',
      'Arabian Sea Horse',
      'Racing Sea Horse'),
 26: ('Pool Shark',
      'Kiddie Pool Shark',
      'Swimming Pool Shark',
      'Olympic Pool Shark',
      'Saw Pool Shark',
      'Great White Pool Shark'),
 28: ('Brown Bear Acuda',
      'Black Bear Acuda',
      'Koala Bear Acuda',
      'Honey Bear Acuda',
      'Polar Bear Acuda',
      'Panda Bear Acuda',
      'Kodiac Bear Acuda',
      'Grizzly Bear Acuda'),
 30: ('Cutthroat Trout', 'Captain Cutthroat Trout', 'Scurvy Cutthroat Trout'),
 32: ('Piano Tuna',
      'Grand Piano Tuna',
      'Baby Grand Piano Tuna',
      'Upright Piano Tuna',
      'Player Piano Tuna',
      'Ivory Piano Tuna'),
 34: ('Whale Shark',
      'Killer Whale Shark',
      'White Whale Shark',
      'Humpback Whale Shark'),
 36: ('Peanut Butter & Jellyfish',
      'Grape PB&J Fish',
      'Crunchy PB&J Fish',
      'Strawberry PB&J Fish',
      'Concord Grape PB&J Fish'),
 38: ('Devil Ray', 'Spotted Devil Ray', 'Black Devil Ray')}
CogPartNames = ('Upper Left Leg',
 'Lower Left Leg',
 'Left Foot',
 'Upper Right Leg',
 'Lower Right Leg',
 'Right Foot',
 'Left Shoulder',
 'Right Shoulder',
 'Chest',
 'Health Meter',
 'Pelvis',
 'Upper Left Arm',
 'Lower Left Arm',
 'Left Hand',
 'Upper Right Arm',
 'Lower Right Arm',
 'Right Hand')
CogPartNamesSimple = ('Upper Torso',)
SellbotLegFactorySpecMainEntrance = 'Front Entrance'
SellbotLegFactorySpecLobby = 'Lobby'
SellbotLegFactorySpecLobbyHallway = 'Lobby Hallway'
SellbotLegFactorySpecGearRoom = 'Gear Room'
SellbotLegFactorySpecBoilerRoom = 'Boiler Room'
SellbotLegFactorySpecEastCatwalk = 'East Catwalk'
SellbotLegFactorySpecPaintMixer = 'Paint Mixer'
SellbotLegFactorySpecPaintMixerStorageRoom = 'Paint Mixer Storage Room'
SellbotLegFactorySpecWestSiloCatwalk = 'West Silo Catwalk'
SellbotLegFactorySpecPipeRoom = 'Pipe Room'
SellbotLegFactorySpecDuctRoom = 'Duct Room'
SellbotLegFactorySpecSideEntrance = 'Side Entrance'
SellbotLegFactorySpecStomperAlley = 'Stomper Alley'
SellbotLegFactorySpecLavaRoomFoyer = 'Lava Room Foyer'
SellbotLegFactorySpecLavaRoom = 'Lava Room'
SellbotLegFactorySpecLavaStorageRoom = 'Lava Storage Room'
SellbotLegFactorySpecWestCatwalk = 'West Catwalk'
SellbotLegFactorySpecOilRoom = 'Oil Room'
SellbotLegFactorySpecLookout = 'Lookout'
SellbotLegFactorySpecWarehouse = 'Warehouse'
SellbotLegFactorySpecOilRoomHallway = 'Oil Room Hallway'
SellbotLegFactorySpecEastSiloControlRoom = 'East Silo Control Room'
SellbotLegFactorySpecWestSiloControlRoom = 'West Silo Control Room'
SellbotLegFactorySpecCenterSiloControlRoom = 'Center Silo Control Room'
SellbotLegFactorySpecEastSilo = 'East Silo'
SellbotLegFactorySpecWestSilo = 'West Silo'
SellbotLegFactorySpecCenterSilo = 'Center Silo'
SellbotLegFactorySpecEastSiloCatwalk = 'East Silo Catwalk'
SellbotLegFactorySpecWestElevatorShaft = 'West Elevator Shaft'
SellbotLegFactorySpecEastElevatorShaft = 'East Elevator Shaft'
FishBingoBingo = 'BINGO!'
FishBingoVictory = 'VICTORY!!'
FishBingoJackpot = 'JACKPOT!'
FishBingoGameOver = 'GAME OVER'
FishBingoIntermission = 'Intermission\nEnds In:'
FishBingoNextGame = 'Next Game\nStarts In:'
FishBingoTypeNormal = 'Classic'
FishBingoTypeCorners = 'Four Corners'
FishBingoTypeDiagonal = 'Diagonals'
FishBingoTypeThreeway = 'Three Way'
FishBingoTypeBlockout = 'BLOCKOUT!'
SillySaturdayStart = "It's time for Silly Saturday! Saturdays are silly with Fish Bingo and Grand Prix throughout the day!"
SillySaturdayOngoing = 'Welcome! Silly Saturday is currently in progress.'
SillySaturdayEnd = 'Silly Saturday is over. Hope you had fun. See you next week!'
AprilToonsWeekStart = "It's April Toons Week!"
AprilToonsWeekEnd = 'April Toons Week is over. See you next year!'
FishBingoStart = "It's time for Fish Bingo!  Go to any available pier to play!"
FishBingoOngoing = 'Welcome! Fish Bingo is currently in progress.'
FishBingoEnd = 'Hope you had fun playing Fish Bingo.'
FishBingoHelpMain = 'Welcome to Toontown Fish Bingo!  Everyone at the pond works together to fill the card before time runs out.'
FishBingoHelpFlash = 'When you catch a fish, click on one of the flashing squares to mark the card.'
FishBingoHelpNormal = 'This is a Classic Bingo card.  Mark any row down, across or diagonally to win.'
FishBingoHelpDiagonals = 'Mark both of the diagonals to win.'
FishBingoHelpCorners = 'An easy Corners card.  Mark all four corners to win.'
FishBingoHelpThreeway = "Three-way.  Mark both diagonals and the middle row to win.  This one isn't easy!"
FishBingoHelpBingo = 'Bingo!'
FishBingoHelpBlockout = 'Blockout!.  Mark the entire card to win.  You are competing against all the other ponds for a huge jackpot!'
FishBingoOfferToSellFish = 'Your fish bucket is full. Would you like to sell your fish?'
FishBingoJackpotWin = 'Win %s Jellybeans!'
ResistanceToonupMenu = 'Toon-up'
ResistanceToonupItem = '%s Toon-up'
ResistanceToonupItemMax = 'Max'
ResistanceToonupChat = 'Toons of the World, Toon-up!'
ResistanceRestockMenu = 'Gag-up'
ResistanceRestockItem = 'Gag-up %s'
ResistanceRestockItemAll = 'All'
ResistanceRestockChat = 'Toons of the World, Gag-up!'
ResistanceMeritsMenu = 'Merits'
ResistanceMeritsItem = 'Merit-up %s'
ResistanceMeritsChat = 'Toons of the World, Merit-up!'
ResistanceMoneyMenu = 'Jellybeans'
ResistanceMoneyItem = '%s Jellybeans'
ResistanceMoneyChat = 'Toons of the World, Spend Wisely!'
ResistanceTicketsMenu = 'Tickets'
ResistanceTicketsItem = '%s Tickets'
ResistanceTicketsChat = 'Toons of the World, Go Race!'
ResistanceEmote1 = NPCToonNames[9228] + ': Welcome to the Resistance!'
ResistanceEmote2 = NPCToonNames[9228] + ': Use your new emote to identify yourself to other members.'
ResistanceEmote3 = NPCToonNames[9228] + ': Good luck!'
KartUIExit = 'Leave Kart'
KartShop_Cancel = lCancel
KartShop_BuyKart = 'Buy Kart'
KartShop_BuyAccessories = 'Buy Accessories'
KartShop_BuyAccessory = 'Buy Accessory'
KartShop_Cost = 'Cost: %d Tickets'
KartShop_ConfirmBuy = 'Buy the %s for %d Tickets?'
KartShop_NoAvailableAcc = 'No available accessories of this type'
KartShop_FullTrunk = 'Your trunk is full.'
KartShop_ConfirmReturnKart = 'Are you sure you want to return your current Kart?'
KartShop_ConfirmBoughtTitle = 'Congratulations!'
KartShop_NotEnoughTickets = 'Not Enough Tickets!'
KartView_Rotate = 'Rotate'
KartView_Right = 'Right'
KartView_Left = 'Left'
StartingBlock_NotEnoughTickets = "You don't have enough tickets! Try a practice race instead."
StartingBlock_NoBoard = 'Boarding has ended for this race. Please wait for the next race to begin.'
StartingBlock_NoKart = 'You need a kart first! Try asking one of the clerks in the Kart Shop.'
StartingBlock_Occupied = 'This block is currently occupied! Please try another spot.'
StartingBlock_TrackClosed = 'Sorry, this track is closed for remodeling.'
StartingBlock_EnterPractice = 'Would you like to enter a practice race?'
StartingBlock_EnterNonPractice = 'Would you like to enter a %s race for %s tickets?'
StartingBlock_EnterShowPad = 'Would you like to park your car here?'
StartingBlock_KickSoloRacer = 'Toon Battle and Grand Prix races require two or more racers.'
StartingBlock_Loading = 'Goofy Speedway'
LeaderBoard_Time = 'Time'
LeaderBoard_Name = 'Racer Name'
LeaderBoard_Daily = 'Daily Scores'
LeaderBoard_Weekly = 'Weekly Scores'
LeaderBoard_AllTime = 'All Time Best Scores'
RecordPeriodStrings = [LeaderBoard_Daily, LeaderBoard_Weekly, LeaderBoard_AllTime]
KartRace_RaceNames = ['Practice', 'Toon Battle', 'Grand Prix']
from toontown.racing import RaceGlobals
KartRace_Go = 'Go!'
KartRace_Reverse = ' Rev'
KartRace_TrackNames = {RaceGlobals.RT_Speedway_1: 'Screwball Stadium',
 RaceGlobals.RT_Speedway_1_rev: 'Screwball Stadium' + KartRace_Reverse,
 RaceGlobals.RT_Rural_1: 'Rustic Raceway',
 RaceGlobals.RT_Rural_1_rev: 'Rustic Raceway' + KartRace_Reverse,
 RaceGlobals.RT_Urban_1: 'City Circuit',
 RaceGlobals.RT_Urban_1_rev: 'City Circuit' + KartRace_Reverse,
 RaceGlobals.RT_Speedway_2: 'Corkscrew Coliseum',
 RaceGlobals.RT_Speedway_2_rev: 'Corkscrew Coliseum' + KartRace_Reverse,
 RaceGlobals.RT_Rural_2: 'Airborne Acres',
 RaceGlobals.RT_Rural_2_rev: 'Airborne Acres' + KartRace_Reverse,
 RaceGlobals.RT_Urban_2: 'Blizzard Boulevard',
 RaceGlobals.RT_Urban_2_rev: 'Blizzard Boulevard' + KartRace_Reverse}
KartRace_Unraced = 'N/A'
KartDNA_KartNames = {0: 'Cruiser',
 1: 'Roadster',
 2: 'Toon Utility Vehicle'}
KartDNA_AccNames = {1000: 'Air Cleaner',
 1001: 'Four Barrel',
 1002: 'Flying Eagle',
 1003: 'Steer Horns',
 1004: 'Straight Six',
 1005: 'Small Scoop',
 1006: 'Single Overhead',
 1007: 'Medium Scoop',
 1008: 'Single Barrel',
 1009: 'Flugle Horn',
 1010: 'Striped Scoop',
 2000: 'Space Wing',
 2001: 'Patched Spare',
 2002: 'Roll Cage',
 2003: 'Single Fin',
 2004: 'Double-decker Wing',
 2005: 'Single Wing',
 2006: 'Standard Spare',
 2007: 'Single Fin',
 2008: 'sp9',
 2009: 'sp10',
 3000: 'Dueling Horns',
 3001: "Freddie's Fenders",
 3002: 'Cobalt Running Boards',
 3003: 'Cobra Sidepipes',
 3004: 'Straight Sidepipes',
 3005: 'Scalloped Fenders',
 3006: 'Carbon Running Boards',
 3007: 'Wood Running Boards',
 3008: 'fw9',
 3009: 'fw10',
 4000: 'Curly Tailpipes',
 4001: 'Splash Fenders',
 4002: 'Dual Exhaust',
 4003: 'Plain Dual Fins',
 4004: 'Plain Mudflaps',
 4005: 'Quad Exhaust',
 4006: 'Dual Flares',
 4007: 'Mega Exhaust',
 4008: 'Striped Dual Fins',
 4009: 'Bubble Duals Fins',
 4010: 'Striped Mudflaps',
 4011: 'Mickey Mudflaps',
 4012: 'Scalloped Mudflaps',
 5000: 'Turbo',
 5001: 'Moon',
 5002: 'Patched',
 5003: 'Three Spoke',
 5004: 'Paint Lid',
 5005: 'Heart',
 5006: 'Mickey',
 5007: 'Five Bolt',
 5008: 'Daisy',
 5009: 'Basketball',
 5010: 'Hypno',
 5011: 'Tribal',
 5012: 'Gemstone',
 5013: 'Five Spoke',
 5014: 'Knockoff',
 6000: 'Number Five',
 6001: 'Splatter',
 6002: 'Checkerboard',
 6003: 'Flames',
 6004: 'Hearts',
 6005: 'Bubbles',
 6006: 'Tiger',
 6007: 'Flowers',
 6008: 'Lightning',
 6009: 'Angel',
 7000: 'Chartreuse',
 7001: 'Peach',
 7002: 'Bright Red',
 7003: 'Red',
 7004: 'Maroon',
 7005: 'Sienna',
 7006: 'Brown',
 7007: 'Tan',
 7008: 'Coral',
 7009: 'Orange',
 7010: 'Yellow',
 7011: 'Cream',
 7012: 'Citrine',
 7013: 'Lime',
 7014: 'Sea Green',
 7015: 'Green',
 7016: 'Light Blue',
 7017: 'Aqua',
 7018: 'Blue',
 7019: 'Periwinkle',
 7020: 'Royal Blue',
 7021: 'Slate Blue',
 7022: 'Purple',
 7023: 'Lavender',
 7024: 'Pink',
 7025: 'Plum',
 7026: 'Black'}
RaceHoodSpeedway = 'Speedway'
RaceHoodRural = 'Rural'
RaceHoodUrban = 'Urban'
RaceTypeCircuit = 'Tournament'
RaceQualified = 'qualified'
RaceSwept = 'swept'
RaceWon = 'won'
Race = 'race'
Races = 'races'
Total = 'total'
GrandTouring = 'Grand Touring'

def getTrackGenreString(genreId):
    genreStrings = ['Speedway', 'Country', 'City']
    return genreStrings[genreId].lower()


def getTunnelSignName(trackId, padId):
    if trackId == 2 and padId == 0:
        return 'tunne1l_citysign'
    elif trackId == 1 and padId == 0:
        return 'tunnel_countrysign1'
    else:
        genreId = RaceGlobals.getTrackGenre(trackId)
        return 'tunnel%s_%ssign' % (padId + 1, RaceGlobals.getTrackGenreString(genreId))


KartTrophyDescriptions = [str(RaceGlobals.QualifiedRaces[0]) + ' ' + RaceHoodSpeedway + ' ' + Race + ' ' + RaceQualified,
 str(RaceGlobals.QualifiedRaces[1]) + ' ' + RaceHoodSpeedway + ' ' + Races + ' ' + RaceQualified,
 str(RaceGlobals.QualifiedRaces[2]) + ' ' + RaceHoodSpeedway + ' ' + Races + ' ' + RaceQualified,
 str(RaceGlobals.QualifiedRaces[0]) + ' ' + RaceHoodRural + ' ' + Race + ' ' + RaceQualified,
 str(RaceGlobals.QualifiedRaces[1]) + ' ' + RaceHoodRural + ' ' + Races + ' ' + RaceQualified,
 str(RaceGlobals.QualifiedRaces[2]) + ' ' + RaceHoodRural + ' ' + Races + ' ' + RaceQualified,
 str(RaceGlobals.QualifiedRaces[0]) + ' ' + RaceHoodUrban + ' ' + Race + ' ' + RaceQualified,
 str(RaceGlobals.QualifiedRaces[1]) + ' ' + RaceHoodUrban + ' ' + Races + ' ' + RaceQualified,
 str(RaceGlobals.QualifiedRaces[2]) + ' ' + RaceHoodUrban + ' ' + Races + ' ' + RaceQualified,
 str(RaceGlobals.TotalQualifiedRaces) + ' ' + Total + ' ' + Races + ' ' + RaceQualified,
 str(RaceGlobals.WonRaces[0]) + ' ' + RaceHoodSpeedway + ' ' + Race + ' ' + RaceWon,
 str(RaceGlobals.WonRaces[1]) + ' ' + RaceHoodSpeedway + ' ' + Races + ' ' + RaceWon,
 str(RaceGlobals.WonRaces[2]) + ' ' + RaceHoodSpeedway + ' ' + Races + ' ' + RaceWon,
 str(RaceGlobals.WonRaces[0]) + ' ' + RaceHoodRural + ' ' + Race + ' ' + RaceWon,
 str(RaceGlobals.WonRaces[1]) + ' ' + RaceHoodRural + ' ' + Races + ' ' + RaceWon,
 str(RaceGlobals.WonRaces[2]) + ' ' + RaceHoodRural + ' ' + Races + ' ' + RaceWon,
 str(RaceGlobals.WonRaces[0]) + ' ' + RaceHoodUrban + ' ' + Race + ' ' + RaceWon,
 str(RaceGlobals.WonRaces[1]) + ' ' + RaceHoodUrban + ' ' + Races + ' ' + RaceWon,
 str(RaceGlobals.WonRaces[2]) + ' ' + RaceHoodUrban + ' ' + Races + ' ' + RaceWon,
 str(RaceGlobals.TotalWonRaces) + ' ' + Total + ' ' + Races + ' ' + RaceWon,
 str(RaceGlobals.WonCircuitRaces[0]) + ' ' + RaceTypeCircuit + ' ' + Race + ' ' + RaceQualified,
 str(RaceGlobals.WonCircuitRaces[1]) + ' ' + RaceTypeCircuit + ' ' + Races + ' ' + RaceQualified,
 str(RaceGlobals.WonCircuitRaces[2]) + ' ' + RaceTypeCircuit + ' ' + Races + ' ' + RaceQualified,
 str(RaceGlobals.WonCircuitRaces[0]) + ' ' + RaceTypeCircuit + ' ' + Race + ' ' + RaceWon,
 str(RaceGlobals.WonCircuitRaces[1]) + ' ' + RaceTypeCircuit + ' ' + Races + ' ' + RaceWon,
 str(RaceGlobals.WonCircuitRaces[2]) + ' ' + RaceTypeCircuit + ' ' + Races + ' ' + RaceWon,
 str(RaceGlobals.SweptCircuitRaces[0]) + ' ' + RaceTypeCircuit + ' ' + Race + ' ' + RaceSwept,
 str(RaceGlobals.SweptCircuitRaces[1]) + ' ' + RaceTypeCircuit + ' ' + Races + ' ' + RaceSwept,
 str(RaceGlobals.SweptCircuitRaces[2]) + ' ' + RaceTypeCircuit + ' ' + Races + ' ' + RaceSwept,
 GrandTouring,
 str(RaceGlobals.TrophiesPerCup) + ' Kart Racing trophies won! Laff point boost!',
 str(RaceGlobals.TrophiesPerCup * 2) + ' Kart Racing trophies won! Laff point boost!',
 str(RaceGlobals.TrophiesPerCup * 3) + ' Kart Racing trophies won! Laff point boost!']
KartRace_TitleInfo = 'Get Ready to Race'
KartRace_SSInfo = 'Welcome to Screwball Stadium!\nPut the pedal to the metal and hang on tight!\n'
KartRace_CoCoInfo = 'Welcome to Corkscrew Coliseum!\nUse the banked turns to keep your speed up!\n'
KartRace_RRInfo = 'Welcome to Rustic Raceway!\nPlease be kind to the fauna and stay on the track!\n'
KartRace_AAInfo = 'Welcome to Airborne Acres!\nHold onto your hats! It looks bumpy up ahead...\n'
KartRace_CCInfo = 'Welcome to City Circuit!\nWatch out for falling safes as you head to the city!\n'
KartRace_BBInfo = 'Welcome to Blizzard Boulevard!\nWatch your speed. There might be ice out there.\n'
KartRace_GeneralInfo = 'Use Control to throw gags you pick up on the track, and the arrow keys to control your kart.'
KartRace_TrackInfo = {RaceGlobals.RT_Speedway_1: KartRace_SSInfo + KartRace_GeneralInfo,
 RaceGlobals.RT_Speedway_1_rev: KartRace_SSInfo + KartRace_GeneralInfo,
 RaceGlobals.RT_Speedway_2: KartRace_CoCoInfo + KartRace_GeneralInfo,
 RaceGlobals.RT_Speedway_2_rev: KartRace_CoCoInfo + KartRace_GeneralInfo,
 RaceGlobals.RT_Rural_1: KartRace_RRInfo + KartRace_GeneralInfo,
 RaceGlobals.RT_Rural_1_rev: KartRace_RRInfo + KartRace_GeneralInfo,
 RaceGlobals.RT_Rural_2: KartRace_AAInfo + KartRace_GeneralInfo,
 RaceGlobals.RT_Rural_2_rev: KartRace_AAInfo + KartRace_GeneralInfo,
 RaceGlobals.RT_Urban_1: KartRace_CCInfo + KartRace_GeneralInfo,
 RaceGlobals.RT_Urban_1_rev: KartRace_CCInfo + KartRace_GeneralInfo,
 RaceGlobals.RT_Urban_2: KartRace_BBInfo + KartRace_GeneralInfo,
 RaceGlobals.RT_Urban_2_rev: KartRace_BBInfo + KartRace_GeneralInfo}
KartRecordStrings = {RaceGlobals.Daily: 'daily',
 RaceGlobals.Weekly: 'weekly',
 RaceGlobals.AllTime: 'all time'}
KartRace_FirstSuffix = 'st'
KartRace_SecondSuffix = '    nd'
KartRace_ThirdSuffix = '  rd'
KartRace_FourthSuffix = '   th'
KartRace_WrongWay = 'Wrong\nWay!'
KartRace_LapText = 'Lap %s'
KartRace_FinalLapText = 'Final Lap!'
KartRace_Exit = 'Exit Race'
KartRace_NextRace = 'Next Race'
KartRace_Leave = 'Leave Race'
KartRace_Qualified = 'Qualified!'
KartRace_Record = 'Record!'
KartRace_RecordString = 'You have set a new %s record for %s! Your bonus is %s tickets.'
KartRace_Tickets = 'Tickets'
KartRace_Exclamations = '!'
KartRace_Deposit = 'Deposit'
KartRace_Winnings = 'Winnings'
KartRace_Bonus = 'Bonus'
KartRace_RaceTotal = 'Race Total'
KartRace_CircuitTotal = 'Circuit Total'
KartRace_Trophies = 'Trophies'
KartRace_Zero = '0'
KartRace_Colon = ':'
KartRace_TicketPhrase = '%s ' + KartRace_Tickets
KartRace_DepositPhrase = KartRace_Deposit + KartRace_Colon + '\n'
KartRace_QualifyPhrase = 'Qualify:\n'
KartRace_RaceTimeout = 'You timed out of that race.  Your tickets have been refunded.  Keep trying!'
KartRace_RaceTimeoutNoRefund = 'You timed out of that race.  Your tickets have not been refunded because the Grand Prix had already started.  Keep trying!'
KartRace_RacerTooSlow = 'You took too long to finish the race.  Your tickets have not been refunded.  Keep trying!'
KartRace_PhotoFinish = 'Photo Finish!'
KartRace_CircuitPoints = 'Circuit Points'
CircuitRaceStart = 'The Toontown Grand Prix at Goofy Speedway is about to begin!  To win, collect the most points in three consecutive races!'
CircuitRaceOngoing = 'Welcome! The Toontown Grand Prix is currently in progress.'
CircuitRaceEnd = "That's all for today's Toontown Grand Prix at Goofy Speedway.  See you next week!"
TrickOrTreatMsg = 'You have already\nfound this treat!'
WinterCarolingMsg = 'You have already been caroling here!'
LawbotBossTempIntro0 = "Hrmmm, what's on the docket for today?"
LawbotBossTempIntro1 = 'Aha, we have a Toon on trial!'
LawbotBossTempIntro2 = "The prosecution's case is strong..."
LawbotBossTempIntro3 = "Hey, your honorable blindness, you're looking the wrong way!"
LawbotBossTempIntro4 = 'I may be blind...'
LawbotBossTempIntro5 = 'But Justice is NOT!'
LawbotBossTempIntro6 = 'I should have known you Toons would try to upset this trial.'
LawbotBossTempJury1 = 'Jury selection will now commence.'
LawbotBossHowToGetEvidence = 'Touch the witness stand to get evidence.'
LawbotBossTrialChat1 = 'Court is now in session'
LawbotBossHowToThrowPies = 'Press the Delete key to throw the evidence\n at the lawyers or into the scale!'
LawbotBossNeedMoreEvidence = 'You need to get more evidence!'
LawbotBossDefenseWins1 = 'Impossible! The defense won?'
LawbotBossDefenseWins2 = 'No. I declare a mistrial! A new one will be scheduled.'
LawbotBossDefenseWins3 = "Hrrmpphh. I'll be in my chambers."
LawbotBossProsecutionWins = 'I find in favor of the plaintiff!'
LawbotBossReward = 'I award a promotion and the ability to summon Cogs'
LawbotBossLeaveCannon = 'Leave cannon'
LawbotBossPassExam = 'Bah, so you passed the bar exam.'
LawbotBossTaunts = ['%s, I find you in contempt of court!',
 'Objection sustained!',
 'Strike that from the record.',
 'Your appeal has been rejected. I sentence you to sadness!',
 'Order in the court!']
WitnessToonPrepareBattleTwo = "Oh no! They're putting only Cogs on the jury!\x07Quick, use the cannons and shoot some Toon jurors into the jury chairs.\x07We need %d to get a balanced scale."
WitnessToonNoJuror = 'Oh oh, no Toon jurors. This will be a tough trial.'
WitnessToonOneJuror = 'Cool! There is 1 Toon in the jury!'
WitnessToonSomeJurors = 'Cool! There are %d Toons in the jury!'
WitnessToonAllJurors = 'Awesome! All the jurors are Toons!'
WitnessToonPrepareBattleThree = 'Hurry, touch the witness stand to get evidence.\x07Press the Delete key to throw the evidence at the lawyers, or at the defense pan.'
WitnessToonCongratulations = "You did it!  Thank you for a spectacular defense!\x07Here, take these papers the Chief Justice left behind.\x07With it you'll be able to summon Cogs from your Cog Gallery page."
WitnessToonLastPromotion = "\x07Wow, you've reached level %s on your Cog Suit!\x07Cogs don't get promoted higher than that.\x07You can't upgrade your Cog Suit anymore, but you can certainly keep working for the Resistance!"
WitnessToonHPBoost = "\x07You've done a lot of work for the Resistance.\x07The Toon Council has decided to give you another Laff point. Congratulations!"
WitnessToonMaxed = '\x07I see that you have a level %s Cog Suit. Very impressive!\x07On behalf of the Toon Council, thank you for coming back to defend more Toons!'
WitnessToonBonus = 'Wonderful! All the lawyers are stunned. Your evidence weight is %s times heavier for %s seconds'
WitnessToonJuryWeightBonusSingular = {6: 'This is a tough case. You seated %d Toon juror, so your evidence has a bonus weight of %d.',
 7: 'This is a very tough case. You seated %d Toon juror, so your evidence has a bonus weight of %d.',
 8: 'This is the toughest case. You seated %d Toon juror, so your evidence has a bonus weight of %d.'}
WitnessToonJuryWeightBonusPlural = {6: 'This is a tough case. You seated %d Toon jurors, so your evidence has a bonus weight of %d.',
 7: 'This is a very tough case. You seated %d Toon jurors, so your evidence has a bonus weight of %d.',
 8: 'This is the toughest case. You seated %d Toon jurors, so your evidence has a bonus weight of %d.'}
IssueSummons = 'Summon'
SummonDlgTitle = 'Issue a Cog Summon'
SummonDlgButton1 = 'Summon a Cog Building'
SummonDlgButton2 = 'Summon a Cog Invasion'
SummonDlgButton3 = 'Summon a Field Office'
SummonDlgButton4 = 'Summon a Skelecog Invasion'
SummonDlgButton5 = 'Summon a Waiter Invasion'
SummonDlgButton6 = 'Summon a Version 2.0 Invasion'
SummonDlgBuildingConf = 'Would you like to summon a %s to a nearby Toon building?'
SummonDlgInvasionConf = 'Would you like to summon a %s invasion?'
SummonDlgSkelInvasionConf = 'Would you like to summon a %s (Skelecog) invasion?'
SummonDlgWaiterInvasionConf = 'Would you like to summon a %s (Waiter) invasion?'
SummonDlgV2InvasionConf = 'Would you like to summon a Version 2.0 %s invasion?'
SummonDlgNumLeft = 'You have %s left.'
SummonDlgDelivering = 'Delivering Summons...'
SummonDlgBldgSuccess = 'You have successfully summoned the Cogs. %s has agreed to let them temporarily take over %s!'
SummonDlgBldgSuccess2 = 'You have successfully summoned the Cogs. A Shopkeeper has agreed to let them temporarily take over their building!'
SummonDlgBldgBadLoc = 'Sorry, there are no Toon buildings nearby for the Cogs to take over.'
SummonDlgBldgNoCogdos = "Sorry, but you can't summon a Field Office right now. Please try again later."
SummonDlgInvasionSuccess = "You have successfully summoned the Cogs. It's an invasion!"
SummonDlgInvasionBusy = 'A %s cannot be found now.  Try again when the Cog invasion is over.'
SummonDlgInvasionFail = 'Sorry, the Cog invasion has failed.'
SummonDlgShopkeeper = 'The Shopkeeper '
PolarPlaceEffect1 = NPCToonNames[3306] + ': Welcome to Polar Place!'
PolarPlaceEffect2 = NPCToonNames[3306] + ': Try this on for size.'
GreenToonEffectMsg = NPCToonNames[5312] + ': You look Toontastic in green!'
LaserGameMine = 'Skull Finder!'
LaserGameRoll = 'Matching'
LaserGameAvoid = 'Avoid the Skulls'
LaserGameDrag = 'Drag three of a color in a row'
LaserGameDefault = 'Unknown Game'
PinballHiScore = 'High Score:     %s\n'
PinballHiScoreAbbrev = '...'
PinballYourBestScore = 'Your Best Score:\n'
PinballScore = 'Score:            %d x %d = '
PinballScoreHolder = '%s\n'
GagTreeFeather = 'Feather Gag Tree'
GagTreeJugglingBalls = 'Juggling Balls Gag Tree'
StatuaryFountain = 'Fountain'
StatuaryDonald = 'Donald Statue'
StatuaryMinnie = 'Minnie Statue'
StatuaryMickey1 = 'Mickey Statue'
StatuaryMickey2 = 'Mickey Fountain'
StatuaryToon = 'Toon Statue'
StatuaryToonWave = 'Toon Wave Statue'
StatuaryToonVictory = 'Toon Victory Statue'
StatuaryToonCrossedArms = 'Toon Authority Statue'
StatuaryToonThinking = 'Toon Embrace Statue'
StatuaryMeltingSnowman = 'Melting Snowman'
StatuaryMeltingSnowDoodle = 'Melting SnowDoodle'
StatuaryGardenAccelerator = 'Insta-Grow Fertilizer'
AnimatedStatuaryFlappyCog = 'Flappy Cog'
FlowerColorStrings = ['Red',
 'Orange',
 'Violet',
 'Blue',
 'Pink',
 'Yellow',
 'White',
 'Green']
FlowerSpeciesNames = {49: 'Daisy',
 50: 'Tulip',
 51: 'Carnation',
 52: 'Lily',
 53: 'Daffodil',
 54: 'Pansy',
 55: 'Petunia',
 56: 'Rose'}
FlowerFunnyNames = {49: ('School Daisy',
      'Lazy Daisy',
      'Midsummer Daisy',
      'Freshasa Daisy',
      'Whoopsie Daisy',
      'Upsy Daisy',
      'Crazy Daisy',
      'Hazy Dazy'),
 50: ('Onelip', 'Twolip', 'Threelip'),
 51: ('What-in Carnation',
      'Instant Carnation',
      'Hybrid Carnation',
      'Side Carnation',
      'Model Carnation'),
 52: ('Lily-of-the-Alley',
      'Lily Pad',
      'Tiger Lily',
      'Livered Lily',
      'Chili Lily',
      'Silly Lily',
      'Indubitab Lily',
      'Dilly Lilly'),
 53: ('Laff-o-dil',
      'Daffy Dill',
      'Giraff-o-dil',
      'Time and a half-o-dil'),
 54: ('Dandy Pansy',
      'Chim Pansy',
      'Potsen Pansy',
      'Marzi Pansy',
      'Smarty Pansy'),
 55: ('Car Petunia', 'Platoonia'),
 56: ("Summer's Last Rose",
      'Corn Rose',
      'Tinted Rose',
      'Stinking Rose',
      'Istilla Rose')}
FlowerVarietyNameFormat = '%s %s'
FlowerUnknown = '????'
FloweringNewEntry = 'New Entry'
ShovelNameDict = {0: 'Tin',
 1: 'Bronze',
 2: 'Silver',
 3: 'Gold'}
WateringCanNameDict = {0: 'Small',
 1: 'Medium',
 2: 'Large',
 3: 'Huge'}
GardeningPlant = 'Plant'
GardeningWater = 'Water'
GardeningRemove = 'Remove'
GardeningPick = 'Pick'
GardeningFull = 'Full'
GardeningSkill = 'Skill'
GardeningWaterSkill = 'Water Skill'
GardeningShovelSkill = 'Shovel Skill'
GardeningNoSkill = 'No Skill Up'
GardeningPlantFlower = 'Plant\nFlower'
GardeningPlantTree = 'Plant\nTree'
GardeningPlantItem = 'Plant\nItem'
PlantingGuiOk = 'Plant'
PlantingGuiCancel = 'Cancel'
PlantingGuiReset = 'Reset'
GardeningChooseBeans = 'Choose the Jellybeans you want to plant.'
GardeningChooseBeansItem = 'Choose the Jellybeans / item you want to plant.'
GardeningChooseToonStatue = 'Choose the toon you want to create a statue of.'
GardenShovelLevelUp = "Congratulations you've earned a %(shovel)s! You've mastered the %(oldbeans)d bean flower! To progress you should pick %(newbeans)d bean flowers."
GardenShovelSkillLevelUp = "Congratulations! You've mastered the %(oldbeans)d bean flower! To progress you should pick %(newbeans)d bean flowers."
GardenShovelSkillMaxed = "Amazing! You've maxed out your shovel skill!"
GardenWateringCanLevelUp = "Congratulations you've earned a new watering can!"
GardenMiniGameWon = "Congratulations you've watered the plant!"
ShovelTin = 'Tin Shovel'
ShovelSteel = 'Bronze Shovel'
ShovelSilver = 'Silver Shovel'
ShovelGold = 'Gold Shovel'
WateringCanSmall = 'Small Watering Can'
WateringCanMedium = 'Medium Watering Can'
WateringCanLarge = 'Large Watering Can'
WateringCanHuge = 'Huge Watering Can'
BeanColorWords = ('red',
 'green',
 'orange',
 'violet',
 'blue',
 'pink',
 'yellow',
 'cyan',
 'silver')
PlantItWith = ' Plant with %s.'
MakeSureWatered = ' Make sure all your plants are watered first.'
UseFromSpecialsTab = ' Use from the specials tab of the garden page.'
UseSpecial = 'Use Special'
UseSpecialBadLocation = 'You can only use that in your garden.'
UseSpecialSuccess = 'Success! Your watered plants just grew.'
ConfirmWiltedFlower = '%(plant)s is wilted.  Are you sure you want to remove it?  It will not go into your flower basket, nor will you get an increase in skill.'
ConfirmUnbloomingFlower = '%(plant)s is not blooming.  Are you sure you want to remove it?  It will not go into your flower basket, nor will you get an increase in skill.'
ConfirmNoSkillupFlower = 'Are you sure you want to pick the %(plant)s? It will go into your flower basket, but you will NOT get an increase in skill.'
ConfirmSkillupFlower = 'Are you sure you want to pick the %(plant)s?  It will go into your flower basket. You will also get an increase in skill.'
ConfirmMaxedSkillFlower = "Are you sure you want to pick the %(plant)s?  It will go into your flower basket. You will NOT get an increase in skill since you've maximized it already."
ConfirmBasketFull = 'Your flower basket is full. Sell some flowers first.'
ConfirmRemoveTree = 'Are you sure you want to remove the %(tree)s?'
ConfirmWontBeAbleToHarvest = " If you remove this tree, you won't be able to harvest gags from the higher level trees."
ConfirmRemoveStatuary = 'Are you sure you want to permanently delete the %(item)s?'
ResultPlantedSomething = 'Congratulations! You just planted a %s.'
ResultPlantedSomethingAn = 'Congratulations! You just planted an %s.'
ResultPlantedNothing = "That didn't work.  Please try a different combination of Jellybeans."
GardenGagTree = ' Gag Tree'
GardenUberGag = 'Uber Gag'

def getRecipeBeanText(beanTuple):
    retval = ''
    if not beanTuple:
        return retval
    allTheSame = True
    for index in xrange(len(beanTuple)):
        if index + 1 < len(beanTuple):
            if not beanTuple[index] == beanTuple[index + 1]:
                allTheSame = False
                break

    if allTheSame:
        if len(beanTuple) > 1:
            retval = '%d %s Jellybeans' % (len(beanTuple), BeanColorWords[beanTuple[0]])
        else:
            retval = 'a %s Jellybean' % BeanColorWords[beanTuple[0]]
    else:
        retval += 'a'
        maxBeans = len(beanTuple)
        for index in xrange(maxBeans):
            if index == maxBeans - 1:
                retval += ' and %s Jellybean' % BeanColorWords[beanTuple[index]]
            elif index == 0:
                retval += ' %s' % BeanColorWords[beanTuple[index]]
            else:
                retval += ', %s' % BeanColorWords[beanTuple[index]]

    return retval


GardenTextMagicBeans = 'Magic Beans'
GardenTextMagicBeansB = 'Some Other Beans'
GardenSpecialDiscription = 'This text should explain how to use a certain garden special'
GardenSpecialDiscriptionB = 'This text should explain how to use a certain garden special, in yo face foo!'
GardenTrophyAwarded = 'Wow! You collected %s of %s flowers. That deserves a trophy and a Laff boost!'
GardenTrophyNameDict = {0: 'Wheelbarrow',
 1: 'Shovels',
 2: 'Flower',
 3: 'Watering Can',
 4: 'Shark',
 5: 'Swordfish',
 6: 'Killer Whale'}
SkillTooLow = 'Skill\nToo Low'
NoGarden = 'No\nGarden'

def isVowelStart(str):
    retval = False
    if str and len(str) > 0:
        vowels = ['A',
         'E',
         'I',
         'O',
         'U']
        firstLetter = str.upper()[0:1]
        if firstLetter in vowels:
            retval = True
    return retval


def getResultPlantedSomethingSentence(flowerName):
    if isVowelStart(flowerName):
        retval = ResultPlantedSomethingAn % flowerName
    else:
        retval = ResultPlantedSomething % flowerName
    return retval

VineGameTitle = 'Jungle Vines'
VineGameInstructions = 'Get to the rightmost vine in time. Press Up or Down to climb the vine.  Press Left or Right to change facing and jump.  The lower you are on the vine, the faster you jump off.  Collect the bananas if you can, but avoid the bats and spiders.'
ValentinesDayStart = "Happy ValenToon's Day!"
ValentinesDayEnd = "That's all for ValenToon's Day!"
GolfCourseNames = {0: 'Walk In The Par',
 1: 'Hole Some Fun',
 2: 'The Hole Kit And Caboodle'}
GolfHoleNames = {0: 'Whole In Won',
 1: 'No Putts About It',
 2: 'Down The Hatch',
 3: 'Seeing Green',
 4: 'Hot Links',
 5: 'Peanut Putter',
 6: 'Swing-A-Long',
 7: 'Afternoon Tee',
 8: 'Hole In Fun',
 9: 'Rock And Roll In',
 10: 'Bogey Nights',
 11: 'Tea Off Time',
 12: 'Holey Mackerel!',
 13: 'One Little Birdie',
 14: 'At The Drive In',
 15: 'Swing Time',
 16: 'Hole On The Range',
 17: 'Second Wind',
 18: 'Whole In Won-2',
 19: 'No Putts About It-2',
 20: 'Down The Hatch-2',
 21: 'Seeing Green-2',
 22: 'Hot Links-2',
 23: 'Peanut Putter-2',
 24: 'Swing-A-Long-2',
 25: 'Afternoon Tee-2',
 26: 'Hole In Fun-2',
 27: 'Rock And Roll In-2',
 28: 'Bogey Nights-2',
 29: 'Tea Off Time-2',
 30: 'Holey Mackerel!-2',
 31: 'One Little Birdie-2',
 32: 'At The Drive In-2',
 33: 'Swing Time-2',
 34: 'Hole On The Range-2',
 35: 'Second Wind-2'}
GolfHoleInOne = 'Hole In One'
GolfCondor = 'Condor'
GolfAlbatross = 'Albatross'
GolfEagle = 'Eagle'
GolfBirdie = 'Birdie'
GolfPar = 'Par'
GolfBogey = 'Bogey'
GolfDoubleBogey = 'Double Bogey'
GolfTripleBogey = 'Triple Bogey'
GolfShotDesc = {-4: GolfCondor,
 -3: GolfAlbatross,
 -2: GolfEagle,
 -1: GolfBirdie,
 0: GolfPar,
 1: GolfBogey,
 2: GolfDoubleBogey,
 3: GolfTripleBogey}
from toontown.golf import GolfGlobals
CoursesCompleted = 'Courses Completed'
CoursesUnderPar = 'Courses Under Par'
HoleInOneShots = 'Hole In One Shots'
EagleOrBetterShots = 'Eagle Or Better Shots'
BirdieOrBetterShots = 'Birdie Or Better Shots'
ParOrBetterShots = 'Par Or Better Shots'
MultiPlayerCoursesCompleted = 'Multiplayer Courses Completed'
TwoPlayerWins = 'Two Player Wins'
ThreePlayerWins = 'Three Player Wins'
FourPlayerWins = 'Four Player Wins'
CourseZeroWins = GolfCourseNames[0] + ' Wins'
CourseOneWins = GolfCourseNames[1] + ' Wins'
CourseTwoWins = GolfCourseNames[2] + ' Wins'
GolfHistoryDescriptions = [CoursesCompleted,
 CoursesUnderPar,
 HoleInOneShots,
 EagleOrBetterShots,
 BirdieOrBetterShots,
 ParOrBetterShots,
 MultiPlayerCoursesCompleted,
 CourseZeroWins,
 CourseOneWins,
 CourseTwoWins]
GolfTrophyDescriptions = [str(GolfGlobals.TrophyRequirements[GolfGlobals.CoursesCompleted][0]) + ' ' + CoursesCompleted,
 str(GolfGlobals.TrophyRequirements[GolfGlobals.CoursesCompleted][1]) + ' ' + CoursesCompleted,
 str(GolfGlobals.TrophyRequirements[GolfGlobals.CoursesCompleted][2]) + ' ' + CoursesCompleted,
 str(GolfGlobals.TrophyRequirements[GolfGlobals.CoursesUnderPar][0]) + ' ' + CoursesUnderPar,
 str(GolfGlobals.TrophyRequirements[GolfGlobals.CoursesUnderPar][1]) + ' ' + CoursesUnderPar,
 str(GolfGlobals.TrophyRequirements[GolfGlobals.CoursesUnderPar][2]) + ' ' + CoursesUnderPar,
 str(GolfGlobals.TrophyRequirements[GolfGlobals.HoleInOneShots][0]) + ' ' + HoleInOneShots,
 str(GolfGlobals.TrophyRequirements[GolfGlobals.HoleInOneShots][1]) + ' ' + HoleInOneShots,
 str(GolfGlobals.TrophyRequirements[GolfGlobals.HoleInOneShots][2]) + ' ' + HoleInOneShots,
 str(GolfGlobals.TrophyRequirements[GolfGlobals.EagleOrBetterShots][0]) + ' ' + EagleOrBetterShots,
 str(GolfGlobals.TrophyRequirements[GolfGlobals.EagleOrBetterShots][1]) + ' ' + EagleOrBetterShots,
 str(GolfGlobals.TrophyRequirements[GolfGlobals.EagleOrBetterShots][2]) + ' ' + EagleOrBetterShots,
 str(GolfGlobals.TrophyRequirements[GolfGlobals.BirdieOrBetterShots][0]) + ' ' + BirdieOrBetterShots,
 str(GolfGlobals.TrophyRequirements[GolfGlobals.BirdieOrBetterShots][1]) + ' ' + BirdieOrBetterShots,
 str(GolfGlobals.TrophyRequirements[GolfGlobals.BirdieOrBetterShots][2]) + ' ' + BirdieOrBetterShots,
 str(GolfGlobals.TrophyRequirements[GolfGlobals.ParOrBetterShots][0]) + ' ' + ParOrBetterShots,
 str(GolfGlobals.TrophyRequirements[GolfGlobals.ParOrBetterShots][1]) + ' ' + ParOrBetterShots,
 str(GolfGlobals.TrophyRequirements[GolfGlobals.ParOrBetterShots][2]) + ' ' + ParOrBetterShots,
 str(GolfGlobals.TrophyRequirements[GolfGlobals.MultiPlayerCoursesCompleted][0]) + ' ' + MultiPlayerCoursesCompleted,
 str(GolfGlobals.TrophyRequirements[GolfGlobals.MultiPlayerCoursesCompleted][1]) + ' ' + MultiPlayerCoursesCompleted,
 str(GolfGlobals.TrophyRequirements[GolfGlobals.MultiPlayerCoursesCompleted][2]) + ' ' + MultiPlayerCoursesCompleted,
 str(GolfGlobals.TrophyRequirements[GolfGlobals.CourseZeroWins][0]) + ' ' + CourseZeroWins,
 str(GolfGlobals.TrophyRequirements[GolfGlobals.CourseZeroWins][1]) + ' ' + CourseZeroWins,
 str(GolfGlobals.TrophyRequirements[GolfGlobals.CourseZeroWins][2]) + ' ' + CourseZeroWins,
 str(GolfGlobals.TrophyRequirements[GolfGlobals.CourseOneWins][0]) + ' ' + CourseOneWins,
 str(GolfGlobals.TrophyRequirements[GolfGlobals.CourseOneWins][1]) + ' ' + CourseOneWins,
 str(GolfGlobals.TrophyRequirements[GolfGlobals.CourseOneWins][2]) + ' ' + CourseOneWins,
 str(GolfGlobals.TrophyRequirements[GolfGlobals.CourseTwoWins][0]) + ' ' + CourseTwoWins,
 str(GolfGlobals.TrophyRequirements[GolfGlobals.CourseTwoWins][1]) + ' ' + CourseTwoWins,
 str(GolfGlobals.TrophyRequirements[GolfGlobals.CourseTwoWins][2]) + ' ' + CourseTwoWins]
GolfCupDescriptions = [str(GolfGlobals.TrophiesPerCup) + ' Trophies won', str(GolfGlobals.TrophiesPerCup * 2) + ' Trophies won', str(GolfGlobals.TrophiesPerCup * 3) + ' Trophies won']
GolfAvReceivesHoleBest = '%(name)s scored a new hole best at %(hole)s!'
GolfAvReceivesCourseBest = '%(name)s scored a new course best at %(course)s!'
GolfAvReceivesCup = '%(name)s receives the %(cup)s cup!!  Laff point boost!'
GolfAvReceivesTrophy = '%(name)s receives the %(award)s trophy!!'
GolfRanking = 'Ranking: \n'
GolfPowerBarText = '%(power)s%%'
GolfChooseTeeInstructions = 'Press Left or Right to change tee spot.\nPress Control to select.'
GolfWarningMustSwing = 'Warning: You must press Control on your next swing.'
GolfAimInstructions = 'Press Left or Right to aim.\nPress and hold Control to swing.'
GolferExited = '%s has left the golf course.'
GolfPowerReminder = 'Hold Down Control Longer to\nHit the Ball Further'
GolfPar = 'Par'
GolfHole = 'Hole'
GolfTotal = 'Total'
GolfExitCourse = 'Exit Course'
GolfUnknownPlayer = '???'
GolfPageTitle = 'Golf'
GolfPageTitleCustomize = 'Golf Customizer'
GolfPageTitleRecords = 'Personal Best Records'
GolfPageTitleTrophy = 'Golfing Trophies'
GolfPageCustomizeTab = 'Customize'
GolfPageRecordsTab = 'Records'
GolfPageTrophyTab = 'Trophy'
GolfPageTickets = 'Tickets : '
GolfPageConfirmDelete = 'Delete Accessory?'
GolfTrophyTextDisplay = 'Trophy %(number)s : %(desc)s'
GolfCupTextDisplay = 'Cup %(number)s : %(desc)s'
GolfCurrentHistory = 'Current %(historyDesc)s : %(num)s'
GolfTieBreakWinner = '%(name)s wins the random tie breaker!'
GolfSeconds = ' -  %(time).2f seconds'
GolfTimeTieBreakWinner = '%(name)s wins the total aiming time tie breaker!!!'
MoreXpHolidayStart = "It's Fun Friday! Earn double gag experience!"
MoreXpHolidayOngoing = 'Welcome! Fun Friday is currently in progress.'
MoreXpHolidayEnd = 'Fun Friday has ended. See you next week!'
MoreMeritsHolidayStart = "It's Merit Monday! Merit multiplier is doubled!"
MoreMeritsHolidayOngoing = 'Welcome! Merit Monday is currently in progress.'
MoreMeritsHolidayEnd = 'Merit Monday has ended. See you next week!'
TaxDayHolidayStart = 'Today is Tax Day! Beware of the Number Crunchers!'
TaxDayHolidayOngoing = 'Today is Tax Day! Beware of the Number Crunchers!'
TaxDayHolidayEnd = 'Tax Day is over! We beat the Number Crunchers!'
JellybeanDayHolidayStart = "It's Jellybean Day! Get Double Jellybean rewards at Parties!"
JellybeanDayHolidayEnd = "That's all for Jellybean Day. See you next year."
PartyRewardDoubledJellybean = 'Double Jellybeans!'
GrandPrixWeekendHolidayStart = "It's Grand Prix Weekend at Goofy Speedway! Toons collect the most points in three consecutive races."
GrandPrixWeekendHolidayEnd = "That's all for Grand Prix Weekend. See you next year."
KartRace_DoubleTickets = 'Double Tickets'
SellbotNerfHolidayStart = 'Operation: Storm Sellbot is happening now! Battle the VP today!'
SellbotNerfHolidayEnd = 'Operation: Storm Sellbot has ended. Great work, Toons!'
LawbotNerfHolidayStart = 'Operation: Lawbots Lose is happening now! Battle the CJ today!'
LawbotNerfHolidayEnd = 'Operation: Lawbots Lose has ended. Great work, Toons!'
CashbotNerfHolidayStart = 'Operation: Cashbot Chaos is happening now! Battle the CFO today!'
CashbotNerfHolidayEnd = 'Opeation: Cashbot Chaos has ended. Great work, Toons!'
BossbotNerfHolidayStart = 'Operation: Besiege Bossbot is happening now! Battle the CEO today!'
BossbotNerfHolidayEnd = 'Operation: Besiege Bossbot has ended. Great work, Toons!'
JellybeanTrolleyHolidayStart = 'Double Bean Days for Trolley Games have begun!'
JellybeanTrolleyHolidayEnd = 'Double Bean Days for Trolley Games have ended!'
JellybeanFishingHolidayStart = 'Double Bean Days for Fishing have begun!'
JellybeanFishingHolidayEnd = 'Double Bean Days for Fishing have ended!'
JellybeanPartiesHolidayStart = "It's Jellybean Week! Get Double Jellybean rewards!"
JellybeanPartiesHolidayEnd = "That's all for Jellybean Week. See you next year."
JellybeanMonthHolidayStart = 'Celebrate Toontown with double beans, Cattlelog items and silly surprises!'
BankUpgradeHolidayStart = 'Something Toontastic happened to your Jellybean Bank!'
HalloweenPropsHolidayStart = "It's Halloween in Toontown!"
HalloweenPropsHolidayEnd = 'Halloween has ended. Boo!'
SpookyPropsHolidayStart = 'Silly Meter spins Toontown into spooky mode!'
BlackToonHolidayStart = 'Create a free Black Toon - today only!'
BlackToonHolidayEnd = 'Black Toon day has ended!'
TopToonsMarathonStart = "The Top Toons New Year's Day Marathon has begun!"
TopToonsMarathonEnd = "The Top Toons New Year's Day Marathon has ended."
WinterDecorationsStart = "It's Winter Holiday time in Toontown!"
WinterDecorationsEnd = 'Winter Holiday is over - Happy New Year!'
WackyWinterDecorationsStart = 'Brrr! Silly Meter goes from silly to chilly!'
WinterCarolingStart = 'Caroling has come to Toontown. Sing for your Snowman Head - see the Blog for details!'
WinterCarolingEnd = 'Caroling is over. See you next year.'
TrickOrTreatStart = 'Happy Halloween! Trick or treat throughout Toontown to get a nifty Halloween pumpkin head reward!'
TrickOrTreatEnd = 'Halloween is over. See you next year.'
ExpandedClosetsStart = 'Attention Toons: For a limited time, Members can purchase the new 50 item Closet from the Cattlelog for the low price of 50 Jellybeans!'
KartingTicketsHolidayStart = 'Get double tickets from Practice races at Goofy Speedway today!'
IdesOfMarchStart = 'Toons go GREEN!'
IdesOfMarchEnd = 'Hope you had fun being green.'
LogoutForced = 'You have done something wrong\n and are being logged out automatically,\n additionally your account may be frozen.\n Try going on a walk outside, it is fun.'
CountryClubToonEnterElevator = '%s \nhas jumped in the golf kart.'
CountryClubBossConfrontedMsg = '%s is battling the Club President!'
ElevatorBlockedRoom = 'All challenges must be defeated first.'
MolesLeft = 'Moles Left: %d'
MolesInstruction = 'Mole Stomp!\nJump on the red moles!'
MolesFinished = 'Mole Stomp successful!'
MolesPityWin = 'Stomp Failed! But the moles left.'
MolesRestarted = 'Stomp Failed! Restarting...'
BustACogInstruction = 'Remove the cog ball!'
BustACogExit = 'Exit for Now'
BustACogHowto = 'How to Play'
BustACogFailure = 'Out of Time!'
BustACogSuccess = 'Success!'
GolfGreenGameScoreString = 'Puzzles Left: %s'
GolfGreenGamePlayerScore = 'Solved %s'
GolfGreenGameBonusGag = 'You won %s!'
GolfGreenGameGotHelp = '%s solved a Puzzle!'
GolfGreenGameDirections = 'Shoot balls using the the mouse\n\n\nMatching three of a color causes the balls to fall\n\n\nRemove all Cog balls from the board'
enterHedgeMaze = 'Race through the Hedge Maze\n for a laff bonus!'
toonFinishedHedgeMaze = '%s \n  finished in %s place!'
hedgeMazePlaces = ['first',
 'second',
 'third',
 'Fourth']
mazeLabel = 'Maze Race!'
BoardingPartyReadme = 'Boarding Group?'
BoardingGroupHide = 'Hide'
BoardingGroupShow = 'Show Boarding Group'
BoardingPartyInform = 'Create an elevator Boarding Group by clicking on another Toon and Inviting them.\nIn this area Boarding Groups cannot have more than %s Toons.'
BoardingPartyTitle = 'Boarding Group'
BoardingPartyTitleMerge = 'Merge Group'
QuitBoardingPartyLeader = 'Disband'
QuitBoardingPartyNonLeader = 'Leave'
QuitBoardingPartyConfirm = 'Are you sure you want to quit this Boarding Group?'
BoardcodeMissing = 'Something went wrong; try again later.'
BoardcodePromotionLeader = 'Your group cannot board because you do not have enough promotion merits.'
BoardcodePromotionNonLeaderSingular = 'Your group cannot board because %s does not have enough promotion merits.'
BoardcodePromotionNonLeaderPlural = 'Your group cannot board because %s do not have enough promotion merits.'
BoardcodeSpace = 'Your group cannot board because there is not enough space.'
BoardcodeBattleLeader = 'Your group cannot board because you are in battle.'
BoardcodeBattleNonLeaderSingular = 'Your group cannot board because %s is in battle.'
BoardcodeBattleNonLeaderPlural = 'Your group cannot board because %s are in battle.'
BoardingInvitePromotionInviter = 'You need to earn a promotion before being a member of this Boarding Group.'
BoardingInvitePromotionInvitee = '%s needs to earn a promotion before being a member of this Boarding Group.'
BoardingInviteeInDiffGroup = '%s is already in a different Boarding Group.'
BoardingInviteeInKickOutList = '%s had been removed by your leader. Only the leader can re-invite removed members.'
BoardingInviteePendingIvite = '%s has a pending invite; try again later.'
BoardingInviteeInElevator = '%s is currently busy; try again later.'
BoardingInviteGroupFull = 'Your Boarding Group is already full.'
BoardingGroupsTooLarge = '%s is already in a different Boarding Group that is too large to merge.'
BoardingAlreadyInGroup = 'You cannot accept this invitation because you are part of another Boarding Group.'
BoardingGroupAlreadyFull = 'You cannot accept this invitation because the group is already full.'
BoardingKickOutConfirm = 'Are you sure you want to remove %s?'
BoardingPendingInvite = 'You need to deal with the\n pending invitation first.'
BoardingCannotLeaveZone = 'You cannot leave this area because you are part of a Boarding Group.'
BoardingInviteeMessage = '%s would like you to join their Boarding Group.'
BoardingInviteeMergeMessage = '%s would like you merge with their Boarding Group.'
BoardingInvitingMessage = 'Inviting %s to your Boarding Group.'
BoardingInvitationRejected = '%s has rejected to join your Boarding Group.'
BoardingMessageKickedOut = 'You have been removed from the Boarding Group.'
BoardingMessageInvited = '%s has invited %s to the Boarding Group.'
BoardingMessageLeftGroup = '%s has left the Boarding Group.'
BoardingMessageGroupDissolved = 'Your Boarding Group was disbanded by the group leader.'
BoardingMessageGroupDisbandedGeneric = 'Your Boarding Group was disbanded.'
BoardingMessageInvitationFailed = '%s tried to invite you to their Boarding Group.'
BoardingMessageGroupFull = '%s tried to accept your invitation but your group was full.'
BoardingGo = 'GO'
BoardingCancelGo = 'Click Again to\nCancel Go'
And = 'and'
BoardingGoingTo = 'Going To:'
BoardingTimeWarning = 'Boarding the elevator in '
BoardingMore = 'more'
BoardingGoShow = 'Going to\n%s in '
BoardingGoPreShow = 'Confirming...'
BossbotBossName = 'C.E.O.'
BossbotRTWelcome = 'You toons will need different disguises.'
BossbotRTRemoveSuit = 'First take off your cog suits...'
BossbotRTFightWaiter = 'and then fight these waiters.'
BossbotRTWearWaiter = "Good job! Now put on the waiters' clothes."
BossbotBossPreTwo1 = "What's taking so long?"
BossbotBossPreTwo2 = 'Get cracking and serve my banquet!'
BossbotRTServeFood1 = 'Hehe, serve the food I place on these conveyor belts.'
BossbotRTServeFood2 = 'If you serve a cog three times in a row it will explode.'
BossbotPhase3Speech1 = "What's happening here?!"
BossbotPhase3Speech2 = 'These waiters are toons!'
BossbotPhase3Speech3 = 'Get them!!!'
BossbotPhase4Speech1 = 'Hrrmmpph. When I need a job done right...'
BossbotPhase4Speech2 = "I'll do it myself."
BossbotRTPhase4Speech1 = 'Good job! Now squirt the C.E.O. with the water on the tables...'
BossbotRTPhase4Speech2 = 'or use golf balls to slow him down and deal damage.'
BossbotPitcherLeave = 'Leave Bottle'
BossbotPitcherLeaving = 'Leaving Bottle'
BossbotPitcherAdvice = 'Use the left and right keys to rotate.\nHold down Ctrl increase power.\nRelease Ctrl to fire.'
BossbotGolfSpotLeave = 'Leave Golf Ball'
BossbotGolfSpotLeaving = 'Leaving Golf Ball'
BossbotGolfSpotAdvice = 'Use the left and right keys to rotate.\nCtrl to fire.'
BossbotRewardSpeech1 = "No! The Chairman won't like this."
BossbotRewardSpeech2 = 'Arrrggghhh!!!!'
BossbotRTCongratulations = "You did it!  You've demoted the C.E.O.!\x07Here, take these pink slips the C.E.O. left behind.\x07With it you'll be able to fire Cogs in a battle."
BossbotRTHPBoost = "\x07You've done a lot of work for the Resistance.\x07The Toon Council has decided to give you another Laff point. Congratulations!"
BossbotRTMaxed = '\x07I see that you have a level %s Cog Suit. Very impressive!\x07On behalf of the Toon Council, thank you for coming back to defend more Toons!'
BossbotRTLastPromotion = "\x07Wow, you've reached level %s on your Cog Suit!\x07Cogs don't get promoted higher than that.\x07You can't upgrade your Cog Suit anymore, but you can certainly keep working for the Resistance!"
GolfAreaAttackTaunt = 'Fore!'
OvertimeAttackTaunts = ["It's time to reorganize.", "Now let's downsize."]
ElevatorBossBotBoss = 'Bossbot Clubhouse'
ElevatorBossBotCourse0 = 'The Front Two'
ElevatorBossBotCourse1 = 'The Middle Four'
ElevatorBossBotCourse2 = 'The Back Six'
ElevatorCashBotBoss = 'Cashbot Vault'
ElevatorCashBotMint0 = 'Coin Mint'
ElevatorCashBotMint1 = 'Dollar Mint'
ElevatorCashBotMint2 = 'Bullion Mint'
ElevatorSellBotBoss = 'Sellbot Towers'
ElevatorSellBotFactory0 = 'Front Entrance'
ElevatorSellBotFactory1 = 'Side Entrance'
ElevatorSellBotFactory2 = 'Megacorp Entrance'
ElevatorLawBotBoss = 'Lawbot Courthouse'
ElevatorLawBotCourse0 = 'Office A'
ElevatorLawBotCourse1 = 'Office B'
ElevatorLawBotCourse2 = 'Office C'
ElevatorLawBotCourse3 = 'Office D'
ElevatorCogTower = 'Cog Battle Tower'
IceGameTitle = 'Ice Slide'
IceGameInstructions = 'Get as close to the center by the end of the second round. Use arrow keys to change direction and force. Press Ctrl to launch your toon.  Hit barrels for extra points and avoid the TNT!'
IceGameInstructionsNoTnt = 'Get as close to the center by the end of the second round. Use arrow keys to change direction and force. Press Ctrl to launch your toon.  Hit barrels for extra points.'
IceGameInfo = 'Match %(curMatch)d/%(numMatch)d, Round %(curRound)d/%(numRound)d'
IceGameControlKeyWarning = 'Remember to press the Ctrl key!'
PicnicTableJoinButton = 'Join'
PicnicTableObserveButton = 'Observe'
PicnicTableCancelButton = 'Cancel'
PicnicTableTutorial = 'How To Play'
PicnicTableMenuTutorial = 'What game do you want to learn?'
PicnicTableMenuSelect = 'What game do you want to play?'
ChineseCheckersGetUpButton = 'Get Up'
ChineseCheckersStartButton = 'Start Game'
ChineseCheckersQuitButton = 'Quit Game'
ChineseCheckersIts = "It's "
ChineseCheckersYourTurn = 'Your Turn'
ChineseCheckersGreenTurn = "Green's Turn"
ChineseCheckersYellowTurn = "Yellow's Turn"
ChineseCheckersPurpleTurn = "Purple's Turn"
ChineseCheckersBlueTurn = "Blue's Turn"
ChineseCheckersPinkTurn = "Pink's Turn"
ChineseCheckersRedTurn = "Red's Turn"
ChineseCheckersColorG = 'You are Green'
ChineseCheckersColorY = 'You are Yellow'
ChineseCheckersColorP = 'You are Purple'
ChineseCheckersColorB = 'You are Blue'
ChineseCheckersColorPink = 'You are Pink'
ChineseCheckersColorR = 'You are Red'
ChineseCheckersColorO = 'You are Observing'
ChineseCheckersYouWon = 'You just won a game of Chinese Checkers!'
ChineseCheckers = 'Chinese Checkers.'
ChineseCheckersGameOf = ' has just won a game of '
ChineseTutorialTitle1 = 'Objective'
ChineseTutorialTitle2 = 'How to Play'
ChineseTutorialPrev = 'Previous Page'
ChineseTutorialNext = 'Next Page'
ChineseTutorialDone = 'Done'
ChinesePage1 = 'The goal of Chinese Checkers is to be the first  toon to move all of your marbles from the bottom triangle across the board and into the triangle at the top. The first toon to do so wins!'
ChinesePage2 = 'Toons take turns moving any marble of their own color.  A marble can move into an adjacent hole or it can hop over other marbles. Hops must go over a marble and end in an empty hole. It is possible to chain hops together for longer moves!'
CheckersPage1 = 'The goal of Checkers is to leave the opponent without any possible moves. To do this you can either capture all of his peices or block them in such that he has no available moves.'
CheckersPage2 = 'Toons take turns moving any peice of their own color. A peice can move one square diagonal and forward. A peice can only move into a square that is not occupied by another peice. Kings follow the same rules but are allowed to move backwards.'
CheckersPage3 = 'To capture an opponents peice your peice must jump over it diagonally into the vacant square beyond it. If you have any jump moves during a turn, you must do one of them. You can chain jump moves together as long as it is with the same peice.'
CheckersPage4 = 'A peice becomes a king when it reaches the last row on the board. A peice that has just become a king cannot continue jumping until the next turn. Additionally, kings are allowed to move all directions and are allowed to change directions while jumping.'
CheckersGetUpButton = 'Get Up'
CheckersStartButton = 'Start Game'
CheckersQuitButton = 'Quit Game'
CheckersIts = "It's "
CheckersYourTurn = 'Your Turn'
CheckersWhiteTurn = "White's Turn"
CheckersBlackTurn = "Black's Turn"
CheckersColorWhite = 'You are White'
CheckersColorBlack = 'You are Black'
CheckersObserver = 'You are Observing'
RegularCheckers = 'Checkers.'
RegularCheckersGameOf = ' has just won a game of '
RegularCheckersYouWon = 'You just won a game of Checkers!'
GardenDropTitle = 'Garden Drop'
GardenDropExitGame = 'Exit Mini Game'
GardenDropHelpTitle = 'Instructions:'
GardenDropInstructions = "Match the ghost balls with the normal balls! But beware of the cog ball, it will try to block you off!"
GardenDropBackToGame = "Back to Game"
GardenDropButtonTitle = 'Garden\nDrop'
GardenDropCongradulations = 'Super Congratulations!!'
GardenDropProgressLevels = "Click 'Next' to go to the next level!"
GardenDropWinGame = 'You have won the Garden Drop Game!'
GardenDropExit = 'Exit'
MailNotifyNewItems = "You've got mail!"
MailNewMailButton = 'Mail'
MailSimpleMail = 'Note'
MailFromTag = 'Note From: %s'
AwardNotifyNewItems = 'You have a new award in your mailbox!'
AwardNotifyOldItems = 'There are still awards waiting in your mailbox for you to pick up!'
InviteInvitation = 'the invitation'
InviteAcceptInvalidError = 'The invitation is no longer valid.'
InviteAcceptPartyInvalid = 'That party has been cancelled.'
InviteAcceptAllOk = 'The host has been informed of your reply.'
InviteRejectAllOk = 'The host has been informed that you declined the invitation.'
Months = {1: 'JANUARY',
 2: 'FEBRUARY',
 3: 'MARCH',
 4: 'APRIL',
 5: 'MAY',
 6: 'JUNE',
 7: 'JULY',
 8: 'AUGUST',
 9: 'SEPTEMBER',
 10: 'OCTOBER',
 11: 'NOVEMBER',
 12: 'DECEMBER'}
DayNames = ('Monday',
 'Tuesday',
 'Wednesday',
 'Thursday',
 'Friday',
 'Saturday',
 'Sunday')
DayNamesAbbrev = ('MON',
 'TUE',
 'WED',
 'THU',
 'FRI',
 'SAT',
 'SUN')
SummerFireworksStart = 'Celebrate Summer with a fireworks show every hour in each playground!'
SummerFireworksEnd = 'Summer Fireworks are over. Hope you had fun.'
NewYearFireworksStart = 'Happy New Year! Enjoy a fireworks show every hour in each playground!'
NewYearFireworksEnd = 'New Year Fireworks are over. See you next year!'
HolidayNamesInCalendar = {1: ('Summer Fireworks', 'Celebrate Summer with a fireworks show every hour in each playground!'),
 2: ('New Year Fireworks', 'Happy New Year! Enjoy a fireworks show every hour in each playground!'),
 3: ('Halloween', 'Happy Halloween! Trick or treat throughout Toontown to get a nifty Halloween pumpkin head reward!'),
 4: ('Winter Holiday', 'Celebrate the Winter Holiday with Toontastic decorations, party and Cattlelog items, and more!'),
 5: ('Skelecog Invasion', 'Stop the Skelecogs from invading Toontown!'),
 6: ('Mr. Hollywood Invasion', 'Stop the Mr. Hollywood Cogs from invading Toontown!'),
 8: ('Toon Species Election', 'Vote on the new Toon species! Will it be Goat? Will it be Pig?'),
 9: ('Black Toon Day', 'Create a free Toontastic Black Toon - today only!'),
 16: ('Grand Prix', 'Grand Prix Monday at Goofy Speedway! To win, collect the most points in three consecutive races!'),
 17: ('Fish Bingo', 'Fish Bingo Wednesday! Everyone at the pond works together to complete the card before time runs out.'),
 18: ('Silly Saturdays', 'Saturdays are silly with Fish Bingo and Grand Prix throughout the day!'),
 24: ('Ides of March', 'Beware the Ides of March! Stop the Backstabber Cogs from invading Toontown!'),
 25: ('Fun Friday', 'Fridays are fun with double gag experience!'),
 26: ('Halloween Decor', 'Celebrate Halloween as spooky trees and streetlights transform Toontown!'),
 27: ('Merit Monday', 'Mondays are marvelous with a doubled merit multiplier!'),
 28: ('Winter Invasion', 'The sellbots are on the loose spreading their cold sales tactics!'),
 29: ("April Toons' Week", "Celebrate April Toons' Week - a holiday built by Toons for Toons!"),
 33: ('Sellbot Surprise 1', 'Sellbot Surprise! Stop the Cold Caller Cogs from invading Toontown!'),
 34: ('Sellbot Surprise 2', 'Sellbot Surprise! Stop the Name Dropper Cogs from invading Toontown!'),
 35: ('Sellbot Surprise 3', 'Sellbot Surprise! Stop the Gladhander Cogs from invading Toontown!'),
 36: ('Sellbot Surprise 4', 'Sellbot Surprise! Stop the Mover & Shaker Cogs from invading Toontown!'),
 37: ('A Cashbot Conundrum 1', 'A Cashbot Conundrum. Stop the Short Change Cogs from invading Toontown!'),
 38: ('A Cashbot Conundrum 2', 'A Cashbot Conundrum. Stop the Penny Pincher Cogs from invading Toontown!'),
 39: ('A Cashbot Conundrum 3', 'A Cashbot Conundrum. Stop the Bean Counter Cogs from invading Toontown!'),
 40: ('A Cashbot Conundrum 4', 'A Cashbot Conundrum. Stop the Number Cruncher Cogs from invading Toontown!'),
 41: ('The Lawbot Gambit 1', 'The Lawbot Gambit. Stop the Bottomfeeder Cogs from invading Toontown!'),
 42: ('The Lawbot Gambit 2', 'The Lawbot Gambit. Stop the Double Talker Cogs from invading Toontown!'),
 43: ('The Lawbot Gambit 3', 'The Lawbot Gambit. Stop the Ambulance Chaser Cogs from invading Toontown!'),
 44: ('The Lawbot Gambit 4', 'The Lawbot Gambit. Stop the Backstabber Cogs from invading Toontown!'),
 45: ('The Trouble With Bossbots 1', 'The Trouble with Bossbots. Stop the Flunky Cogs from invading Toontown!'),
 46: ('The Trouble With Bossbots 2', 'The Trouble with Bossbots. Stop the Pencil Pusher Cogs from invading Toontown!'),
 47: ('The Trouble With Bossbots 3', 'The Trouble with Bossbots. Stop the Micromanager Cogs from invading Toontown!'),
 48: ('The Trouble With Bossbots 4', 'The Trouble with Bossbots. Stop the Downsizer Cogs from invading Toontown!'),
 49: ('Jellybean Day', 'Celebrate Jellybean Day with double Jellybean rewards at parties!'),
 53: ('Cold Caller Invasion', 'Stop the Cold Caller Cogs from invading Toontown!'),
 54: ('Bean Counter Invasion', 'Stop the Bean Counter Cogs from invading Toontown!'),
 55: ('Double Talker Invasion', 'Stop the Double Talker Cogs from invading Toontown!'),
 56: ('Downsizer Invasion', 'Stop the Downsizer Cogs from invading Toontown!'),
 59: ("ValenToon's Day", "Celebrate ValenToon's Day from Feb 09 to Feb 16!"),
 72: ('Yes Men Invasion', 'Stop the Yes Men Cogs from invading Toontown!'),
 73: ('Tightwad Invasion', 'Stop the Tightwad Cogs from invading Toontown!'),
 74: ('Telemarketers Invasion', 'Stop the Telemarketer Cogs from invading Toontown!'),
 75: ('Head Hunter Invasion', 'Stop the Head Hunter Cogs from invading Toontown!'),
 76: ('Spin Doctor Invasion', 'Stop the Spin Doctor Cogs from invading Toontown!'),
 77: ('Moneybags Invasion', 'Stop the Moneybags from invading Toontown!'),
 78: ('Two-faces Invasion', 'Stop the Two-faces from invading Toontown!'),
 79: ('Mingler Invasion', 'Stop the Mingler Cogs from invading Toontown!'),
 80: ('Loan Shark Invasion', 'Stop the Loanshark Cogs from invading Toontown!'),
 81: ('Corporate Raider Invasion', 'Stop the Corporate Raider Cogs from invading Toontown!'),
 82: ('Robber Baron Invasion', 'Stop the Robber Baron Cogs from invading Toontown!'),
 83: ('Legal Eagle Invasion', 'Stop the Legal Eagle Cogs from invading Toontown!'),
 84: ('Big Wig Invasion', 'Stop the Big Wig Cogs from invading Toontown!'),
 85: ('Big Cheese Invasion', 'Stop the Big Cheese from invading Toontown!'),
 86: ('Down Sizer Invasion', 'Stop the Down Sizer Cogs from invading Toontown!'),
 87: ('Mover And Shaker Invasion', 'Stop the Mover and Shaker Cogs from invading Toontown!'),
 88: ('Double Talker Invasion', 'Stop the Double Talkers Cogs from invading Toontown!'),
 89: ('Penny Pincher Invasion', 'Stop the Penny Pinchers Cogs from invading Toontown!'),
 90: ('Name Dropper Invasion', 'Stop the Name Dropper Cogs from invading Toontown!'),
 91: ('Ambulance Chaser Invasion', 'Stop the Ambulance Chaser Cogs from invading Toontown!'),
 92: ('Micro Manager Invasion', 'Stop the Micro Manager Cogs from invading Toontown!'),
 93: ('Number Cruncher Invasion', 'Stop the Number Cruncher Cogs from invading Toontown!'),
 95: ('Victory Parties', 'Celebrate our historic triumph against the Cogs!'),
 96: ('Operation: Storm Sellbot', "Sellbot HQ is open to everyone. Let's go fight the VP!"),
 97: ('Operation: Lawbots Lose', "Lawbot HQ is open to everyone. Let's go fight the CJ!"),
 98: ('Operation: Cashbot Chaos', "Cashbot HQ is open to everyone. Let's go fight the CFO!"),
 99: ('Operation: Besiege Bossbot', "Bossbot HQ is open to everyone. Let's go fight the CEO!"),
 100: ('Double Bean Days - Trolley Games', ''),
 101: ('Double Bean Days - Fishing', ''),
 102: ('Jellybean Week', 'Celebrate Jellybean Week with double Jellybean rewards!'),
 103: ("Top Toons New Year's Day Marathon", "Chances to win every hour! See the What's New Blog for details!"),
 105: ('Toons go GREEN!', 'Toons make a green scene at Green Bean Jeans on Oak Street in Daisy Gardens!'),
 107: ('Tax Day', 'Number Crunchers are planning a mega invasion! Stop those Number Crunchers!'),
 123: ('Day of the Magic Cat', 'Toons gather around to honor the Magic Cat, the creator of the universe!')}
UnknownHoliday = 'Unknown Holiday %d'
HolidayFormat = '%b %d '
HourFormat = '12'
CogdoMemoGuiTitle = 'Memos:'
CogdoMemoNames = 'Barrel-Destruction Memos'
CogdoStomperName = 'Stomp-O-Matic'
BoardroomGameTitle = 'Boardroom Hijinks'
BoardroomGameInstructions = 'The Bossbots are having a meeting to decide what to do with stolen gags. Slide on through and grab as many gag-destruction memos as you can!'
CogdoCraneGameTitle = 'Vend-A-Stomper'
CogdoCraneGameInstructions = 'The Cashbots are using a coin-operated machine to destroy laff barrels. Use the cranes to pick up and throw money bags, in order to prevent barrel destruction!'
CogdoMazeGameTitle = 'Mover & Shaker\nField Office'
CogdoMazeGameInstructions = 'The big Mover & Shaker Cogs have the code to open the door. Defeat them with your water balloons in order to get it!'
CogdoMazeIntroMovieDialogue = (("This is the Toon Resistance! The Movers & Shakers\nhave our Jokes, and they've locked the exit!",), ('Grab water balloons at coolers, and throw them at Cogs!\nSmall Cogs drop Jokes, BIG COGS open the exit.',), ('The more Jokes you rescue, the bigger your Toon-Up\nat the end. Good luck!',))
CogdoMazeGameDoorOpens = 'THE EXIT IS OPEN FOR 60 SECONDS!\nGET THERE FAST FOR A BIGGER TOON-UP'
CogdoMazeGameLocalToonFoundExit = "The exit will open when\nyou've busted all four BIG COGS!"
CogdoMazeGameTimeOut = 'Oh no, time ran out! You lost your jokes.'
CogdoMazeGameTimeAlert = 'Hurry up! 60 seconds to go!'
CogdoMazeGameBossGuiTitle = 'BIG COGS:'
CogdoMazeFindHint = 'Find a Water Cooler'
CogdoMazeThrowHint = "Press '%s' to throw your water balloon"
CogdoMazeSquashHint = 'Falling objects popped your balloon'
CogdoMazeBossHint = 'Big Cogs take TWO hits to defeat'
CogdoMazeMinionHint = 'Smaller Cogs drop jokes'
CogdoMazeGameElevatorRewardLaff = 'Great job, Toons!\nYou get a Toon-Up from the jokes you saved!'
CogdoFlyingGameTitle = 'Legal Eagle\nField Office'
CogdoFlyingGameInstructions = "Fly through the Legal Eagles' lair. Watch out for obstacles and Cogs along the way, and don't forget to refuel your helicopter!"
CogdoFlyingIntroMovieDialogue = (("You won't ruffle our feathers, Toons! We're destroying barrels of your Laff, and you cannot stop us!", "A flock of Toons! We're crushing barrels of your Laff in our %s, and there's nothing you can do about it!" % CogdoStomperName, "You can't egg us on, Toons! We're powering our offices with your Laff, and you're powerless to stop us!"), ('This is the Toon Resistance! A little bird told me you can use propellers to fly around, grab Barrel Destruction Memos, and keep Laff from being destroyed! Good luck, Toons!', 'Attention Toons! Wing it with a propeller and collect Barrel Destruction Memos to keep our Laff from being stomped! Toon Resistance out!', 'Toon Resistance here! Cause a flap by finding propellers, flying to the Barrel Destruction Memos, and keeping our Laff from being smashed! Have fun!'), ("Squawk! I'm a Silver Sprocket Award winner, I don't need this!", 'Do your best, Toons! You will find us to be quite talon-ted!', "We'll teach you to obey the pecking order, Toons!"))
CogdoFlyingGameFuelLabel = 'Fuel'
CogdoFlyingGameLegalEagleTargeting = 'A Legal Eagle has noticed you!'
CogdoFlyingGameLegalEagleAttacking = 'Incoming Eagle!'
CogdoFlyingGamePickUpAPropeller = 'You need a propeller to fly!'
CogdoFlyingGamePressCtrlToFly = "Press '%s' to fly up!"
CogdoFlyingGameYouAreInvincible = 'Red Tape protects you!'
CogdoFlyingGameTimeIsRunningOut = 'Time is running out!'
CogdoFlyingGameMinimapIntro = 'This meter shows your progress!\nX marks the finish line.'
CogdoFlyingGameMemoIntro = 'Memos prevent Laff Barrels in\nthe Stomper Room from being destroyed!'
CogdoFlyingGameOutOfTime = 'Oh No! You ran out of time!'
CogdoFlyingGameYouMadeIt = 'Good work, you made it on time!'
CogdoFlyingGameTakingMemos = 'The Legal Eagles took all your memos!'
CogdoBarrelRoomTitle = 'Stomper Room'
CogdoBarrelRoomIntroDialog = 'Good work, Toons! You have haulted the Stomp-O-Matic and are now able to collect some of the stolen Laff barrels, but make sure to hurry before the Cogs come!'
CogdoExecutiveSuiteTitle = 'Executive Suite'
CogdoExecutiveSuiteIntroMessage = "Oh no, they've got the shop keeper!\nDefeat the Cogs and free the captive."
CogdoExecutiveSuiteToonThankYou = 'Thanks for the rescue!\nIf you need help in a fight, use this SOS card to call my friend %s.'
CogdoExecutiveSuiteToonThankYouLawbot = 'Thanks for the rescue!\nThe Lawbots have left behind some sprocket awards that you can use to buy new things in your cattlelog!'
CogdoExecutiveSuiteToonBye = 'Bye!'
SillySurgeTerms = ['Amusing Ascent!',
 'Silly Surge!',
 'Ridiculous Rise!',
 'Giggle Growth!',
 'Funny Fueling!',
 'Batty Boost!',
 'Crazy Climb!',
 'Jolly Jump!',
 'Loony Lift!',
 'Hilarity Hike!',
 'Insanity Increase!',
 'Cracked-Uptick!']
InteractivePropTrackBonusTerms = {0: 'Super Toon-Up!',
 1: '',
 2: '',
 3: '',
 4: 'Super Throw!',
 5: 'Super Squirt!',
 6: ''}
GloveInvalidColorMessage = "That's an unpainted color."
GloveSameColorMessage = "You're already wearing those gloves!"
GloveNoMoneyMessage = "You don't have enough jellybeans!"
GloveMoreMoneyMessage = 'You need %s jellybeans to buy new gloves!'
GloveSuccessMessage = 'Have fun with your new gloves!'
GlovePickColorMessage = 'Feel free to choose!'
GloveGuiTitle = 'Choose a glove color!'
GloveGuiNotice = 'Costs %s jellybeans.'
GloveGuiBuy = 'Buy'
GloveGuiSameColor = 'You already have these!'
NametagBuyMessage = 'Change your nametag!'
NametagColorButton = 'Color'
NametagStyleButton = 'Style'
NametagGuiNotice = 'Costs %s jellybeans.'
NametagColorMoreMoneyMessage = 'You need %s jellybeans to buy new nametag colors!'
NametagColorGuiTitle = 'Choose a nametag color!'
NametagGuiBuy = 'Buy'
NametagColorGuiSameColor = 'You already have this color!'
NametagColorPickMessage = 'Change the look of your nametag!'
NametagColorPurchaseSuccess = 'Enjoy your new nametag color!'
NametagInvalidStyleMessage = "That's an invalid style."
NametagStyleGuiSameStyle = 'You already have this style!'
NametagStyleGuiTitle = 'Choose a nametag style!'
NametagStyleMoreMoneyMessage = 'You need %s jellybeans to buy new nametag styles!'
NametagStylePurchaseSuccess = 'Enjoy your new nametag style!'
CheesyTitle = 'Cheesy Effects'
CheesyExit = 'Exit'
CheesyPickMessage = 'Buy a cheesy effect!'
CheesyName = 'Name: %s'
CheesyDescription = 'Description:'
CheesyCost = 'Cost: %s Jellybeans'
CheesyPreview = 'Preview'
CheesyPurchase = 'Purchase'
CheesyGoBack = 'Go Back'
AllCheesyPurchased = "You've purchased all purchasable cheesy effects! Wait for new ones to come out!"
NoCheesySelected = "You haven't chosen a cheesy effect! Click on a cheesy effect name to purchase it."
CheesyPurchaseSuccess = 'Purchase Successful!'
CogLevelLabelOn = 'The cog level GUI is on.'
CogLevelLabelOff = 'The cog level GUI is off.'

HouseNames = ("Bungalow", "Tiki", "Teepee", "Castle", "Cupcake", "Cabin")
CatalogPurchaseHouseType = "When you buy a new house type, the current one is replaced by it. To recover the old type, you'll need to buy it back. Continue?"
# Buffs

buffIdStrings = {
  0: ('Your movement speed will be slightly increased for the next %d %s.',
      'Reward: Increased movement speed')
}

def getBuffString(buffId, buffTime):
    if buffTime < 60:
        return buffIdStrings[buffId][0] % (buffTime, 'minutes')
    else:
        return buffIdStrings[buffId][0] % (buffTime / 60, 'hours')


def getBuffPosterString(buffId):
    return buffIdStrings[buffId][1]

BoyPetNames = ['Achilles', 'Adolfo', 'Adonis', 'Aesop', 'Agamemnon', 'Ahab', 'Ahmed', 'Ajax', 'Alastair', 'Alberto', 'Alexander', 'Alfonso', 'Alonzo', 'Amadeus', 'Ambrose', 'Andre', 'Angelo', 'Angus', 'Antoine', 'Anton', 'Antonio', 'Archibald', 'Archimedes', 'Arnold', 'Atilla', 'Attaboy', 'Avi', 'Barney', 'Bart', 'Bartleby', 'Basil', 'Baxter', 'Beardsley', 'Beauchamp', 'Beauregard', 'Ben', 'Benny', 'Bernie', 'Billygoat', 'Bluebeard', 'Bo', 'Bogart', 'Bogie', 'Bowser', 'Brando', 'Bruce', 'Bruno', 'Brutus', 'Bubba', 'Buck', 'Buster', 'Butch', 'Cagney', 'Carlton', 'Casanova', 'Casper', 'Cecil', 'Cedric', 'Charlie', 'Chekhov', 'Chico', 'Chief', 'Chip', 'Chuck', 'Chuckie', 'Chucko', 'Clancy', 'Clark', 'Claude', 'Clayton', 'Cliff', 'Clive', 'Clyde', 'Cody', 'Colonel', 'Confucius', 'Conrad', 'Cooper', 'Cowboy', 'Cyril', 'Dagwood', 'Dante', 'Deano', 'Donahue', 'Donatello', 'Drysdale', 'Duke', 'Dweezil', 'Eddie', 'Edgar', 'Edison', 'Eggman', 'Einstein', 'Elmer', 'Elwood', 'Emerson', 'Emmet', 'Errol', 'Ethan', 'Fafnir', 'Farnsworth', 'Felix', 'Fenimore', 'Fenwick', 'Ferdinand', 'Fergus', 'Fido', 'Figaro', 'Filbert', 'Fitzgerald', 'Floyd', 'Frampton', 'Fred', 'Gabriel', 'Garfunkel', 'General', 'Genghis', 'Gershwin', 'Gladiator', 'Gladstone', 'Gorilla', 'Grampa', 'Gramps', 'Groucho', 'Gulliver', 'Gunther', 'Gus', 'Hamlet', 'Harold', 'Harpo', 'Harvey', 'Haseltine', 'Heathcliff', 'Hector', 'Hemingway', 'Hendrix', 'Herbert', 'Hercules', 'Herman', 'Hermes', 'Higgins', 'Hobart', 'Homestar', 'Horace', 'Horatio', 'Horton', 'Houdini', 'Humphrey', 'Ichabod', 'Iggy', 'Ignatius', 'Ignatz', 'Igor', 'Ike', 'Iron Ike', 'Ironside', 'Irving', 'Irwin', 'Isaac', 'Ishmael', 'Ivan', 'Ivanhoe', 'Jack', 'Jake', 'Jasper', 'Jaymo', 'Jerry', 'Jethro', 'Jimmy', 'Jonah', 'Karloff', 'Kasper', 'Keanu', 'Kilroy', 'King', 'Kingfish', 'Kirby', 'Kissinger', 'Lambert', 'Lancelot', 'Lazarus', 'Leonardo', 'Lindbergh', 'Linus', 'Lionel', 'Luigi', 'Macarthur', 'Macbeth', 'Mack', 'Malcolm', 'Mandrake', 'Marcel', 'Marco', 'Mario', 'Marmalade', 'Matador', 'Maurice', 'Maximilian', 'Maxwell', 'Maynard', 'Melville', 'Merlin', 'Michelangelo', 'Milo', 'Moe', 'Morissey', 'Mortimer', 'Mozart', 'Mugsy', 'Muldoon', 'Nabokov', 'Napoleon', 'Narcissus', 'Nelson', 'Nero', 'Nimoy', 'Nimrod', 'Norbert', 'Norman', 'Norris', 'Obadiah', 'Odysseus', 'Ogden', 'Olaf', 'Omar', 'Opie', 'Opus', 'Oswald', 'Othello', 'Otto', 'Pablo', 'Paco', 'Paddington', 'Pancho', 'Paolo', 'Pappy', 'Pavarotti', 'Pavlov', 'Peabody', 'Petey', 'Picasso', 'Pierre', 'Pinkerton', 'Pippin', 'Poindexter', 'Pop', 'Popperton', 'Poseidon', 'Prince', 'Puccini', 'Puck', 'Pugsly', 'Pushkin', 'Quigley', 'Quimby', 'Quincy', 'Reggie', 'Regis', 'Reinhold', 'Rembrandt', 'Renoir', 'Reuben', 'Rex', 'Rhett', 'Ricardo', 'Richter', 'Rocky', 'Roderick', 'Romeo', 'Romulus', 'Roosevelt', 'Rover', 'Rudolph', 'Rudy', 'Rufus', 'Rupert', 'Salvador', 'Sandeep', 'Schubert', 'Scooby', 'Scotty', 'Scruffy', 'Sebastian', 'Seymour', 'Shakespeare', 'Shatner', 'Siegfried', 'Sigmund', 'Simon', 'Sinbad', 'Skyler', 'Snowman', 'Snyder', 'Socrates', 'Sorcerer', 'Spalding', 'Spanky', 'Spencer', 'Spinoza', 'Spock', 'Stallion', 'Steinbeck', 'Stradivarius', 'T Bone', 'Tchaikovsky', 'Terminator', 'Tesla', 'Thaxter', 'Theo', 'Theodore', 'Thessalus', 'Throckmorton', 'Tiberius', 'Tiger', 'Tobias', 'Tolkein', 'Toreador', 'Travis', 'Travolta', 'Triton', 'Ulysses', 'Umberto', 'Victor', 'Vincent', 'Vinnie', 'Virgil', 'Vlad', 'Vladimir', 'Voltaire', 'Vonnegut', 'Wainwright', 'Waldo', 'Waldorf', 'Walter', 'Warhol', 'Watson', 'Wayne', 'Wilbur', 'Wilfred', 'Wilhelm', 'Winston', 'Wiseguy', 'Wolfgang', 'Woodbury', 'Woodrow', 'Wyatt', 'Xanthus', 'Xavier', 'Zeus', 'Zorro']
GirlPetNames = ['Abby', 'Adorabelle', 'Aggie', 'Akiko', 'Allessandria', 'Amaryllis', 'Ambrosia', 'Andrea', 'Anita', 'Annette', 'Annie', 'Antionette', 'April', 'Arabella', 'Ariel', 'Ashley', 'Athena', 'Babette', 'Babs', 'Babydoll', 'Ballerina', 'Beatrice', 'Bertie', 'Beulah', 'Beverly', 'Bianca', 'Blossom', 'Bozette', 'Brittany', 'Buttercup', 'Callalilly', 'Candy', 'Carmen', 'Carnation', 'Cassandra', 'Cece', 'Celeste', 'Chanel', 'Chantilly', 'Charlotte', 'Chelsea', 'Cher', 'Cherry', 'Chickie', 'Chloe', 'Cindy', 'Cinnamon', 'Cissy', 'Claire', 'Clementine', 'Cleopatra', 'Coco', 'Cowgirl', 'Daffodil', 'Dagmar', 'Daisy', 'Daphne', 'Dee Dee', 'Delilah', 'Dixie', 'Dolly', 'Dot', 'Dottie', 'Duchess', 'Edith', 'Electra', 'Elsie', 'Elvira', 'Emerald', 'Europa', 'Fannie', 'Fatima', 'Felicity', 'Fifi', 'Flopsy', 'Flower', 'Funnygirl', 'Gabby', 'Garbo', 'Geranium', 'Gidget', 'Gigi', 'Ginger', 'Goldie', 'Granny', 'Guinevere', 'Gwen', 'Hannah', 'Heidi', 'Henrietta', 'Hera', 'Hermione', 'Hildegard', 'Honey', 'Honeysuckle', 'Hortense', 'Iris', 'Ivy', 'Jade', 'Jaquelin', 'Jasmine', 'Jewel', 'Jo', 'Josephine', 'Joy', 'Juliet', 'June', 'Juniper', 'Kandy', 'Kate', 'Katrina', 'Koko', 'Kornelia', 'Krystal', 'Lacey', 'Lady', 'Lambchop', 'Lapis Lazuli', 'Lassie', 'Laverne', 'Leonora', 'Libby', 'Libra', 'Lilac', 'Lily', 'Lipstick', 'Lisa', 'Lottie', 'Lovebird', 'Lovesong', 'Lucretia', 'Lucy', 'Lulu', 'Luna', 'MK', 'Mabel', 'Magenta', 'Maggie', 'Mamacita', 'Mantissa', 'Maxine', 'Mayflower', 'Medusa', 'Melody', 'Mercedes', 'Meriwether', 'Mermaid', 'Mildred', 'Minerva', 'Missy', 'Mitzi', 'Mocha', 'Molly', 'Mona Lisa', 'Moneypenny', 'Monique', 'Mopsy', 'Nadia', 'Nancy', 'Nannygoat', 'Naomi', 'Nellybelle', 'Nightingale', 'Nikita', 'Odelia', 'Olga', 'Olive', 'Olympia', 'Oona', 'Opal', 'Ophelia', 'Organdy', 'Pandora', 'Patrikia', 'Penelope', 'Penny', 'Petinka', 'Petunia', 'Phoebe', 'Phoenicia', 'Pixie', 'Poinsettia', 'Pookie', 'Precious', 'Prettipaws', 'Primrose', 'Princess', 'Pudgette', 'Queenie', 'Raphael', 'Rapunzel', 'Raquel', 'Rosabelle', 'Rosebud', 'Roxanne', 'Roxy', 'Ruby', 'Sable', 'Sabrina', 'Sadie', 'Saffron', 'Sage', 'Sapphire', 'Sassafras', 'Savannah', 'Scarlett', 'Scheherazade', 'Serenade', 'Sienna', 'Silky', 'Sissy', 'Snoogie', 'Snookie', 'Sonja', 'Sophia', 'Sophie', 'Sorceress', 'Summer', 'Sunbonnet', 'Sunny', 'Sunshine', 'Tabitha', 'Tasha', 'Titania', 'Tootsie', 'Topaz', 'Trixie', 'Truffles', 'Tulip', 'Twiggy', 'Velma', 'Venice', 'Venus', 'Veronica', 'Vicki', 'Victoria', 'Viola', 'Violet', 'Wallflower', 'Winnie', 'Winona', 'Yum Yum', 'Zelda', 'Zsa Zsa']
NeutralPetNames = ['Abner', 'Abracadabra', 'Acacia', 'Ace', 'Admiral', 'Aglet', 'Akimbo', 'Alabaster', 'Alcatraz', 'Alchemy', 'Alfalfa', 'Alien', 'Allegro', 'Alto', 'Amazon', 'Ambassador', 'Amethyst', 'Amnesia', 'Ampersand', 'Anaconda', 'Anchovy', 'Andretti', 'Andromeda', 'Angstrom', 'Animal', 'Antergy', 'Anubus', 'Apogee', 'Apollo', 'Applesauce', 'Apprentice', 'Apricot', 'Aquarius', 'Aramis', 'Archer', 'Arf', 'Argus', 'Argyle', 'Aristotle', 'Arizona', 'Arrow', 'Arsenio', 'Asimov', 'Asparagus', 'Asphalt', 'Astro', 'Atom', 'Augie', 'August', 'Avalanche', 'Avalon', 'Avenger', 'Avis', 'Axel', 'Axle', 'Azalea', 'Aztec', 'Azure', 'Babbit', 'Babble', 'Babbler', 'Baby', 'Babykins', 'Baccarat', 'Backgammon', 'Badger', 'Baggy', 'Bailey', 'Baja', 'Balboa', 'Baldo', 'Baldric', 'Baldy', 'Ballyhoo', 'Bambino', 'Bamboo', 'Bamboozle', 'Bamboozler', 'Banana', 'Bandit', 'Bandito', 'Bangle', 'Banjo', 'Banshee', 'Banzai', 'Barbarian', 'Bargraph', 'Barky', 'Barnacle', 'Barracuda', 'Bashful', 'Bazooka', 'Beaker', 'Bean', 'Beaner', 'Beanstalk', 'Beany', 'Bear', 'Beauty', 'Beaver', 'Beep', 'Beeper', 'Beepy', 'Beethoven', 'Beezneez', 'Begonia', 'Bellyflop', 'Benson', 'Bentley', 'Beppo', 'Bermuda', 'Betatest', 'Bewitched', 'Big Red', 'Big Shot', 'Bigbelly', 'Bigfoot', 'Bijou', 'Bindle', 'Bing', 'Bingo', 'Binky', 'Biscuit', 'Bitsy', 'Bizzy', 'Blackberry', 'Blackbird', 'Blackfoot', 'Blackie', 'Blackjack', 'Blacktop', 'Blanket', 'Blaze', 'Bleary', 'Blimp', 'Blimpo', 'Blimpy', 'Blip Blop', 'Blizzard', 'Blockhead', 'Blondie', 'Blooper', 'Blorange', 'Blot', 'Blotto', 'Bluebell', 'Blueberry', 'Bluegrass', 'Bluenose', 'Blueprint', 'Blunder', 'Blurp', 'Boa', 'Bobbin', 'Bobo', 'Bobtail', 'Bodyguard', 'Boggs', 'Bojangles', 'Bolt', 'Bombshell', 'Bonbon', 'Bones', 'Bongo', 'Bonkers', 'Bono', 'Bonsai', 'Boo Boo', 'Boober', 'Boogeyman', 'Boom Boom', 'Boomer', 'Boots', 'Borax', 'Borg', 'Bosco', 'Bottlecap', 'Bottlenose', 'Boulder', 'Bounce Bounce', 'Bouncer', 'Bouncy', 'Bowtie', 'Bowzer', 'Boyd', 'Bozo', 'Brahms', 'Brainchild', 'Bratwurst', 'Bravo', 'Briar', 'Brie', 'Broadway', 'Broccoli', 'Bronco', 'Brooklyn', 'Brouhaha', 'Brownie', 'Bruiser', 'Bubblegum', 'Bubbles', 'Bubo', 'Buccaneer', 'Buckaroo', 'Buckeye', 'Buckingham', 'Buckle', 'Buckshot', 'Buckskin', 'Buckwheat', 'Budapest', 'Buddy', 'Buffalo', 'Buffoon', 'Bug', 'Bugaboo', 'Bugeye', 'Bugsy', 'Bullet', 'Bullwinkle', 'Bumblebee', 'Bumbler', 'Bumper', 'Bumpkin', 'Bumpus', 'Bumpy', 'Bungee', 'Bunko', 'Bunyan', 'Burbank', 'Butterball', 'Butterscotch', 'Buzz', 'Buzzard', 'Buzzy', 'Byte', 'Caboodle', 'Caboose', 'Cadbury', 'Cadet', 'Caesar', 'Calculus', 'Calico', 'Callisto', 'Calypso', 'Calzone', 'Cambridge', 'Camelot', 'Camembert', 'Cameo', 'Campbell', 'Canoe', 'Cap', 'Cappy', 'Capricorn', 'Captain', 'Caramba', 'Caramel', 'Cargo', 'Carlos', 'Carpool', 'Caruso', 'Casablanca', 'Casbah', 'Casey', 'Cashmere', 'Cassidy', 'Castaway', 'Catamaran', 'Caviar', 'Cayenne', 'Cerebro', 'Cha Cha', 'Challenger', 'Chamberlain', 'Chamomile', 'Champ', 'Chaos', 'Charade', 'Charcoal', 'Charger', 'Charmed', 'Chaser', 'Chasm', 'Checkers', 'Cheesecake', 'Cheesy', 'Cheetah', 'Chester', 'Chewie', 'Chicory', 'Chiffon', 'Chigger', 'Chili', 'Chili Bean', 'Chipmunk', 'Chipper', 'Chips', 'Chocolate', 'Choo Choo', 'Chopin', 'Chopper', 'Chops', 'Chopsticks', 'Chowder', 'Chowderhead', 'Chromium', 'Chubby', 'Chuckles', 'Chutzpah', 'Cinder', 'Citrus', 'Clipper', 'Cloud', 'Cloudy', 'Clover', 'Clue', 'Clueless', 'Clunky', 'Coach', 'Cobol', 'Cobra', 'Cocoa', 'Coconut', 'Cola', 'Colorado', 'Comet', 'Comma', 'Confetti', 'Connecticut', 'Cookie', 'Cooter', 'Copper', 'Coral', 'Corduroy', 'Corky', 'Cornball', 'Corncob', 'Cornelia', 'Cornmo', 'Corny', 'Corona', 'Coronet', 'Cosmo', 'Cottontail', 'Couscous', 'Coyote', 'Crackers', 'Cranberry', 'Crash', 'Crawdad', 'Creamy', 'Creeper', 'Creepy', 'Crescent', 'Cricket', 'Critter', 'Croissant', 'Crouton', 'Crufty', 'Cruiser', 'Crumb', 'Crumbly', 'Cruncher', 'Crunchy', 'Cucamonga', 'Cucaracha', 'Cuckoo', 'Cucumber', 'Cuddles', 'Cupcake', 'Cupid', 'Curmudgeon', 'Curry', 'Cutie', 'Cutie Pie', 'Cypress', 'DJ', 'Dakota', 'Dali', 'Damascus', 'Dancer', 'Dandelion', 'Danger', 'Database', 'Dazzle', 'Dazzler', 'Dazzy', 'December', 'Delaware', 'Delphi', 'Detonator', 'Detour', 'Detroit', 'Deuce', 'Dewfall', 'Diamond', 'Dice', 'Diego', 'Digby', 'Digger', 'Digit', 'Dimples', 'Dingo', 'Dingus', 'Dinky', 'Divot', 'Dizzy', 'Doc', 'Dodger', 'Dodo', 'Dolby', 'Donut', 'Doodad', 'Doodah', 'Doodle', 'Draco', 'Dracula', 'Drawers', 'Dreadnought', 'Dream', 'Dreamer', 'Dreamweaver', 'Dreamy', 'Drippy', 'Droopy', 'Drummer', 'Dumpling', 'Durango', 'Dustmop', 'Dynamite', 'Dynamo', 'Eagle', 'Ebony', 'Eccentric', 'Echo', 'Eclipse', 'Ecstatic', 'Edge', 'Egad', 'Egghead', 'Eggnog', 'Eggtoss', 'Egypt', 'Elderberry', 'Electron', 'Elf', 'Elijah', 'Elvis', 'Email', 'Ember', 'Encore', 'Enoch', 'Epcot', 'Epic', 'Epilog', 'Equinox', 'Ergo', 'Escapade', 'Eskimo', 'Espresso', 'Euclid', 'Euphoria', 'Euphrates', 'Excalibur', 'Exeter', 'Eyespy', 'Faberge', 'Fable', 'Facepuff', 'Fahrenheit', 'Fairbanks', 'Fairfax', 'Faith', 'Faithful', 'Fajita', 'Falafel', 'Falcon', 'Fancy', 'Fandango', 'Fang', 'Fangtastic', 'Fantasia', 'Fats', 'Fatso', 'Fatty', 'Faust', 'Fax', 'Fearless', 'Feather', 'Feedback', 'Fellini', 'Ferrari', 'Fester', 'Fetch', 'Fiddler', 'Fiddlesticks', 'Fiesta', 'Filibuster', 'Fingerprint', 'Fingers', 'Fink', 'Fishbone', 'Fishface', 'Fishhook', 'Fizz', 'Fizzle', 'Fizzy', 'Flabby', 'Flagpole', 'Flame', 'Flannel', 'Flapjack', 'Flash', 'Flatfoot', 'Flicker', 'Fling', 'Flip', 'Flipper', 'Flop', 'Flopper', 'Floppy', 'Florida', 'Fluffster', 'Fluffy', 'Flurry', 'Flute', 'Fog', 'Fogarty', 'Fondue', 'Fortran', 'Fox', 'Foxy', 'Frankfurter', 'Freckles', 'Freebie', 'Freezerburn', 'French Toast', 'Friday', 'Frogface', 'Frogmar', 'Frost', 'Frosty', 'Fruitcake', 'Frump', 'Frumpson', 'Frumpy', 'Fudd', 'Fuddles', 'Fudge', 'Fugitive', 'Fuji', 'Fungus', 'Funky', 'Furball', 'Furface', 'Fusebox', 'Fuzzball', 'Fuzzy', 'Fuzzyface', 'Fuzzykins', 'Gabardine', 'Galaxy', 'Gallop', 'Gambit', 'Gambler', 'Gangway', 'Garlic', 'Garlicbreath', 'Garnet', 'Garth', 'Gavotte', 'Gecko', 'Geewhiz', 'Gem', 'Gemini', 'Gerbil', 'Gewgaw', 'Ghost', 'Giddyup', 'Giggles', 'Gingerbread', 'Gingersnap', 'Glick', 'Gnash', 'Gnasher', 'Gnocchi', 'Gnome', 'Gobbledegook', 'Gobbler', 'Goblet', 'Goblin', 'Gobo', 'Gogo', 'Goiter', 'Goliath', 'Gomer', 'Goober', 'Gooch', 'Gooey', 'Googol', 'Goose', 'Gooseberry', 'Goosebump', 'Gopher', 'Gouda', 'Governor', 'Gracie', 'Graffiti', 'Graham', 'Granite', 'Granola', 'Gravlax', 'Gremlin', 'Grep', 'Grok', 'Grue', 'Grumpus', 'Grumpy', 'Grungy', 'Guffaw', 'Gumbo', 'Gumdrop', 'Gump', 'Gumpus', 'Gumshoe', 'Gypsy', 'Gyro', 'Haggis', 'Haha', 'Hairball', 'Half Pint', 'Halibut', 'Halifax', 'Halloweenie', 'Halo', 'Halogen', 'Hambone', 'Hamburger', 'Hammer', 'Hammerhead', 'Hammerstein', 'Hammy', 'Hamster', 'Happy', 'Harlequin', 'Harley', 'Harmonica', 'Harmony', 'Harvard', 'Havoc', 'Hawk', 'Hawkeye', 'Hayseed', 'Haywire', 'Hazel', 'Heartbreaker', 'Heathrow', 'Heckler', 'Hedgehog', 'Heehee', 'Hemlock', 'Herringbone', 'Hiccup', 'Hifi', 'Hip Hip', 'Hippo', 'Hippodrome', 'Hoagie', 'Hobo', 'Hoho', 'Holmes', 'Honeybee', 'Hooligan', 'Hoops', 'Hoosier', 'Horoscope', 'Hot Dog', 'Hotfoot', 'Hotshot', 'Houston', 'Howard', 'Huckleberry', 'Huffy', 'Huggy', 'Hugo', 'Humdinger', 'Humdrum', 'Hurricane', 'Hydraulic', 'Hypnos', 'IOU', 'Iapyx', 'Ibex', 'Icarus', 'Icky', 'Icon', 'Icy', 'Idiom', 'Idlewild', 'Igloo', 'Iguana', 'Illogical', 'Illusion', 'Imagine', 'Imp', 'Impy', 'Imus', 'Indigo', 'Indy', 'Inferno', 'Infinity', 'Infrared', 'Ingot', 'Inkblot', 'Inkwell', 'Innie', 'Input', 'Insomnia', 'Intro', 'Iodine', 'Iota', 'Itchy', 'Ivory', 'Izzat', 'Izzy', 'Jabber', 'Jabberwock', 'Jackaroo', 'Jackhammer', 'Jackpot', 'Jackrabbit', 'Jacuzzi', 'Jag', 'Jaguar', 'Jalapeno', 'Jambalaya', 'Jamboree', 'January', 'Jargon', 'Java', 'Jaws', 'Jaybird', 'Jester', 'Jet', 'Jicko', 'Jiffy', 'Jigsaw', 'Jimjam', 'Jingle', 'Jinx', 'Jitterbug', 'Jocko', 'Jojo', 'Joker', 'Jokester', 'Joliet', 'Joplin', 'Jordie', 'Jove', 'Joyride', 'Jubilee', 'Jughead', 'Jujitsu', 'Jukebox', 'July', 'Jumbo', 'Jumpy', 'Junior', 'Juno', 'Kabob', 'Kabuki', 'Kafka', 'Kahuna', 'Kalamazoo', 'Kaleidoscope', 'Kalmuk', 'Kansas', 'Kappa', 'Karamazov', 'Karate', 'Karma', 'Katmandu', 'Katsumi', 'Kayak', 'Keepsake', 'Kellogg', 'Kelvin', 'Ketchup', 'Kewpie', 'Keyboard', 'Keyring', 'Khaki', 'Kibbles', 'Kiddo', 'Kielbasa', 'Kilimanjaro', 'Kilowatt', 'Kimono', 'Kinetic', 'Kipling', 'Kismet', 'Kissyface', 'Kitten', 'Klinger', 'Klondike', 'Kludge', 'Klute', 'Klutz', 'Klutzy', 'Knickerbocker', 'Knievel', 'Knish', 'Knock Knock', 'Knockwurst', 'Knoop', 'Knucklebone', 'Knuckles', 'Koala', 'Kodiak', 'Kong', 'Kookaburra', 'Kooky', 'Kool Beanz', 'Kornball', 'Kosmix', 'Krakatoa', 'Kramer', 'Krispy', 'Krooner', 'Lab Rat', 'Labyrinth', 'Lacquer', 'Laddie', 'Ladybug', 'Lambada', 'Lamborghini', 'Lampoon', 'Lamster', 'Landmark', 'Landshark', 'Lanky', 'Lapper', 'Laptop', 'Lasagna', 'Laser', 'Latex', 'Lava', 'Lava Lamp', 'Lavender', 'Layaway', 'Leafy', 'Leaky', 'Lefty', 'Legend', 'Lemming', 'Lemonade', 'Lentil', 'Lettuce', 'Lexy', 'Lickety Split', 'Lickums', 'Licky', 'Licorice', 'Lightning', 'Lima', 'Limbo', 'Limey', 'Linguini', 'Link', 'Lintball', 'Lionheart', 'Lithgow', 'Litmus', 'Littlefoot', 'Liverpool', 'Liverwurst', 'Lizard', 'Lobo', 'Lofty', 'Logan', 'Logical', 'Lollipop', 'London', 'Longfellow', 'Longshot', 'Loofah', 'Looney', 'Loopy', 'Lotus', 'Luau', 'Lucky', 'Ludwig', 'Lullaby', 'Lumpy', 'Lunatic', 'Lynx', 'Lyrical', 'Macaroni', 'Macaroon', 'Macho', 'Macintosh', 'Mackerel', 'Mad Max', 'Madison', 'Maestro', 'Mage', 'Magic', 'Magma', 'Magnet', 'Magnolia', 'Magnus', 'Magoo', 'Magpie', 'Mahogany', 'Majestic', 'Malibu', 'Mambo', 'Mango', 'Manhattan', 'Manitoba', 'Mantra', 'Maple Syrup', 'Maraschino', 'Marathon', 'Mariachi', 'Marquee', 'Marshmallow', 'Martian', 'Marzipan', 'Mascot', 'Matchmaker', 'Matzoh', 'Maverick', 'Max', 'Maybe', 'Mayhem', 'Mazy', 'Meanie', 'Meatball', 'Meatloaf', 'Melange', 'Melbourne', 'Mellifluent', 'Melrose', 'Memo', 'Memphis', 'Menthol', 'Meow Meow', 'Meringue', 'Mesopotamia', 'Mesquite', 'Meta', 'Metric', 'Metro', 'Mezzo', 'Miami', 'Microfilm', 'Microwave', 'Midas', 'Midget', 'Midnight', 'Mikado', 'Milestone', 'Milkshake', 'Minty', 'Minuet', 'Minus', 'Mischief', 'Misery', 'Mist', 'Misty', 'Mittens', 'Mo', 'Mobius', 'Modesta', 'Mohair', 'Mohawk', 'Mojo', 'Molasses', 'Mole', 'Molecule', 'Monday', 'Mongoose', 'Monkey', 'Monogram', 'Montgomery', 'Monty', 'Moocher', 'Moochie', 'Moonbeam', 'Moondancer', 'Moondoggie', 'Moonmist', 'Moose', 'Mooshoo', 'Moptop', 'Mork', 'Morocco', 'Mosaic', 'Moscow', 'Motley', 'Moustache', 'Moxie', 'Mudpie', 'Muffin', 'Mulberry', 'Mumbles', 'Mumford', 'Mumpy', 'Munchkin', 'Murphy', 'Mushmouth', 'Mushroom', 'Mustang', 'Mustard', 'Mutt', 'Muttzie', 'Mylar', 'Nacho', 'Nameless', 'Nardek', 'Nashville', 'Naugahyde', 'Navel', 'Naxos', 'Nectarine', 'Ned', 'Needle', 'Needler', 'Needles', 'Nehru', 'Neon', 'Neptune', 'Network', 'Neuron', 'Neutron', 'Nevada', 'Newt', 'Newton', 'Niagara', 'Nibbler', 'Nibbles', 'Nibbly', 'Niccolo', 'Nickel', 'Nifty', 'Niftykins', 'Nightmare', 'Nim', 'Nimbus', 'Nitro', 'Nix', 'Nixy', 'Noisemaker', 'Nomad', 'Noname', 'Noodles', 'Nooly', 'Norbie', 'Nostrildamus', 'Nosy', 'November', 'Nugget', 'Numbers', 'Nutmeg', 'Oasis', 'Oatcake', 'Oatmeal', 'Oberon', 'Oblong', 'Oboe', 'Obsession', 'Octagon', 'October', 'Oddjob', 'Odzanends', 'Offbeat', 'Ogee', 'Ohio', 'Oink Oink', 'Oinker', 'Okeedoke', 'Okra', 'Oleander', 'Omega', 'Omelet', 'Onion', 'Onionbreath', 'Onionhead', 'Ono', 'Onomatopoeia', 'Onyx', 'Oozy', 'Opaque', 'Opossum', 'Orangeade', 'Orbit', 'Orchid', 'Oregano', 'Original', 'Oriole', 'Orlando', 'Oroonoko', 'Orpheus', 'Orville', 'Oscar', 'Osmosis', 'Ostrich', 'Outie', 'Outlaw', 'Outlet', 'Outrageous', 'Owl', 'Ox', 'Oyster', 'Ozzie', 'PJ', 'Pacemaker', 'Pachyderm', 'Padlock', 'Pagoda', 'Paisley', 'Paladin', 'Palomino', 'Panache', 'Panda', 'Pandemonium', 'Panfried', 'Pantaloon', 'Panther', 'Paprika', 'Papyrus', 'Parachute', 'Paradise', 'Parakeet', 'Parallax', 'Paris', 'Parmesan', 'Parsley', 'Parsnip', 'Pascal', 'Pasternak', 'Patches', 'Patchouli', 'Patchwork', 'Patience', 'Pauper', 'Paws', 'Peachy', 'Peanut', 'Pearl', 'Pebbles', 'Pecan', 'Peck Peck', 'Peepers', 'Peewee', 'Pegasus', 'Pele', 'Pendragon', 'Penguin', 'Peoria', 'Pepper', 'Peppermint', 'Pepperoni', 'Peppy', 'Percival', 'Periwinkle', 'Peroxide', 'Persephone', 'Perseus', 'Persnickety', 'Pesto', 'Pesty', 'Petra', 'Petros', 'Pettibones', 'Phantom', 'Philadelphia', 'Phoenix', 'Phynotaprox', 'Piano', 'Piccolo', 'Pickles', 'Pickwick', 'Pico', 'Piecewise', 'Pigpen', 'Pilaf', 'Pimento', 'Ping', 'Ping Pong', 'Pip', 'Pipsqueak', 'Pistachio', 'Piston', 'Pitabread', 'Pixel', 'Pizza', 'Pizzazz', 'Plato', 'Plumb Bob', 'Plumpy', 'Plunko', 'Pluto', 'Pocket', 'Poco', 'Poe', 'Pointer', 'Pointy', 'Pokey', 'Polaris', 'Polifax', 'Pollywog', 'Poltergeist', 'Pom Pom', 'Poofball', 'Poofy', 'Popcorn', 'Poppy', 'Porcupine', 'Porkchop', 'Portobello', 'Postcard', 'Potbelly', 'Potpie', 'Potzy', 'Pouncer', 'Powder', 'Prancer', 'Preston', 'Pretzel', 'Priscilla', 'Prissy', 'Procyon', 'Prodigy', 'Proton', 'Providence', 'Prowler', 'Proxy', 'Pudding', 'Puddles', 'Pudgy', 'Puff', 'Puffball', 'Puffin', 'Puffy', 'Pugnose', 'Pumpernickel', 'Pumpkin', 'Punch', 'Punky', 'Puree', 'Purrfect', 'Pygmy', 'Pyrex', 'Python', 'Quack Quack', 'Quagmire', 'Quartz', 'Quasar', 'Quasi', 'Queasy', 'Quenby', 'Quesadilla', 'Quester', 'Quetzal', 'Quibbler', 'Quicksand', 'Quicksilver', 'Quinn', 'Quippy', 'Quiqui', 'Quirky', 'Quixote', 'Quizzical', 'Quizzix', 'Rabbit', 'Raccoon', 'Racecar', 'Rachel', 'Radar', 'Radcliffe', 'Radish', 'Radium', 'Radix', 'Radman', 'Raffle', 'Ragamuffin', 'Ragdoll', 'Ragmop', 'Rags', 'Ragtime', 'Ragweed', 'Rainbow', 'Rainstorm', 'Rainwater', 'Raisin', 'Rambler', 'Ramrod', 'Ranger', 'Rascal', 'Raspberry', 'Rathbone', 'Rattler', 'Raven', 'Ravioli', 'Rawhide', 'Raymond', 'Razzmatazz', 'Reactor', 'Recall', 'Recycler', 'Redwood', 'Relay', 'Relic', 'Relish', 'Renegade', 'Repeat', 'Rescuer', 'Retread', 'Rewind', 'Rhapsody', 'Rhinestone', 'Rhino', 'Rhymer', 'Rhythm', 'Ribbons', 'Rickrack', 'Ricochet', 'Riddler', 'Riddles', 'Riffraff', 'Rigatoni', 'Righty', 'Ringleader', 'Ringo', 'Riot', 'Ripley', 'Ripple', 'Ripples', 'Risky', 'Ritz', 'Ritzy', 'Roamer', 'Robin', 'Rocco', 'Rocket', 'Rockhead', 'Rockwell', 'Rococo', 'Rogue', 'Rolex', 'Rollo', 'Roly Poly', 'Ronno', 'Rookie', 'Rooster', 'Roscoe', 'Rosebug', 'Rothchild', 'Rowf', 'Rowser', 'Ruffles', 'Ruggelah', 'Ruggles', 'Rumba', 'Runaway', 'Runt', 'Rushmore', 'Rusty', 'Sabotage', 'Safari', 'Saga', 'Saggy', 'Sagittarius', 'Sahara', 'Salamander', 'Salazar', 'Salinger', 'Salisbury', 'Salsa', 'Salty', 'Sam', 'Samba', 'Sammy', 'Samson', 'Samurai', 'Sandman', 'Sandy', 'Santana', 'Santiago', 'Sasha', 'Sashimi', 'Sasquatch', 'Sassy', 'Satchel', 'Satire', 'Saturn', 'Saucer', 'Saucy', 'Sausage', 'Savage', 'Saxophone', 'Scallop', 'Scamp', 'Scamper', 'Scandal', 'Scarecrow', 'Scary', 'Schlemmer', 'Schmooze', 'Schnook', 'Schnookie', 'Scone', 'Scoops', 'Scoot', 'Scooter', 'Scorpio', 'Scorpion', 'Scoundrel', 'Scout', 'Scrabble', 'Scrambler', 'Scrappy', 'Scrooge', 'Scrumptious', 'Scupper', 'Seagull', 'Seismic', 'Seltzer', 'Seneca', 'September', 'Sepulveda', 'Serengeti', 'Shackles', 'Shamrock', 'Shangri La', 'Sharky', 'Shazam', 'Sheba', 'Shelby', 'Sheldrake', 'Shelley', 'Shelton', 'Shenanigan', 'Shep', 'Sherbet', 'Sherlock', 'Sherwood', 'Shiny', 'Shmunday', 'Shoeless', 'Shogun', 'Shortcake', 'Shortstack', 'Shortstop', 'Shorty', 'Showboat', 'Showoff', 'Shredder', 'Shrimpy', 'Shylock', 'Sideshow', 'Sideways', 'Sidney', 'Silhouette', 'Silverspoon', 'Siren', 'Skeet', 'Skeeter', 'Skelton', 'Skidder', 'Skidoo', 'Skidsy', 'Skinky', 'Skipper', 'Skippy', 'Skunk', 'Skunkmuffin', 'Skunky', 'Sky', 'Skyrocket', 'Slappy', 'Slate', 'Slick', 'Slicker', 'Slippers', 'Sloth', 'Slothful', 'Slugger', 'Sly', 'Smarty', 'Smartypants', 'Smash', 'Smasher', 'Smilestone', 'Smocks', 'Smoke', 'Smoky', 'Smoocher', 'Smoothie', 'Smores', 'Smug', 'Snaggletooth', 'Snapdragon', 'Snappy', 'Snaps', 'Snarly', 'Sneaker', 'Sneakers', 'Sneezer', 'Sneezy', 'Snickers', 'Sniffer', 'Sniffler', 'Sniffles', 'Sniffy', 'Snooker', 'Snookums', 'Snooper', 'Snoots', 'Snooty', 'Snowball', 'Snowberry', 'Snowbunny', 'Snowcap', 'Snowflake', 'Snowpea', 'Snowshoe', 'Snowy', 'Snuffles', 'Snuffy', 'Snugglepot', 'Snuggles', 'Socks', 'Sodapop', 'Soho', 'Sojourner', 'Solo', 'Sonar', 'Sorbet', 'Souffle', 'Soupbowl', 'Soupy', 'Sourball', 'Sourdough', 'Southpaw', 'Spacey', 'Spades', 'Spaghetti', 'Spam', 'Sparkler', 'Sparkplug', 'Sparky', 'Sparrow', 'Sparx', 'Speck', 'Speckles', 'Spectro', 'Spectrum', 'Speedy', 'Spex', 'Sphinx', 'Spicy', 'Spider', 'Spiffy', 'Spike', 'Spiky', 'Spinach', 'Spinner', 'Spiral', 'Spirit', 'Spiro', 'Spitfire', 'Splash', 'Splashy', 'Spoiler', 'Spoof', 'Spooky', 'Sport', 'Sporty', 'Spot', 'Spots', 'Spotty', 'Spring', 'Springbok', 'Springy', 'Sprinkle', 'Sprinkles', 'Spud', 'Spunky', 'Sputnik', 'Spy', 'Squash', 'Squeak', 'Squeaky', 'Squid', 'Squiddly', 'Squidface', 'Squiggle', 'Squiggly', 'Squishy', 'Stalactite', 'Stalagmite', 'Starbuck', 'Stardust', 'Starfire', 'Stargazer', 'Starlight', 'Steamy', 'Steely', 'Stereopsis', 'Sterling', 'Stethoscope', 'Stetson', 'Stewart', 'Sticky', 'Stinger', 'Stingy', 'Stinkwell', 'Stinky', 'Stony', 'Storm', 'Stormy', 'Stowaway', 'Strange', 'Strawberry', 'Strep', 'Stretch', 'Stretchy', 'Stripe', 'Striper', 'Stripes', 'Strudel', 'Stubby', 'Stumpy', 'Sudsy', 'Suede', 'Sugar', 'Sugarbaby', 'Sulfur', 'Sultan', 'Sumo', 'Sundance', 'Sundown', 'Sunflower', 'Sunset', 'Superdoodle', 'Surprise', 'Sushi', 'Swabbie', 'Swampy', 'Sweathog', 'Sweetheart', 'Sweetie Pie', 'Sweetness', 'Sweets', 'Swift', 'Swifty', 'Swizzle', 'Sylvester', 'Synergy', 'Syrup', 'TNT', 'Tablespoon', 'Tabloid', 'Taboo', 'Tacky', 'Taco', 'Tacos', 'Tadpole', 'Taffeta', 'Taffy', 'Tagalong', 'Tags', 'Tahiti', 'Taj', 'Takeout', 'Talisman', 'Tallahassee', 'Tallulah', 'Talon', 'Tamale', 'Tambourine', 'Tandem', 'Tanglewood', 'Tango', 'Tank', 'Tanker', 'Tanner', 'Tantrum', 'Tapestry', 'Tapioca', 'Tapper', 'Tarantula', 'Tardy', 'Target', 'Tarkington', 'Tartan', 'Tasty', 'Tatsu', 'Tatters', 'Tattletale', 'Tattoo', 'Taurus', 'Tawny', 'Taxbreak', 'Taxcut', 'Taxi', 'Taxicab', 'Teacup', 'Teaky', 'Teapot', 'Teaspoon', 'Technicolor', 'Teddy', 'Teehee', 'Teevee', 'Telegram', 'Telepath', 'Telescope', 'Telex', 'Tempest', 'Templeton', 'Tempo', 'Tenderfoot', 'Tennessee', 'Tennisball', 'Tennyson', 'Terence', 'Teriyaki', 'Terror', 'Texas', 'Textbook', 'Thackeray', 'Thaddeus', 'Tharp', 'Tharpo', 'Theoretical', 'Theory', 'Thermos', 'Thickie', 'Thimble', 'Thistle', 'Thorny', 'Thriller', 'Thud', 'Thumbtack', 'Thunder', 'Thunderbird', 'Thurgood', 'Thursday', 'Thyme', 'Tickets', 'Tidbit', 'Tilly', 'Tilted', 'Timbuktu', 'Tinkles', 'Tinsel', 'Tintin', 'Tiny', 'Tipperary', 'Tipsy', 'Titanium', 'Tizzy', 'Toad', 'Toadstool', 'Toady', 'Toaster', 'Toby', 'Toco', 'Toffee', 'Tofu', 'Tokyo', 'Toledo', 'Tomato', 'Tomorrow', 'Tonic', 'Toodleoo', 'Toodles', 'Toot', 'Tooter', 'Toothsome', 'Toothy', 'Tootles', 'Toots', 'Topeka', 'Topper', 'Topsy', 'Tornado', 'Torpedo', 'Tortellini', 'Tortoni', 'Totem', 'Toto', 'Totsy', 'Toucan', 'Toupee', 'Toy', 'Toybox', 'Tracer', 'Trailblazer', 'Tramp', 'Trampoline', 'Trancer', 'Trapper', 'Traveller', 'Treasure', 'Treetop', 'Trekker', 'Trickster', 'Trickstick', 'Tricky', 'Trident', 'Trilogy', 'Trinidad', 'Trinket', 'Trio', 'Tripper', 'Troll', 'Tropix', 'Trouble', 'Trout', 'Trumpet', 'Trusty', 'Tsunami', 'Tuba', 'Tubbo', 'Tubby', 'Tuesday', 'Tuffy', 'Tugboat', 'Tumblebumble', 'Tumbler', 'Tumbleweed', 'Tunafish', 'Tundra', 'Turbo', 'Turkey', 'Turnip', 'Turtleneck', 'Tutu', 'Twaddler', 'Twain', 'Tweezer', 'Twerp', 'Twiggs', 'Twilight', 'Twinkle', 'Twirler', 'Twister', 'Twittery', 'Tycoon', 'Typhoon', 'UFO', 'Ubu', 'Ugly', 'Ukelele', 'Ultimate', 'Ultra', 'Ultrasonic', 'Ultra', 'Umber', 'Umbrella', 'Umpire', 'Underfoot', 'Underwood', 'Unicorn', 'Unique', 'Upbeat', 'Upshot', 'Upside', 'Upstart', 'Uptight', 'Urchin', 'Ursula', 'Utoo', 'Utopia', 'Vacuum', 'Vagabond', 'Valentine', 'Valerie', 'Valiant', 'Vamp', 'Vanderbilt', 'Vanilla', 'Vanity', 'Vaudeville', 'Vegas', 'Velvet', 'Venezuela', 'Vermicelli', 'Vermont', 'Vern', 'Vernon', 'Vertigo', 'Vexy', 'Vibes', 'Victrola', 'Video', 'Viking', 'Vinaigrette', 'Vintage', 'Viper', 'Virtuosity', 'Vivian', 'Voodoo', 'Vulcan', 'Vulture', 'Wabble', 'Wabbler', 'Wacky', 'Waddle', 'Waddler', 'Waddles', 'Wafer', 'Waffle', 'Waffler', 'Waffles', 'Wag', 'Waggles', 'Wags', 'Wagtail', 'Wahoo', 'Waikiki', 'Wallaby', 'Wallaroo', 'Walnut', 'Walnuts', 'Walrus', 'Waltzy', 'Wanderer', 'Warthog', 'Warty', 'Wasco', 'Waterberry', 'Watergate', 'Wavy', 'Waxy', 'Weasel', 'Weaver', 'Webster', 'Wedgewood', 'Wedgie', 'Wednesday', 'Weekend', 'Weepy', 'Weezer', 'Weezie', 'Welcome', 'Wellington', 'Wembly', 'Wendy', 'Wesley', 'Whatchamacallit', 'Whatever', 'Wheatcake', 'Wheedler', 'Whim', 'Whimsy', 'Whipple', 'Whirlwind', 'Whisker', 'Whiskers', 'Whisper', 'Whistler', 'Whistlestop', 'Whittaker', 'Whiz', 'Whizzer', 'Wholesale', 'Whoopdedoo', 'Whoopie', 'Wiggle', 'Wiggler', 'Wiggles', 'Wiggly', 'Wildberry', 'Wildcat', 'Wildflower', 'Wildwood', 'Willy', 'Wily', 'Wimbledon', 'Wimpster', 'Wimpy', 'Windjammer', 'Wing', 'Wink', 'Winker', 'Winkle', 'Winkles', 'Winky', 'Winx', 'Wiretap', 'Wisecrack', 'Wispy', 'Wisteria', 'Wizard', 'Wizkid', 'Wobble', 'Wobbler', 'Wobbles', 'Wobbly', 'Wolverine', 'Wonder', 'Wonderbunny', 'Wonton', 'Wooble', 'Woobles', 'Woobly', 'Woodchuck', 'Woodstock', 'Woodwind', 'Woof Woof', 'Woofer', 'Woolly', 'Woolworth', 'Wordsworth', 'Worm', 'Wormy', 'Wrex', 'Wriggler', 'Wriggles', 'Wriggly', 'Wrinkle', 'Wrinkler', 'Wrinkles', 'Wuggums', 'Wumpus', 'Wuzzie', 'Wyoming', 'Xanadu', 'Xenobia', 'Xifto', 'Xinx', 'Xinxu', 'Xippy', 'Xowie', 'Xoxo', 'Xoxxy', 'Xpresso', 'Yahoo', 'Yammie', 'Yancy', 'Yappy', 'Yardstick', 'Yasu', 'Yeasty', 'Yellowstone', 'Yelper', 'Yertle', 'Yesterday', 'Yeti', 'Yippie', 'Yodeler', 'Yoga', 'Yoko', 'Yonder', 'Yonkers', 'Yorty', 'Yosemite', 'Yukon', 'Yummy', 'Yutu', 'Yvonne', 'Zack', 'Zadok', 'Zaftig', 'Zaire', 'Zapata', 'Zappa', 'Zazen', 'Zebu', 'Zebulon', 'Zen', 'Zenith', 'Zenzen', 'Zepellin', 'Zephyr', 'Zeppo', 'Zero', 'Zesty', 'Zigzag', 'Zilch', 'Zillion', 'Zing', 'Zinger', 'Zingy', 'Zipcode', 'Zircon', 'Zodiac', 'Zoltan', 'Zonk', 'Zoo', 'Zooble', 'Zoom', 'Zoomer', 'Zoomy', 'Zowie', 'Zucchini', 'Zylon']
PetNameDictionary = {}
id = 0

for dictionary in [BoyPetNames, GirlPetNames, NeutralPetNames]:
    for name in dictionary:
        PetNameDictionary[id] = name
        id += 1

def getPetName(uniqueID):
    try:
        return PetNameDictionary[uniqueID]
    except:
        return PetNameDictionary[0]

def getRandomPetName(gender = None, seed = None):
    if seed is not None:
        random.seed(seed)

    nameList = list(NeutralPetNames)

    if gender == 0:
        nameList += BoyPetNames
    else:
        nameList += GirlPetNames

    return random.choice(nameList)

def getPetNameId(name):
    for key, value in PetNameDictionary.items():
        if name == value:
            return key

    return 0

DonaldChatter = ["I'm glad you're here today!",
 "You look like you're having fun.",
 "Oh boy, I'm having a good day.",
 'I hope you are enjoying your ride!',
 'I like meeting new people.',
 'Have fun in my neighborhood.',
 'I like to make people laugh.',
 'Watch out for the Cogs!',
 'Come aboard!',
 "I heard it's snowing at the Brrrgh.",
 'Looks like the trolley is coming!',
 'Sometimes I play trolley games just to eat the fruit pie!',
 'I hope you are enjoying your stay in Toontown!',
 'I like what you are wearing.',
 'I love to play tag. Do you?']
NPCFriendUnavailable = 'Unavailable'

InVP = ' in a V.P. Battle'
InFieldOffice = ' in a Sellbot Field Office'
CogPanelLevel = 'Level %s'
CogPanelSkeleton = 'Skelecog'
CogPanelVirtual = 'Virtual'
CogPanelRevives = 'v%s.0'
CogPanelWaiter = 'Waiter'

ToonDefeatedMessage = '%s was defeated!'

CogInterfaceLabelOn = 'The cog battle interface is on.'
CogInterfaceLabelOff = 'The cog battle interface is off.'
FieldOfViewLabel = 'Field of View:'
NametagStyleLabel = 'Nametag Style:'
NametagColorLabel = 'Nametag Color:'
NametagPanelLabel = 'Nametag Panel:'
FishingPoleLabel = 'Fishing Rod:'
CheesyEffectLabel = 'Cheesy Effect:'
TTOAspectRatioLabel = 'TTO Aspect Ratio:'
discordPresenceLabel = 'Discord Presence:'
discordPresenceButton = 'Discord Presence'

KeybindLabel = 'Keybinds:'
KeybindButton = 'Update'
KeybindDialogTitle = 'Keybinds'
KeybindInstructions = 'Press any key to update the %s key.'
OfficialKeybindNames = ['Move Up', 'Move Down', 'Move Left', 'Move Right', 'Enter Chat', 'Fire/Jump', 'Action', 'Screenshot', 'Map', 'Sprint']

BossLocations = {
 'c': 'Bossbot Clubhouse\nBanquet',
 'l': "Lawbot Courthouse\nBumpy Bumblebehr's Trial",
 'm': 'Cashbot Treasury Vault',
 's': 'Sellbot Towers\nRooftop'
}
SendCogBossTaunts = {
 's': [
  "We're going door to door to give you an dedious offer.",
  "It's time for your estimated cost.",
  'You toons never learn when to snatch up a great deal.',
  "Call now and we'll reduce your laff, absolutely free.",
  'Sell, sell, sell!',
  'Let us Sellbots give you a helping hand.',
  'The deal has only just begun.',
  'Going sad already? How about we settle a retirement plan.',
  'Get them! Get them all!'
 ],
 'm': [
  "Let's show you how money talks.",
  "We'll bring you into bankruptcy.",
  'The Jellybean is only worth a tenth of the cogbuck!',
  'Hey! Those cogs cost me money!',
  "I'll put you on the next train back to the playground!",
  'You toons are wasting so much of your currency fighting us.',
  'It seems Toontown has high amounts of debt to the Cogs.',
  "Invest in Cogbucks, it'll fix Toontown right up!",
  'Do toons understand the value of money?'
 ],
 'l': [
  'Order in the court!',
  'The defendant is appearing to be proven guilty.',
  'Justice is important to keep a stable society.',
  'Toontown will be full of corruption and greed.',
  'Toons do not understand the importance of the Cog order.',
  'The state of your actions will prove you toons guilty.',
  "Bah! Don't you tell me how to run a trial!",
  'My decision will state what to legally do to you Toons.',
  'This blindfold protects me from the horrible corruption!'
 ]
}
VPRampMessage = "I don't have time for this, I'm late for my meeting!"
VPDeathTaunt = "WAAAH! YOU HAVEN'T SEEN THE LAST OF ME!"
DirectedAttackBossTaunts = {
 's': [
  'Have a free sample!',
  'I see you over there!',
  'My products beat out all of Toontown!',
  "Don't think I've skipped you, %(toon)s!"
 ],
 'm': [
  "Here's money well spent.",
  'Hey! Get away from that crane!',
  'Stop!',
  '%(toon)s, get over here!'
 ],
 'c': [
  'These are brand new tables!',
  "A little water isn't going to affect me!",
  'Bug off! This is my clubhouse!',
  "You've ruined my banquet! Now you'll pay!"
 ]
}
VPSpinMessages = [
 "Let's get these ideas going!",
 "I wouldn't get too close. My patents protect these gears.",
 'Why worry about problems when you can shake them off?',
 "I may be old, but I'm still reliable."
]
JumpBossTaunts = {
 's': [
  'STOP!',
  'Pay attention to my pitch!',
  'This is a waste of my time!',
  'Time to send you back to the playground!'
 ],
 'l': [
  "You're all in contempt of court!"
 ],
 'm': [
  "These Goons weren't free you know!",
  'HEY, THOSE ARE VINTAGE SAFES!',
  'This will cost you a lot more than candy!',
  "I'll buy out Toontown if it means getting rid of you Toons!"
 ]
}
CEOSpeech = [
 "Good evening Cogs, it's an honor having you here tonight in the Bossbot Clubhouse.",
 'I apologize for sending invitations on such short notice, but your presence is urgent.',
 'Lately, it appears the Toons have created strategies to fight against us.',
 "This is a sign that each day us Cogs are getting weaker, and they're getting stronger.",
 'I have gathered you all here today not only to state this problem, but to propose an idea.',
 'This idea is the same one that was mentioned in the meeting 3 weeks ago, as to hire a new department of employees.',
 'If we were to do such however, they would be more or less assisting over attacking.',
 'We also can consider the odds that a department would have to be treated special.',
 'On another note, business operations are higher than ever.',
 'Because of this, improvement for HQs will be funded.',
 'And thus we, the Cog Nation, are striving.',
 'I am very delighted by this news, I just wanted to thank you all for working so hard for this news.',
 "Wait, what's going on? I can't see but I hear explosions."
] # Len of words + 10

TitleScreenPlayButton = 'Play'
TitleScreenSettingsButton = 'Settings'
TitleScreenQuitButton = 'Quit'
TitleScreenDoneButton = 'Done'

ChairAskToUse = 'Would you like to sit on this chair?'

FriendSecretIntro = "If you are playing with someone you know in the real world, you can become True Friends.  You can chat using the keyboard with your True Friends.  Other Toons won't understand what you're saying.\n\nYou do this by getting a True Friend Code.  Tell the True Friend Code to your friend, but not to anyone else.  When your friend types in your True Friend Code on his or her screen, you'll be True Friends in Toontown!"
FriendSecretGetSecret = 'Get a True Friend Code'
FriendSecretEnterSecret = 'If you have a True Friend Code from someone you know, type it here.'
FriendSecretOK = lOK
FriendSecretEnter = 'Enter True Friend Code'
FriendSecretCancel = lCancel
FriendSecretGettingSecret = 'Getting True Friend Code. . .'
FriendSecretGotSecret = "Here is your new True Friend Code.  Be sure to write it down!\n\nYou may give this True Friend Code to one person only.  Once someone types in your True Friend Code, it will not work for anyone else.  If you want to give a True Friend Code to more than one person, get another True Friend Code.\n\nThe True Friend Code will only work for the next three days.  Your friend will have to type it in before it goes away, or it won't work.\n\nYour True Friend Code is:"
FriendSecretTooMany = "Sorry, you can't have any more True Friend Codes today.  You've already had more than your fair share!\n\nTry again tomorrow."
FriendSecretTryingSecret = 'Trying True Friend Code. . .'
FriendSecretEnteredSecretUnknown = "That's not anyone's True Friend Code.  Are you sure you spelled it correctly?\n\nIf you did type it correctly, it may have expired.  Ask your friend to get a new True Friend Code for you (or get a new one yourself and give it to your friend)."
FriendSecretEnteredSecretFullYou = "You can't be True Friends because you have too many friends on your friends list."
FriendSecretEnteredSecretFullHim = "You can't be True Friends because %s has too many friends on his friends list."
FriendSecretAlreadyFriends = 'You are already True Friends!'
FriendSecretAlreadyFriendsName = 'You are already True Friends with %s!'
FriendSecretEnteredSecretSelf = 'You just typed in your own True Friend Code!'
FriendSecretTooFast = 'You are redeeming codes too fast! Please wait a few seconds.'
FriendSecretNowFriends = 'You are now True Friends with %s!'

GroupAskAccess = 'Would you like to teleport %s %s in %s?'

GagPopup = '%s: %s\nGags: %s'

ColorfulToon = 'Vibrant'
ColorAdvanced = 'Advanced'
ColorBasic = 'Basic'
ColorAll = 'All'

ShardPagePreferred = 'Preferred'
ShardPageShardTitle = '%s Population: %s'
ShardPageTeleport = 'Teleport to\n%s'

TeleportButton = 'Teleport'
TeleportButtonNoMoney = 'Sorry, but you need %s jellybeans to teleport!'
TeleportButtonConfirm = 'Would you like to spend %s jellybeans to teleport?'
TeleportButtonTakenOver = 'Sorry, but this shop has been taken over by the Cogs!'

BattleCogPopup = '%s/%s HP\n\n\x01androidGreen\x01Group attacks:\x02\n%s\n\n\x01androidGreen\x01Regular attacks:\x02\n%s'
BattleCogPopupAttack = '%s %s HP'
BattleCogPopupAttackDanger = '\x01red\x01' + BattleCogPopupAttack + '\x02'
BattleCogPopupDanger = '\x01red\x01Dangerous!\x02\n\n'
BattleCogPopupDangerColor = '\x01red'
BattleCogNoAttacks = 'None'

BattleGagPopup = '%s: %s\nGags left: %s'
BattleSOSPopup = '\x01azure\x01%s\x02\n%s\n%s%s stars\nSOS left: %s'
BattleSOSPopupHeal = 'Heals'
BattleSOSPopupHarm = 'Deals'
BattleSOSPopupHP = '%s %s HP\n'

DetailPanelSOS = 'SOS Cards'

TeleportLabelOn = 'Accepting teleports.'
TeleportLabelOff = 'Not accepting teleports.'
TeleportPanelNoTeleport = '%s needs some time alone right now.'

InventoryDeleteAll = 'DELETE ALL'
InventoryDeleteConfirm = "Are you sure you want to delete all your gags? Don't worry, your level 7 gags are safe!"

ClothesGUICount = '%s/%s'

FpsMeterLabelOn = 'The frame rate meter is on.'
FpsMeterLabelOff = 'The frame rate meter is off.'

DefaultDoodleName = 'Smiley'

CheesyEffectNames = ['Normal',
 'Big Head',
 'Small Head',
 'Big Legs',
 'Small Legs',
 'Big Toon',
 'Small Toon',
 'Flat Portrait',
 'Flat Profile',
 'Transparent',
 'No Color',
 'Invisible',
 'Pumpkin',
 'Big White',
 'Snowman',
 'Green Toon']
CheesyEffectDesc = ['???',
 "Increases the size of your Toon's head",
 "Decreases the size of your Toon's head",
 "Increases the size of your Toon's legs",
 "Decreases the size of your Toon's legs",
 "Increases the size of your Toon",
 "Decreases the size of your Toon",
 "Makes your Toon only visible in the front and back",
 "Makes your Toon only visible on your sides",
 "Makes your Toon appear transparent",
 "Makes your Toon completely white",
 "Makes your Toon mostly invisible",
 '???',
 '???',
 '???',
 '???']

WarnMessage = 'You have been warned by a cast member for: %s. Behave, or you shall receive punishment.'
DistrictDifficulty = 'Difficulty: {0}' 
DistrictDifficultyNames = ['Normal',
 'Hard',
 'Extreme']

FactoryRewardMessageExtreme = "Way to go! That was a long run. You've earned a {0} SOS card and 1000 jellybeans!"
FactoryRewardMessageHard = "Way to go! You've crushed those harder Cogs! You've earned a {0} SOS card and 500 jellybeans!"

NoSprint = "You can't sprint here!"

GiftJellybeanTitle = 'Gift Jellybeans'
GiftJellybeanEnter = 'Enter Amount'
GiftJellybeanGifting = 'Gifting...'
GiftJellybeanInvalidJellybeans = 'Invalid number!'
GiftJellybeanTooMuchJellybeans = 'Not enough jellybeans!'
GiftJellybeanSuccess = 'Success!'
GiftJellybeanFullMailbox = 'Full mailbox!'

NPCFriendPageDeleteConfirmation = 'Are you sure you want to delete ALL of your %s SOS cards?'

CannotRaceHere = "You can't race here!"
NoKartAvailable = "You don't have a kart!"
KartToggleTooFast = "Toggling kart too fast!"