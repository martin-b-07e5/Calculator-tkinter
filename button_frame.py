import tkinter as tk
from tkinter import ttk
from operations.arithmetic import basic_calculation, percentage, factorial
from operations.advanced import square_root, power
from operations.parsing import parse_expression, extract_last_number, is_valid_expression

class ButtonFrame:
    def __init__(self, parent, result_frame):
        self.result_frame = result_frame

        # Create style for buttons with desired background
        style = ttk.Style()
        style.configure("Custom.TButton", background="#E9E9E9")

        # Create a frame for the buttons
        self.frame = ttk.Frame(parent)  # Changed from self.button_frame to self.frame

        # Configure grid for button frame
        self.frame.grid_rowconfigure(0, weight=1)
        self.frame.grid_rowconfigure(1, weight=1)
        self.frame.grid_rowconfigure(2, weight=1)
        self.frame.grid_rowconfigure(3, weight=1)
        self.frame.grid_columnconfigure(0, weight=1)
        self.frame.grid_columnconfigure(1, weight=1)
        self.frame.grid_columnconfigure(2, weight=1)
        self.frame.grid_columnconfigure(3, weight=1)
        self.frame.grid_columnconfigure(4, weight=1)
        self.frame.grid_columnconfigure(5, weight=1)

        # Button layout
        self.button_layout = [
            ["7", "8", "9", "/", "C", "√"],
            ["4", "5", "6", "*", "DEL", "^"],
            ["1", "2", "3", "-", "(", ")"],
            ["0", ".", "=", "+", "%", "!"],
        ]

        # Create buttons according to the specified layout
        for r, row in enumerate(self.button_layout):
            for c, value in enumerate(row):
                button = ttk.Button(
                    self.frame,
                    text=value,
                    style="Custom.TButton",
                    command=self.get_command(value)
                )
                button.grid(row=r, column=c, padx=5, pady=5, sticky="nsew")

        # Set calculate callback for Enter key or keypad Enter
        self.result_frame.set_calculate_callback(self.calculate_result)

        # Set clear callback for Escape key ← NUEVA LÍNEA
        self.result_frame.set_clear_callback(self.clear_all)

    def get_command(self, value):
        """Returns the corresponding function for each button"""
        commands = {
            "=": self.calculate_result,
            "C": self.clear_all,
            "DEL": self.delete_last,
            "√": self.square_root,
            "^": lambda: self.button_click("^"),
            "%": self.percentage,
            "!": self.factorial
        }

        return commands.get(value, lambda: self.button_click(value))

    def button_click(self, value):
        """Handles clicks on numeric buttons and basic operators"""
        current_input = self.result_frame.get_input()

        # If current input is "0", replace it (except for decimal point)
        if current_input == "0" and value not in [".", "%", "!"]:
            self.result_frame.set_input(str(value))
        else:
            self.result_frame.append_to_input(str(value))

    def clear_all(self):
        """Clears the input field"""
        self.result_frame.clear_input()

    def delete_last(self):
        """Deletes the last character from input"""
        self.result_frame.delete_last_char()

    def calculate_result(self):
        """Calculates the result of the current expression"""
        try:
            current_input = self.result_frame.get_input()
            if not current_input:
                return

            expression = parse_expression(current_input)
            result = basic_calculation(expression)

            # Add to history and clear input for next calculation
            self.result_frame.add_to_history(current_input, result)
            self.result_frame.clear_input()

        except Exception as e:
            # Show error in history but keep the input
            self.result_frame.add_to_history(current_input, f"Error: {str(e)}")

    def square_root(self):
        """Calculates square root of the current input"""
        try:
            current_input = self.result_frame.get_input()
            if not current_input:
                return

            # If there's a full expression, calculate it first
            if any(op in current_input for op in ['+', '-', '*', '/', '^']):
                expression = parse_expression(current_input)
                base_result = basic_calculation(expression)
                result = square_root(base_result)
                self.result_frame.add_to_history(f"√({current_input})", result)
            else:
                # Just calculate square root of the number
                result = square_root(current_input)
                self.result_frame.add_to_history(f"√{current_input}", result)

            self.result_frame.clear_input()

        except Exception as e:
            self.result_frame.add_to_history(self.result_frame.get_input(), f"Error: {str(e)}")

    def percentage(self):
        """Converts the current input to percentage"""
        try:
            current_input = self.result_frame.get_input()
            if not current_input:
                return

            result = percentage(current_input)
            self.result_frame.set_input(result)

        except Exception as e:
            self.result_frame.add_to_history(current_input, f"Error: {str(e)}")

    def factorial(self):
        """Calculates factorial of the current input"""
        try:
            current_input = self.result_frame.get_input()
            if not current_input:
                return

            result = factorial(current_input)
            self.result_frame.add_to_history(f"{current_input}!", result)
            self.result_frame.clear_input()

        except Exception as e:
            self.result_frame.add_to_history(current_input, f"Error: {str(e)}")
