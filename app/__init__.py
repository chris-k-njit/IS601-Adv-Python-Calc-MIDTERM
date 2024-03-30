import os
import csv
import pkgutil
import importlib
import sys
import inspect
from app.commands import Command, CommandHandler
from dotenv import load_dotenv
import logging
import logging.config

class App:
    def __init__(self): # Constructor
        os.makedirs('logs', exist_ok=True)
        self.configure_logging()
        load_dotenv()
        self.initialize_data_directory() # New method I added, to account for CSV storing calculator calculations history.
        self.settings = self.load_environment_variables()
        self.settings.setdefault('ENVIRONMENT', 'DEVELOPMENT')
        self.command_handler = CommandHandler()

    def initialize_data_directory(self):
        data_dir = os.getenv('DATA_DIR', './data')
        csv_filename = os.getenv('CALCULATIONS_HISTORY_CSVFILE', 'all_calculator_calculations.csv')
        csv_filepath = os.path.join(data_dir, csv_filename)

        os.makedirs(data_dir, exist_ok=True)

        headers = ['Calculator Calculation', 'Calculator Result'] 
        with open(csv_filepath, 'w', newline='') as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow(headers)
        
        logging.info(f"Data directory for Chris Calculator Midterm Project '{data_dir}' and the CSV file for this Midterm Project '{csv_filename}' have been initialized.")
    
    def configure_logging(self):
        logging_conf_path = 'logging.conf'
        if os.path.exists(logging_conf_path):
            logging.config.fileConfig(logging_conf_path, disable_existing_loggers=False)
        else:
            logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
        logging.info("Logging has successfully configured.")

    def load_environment_variables(self):
        settings = {key: value for key, value in os.environ.items()}
        logging.info("Environment variables loaded.")
        return settings

    def get_environment_variable(self, env_var: str = 'ENVIRONMENT'):
        return self.settings.get(env_var, None)

    def load_plugins(self):
        # Assuming this method dynamically loads plugin modules
        plugins_package = 'app.plugins'
        for _, plugin_name, is_pkg in pkgutil.iter_modules([plugins_package.replace('.', '/')]):
            if is_pkg:
                plugin_module = importlib.import_module(f'{plugins_package}.{plugin_name}')
                self.register_plugin_commands(plugin_module)

    def register_plugin_commands(self, plugin_module):
        for item_name in dir(plugin_module):
            item = getattr(plugin_module, item_name)
            if inspect.isclass(item) and issubclass(item, Command) and item is not Command and not inspect.isabstract(item):
                # This ensures we're only instantiating non-abstract subclasses of Command
                command_instance = item()
                self.command_handler.register_command(command_instance.name, command_instance)

    def start(self):
        # Register commands here
        self.load_plugins()
        print("Type 'exit' to exit.")
        while True:  #REPL Read, Evaluate, Print, Loop
            cmd_input = self.get_command_input()
            if cmd_input.lower() == 'exit':
                    logging.info("Application exit.")
                    sys.exit(0)
            self.execute_command(cmd_input)

    def get_command_input(self):
            return  input(">>> ").strip()
    
    def execute_command(self, cmd_input):
        try: 
            self.command_handler.execute_command(cmd_input)
        except KeyError:
            logging.error(f"Unknown command entered: {cmd_input}")

if __name__ == "__main__":
    app = App()
    app.start()