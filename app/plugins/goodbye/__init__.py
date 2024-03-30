from app.commands import Command

class ByeCommand(Command):
    def __init__(self):
        super().__init__()
        self.name="bye"
    
    def execute(self):
        print("Goodbye! Thank you for using the calculator.")