"""
blockmap.py

Contains the `BlockMap` class and handles blockmap resolution.
"""

import logging
import re
import textwrap
from typing import Dict, List, NamedTuple, Union

from . import data, mutations

__all__ = ["BlockMap", "get_blockmap"]

logger = logging.getLogger(__name__)


INDENT_PAT = r"(?m)^(\s+)\{(\w+)\}"


class BlockMap(NamedTuple):
    """
    Tuple which represents the base data of a block.

    Note that this data format is not the same as the data format in
    the json. This class handles parsing the json data into a code
    friendly format, while the json format is user friendly.

    The from_dict function for this class accepts data in the same
    format as the json file.

    Attributes:
        return_type: The return type of the block. For some blocks,
            this may be a special value such as "hat" or "stack".

        args: A dictionary of "arguments," which are a concatenation of
            inputs and field on the block, and the type each argument
            needs to be after it has been casted.

        code: An unformatted string representing the Python code of the
            block.

        indents: A dictionary containing the indentation for each
            format key in the code string. If a multiline string is
            an input to the code string, then all lines in the string
            should be indented before formating.

        switch: A format string which can be used to get an alternative
            opcode for the block. Only fields are used to format the
            switch.

        basename: For hat blocks, the basename of the hat event. It is
            a format string, so some args can be used as an input.
    """

    return_type: str
    args: Dict[str, str]
    code: Union[str, List[str]]
    indents: Dict[str, str]
    switch: str = ""
    basename: str = ""

    @classmethod
    def from_dict(cls, opcode, block):
        """
        Creates a blockmap from a blockmap as formated in the json.
        """
        # Get the code from the data
        code = block.get("code")

        # Pure switches don't need code
        if code is not None:
            # Allow lists of code to replace newlines
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

        else:
            # The blockmap must have either code or a switch
            assert block.get("switch") is not None, \
                f"Blockmap for '{opcode}' must have either code or a switch"

            # No indentation
            indents = {}

        # Verify hats have a basename
        assert block["type"] != "hat" or "basename" in block, \
            f"Hat blockmap for '{opcode}' missing basename."

        return cls(block["type"], block["args"], code, indents,
                   block.get("switch"), block.get("basename"))

    def format_switch(self, block):
        """Formats a blockswitch"""
        # Read and standardize fields in the block
        fields = {}
        for field, value in block['fields'].items():
            fields[field] = value[0].lower().replace(' ', '_')

        return self.switch.format(**fields)

    def format_code(self, args):
        """
        Indents values in `args` and returns the formatted code.
        """
        for key in self.args:
            # The value should always be a string
            assert isinstance(args[key], str), "Improperly parsed block arg"

            # Indent the value, if necessary
            indent = self.indents.get(key)
            if indent:
                args[key] = textwrap.indent(args[key], indent)

        # Format the code string
        return self.code.format(**args)


def get_blockmap(block, target):
    """
    Creates the blockmap for the block.
    """
    # Step 1, get the base block map.
    # Attempt to get the blockmap from BLOCKS
    blockmap = data.BLOCKS.get(block['opcode'])

    # Report an error and use a fallback
    if blockmap is None:
        logger.warning("Unknown block with opcode '%s'", block['opcode'])
        blockmap = data.BLOCKS['default']

    # Step 2, apply any basic switches.
    if blockmap.switch:
        # Format the switch using the fields
        opcode = blockmap.format_switch(block)
        blockmap = data.BLOCKS.get(opcode, blockmap)

    # Step 3, apply mutations.
    # Modify the block if it is a hat
    if blockmap.return_type == "hat":
        blockmap = mutations.hat_mutation(block, target, blockmap)

    # Find another mutation
    mutation = mutations.get_mutation(block['opcode'])
    if mutation is not None:
        blockmap = mutation(block, target, blockmap)

    # Step 4, validate the blockmap and return it
    if blockmap.code is None:
        logger.warning(
            "Failed to resolve blockmap for opcode '%s'", block['opcode'])
        blockmap = data.BLOCKS['default']

    return BlockMap(*blockmap)
