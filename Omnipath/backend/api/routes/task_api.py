from flask import Blueprint, request, jsonify
from pathlib import Path
import sqlite3
from datetime import datetime

task_bp = Blueprint("task_bp", __name__)
DB_PATH = Path(__file__).resolve().parents[2] / "backend" / "forks" / "task_manager" / "task_log.db"

def get_db():
    conn = sqlite3.connect(DB_PATH)
    return conn

@task_bp.route("/create", methods=["POST"])
def create_task():
    data = request.get_json()
    name = data.get("name")
    agent = data.get("agent")
    now = datetime.utcnow().isoformat()
    conn = get_db()
    conn.execute(
        "INSERT INTO tasks (name, status, agent, created_at, updated_at, log) VALUES (?, 'active', ?, ?, ?, '')",
        (name, agent, now, now)
    )
    conn.commit()
    cur = conn.execute("SELECT last_insert_rowid()").fetchone()
    conn.close()
    return jsonify({"id": cur[0], "name": name, "agent": agent, "status": "active", "updated_at": now})

@task_bp.route("/<int:task_id>/log", methods=["POST"])
def append_log(task_id):
    entry = request.get_json().get("entry")
    conn = get_db()
    current = conn.execute("SELECT log FROM tasks WHERE id=?", (task_id,)).fetchone()[0]
    updated = f"{current}\n{datetime.utcnow().isoformat()} - {entry}"
    conn.execute("UPDATE tasks SET log=?, updated_at=? WHERE id=?", (updated, datetime.utcnow().isoformat(), task_id))
    conn.commit()
    conn.close()
    return jsonify({"message": "Log updated"})

@task_bp.route("/<int:task_id>/status", methods=["POST"])
def update_status(task_id):
    status = request.get_json().get("status")
    conn = get_db()
    conn.execute("UPDATE tasks SET status=?, updated_at=? WHERE id=?", (status, datetime.utcnow().isoformat(), task_id))
    conn.commit()
    conn.close()
    return jsonify({"message": "Status updated"})

@task_bp.route("", methods=["GET"])
def list_tasks():
    conn = get_db()
    cur = conn.execute("SELECT id, name, status, agent, updated_at FROM tasks")
    rows = cur.fetchall()
    conn.close()
    return jsonify([dict(zip(["id", "name", "status", "agent", "updated_at"], r)) for r in rows])
