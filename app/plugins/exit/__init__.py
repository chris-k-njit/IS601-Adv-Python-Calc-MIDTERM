import sys
from app.commands import Command

class ExitCommand(Command):
    def execute(self):
        sys.exit("Now exiting the calculator program.")