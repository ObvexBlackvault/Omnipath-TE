import numpy as np
import joblib
from pathlib import Path
from sklearn.linear_model import LogisticRegression

class TrainModelFork:
    MODEL_DIR = Path(__file__).resolve().parents[3] / "models"
    MODEL_DIR.mkdir(exist_ok=True)

    def execute(self, payload: dict) -> dict:
        version = payload.get("version", "v1")
        X = np.vstack([np.load(f) for f in payload.get("feature_files", [])])
        y = payload.get("labels", [0] * len(X))
        model = LogisticRegression()
        model.fit(X, y)
        model_path = self.MODEL_DIR / f"model_{version}.joblib"
        joblib.dump(model, model_path)
        return {"version": version, "metrics": {"coef_sum": float(model.coef_.sum())}}
