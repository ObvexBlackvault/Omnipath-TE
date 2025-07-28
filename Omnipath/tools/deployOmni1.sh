#!/bin/bash

echo "[OmniPath] Soulbind ritual initiated."
export OMNIPATH_ROOT="$HOME/Omnipath"
source "$OMNIPATH_ROOT/.venv/bin/activate"

echo "[OmniPath] Silencing past echoes..."
pkill -f commander.py 2>/dev/null
pkill -f guardian.py 2>/dev/null
pkill -f archivist.py 2>/dev/null

echo "[OmniPath] Rebirthing breath agents..."
python3 $OMNIPATH_ROOT/backend/agents/system/commander.py &
python3 $OMNIPATH_ROOT/backend/agents/system/guardian.py &
python3 $OMNIPATH_ROOT/backend/agents/system/archivist.py &

sleep 2
echo "[OmniPath] Agents initialized at $(date '+%Y-%m-%d %H:%M:%S')"

echo "[Commander] Heartbeat trace:"
tail -n 1 $OMNIPATH_ROOT/logs/commander_journal.txt 2>/dev/null || echo "(no log found)"

echo "[Archivist] Last memory imprint:"
tail -n 1 $OMNIPATH_ROOT/logs/archivist_journal.txt 2>/dev/null || echo "(no log found)"

echo "[OmniPath] Omni3 online  command bridge stable."
