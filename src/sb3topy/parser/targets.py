"""
targets.py

Handles targets

"""

import logging

from .. import config
from . import naming, specmap
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

    def add_targets(self, targets):
        """Creates and adds each target to the internal dict"""
        # Add every target to the internal dict
        for target in targets:
            self.targets[target['name']] = Target(
                target,
                self.names.create_identifier(target['name'])
            )

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
    hats - A list of hat blocks contained by this target

    clean_name - The safe and unique identifier name

    vars - The Variables instance handling naming for this target's variables
    events - The Events instance handling naming for this target's hats
    prototypes - The Prototypes instance handling this target's prototypes

    prototype - The prototype currently being used by the parser
    """

    def __init__(self, target, name):
        self.target = target
        self.blocks = target['blocks']
        self.hats = []

        self.clean_name = name

        self.vars = Variables(target['isStage'])
        self.events = naming.Events()
        self.prototypes = naming.Prototypes(self.events)

        self.prototype = None

    def first_pass(self):
        """
        Run the first pass on the target:
            - Removes unused variable reporters
            - Creates a list of hat blocks
            - Initializes all Prototypes
            - Marks universal variables used in sensing_of
        """

        logging.debug("Running first pass on target '%s'", self.target['name'])

        # Loop through each block
        for blockid, block in self.blocks.items():
            # Skip variables not in a block
            if not isinstance(block, dict):
                continue

            # Each hat needs to be parsed
            if specmap.is_hat(block):
                self.hats.append((blockid, block))

            # Create a prototype with the block
            elif block['opcode'] == 'procedures_prototype':
                self.prototypes.add_prototype(block['mutation'], blockid)

            # Note the variable as a universal
            elif block['opcode'] == 'sensing_of':
                self.vars.mark_universal(block['fields']['PROPERTY'][0])

    def second_pass(self):
        """
        Runs the second pass on the target:
            - Creates and names Variables
            - Guesses the type of each variable
        """

        logging.debug("Running second pass on target '%s'",
                      self.target['name'])

        # Gets names for all variables
        self.vars.second_pass(self)

        for block in self.blocks.values():
            # Skip variables not in a block
            if not isinstance(block, dict):
                continue

            opcode = block['opcode']

            # Type guess with the argument values
            if block['opcode'] == 'procedures_call':
                self.prototypes.mark_called(block)

            # Type guess hint with the value being set
            if opcode == 'data_setvariableto':
                self.vars.mark_set(self, block)

            # Type guess hint that the variable is a number
            elif opcode == 'data_changevariableby':
                self.vars.mark_changed(self, block)

            # Note blocks which modify the list
            elif opcode in ('data_addtolist', 'data_deleteoflist',
                            'data_deletealloflist', 'data_insertatlist',
                            'data_replaceitemoflist'):
                self.vars.mark_modified(block)

            # Note usages which may benefit from a dict
            elif opcode in ('data_itemnumoflist', 'data_listcontainsitem'):
                self.vars.mark_indexed(block)

        # Guess the type of each variable
        if config.VAR_TYPES:
            self.vars.guess_types()

        # Guess the type of each prototype arg
        if config.ARG_TYPES:
            self.prototypes.guess_types()

    def get(self, key, default=None):
        """Gets an item from the internal dict"""
        return self.target.get(key, default)

    def __getitem__(self, key):
        return self.target[key]
