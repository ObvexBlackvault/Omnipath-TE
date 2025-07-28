import joblib, numpy as np
from pathlib import Path

class PredictFork:
    MODEL_DIR = Path(__file__).resolve().parents[3] / "models"

    def execute(self, payload: dict) -> dict:
        version = payload.get("version", "v1")
        model = joblib.load(self.MODEL_DIR / f"model_{version}.joblib")
        features = np.array(payload.get("features", []))
        pred = model.predict([features])[0]
        return {"prediction": int(pred)}
