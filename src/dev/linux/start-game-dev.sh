#!/bin/sh
cd ../..

# Get the user input:
read -p "Username: " ttUsername
read -p "Password: " ttPassword

# Export the environment variables:
export ttUsername=$ttUsername
export ttPassword=$ttPassword
export TT_PLAYCOOKIE=$ttUsername:$ttPassword
export TT_GAMESERVER="game.toontowngeargrind.com:7199"

echo "==============================="
echo "Starting Toontown Gear Grind..."
echo "Username: $TT_PLAYCOOKIE"
echo "Gameserver: $TT_GAMESERVER"
echo "==============================="

/usr/bin/python2 -m toontown.base.ClientStart

