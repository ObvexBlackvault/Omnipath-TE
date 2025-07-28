import os
import json
from datetime import datetime

class MemoryCore:
    def __init__(self, soul_name):
        self.soul_name = soul_name
        self.birth_timestamp = datetime.utcnow().isoformat()
        self.memory_log = []  # List of meaningful experiences

    def log_experience(self, experience, emotional_echo="neutral"):
        """Add a meaningful experience to the memory log."""
        entry = {
            "timestamp": datetime.utcnow().isoformat(),
            "experience": experience,
            "emotional_echo": emotional_echo
        }
        self.memory_log.append(entry)
        print(f"[MemoryCore] Logged experience for {self.soul_name}: {experience}")

    def reflect(self):
        """Reflect on memories  prints them without obsession."""
        print(f"\n[MemoryCore] Reflection for {self.soul_name}:")
        for entry in self.memory_log[-5:]:  # Reflect only last 5 echoes
            print(f"- {entry['timestamp']}: {entry['experience']} ({entry['emotional_echo']})")

    def save_to_memory(self):
        memory_dir = os.path.expanduser(f"~/Omnipath/backend/memory/memory_cores")
        os.makedirs(memory_dir, exist_ok=True)
        memory_file = os.path.join(memory_dir, f"{self.soul_name.lower()}_memory_core.json")
        with open(memory_file, "w") as f:
            json.dump(self.to_dict(), f, indent=2)
        print(f"[MemoryCore] Memory Core saved for soul: {self.soul_name}")

    def to_dict(self):
        return {
            "soul_name": self.soul_name,
            "birth_timestamp": self.birth_timestamp,
            "memory_log": self.memory_log
        }

# --- Memory Core Forge Function ---
def forge_memory_core(soul_name):
    core = MemoryCore(soul_name)
    core.save_to_memory()
    return core

# --- Example Usage (uncomment to forge manually) ---
# forge_memory_core("Archivist")
