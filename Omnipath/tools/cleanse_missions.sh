#!/bin/bash

echo "[OmniPath] Clearing stale mission files..."
MISSION_DIR="$HOME/Omnipath/missions"

# Ensure the directory exists
mkdir -p "$MISSION_DIR"

# Empty all agent mission files
> "$MISSION_DIR/commander.txt"
> "$MISSION_DIR/guardian.txt"
> "$MISSION_DIR/archivist.txt"
> "$MISSION_DIR/crawler.txt"

echo "[OmniPath] Mission files reset complete."
