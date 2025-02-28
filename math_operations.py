"""This module provides basic math operations like add, subtract, multiply, divide, and exponentiate."""

def is_valid(a, b):
    """Check if both a and b are numbers (int or float)."""
    return isinstance(a, (int, float)) and isinstance(b, (int, float))

def add(a, b):
    """Add two numbers.

    Args:
        a (int or float): The first number.
        b (int or float): The second number.

    Returns:
        int or float: The sum of a and b.
    """
    if not is_valid(a, b):
        raise ValueError("Both a and b must be numbers.")
    return a + b

def subtract(a, b):
    """Subtract two numbers.

    Args:
        a (int or float): The first number.
        b (int or float): The second number.

    Returns:
        int or float: The result of a - b.
    """
    if not is_valid(a, b):
        raise ValueError("Both a and b must be numbers.")
    return a - b

def multiply(a, b):
    """Multiply two numbers.

    Args:
        a (int or float): The first number.
        b (int or float): The second number.

    Returns:
        int or float: The product of a and b.
    """
    if not is_valid(a, b):
        raise ValueError("Both a and b must be numbers.")
    return a * b

def divide(a, b):
    """Divide two numbers.

    Args:
        a (int or float): The numerator.
        b (int or float): The denominator.

    Returns:
        float: The result of a / b.

    Raises:
        ValueError: If a or b is not a number.
        ZeroDivisionError: If b is zero.
    """
    if not is_valid(a, b):
        raise ValueError("Both a and b must be numbers.")
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return a / b

def exponentiate(a, b):
    """Raise a to the power of b.

    Args:
        a (int or float): The base.
        b (int or float): The exponent.

    Returns:
        int or float: The result of a ** b.
    """
    if not is_valid(a, b):
        raise ValueError("Both a and b must be numbers.")
    return a ** b