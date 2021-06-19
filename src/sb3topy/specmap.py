"""
specmap.py

Handles reading data from the specmap

The goal of the specmap is to provide text which
can easily be formatted using input data to make
valid Python code.

SPEC_PAT - A regex pattern used to parse the specmap
INDENT_PAT - A regex pattern used to get indentation for substacks


TODO specmap docs outdated?
Hats need a generated {NAME} flag for the cb definition
They also need an indented {SUBSTACK} containing their blocks
Custom blocks must be provided with {PARAMETERS}

base name
code

Specmap
    Loads the specmap
    Initializes blockmaps
    Retrieves blockmaps

BlockMap
    Represents a certain block
    Handles creating block code
    Parses flags

TODO Args not copied to switches
"""

import logging
import re
from textwrap import indent

from . import naming

SPEC_PAT = (
    r"(?s)#: ?(\w*?)?(?# type)"
    r" ?((?:\w|'|\^|#)+)(?# opcode) ?"
    r"(?:\(([\w, ]+)?\))?(?# args) ?"
    r"(?:-(\w+))?(?# flags)"
    r"(?:\n#\? ?([\w{}]+))?(?# switch)"
    r"\n(.+?)\n\n(?# code)"
)

INDENT_PAT = r"(?m)^(\s+)\{(\w+)\}"


class Specmap:
    """Handles the specmap file"""

    def __init__(self, path):
        # Read the specmap file
        with open(path, 'r') as file:
            data = file.read()

        # Parse with regex
        data = re.findall(SPEC_PAT, data)

        self.specmap = {}
        for block in data:
            self._add_block(block)

    def _add_block(self, block):
        """Creates a BlockMap for a specmap item"""
        self.specmap[block[1]] = BlockMap(*block)

    def __getitem__(self, opcode):
        return self.specmap.get(opcode)

    def special(self, name):
        """Gets the code for a special"""
        return self.specmap["special_" + name]['code']

    def code(self, name):
        """Gets the code for code_name"""
        return self.specmap['code_' + name].code

    def get(self, block, fields, protoypes):
        """Gets the right BlockMap to represent this block"""
        # Get the block's opcode
        opcode = block['opcode']
        blockmap: BlockMap = self.specmap.get(opcode)

        if blockmap is None:
            logging.error("Missing blockmap for opcode '%s'", opcode)
            blockmap = self.specmap['special_unkown']

        switch = blockmap.switch(fields)
        blockmap = self.specmap.get(switch, blockmap)

        if opcode == 'procedures_definition':
            return self.map_prototype(block, protoypes)
        elif opcode == 'procedures_call':
            return self.map_proccall(block, protoypes)

        return blockmap

    @staticmethod
    def map_prototype(block, protoypes: naming.Prototypes):
        """Gets the blockmap for a procedure definition"""
        # Move the next block to a substack
        # block['inputs']['SUBSTACK'] = [1, block['next']]
        # block['next'] = None

        # Get information about the procedure
        protoype = protoypes.get_definition(
            block['inputs'].pop('custom_block')[1])
        parameters = protoype.args_list()
        name = protoype.name

        return BlockMap(
            "stack", "procedures_definition",
            "stack SUBSTACK", "", "",
            f"async def {name}(self, util, {parameters}):\n    {{SUBSTACK}}",
            protoype
        )

    @staticmethod
    def map_proccall(block, prototypes: naming.Prototypes):
        """Creates a blockmap for a procedure call"""
        # Get the prototype for the block
        prototype = prototypes.from_proccode(block['mutation']['proccode'])

        # Replace input names with cleaned arg names
        block['inputs'] = {prototype.arg_from_id(
            argid): value for argid, value in block['inputs'].items()}

        # Create arg definition parsed by the BlockMap
        args_def = prototype.args_list(', stack ')
        if args_def:
            args_def = "stack " + args_def

        # Create arg code formatted by the BlockMap
        args_code = prototype.args_list('}, {')
        if args_code:
            args_code = '{' + args_code + '}'

        return BlockMap(
            "stack", "procedures_call",
            args_def, "", "",
            f"await self.{prototype.name}(util, {args_code})"
        )


class BlockMap:
    """
    Handles the blockmap for a block

    return_type - The type the block returns
    args - Dict of {name: type} pairs

    dirty - How dirty the block makes the sprite
    do_yield - Decides whether to yield after each substack
    set_dirty - Decides whether dirty needs to be set before running

    code - The unformatted Python code
    name - The base name for a hat

    _switch - The unformatted opcode switch
    """

    def __init__(self, return_type, opcode, args, flags, switch, code, prototype=None):
        """
        Initializes from a blockmap tuple in the format:
         *(return_type, opcode, args, flags, switch, data)
        """

        # Get return type
        self.return_type = return_type

        # Get opcode
        self.opcode = opcode

        # Get the type of each arg
        self.args = {}
        for arg in re.split(", ?", args):
            # Ignore blocks without args
            if not arg:
                continue

            # Split the "type arg" pair
            arg = arg.split()

            # Throw a nice error if missing type
            assert len(arg) == 2, "Check specmap args for " + opcode

            # Add name: type pair to args dict
            self.args[arg[1]] = arg[0]

        # Check the dirty flag
        self.dirty = 0
        if 'd1' in flags:
            self.dirty = 1
        elif 'd2' in flags:
            self.dirty = 2
        elif 'd3' in flags:
            self.dirty = 3

        # Save the yield and set dirty flags
        self.do_yield = 'y' in flags
        self.set_dirty = 's' in flags

        # Save the switch
        self._switch = switch

        # Get the code and hat name for hats
        if 'h' in flags:
            # 1st line of data = hat name
            lines = code.splitlines()
            self.name = lines[0]
            lines[0] = "async def {NAME}(self, util):"
            self.code = '\n'.join(lines)
        else:
            self.name = None
            self.code = code

        # Read indentation data
        self.indents = {
            name: space for space, name in re.findall(INDENT_PAT, self.code)
        }
        self.code = re.sub(INDENT_PAT, "{\\2}", self.code)  # Strip indentation

        # Save the prototype
        self.prototype = prototype

    def switch(self, fields):
        """Returns a new opcode using the switch and fields"""
        return self._switch.format(
            **dict(map(lambda item: (item[0], item[1][1]), fields.items()))
        ).replace(" ", "_")

    def format(self, args):
        """Formats the code using the input+field dict"""
        # Indent args with indention
        for name, space in self.indents.items():
            args[name] = indent(args[name], space)

        # Replace {tags} with args
        return self.code.format(**args)

    def get_identifier(self, hats: naming.Events, args):
        """Gets an identifier for a hat"""
