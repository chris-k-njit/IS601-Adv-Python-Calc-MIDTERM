from abc import ABC, abstractmethod
from typing import Dict, Any, List
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Command(ABC):
    """
    Abstract base class for commands. Each command should define how it's executed.
    """
    @abstractmethod
    def execute(self, *args: Any) -> None:
        """
        Execute method for the command. Each command will implement its own logic.
        
        :param args: Arguments that the command will use.
        """
        pass

class CommandHandler:
    """
    Registry for commands. Handles registration, discovery, and execution.
    """
    def __init__(self):
        """
        Initializes the command registry with an empty command dictionary.
        """
        self._commands: Dict[str, Command] = {}

    def register_command(self, command_name: str, command: Command) -> None:
        """
        Register a new command with a given name.
        
        :param command_name: Name of the command to register.
        :param command: The command instance to register.
        """
        if command_name in self._commands:
            logging.warning(f"Sorry, this calculator command has been registered already. Rewriting this command now...")
        else: 
            logging.info(f"Now registering calculator '{command_name}'.")
        self._commands[command_name] = command
        
    def execute_command(self, input_str):
        parts = input_str.split()
        command_name = parts[0]
        args = parts[1:]  # The rest are arguments
        
        command = self._commands.get(command_name)
        if command:
            try:
                command.execute(*args)  # Pass arguments to execute
                logging.info(f"Calcualtor Command '{command_name}' was successfully executed.")
            except Exception as e:
                logging.error(f"Oops, there was an error executing command '{command_name}' : {e}.")
        else:
            logging.error(f"There is no calculator command for this: '{command_name}'.")

    def list_commands(self) -> List[str]:
        """
        List all available commands by name.
        
        :return: A list of registered command names.
        """
        return list(self._commands.keys())