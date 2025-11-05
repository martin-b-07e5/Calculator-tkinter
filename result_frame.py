import tkinter as tk
from tkinter import ttk


class ResultFrame:
    """Result display frame that shows calculation output with a styled label."""

    def __init__(self, parent):
        # Main frame to hold the results section
        self.frame = ttk.Frame(parent)
        self.frame.pack(side=tk.LEFT, fill=tk.Y, padx=10, pady=10)

        # Label for output (2 lines), with dark purple background and white text
        self.result_label = tk.Label(
            self.frame,
            font=("Arial", 14),
            height=2,
            bg="#2F0A24",  # dark purple background
            fg="white",  # white font for contrast
        )
        self.result_label.pack(fill=tk.X)
