from app.commands import Command

class DivideCommand(Command):
    def execute(self, *args):
        try:
            if float(args[1]) == 0:
                print("Error: Division by zero is not allowed.")
                return
            result = float(args[0]) / float(args[1])
            print(f"Result: {result}")
        except ValueError:
            print("Error: All arguments must be numbers.")
        except IndexError:
            print("Error: Two arguments are required for division.")