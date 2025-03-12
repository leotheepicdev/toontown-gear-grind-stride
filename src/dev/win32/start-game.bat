@echo off

title Toontown Gear Grind Game Launcher

echo Choose your connection method!
echo.
echo #1 - Localhost
echo #2 - Developer Server (Sanae Server)
echo #3 - Custom
echo #4 - Local RemoteDB
echo #5 - Prod Server
echo #6 - Rockets Server
echo.

:selection

set INPUT=-1
set /P INPUT=Selection: 

if %INPUT%==1 (
    set TT_GAMESERVER=127.0.0.1
) else if %INPUT%==2 (
    set TT_GAMESERVER=game.gogeargrind.com
) else if %INPUT%==4 (
    set TT_GAMESERVER=127.0.0.1
) else if %INPUT%==5 (
    SET TT_GAMESERVER=lw2.ez-webz.com:7198
) else if %INPUT%==6 (
    SET TT_GAMESERVER=91.211.245.8
) else if %INPUT%==3 (
    echo.
    set /P TT_GAMESERVER=Gameserver: 
) else (
	goto selection
)

echo.

if %INPUT%==2 (
    set /P TT_PLAYCOOKIE="Username: "
    set /P ttPassword="Password: "
) else if %INPUT%==4 (
    set /P ttUsername="Username: "
    set /P ttPassword="Password: "
) else (
    set /P TT_PLAYCOOKIE=Username: 
)

echo.

echo ===============================
echo Starting Toontown Gear Grind...
echo Python: "panda3d/python/python.exe"

if %INPUT%==2 (
    echo Username: %TT_PLAYCOOKIE%
) else if %INPUT%==4 (
    echo Username: %ttUsername%
) else (
    echo Username: %TT_PLAYCOOKIE%
)

echo Gameserver: %TT_GAMESERVER%
echo ===============================

cd ../../

:main
if %INPUT%==2 (
    "panda3d/python/python.exe" -m toontown.base.ClientStart
) else if %INPUT%==4 (
    "panda3d/python/python.exe" -m toontown.base.ClientStart
) else (
    "panda3d/python/python.exe" -m toontown.base.ClientStart
)
pause

goto main
