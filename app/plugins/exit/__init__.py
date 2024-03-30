import sys
from app.commands import Command

class ExitCommand(Command):
    def __init__(self):
        super().__init__()
        self.name="exit"

    def execute(self):
        sys.exit("Now exiting the calculator program.")