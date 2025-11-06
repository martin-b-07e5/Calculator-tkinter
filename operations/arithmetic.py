"""Basic arithmetic operations"""
import math

def basic_calculation(expression):
    """Evaluates basic arithmetic expressions"""
    try:
        # Replace ^ with power function call
        expression = _replace_power_operator(expression)
        result = eval(expression) # ← ALL BASIC OPERATIONS ARE PERFORMED HERE
        return str(result)
    except Exception as e:
        raise ValueError(f"Calculation error: {str(e)}")

def _replace_power_operator(expression):
    """Replaces ^ operator with power function calls"""
    import re
    # Pattern to find number^number
    pattern = r'(\d+(?:\.\d+)?)\s*\^\s*(\d+(?:\.\d+)?)'

    def replace_match(match):
        base = match.group(1)
        exponent = match.group(2)
        return f'power({base}, {exponent})'

    return re.sub(pattern, replace_match, expression)

def power(base, exponent):
    """Calculates base^exponent"""
    try:
        base_num = float(base)
        exp_num = float(exponent)
        return math.pow(base_num, exp_num)
    except ValueError:
        raise ValueError("Invalid values for power operation")

def square_root(number):
    """Calculates square root"""
    try:
        n = float(number)
        if n < 0:
            raise ValueError("Square root not defined for negative numbers")
        return str(math.sqrt(n))
    except ValueError:
        raise ValueError("Invalid value for square root")

def percentage(number):
    """Converts a number to percentage (divide by 100)"""
    try:
        return str(float(number) / 100)
    except ValueError:
        raise ValueError("Invalid value for percentage")

def factorial(number):
    """Calculates factorial of a number"""
    try:
        n = int(float(number))
        if n < 0:
            raise ValueError("Factorial not defined for negative numbers")
        if n > 100:  # Limit to avoid heavy computations
            raise ValueError("Number too large for factorial")
        return str(math.factorial(n))
    except (ValueError, OverflowError) as e:
        raise ValueError(f"Factorial error: {str(e)}")
