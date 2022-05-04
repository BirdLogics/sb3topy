"""
parser.py

Orchestrates the job of parsing the project.json
"""

import logging

from .. import config
from . import sanitizer, specmap, targets
from .specmap import codemap
from .variables import Variables

__all__ = ('parse_project', 'Parser')

logger = logging.getLogger(__name__)


def parse_project(project, manifest):
    """Parses project and returns the Python code"""
    logger.info("Compiling project into Python...")
    return Parser(project, manifest).parse()


class Parser:
    """
    Handles parsing a target

    Attributes:
        targets: A Targets instance used to handle each target in the
            sb3 project.json.

        project: A dict like object containing the data from the sb3
            project.json.
    """

    def __init__(self, project, manifest):
        self.targets = targets.Targets()
        self.manifest = manifest
        self.project = project

    def parse(self):
        """Parses the sb3 and returns Python code"""
        # Run the first parsing pass
        self.first_pass()

        # Run the second parsing pass
        self.second_pass()

        # Run the final parsing pass
        return self.third_pass()

    def first_pass(self):
        """
        Runs the first pass of the parser.
        The first pass creates classes for targets and prototypes,
        and marks universal variable used in sensing_of.
        """
        logger.info("Initializing parser...")

        # Create a class for each target
        self.targets.add_targets(self.project['targets'])

        # Have each target run a first pass
        for target in self.targets:
            target.first_pass()

    def second_pass(self):
        """
        Runs the second pass of the parser.

        Creates classes for each Variable and runs type
        guessing for variables and procedure arguments.

        Also names solo broadcast receivers.
        """
        logger.info("Running optimizations...")

        for target in self.targets:
            target.second_pass()

        # Guess the type of each variable
        if config.VAR_TYPES:
            self.targets.digraph.resolve()

        # Name solo broadcast receivers
        broadcasts = targets.Target.broadcasts
        for broadcast, target_name in broadcasts.items():
            if target_name is not None:
                target = self.targets.targets[target_name]
                target.events.name_hat("broadcast_{BROADCAST}", {
                    'BROADCAST': broadcast})

    def third_pass(self):
        """
        Runs the third pass of the parser.
        This pass actually creates the Python code for the project.
        """
        logger.info("Generating Python code...")

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
        init_code = codemap.create_init(target, self.manifest) + "\n\n"

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

        logger.debug("Skipping topLevel block '%s' with opcode '%s'",
                     blockid, block['opcode'])
        return ""

    def parse_stack(self, blockid, parent_block=None):
        """
        Parses a stack/input
        """

        code = ""
        block = self.target.blocks[blockid]

        while block:
            # logger.debug("Parsing block '%s' with opcode '%s'",
            #               blockid, block['opcode'])

            # Get the conversion map
            # May "mutate" the block to add custom arguments
            # May set target.prototype
            blockmap = specmap.get_blockmap(block, self.target)

            # Get fields
            args = {}
            for name in block['fields']:
                args[name] = 'field', block['fields'][name][0]

            # Get inputs
            for name, value in block['inputs'].items():
                args[name] = specmap.parse_input(self.target.blocks, value)

            # Parse each argument using the blockmap
            clean_args = {}
            for name, end_type in blockmap.args.items():
                clean_args[name] = self.parse_arg(name, args, end_type, block)
                assert isinstance(clean_args[name], str)

            # Create the code for the block
            code = code + blockmap.format_code(clean_args) + "\n"

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
        start_type, value = args.get(name, ('none', "None"))

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
            value = self.target.vars.get_reference('list', value) + '.join()'

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
        be converted into a function identifier.

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
            return self.target.events.name_hat(
                value, {name: val[1] for name, val in args.items()})

        # Get an existing hat identifier for another target
        if end_type == 'ex_hat_ident':
            return self.targets.targets[
                args['TARGET'][1]].events.existing_hat(
                    value, {name: value[1] for name, value in args.items()})

        # Get a procedure argument identifier
        if end_type == 'proc_arg':
            return self.target.prototype.get_arg(value)

        # Default to quoting
        logger.warning("Unknown field type '%s'", end_type)
        return sanitizer.quote_field(value)
