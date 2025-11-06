import tkinter as tk
from tkinter import ttk
from button_handlers import ButtonHandlers


class ButtonFrame:
    def __init__(self, parent, result_frame):
        self.result_frame = result_frame
        self.handlers = ButtonHandlers(result_frame)

        # Create style for buttons with desired background
        style = ttk.Style()
        style.configure("Custom.TButton", background="#E9E9E9")

        # Create a frame for the buttons
        self.frame = ttk.Frame(parent)

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
                    command=self.get_command(value),
                )
                button.grid(row=r, column=c, padx=5, pady=5, sticky="nsew")

        # Set callbacks for keyboard shortcuts
        self.result_frame.set_calculate_callback(self.handlers.calculate_result)
        self.result_frame.set_clear_callback(self.handlers.clear_all)

    def get_command(self, value):
        """Returns the corresponding function for each button"""
        commands = {
            "=": self.handlers.calculate_result,
            "C": self.handlers.clear_all,
            "DEL": self.handlers.delete_last,
            "√": self.handlers.square_root,
            "^": lambda: self.handlers.handle_button_click("^"),
            "%": self.handlers.percentage,
            "!": self.handlers.factorial,
        }

        return commands.get(value, lambda: self.handlers.handle_button_click(value))

