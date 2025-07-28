
import json
import os

class ForkLink:
    def __init__(self, shared_file="shared_forklink.json"):
        self.shared_path = os.path.join(os.path.dirname(__file__), shared_file)
        if not os.path.exists(self.shared_path):
            with open(self.shared_path, "w") as f:
                json.dump({}, f)

    def share(self, fork_name, key, value):
        with open(self.shared_path, "r") as f:
            data = json.load(f)
        if fork_name not in data:
            data[fork_name] = {}
        data[fork_name][key] = value
        with open(self.shared_path, "w") as f:
            json.dump(data, f, indent=2)

    def fetch(self, fork_name, key):
        with open(self.shared_path, "r") as f:
            data = json.load(f)
        return data.get(fork_name, {}).get(key)

    def all(self):
        with open(self.shared_path, "r") as f:
            return json.load(f)

# Example usage
if __name__ == "__main__":
    link = ForkLink()
    link.share("ForkAlpha", "task", "Scan perimeter")
    print(link.fetch("ForkAlpha", "task"))
    print(link.all())
