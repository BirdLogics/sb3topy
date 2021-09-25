"""
blockutil.py

Contains functions and classes
primarily used within project.py
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


def pick_rand(val1, val2):
    """Rand int or float depending on values"""
    val1, val2 = min(val1, val2), max(val1, val2)
    if isinstance(val1, float) or isinstance(val2, float):
        return random.random() * abs(val2-val1) + val1
    return random.randint(val1, val2)


def gt(val1, val2):  # pylint: disable=invalid-name
    """Either numerical or string comparison"""
    try:
        return float(val1) > float(val2)
    except ValueError:
        return str(val1).lower() > str(val2).lower()


def lt(val1, val2):  # pylint: disable=invalid-name
    """Either numerical or string comparison"""
    try:
        return float(val1) < float(val2)
    except ValueError:
        return str(val1).lower() < str(val2).lower()


def eq(val1, val2):  # pylint: disable=invalid-name
    """Either numerical or string comparison"""
    try:
        return float(val1) == float(val2)
    except ValueError:
        return str(val1).lower() == str(val2).lower()


def div(val1, val2):
    """Divide handling division by zero"""
    try:
        return tonum(val1) / tonum(val2)
    except ZeroDivisionError:
        return float('infinity')


def sqrt(val):
    """Gets the square root handling negative values"""
    try:
        return math.sqrt(val)
    except ValueError:
        return float('nan')
