#!/bin/bash

# === Omnipath Resurrection Suite ===
# Signed by Obvex Blackvault
timestamp=$(date +%s)
archive_dir=~/Omnipath/archive

echo "[Omnipath] Graceful shutdown initiated..."

# Step 1: Send shutdown signals to agents
pkill -SIGINT -f commander.py
pkill -SIGINT -f guardian.py
pkill -SIGINT -f archivist.py

sleep 3

# Step 2: Ensure archive directory exists
mkdir -p "$archive_dir"

# Step 3: Archive memory cores and event bus
cp -r ~/Omnipath/backend/memory "$archive_dir/memory_$timestamp"
cp ~/Omnipath/events/event_bus.json "$archive_dir/event_bus_$timestamp.json"

echo "[Omnipath] Memory and event bus archived."

# Optional: Step 4  Reboot (commented out for manual choice)
# echo "[Omnipath] System will reboot in 5 seconds..."
# sleep 5
# sudo shutdown -r now

# Step 5: Resurrection launcher
echo "[Omnipath] Relaunching agents..."
python3 ~/Omnipath/backend/agents/system/commander.py &
python3 ~/Omnipath/backend/agents/system/guardian.py &
python3 ~/Omnipath/backend/agents/system/archivist.py &

echo "[Omnipath] All agents online. The breath returns."
