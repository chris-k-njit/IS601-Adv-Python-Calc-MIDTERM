''' Test all commands here '''
import unittest
from unittest.mock import patch#, mock_open
from app.plugins.addition import AddCommand
from app.plugins.subtraction import SubtractCommand
from app.plugins.multiplication import MultiplyCommand
from app.plugins.division import DivideCommand
from app.plugins.squareroot import SqrtCommand
from app.plugins.greet import GreetCommand
from app.plugins.goodbye import ByeCommand
from app.plugins.caffeine import CaffeineCommand
from app.plugins.help import HelpCommand
# from app.plugins.calculation_history import CalculatorHistoryCommand

class TestCalculatorCommands(unittest.TestCase):
    ''' Test all commands'''
    @patch('builtins.print')
    def test_add_command(self, mock_print):
        AddCommand().execute(1, 2, 3)
        mock_print.assert_called_with('Result: 6.0')

    @patch('builtins.print')
    def test_subtract_command(self, mock_print):
        SubtractCommand().execute(10, 1, 2)
        mock_print.assert_called_with('Result: 7.0')

    @patch('builtins.print')
    def test_multiply_command(self, mock_print):
        MultiplyCommand().execute(2, 3, 4)
        mock_print.assert_called_with('Result: 24.0')

    @patch('builtins.print')
    def test_divide_command(self, mock_print):
        DivideCommand().execute(10, 2)
        mock_print.assert_called_with('Result: 5.0')

    @patch('builtins.print')
    def test_sqrt_command(self, mock_print):
        SqrtCommand().execute(16)
        mock_print.assert_called_with('Result: 4.0')

    @patch('builtins.print')
    def test_greet_command(self, mock_print):
        GreetCommand().execute()
        mock_print.assert_called_with("Hello! Welcome to Chris' the calculator. Type 'help' to see available commands.")

    @patch('builtins.print')
    def test_bye_command(self, mock_print):
        ByeCommand().execute()
        mock_print.assert_called_with("Goodbye! Thank you for using the calculator.")

    @patch('builtins.print')
    def test_caffeine_command(self, mock_print):
        CaffeineCommand().execute()
        mock_print.assert_called_with("Don't forget to take a break and have some coffee, or else you might get coder's block!")

    @patch('builtins.print')
    def test_help_command(self, mock_print):
        HelpCommand().execute()
        mock_print.assert_called_with("Available commands here are: addition, subtraction, multiplication, division, squareroot, greet, goodbye, caffeine, help\nUse 'exit' to quit the application.")

#     @patch('builtins.print')
#     @patch('builtins.input', side_effect=['1', 'exit'])  # Assuming '1' selects an option, 'exit' returns to the main menu
#     def test_calculation_history_command(self, mock_input, mock_print):
#         '''Test the calculation history command'''
#         CalculatorHistoryCommand().execute()
#         expected_calls = [
#             # Mock print calls you expect based on the '1' input and then 'exit'.
#             # For instance, if '1' should print the latest calculation, but since
#             # there might be no calculations yet, it could print a specific message.
#             # Add calls to mock_print.assert_has_calls with the expected messages.
#         ]
#         mock_print.assert_has_calls(expected_calls, any_order=True)
# # if __name__ == '__main__':
#     unittest.main()
