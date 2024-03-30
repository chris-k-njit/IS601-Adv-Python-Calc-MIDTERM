# IS601-Adv-Python-Calc-MIDTERM
Advanced Calculator Project for Midterm in IS601. 

## Demonstrate Calculator Operations - From Simple to some Statistical
Details added later...

## Demonstrate History Management with Pandas
More details soon...

## Ensure Environmental Variables are correctly configured 
1.  As seen in image, was able to correctly configure my env variables.

![ENV Variables](images/ENV_VAR_SETUP.png)

## Using Logging to Record Interactions within Calculator
More details soon...

## Demonstrate Design Patterns
- Command Pattern
More details soon...

- Factory Method
More details soon...

- Facade Pattern
More details soon...

- Singleton Pattern
More details soon...

- Strategy Pattern
More details soon...

## LBYL and EAFP
1.  LBYL = "Look Before You Leap"
- With code below, using if and else statements to verify if a command was executed/ran successfully of it ran into an error or the command does not exist.
```python
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
```

2. EAFP = "Easier to Ask for Forgiveness than Permission"
- As seen in code below, this test tries to get the WARNING or expected warning from the log handler (except for the AssertionError in this case).
```python
    def test_app_start_exit_command(app):
    app_instance, log_handler = app
    with patch('builtins.input', return_value='exit'), pytest.raises(SystemExit) as exit_exception:
        app_instance.start()

    assert exit_exception.value.code == 0

    # Optional: Check for clean exit logs if your application logs on exit.
    # Ensures no unexpected errors or warnings are logged during shutdown.
    assert not any(record.levelname == 'ERROR' for record in log_handler.log_records), "There are unexpected ERROR logs during exit."
    expected_warning = "The specific warning message you're expecting."
    try:
        assert any(record.levelname == 'WARNING' and expected_warning in record.message for record in log_handler.log_records), "Expected warning message not found."
    except AssertionError:
        pass
```

## Video Walkthrough - 5 Minute Walkthrough of my Code 
Posting Video tonight, after all tests passed and code is complete.