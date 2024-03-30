from app.commands import Command

class SubtractCommand(Command):
    def __init__(self):
        super().__init__()
        self.name="subtract"

    def execute(self, *args):
        try:
            result = float(args[0]) - sum(float(arg) for arg in args[1:])
            print(f"Result: {result}")
        except ValueError:
            print("Error: All arguments must be numbers.")