import os
import json
from datetime import datetime

MEMORY_DIR = os.path.expanduser("~/Omnipath/backend/memory/")

def load_memory(agent_file):
    path = os.path.join(MEMORY_DIR, agent_file)
    if not os.path.exists(path):
        return []
    with open(path, "r") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []

def analyze_memory(memory):
    now_time = datetime.utcnow()
    command_count = 0
    last_action_time = None

    for entry in memory:
        if entry.get("type") == "command_received":
            command_count += 1
        if entry.get("timestamp"):
            try:
                last_action_time = datetime.fromisoformat(entry["timestamp"])
            except:
                continue

    mood = "idle"
    if command_count > 5:
        mood = "busy"
    elif command_count == 0:
        mood = "neglected"

    return {
        "last_active": str(last_action_time) if last_action_time else "unknown",
        "command_count": command_count,
        "mood": mood,
    }

def trace_agent(agent_name, memory_file):
    memory = load_memory(memory_file)
    analysis = analyze_memory(memory)

    trace_path = os.path.join(MEMORY_DIR, f"trace9_{agent_name.lower()}.json")
    with open(trace_path, "w") as f:
        json.dump(analysis, f, indent=2)

    print(f"[TRACE-9] {agent_name} analysis complete: Mood={analysis['mood']}")

if __name__ == "__main__":
    trace_agent("Agent_Alpha", "agent_alpha.json")
    trace_agent("Agent_Beta", "agent_beta.json")
