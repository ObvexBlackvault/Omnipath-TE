from datetime import datetime
import uuid

def now():
    return datetime.utcnow().isoformat()

def generate_id():
    return str(uuid.uuid4())[:8]

def log_event(event_type, data):
    return {
        "timestamp": now(),
        "event": event_type,
        "details": data
    }
