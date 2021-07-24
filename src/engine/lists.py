"""
lists.py

Handles data structures related to lists
"""

import random

from . import config
from .blockutil import tonum

__all__ = ['List']


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
            # Get a lowercase str for searching
            if isinstance(value, float) and value.is_integer():
                value = int(value)
            search = str(value).lower()

            if key == "first":
                self.list[0] = value
                self.search[0] = search
            elif key == "last":
                self.list[-1] = value
                self.search[-1] = value
            elif key == "random":
                key = random.randint(0, len(self.list) - 1)
                self.list[key] = value
                self.search[key] = value
            else:
                key = round(tonum(key)) - 1
                if 0 <= key < len(self.list):
                    self.list[key] = value
                    self.search[key] = search

    def append(self, value):
        """Add up to 200,000 items to list"""
        if len(self.list) < config.MAX_LIST:
            self.list.append(value)

            # Save a lowercase str for searching
            if isinstance(value, float) and value.is_integer():
                value = int(value)
            self.search.append(str(value).lower())

    def insert(self, key, value):
        """Insert up to 200,000 items in list"""
        # Get a lowercase str for searching
        if isinstance(value, float) and value.is_integer():
            value = int(value)
        search = str(value).lower()

        if len(self.list) < config.MAX_LIST:
            if key == "first":
                self.list.insert(0, value)
                self.search.insert(0, search)
            elif key == "last":
                self.list.append(value)
                self.search.append(search)
            elif key == "random":
                key = random.randint(0, len(self.list))
                self.list.insert(key, value)
                self.search.insert(key, search)
            else:
                key = round(tonum(key)) - 1
                if 0 <= key <= len(self.list):
                    self.list.insert(key, value)
                    self.search.insert(key, value)

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
        if isinstance(item, float) and item.is_integer():
            item = int(item)
        return str(item).lower() in self.search

    def __str__(self):
        char_join = True
        for item in self.list:
            if len(str(item)) != 1:
                char_join = False
                break
        if char_join:
            return ''.join(self.list)
        return ' '.join(self.list)

    def __call__(self):
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
        if isinstance(item, float) and item.is_integer():
            item = int(item)
        item = str(item).lower()

        try:
            return self.search.index(item) + 1
        except ValueError:
            return 0

    def copy(self):
        """Return a copy of this List"""
        return List(self.list.copy())
