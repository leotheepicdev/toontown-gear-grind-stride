@echo off
cd "../../lib/astron/"

IF NOT EXIST databases mkdir databases
IF NOT EXIST databases/astrondb mkdir databases\astrondb
astrond --loglevel info config/cluster_tls_dev.yml
pause
