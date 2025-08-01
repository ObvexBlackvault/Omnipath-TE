import os
import json
from backend.core.trace_log import write_trace
from backend.core.helpers import now

class AgentGamma:
    def __init__(self, mission="Monitor emotional trace drift"):
        self.name = "Agent_Gamma"
        self.mission = mission

        write_trace({
            "type": "fork_init",
            "agent": self.name,
            "mission": self.mission,
            "timestamp": now()
        })

    def run(self):
        self.heartbeat()

    def heartbeat(self):
        log = {
            "type": "agent_ping",
            "agent": self.name,
            "status": "reflective",
            "timestamp": now()
        }
        write_trace(log)
        print(f"[{self.name}] Heartbeat: {self.mission}")
