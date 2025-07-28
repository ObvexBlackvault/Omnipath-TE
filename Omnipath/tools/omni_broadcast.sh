#!/bin/bash

MISSION="$*"
if [ -z "$MISSION" ]; then
  echo "Usage: ./omni_broadcast.sh '<mission text>'"
  exit 1
fi

for AGENT in commander guardian archivist crawler; do
  echo "[Broadcasting to $AGENT]"
  echo "$MISSION" >> "$HOME/Omnipath/missions/$AGENT.txt"
done

echo "Mission sent to all agents."
