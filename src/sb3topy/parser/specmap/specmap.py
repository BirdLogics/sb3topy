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
from . import type_switches


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
            logging.warning("Unknown block with opcode '%s'", block['opcode'])
            blockmap = BLOCKS['default']

    return BlockMap(*blockmap)


def get_literal_type(value):
    """Attempts to determine the type of a literal value"""

    if str(value).isdigit() and len(str(value)) < config.SIG_DIGITS:
        return 'int'
    if str(sanitizer.cast_number(value)) == str(value) and \
            len(str(value).partition('.')[2]) < config.SIG_DIGITS:
        return 'float'
    if str(value) == "":
        return 'int'
    return 'str'


def get_input_type(target, value):
    """Parses a block input to determine the type"""
    # 1 Wrapped value
    if value[0] == 1 and isinstance(value[1], list):
        value = value[1]

    # Handle a block input
    # 1 wrapper with block, 2 block, 3 block over value
    if value[0] in (1, 2, 3):
        value = value[1]

        # Empty block
        if value is None:
            return 'none'

        # Verify not a variable
        if isinstance(value, str):
            block = target.blocks[value]
            # Shadow block (dropdown)
            if block['shadow']:
                # Return the value of the field
                return 'literal', value[0]

            # Just a block
            return get_block_type(target, block)

    # 4-8 Number, 9-10 String, # 11 Broadcast
    if 4 <= value[0] <= 10:
        return get_literal_type(value[1])

    # 12 Variable
    if value[0] == 12:
        var = target.vars.get_var('var', value[1])
        return target.digraph.get_node(var.node.id_tuple)

    # 13 List reporter
    if value[0] == 13:
        # TODO StaticList reporter typing?
        return 'str'

    return 'any'


def get_block_type(target, block):
    """Gets the return type of a block"""
    type_ = None

    # Attempt to get the type from a switch
    switchf = type_switches.SWITCHES.get(block['opcode'])
    if switchf is not None:
        type_ = switchf(target, block)

    # Default to the blockmap's return_type
    if type_ is None:
        blockmap = BLOCKS.get(block['opcode'])
        if blockmap is not None:
            type_ = blockmap.return_type

    if type_ is not None:
        return type_

    # Missing blockmap or something, give a warning
    logging.warning("Unknown type for block '%s'", block['opcode'])
    return "any"


def parse_input(blocks, value):
    """
    Parses an input value and returns (type, value).

    The returned type determines what value is:
        'literal': A literal value which needs to be sanitized
        'blockid': A blockid which needs to be parsed
        'variable': An unparsed variable reporter
        'list_reporter': An unparsed list reporter
        'none': The literal None
    """

    # Handle a wrapped value
    if value[0] == 1 and isinstance(value[1], list):
        value = value[1]

    # Handle a block input
    # 1 wrapper with block, 2 block, 3 block over value
    if value[0] in (1, 2, 3):
        value = value[1]

        # Empty block
        if value is None:
            return 'none', None

        # Verify not a variable
        if isinstance(value, str):
            # Shadow block (dropdown)
            if blocks[value]['shadow']:
                # Get the only field from the dropdown menu
                value = next(iter(blocks[value]['fields'].values()))

                # Return the value of the field
                return 'literal', value[0]

            # Just a block
            return 'blockid', value

    # 12 Variable
    if value[0] == 12:
        return 'variable', value[1]

    # 13 List
    if value[0] == 13:
        return 'list_reporter', value[1]

    # Default to a literal
    # 4-8 Number, 9-10 String, # 11 Broadcast
    if not 4 <= value[0] <= 11:
        logging.error("Unexpected input type %i", value[0])

    return 'literal', value[1]


def get_broadcast(block, target):
    """
    Parses a event_broadcast(andwait) block to get the name of the
    sent broadcast. Returns the lowered broadcast name unless a block
    is in the input.
    """

    type_, value = parse_input(
        target.blocks, block['inputs']['BROADCAST_INPUT'])

    if type_ == 'literal':
        return value.lower()
    return None


def get_clone(block, target):
    """
    Parses a control_create_clone_of block to get the name of the
    target which is cloned. Returns the uncleaned target name unless
    a block is in the input.
    """

    type_, value = parse_input(target.blocks, block['inputs']['CLONE_OPTION'])

    if type_ == 'literal':
        if value == '_myself_':
            return target['name']

        return value

    return None
