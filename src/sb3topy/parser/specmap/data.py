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

__all__ = ["HATS", "LOOPS", "BLOCKS"]

DATA_PATH = path.join(path.dirname(__file__), "data.json")


def _read_blocks():
    """Reads blocks from data.json"""

    # Read the json block data
    with open(DATA_PATH, 'r', encoding="utf-8") as data_file:
        data = json.load(data_file)

    # Parse the block data
    blocks: Dict[str, blockmap.BlockMap] = {
        opcode: blockmap.BlockMap.from_dict(opcode, block)
        for opcode, block in data.items()
    }

    return blocks


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

BLOCKS = _read_blocks()
