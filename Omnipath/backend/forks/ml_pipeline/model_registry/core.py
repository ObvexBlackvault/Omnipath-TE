import sqlite3
from pathlib import Path

class ModelRegistryFork:
    DB = Path(__file__).resolve().parents[3] / "data" / "models.db"
    DB.parent.mkdir(exist_ok=True)

    def __init__(self):
        conn = sqlite3.connect(self.DB)
        conn.execute("CREATE TABLE IF NOT EXISTS registry (version TEXT PRIMARY KEY, metrics TEXT)")
        conn.commit()
        conn.close()

    def execute(self, payload: dict) -> dict:
        version = payload["version"]
        metrics = str(payload.get("metrics", {}))
        conn = sqlite3.connect(self.DB)
        conn.execute("REPLACE INTO registry (version, metrics) VALUES (?, ?)", (version, metrics))
        rows = conn.execute("SELECT version, metrics FROM registry").fetchall()
        conn.commit()
        conn.close()
        return {"registry": [{"version": v, "metrics": m} for v, m in rows]}
