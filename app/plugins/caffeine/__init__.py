from app.commands import Command

class CaffeineCommand(Command):
    def __init__(self):
        super().__init__()
        self.name="coffee"

    def execute(self):
        print("Don't forget to take a break and have some coffee, or else you might get coder's block!")