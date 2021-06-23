"""
variables.py

Handles variable naming.

TODO Variable type optimizations
"""

import logging

from .naming import Identifiers
from . import sanitizer


class Variables:
    """
    Handles variable and list naming for a target

    local_vars - Contains variables used by a single sprite

    global_vars - Contains variables owned by the stage
    universal_vars - Contains variable names which should be kept
        consistent across sprites since they are used in sensing_of

    Universal variable names must be marked before adding variables.

    """
    global_vars: Identifiers = None
    universal_vars: Identifiers = None

    def __init__(self, target, is_stage=False):
        # Initialize class attributes
        if self.global_vars is None:
            Variables.global_vars = Identifiers()
            Variables.universal_vars = Identifiers()

        if is_stage:
            self.local_vars = self.global_vars
        else:
            self.local_vars = Identifiers()

        logging.debug("Variable preparse for target '%s'", target['name'])

        # Save variable names used in sensing_of
        for block in target['blocks'].values():
            # Skip unused variable reporters
            if not isinstance(block, dict):
                continue

            # Variables used in sensing_of should have
            # a consistent clean name across sprites
            if block['opcode'] == 'sensing_of':
                name = block['fields']['PROPERTY'][0]
                self.mark_universal('var', name)

    def get_reference(self, prefix, name):
        """
        Gets a variable reference,
        eg. self.var_x or util.sprites.stage.var_x
        """
        # Ensure the name starts with the prefix
        if not name.startswith(prefix):
            name = prefix + '_' + name

        # Check if a local variable exists with the name
        if name in self.local_vars.dict:
            return "self." + self.local_vars.dict[name]

        # Check if a global variable exists with the name
        if name in self.global_vars.dict:
            return "util.sprites.stage." + self.global_vars.dict[name]

        # This should not occur, but can be handled
        logging.warning("Unregistered var '%s'", name)

        # Create a new local variable
        return "self." + self.create_local('', name)

    def get_local(self, prefix, name):
        """
        Gets the identifier for a local variable
        No self. prefix is added.
        """
        # Ensure the name starts with the prefix
        if not name.startswith(prefix):
            name = prefix + '_' + name

        # Check if a local variable exists with the name
        if name in self.local_vars.dict:
            return self.local_vars.dict[name]

        # This should not normally occur, but can be handled
        logging.warning("Unregistered local var '%s'", name)

        # Create a new local variable
        return self.create_local('', name)

    def create_local(self, prefix, name):
        """Creates a safe identifier name"""
        # Ensure the name starts with the prefix
        if not name.startswith(prefix):
            name = prefix + '_' + name

        # Verify the variable doesn't already exist
        if name in self.local_vars.dict:
            logging.warning("Duplicate local var '%s'", name)
            return self.local_vars.dict[name]

        # Check if a universal identifier is assigned to name
        if name in self.universal_vars.dict:
            return self.universal_vars.dict[name]

        # Remove invalid characters
        ident = sanitizer.clean_identifier(name)

        # Ensure the identifier is unique
        ident = self.local_vars.suffix(ident)

        # Save the identifier for future use
        self.local_vars.dict[name] = ident

        logging.debug("Creating local var '%s' as '%s'", name, ident)

        return ident

    @classmethod
    def mark_universal(cls, prefix, name):
        """Saves a name as a universal identifier"""
        # Ensure the name starts with the prefix
        if not name.startswith(prefix):
            name = prefix + '_' + name

        # Verify the name isn't already marked
        if name in cls.universal_vars.dict:
            return cls.universal_vars.dict[name]

        # Remove invalid characters
        ident = sanitizer.clean_identifier(name)

        # Ensure the identifier is unique
        ident = cls.universal_vars.suffix(ident)

        # Save the identifier for future use
        cls.universal_vars.dict[name] = ident

        logging.debug("Creating universal var '%s' as '%s'", name, ident)

        return ident

    @classmethod
    def get_universal(cls, prefix, name):
        """Gets a universal identifier from a name"""
        # Ensure the name starts with the prefix
        if not name.startswith(prefix):
            name = prefix + '_' + name

        # Get the universal identifier
        ident = cls.universal_vars.dict.get(name)

        if ident is None:
            logging.error("Unmarked universal var '%s'", name)
            ident = cls.mark_universal(prefix, name)

        return ident

    def parse(self, target):
        """
        Parses the variables in a target

        Should not be called until a Variables
        instance has been created for every target
        """

        # Update universal names
        self.local_vars.set.update(self.universal_vars.set)

        # Read variables
        for name, _ in target['variables'].values():
            self.create_local("var", name)

        # Read lists
        for name, _ in target['lists'].values():
            self.create_local('list', name)

#         # Assign types to each variable
#         self.guess_types(target.blocks)

#     def guess_types(self, blocks):
#         """Attempts to assign variable types"""
#         for block in blocks:
#             if block['opcode'] == 'data_setvariableto':
#                 pass


# def get_type(value):
#     """Attempts to determine the type of a value"""
#     if sanitizer.cast_number(value) is not None:
#         return float
#     if str(value).lower() in ('true', 'false'):
#         return bool
#     if str(value) == "":
#         return None
#     return str
