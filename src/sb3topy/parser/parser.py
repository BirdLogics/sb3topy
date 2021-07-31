"""
parser.py

Orchestrates the job of parsing the project.json

TODO Costume/Sound initializer indentation
TODO Some literals are wrapped with a conversion
TODO Smart variable type detection
"""

import json
import logging

from .. import config
from . import sanitizer, specmap, targets, typing
from .specmap import codemap
from .variables import Variables


class Parser:
    """
    Handles parsing a target

    TODO No newlines on non stack block
    TODO Sprite class
    """

    target: targets.Target

    def __init__(self):
        self.targets = targets.Targets()

    def parse(self, sb3):
        """Parses the sb3 and returns Python code"""
        logging.info("Compiling project...")

        # Run the first parsing pass
        self.first_pass(sb3)

        # Run the second parsing pass
        self.second_pass()

        # Run the final parsing pass
        return self.third_pass()

    def first_pass(self, sb3):
        """
        Runs the first pass of the parser.
        The first pass creates classes for targets and prototypes,
        and marks universal variable used in sensing_of.
        """

        # Create a class for each target
        self.targets.add_targets(sb3['targets'])

        # Have each target run a first pass
        for target in self.targets:
            target.first_pass()

    def second_pass(self):
        """
        Runs the second pass of the parser.
        The second pass creates classes for each Variable and
        runs type guessing for variables and procedure arguments
        """

        for target in self.targets:
            target.second_pass()

        # Guess the type of each variable
        if config.VAR_TYPES:
            self.targets.digraph.resolve()

    def third_pass(self):
        """
        Runs the third pass of the parser.
        This pass actually creates the Python code for the project.
        """
        code = codemap.file_header() + "\n\n\n"

        for target in self.targets:
            self.target = target
            code = code + self.parse_target(target) + "\n\n\n"

        code = code + "\n\n" + codemap.file_footer() + "\n"

        return code

    def parse_target(self, target: targets.Target):
        """Converts a sb3 target dict into the code for a Python class"""

        # Get property definitions, class description, etc.
        header_code = codemap.create_header(target) + "\n\n"

        # Parse variables, lists, costumes, and sounds
        init_code = codemap.create_init(target) + "\n\n"

        # Parse all blocks into code
        block_code = self.parse_blocks()

        # Indent init and block code
        code = header_code + init_code + block_code

        # Return the final code for the class
        return codemap.target_class(code, target['name'], target.clean_name)

    def parse_blocks(self):
        """Creates a function for each topLevel hat in self.target.blocks"""
        # Parse all topLevel blocks into code
        code = []
        for blockid, block in self.target.hats:
            code.append(self.parse_hat(blockid, block))

        return '\n\n'.join(code)

    def parse_hat(self, blockid, block):
        """Gets the code if any, for a topLevel block"""

        # Verify the block is a known hat
        if specmap.is_hat(block):
            stack = self.parse_stack(blockid)
            return stack[1]

        # TODO Add hats to identifiers

        logging.debug("Skipping topLevel block '%s' with opcode '%s'",
                      blockid, block['opcode'])
        return ""

    def parse_stack(self, blockid, parent_block=None):
        """
        Parses a stack/input
        """

        code = ""
        block = self.target.blocks[blockid]

        while block:
            # logging.debug("Parsing block '%s' with opcode '%s'",
            #               blockid, block['opcode'])

            # Get the block's conversion map
            # Also sets the target's procedure if necesary
            blockmap = specmap.get_blockmap(block, self.target)

            # Get fields
            args = {}
            for name in block['fields']:
                args[name] = 'field', block['fields'][name][0]

            # Get inputs
            for name in block['inputs']:
                args[name] = self.parse_input(block, name)

            # Parse each argument using the blockmap
            clean_args = {}
            for name, end_type in blockmap.args.items():
                clean_args[name] = self.parse_arg(name, args, end_type, block)
                assert isinstance(clean_args[name], str)

            # Create the code for the block
            code = code + blockmap.format(clean_args) + "\n"

            # Get the next block
            block = self.target.blocks.get(block['next'])

        # If the parent block is a loop, yield
        if parent_block and specmap.is_loop(parent_block) and \
            blockmap.return_type == 'stack' and not \
                (self.target.prototype and self.target.prototype.warp):
            code = code + "\n" + codemap.yield_()

        # At the end of a procedure definition,
        # clear the target's prototype
        if parent_block and specmap.is_procedure(parent_block):
            self.target.prototype = None

        return blockmap.return_type, code.strip()

    def parse_input(self, block, name):
        """
        Parses an input and returns (type, value)

        The type may be:
         literal - A literal value which needs to be sanitized
         blockid - A blockid which needs to be parsed
         block - A parsed block of unkown type
         string - A parsed block which returns a str
        """

        # Get the value of the input
        value = block["inputs"][name]

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
                if self.target.blocks[value]['shadow']:
                    return 'literal', \
                        self.target.blocks[value]['fields'].popitem()[1][0]

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

    def parse_arg(self, name, args, end_type, block):
        """
        Ensures the type of an input matches
        the type expected by the blockmap.

        start_type is the type of value
        end_type is the type expected by the blockmap

        If start_type is blockid, variable, or list_reporter,
        the value will be parsed and a new type generated.

        start_type will then be 'field', 'literal', or the type of a block.

        Fields can contain many values, such as the name of a
        variable. They are parsed by the parse_field function.

        Literals are forcibly casted to mach the end_type.

        Blocks are casted at runtime. Depending on the
        type, a wrapper may be placed around the block.
        """

        # Get the unparsed value and type from args
        start_type, value = args.get(name, ('none', None))

        # An unparsed block
        if start_type == 'blockid':
            start_type, value = self.parse_stack(value, block)

        # A variable reporter
        elif start_type == 'variable':
            start_type = self.target.vars.get_type('var', value)
            value = self.target.vars.get_reference('var', value)

        # A list reporter
        elif start_type == 'list_reporter':
            start_type = 'block'
            value = self.target.vars.get_reference('var', value) + '.join()'

        # Directly cast a literal
        if start_type == 'literal':
            return sanitizer.cast_literal(value, end_type)

        # Fields take special parsing
        if start_type == 'field':
            return self.parse_field(value, end_type, args)

        # Put a runtime cast wrapper around a block
        return sanitizer.cast_wrapper(value, start_type, end_type)

    def parse_field(self, value, end_type, args):
        """
        Parses a field depending on the value of end_type.

        If end_type is 'field', the value will be lowered and quoted.

        If end_type is 'variable', the value will
        be converted into a variable identifier.

        If end_type is 'list', the value will
        be converted into a list identifier.

        If end_type is 'property', the value will
        be converted into a universal identifier.

        If end_type is 'hat_ident', the value will
        be converted into a functon identifier.

        Otherwise, the value will be quoted and a warning shown.
        """
        # Quote and lower a field
        if end_type == 'field':
            return sanitizer.quote_field(value.lower())

        # Get a variable identifier
        if end_type == 'variable':
            return self.target.vars.get_reference('var', value)

        # Get a list identifier
        if end_type == 'list':
            return self.target.vars.get_reference('list', value)

        # Get a universal variable identifier
        if end_type == 'property':
            return Variables.get_universal(value)

        # Create a hat identifier
        if end_type == 'hat_ident':
            return self.target.events.name_hat(value, args)

        # Get a procedure argument identifier
        if end_type == 'proc_arg':
            return self.target.prototype.get_arg(value)

        # Default to quoting
        logging.warning("Unkown field type '%s'", end_type)
        return sanitizer.quote_field(value)
