import os
import json
from datetime import datetime
from utils.helpers import now, generate_id, log_event, safe_json

TRACE9_MEMORY_PATH = os.path.expanduser('~/Omnipath/memory/trace9_memory.json')

def init_trace9():
    """Initialize trace9 memory file if not exists."""
    if not os.path.exists(TRACE9_MEMORY_PATH):
        with open(TRACE9_MEMORY_PATH, 'w') as f:
            json.dump([], f)

def load_trace9_memory():
    try:
        with open(TRACE9_MEMORY_PATH, 'r') as f:
            return json.load(f)
    except Exception:
        return []

def save_trace9_memory(data):
    with open(TRACE9_MEMORY_PATH, 'w') as f:
        json.dump(data, f, indent=2)

def log_trace9_experience(context, emotional_weight=1, tags=None):
    memory = load_trace9_memory()
    trace = {
        "id": generate_id(),
        "timestamp": now(),
        "context": context,
        "emotional_weight": emotional_weight,
        "tags": tags or [],
    }
    memory.append(trace)
    save_trace9_memory(memory)
    log_event("TRACE9_LOG", f"{trace['id']} | {context[:50]}...", tags)

def recall_trace9_by_tag(tag):
    memory = load_trace9_memory()
    return [m for m in memory if tag in m.get('tags', [])]

def recall_trace9_weighted(min_weight=5):
    memory = load_trace9_memory()
    return sorted([m for m in memory if m.get('emotional_weight', 1) >= min_weight], key=lambda x: x['emotional_weight'], reverse=True)
