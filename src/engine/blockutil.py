"""
blockutil.py

Contains functions and classes
primarily used within project.py
"""

__all__ = [
    'List',
    'tonum', 'letter_of', 'pick_rand',
    'gt', 'lt', 'eq', 'div'
]

import random


class List:
    """Handles special list behaviors"""

    def __init__(self, values):
        self.list = values

    def __getitem__(self, key):
        key = self._to_index(key)
        if key is not None:
            return self.list[key]
        return ""

    def __setitem__(self, key, value):
        key = self._to_index(key)
        if key is not None:
            self.list[key] = value

    def append(self, value):
        """Add up to 200,000 items to list"""
        if len(self.list) < 200000:
            self.list.append(value)

    def insert(self, key, value):
        """Insert up to 200,000 items in list"""
        if len(self.list) < 200000:
            if key == "first":
                key = 0
            elif key == "last":
                key = -1
            elif key == "random":
                key = random.randint(0, len(self.list))
            else:
                key = round(tonum(key)) - 1

            if key is not None and 0 <= key <= len(self.list):
                self.list.insert(key, value)

    def delete(self, key):
        """Remove an item from list"""
        if key == "all":
            self.list = []
        else:
            key = self._to_index(key)
            if key is not None:
                self.list.pop(key)

    def delete_all(self):
        """Delete all items in list"""
        self.list = []

    def _to_index(self, key):
        """Gets the index of first, last, random strings"""
        if self.list:
            if key == "first":
                return 0
            if key == "last":
                return -1
            if key == "random":
                return random.randint(0, len(self.list) - 1)
            key = round(tonum(key))
            if 0 < key <= len(self.list):
                return key - 1
        return None

    def __contains__(self, item):
        item = str(item).casefold()
        for value in self.list:
            if item == str(value).casefold():
                return True
        return False

    def __str__(self):
        char_join = True
        for item in self.list:
            if len(str(item)) != 1:
                char_join = False
                break
        if char_join:
            return ''.join(self.list)
        return ' '.join(self.list)

    def __len__(self):
        return self.list.__len__()

    # TODO Variable/list reporters
    def show(self):
        """Print list"""
        print(self.list)

    def hide(self):
        """Do nothing"""

    def index(self, item):
        """Find the index of an item, case insensitive"""
        item = str(item).casefold()
        for i, value in enumerate(self.list):
            if str(value).casefold() == item:
                return i + 1
        return 0

    def index1(self, item):
        """Find the index of an item in the list"""
        try:
            return self.list.index(item) + 1
        except ValueError:
            return 0

    def copy(self):
        """Return a copy of this List"""
        return List(self.list.copy())


def tonum(value):
    """Attempt to cast a value to a number"""
    if isinstance(value, str):
        try:
            value = float(value)
            if value.is_integer():
                value = int(value)
        except ValueError:
            return 0
    if value == float('NaN'):
        return 0
    return value


def letter_of(text, index):
    """Gets a letter from string"""
    try:
        return str(text)[tonum(index) - 1]
    except IndexError:
        return ""


def pick_rand(val1, val2):
    """Rand int or float depending on values"""
    val1 = tonum(val1)
    val2 = tonum(val2)
    val1, val2 = min(val1, val2), max(val1, val2)
    if isinstance(val1, float) or isinstance(val2, float):
        return random.random() * abs(val2-val1) + val1
    return random.randint(val1, val2)


def gt(val1, val2):  # pylint: disable=invalid-name
    """Either numerical or string comparison"""
    try:
        return float(val1) > float(val2)
    except ValueError:
        return str(val1).casefold() > str(val2).casefold()


def lt(val1, val2):  # pylint: disable=invalid-name
    """Either numerical or string comparison"""
    try:
        return float(val1) < float(val2)
    except ValueError:
        return str(val1).casefold() < str(val2).casefold()


def eq(val1, val2):  # pylint: disable=invalid-name
    """Either numerical or string comparison"""
    try:
        return float(val1) == float(val2)
    except ValueError:
        return str(val1).casefold() == str(val2).casefold()


def div(val1, val2):
    """Divide handling division by zero"""
    try:
        return tonum(val1) / tonum(val2)
    except ZeroDivisionError:
        return float('infinity')
