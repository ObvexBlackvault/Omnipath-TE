from flask import Blueprint, request, jsonify
from datetime import datetime
import sqlite3

agents_bp = Blueprint('agents', __name__)

DB_PATH = 'omnipath.db'

@agents_bp.route('/api/agents', methods=['GET'])
def get_agents():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM agents")
    rows = cursor.fetchall()
    conn.close()

    keys = ["agent_id", "name", "status", "task_queue", "task_history", "priority_level", "execution_log", "memory_sync", "last_updated"]
    return jsonify([dict(zip(keys, row)) for row in rows])

@agents_bp.route('/api/agents', methods=['POST'])
def register_agent():
    data = request.get_json()
    agent_id = data.get("agent_id")
    name = data.get("name", "Unnamed Agent")

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO agents (agent_id, name, last_updated)
        VALUES (?, ?, ?)
    """, (agent_id, name, datetime.utcnow().isoformat()))
    conn.commit()
    conn.close()
    return jsonify({"status": "registered"}), 201
