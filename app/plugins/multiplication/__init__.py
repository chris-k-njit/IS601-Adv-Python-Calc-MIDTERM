from app.commands import Command

class MultiplyCommand(Command):
    def __init__(self):
        super().__init__()
        self.name="multiply"

    def execute(self, *args):
        try:
            # Convert args to floats and perform multiplication
            result = 1
            for arg in args:
                result *= float(arg)  # Ensure arg is converted to float
            print(f"Result: {result}")
        except ValueError:
            print("Error: All arguments must be numbers.")