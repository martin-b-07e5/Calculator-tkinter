"""Mathematical expression parsing and processing"""

import re


def parse_expression(expression):
    """Parses and normalizes mathematical expressions"""
    if not expression or expression.strip() == "":
        raise ValueError("Empty expression")

    # Clean spaces
    expression = expression.strip()

    # Replace alternative notations
    expression = expression.replace("×", "*").replace("÷", "/")

    # Validate allowed characters
    valid_chars = r"^[0-9+\-*/().\s^%!eE]+$"
    if not re.match(valid_chars, expression):
        raise ValueError("Invalid characters in expression")

    return expression
