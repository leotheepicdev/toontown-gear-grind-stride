@echo off
cd "../../lib/astron/"

IF NOT EXIST databases mkdir databases
IF NOT EXIST databases/astrondb mkdir databases\astrondb
astrond --pretty --loglevel info config/cluster_mongo.yml
pause
