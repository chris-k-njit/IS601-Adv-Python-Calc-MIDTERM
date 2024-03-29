from app.commands import Command

class ByeCommand(Command):
    def execute(self):
        print("Goodbye! Thank you for using the calculator.")