import tkinter as tk
from tkinter import ttk

class ButtonFrame:
    def __init__(self, parent, result_label):
        self.result_label = result_label

        # Create a frame for the buttons
        self.button_frame = ttk.Frame(parent)
        self.button_frame.pack(side=tk.BOTTOM, fill=tk.BOTH, padx=10, pady=10)

        # Button layout
        self.button_layout = [
            ["7", "8", "9", "/", "C"],
            ["4", "5", "6", "*", "E"],
            ["1", "2", "3", "-", "x"],
            ["0", ".", "=", "+"],
        ]

        # Create buttons according to the specified layout
        for r, row in enumerate(self.button_layout):
            for c, value in enumerate(row):
                button = ttk.Button(
                    self.button_frame,
                    text=value,
                    command=self.get_command(value)
                )
                button.grid(row=r, column=c, padx=5, pady=5, sticky="nsew")

        # Configure rows and columns to expand when resized
        for i in range(len(self.button_layout)):
            self.button_frame.grid_rowconfigure(i, weight=1)
        for j in range(len(self.button_layout[0])):
            self.button_frame.grid_columnconfigure(j, weight=1)

    def get_command(self, value):
        if value == "=":
            return self.calculate_result
        elif value == "C":
            return lambda: self.result_label.config(text="")  # Clear output
        else:
            return lambda v=value: self.button_click(v)

    def button_click(self, value):
        current_text = self.result_label.cget("text")
        self.result_label.config(text=current_text + str(value))  # Append value

    def calculate_result(self):
        try:
            expression = self.result_label.cget("text")
            result = eval(expression)  # Evaluate the expression
            self.result_label.config(text=f"= {result}")  # Show result
        except Exception:
            self.result_label.config(text="Error")
