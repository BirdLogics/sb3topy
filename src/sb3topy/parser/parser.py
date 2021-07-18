"""
parser.py

Orchestrates the job of parsing the project.json

TODO Costume/Sound initializer indentation
TODO Some literals are wrapped with a conversion
TODO Smart variable type detection
"""

import json
import logging
from textwrap import indent

from .. import config
from . import sanitizer, specmap, targets
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
        code = codemap.file_header() + "\n\n\n"

        # TODO Better pre parse
        for target in sb3['targets']:
            self.targets.add_target(target)
        self.targets.parse_variables()

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
        block_code = self.parse_blocks(target.blocks)

        # Indent init and block code
        code = header_code + init_code + block_code

        # Return the final code for the class
        return codemap.target_class(code, target['name'], target.clean_name)

    def parse_blocks(self, blocks):
        """Creates a function for each topLevel hat in self.target.blocks"""
        # Preparse custom block mutations
        for blockid, block in blocks.items():
            if isinstance(block, dict) and \
                    block['opcode'] == "procedures_prototype":
                self.parse_prototype(block, blockid)

        # Parse all topLevel blocks into code
        code = ""
        for blockid, block in blocks.items():
            if isinstance(block, dict) and block.get('topLevel'):
                assert blockid in self.target.blocks
                code = code + self.parse_hat(blockid, block) + "\n\n"

        return code.rstrip()

    def parse_prototype(self, block, blockid):
        """Preparses custom blocks"""
        mutation = block['mutation']

        proccode = mutation['proccode']
        warp = mutation['warp'] in (True, 'true')
        arg_ids = json.loads(mutation['argumentids'])
        arg_names = json.loads(mutation['argumentnames'])

        self.target.prototypes.add_prototype(
            blockid, proccode, warp, zip(arg_ids, arg_names))

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

            # Get fields, used for blockmap switches
            fields = {}
            for name in block['fields']:
                fields[name] = self.parse_field(block, name)

            # Get inputs
            inputs = {}
            for name in block['inputs']:
                inputs[name] = self.parse_input(block, name)

            # sanitize inputs and fields
            args = self.parse_args(inputs, fields, blockmap, block)

            # Create the code for the block
            code = code + blockmap.format(args) + "\n"

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

    def parse_field(self, block, name):
        """Parses and sanitizes fields"""
        # Get the value of the field
        value = block['fields'][name]

        return 'field', value[0]

    def parse_input(self, block, name):
        """
        Parses an input and returns (type, value)

        The type may be:
         value - A value which needs to be sanitized
         blockid - A blockid which needs to be parsed
         any - A parsed block which needs a cast wrapper
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
                return 'value', None

            # Verify not a variable
            if isinstance(value, str):
                # Shadow block (dropdown)
                if self.target.blocks[value]['shadow']:
                    return 'value', \
                        self.target.blocks[value]['fields'].popitem()[1][0]

                # Just a block
                return 'blockid', value

        # 12 Variable
        if value[0] == 12:
            return self.target.vars.get_type('var', value[1]), \
                self.target.vars.get_reference('var', value[1])

        # 13 List
        if value[0] == 13:
            return "string", self.target.vars.get_reference('var', value[1]) + ".join()"

        # Default to a literal
        # 4-8 Number, 9-10 String, # 11 Broadcast
        if not 4 <= value[0] <= 11:
            logging.error("Unexpected input type %i", value[0])

        return 'value', value[1]

    def parse_args(self, inputs, fields, blockmap, block):
        """
        Ensures the input types match the blockmap
        The result is saved to parameters

        ONLY input types of 'value' and 'field' are sanitized.
        Everything else is given a runtime cast wrapper.
        """

        args = {**fields, **inputs}

        for name, out_type in blockmap.args.items():
            # Get the current value and type
            in_type, value = args.get(name, ('value', None))

            # Parse a stack
            if in_type == 'blockid':
                in_type, value = self.parse_stack(value, block)

            # Sanitize a value
            if in_type == 'value':
                value = sanitizer.cast_value(value, out_type)

            # Handle field inputs
            elif in_type == 'field':
                # Quote the field
                if out_type == 'field':
                    value = sanitizer.quote_field(value.lower())

                # Create a hat identifier
                elif out_type == 'hat_ident':
                    value = self.target.events.name_hat(value, args)

                # Get a procedure argument identifier
                elif out_type == 'proc_arg':
                    value = self.target.prototype.get_arg(value)

                elif out_type == 'var':
                    value = self.target.vars.get_reference('var', value)

                elif out_type == 'list':
                    value = self.target.vars.get_reference('list', value)

                elif out_type == 'property':
                    value = Variables.get_universal('var', value)

                else:
                    logging.error("Unkown field out_type '%s'", out_type)
                    value = '0'

            # Add a runtime cast wrapper
            elif out_type != in_type:
                value = sanitizer.cast_wrapper(value, out_type)

            # This shouldn't be possible
            assert not isinstance(value, tuple)

            # Update the parsed argument
            args[name] = value

        return args
