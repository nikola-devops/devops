#!/usr/bin/env bash

TARGET_HOST="atlassian.com"

echo "Checking connectivity to $TARGET_HOST..."

# Ping 1 packet, suppress output
ping -c 1 "$TARGET_HOST" > /dev/null 2>&1

# Check the exit code of the ping command
if [ $? -eq 0 ]; then
  echo "SUCCESS: Network is online."
else
  echo "ERROR: Cannot reach $TARGET_HOST."
  exit 1
fi
