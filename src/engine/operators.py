"""
operators.py

Contains functions primarily used by project.py to ensure maximum
compatibility.
"""

__all__ = [
    'tonum', 'toint', 'letter_of', 'pick_rand',
    'gt', 'lt', 'eq', 'div', 'sqrt'
]

import math
import random


def tonum(value):
    """Attempt to cast a value to a number"""
    try:
        value = float(value)
        if value.is_integer():
            return int(value)
        if math.isnan(value):
            return 0
        return value
    except ValueError:
        return 0


def toint(value):
    """Attempts to round a value to an int"""
    try:
        return round(float(value))
    except ValueError:
        return 0
    except OverflowError:
        return 0


def letter_of(text, index):
    """Gets a letter from string"""
    try:
        return text[index - 1]
    except IndexError:
        return ""


def pick_rand(number1, number2):
    """Rand int or float depending on values"""
    number1, number2 = min(number1, number2), max(number1, number2)
    if isinstance(number1, float) or isinstance(number2, float):
        return random.random() * abs(number2-number1) + number1
    return random.randint(number1, number2)


def gt(value1, value2):  # pylint: disable=invalid-name
    """Either numerical or string comparison"""
    try:
        return float(value1) > float(value2)
    except ValueError:
        return str(value1).lower() > str(value2).lower()


def lt(value1, value2):  # pylint: disable=invalid-name
    """Either numerical or string comparison"""
    try:
        return float(value1) < float(value2)
    except ValueError:
        return str(value1).lower() < str(value2).lower()


def eq(value1, value2):  # pylint: disable=invalid-name
    """Either numerical or string comparison"""
    try:
        return float(value1) == float(value2)
    except ValueError:
        return str(value1).lower() == str(value2).lower()


def div(value1, value2):
    """Divide handling division by zero"""
    try:
        return tonum(value1) / tonum(value2)
    except ZeroDivisionError:
        return float('infinity')


def sqrt(value):
    """Gets the square root handling negative values"""
    try:
        return math.sqrt(value)
    except ValueError:
        return float('nan')
