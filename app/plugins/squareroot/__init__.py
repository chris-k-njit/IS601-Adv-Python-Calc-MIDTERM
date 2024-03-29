from app.commands import Command
import math

class SqrtCommand(Command):
    def execute(self, *args):
        try:
            number = float(args[0])
            if number < 0:
                print("Error: Cannot take the square root of a negative number.")
                return
            result = math.sqrt(number)
            print(f"Result: {result}")
        except ValueError:
            print("Error: The argument must be a number.")
        except IndexError:
            print("Error: One argument is required for square root.")