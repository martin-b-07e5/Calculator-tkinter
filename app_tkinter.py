import tkinter as tk
from tkinter import ttk
import math

# --------------------------------------------------
# Create the main window
root = tk.Tk()
root.title("SpeedCrunch Clone")

# Adjust the geometry of the main window
root.geometry("900x600")  # Increase height for better layout

# Input area for mathematical expressions
entry = tk.Text(root, font=("Arial", 14), height=3)  # Change Entry to Text for multiple lines
entry.pack(side=tk.TOP, fill=tk.X, padx=10, pady=(10, 0))  # Update padding for better layout

# Output label for the result (keeping the label for the result display)
result_label = tk.Label(root, font=("Arial", 14), height=2)  # Give it some height for better appearance
result_label.pack(side=tk.TOP, fill=tk.X, padx=10, pady=(0, 10))

# Create a frame for the side panel
# Make the side panel fill the entire vertical space
side_frame = ttk.Frame(root)
side_frame.pack(side=tk.RIGHT, fill=tk.Y)

# Tabs for "history and user functions"
notebook = ttk.Notebook(side_frame)
notebook.pack(fill=tk.BOTH, expand=True)

# Tab for user functions
user_functions_tab = ttk.Frame(notebook)
notebook.add(user_functions_tab, text="User Functions")

# Tab for history
history_tab = ttk.Frame(notebook)
notebook.add(history_tab, text="History")

# --------------------------------------------------
# Function to handle button clicks
def button_click(value):
    current_text = entry.get()
    entry.delete(0, tk.END)  # Clear the current text
    entry.insert(0, current_text + str(value))  # Append the clicked value

def calculate_result():
    try:
        expression = entry.get()
        result = eval(expression)  # Evaluate the expression
        result_label.config(text=f"= {result}")  # Show result
    except Exception as e:
        result_label.config(text="Error")

# Create a frame for the buttons at the bottom left
button_frame = ttk.Frame(root)
button_frame.pack(side=tk.BOTTOM, fill=tk.X, padx=10, pady=10)

# Button layout as specified
button_layout = [
    ["7", "8", "9", "/", "C", "sqr", "pi", "exp", "ln"],
    ["4", "5", "6", "*", "E", "^", "ans", "sin", "arcsin"],
    ["1", "2", "3", "-", "(", ")", "x", "cos", "arccos"],
    ["0", ".", "=", "+", ")", "!", "x=", "tan", "arctan"],
]

# Create buttons according to the specified layout
for r, row in enumerate(button_layout):
    for c, value in enumerate(row):
        if value == "=":
            button = ttk.Button(button_frame, text=value, command=calculate_result)
        elif value == "C":
            button = ttk.Button(button_frame, text=value, command=lambda: entry.delete(0, tk.END))  # Clear entry
        else:
            button = ttk.Button(button_frame, text=value, command=lambda v=value: button_click(v))
        button.grid(row=r, column=c, padx=5, pady=5)

# Make the button grid expand proportionally
for row in range(len(button_layout)):
    button_frame.grid_rowconfigure(row, weight=1)

# Start the main loop (only once at the end)
root.mainloop()
