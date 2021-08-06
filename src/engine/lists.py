"""
lists.py

Handles data structures related to lists

TODO Toggleable list compatibility
A new list type based on List should be created.
The specmap would need to be adjusted to handle it.
"""

import random

from . import config
from .blockutil import toint, tonum

__all__ = ['BaseList', 'StaticList']


class List:
    """Handles special list behaviors"""

    def __init__(self, values):
        self.list = values
        self.search = []
        for item in values:
            if isinstance(item, float) and item.is_integer():
                item = int(item)
            self.search.append(str(item).lower())

    def __getitem__(self, key):
        if self.list:
            if key == "first":
                return self.list[0]
            if key == "last":
                return self.list[-1]
            if key == "random":
                return self.list[random.randint(0, len(self.list) - 1)]
            key = round(tonum(key)) - 1
            if 0 <= key < len(self.list):
                return self.list[key]
        return ""

    def __setitem__(self, key, value):
        if self.list:
            if key == "first":
                self.list[0] = value
                self.search[0] = search_str(value)
            elif key == "last":
                self.list[-1] = value
                self.search[-1] = search_str(value)
            elif key == "random":
                key = random.randint(0, len(self.list) - 1)
                self.list[key] = value
                self.search[key] = search_str(value)
            else:
                key = round(tonum(key)) - 1
                if 0 <= key < len(self.list):
                    self.list[key] = value
                    self.search[key] = search_str(value)

    def append(self, value):
        """Add up to 200,000 items to list"""
        if len(self.list) < config.MAX_LIST:
            self.list.append(value)
            self.search.append(search_str(value))

    def insert(self, key, value):
        """Insert up to 200,000 items in list"""
        if len(self.list) < config.MAX_LIST:
            if key == "first":
                self.list.insert(0, value)
                self.search.insert(0, search_str(value))
            elif key == "last":
                self.list.append(value)
                self.search.append(search_str(value))
            elif key == "random":
                key = random.randint(0, len(self.list))
                self.list.insert(key, value)
                self.search.insert(key, search_str(value))
            else:
                key = round(tonum(key)) - 1
                if 0 <= key <= len(self.list):
                    self.list.insert(key, value)
                    self.search.insert(key, search_str(value))

    def delete(self, key):
        """Remove an item from list"""
        if key == "all":
            self.list = []
            self.search = []
        elif self.list:
            if key == "first":
                del self.list[0]
                del self.search[0]
            elif key == "last":
                del self.list[-1]
                del self.search[-1]
            elif key == "random":
                key = random.randint(0, len(self.list) - 1)
                del self.list[key]
                del self.search[key]
            else:
                key = round(tonum(key)) - 1
                if 0 <= key < len(self.list):
                    del self.list[key]
                    del self.search[key]

    def delete_all(self):
        """Delete all items in list"""
        self.list = []
        self.search = []

    def __contains__(self, item):
        return search_str(item) in self.search

    def index(self, item):
        """Find the index of an item, case insensitive"""
        try:
            return self.search.index(search_str(item)) + 1
        except ValueError:
            return 0


class BaseList:
    """
    Emulates the correct list behavior
    """

    __slots__ = ('list',)

    def __init__(self, values):
        self.list = values

    def __getitem__(self, key):
        key -= 1
        if 0 <= key < len(self.list):
            return self.list[key]
        return ""

    def get(self, key):
        """Gets an item, supporting legacy indices (first, last, random)"""
        if key == 'first':
            return self.list[0]
        if key == 'last':
            return self.list[-1]
        if key == 'random':
            return random.choice(self.list)
        return self.__getitem__(toint(key))

    def __setitem__(self, key, value):
        key -= 1
        if 0 <= key < len(self.list):
            self.list[key] = value

    def set(self, key, item):
        """Sets an item, supporting legacy indices (first, last, random)"""
        if key == 'first':
            self.__setitem__(1, item)
        elif key == 'last':
            self.__setitem__(len(self.list), item)
        elif key == 'random':
            self.__setitem__(random.randint(1, len(self.list)), item)
        else:
            self.__setitem__(toint(key), item)

    def append(self, value):
        """Add an item to list"""
        self.list.append(value)

    def insert(self, key, value):
        """Insert an item in list"""
        key -= 1
        if 0 <= key <= len(self.list):
            self.list.insert(key, value)

    def insert2(self, key, item):
        """Inserts an item, supporting legacy indices (first, last random)"""
        if key == 'first':
            self.insert(1, item)
        elif key == 'last':
            self.append(item)
        elif key == 'random':
            self.insert(random.randint(1, len(self.list)), item)
        else:
            self.insert(toint(key), item)

    def delete(self, key):
        """Remove an item from list"""
        key -= 1
        if 0 <= key < len(self.list):
            del self.list[key]

    def delete2(self, key):
        """Deletes an item, supporting legacy indices (first, last, random, all)"""
        if key == 'all':
            self.delete_all()
        elif key == 'first':
            self.delete(1)
        elif key == 'last':
            self.delete(len(self.list))
        elif key == 'random':
            self.delete(random.randint(1, len(self.list)))
        else:
            self.delete(toint(key))

    def delete_all(self):
        """Deletes all items in list"""
        self.list = []

    def __contains__(self, item):
        item = search_str(item)
        return any(item == search_str(value) for value in self.list)

    def join(self):
        """Joins the list"""
        if all(len(search_str(item)) == 1 for item in self.list):
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
        """Gets the position of item in list"""
        item = search_str(item)
        for i, value in enumerate(self.list):
            if item == search_str(value):
                return i + 1
        return 0

    def copy(self):
        """Return a copy of this List"""
        return self.__class__(self.list.copy())


class StaticList(BaseList):
    """
    A list that doesn't change
    """

    __slots__ = ('dict',)

    def __init__(self, values):  # pylint: disable=super-init-not-called
        self.list = tuple(values)

        self.dict = {}
        for i, item in enumerate(values):
            self.dict.setdefault(search_str(item), i+1)

    def index(self, item):
        """Gets the position of item in list"""
        return self.dict.get(search_str(item), 0)

    def __contains__(self, item):
        return search_str(item) in self.dict

    def copy(self):
        """Returns self; this list is static"""
        return self


def search_str(value):
    """
    Gets a lowercase str for searching
    Also handles integer floats.
    """
    if isinstance(value, float) and value.is_integer():
        return str(int(value))
    return str(value).lower()
