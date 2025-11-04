import tkinter as tk
from tkinter import ttk

class SidePanel:
    def __init__(self, parent):
        self.side_frame = ttk.Frame(parent)
        self.notebook = ttk.Notebook(self.side_frame)

        # Create tabs for user functions and history
        self.user_functions_tab = ttk.Frame(self.notebook)
        self.history_tab = ttk.Frame(self.notebook)

        # Add tabs to the notebook
        self.notebook.add(self.user_functions_tab, text="User Functions")
        self.notebook.add(self.history_tab, text="History")

        self.notebook.pack(fill=tk.BOTH, expand=True)

        self.side_frame.pack(side=tk.RIGHT, fill=tk.Y)
