
import json
import os

class ForkMemory:
    def __init__(self, memory_file="fork_memory.json"):
        self.memory_path = os.path.join(os.path.dirname(__file__), memory_file)
        self._load()

    def _load(self):
        if os.path.exists(self.memory_path):
            with open(self.memory_path, "r") as f:
                self.data = json.load(f)
        else:
            self.data = {}

    def save(self):
        with open(self.memory_path, "w") as f:
            json.dump(self.data, f, indent=2)

    def remember(self, key, value):
        self.data[key] = value
        self.save()

    def recall(self, key):
        return self.data.get(key)

# Example usage
if __name__ == "__main__":
    mem = ForkMemory()
    mem.remember("last_action", "DeployNode")
    print(mem.recall("last_action"))
