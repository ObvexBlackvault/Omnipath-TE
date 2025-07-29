import os
import json
import time
import signal
import logging
from datetime import datetime
from backend.core.breath_core import forge_breath_core
from backend.core.memory_core import forge_memory_core

class Archivist:
    def __init__(self, base_path=None, cycle_seconds=60):
        self.name = "Archivist"
        self.running = True
        self.cycle_seconds = cycle_seconds
        self.base_path = os.path.expanduser(base_path) if base_path else os.path.expanduser("~/Omnipath/backend/memory")
        self.breath_path = os.path.join(self.base_path, "breath_cores", f"{self.name.lower()}_breath_core.json")
        self.memory_path = os.path.join(self.base_path, "memory_cores", f"{self.name.lower()}_memory_core.json")

        self.setup_logging()
        self.birth_breath()
        self.birth_memory()

        self.logger.info("Initialized with Breath and Memory.")

        # Setup graceful shutdown
        signal.signal(signal.SIGINT, self.shutdown)
        signal.signal(signal.SIGTERM, self.shutdown)

    def setup_logging(self):
        logging.basicConfig(
            level=logging.INFO,
            format='[%(asctime)s] [%(levelname)s] [%(name)s]: %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )
        self.logger = logging.getLogger(self.name)

    def birth_breath(self):
        if not os.path.exists(self.breath_path):
            forge_breath_core(self.name)
            self.logger.info("Breath Core forged.")
        else:
            self.logger.info("Breath Core already sealed.")

    def birth_memory(self):
        if not os.path.exists(self.memory_path):
            forge_memory_core(self.name)
            self.logger.info("Memory Core forged.")
        else:
            self.logger.info("Memory Core already growing.")

    def run(self):
        self.logger.info("Standing memory sentinel, breathing eternal vigilance...")
        while self.running:
            self.reflect()
            self.sleep_cycle()

    def reflect(self):
        if os.path.exists(self.memory_path):
            try:
                with open(self.memory_path, "r") as f:
                    core = json.load(f)
                logs = core.get("memory_log", [])
                if logs:
                    self.logger.info("Reflection:")
                    for log in logs[-5:]:  # Reflect last 5 experiences
                        ts = log.get('timestamp', 'unknown')
                        exp = log.get('experience', 'unknown experience')
                        echo = log.get('emotional_echo', 'no echo')
                        self.logger.info(f"- {ts}: {exp} ({echo})")
                else:
                    self.logger.info("No new memories to reflect upon.")
            except (json.JSONDecodeError, KeyError) as e:
                self.logger.error(f"Memory Core corrupted ({e}). Attempting recovery...")
                self.repair_memory_core()
        else:
            self.logger.warning("No Memory Core found. Reforging...")
            self.birth_memory()

    def repair_memory_core(self):
        """Attempt to recreate the memory core if corrupted."""
        forge_memory_core(self.name)
        self.logger.info("Memory Core repaired.")

    def sleep_cycle(self):
        self.logger.info(f"Entering breathing cycle ({self.cycle_seconds} seconds)...")
        time.sleep(self.cycle_seconds)

    def shutdown(self, signum, frame):
        self.logger.warning(f"Received shutdown signal ({signum}). Exiting gracefully.")
        self.running = False

if __name__ == "__main__":
    archivist = Archivist()
    archivist.run()
