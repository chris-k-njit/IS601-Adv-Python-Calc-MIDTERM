from app.commands import Command
import logging

class CalculatorHistory(Command):
    """
    Handles actions related to the calculation history, including viewing, clearing, saving,
    loading, and deleting history entries.
    """
    def __init__(self):
        self.command_name = "history"
        self.description = "Options for calculation history management."

    def run(self):
        """Shows the menu for history-related actions and handles user input."""
        actions = {
            'A': self.load_from_csv,
            'B': self.save_to_csv,
            'C': self.show_recent,
            'D': self.show_all,
            'E': self.clear_all,
            'F': self.remove_entry,
        }
        
        while True:
            self.display_menu()
            user_input = input("Select an option from this list or type 'exit' to go back: ").strip().lower()
            if user_input == 'exit':
                break
            self.handle_action(user_input, actions)

    def display_menu(self):
        print("\nChris' Calculation History (Menu):")
        print("A - Load csv calculation history.")
        print("B - Save calculation history to a CSV file.")
        print("C - Show the last completed calculation.")
        print("D - Display all calculations saved in app history.")
        print("E - Clear calculator history.")
        print("F - Delete an entry from calculator history.")

    def handle_action(self, choice, actions):
        action = actions.get(choice)
        if action:
            action()
        else:
            print("Please select a valid option.")

    # Action methods
    def load_from_csv(self):
        """Loads history from a CSV file."""
        try:
            self.history_manager.load_csv()
            print("History loaded from CSV.")
        except Exception as e:
            logging.error(f"Failed to load history from CSV: {e}")
            print("An error occurred while loading the history.")

    def save_to_csv(self):
        """Saves the current history to a CSV file."""
        self.history_manager.save_csv()
        print("Calculation history was saved to CSV.")

    def show_recent(self):
        """Displays the most recent calculation."""
        calculation = self.history_manager.latest()
        self.display_calculation(calculation)

    def show_all(self):
        """Displays all calculations in history."""
        for i, calculation in enumerate(self.history_manager.all(), 1):
            self.display_calculation(calculation, index=i)

    def clear_all(self):
        """Clears all calculation history."""
        self.history_manager.clear()
        print("History has been cleared.")

    def remove_entry(self):
        """Removes a specific entry from the history based on user input."""
        entry_index = input("Enter the entry number to delete: ")
        try:
            self.history_manager.delete(int(entry_index))
            print(f"Entry {entry_index} has been deleted.")
        except (ValueError, IndexError):
            print("Invalid entry. Please enter a valid number.")

    def display_calculation(self, calculation, index=None):
        if calculation:
            prefix = f"{index}: " if index is not None else ""
            print(f"{prefix}{calculation}")
        else:
            print("No calculation was found.")