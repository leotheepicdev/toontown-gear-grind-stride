#!/bin/sh
cd ../..

# Define some constants for our AI server:
MAX_CHANNELS=999999
STATESERVER=4002
ASTRON_IP="127.0.0.1:7100"
EVENTLOGGER_IP="127.0.0.1:7198"

# Get the user input:
read -p "District name (DEFAULT: Nuttyboro): " DISTRICT_NAME
DISTRICT_NAME=${DISTRICT_NAME:-Nuttyboro}
read -p "Base channel (DEFAULT: 401000000): " BASE_CHANNEL
BASE_CHANNEL=${BASE_CHANNEL:-401000000}
read -p "District difficulty (DEFAULT: 0): " DISTRICT_DIFFICULTY
DISTRICT_DIFFICULTY=${DISTRICT_DIFFICULTY:-0}

echo "==============================="
echo "Starting Toontown Gear Grind AI server..."
echo "District name: $DISTRICT_NAME"
echo "District difficulty: $DISTRICT_DIFFICULTY"
echo "Base channel: $BASE_CHANNEL"
echo "Max channels: $MAX_CHANNELS"
echo "State Server: $STATESERVER"
echo "Astron IP: $ASTRON_IP"
echo "Event Logger IP: $EVENTLOGGER_IP"
echo "==============================="

while [ true ]
do
    /usr/bin/python2 -m toontown.ai.ServiceStart --base-channel $BASE_CHANNEL \
                     --max-channels $MAX_CHANNELS --stateserver $STATESERVER \
                     --astron-ip $ASTRON_IP --eventlogger-ip $EVENTLOGGER_IP \
                     --district-name $DISTRICT_NAME --district-difficulty $DISTRICT_DIFFICULTY
done

