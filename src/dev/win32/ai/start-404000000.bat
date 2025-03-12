@echo off

rem Define some constants for our AI server:
set MAX_CHANNELS=999999
set STATESERVER=4002
set ASTRON_IP=127.0.0.1:7100
set EVENTLOGGER_IP=127.0.0.1:7198

rem Get the user input:
set DISTRICT_NAME=Kooky Grove
set DISTRICT_DIFFICULTY=0
set BASE_CHANNEL=404000000

echo ===============================
echo Starting Toontown Gear Grind AI server...
echo Python: "C:\Panda3D-GearGrind\python\python.exe"
echo District name: %DISTRICT_NAME%
echo District difficulty: %DISTRICT_DIFFICULTY%
echo Base channel: %BASE_CHANNEL%
echo Max channels: %MAX_CHANNELS%
echo State Server: %STATESERVER%
echo Astron IP: %ASTRON_IP%
echo Event Logger IP: %EVENTLOGGER_IP%
echo ===============================

cd ../../../

:main
"C:\Panda3D-GearGrind\python\python.exe" ^
	-m toontown.ai.ServiceStart ^
	--base-channel %BASE_CHANNEL% ^
	--max-channels %MAX_CHANNELS% ^
	--stateserver %STATESERVER% ^
	--astron-ip %ASTRON_IP% ^
	--eventlogger-ip %EVENTLOGGER_IP% ^
	--district-name "%DISTRICT_NAME%" ^
    --district-difficulty "%DISTRICT_DIFFICULTY%"
goto main
