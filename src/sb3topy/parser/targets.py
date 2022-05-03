"""
targets.py

Handles targets

TODO Consider adding a cache to get_parent_hat
"""

import logging
from typing import Dict

from . import naming, specmap
from .prototypes import Prototypes
from .typing import DiGraph
from .variables import Variables

logger = logging.getLogger(__name__)


class Targets:
    """
    Represents all targets in the json

    names - The Sprites instance handling naming
    targets - The dict linking target names to Target instances
    """

    def __init__(self):
        self.names = naming.Sprites()
        self.targets: Dict[str, Target] = {}
        self.digraph = DiGraph()

    def add_targets(self, targets):
        """Creates and adds each target to the internal dict"""
        Target.digraph = self.digraph

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

    Class Attributes:
        broadcasts: A dict used to keep track of which broadcasts only
            have a single "when I recieve" hat. If a value of the dict
            is None, there are mulitple recievers. Otherwise, the value
            is an unclean target name. {broadcast: target_name | None}

        digraph: The DiGraph instance used by the parser to handle
            typing.
        TODO Some things are in here just to pass them to the specmap

        cloned_targets: A set of clones which are likely to have clones
            made of them.

    Attributes:
        target: The sb3 target dict

        blocks:  The sb3 blocks list of this target

        hats: A list of hat blocks contained by this target

        clean_name: The safe and unique identifier name

        vars: The Variables instance used to name for this target's
            variables

        events: The Events instance used to name for this target's hats

        prototypes: The Prototypes instance used to handle this target's
            prototypes

        prototype: The prototype currently being used by the parser
    """

    digraph: DiGraph
    broadcasts = {}
    cloned_targets = set()

    def __init__(self, target, name):
        self.target = target
        self.clean_name = name
        self.blocks: Dict[str, dict] = target['blocks']
        self.hats = []

        self.vars = Variables(name, target['isStage'])

        self.events = naming.Events()
        self.prototypes = Prototypes(self.events)

        self.prototype = None

    def first_pass(self):
        """
        Run the first pass on the target:
            - Removes unused variable reporters
            - Creates a list of hat blocks
            - Keeps track of broadcast recievers
            - Initializes all Prototypes
            - Marks universal variables used in sensing_of
        """

        logger.debug("Running first pass on target '%s'", self.target['name'])

        # Loop through each block
        for blockid, block in self.blocks.items():
            # Skip variables not in a block
            if not isinstance(block, dict):
                continue

            # Each hat needs to be parsed
            if specmap.is_hat(block):
                self.hats.append((blockid, block))

                # Count the number of broadcast recievers
                if block['opcode'] == 'event_whenbroadcastreceived':
                    self.add_broadcast(
                        block['fields']['BROADCAST_OPTION'][0].lower())

            # Save when targets are cloned
            if block['opcode'] == 'control_create_clone_of':
                self.cloned_targets.add(specmap.get_clone(block, self))

            # Create a prototype with the block
            elif block['opcode'] == 'procedures_prototype':
                self.prototypes.add_prototype(self, block['mutation'], blockid)

            # Note the variable as a universal
            elif block['opcode'] == 'sensing_of':
                self.vars.mark_universal(block['fields']['PROPERTY'][0])

    def second_pass(self):
        """
        Runs the second pass on the target:
            - Creates and names Variables
            - Guesses the type of each variable
        """

        logger.debug("Running second pass on target '%s'",
                      self.target['name'])

        # Gets names for all variables
        self.vars.second_pass(self.target, self.digraph)

        for block in self.blocks.values():
            # Skip variables not in a block
            if not isinstance(block, dict):
                continue

            opcode = block['opcode']

            # Type guess with the argument values
            if block['opcode'] == 'procedures_call':
                self.prototypes.mark_called(self, block)

            # Type guess hint with the value being set
            if opcode == 'data_setvariableto':
                self.vars.mark_set(self, block)

            # Type guess hint that the variable is a number
            elif opcode == 'data_changevariableby':
                self.vars.mark_changed(block)

            # Note blocks which modify the list
            elif opcode in ('data_addtolist', 'data_deleteoflist',
                            'data_deletealloflist', 'data_insertatlist',
                            'data_replaceitemoflist'):
                self.vars.mark_modified(self, block)

            # Note usages which may benefit from a dict
            elif opcode in ('data_itemnumoflist', 'data_listcontainsitem'):
                self.vars.mark_indexed(block)

    def get(self, key, default=None):
        """Gets an item from the internal dict"""
        return self.target.get(key, default)

    def __getitem__(self, key):
        return self.target[key]

    def add_broadcast(self, broadcast):
        """Keeps track of which broadcasts only have a single reciever"""
        if broadcast in self.broadcasts:
            self.broadcasts[broadcast] = None
        else:
            self.broadcasts[broadcast] = self.target['name']

    def get_parent_hat(self, block: dict):
        """
        Returns the hat block the passed block is a child of or None if
        the block is part of a stack without a hat.
        """
        while block:
            if specmap.is_hat(block):
                break
            block = self.blocks.get(block['parent'])

        return block
