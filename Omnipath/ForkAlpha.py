
import time
from ForkMemory import ForkMemory
from CoreStatus import CoreStatus
from CommandBridge import CommandBridge
from ForkLink import ForkLink

class ForkAgent:
    def __init__(self, name="ForkAlpha"):
        self.name = name
        self.memory = ForkMemory(f"{name.lower()}_memory.json")
        self.status = CoreStatus()
        self.bridge = CommandBridge()
        self.link = ForkLink()
        self._setup()

    def _setup(self):
        self.status.ping(self.name, "INIT")
        self.memory.remember("startup_time", time.ctime())
        self.bridge.register("log_note", self.log_note)
        self.bridge.register("set_mode", self.set_mode)
        self.bridge.register("set_mission", self.set_mission)

    def log_note(self, note):
        key = f"note_{int(time.time())}"
        self.memory.remember(key, note)
        self.status.ping(self.name, "NOTE_LOGGED")
        return f"Note stored under {key}"

    def set_mode(self, mode):
        self.memory.remember("mode", mode)
        self.status.ping(self.name, f"MODE SET: {mode}")
        return f"Mode set to {mode}"

    def set_mission(self, mission):
        self.link.share("shared", "mission", mission)
        self.status.ping(self.name, f"MISSION SET: {mission}")
        return f"Mission set to '{mission}'"

    def decide(self):
        mode = self.memory.recall("mode")
        if mode == "stealth":
            self.status.ping(self.name, "STEALTH MODE")
            return 4
        elif mode == "aggressive":
            self.status.ping(self.name, "AGGRESSIVE MODE")
            return 1
        return 2

    def loop(self):
        self.status.ping(self.name, "RUNNING")
        delay = self.decide()

        mission = self.link.fetch("shared", "mission")
        if mission:
            self.status.ping(self.name, f"MISSION DETECTED: {mission}")
            self.memory.remember("executing", mission)
            for i in range(3):
                msg = f"{self.name} executes '{mission}' [step {i+1}]"
                self.memory.remember(f"mission_step_{i+1}", msg)
                self.status.ping(self.name, msg)
                time.sleep(delay)
            self.status.ping(self.name, f"MISSION COMPLETE: {mission}")
        else:
            for i in range(3):
                msg = f"Cycle {i+1} [no mission]"
                self.memory.remember(f"cycle_{i+1}", msg)
                self.status.ping(self.name, msg)
                time.sleep(delay)

        self.status.ping(self.name, "COMPLETE")

if __name__ == "__main__":
    agent = ForkAgent("ForkAlpha")  # or ForkBeta
    agent.loop()
