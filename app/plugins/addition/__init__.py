from app.commands import Command

class AddCommand(Command):
    def execute(self, *args):
        try:
            result = sum(float(arg) for arg in args)
            print(f"Result: {result}")
        except ValueError:
            print("Error: All arguments must be numbers.")