def is_valid(a, b):
    """Check if both a and b are numbers (int or float)."""
    return isinstance(a, (int, float)) and isinstance(b, (int, float))

def add(a, b):
    if not is_valid(a, b):
        print("Both a and b must be numbers.")
        return None
    return a + b

def subtract(a, b):
    if not is_valid(a, b):
        print("Both a and b must be numbers.")
        return None
    return a - b

def multiply(a, b):
    if not is_valid(a, b):
        print("Both a and b must be numbers.")
        return None
    return a * b

def divide(a, b):
    if not is_valid(a, b):
        raise ValueError("Both a and b must be numbers.")  
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero.") 
    return a / b


def exponentiate(a, b):
    if not is_valid(a, b):
        print("Both a and b must be numbers.")
        return None
    return a ** b
