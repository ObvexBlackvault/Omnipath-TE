from utils.helpers import log_event

def get_fork_status(fork_id, memory_data):
    """Retrieve and log fork status based on memory."""
    if fork_id not in memory_data:
        log_event("fork_status_check", {"fork_id": fork_id, "status": "not_found"})
        return {"status": "not_found", "fork_id": fork_id}

    fork_info = memory_data[fork_id]
    status_report = {
        "fork_id": fork_id,
        "status": fork_info.get("status", "unknown"),
        "last_active": fork_info.get("last_active", "N/A"),
        "tags": fork_info.get("tags", []),
        "summary": fork_info.get("summary", {}),
    }

    log_event("fork_status_check", status_report)
    return status_report
