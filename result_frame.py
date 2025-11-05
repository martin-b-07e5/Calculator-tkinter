import tkinter as tk
from tkinter import ttk

class ResultFrame:
    """Result display frame with SpeedCrunch-style history and input fields."""

    def __init__(self, parent):
        # Main frame to hold the results section
        self.frame = ttk.Frame(parent)

        # Configure grid weights for proper expansion
        self.frame.grid_rowconfigure(0, weight=1)  # History expands
        self.frame.grid_rowconfigure(1, weight=0)  # Input field fixed height
        self.frame.grid_columnconfigure(0, weight=1)
        self.frame.grid_columnconfigure(1, weight=0)  # Scrollbar fixed

        # Multi-line Text widget for history (read-only)
        self.history_text = tk.Text(
            self.frame,
            font=("Courier New", 12),  # Monospaced font for alignment
            bg="#2F0A24",  # dark purple background
            fg="white",    # white font for contrast
            wrap=tk.WORD,
            state=tk.DISABLED,  # Make it read-only
            relief=tk.FLAT,
            borderwidth=0,
            padx=10,
            pady=10
        )
        self.history_text.grid(row=0, column=0, sticky="nsew", pady=(0, 10))

        # Add scrollbar to history
        history_scrollbar = ttk.Scrollbar(self.frame, orient=tk.VERTICAL, command=self.history_text.yview)
        history_scrollbar.grid(row=0, column=1, sticky="ns", pady=(0, 10))
        self.history_text.configure(yscrollcommand=history_scrollbar.set)

        # Single-line Entry widget for current input
        self.input_entry = tk.Entry(
            self.frame,
            font=("Courier New", 14),
            justify=tk.RIGHT,
            bg="#1A1A1A",  # Dark background
            fg="white",    # White text
            insertbackground="white",  # White cursor
            relief=tk.FLAT
        )
        self.input_entry.grid(row=1, column=0, columnspan=2, sticky="ew", pady=(0, 5))
        self.input_entry.focus_set()  # Focus on input field by default

        # Bind Enter key to calculate
        self.input_entry.bind('<Return>', self.on_enter_pressed)
        self.input_entry.bind('<KP_Enter>', self.on_enter_pressed)

         # Bind Escape key to clear input
        self.input_entry.bind('<Escape>', self.on_escape_pressed)

    def on_enter_pressed(self, event):
        """Handler for Enter key in input field"""
        # This will be connected to the calculate function from button_frame
        if hasattr(self, 'calculate_callback'):
            self.calculate_callback()

    def on_escape_pressed(self, event):
        """Handler for Escape key - clears the input field"""
        if hasattr(self, 'clear_callback'):
            self.clear_callback()

    def add_to_history(self, expression, result):
        """Adds a calculation to the history display"""
        self.history_text.config(state=tk.NORMAL)  # Enable writing

        # Format: "expression = result" on one line
        history_line = f"{expression} = {result}\n"
        self.history_text.insert(tk.END, history_line)

        # Auto-scroll to bottom
        self.history_text.see(tk.END)
        self.history_text.config(state=tk.DISABLED)  # Back to read-only

    def clear_input(self):
        """Clears the input field"""
        self.input_entry.delete(0, tk.END)

    def set_input(self, text):
        """Sets the input field text"""
        self.input_entry.delete(0, tk.END)
        self.input_entry.insert(0, text)

    def get_input(self):
        """Gets the current input text"""
        return self.input_entry.get()

    def append_to_input(self, text):
        """Appends text to the current input"""
        current = self.get_input()
        self.set_input(current + text)

    def delete_last_char(self):
        """Deletes the last character from input"""
        current = self.get_input()
        if current:
            self.set_input(current[:-1])

    def clear_history(self):
        """Clears the entire history"""
        self.history_text.config(state=tk.NORMAL)
        self.history_text.delete(1.0, tk.END)
        self.history_text.config(state=tk.DISABLED)

    def set_calculate_callback(self, callback):
        """Sets the callback function for calculation"""
        self.calculate_callback = callback

    def set_clear_callback(self, callback):
        """Sets the callback function for clearing input"""
        self.clear_callback = callback
