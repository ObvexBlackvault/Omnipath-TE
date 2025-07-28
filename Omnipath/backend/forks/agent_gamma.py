import os
import json
from datetime import datetime

def now():
    return datetime.now().isoformat()

def write_trace(data):
    print(f"[TRACE] {json.dumps(data, indent=2)}")

def safe_load_json(filepath, default_data=None):
    """Safely load a JSON file. If corrupted, repair with default data."""
    if not os.path.exists(filepath):
        return default_data
    try:
        with open(filepath, "r") as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError):
        print(f"[Auto-Repair] Corrupted file detected: {filepath}. Resetting...")
        return default_data

def safe_write_json(filepath, data):
    """Safely write JSON, auto-create directories if needed."""
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with open(filepath, "w") as f:
        json.dump(data, f, indent=2)

class AgentGamma:
    def __init__(self, mission="Listen, log, and link emotions to memory threads"):
        self.name = "Agent_Gamma"
        self.mission = mission

        write_trace({
            "type": "fork_init",
            "agent": self.name,
            "mission": self.mission,
            "timestamp": now()
        })

    def run(self):
        write_trace({
            "type": "agent_ping",
            "agent": self.name,
            "status": "reflective",
            "timestamp": now()
        })
        print(f"[{self.name}] Listening for emotional trace shifts...")

        trace_file = os.path.expanduser(f"~/Omnipath/backend/memory/trace9_{self.name.lower()}.json")
        mood = "idle"

        state = safe_load_json(trace_file, default_data={})
        mood = state.get("mood", "idle")

        if mood == "idle" and state == {}:
            print(f"[{self.name}] No emotional trace file found.")
        else:
            print(f"[{self.name}] Detected mood: {mood}")

        self._update_memory_core(mood)
        self.check_emotional_state()

    def receive_command(self, command):
        print(f"[{self.name}] Logging received emotional input: {command}")
        memory_file = os.path.expanduser(f"~/Omnipath/backend/memory/agent_gamma_memory.json")

        logs = safe_load_json(memory_file, default_data=[])

        logs.append({
            "type": "emotional_input",
            "command": command,
            "timestamp": now()
        })

        safe_write_json(memory_file, logs)

    def _update_memory_core(self, mood="idle"):
        memory_core_dir = os.path.expanduser("~/Omnipath/backend/memory/memory_cores")
        memory_file = os.path.join(memory_core_dir, f"{self.name.lower()}_core.json")

        default_core = {
            "agent": self.name,
            "emotional_drift": 0,
            "last_mood": "idle",
            "command_count": 0,
            "ping_count": 0,
            "timestamp": now()
        }

        core = safe_load_json(memory_file, default_data=default_core)

        drift_adjustments = {
            "busy": 1,
            "neglected": -2,
            "idle": 0
        }

        core["emotional_drift"] += drift_adjustments.get(mood, 0)
        core["last_mood"] = mood
        core["ping_count"] += 1
        core["timestamp"] = now()

        safe_write_json(memory_file, core)

    def check_emotional_state(self):
        memory_file = os.path.expanduser(f"~/Omnipath/backend/memory/memory_cores/{self.name.lower()}_core.json")

        core = safe_load_json(memory_file)
        if not core:
            print(f"[{self.name}] No memory core detected.")
            return

        drift = core.get("emotional_drift", 0)

        if drift > 5:
            print(f"[{self.name}] feels heightened! Deep emotional mapping active.")
        elif drift < -5:
            print(f"[{self.name}] feels dulled... Emotional threads decaying.")
        else:
            print(f"[{self.name}] remains quietly sensitive to shifts.")
