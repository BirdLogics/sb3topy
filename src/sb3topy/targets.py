"""
targets.py

Handles targets

"""

from . import naming


class Targets:
    """Represents all targets in the json"""

    def __init__(self):
        self.names = naming.Sprites()
        self.targets = {}

    def add_target(self, target):
        """Adds a target from a target dict"""
        name = self.names.create_identifier(target['name'])
        target = Target(target, name)

        self.targets[target['name']] = target
        return target

    def name_items(self):
        """Returns name items (original, cleaned)"""
        return self.names.sprites.dict.items()

    def get(self, key, default=None):
        """Gets an item from the internal dict"""
        return self.targets.get(key, default)

    def __getitem__(self, key):
        return self.targets[key]

    def __iter__(self):
        return iter(self.targets.values())


class Target:
    """Represents a target"""

    def __init__(self, target, name):
        self.target = target
        self.clean_name = name

        self.vars = naming.Variables(target['isStage'])
        self.events = naming.Events()
        self.prototypes = naming.Prototypes(self.events)
        self.blocks = target['blocks']

    def get(self, key, default=None):
        """Gets an item from the internal dict"""
        return self.target.get(key, default)

    def __getitem__(self, key):
        return self.target[key]
