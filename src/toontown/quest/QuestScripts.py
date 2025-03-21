script = '''
ID quest_assign_101
CLEAR_CHAT npc
LOAD squirt1 "phase_3.5/models/gui/tutorial_gui" "squirt1"
LOAD squirt2 "phase_3.5/models/gui/tutorial_gui" "squirt2"
LOAD toonBuilding "phase_3.5/models/gui/tutorial_gui" "toon_buildings"
LOAD cogBuilding "phase_3.5/models/gui/tutorial_gui" "suit_buildings"
LOAD cogs "phase_3.5/models/gui/tutorial_gui" "suits"
POSHPRSCALE cogs -1.05 7 0 0 0 0 1 1 1
POSHPRSCALE toonBuilding -1.05 7 0 0 0 0 1.875 1.875 1.875
POSHPRSCALE cogBuilding -1.05 7 0 0 0 0 1.875 1.875 1.875
POSHPRSCALE squirt1 -1.05 7 0 0 0 0 1.875 1.875 1.875
POSHPRSCALE squirt2 -1.05 7 0 0 0 0 1.875 1.875 1.875
WRTREPARENTTO camera npc
LERP_POSHPRSCALE camera 2.8 0.0 3.5 35 5 0 1 1 1 1.5
WRTREPARENTTO camera localToon
PLAY_ANIM npc "right-hand-start" 1
WAIT 1
REPARENTTO cogs camera
LERP_SCALE cogs 1.875 1.875 1.875 0.5
WAIT 1.0833
LOOP_ANIM npc "right-hand" 1
FUNCTION npc "angryEyes"
FUNCTION npc "blinkEyes"
LOCAL_CHAT_CONFIRM npc QuestScript101_1 "CFReversed"
LOCAL_CHAT_CONFIRM npc QuestScript101_2 "CFReversed"
REPARENTTO cogs hidden
REPARENTTO toonBuilding camera
LOCAL_CHAT_CONFIRM npc QuestScript101_3 "CFReversed"
REPARENTTO toonBuilding hidden
REPARENTTO cogBuilding camera
FUNCTION npc "sadEyes"
FUNCTION npc "blinkEyes"
LOCAL_CHAT_CONFIRM npc QuestScript101_4 "CFReversed"
REPARENTTO cogBuilding hidden
REPARENTTO squirt1 camera
FUNCTION npc "normalEyes"
FUNCTION npc "blinkEyes"
LOCAL_CHAT_CONFIRM npc QuestScript101_5 "CFReversed"
REPARENTTO squirt1 hidden
REPARENTTO squirt2 camera
LOCAL_CHAT_CONFIRM npc QuestScript101_6 "CFReversed"
LERP_SCALE squirt2 1 1 0.01 0.5
WAIT 0.5
REPARENTTO squirt2 hidden
OBSCURE_LAFFMETER 0
SHOW laffMeter
POS laffMeter 0.153 0.0 0.13
SCALE laffMeter 0.0 0.0 0.0
WRTREPARENTTO laffMeter aspect2d
LERP_POS laffMeter -0.25 0 -0.15 1
LERP_SCALE laffMeter 0.2 0.2 0.2 0.6
WAIT 1.0833
LOOP_ANIM npc "right-hand"
LOCAL_CHAT_CONFIRM npc QuestScript101_8 "CFReversed"
LOCAL_CHAT_CONFIRM npc QuestScript101_9 "CFReversed"
FUNCTION npc "sadEyes"
FUNCTION npc "blinkEyes"
LAFFMETER 15 15
WAIT 0.1
LAFFMETER 14 15
WAIT 0.1
LAFFMETER 13 15
WAIT 0.1
LAFFMETER 12 15
WAIT 0.1
LAFFMETER 11 15
WAIT 0.1
LAFFMETER 10 15
WAIT 0.1
LAFFMETER 9 15
WAIT 0.1
LAFFMETER 8 15
WAIT 0.1
LAFFMETER 7 15
WAIT 0.1
LAFFMETER 6 15
WAIT 0.1
LAFFMETER 5 15
WAIT 0.1
LAFFMETER 4 15
WAIT 0.1
LAFFMETER 3 15
WAIT 0.1
LAFFMETER 2 15
WAIT 0.1
LAFFMETER 1 15
WAIT 0.1
LAFFMETER 0 15
LOCAL_CHAT_CONFIRM npc QuestScript101_10 "CFReversed"
FUNCTION npc "normalEyes"
FUNCTION npc "blinkEyes"
LAFFMETER 15 15
WRTREPARENTTO laffMeter bottomLeft
WAIT 0.5
LERP_POS laffMeter 0.153 0.0 0.13 0.6
LERP_SCALE laffMeter 0.075 0.075 0.075 0.6
PLAY_ANIM npc "right-hand-start" -2
WAIT 1.0625
LOOP_ANIM npc "neutral"
WAIT 0.5
LERP_HPR npc -50 0 0 0.5
FUNCTION npc "surpriseEyes"
FUNCTION npc "showSurpriseMuzzle"
PLAY_ANIM npc "right-point-start" 1.5
WAIT 0.6944
LOOP_ANIM npc "right-point"
LOCAL_CHAT_CONFIRM npc QuestScript101_11 "CFReversed"
LOCAL_CHAT_CONFIRM npc QuestScript101_12 "CFReversed"
PLAY_ANIM npc "right-point-start" -1
LERP_HPR npc -0.068 0 0 0.75
WAIT 1.0417
FUNCTION npc "angryEyes"
FUNCTION npc "blinkEyes"
FUNCTION npc "hideSurpriseMuzzle"
LOOP_ANIM npc "neutral"
FUNCTION localToon "questPage.showQuestsOnscreenTutorial"
LOCAL_CHAT_CONFIRM npc QuestScript101_13 "CFReversed"
FUNCTION localToon "questPage.hideQuestsOnscreenTutorial"
LOCAL_CHAT_CONFIRM npc QuestScript101_14 1 "CFReversed"
FUNCTION npc "normalEyes"
FUNCTION npc "blinkEyes"
UPON_TIMEOUT FUNCTION cogs "removeNode"
UPON_TIMEOUT FUNCTION toonBuilding "removeNode"
UPON_TIMEOUT FUNCTION cogBuilding "removeNode"
UPON_TIMEOUT FUNCTION squirt1 "removeNode"
UPON_TIMEOUT FUNCTION squirt2 "removeNode"
UPON_TIMEOUT LOOP_ANIM npc "neutral"
UPON_TIMEOUT SHOW laffMeter
UPON_TIMEOUT REPARENTTO laffMeter bottomLeft
UPON_TIMEOUT POS laffMeter 0.15 0 0.13
UPON_TIMEOUT SCALE laffMeter 0.075 0.075 0.075
POS localToon 0.776 14.6 0
HPR localToon 47.5 0 0
FINISH_QUEST_MOVIE


ID quest_incomplete_110
LOCAL_CHAT_CONFIRM npc QuestScript110_1
OBSCURE_BOOK 0
REPARENTTO bookOpenButton aspect2d
SHOW bookOpenButton
POS bookOpenButton 0 0 0
SCALE bookOpenButton 0.5 0.5 0.5
LERP_COLOR_SCALE bookOpenButton 1 1 1 0 1 1 1 1 0.5
WRTREPARENTTO bookOpenButton bottomRight
WAIT 1.5
LERP_POS bookOpenButton -0.158 0 0.17 1
LERP_SCALE bookOpenButton 0.305 0.305 0.305 1
WAIT 1
LOCAL_CHAT_CONFIRM npc QuestScript110_2
REPARENTTO arrows bottomRight
ARROWS_ON -0.41 0.11 0 -0.11 0.36 90
LOCAL_CHAT_PERSIST npc QuestScript110_3
WAIT_EVENT "enterStickerBook"
ARROWS_OFF
SHOW_BOOK
HIDE bookPrevArrow
HIDE bookNextArrow
CLEAR_CHAT npc
WAIT 0.5
TOON_HEAD npc -0.2 -0.45 1
LOCAL_CHAT_CONFIRM npc QuestScript110_4
REPARENTTO arrows aspect2d
ARROWS_ON 0.85 -0.75 -90 0.85 -0.75 -90
SHOW bookNextArrow
LOCAL_CHAT_PERSIST npc QuestScript110_5
WAIT_EVENT "stickerBookPageChange-3"
HIDE bookPrevArrow
HIDE bookNextArrow
ARROWS_OFF
CLEAR_CHAT npc
WAIT 0.5
LOCAL_CHAT_CONFIRM npc QuestScript110_6
ARROWS_ON 0.85 -0.75 -90 0.85 -0.75 -90
SHOW bookNextArrow
LOCAL_CHAT_PERSIST npc QuestScript110_7
WAIT_EVENT "stickerBookPageChange-4"
HIDE bookNextArrow
HIDE bookPrevArrow
ARROWS_OFF
CLEAR_CHAT npc
LOCAL_CHAT_CONFIRM npc QuestScript110_8
LOCAL_CHAT_CONFIRM npc QuestScript110_9
LOCAL_CHAT_PERSIST npc QuestScript110_10
ENABLE_CLOSE_BOOK
REPARENTTO arrows bottomRight
ARROWS_ON -0.41 0.11 0 -0.11 0.36 90
WAIT_EVENT "exitStickerBook"
ARROWS_OFF
TOON_HEAD npc 0 0 0
HIDE_BOOK
HIDE bookOpenButton
LOCAL_CHAT_CONFIRM npc QuestScript110_11 1
UPON_TIMEOUT OBSCURE_BOOK 0
UPON_TIMEOUT ARROWS_OFF
UPON_TIMEOUT REPARENTTO arrows aspect2d
UPON_TIMEOUT HIDE_BOOK
UPON_TIMEOUT COLOR_SCALE bookOpenButton 1 1 1 1
UPON_TIMEOUT POS bookOpenButton -0.158 0 0.17
UPON_TIMEOUT SCALE bookOpenButton 0.305 0.305 0.305
UPON_TIMEOUT TOON_HEAD npc 0 0 0
UPON_TIMEOUT SHOW bookOpenButton
FINISH_QUEST_MOVIE

ID tutorial_blocker
HIDE localToon
REPARENTTO camera npc
FUNCTION npc "stopLookAround"
POS camera 0.0 6.0 4.0
HPR camera 180.0 0.0 0.0
LOCAL_CHAT_CONFIRM npc QuestScriptTutorialBlocker_1
WAIT 0.8 
LOCAL_CHAT_CONFIRM npc QuestScriptTutorialBlocker_2
WAIT 0.8 
POS camera -5.0 -9.0 6.0
HPR camera -25.0 -10.0 0.0
POS localToon 203.8 18.64 -0.475
HPR localToon -90.0 0.0 0.0
SHOW localToon
LOCAL_CHAT_CONFIRM npc QuestScriptTutorialBlocker_3
OBSCURE_CHAT 1 0 0
REPARENTTO chatScButton aspect2d
SHOW chatScButton
POS chatScButton -0.3 0 -0.1
SCALE chatScButton 2.0 2.0 2.0
LERP_COLOR_SCALE chatScButton 1 1 1 0 1 1 1 1 0.5
WRTREPARENTTO chatScButton topLeft
WAIT 0.5
LERP_POS chatScButton 0.204 0 -0.072 0.6
LERP_SCALE chatScButton 1.179 1.179 1.179 0.6
WAIT 0.6 
REPARENTTO arrows topLeft
ARROWS_ON 0.41 -0.09 180 0.21 -0.26 -90
LOCAL_CHAT_PERSIST npc QuestScriptTutorialBlocker_4
WAIT_EVENT "enterSpeedChat"
ARROWS_OFF
BLACK_TOON_LISTEN 1
WAIT_EVENT "SCChatEvent"
BLACK_TOON_LISTEN 0
WAIT 0.5
CLEAR_CHAT localToon
REPARENTTO camera localToon
LOCAL_CHAT_CONFIRM npc QuestScriptTutorialBlocker_5 "CFReversed"
LOCAL_CHAT_CONFIRM npc QuestScriptTutorialBlocker_6 "CFReversed"
OBSCURE_CHAT 0 0 0
REPARENTTO chatNormalButton aspect2d
SHOW chatNormalButton
POS chatNormalButton -0.3 0 -0.1
SCALE chatNormalButton 2.0 2.0 2.0
LERP_COLOR_SCALE chatNormalButton 1 1 1 0 1 1 1 1 0.5
WAIT 0.5
WRTREPARENTTO chatNormalButton topLeft
LERP_POS chatNormalButton 0.068 0 -0.072 0.6
LERP_SCALE chatNormalButton 1.179 1.179 1.179 0.6
WAIT 0.6
TUTORIAL_ACK_DONE
LOCAL_CHAT_CONFIRM npc QuestScriptTutorialBlocker_7 "CFReversed"
LOCAL_CHAT_CONFIRM npc QuestScriptTutorialBlocker_8 1 "CFReversed"
LOOP_ANIM npc "walk"
LERP_HPR npc 270 0 0 0.5
WAIT 0.5
LOOP_ANIM npc "run"
LERP_POS npc 217.4 18.81 -0.475 0.75 
LERP_HPR npc 240 0 0 0.75 
WAIT 0.75
LERP_POS npc 222.4 15.0 -0.475 0.35
LERP_HPR npc 180 0 0 0.35
WAIT 0.35
LERP_POS npc 222.4 5.0 -0.475 0.75
WAIT 0.75
REPARENTTO npc hidden
FREE_LOCALTOON
UPON_TIMEOUT ARROWS_OFF
UPON_TIMEOUT REPARENTTO arrows aspect2d
UPON_TIMEOUT POS chatScButton 0.204 0 -0.072
UPON_TIMEOUT SCALE chatScButton 1.179 1.179 1.179 
UPON_TIMEOUT POS chatNormalButton 0.068 0 -0.072
UPON_TIMEOUT SCALE chatNormalButton 1.179 1.179 1.179 
UPON_TIMEOUT OBSCURE_CHAT 0 0 0
UPON_TIMEOUT REPARENTTO camera localToon
FINISH_QUEST_MOVIE

ID quest_incomplete_145
CHAT_CONFIRM npc QuestScript145_1 1
LOAD frame "phase_4/models/gui/tfa_images" "FrameBlankA"
LOAD tunnel "phase_4/models/gui/tfa_images" "tunnelSignA"
POSHPRSCALE tunnel 0 0 0 0 0 0 0.8 0.8 0.8
REPARENTTO tunnel frame
POSHPRSCALE frame 0 0 0 0 0 0 0.1 0.1 0.1
REPARENTTO frame aspect2d
LERP_SCALE frame 1.0 1.0 1.0 1.0
WAIT 3.0
LERP_SCALE frame 0.1 0.1 0.1 0.5
WAIT 0.5
REPARENTTO frame hidden
CHAT_CONFIRM npc QuestScript145_2 1
UPON_TIMEOUT FUNCTION frame "removeNode"
FINISH_QUEST_MOVIE

ID quest_incomplete_150
CHAT_CONFIRM npc QuestScript150_1
ARROWS_ON  1.05 0.51 -120 1.05 0.51 -120
SHOW_FRIENDS_LIST
CHAT_CONFIRM npc QuestScript150_2
ARROWS_OFF
HIDE_FRIENDS_LIST
CHAT_CONFIRM npc QuestScript150_3
HIDE bFriendsList
CHAT_CONFIRM npc QuestScript150_4 1
UPON_TIMEOUT HIDE_FRIENDS_LIST
UPON_TIMEOUT ARROWS_OFF
FINISH_QUEST_MOVIE
'''