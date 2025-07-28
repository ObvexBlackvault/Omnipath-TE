
import datetime

class CoreStatus:
    def __init__(self):
        self.status_log = []

    def ping(self, module_name, status="OK"):
        timestamp = datetime.datetime.now().isoformat()
        self.status_log.append(f"[{timestamp}] {module_name} STATUS: {status}")
        print(self.status_log[-1])

    def get_log(self):
        return self.status_log

# Example usage
if __name__ == "__main__":
    cs = CoreStatus()
    cs.ping("VoiceSynth")
    cs.ping("AgentLogger", "WARNING")
