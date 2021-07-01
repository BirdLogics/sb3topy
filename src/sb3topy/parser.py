"""
parser.py




Target needs:
 global broadcasts
 global variables
 specmap

 variables
 hats
 target

Methods:
 parse
 parse_target

 parse_broadcasts

 parse_costumes
 parse_sounds
 parse_variables
 parse_lists
 parse_customblocks
 parse_blocks

 parse_fields
 parse_inputs
 parse_inputs

TODO Costume/Sound initializer indentation
TODO Some literals are wrapped with a conversion
TODO Smart variable type detection
"""

import json
import logging
from textwrap import indent

from . import config, sanitizer, specmap, targets
from .variables import Variables


class Parser:
    """
    Handles parsing a target

    TODO No newlines on non stack block
    TODO Sprite class
    """

    target: targets.Target

    def __init__(self):
        self.specmap = specmap.Specmap(config.SPECMAP_PATH)
        self.targets = targets.Targets()

    def parse(self, sb3):
        """Parses the sb3 and returns Python code"""
        logging.info("Compiling project...")
        code = self.specmap.code("header") + "\n\n\n"

        # TODO Better pre parse
        for target in sb3['targets']:
            self.targets.add_target(target)
        self.targets.parse_variables()

        for target in self.targets:
            self.target = target
            code = code + self.parse_target(target) + "\n\n\n"

        code = code + self.create_footer() + "\n"

        return code

    def parse_target(self, target: targets.Target):
        """Converts a sb3 target dict into the code for a Python class"""

        # Get property definitions, class description, etc.
        header_code = self.create_header(target) + "\n\n"

        # Parse variables, lists, costumes, and sounds
        init_code = self.create_init(target) + "\n\n"

        # Parse all blocks into code
        block_code = self.parse_blocks(target.blocks)

        # Indent init and block code
        code = indent(header_code + init_code + block_code, "    ")

        # Return the final code for the class
        return self.specmap.code("class").format(
            code=code, name=target.clean_name).rstrip()

    def create_header(self, target: targets.Target):
        """Creates code between "class ...:" and "def __init__" """

        comment = '"""Sprite ' + \
            sanitizer.quote_string(target['name']).strip('"') + '"""\n\n'

        variable_code = self.parse_variables(target)

        return comment + variable_code

    def create_init(self, target):
        """Creates Python __init__ code for a target dict"""
        info = self.specmap.code('info').format(
            xpos=target.get('x', 0),
            ypos=target.get('y', 0),
            direction=target.get('direction', 90),
            visible=target.get('visible', True)
        ) + "\n\n"

        costumes = self.parse_costumes(target) + "\n\n"
        sounds = self.parse_sounds(target) + "\n\n"

        lists_init = self.parse_lists(target)

        init_code = info + costumes + sounds + "\n" + lists_init

        return self.specmap.code('target_init').format(
            init_code=indent(init_code, "    "*2),
            layer=int(target['layerOrder'])
        ).rstrip()

    def parse_costumes(self, target):
        """Creates code to init costumes for a target"""
        costumes = []
        costume_code = self.specmap.code('costume')

        # Create a dict str for each costume
        for costume in target['costumes']:
            name = sanitizer.quote_string(costume['name'])

            # Validate the costume path
            if not sanitizer.valid_md5ext(costume['md5ext']):
                logging.error(
                    "Invalid costume format or path '%s'", costume['md5ext'])
                costumes.append("{'name': " + name + "}")
                continue

            # Create the costume dict
            costumes.append(costume_code.format(
                name=name,
                path=sanitizer.quote_string(costume['md5ext']),
                center=(
                    int(costume['rotationCenterX']),
                    int(costume['rotationCenterY'])
                ),
                scale=costume['bitmapResolution']
            ))

        # Create the costumes list string
        costumes = "[\n" + \
            indent(',\n'.join(costumes), "    ") + "\n]"

        return self.specmap.code('costumes_init').format(
            costume=int(target['currentCostume']),
            size=target.get('size', 100),
            rotation=sanitizer.quote_string(target.get('rotationStyle')),
            costumes=costumes
        )

    def parse_sounds(self, target):
        """Creates code to init sounds for a target"""
        sounds = []
        sound_code = self.specmap['code_sound'].code

        # Create a dict string for each sound
        for sound in target['sounds']:
            name = sanitizer.quote_string(sound['name'])

            # Validate the sound path
            if not sanitizer.valid_md5ext(sound['md5ext']):
                logging.error(
                    "Invalid sound format or path '%s'", sound['md5ext'])
                sounds.append("{'name': " + name + "}")
                continue

            sounds.append(sound_code.format(
                name=name,
                path=sanitizer.quote_string(sound['md5ext'])
            ))

        # Create the sounds list string
        sounds = "[\n" + indent(',\n'.join(sounds), "    ") + "\n]"

        return self.specmap.code('sounds_init').format(
            volume=int(target['volume']),
            sounds=sounds
        )

    def parse_variables(self, target: targets.Target):
        """Creates code to init variables for a target and clones"""
        vars_init = []

        init_code = self.specmap['code_var_init'].code

        for var in target['variables'].values():
            name = target.vars.get_local('var', var[0])
            vars_init.append(init_code.format(
                name=name,
                value=sanitizer.quote_number(var[1])
            ))

        return '\n'.join(vars_init).rstrip()

    def parse_lists(self, target):
        """Creates code to init lists for a target and clones"""
        list_init = []

        init_code = self.specmap.code('list_init')

        for lst in target['lists'].values():
            # Validate list items
            items = []
            for value in lst[1]:
                items.append(sanitizer.quote_number(value))

            # Create code with
            name = self.target.vars.get_local('list', lst[0])
            list_init.append(init_code.format(
                name=name,
                items=indent("[" + ', '.join(items) + "]", "    ")
            ) + "\n")

        return "".join(list_init).rstrip()

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
        blockmap: specmap.BlockMap = self.specmap[block['opcode']]

        # Verify the block is a known hat
        if blockmap is not None and blockmap.name:
            block['inputs']['SUBSTACK'] = [2, block['next']]
            block['next'] = None

            stack = self.parse_stack(blockid)
            return stack[1]

        # TODO Add hats to identifiers

        logging.debug("Skipping topLevel block '%s' with opcode '%s'",
                      blockid, block['opcode'])
        return ""

    def parse_stack(self, blockid, prototype=None, parent_bm=None, is_stack=False):
        """
        Parses a stack/input
        """

        code = ""
        block = self.target.blocks[blockid]

        while block:
            # logging.debug("Parsing block '%s' with opcode '%s'",
            #               blockid, block['opcode'])

            # Get fields, used for blockmap switches
            fields = {}
            for name in block['fields']:
                fields[name] = self.parse_field(block, name, prototype)

            # Get the block's conversion map
            blockmap = self.specmap.get(block, fields, self.target.prototypes)

            # Get the prototype if there is one4
            if blockmap.prototype is not None:
                prototype = blockmap.prototype

            # Get inputs
            inputs = {}
            for name in block['inputs']:
                inputs[name] = self.parse_input(block, name)

            # sanitize inputs and fields
            args = self.parse_args(inputs, fields, blockmap, prototype)

            # Get a name for functions
            if blockmap.name:
                args['NAME'] = self.target.events.name_hat(blockmap.name, args)
                args['EVENT'] = sanitizer.quote_field(
                    self.target.events.get_event(blockmap.name, args))

            # Create the code for the block
            code = code + blockmap.format(args) + "\n"

            # Get the next block
            block = self.target.blocks.get(block['next'])

        code = code.strip()
        if parent_bm and parent_bm.do_yield and is_stack and not (prototype and prototype.warp):
            code = code + "\n" + self.specmap.code("yield") + "\n"

        return blockmap.return_type, code

    def parse_field(self, block, name, prototype):
        """Parses and sanitizes fields"""
        # Get the value of the field
        value = block['fields'][name]

        if name == 'BROADCAST_OPTION':
            return 'field', value[0]

        if name == 'VARIABLE':
            return 'field', self.target.vars.get_reference('var', value[0])

        if name == 'PROPERTY':
            return 'field', Variables.get_universal('var', value[0])

        if name == 'LIST':
            return 'field', self.target.vars.get_reference('list', value[0])

        if block['opcode'] in (
                'argument_reporter_string_number',
                'argument_reporter_boolean'):
            return 'field', prototype.get_arg(value[0])

        return 'field', sanitizer.quote_field(value[0].lower())

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

        # Handle possible block input
        if value[0] == 1:
            if isinstance(value[1], list):
                # Wrapped value
                value = value[1]
            else:
                # Wrapped block
                value = [2, value[1]]
        elif value[0] == 3:
            # Block covering value
            value = [2, value[1]]

        # Handle a block input
        if value[0] == 2:
            value = value[1]

            # Handle an empty block
            if value is None:
                return 'value', None

            if isinstance(value, str):
                # Shadow block (dropdown)
                if self.target.blocks[value]['shadow']:
                    return 'value', \
                        self.target.blocks[value]['fields'].popitem()[1][0]

                # A block
                return 'blockid', value

        # 4-8 Number, 9-10 String, # 11 Broadcast
        if 4 <= value[0] <= 11:
            return 'value', value[1]

        # 12 Variable
        if value[0] == 12:
            return self.target.vars.get_type('var', value[1]), \
                self.target.vars.get_reference('var', value[1])

        # 13 List
        if value[0] == 13:
            return "string", self.target.vars.get_reference('var', value[1]) + ".join()"

        # Unkown
        logging.error("Unexpected input type %i", value[0])
        return 'value', value[1]

    def parse_args(self, inputs, fields, blockmap, prototype):
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
                in_type, value = self.parse_stack(
                    value, prototype, blockmap, (out_type == 'stack'))

            # sanitize a value
            if in_type == 'value':
                value = sanitizer.cast_value(value, out_type)

            # Quote an expected field
            # If in_type is a field, it should already be sanitized
            elif out_type == 'field' and in_type != 'field':
                value = sanitizer.quote_field(value)

            # Add a runtime cast wrapper
            elif out_type != in_type:
                value = sanitizer.cast_wrapper(value, out_type)

            # Update the parsed input
            if isinstance(value, tuple):
                raise Exception()
            args[name] = value

        return args

    def create_footer(self):
        """Creates the code at the end to run the program"""
        # Create a dict linking sprite names to their identifers
        sprites = []
        for name, identifier in self.targets.name_items():
            sprites.append(sanitizer.quote_field(name) + ": " + identifier)
        items = indent(',\n'.join(sprites), "    ")
        sprites_code = self.specmap.code(
            "sprites").format(items=items)

        # Create an if __name__ == '__main__' statement
        main_code = self.specmap.code("main")

        return sprites_code + "\n\n" + main_code
