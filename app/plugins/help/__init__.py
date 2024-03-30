''' Test help command here. '''
from app.commands import Command

class HelpCommand(Command):
    def __init__(self):
        super().__init__()
        self.name="help"

    def execute(self):
        print("Available commands here are: addition, subtraction, multiplication, division, squareroot, greet, goodbye, caffeine, help\nUse 'exit' to quit the application.")