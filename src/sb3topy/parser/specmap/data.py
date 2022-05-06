"""
data.py

Handles the base block data used by all blocks.

Globals:
    BLOCKS: A dictionary with the base Block data for most opcodes.

    HATS: A set containing opcodes which should be treated as hats.

    LOOPS: A set containing opcodes which should be treated as loops.
        Loop blocks should yield at the end, but the yield can be
        omitted in warped blocks as an optimization.

TODO Verify all blocks in data.json have args matching code
TODO Automatically generate LOOPS and HATS from the json
"""


import json
from os import path
from typing import Dict

from . import blockmap

__all__ = ["is_hat", "is_loop", "is_procedure"]

DATA_PATH = path.join(path.dirname(__file__), "data.json")


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
    'control_repeat_until',
    'control_for_each',
    'control_while'
}

BLOCKS: Dict[str, "blockmap.BlockMap"] = {}


def init_data():
    """
    Reads data into BLOCKS from data.json.
    Called automatically at startup.
    """
    global BLOCKS  # pylint: disable=global-statement

    # Read the json block data
    with open(DATA_PATH, 'r', encoding="utf-8") as data_file:
        data = json.load(data_file)

    # Parse the block data
    BLOCKS = {
        opcode: blockmap.BlockMap.from_dict(opcode, block)
        for opcode, block in data.items()
    }


def is_hat(block):
    """Determines if an opcode belongs to a hat block."""
    return block['opcode'] in HATS


def is_loop(block):
    """
    Determines if an opcode belongs to a loop block.

    All loops need to have yield placed at their end. In a no refresh
    custom block, the yield can optionally be omitted for speed.
    """
    return block['opcode'] in LOOPS


def is_procedure(block):
    """Determines if the opcode is 'procedures_definition'."""
    return block['opcode'] == 'procedures_definition'
