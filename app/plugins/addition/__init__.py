from app.commands import Command

class AddCommand(Command):
    def __init__(self):
        super().__init__()
        self.name="add"

    def execute(self, *args):
        try:
            result = sum(float(arg) for arg in args)
            print(f"Result: {result}")
        except ValueError:
            print("Error: All arguments must be numbers.")