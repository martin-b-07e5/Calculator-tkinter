import tkinter as tk
from tkinter import ttk

class SidePanel:
    def __init__(self, parent):
        self.side_frame = ttk.Frame(parent)

        # Configure grid for side frame
        self.side_frame.grid_rowconfigure(0, weight=1)
        self.side_frame.grid_columnconfigure(0, weight=1)

        self.notebook = ttk.Notebook(self.side_frame)

        # Create tabs for user functions and history
        self.user_functions_tab = ttk.Frame(self.notebook)
        self.history_tab = ttk.Frame(self.notebook)

        # Add tabs to the notebook
        self.notebook.add(self.user_functions_tab, text="User Functions")
        self.notebook.add(self.history_tab, text="History")

        self.notebook.grid(row=0, column=0, sticky="nsew")
