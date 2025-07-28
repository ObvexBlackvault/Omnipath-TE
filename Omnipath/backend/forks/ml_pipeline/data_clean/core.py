import pandas as pd
from pathlib import Path

class DataCleanFork:
    def execute(self, payload: dict) -> dict:
        cleaned = []
        for file in payload.get("files", []):
            df = pd.read_csv(file).dropna()
            out = Path(file).with_suffix(".cleaned.csv")
            df.to_csv(out, index=False)
            cleaned.append(str(out))
        return {"cleaned_files": cleaned}
