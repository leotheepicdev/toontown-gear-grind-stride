#!/bin/sh
cd ../../lib/astron
mkdir databases
cd databases
mkdir astrondb
cd ..

while [ true ]
do
  ./astrondlinux --loglevel info config/cluster_tls_mongo_dev.yml
done