import tkinter as tk
from tkinter import ttk

# Create the main window
root = tk.Tk()
root.title("SpeedCrunch Clone")
root.geometry("400x600")

# Input area for mathematical expressions
entry = tk.Entry(root, font=("Arial", 14), justify='right')
entry.pack(fill=tk.BOTH, padx=10, pady=10)


# Create a frame for the side panel
side_frame = ttk.Frame(root)
side_frame.pack(side=tk.RIGHT, fill=tk.Y)

# Tabs for history and user functions
notebook = ttk.Notebook(side_frame)
notebook.pack(fill=tk.BOTH, expand=True)

# Tab for user functions
user_functions_tab = ttk.Frame(notebook)
notebook.add(user_functions_tab, text="User Functions")

# Tab for history
history_tab = ttk.Frame(notebook)
notebook.add(history_tab, text="History")

# Start the main loop
root.mainloop()