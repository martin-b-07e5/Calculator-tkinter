import tkinter as tk
from tkinter import ttk
from button_frame import ButtonFrame
from side_panel import SidePanel

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("SpeedCrunch Clone")
        self.root.geometry("900x600")

        # Frame for Results
        self.result_frame = ttk.Frame(self.root)
        self.result_frame.pack(side=tk.LEFT, fill=tk.Y, padx=10, pady=10)

        # Output label for results
        self.result_label = tk.Label(self.result_frame, font=("Arial", 14), height=2)
        self.result_label.pack(fill=tk.X)

        # Frame for Buttons
        self.button_frame = ButtonFrame(self.result_frame, self.result_label)

        # Side Panel
        self.side_panel = SidePanel(self.root)
        self.side_panel.side_frame.pack(side=tk.RIGHT, fill=tk.Y, padx=10, pady=10)

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()
