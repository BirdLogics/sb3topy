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
"""

import json
import re
from collections import namedtuple
from os import path
from typing import Dict

INDENT_PAT = r"(?m)^(\s+)\{(\w+)\}"

Block = namedtuple('Block', ['return_type', 'args', 'code', 'indents'])


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
        code = block["code"]
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
        blocks[opcode] = Block(block["type"], block["args"], code, indents)

    return blocks


BLOCKS = _read_blocks()

