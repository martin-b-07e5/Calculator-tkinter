import tkinter as tk
from tkinter import ttk
from button_frame import ButtonFrame
from side_panel import SidePanel


class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("SpeedCrunch Clone")
        self.root.geometry("900x600")

        # Set minimum width to initial width, but smaller height allowed
        self.root.minsize(
            900, 250
        )  # Adjust 200 if needed to fit min height requirements

        # Frame for Results
        self.result_frame = ttk.Frame(self.root)
        self.result_frame.pack(side=tk.LEFT, fill=tk.Y, padx=10, pady=10)

        # Output label for results - at least two lines needed; height=2 already set
        self.result_label = tk.Label(
            self.result_frame,
            font=("Arial", 14),
            height=2,
            bg="#2F0A24",  # Set result background color
            fg="white"  # Set text color for contrast on dark bg
        )
        self.result_label.pack(fill=tk.X)

        # Frame for Buttons
        self.button_frame = ButtonFrame(self.result_frame, self.result_label)

        # Side Panel
        self.side_panel = SidePanel(self.root)
        self.side_panel.side_frame.pack(side=tk.RIGHT, fill=tk.Y, padx=10, pady=10)


if __name__ == "__main__":
    root = tk.Tk()
    app_instance = CalculatorApp(root)
    root.mainloop()
