import sqlite3
from pathlib import Path
from datetime import datetime

class TaskManagerFork:
    DB_PATH = Path(__file__).resolve().parents[1] / "task_log.db"

    def __init__(self):
        self.conn = sqlite3.connect(self.DB_PATH)
        self.conn.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            status TEXT,
            agent TEXT,
            created_at TEXT,
            updated_at TEXT,
            log TEXT
        )
        """)
        self.conn.commit()

    def create_task(self, name, agent):
        now = datetime.utcnow().isoformat()
        self.conn.execute("""
            INSERT INTO tasks (name, status, agent, created_at, updated_at, log)
            VALUES (?, 'active', ?, ?, ?, '')
        """, (name, agent, now, now))
        self.conn.commit()

    def update_status(self, task_id, status):
        now = datetime.utcnow().isoformat()
        self.conn.execute("""
            UPDATE tasks SET status=?, updated_at=? WHERE id=?
        """, (status, now, task_id))
        self.conn.commit()

    def append_log(self, task_id, entry):
        cur = self.conn.cursor()
        cur.execute("SELECT log FROM tasks WHERE id=?", (task_id,))
        current = cur.fetchone()[0]
        updated = f"{current}\n{datetime.utcnow().isoformat()} - {entry}"
        self.conn.execute("UPDATE tasks SET log=? WHERE id=?", (updated, task_id))
        self.conn.commit()

    def list_tasks(self):
        cur = self.conn.cursor()
        rows = cur.execute("SELECT id, name, status, agent, updated_at FROM tasks").fetchall()
        return [dict(zip(['id', 'name', 'status', 'agent', 'updated_at'], row)) for row in rows]
