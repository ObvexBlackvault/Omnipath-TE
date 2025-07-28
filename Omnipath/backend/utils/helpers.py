import json
import datetime

def now():
    return datetime.datetime.utcnow().isoformat()

def timestamped_log(message):
    return f"[{now()}] {message}"

def log_event(event, log_file):
    entry = {
        "timestamp": now(),
        "event": event
    }
    try:
        with open(log_file, 'r') as f:
            logs = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        logs = []

    logs.append(entry)

    with open(log_file, 'w') as f:
        json.dump(logs, f, indent=2)
