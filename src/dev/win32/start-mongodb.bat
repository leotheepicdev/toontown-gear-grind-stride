@echo off
title Toontown Gear Grind - MongoDB Service

cd ../../lib/astron/

:main
IF NOT EXIST databases mkdir databases
IF NOT EXIST databases/astrondb mkdir databases\astrondb
cd mongodb
mkdir database
cd ..

"mongodb\bin\mongod.exe" --auth --config "mongodb\bin\mongod.cfg" --dbpath mongodb/database
pause
goto :main