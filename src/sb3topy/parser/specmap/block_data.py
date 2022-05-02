"""
block_data.py

Contains the base block data for most blocks. Used as a fallback if a
type switch is not found for a given opcode.

Globals:
    Block: Used to store the base data for a block. Contains a return
        type for the blok, a list of arg (type, name) tuples, the
        unformatted code, and indents for each {} format tag.

    BLOCKS: A dictionary with the base Block data for most opcodes.

    HATS: A set containing opcodes which should be treated as hats.

    LOOPS: A set containing opcodes which should be treated as loops.
        Loop blocks should yield at the end, but the yield can be
        omitted in warped blocks as an optimization.

TODO Validate block_data.json to prevent obscure errors
"""

import json
import logging
import re
import textwrap
from collections import namedtuple
from os import path
from typing import Dict

from . import block_switches

__all__ = ["get_blockmap"]

INDENT_PAT = r"(?m)^(\s+)\{(\w+)\}"

Block = namedtuple('Block', ['return_type', 'args',
                             'code', 'indents', 'switch', 'basename'])


class BlockMap(Block):
    """A named tuple with a format function"""

    def format(self, kwargs):
        """Formats the blockmap code and handles indentation"""
        args = {}
        for key in self.args:
            # Get the argument from kwargs
            arg = kwargs[key]
            assert isinstance(arg, str), "Improperly parsed block arg"

            # Indent it if necessary
            indent = self.indents.get(key)
            if indent:
                arg = textwrap.indent(arg, indent)

            # Save the parsed argument
            args[key] = arg

        return self.code.format(**args)


HATS = {
    'procedures_definition',
    'event_whenflagclicked',
    'event_whenkeypressed',
    'event_whenthisspriteclicked',
    'event_whenstageclicked',
    'event_whenbackdropswitchesto',
    'event_whengreaterthan',
    'event_whenbroadcastreceived',
    'control_start_as_clone'
}

LOOPS = {
    'control_repeat',
    'control_forever',
    'control_repeat_until'
}


def _read_blocks():
    """Reads blocks from block_data.json"""
    blocks: Dict[str, Block] = {}

    # Read the json block data
    data_path = path.join(path.dirname(__file__), "block_data.json")
    with open(data_path, 'r') as data_file:
        block_data = json.load(data_file)

    # Parse the block data
    for opcode, block in block_data.items():
        # Get the code from the data
        code = block.get("code")
        if code is None:
            continue
        if isinstance(code, list):
            code = '\n'.join(code)

        # Read indents from the code
        indents = {
            arg_name: indent for indent, arg_name in re.findall(
                INDENT_PAT, code
            )
        }

        # Remove indents from the code
        code = re.sub(INDENT_PAT, "{\\2}", code)

        # Save the block
        blocks[opcode] = Block(block["type"], block["args"], code, indents,
                               block.get("switch"), block.get("basename"))

    return blocks


BLOCKS = _read_blocks()


def format_switch(switch, args):
    """Formats a blockswitch"""
    fields = {
        key: value.lower().replace(' ', '_')
        for key, (type_, value) in args.items()
        if type_ == "field"
    }

    return switch.format(**fields)


def get_blockmap(block, target):
    """
    Creates the blockmap for the block.
    """
    # Step 1, get the base block map.
    # Attempt to get the blockmap from BLOCKS
    blockmap = BLOCKS.get(block['opcode'])

    # Report an error and use a fallback
    if blockmap is None:
        logging.warning("Unknown block with opcode '%s'", block['opcode'])
        blockmap = BLOCKS['default']

    # Step 2, apply any basic switches.
    if blockmap.switch:
        # Get fields from the block
        fields = {}
        for field, value in block['fields'].items():
            fields[field] = value[0].lower().replace(' ', '_')

        # Format the switch using the fields
        opcode = format_switch(blockmap.switch, fields)
        blockmap = BLOCKS.get(opcode, blockmap)

    # Step 3, apply mutations.
    # Modify the block if it is a hat
    if blockmap.return_type == "hat":
        block_switches.hat_mutation(block, target, blockmap)

    # Find another mutation
    switch = block_switches.get_switch(block['opcode'])
    if switch is not None:
        blockmap = switch(block, target) or blockmap

    # Step 4, validate the blockmap and return it
    # Verify the blockmap is a valid
    if blockmap.code is None:
        logging.warning(
            "Failed to resolve blockmap for opcode '%s'", block['opcode'])
        blockmap = BLOCKS['default']

    return BlockMap(*blockmap)
