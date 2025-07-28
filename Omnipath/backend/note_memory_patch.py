
from flask import Blueprint, request, jsonify
from ForkMemory import ForkMemory
from datetime import datetime

note_memory = Blueprint("note_memory", __name__)
memory = ForkMemory("note_history.json")

@note_memory.route("/api/notes", methods=["POST"])
def log_note():
    data = request.get_json()
    note = {
        "content": data.get("content", ""),
        "timestamp": datetime.now().isoformat()
    }
    memory.remember(str(datetime.now().timestamp()), note)
    return jsonify({"success": True, "note": note}), 201
