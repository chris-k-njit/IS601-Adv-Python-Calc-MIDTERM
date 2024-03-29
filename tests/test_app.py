import sys
from unittest.mock import MagicMock, patch
import os
import logging
import pytest
from app import App

@pytest.fixture
def app_instance(monkeypatch):
    # This fixture sets an environment variable and instantiates the App class
    monkeypatch.setenv("ENVIRONMENT", "TEST")
    return App()

def test_some_functionality(app_instance):
    # This test checks if the application correctly identifies the environment variable
    assert app_instance.get_environment_variable("ENVIRONMENT") == "TEST"

def test_configure_logging(app_instance, caplog):
    caplog.clear()  # Clear any logs captured prior to this test.
    app_instance.configure_logging()
    # Print out all log messages captured by caplog
    for record in caplog.records:
        print(f"Captured log message: {record.message}")
    # Check for the presence of the expected log message
    log_messages = [record.message for record in caplog.records]
    assert "Logging configured." in log_messages, \
        "Expected log message 'Logging configured.' not found"

# def test_configure_logging(app_instance, caplog):
#     caplog.clear()  # Clear any logs captured prior to this test.
#     app_instance.configure_logging()
#     assert any("Logging configured." in record.message for record in caplog.records), \
#         "Expected log message 'Logging configured.' not found"


@pytest.mark.parametrize("user_input, expected", [
    (["exit"], "Now exiting the calculator program."),  # Adjusted to expect the correct output upon exiting
])
def test_app_start_response(app_instance, monkeypatch, capsys, user_input, expected):
    def input_side_effect(prompt):
        if user_input:
            return user_input.pop(0)
        else:
            return ""  # Return an empty string or handle the empty case as per your requirement

    monkeypatch.setattr('builtins.input', input_side_effect)

    with patch.object(sys, 'exit') as mock_exit:
        App = app_instance.start()

    mock_exit.assert_called_once_with(0)

    captured = capsys.readouterr()

    # Now we check if the exit message is part of the captured output
    assert expected in captured.out

@pytest.mark.parametrize("env_var, expected", [
    ("ENVIRONMENT", "TEST"),
    ("UNSET_VARIABLE", None)
])
def test_get_environment_variable(app_instance, env_var, expected):
    # This test verifies the retrieval of environment variables by the app
    value = app_instance.get_environment_variable(env_var)
    assert value == expected

def test_load_plugins(app_instance, monkeypatch):
    # This test checks the plugin loading mechanism of the application
    mock_module = MagicMock()
    monkeypatch.setattr('pkgutil.iter_modules', lambda _: [('mock_plugin', 'mock_name', True)])
    monkeypatch.setattr('importlib.import_module', lambda _: mock_module)
    app_instance.load_plugins()
    # This assertion needs adjustment based on your implementation
    # assert "mock_name" in app_instance.command_handler.commands

def test_keyboard_interrupt_graceful_shutdown(app_instance, monkeypatch, caplog):
    # This test ensures the application exits gracefully upon a KeyboardInterrupt
    monkeypatch.setattr('builtins.input', lambda _: exec('raise KeyboardInterrupt'))
    with pytest.raises(SystemExit):
        App = app_instance.start()
    assert "Application has been interrupted and is now exiting gracefully." in caplog.text

# # KEEP Below or get rid of????
#     ''' Test app.py here'''
# import logging
# import pytest
# from app import App  # Adjust import based on actual class name


# def test_app_get_environment_variable():
#     app = App()
# #   Retrieve the current environment setting
#     current_env = app.get_environment_variable('ENVIRONMENT')
#     # Assert that the current environment is what you expect
#     assert current_env in ['DEVELOPMENT', 'TESTING', 'PRODUCTION'], f"Invalid ENVIRONMENT: {current_env}"

# def test_app_start_exit_command(monkeypatch):
#     """Test that the REPL exits correctly or handles 'exit' command."""
#     monkeypatch.setattr('builtins.input', lambda _: 'exit')
#     app = App()
#     with pytest.raises(SystemExit) as e:
#         app.start()  # Assuming 'start' is the correct method name
    
#     assert e.type == SystemExit

# def test_app_start_unknown_command(capfd, monkeypatch):
#     """Test how the REPL handles an unknown command before exiting."""
#     inputs = iter(['unknown_command', 'exit'])
#     monkeypatch.setattr('builtins.input', lambda _: next(inputs))

#     app = App()
#     with pytest.raises(SystemExit) as e:
#         app.start()  # Adjust for the actual method name
#     assert e.value.code == 0
#     captured = capfd.readouterr()
#     # Make sure this matches the exact output format of your application
#     assert "No such command: 'unknown_command'" in captured.out
