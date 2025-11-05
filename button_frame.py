import tkinter as tk
from tkinter import ttk
from operations.arithmetic import basic_calculation, percentage, factorial
from operations.advanced import square_root, power
from operations.parsing import (
    parse_expression,
    extract_last_number,
    is_valid_expression,
)


class ButtonFrame:
    def __init__(self, parent, result_label):
        self.result_label = result_label
        self.current_expression = ""

        # Create style for buttons with desired background
        style = ttk.Style()
        style.configure("Custom.TButton", background="#E9E9E9")

        # Create a frame for the buttons
        self.button_frame = ttk.Frame(parent)
        self.button_frame.pack(side=tk.BOTTOM, fill=tk.BOTH, padx=10, pady=10)

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
                    self.button_frame,
                    text=value,
                    style="Custom.TButton",
                    command=self.get_command(value),
                )
                button.grid(row=r, column=c, padx=5, pady=5, sticky="nsew")

        # Configure rows and columns to expand when resized
        for i in range(len(self.button_layout)):
            self.button_frame.grid_rowconfigure(i, weight=1)
        for j in range(len(self.button_layout[0])):
            self.button_frame.grid_columnconfigure(j, weight=1)

    def get_command(self, value):
        """Returns the corresponding function for each button"""
        commands = {
            "=": self.calculate_result,
            "C": self.clear_all,
            "DEL": self.delete_last,
            "√": self.square_root,
            "^": lambda: self.button_click("^"),
            "%": self.percentage,
            "!": self.factorial,
        }

        return commands.get(value, lambda: self.button_click(value))

    def button_click(self, value):
        """Handles clicks on numeric buttons and basic operators"""
        self.current_expression += str(value)
        self.update_display()

    def clear_all(self):
        """Clears the entire expression"""
        self.current_expression = ""
        self.update_display()

    def delete_last(self):
        """Deletes the last character"""
        self.current_expression = self.current_expression[:-1]
        self.update_display()

    def update_display(self):
        """Updates the label with current expression"""
        display_text = self.current_expression if self.current_expression else "0"
        self.result_label.config(text=display_text)

    def calculate_result(self):
        """Calculates the result of the current expression"""
        try:
            if not self.current_expression:
                return

            expression = parse_expression(self.current_expression)
            result = basic_calculation(expression)
            self.current_expression = result
            self.update_display()

        except Exception as e:
            self.result_label.config(text=f"Error: {str(e)}")
            self.current_expression = ""

    def square_root(self):
        """Calculates square root of the last number"""
        try:
            last_number = extract_last_number(self.current_expression)
            if last_number:
                result = square_root(last_number)
                # Replace the last number with its square root
                self.current_expression = (
                    self.current_expression.rsplit(last_number, 1)[0] + result
                )
                self.update_display()
            else:
                self.result_label.config(text="Error: No number found")
        except Exception as e:
            self.result_label.config(text=f"Error: {str(e)}")

    def percentage(self):
        """Converts the last number to percentage"""
        try:
            last_number = extract_last_number(self.current_expression)
            if last_number:
                result = percentage(last_number)
                self.current_expression = (
                    self.current_expression.rsplit(last_number, 1)[0] + result
                )
                self.update_display()
            else:
                self.result_label.config(text="Error: No number found")
        except Exception as e:
            self.result_label.config(text=f"Error: {str(e)}")

    def factorial(self):
        """Calculates factorial of the last number"""
        try:
            last_number = extract_last_number(self.current_expression)
            if last_number:
                result = factorial(last_number)
                self.current_expression = (
                    self.current_expression.rsplit(last_number, 1)[0] + result
                )
                self.update_display()
            else:
                self.result_label.config(text="Error: No number found")
        except Exception as e:
            self.result_label.config(text=f"Error: {str(e)}")
