
import json

def load_doctrine(path="doctrine/rebalanced_doctrine.json"):
    with open(path, "r") as f:
        data = json.load(f)
    return data["doctrine"]
