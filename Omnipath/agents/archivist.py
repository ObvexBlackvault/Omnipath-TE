
import json
from datetime import datetime
from pathlib import Path

class Archivist:
    def log_pulse(self, data, path="memory/pulse_log.json"):
        Path("memory").mkdir(exist_ok=True)
        data["timestamp"] = datetime.utcnow().isoformat()
        with open(path, "w") as f:
            json.dump(data, f, indent=2)
