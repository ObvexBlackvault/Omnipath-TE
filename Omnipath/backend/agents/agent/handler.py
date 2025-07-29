from .task import AgentTask
from utils.helpers import now, log_event
from backend.core.trace_log import write_trace

class AgentHandler:
    def __init__(self, agent_id, name="Unnamed Agent"):
        self.agent_id = agent_id
        self.name = name
        self.tasks = []
        self.status = "idle"
        self.last_updated = now()

    def add_task(self, title, data=None, priority=5):
        task = AgentTask(title=title, agent_id=self.agent_id, data=data, priority=priority)
        self.tasks.append(task)
        self.last_updated = now()
        log_event(f"Task '{title}' added to Agent '{self.name}'")
        write_trace({
            "event": "task_added",
            "agent_id": self.agent_id,
            "task_id": task.id,
            "title": title,
            "timestamp": self.last_updated
        })

    def run_tasks(self):
        self.status = "working"
        for task in self.tasks:
            if task.status == "queued":
                task.execute()
        self.status = "idle"
        self.last_updated = now()
