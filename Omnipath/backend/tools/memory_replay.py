import json
import os
from datetime import datetime

MEMORY_FILE = os.path.expanduser("~/Omnipath/backend/memory/agent_alpha.json")

def replay_memory():
    if not os.path.exists(MEMORY_FILE):
        print("No memory log found.")
        return

    with open(MEMORY_FILE, "r") as f:
        try:
            logs = json.load(f)
        except json.JSONDecodeError:
            print("Memory file is corrupted or empty.")
            return

    print("\n--- Agent Alpha Memory Replay ---\n")
    for entry in logs:
        timestamp = entry.get("timestamp", "No time")
        event = entry.get("type", "No type")
        details = {k: v for k, v in entry.items() if k not in ["timestamp", "type"]}
        print(f"[{timestamp}] - {event}")
        for k, v in details.items():
            print(f"  {k}: {v}")
        print("-" * 40)
