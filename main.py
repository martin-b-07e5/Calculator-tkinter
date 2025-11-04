import tkinter as tk
from result_frame import ResultFrame  # import the new ResultFrame module
from button_frame import ButtonFrame
from side_panel import SidePanel


class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("SpeedCrunch Clone")
        self.root.geometry("900x600")

        # Set minimum window size (fixed width, flexible height)
        self.root.minsize(900, 250)

        # Use the modular ResultFrame for output area
        self.result_section = ResultFrame(self.root)

        # Frame for Buttons, pass the result_label for updating output
        self.button_frame = ButtonFrame(self.result_section.frame, self.result_section.result_label)

        # Side Panel on the right
        self.side_panel = SidePanel(self.root)
        self.side_panel.side_frame.pack(side=tk.RIGHT, fill=tk.Y, padx=10, pady=10)


if __name__ == "__main__":
    root = tk.Tk()
    app_instance = CalculatorApp(root)
    root.mainloop()
