"""Basic arithmetic operations"""
import math

def basic_calculation(expression):
    """Evaluates basic arithmetic expressions"""
    try:
        # Replace ^ with ** for exponents
        expression = expression.replace('^', '**')
        result = eval(expression)
        return str(result)
    except Exception as e:
        raise ValueError(f"Calculation error: {str(e)}")

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

