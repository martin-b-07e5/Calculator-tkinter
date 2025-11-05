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


def extract_last_number(expression):
    """Extracts the last number from an expression"""
    # Find numbers (integers, decimals, scientific notation)
    numbers = re.findall(r"[-+]?\d*\.?\d+(?:[eE][-+]?\d+)?", expression)
    return numbers[-1] if numbers else None


def is_valid_expression(expression):
    """Checks if the expression is syntactically valid"""
    try:
        # Count parentheses
        if expression.count("(") != expression.count(")"):
            return False

        # Check consecutive operators (except +- for negative numbers)
        if re.search(r"[*/^]{2,}", expression):
            return False

        return True
    except:
        return False
