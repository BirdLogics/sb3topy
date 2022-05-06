"""
typing.py

Contains functions used to determine the type of literals, the return
type of blocks, and the type of input.

TODO Switches for arithmetic operators
TODO Proper type detection
"""

import logging
from typing import Any, Callable, Dict

from ... import config
from .. import sanitizer
from . import data

__all__ = ["get_literal_type", "get_input_type", "get_block_type"]

logger = logging.getLogger(__name__)


SWITCHES: Dict[str, Callable[[Any, Any], Any]] = {}


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

    # Step 1, get the base blockmap.
    blockmap = data.BLOCKS.get(block['opcode'])
    if blockmap is not None:
        # Step 2, apply any basic switches.
        if blockmap.switch:
            # Format the switch using the fields
            opcode = blockmap.format_switch(block)
            blockmap = data.BLOCKS.get(opcode, blockmap)

        # Save the return type
        type_ = blockmap.return_type

    # TODO Step 3, apply mutations / type switches?

    # Return the result
    if type_ is not None:
        return type_

    # Missing blockmap or something, give a warning
    logger.warning("Unknown type for block '%s'", block['opcode'])
    return "any"


def switch(opcode):
    """Adds a funtion to the SWITCHES dict"""
    def wrapper(func):
        SWITCHES[opcode] = func
        return func
    return wrapper


@switch("argument_reporter_string_number")
def arg_reporter(target, block):
    """Determines the type of a argument reporter"""
    return target.prototypes.get_arg_node(target, block)


@switch("data_itemoflist")
def list_item(target, block):
    """Determines the type of a list item reporter"""
    name = block['fields']['LIST'][0]
    return target.vars.get_var('list', name).node
