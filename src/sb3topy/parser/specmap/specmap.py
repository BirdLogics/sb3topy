"""
specmap.py

Contains functions used to read specmap data
"""


import logging
import textwrap
from collections import namedtuple

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
            logging.error("Unkown block with opcode '%s'", block['opcode'])
            blockmap = BLOCKS['default']

    return BlockMap(*blockmap)
