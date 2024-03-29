''' Test help command here. '''
from app.commands import Command

class HelpCommand(Command):
    def execute(self):
        print("Available commands here are: addition, subtraction, multiplication, division, squareroot, greet, bye, caffeine, help\nUse 'exit' to quit the application.")