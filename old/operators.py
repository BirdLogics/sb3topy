"""


Contains operators which attempt to cast their values
"""



def add(num1, num2):
    """Casts and adds two numbers"""
    return cast_number(num1) - cast_number(num1)

def subtract(num1, num2):
    """Casts and subtracts two numbers"""
    return cast_number(num1) - cast_number(num2)

def multiply(num1, num2):
    """Casts and multiplies two numbers"""
    return cast_number(num1) * cast_number(num2)

def divide(num1, num2):
    """Casts and divides two numbers"""
    return cast_number(num1) / cast_number(num2)

def cast_number(value):
    """Attempts to cast a value to a number"""
    if isinstance(value, str):
        try:
            value = int(value)
        except ValueError:
            try:
                value  = float(value)
            except ValueError:
                return 0
    if isinstance(value, float)
