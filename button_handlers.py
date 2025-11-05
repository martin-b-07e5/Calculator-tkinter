"""Button action handlers for calculator operations"""

from operations.arithmetic import basic_calculation, percentage, factorial
from operations.advanced import square_root, power
from operations.parsing import parse_expression, extract_last_number


class ButtonHandlers:
    def __init__(self, result_frame):
        self.result_frame = result_frame

    def handle_button_click(self, value):
        """Handles clicks on numeric buttons and basic operators"""
        current_input = self.result_frame.get_input()

        # If current input is "0", replace it (except for decimal point)
        if current_input == "0" and value not in [".", "%", "!"]:
            self.result_frame.set_input(str(value))
        else:
            self.result_frame.append_to_input(str(value))

    def clear_all(self):
        """Clears the input field"""
        self.result_frame.clear_input()

    def delete_last(self):
        """Deletes the last character from input"""
        self.result_frame.delete_last_char()

    def calculate_result(self):
        """Calculates the result of the current expression"""
        try:
            current_input = self.result_frame.get_input()
            if not current_input:
                return

            expression = parse_expression(current_input)
            result = basic_calculation(expression)

            # Add to history and clear input for next calculation
            self.result_frame.add_to_history(current_input, result)
            self.result_frame.clear_input()

        except Exception as e:
            # Show error in history but keep the input
            self.result_frame.add_to_history(current_input, f"Error: {str(e)}")

    def square_root(self):
        """Calculates square root of the current input"""
        try:
            current_input = self.result_frame.get_input()
            if not current_input:
                return

            # If there's a full expression, calculate it first
            if any(op in current_input for op in ["+", "-", "*", "/", "^"]):
                expression = parse_expression(current_input)
                base_result = basic_calculation(expression)
                result = square_root(base_result)
                self.result_frame.add_to_history(f"√({current_input})", result)
            else:
                # Just calculate square root of the number
                result = square_root(current_input)
                self.result_frame.add_to_history(f"√{current_input}", result)

            self.result_frame.clear_input()

        except Exception as e:
            self.result_frame.add_to_history(
                self.result_frame.get_input(), f"Error: {str(e)}"
            )

    def percentage(self):
        """Converts the current input to percentage"""
        try:
            current_input = self.result_frame.get_input()
            if not current_input:
                return

            result = percentage(current_input)
            self.result_frame.set_input(result)

        except Exception as e:
            self.result_frame.add_to_history(current_input, f"Error: {str(e)}")

    def factorial(self):
        """Calculates factorial of the current input"""
        try:
            current_input = self.result_frame.get_input()
            if not current_input:
                return

            result = factorial(current_input)
            self.result_frame.add_to_history(f"{current_input}!", result)
            self.result_frame.clear_input()

        except Exception as e:
            self.result_frame.add_to_history(current_input, f"Error: {str(e)}")
