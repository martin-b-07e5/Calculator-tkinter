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

    # Replace ^ operator with power function calls
    expression = _replace_power_operator(expression)

    # Validate allowed characters
    valid_chars = r"^[0-9+\-*/().\s^%!eE]+$"
    if not re.match(valid_chars, expression):
        raise ValueError("Invalid characters in expression")

    return expression

def _replace_power_operator(expression):
    """Replaces ^ operator with power function calls"""
    # Pattern to find number^number
    pattern = r'(\d+(?:\.\d+)?)\s*\^\s*(\d+(?:\.\d+)?)'

    def replace_match(match):
        base = match.group(1)
        exponent = match.group(2)
        return f'power({base}, {exponent})'

    return re.sub(pattern, replace_match, expression)
