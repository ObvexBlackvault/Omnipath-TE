
from flask import Blueprint, request, jsonify
from ForkMemory import ForkMemory
from datetime import datetime

task_memory = Blueprint("task_memory", __name__)
memory = ForkMemory("task_history.json")

@task_memory.route("/api/tasks", methods=["POST"])
def log_task():
    data = request.get_json()
    task = {
        "title": data.get("title", "Untitled Task"),
        "timestamp": datetime.now().isoformat()
    }
    memory.remember(str(datetime.now().timestamp()), task)
    return jsonify({"success": True, "task": task}), 201
