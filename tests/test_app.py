import logging
import pytest
from app import App
from unittest.mock import patch, mock_open

class ListHandler(logging.Handler):
    def __init__(self):
        super().__init__()
        self.log_records = []
    
    def emit(self, record):
        self.log_records.append(record)

@pytest.fixture
def app():
    app_instance = App()
    log_handler = ListHandler()
    logging.getLogger().addHandler(log_handler)
    yield app_instance, log_handler
    logging.getLogger().removeHandler(log_handler)

def test_configure_logging_default(app):
    """Test the default logging configuration is applied if logging.conf does not exist."""
    app_instance, log_handler = app
    with patch('os.path.exists', return_value=False):
        app_instance.configure_logging()
    assert any("Logging has successfully configured." in record.msg for record in log_handler.log_records)
    
def test_configure_logging_from_file(app, monkeypatch):
    """Test logging configuration from a file."""
    app_instance, log_handler = app
    config_file_content = "[loggers]\nkeys=root\n"
    with patch('os.path.exists', return_value=True), \
         patch('builtins.open', mock_open(read_data=config_file_content)), \
         patch('logging.config.fileConfig') as mock_fileConfig:
        app_instance.configure_logging()
    assert any("Logging has successfully configured." in record.msg for record in log_handler.log_records)
    mock_fileConfig.assert_called_once()

def test_initialize_data_directory(app, tmp_path):
    """Test the initialization of the data directory and CSV file."""
    app_instance, _ = app
    # Use tmp_path to create a temporary directory for the test
    with patch.dict('os.environ', {'DATA_DIR': str(tmp_path), 'CALCULATIONS_HISTORY_CSVFILE': 'all_calculator_calculations.csv'}):
        app_instance.initialize_data_directory()
    assert (tmp_path / 'all_calculator_calculations.csv').exists()

def test_app_start_unknown_command(app):
    """Test handling and logging of an unknown command."""
    app_instance, log_handler = app
    # Use an iterator to simulate first entering 'unknown_command', then 'exit'
    input_values = iter(['unknown_command', 'exit'])
    with patch('builtins.input', lambda _: next(input_values)), \
         pytest.raises(SystemExit):
        app_instance.start()
    assert any("An unknown command has been entered: unknown_command" in record.msg for record in log_handler.log_records)

def test_get_environment_variable(app):
    """Test retrieval of environment variables."""
    expected_env = "PRODUCTION"
    assert app.get_environment_variable('ENVIRONMENT') == expected_env

def test_app_start_exit_command(app):
    """Test that the REPL exits correctly on 'exit' command."""
    app_instance, log_handler = app
    with patch('builtins.input', return_value='exit'), pytest.raises(SystemExit) as ex:
        app_instance.start()
    assert ex.value.code == 0

    # Optional: Check for clean exit logs if your application logs on exit.
    # Ensures no unexpected errors or warnings are logged during shutdown.
    assert not any(record.levelname == 'ERROR' for record in log_handler.log_records), "There are unexpected ERROR logs during exit."
    assert not any(record.levelname == 'WARNING' for record in log_handler.log_records), "There are unexpected WARNING logs during exit."