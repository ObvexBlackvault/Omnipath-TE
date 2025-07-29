from utils.helpers import now, generate_id, log_event, safe_json
from backend.core.trace_log import write_trace

class AgentTask:
    def __init__(self, title, agent_id, data=None, priority=5):
        self.id = generate_id()
        self.title = title
        self.agent_id = agent_id
        self.data = data or {}
        self.priority = priority
        self.timestamp = now()
        self.status = "queued"

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "agent_id": self.agent_id,
            "data": self.data,
            "priority": self.priority,
            "timestamp": self.timestamp,
            "status": self.status
        }

    def execute(self):
        log_event(f"Executing task: {self.title} for Agent {self.agent_id}")
        write_trace(self.to_dict())
        self.status = "completed"
