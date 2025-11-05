"""Advanced mathematical operations"""
import math

def square_root(number):
    """Calculates square root"""
    try:
        n = float(number)
        if n < 0:
            raise ValueError("Square root not defined for negative numbers")
        return str(math.sqrt(n))
    except ValueError:
        raise ValueError("Invalid value for square root")

def power(base, exponent):
    """Calculates base^exponent"""
    try:
        base_num = float(base)
        exp_num = float(exponent)
        return str(math.pow(base_num, exp_num))
    except ValueError:
        raise ValueError("Invalid values for power operation")

def scientific_notation(number):
    """Converts to scientific notation"""
    try:
        n = float(number)
        return f"{n:.2e}"
    except ValueError:
        raise ValueError("Invalid value for scientific notation")