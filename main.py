import tkinter as tk
from tkinter import ttk
from result_frame import ResultFrame
from button_frame import ButtonFrame
from side_panel import SidePanel

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("SpeedCrunch Clone")
        self.root.geometry("900x600")

        # Set minimum window size (fixed width, flexible height)
        self.root.minsize(900, 300)

        # Main container frame using grid for proper layout
        self.main_container = ttk.Frame(root)
        self.main_container.pack(fill=tk.BOTH, expand=True)

        # Configure grid weights for main container
        self.main_container.grid_rowconfigure(0, weight=1)  # Result section expands
        self.main_container.grid_rowconfigure(1, weight=0)  # Button frame fixed
        self.main_container.grid_columnconfigure(0, weight=1)  # Main content
        self.main_container.grid_columnconfigure(1, weight=0)  # Side panel fixed

        # Use the modular ResultFrame for output area
        self.result_section = ResultFrame(self.main_container)
        self.result_section.frame.grid(row=0, column=0, sticky="nsew", padx=10, pady=(10, 0))

        # Frame for Buttons, pass the entire ResultFrame instance
        self.button_frame = ButtonFrame(self.main_container, self.result_section)
        self.button_frame.frame.grid(row=1, column=0, sticky="ew", padx=10, pady=10)

        # Side Panel on the right
        self.side_panel = SidePanel(self.main_container)
        self.side_panel.side_frame.grid(row=0, column=1, rowspan=2, sticky="ns", padx=10, pady=10)

if __name__ == "__main__":
    root = tk.Tk()
    app_instance = CalculatorApp(root)
    root.mainloop()