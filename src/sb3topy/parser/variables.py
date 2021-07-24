"""
variables.py

Handles variable naming.

TODO Variable type optimizations
TODO Names such as 'x position' are marked as universals
"""

import logging

from .. import config
from . import sanitizer
from .naming import Identifiers


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

    def __init__(self, is_stage):
        # Initialize class attributes
        if self.global_vars is None:
            Variables.global_vars = Identifiers()
            Variables.universal_vars = Identifiers()

        if is_stage:
            self.local_vars = self.global_vars
        else:
            self.local_vars = Identifiers()

    def second_pass(self, target):
        """
        Parses the variables in a target

        Should not be called until a Variables
        instance has been created for every target
        """

        # Update universal names
        self.local_vars.set.update(self.universal_vars.set)

        # Read variables
        for name, value in target['variables'].values():
            self.create_local("var", name, value)

        # Read lists
        for name, _ in target['lists'].values():
            self.create_local('list', name)

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
            return "self." + self.local_vars.dict[name].clean_name

        # Check if a global variable exists with the name
        if name in self.global_vars.dict:
            return "util.sprites.stage." + self.global_vars.dict[name].clean_name

        # This should not occur, but can be handled
        logging.warning("Unregistered var '%s'", name)

        # Create a new local variable
        return "self." + self.create_local('', name).clean_name

    def get_type(self, prefix, name):
        """
        Gets the type for a global or local variable
        """
        # Ensure the name starts with the prefix
        if not name.startswith(prefix):
            name = prefix + '_' + name

        # Check if a local variable exists with the name
        if name in self.local_vars.dict:
            return self.local_vars.dict[name].guessed_type

        # Check if a global variable exists with the name
        if name in self.global_vars.dict:
            return self.global_vars.dict[name].guessed_type

        # This should not occur, but can be handled
        logging.warning("Unregistered var '%s'", name)

        # Create a new local variable
        return self.create_local('', name).guessed_type

    def get_local(self, prefix, name) -> str:
        """
        Gets the identifier for a local variable
        No self. prefix is added.
        """
        # Ensure the name starts with the prefix
        if not name.startswith(prefix):
            name = prefix + '_' + name

        # Check if a local variable exists with the name
        if name in self.local_vars.dict:
            return self.local_vars.dict[name].clean_name

        # This should not normally occur, but can be handled
        logging.warning("Unregistered local var '%s'", name)

        # Create a new local variable
        return self.create_local(prefix, name).clean_name

    def get_var(self, prefix, name):
        """
        Gets a Variable object, either global or local
        """
        # Ensure the name starts with the prefix
        if not name.startswith(prefix):
            name = prefix + '_' + name

        # Check if a local variable exists with the name
        if name in self.local_vars.dict:
            return self.local_vars.dict[name]

        # Check if a global variable exists with the name
        if name in self.global_vars.dict:
            return self.global_vars.dict[name]

        # This should not normally occur, but can be handled
        logging.warning("Unregistered var '%s'", name)

        # Create a new local variable
        return self.create_local(prefix, name)

    def create_local(self, prefix, name, value=None):
        """Creates a safe identifier name"""
        # Ensure the name starts with the prefix
        if not name.startswith(prefix):
            name = prefix + '_' + name

        # Check if a universal identifier already exists
        if name in self.universal_vars.dict:
            # Get the universal identifier
            ident = self.universal_vars.dict[name]

            # Save the identifier
            self.local_vars.dict[name] = Variable(ident, value)

            logging.debug(
                "Creating local var '%s' as universal '%s'", name, ident)

            return self.local_vars.dict[name]

        # Verify the variable doesn't already exist
        if name in self.local_vars.dict:
            logging.warning("Duplicate local var '%s'", name)
            return self.local_vars.dict[name]

        # Remove invalid characters
        ident = sanitizer.clean_identifier(name)

        # Ensure the identifier is unique
        ident = self.local_vars.suffix(ident)

        # Save the identifier for future use
        self.local_vars.dict[name] = Variable(ident, value)

        logging.debug("Creating local var '%s' as '%s'", name, ident)

        return self.local_vars.dict[name]

    @classmethod
    def mark_universal(cls, name):
        """Saves a name as a universal identifier"""
        # Ensure the name starts with the prefix
        if not name.startswith('var'):
            name = 'var' + '_' + name

        # Verify the name isn't already marked
        if name in cls.universal_vars.dict:
            return cls.universal_vars.dict[name]

        # Remove invalid characters
        ident = sanitizer.clean_identifier(name)

        # Ensure the identifier is unique
        ident = cls.universal_vars.suffix(ident)

        # Save the identifier for future use
        cls.universal_vars.dict[name] = ident

        logging.debug("Created universal var '%s' as '%s'", name, ident)

        return ident

    @classmethod
    def get_universal(cls, name):
        """Gets a universal identifier from a name"""
        # Ensure the name starts with the prefix
        if not name.startswith('var'):
            name = 'var_' + name

        # Get the universal identifier
        ident = cls.universal_vars.dict.get(name)

        if ident is None:
            logging.error("Unmarked universal var '%s'", name)
            ident = cls.mark_universal(name)

        return ident

    def mark_set(self, block):
        """Parses a data_setvariableto block for type guessing"""
        if config.VAR_TYPES:
            self.get_var('var', block['fields']['VARIABLE'][0]).mark_set(
                block['inputs']['VALUE'])

    def mark_changed(self, block):
        """Parses a data_changevariableby block for type guessing """
        if config.VAR_TYPES:
            self.get_var('var', block['fields']['VARIABLE'][0]).mark_changed()

    def guess_types(self):
        """Guesses the type of all variables"""
        for variable in self.local_vars.dict.values():
            variable.guess_type()


# TODO Proper type detection
def get_type(value):
    """Attempts to determine the type of a value"""

    if str(value).isdigit() and len(str(value)) < config.SIG_DIGITS:
        return 'int'
    if str(sanitizer.cast_number(value)) == str(value) and \
            len(str(value).partition('.')[2]) < config.SIG_DIGITS:
        return 'float'
    if str(value).lower() in ('true', 'false'):
        return 'bool'
    if str(value) == "":
        return None
    return 'str'


class Variable:
    """Represents a variable"""

    def __init__(self, clean_name, initial_value):
        self.clean_name = clean_name
        self.initial_value = initial_value
        self.is_changed = False
        self.set_types = set()
        self.set_values = set()
        self.guessed_type = 'any'

    def mark_set(self, value):
        """Saves the type of the variable"""
        # TODO Block detection

        # Handle possible block input
        if value[0] == 1:
            if isinstance(value[1], list):
                # Wrapped value
                value = value[1]
            else:
                # Wrapped block
                value = [2, value[1]]
        elif value[0] == 3:
            # Block covering value
            value = [2, value[1]]

        # 4-8 Number, 9-10 String, # 11 Broadcast
        if 4 <= value[0] <= 10:
            self.set_types.add(get_type(value[1]))
            self.set_values.add(value[1])

    def mark_changed(self):
        """Saves that the variable is modified by a change by block"""
        self.is_changed = True

    def guess_type(self):
        """Guesses the type"""
        if get_type(self.initial_value) == 'float' and (
                self.is_changed or 'str' not in self.set_types and
                'bool' not in self.set_types):
            self.guessed_type = 'float'
        else:
            self.guessed_type = 'any'

        logging.debug("Guessing variable '%s' as type %s",
                      self.clean_name, self.guessed_type)
