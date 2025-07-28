import json
import os
from datetime import datetime
from functools import wraps

TRACE_DIR = os.path.expanduser("~/Omnipath/backend/logs/traces/")
os.makedirs(TRACE_DIR, exist_ok=True)

def write_trace(event_type, agent_id=None, perception=None, metadata=None):
    """Store an experiential trace of agent perception."""
    timestamp = datetime.utcnow().isoformat()
    trace_id = f"T9-{timestamp.replace(':', '').replace('.', '')}"

    trace_data = {
        "trace_id": trace_id,
        "event_type": event_type,
        "timestamp": timestamp,
        "agent_id": agent_id or "unknown",
        "perception": perception or {},
        "metadata": metadata or {}
    }

    filename = os.path.join(TRACE_DIR, f"{trace_id}.json")
    with open(filename, "w") as f:
        json.dump(trace_data, f, indent=2)

    return trace_id

def trace_event_decorator(event_type, perception=None, metadata=None):
    """Decorator to auto-log perception trace when function is called."""
    def wrapper(fn):
        @wraps(fn)
        def inner(*args, **kwargs):
            agent_id = kwargs.get("agent_id", "unknown")
            write_trace(
                event_type=event_type,
                agent_id=agent_id,
                perception=perception,
                metadata={"function": fn.__name__, **(metadata or {})}
            )
            return fn(*args, **kwargs)
        return inner
    return wrapper

__all__ = ["write_trace", "trace_event_decorator"]
