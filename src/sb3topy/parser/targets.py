"""
targets.py

Handles targets

"""

from . import naming
from .variables import Variables


class Targets:
    """
    Represents all targets in the json

    names - The Sprites instance handling naming
    targets - The dict linking target names to Target instances
    """

    def __init__(self):
        self.names = naming.Sprites()
        self.targets: dict[str, Target] = {}

    def add_target(self, target):
        """Adds a target from a target dict"""
        name = self.names.create_identifier(target['name'])
        target = Target(target, name)

        self.targets[target['name']] = target
        return target

    def parse_variables(self):
        """Preparses variables for each target"""
        for target in self.targets.values():
            target.vars.parse(target)

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
    """
    Represents a target

    target - The sb3 target dict
    blocks - The sb3 blocks list of this target

    clean_name - The safe and unique identifier name

    vars - The Variables instance handling naming for this target's variables
    events - The Events instance handling naming for this target's hats
    prototypes - The Prototypes instance handling this target's prototypes

    prototype - The prototype currently being used by the parser
    """

    def __init__(self, target, name):
        self.target = target
        self.blocks = target['blocks']

        self.clean_name = name

        self.vars = Variables(target, target['isStage'])
        self.events = naming.Events()
        self.prototypes = naming.Prototypes(self.events)

        self.prototype = None

    def set_prototype(self, custom_block):
        """
        Selects a prototype from the internal Prototypes instance

        custom_block is the blockid of the prototype
        """
        self.prototype = self.prototypes.get_definition(custom_block)

    def get(self, key, default=None):
        """Gets an item from the internal dict"""
        return self.target.get(key, default)

    def __getitem__(self, key):
        return self.target[key]
