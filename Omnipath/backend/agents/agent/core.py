from utils.timeutils import now, generate_id, log_event
from backend.core.trace_log import write_trace

class AgentCore:
    def __init__(self, name, role="general", memory=None):
        self.id = generate_id()
        self.name = name
        self.role = role
        self.memory = memory or []
        self.status = "idle"
        self.created_at = now()

    def remember(self, memory_entry):
        log_event("memory_add", memory_entry)
        self.memory.append(memory_entry)

    def act(self, input_data):
        action = {
            "agent_id": self.id,
            "input": input_data,
            "response": f"Processed input: {input_data}",
            "timestamp": now()
        }
        self.remember(action)
        write_trace(action)
        return action

    def status_report(self):
        return {
            "id": self.id,
            "name": self.name,
            "role": self.role,
            "status": self.status,
            "memory_size": len(self.memory),
            "created_at": self.created_at
        }
