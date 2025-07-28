import pandas as pd, numpy as np
from pathlib import Path
from sklearn.preprocessing import StandardScaler

class FeaturePrepFork:
    def execute(self, payload: dict) -> dict:
        scaler = StandardScaler()
        feature_files = []
        for file in payload.get("cleaned_files", []):
            df = pd.read_csv(file)
            nums = df.select_dtypes(include=[np.number])
            feats = scaler.fit_transform(nums)
            out = Path(file).with_suffix(".features.npy")
            np.save(out, feats)
            feature_files.append(str(out))
        return {"feature_files": feature_files}
