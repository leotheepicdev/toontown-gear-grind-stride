#!/bin/sh
cd ../..

# Get the user input:
read -p "Username: " ttUsername

# Export the environment variables:
export ttUsername=$ttUsername
export TT_PLAYCOOKIE=$ttUsername
export TT_GAMESERVER="127.0.0.1"

echo "==============================="
echo "Starting Toontown Gear Grind..."
echo "Username: $ttUsername"
echo "Gameserver: $TT_GAMESERVER"
echo "==============================="

/usr/bin/python2 -m toontown.base.ClientStart
