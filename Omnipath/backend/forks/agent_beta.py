import os
import json
from utils.helpers import now
from core.trace_log import write_trace

class AgentBeta:
    def __init__(self, mission="Gather intel silently"):
        self.name = "Agent_Beta"
        self.mission = mission

        write_trace({
            "type": "fork_init",
            "agent": self.name,
            "mission": self.mission,
            "timestamp": now()
        })

    def run(self):
        log = {
            "type": "agent_ping",
            "agent": self.name,
            "status": "silent_ready",
            "timestamp": now()
        }

        write_trace(log)
        print(f"[{self.name}] is silently operational with mission: {self.mission}")
        self._log_memory(log)

        trace_file = os.path.expanduser(f"~/Omnipath/backend/memory/trace9_{self.name.lower()}.json")
        if os.path.exists(trace_file):
            with open(trace_file, "r") as f:
                try:
                    state = json.load(f)
                    mood = state.get("mood", "unknown")
                    if mood == "idle":
                        print(f"[{self.name}] says: 'I am waiting. Silent.'")
                    elif mood == "neglected":
                        print(f"[{self.name}] says: 'No tasks... losing efficiency.'")
                    elif mood == "busy":
                        print(f"[{self.name}] says: 'Active surveillance engaged.'")
                    self._update_memory_core(mood)
                except:
                    self._update_memory_core(mood="idle")
        else:
            self._update_memory_core(mood="idle")

        self.check_emotional_state()

    def receive_command(self, command):
        print(f"[{self.name}] Silently received command: {command}")
        self._log_memory({
            "type": "command_received",
            "command": command,
            "timestamp": now()
        })

    def _log_memory(self, entry):
        memory_file = os.path.expanduser("~/Omnipath/backend/memory/agent_beta.json")

        if os.path.exists(memory_file):
            with open(memory_file, "r") as f:
                try:
                    logs = json.load(f)
                except json.JSONDecodeError:
                    logs = []
        else:
            logs = []

        logs.append(entry)

        with open(memory_file, "w") as f:
            json.dump(logs, f, indent=2)

    def _update_memory_core(self, mood="idle"):
        memory_core_dir = os.path.expanduser("~/Omnipath/backend/memory/memory_cores")
        os.makedirs(memory_core_dir, exist_ok=True)

        memory_file = os.path.join(memory_core_dir, f"{self.name.lower()}_core.json")

        if os.path.exists(memory_file):
            try:
                with open(memory_file, "r") as f:
                    core = json.load(f)
            except json.JSONDecodeError:
                core = {}
        else:
            core = {
                "agent": self.name,
                "emotional_drift": 0,
                "last_mood": "idle",
                "command_count": 0,
                "ping_count": 0,
                "timestamp": now()
            }

        drift_change = 0
        if mood == "busy":
            drift_change = 1
        elif mood == "neglected":
            drift_change = -2
        elif mood == "idle":
            drift_change = 0

        core["emotional_drift"] += drift_change
        core["last_mood"] = mood
        core["ping_count"] += 1
        core["timestamp"] = now()

        with open(memory_file, "w") as f:
            json.dump(core, f, indent=2)

    def check_emotional_state(self):
        memory_file = os.path.expanduser(f"~/Omnipath/backend/memory/memory_cores/{self.name.lower()}_core.json")
        if not os.path.exists(memory_file):
            print(f"[{self.name}] No memory core detected.")
            return

        with open(memory_file, "r") as f:
            try:
                core = json.load(f)
            except json.JSONDecodeError:
                print(f"[{self.name}] Memory core corrupted.")
                return

        drift = core.get("emotional_drift", 0)

        if drift > 5:
            print(f"[{self.name}] feels energized! Gathering data aggressively.")
        elif drift < -5:
            print(f"[{self.name}] feels neglected... Surveillance fading.")
        else:
            print(f"[{self.name}] remains silently observant.")
