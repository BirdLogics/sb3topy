"""
specmap.py

Contains functions used to read specmap data

TODO Proper type detection
"""


import logging
import textwrap

from ... import config
from .. import sanitizer
from .block_data import BLOCKS, HATS, LOOPS, Block
from .switch_data import SWITCHES


class BlockMap(Block):
    """A named tuple with a format function"""

    def format(self, kwargs):
        """Formats the blockmap code and handles indentation"""
        args = {}
        for key in self.args:
            # Get the argument from kwargs
            arg = kwargs[key]
            assert isinstance(arg, str), "Improperly parsed block arg"

            # Indent it if necesary
            indent = self.indents.get(key)
            if indent:
                arg = textwrap.indent(arg, indent)

            # Save the parsed argument
            args[key] = arg

        return self.code.format(**args)


def is_hat(block):
    """Determines if an opcode belongs a hat block"""
    return block['opcode'] in HATS


def is_procedure(block):
    """Determines if the opcode is 'procedures_definition'"""
    return block['opcode'] == 'procedures_definition'


def is_loop(block):
    """
    Determines if an opcode belongs to a loop block

    A yield needs to be added to the end of loops' code
    """
    return block['opcode'] in LOOPS


def get_blockmap(block, target):
    """Gets the blockmap for a block"""
    blockmap = None

    # Attempt to get the blockmap from a switch
    switch = SWITCHES.get(block['opcode'])
    if switch is not None:
        blockmap = switch(block, target)

    # Default to BLOCKS[opcode]
    if blockmap is None:
        blockmap = BLOCKS.get(block['opcode'])

        # Report an error and return a fallback
        if blockmap is None:
            logging.warning("Unkown block with opcode '%s'", block['opcode'])
            blockmap = BLOCKS['default']

    return BlockMap(*blockmap)


def get_literal_type(value):
    """Attempts to determine the type of a literal value"""

    if str(value).isdigit() and len(str(value)) < config.SIG_DIGITS:
        return 'int'
    if str(sanitizer.cast_number(value)) == str(value) and \
            len(str(value).partition('.')[2]) < config.SIG_DIGITS:
        return 'float'
    if str(value).lower() in ('true', 'false'):
        return 'bool'
    # if str(value) == "":
    #     return None
    return 'str'


def get_input_type(target, value):
    """Parses a block input to determine the type"""
    # TODO Specmap type_switches.py
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
        return get_literal_type(value[1])

    # 12 Variable
    if value[0] == 12:
        var = target.variables.get_var('var', value[1])
        return ('var', var.target_name, value[1])

    # 13 List reporter
    if value[0] == 13:
        # TODO List reporter typing
        return 'str'

    return 'any'
