
from flask import Blueprint, request, jsonify
from CommandBridge import CommandBridge
from ForkMemory import ForkMemory
from CoreStatus import CoreStatus
from utils.helpers import now, log_event

memory_store = {}

def store_task(task_id, task_data):
    memory_store[task_id] = {
        "data": task_data,
        "created_at": now(),
        "logs": [log_event("stored", task_data)]
    }

def update_task_status(task_id, new_status):
    if task_id in memory_store:
        memory_store[task_id]["data"]["status"] = new_status
        memory_store[task_id]["logs"].append(log_event("status_update", {"status": new_status}))
        return True
    return False

def get_task(task_id):
    return memory_store.get(task_id, None)

def list_all_tasks():
    return memory_store

command_api = Blueprint("command_api", __name__)

# Init modules
bridge = CommandBridge()
memory = ForkMemory()
status = CoreStatus()

# Register command example
def save_note(note):
    memory.remember("note", note)
    status.ping("ForkMemory", "WROTE")
    return f"Note saved: {note}"

bridge.register("save_note", save_note)

@command_api.route("/api/command", methods=["POST"])
def handle_command():
    data = request.json
    command = data.get("command")
    args = data.get("args", [])

    try:
        result = bridge.execute(command, *args)
        status.ping("CommandBridge", "EXECUTED")
        return jsonify({"success": True, "result": result}), 200
    except Exception as e:
        status.ping("CommandBridge", "ERROR")
        return jsonify({"success": False, "error": str(e)}), 400
