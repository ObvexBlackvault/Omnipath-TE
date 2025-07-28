
class CommandBridge:
    def __init__(self):
        self.commands = {}

    def register(self, command_name, function):
        self.commands[command_name] = function

    def execute(self, command_name, *args, **kwargs):
        if command_name in self.commands:
            return self.commands[command_name](*args, **kwargs)
        else:
            raise ValueError(f"Command '{command_name}' not recognized.")

# Example usage
if __name__ == "__main__":
    def test_func(x): return f"Echo: {x}"
    bridge = CommandBridge()
    bridge.register("echo", test_func)
    print(bridge.execute("echo", "Omnipath"))
