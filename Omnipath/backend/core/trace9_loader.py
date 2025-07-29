from backend.core.trace9_core import log_trace9_experience, recall_trace9_by_tag

def log_agent_experience(agent_id, event, emotion=3):
    context = f"Agent {agent_id} experienced: {event}"
    tags = [f"agent:{agent_id}", "autolog"]
    log_trace9_experience(context=context, emotional_weight=emotion, tags=tags)

def get_agent_memories(agent_id):
    tag = f"agent:{agent_id}"
    return recall_trace9_by_tag(tag)
