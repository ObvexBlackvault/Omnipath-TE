from pathlib import Path

class DataIngestFork:
    def execute(self, payload: dict) -> dict:
        path = payload.get("path", "./data")
        p = Path(path)
        files = [str(f) for f in p.glob("*.csv")]
        return {"files": files}
