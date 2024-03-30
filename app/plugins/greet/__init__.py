import logging
from app.commands import Command

class GreetCommand(Command):
    def __init__(self):
        super().__init__()
        self.name="greet"
    
    def execute(self):
        logging.info("Hello! Welcome to Chris' the calculator. Type 'help' to see available commands.")
        logging.debug("Greet needs debugging")
        print("Hello! Welcome to Chris' the calculator. Type 'help' to see available commands.")