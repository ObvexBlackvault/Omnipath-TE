
import sqlite3

conn = sqlite3.connect("omnipath.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS agents (
    agent_id TEXT PRIMARY KEY,
    name TEXT NOT NULL,
    status TEXT DEFAULT 'idle',
    task_queue TEXT,
    task_history TEXT,
    priority_level INTEGER DEFAULT 5,
    execution_log TEXT,
    memory_sync BOOLEAN DEFAULT 0,
    last_updated TEXT
)
""")

conn.commit()
conn.close()
