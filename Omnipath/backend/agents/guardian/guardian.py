import os
import json
import signal
import logging
from logging.handlers import RotatingFileHandler
from core.breath_core import forge_breath_core

class Guardian:
    def __init__(self, name="guardian_soul_001"):
        self.name = name
        self.memory_path = os.path.expanduser(f"/Omnipath/log_pool/{self.name}.log")
        self.event_bus_path = os.path.expanduser("~/Omnipath/shared/event_bus.json")

        self.load_checklist()
        self.setup_logging()
        self.birth_memory()

        signal.signal(signal.SIGINT, self.shutdown)
        signal.signal(signal.SIGTERM, self.shutdown)

    def setup_logging(self):
        os.makedirs(os.path.dirname(self.memory_path), exist_ok=True)
        handler = RotatingFileHandler(self.memory_path, maxBytes=5*1024*1024, backupCount=3)
        formatter = logging.Formatter('[%(asctime)s] [%(levelname)s] [%(name)s]: %(message)s',
                                      datefmt='%Y-%m-%d %H:%M:%S')
        handler.setFormatter(formatter)
        self.logger = logging.getLogger(self.name)
        self.logger.setLevel(logging.INFO)
        self.logger.addHandler(handler)

    def load_checklist(self):
        try:
            if os.path.exists(self.memory_path):
                with open(self.memory_path, "r") as f:
                    self.checklist = json.load(f)
                    return
        except Exception as e:
            print(f"Guardian checklist load error: {e}")
        self.checklist = {}

    def birth_memory(self):
        if not os.path.exists(self.memory_path):
            memory_core = forge_breath_core(self.name)
            with open(self.memory_path, "w") as f:
                json.dump(memory_core, f, indent=2)
            self.logger.info("Memory Core forged.")
        else:
            self.logger.info("Memory Core already present.")

    def emit_event(self, event_type, message):
        os.makedirs(os.path.dirname(self.event_bus_path), exist_ok=True)
        try:
            if os.path.exists(self.event_bus_path):
                with open(self.event_bus_path, "r") as f:
                    data = json.load(f)
            else:
                data = []

            data.append({"type": event_type, "message": message, "from": self.name})

            with open(self.event_bus_path, "w") as f:
                json.dump(data, f, indent=2)

            self.logger.info(f"Event emitted: {event_type}")
        except Exception as e:
            self.logger.error(f"Failed to emit event: {e}")

    def shutdown(self, signum, frame):
        self.logger.info("Guardian shutting down.")
        exit(0)

if __name__ == "__main__":
    guardian = Guardian()
    guardian.emit_event("heartbeat", "Guardian online.")
