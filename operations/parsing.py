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

    # Validate allowed characters (updated to include power() function)
    valid_chars = r"^[0-9+\-*/().\s^%!eEa-zA-Z_,]+$"
    if not re.match(valid_chars, expression):
        raise ValueError("Invalid characters in expression")

    return expression


def _replace_power_operator(expression):
    """Replaces ^ operator with power function calls"""
    # Pattern to find any valid expression before and after ^
    # This handles: numbers, variables, parenthesized expressions
    pattern = r"([0-9]+(?:\.[0-9]+)?|\([^)]+\)|[a-zA-Z_][a-zA-Z0-9_]*)\s*\^\s*([0-9]+(?:\.[0-9]+)?|\([^)]+\)|[a-zA-Z_][a-zA-Z0-9_]*)"

    def replace_match(match):
        base = match.group(1)
        exponent = match.group(2)
        return f"power({base}, {exponent})"

    # Apply replacement until no more ^ operators are found
    while "^" in expression:
        new_expression = re.sub(pattern, replace_match, expression)
        if new_expression == expression:  # No changes made
            break
        expression = new_expression

    return expression
