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

TODO Set sprite._layer in __init__?
TODO Costume/Sound initializer indentation
TODO Some literals are wrapped with a conversion
TODO Preparse sensing of variables to keep same name
Eg. If two sprites have a var named 't123$%@' the clened name
should be guaranteed to be the same if used in a sensing of
"""

import logging
import json
from textwrap import indent

from . import config
from . import sanitizer
from . import naming
from . import specmap


class Parser:
    """
    Handles parsing a target

    TODO No newlines on non stack block
    TODO Sprite class
    """

    def __init__(self):
        self.specmap = specmap.Specmap(config.SPECMAP_PATH)

        self.targets = naming.Sprites()
        self.events = naming.Events()
        self.vars = naming.Variables()
        self.prototypes = naming.Prototypes(self.events)
        self.blocks = {}
        self.vars_dict = {}

    def parse(self, sb3):
        """Parses the sb3 and returns Python code"""
        if not sb3['targets'][0]['isStage']:
            logging.error("First target in sb3 is not stage.")

        code = self.specmap.code("header") + "\n\n\n"

        # TODO Better pre parse
        for target in sb3['targets']:
            self.vars_dict[target['name']] = naming.Variables(target['isStage'])

        for target in sb3['targets']:
            code = code + self.parse_target(target) + "\n\n\n"

        code = code + self.create_footer() + "\n"

        return code

    def parse_target(self, target):
        """Converts a sb3 target dict into the code for a Python class"""
        # Parse variables, lists, costumes, and sounds
        self.vars = self.vars_dict[target['name']]
        init_code = self.create_init(target)

        # Parse all blocks into code
        block_code = self.parse_blocks(target['blocks'])

        # Get the event dict from hats
        init_code = init_code + "\n\n" + \
            indent(self.parse_events(), "    ") + "\n\n"

        # Indent init and block code
        code = indent(init_code+block_code, "    ")

        # Get a sanitized sprite name
        name = self.targets.get_sprite(target['name'])

        # Return the final code for the class
        return self.specmap.code("class").format(code=code, name=name).rstrip()

    def create_init(self, target):
        """Creates Python __init__ code for a target dict"""
        info = self.specmap.code('info').format(
            xpos=target.get('x', 0),
            ypos=target.get('y', 0),
            direction=target.get('direction', 90),
            visible=target.get('visible', True)
        ) + "\n\n"
        info_clone = self.specmap.code('info_clone') + "\n\n"

        costumes = self.parse_costumes(target) + "\n\n"
        sounds = self.parse_sounds(target) + "\n\n"
        assets_clone = self.specmap.code('assets_clone') + "\n\n"

        vars_init, vars_clone = self.parse_variables(target)
        lists_init, lists_clone = self.parse_lists(target)

        init_code = info + costumes + sounds + vars_init + "\n" + lists_init
        clone_code = info_clone + assets_clone + vars_clone + "\n" + lists_clone

        return self.specmap.code('target_init').format(
            init_code=indent(init_code, "    "*2),
            clone_code=indent(clone_code, "    "*2),
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

    def parse_variables(self, target):
        """Creates code to init variables for a target and clones"""
        vars_init = []
        vars_clone = []

        init_code = self.specmap['code_var_init'].code
        clone_code = self.specmap['code_var_clone'].code
        for var in target['variables'].values():
            name = self.vars.get_local('var', var[0])
            vars_init.append(init_code.format(
                name=name,
                value=sanitizer.quote_number(var[1])
            ))
            vars_clone.append(clone_code.format(
                name=name
            ))

        return '\n'.join(vars_init).rstrip(), '\n'.join(vars_clone).rstrip()

    def parse_lists(self, target):
        """Creates code to init lists for a target and clones"""
        list_init = []
        list_clone = []

        init_code = self.specmap.code('list_init')
        clone_code = self.specmap.code('list_clone')

        for lst in target['lists'].values():
            # Validate list items
            items = []
            for value in lst[1]:
                items.append(sanitizer.quote_number(value))

            # Create code with
            name = self.vars.get_local('list', lst[0])
            list_init.append(init_code.format(
                name=name,
                items=indent("[" + ', '.join(items) + "]", "    ")
            ) + "\n")
            list_clone.append(clone_code.format(
                name=name
            ) + "\n")

        return "".join(list_init).rstrip(), "".join(list_clone).rstrip()

    def parse_events(self):
        """Creates code to link hat coroutines to named events"""
        hats_init = []

        init_code = self.specmap.code("hat")

        for event, hats in self.events.event_items():
            idents = []
            for hat in hats:
                idents.append("self." + hat)
            hats_init.append(init_code.format(
                name=sanitizer.quote_field(event),
                hats=indent(', '.join(idents), "    ")
            ))

        hats = indent(",\n".join(hats_init).rstrip(), "    ")

        return self.specmap.code("hats_dict").format(hats=hats)

    def parse_blocks(self, blocks):
        """Creates a function for each topLevel hat in self.blocks"""
        # Preparse custom block mutations
        self.prototypes = naming.Prototypes(self.events)
        for blockid, block in blocks.items():
            if isinstance(block, dict) and \
                    block['opcode'] == "procedures_prototype":
                self.parse_prototype(block, blockid)

        # Save blocks to self and reset hats
        self.blocks = blocks
        self.events = naming.Events()

        # Parse all topLevel blocks into code
        code = ""
        for blockid, block in blocks.items():
            if isinstance(block, dict) and block.get('topLevel'):
                code = code + self.parse_hat(blockid, block) + "\n\n"

        return code.rstrip()

    def parse_prototype(self, block, blockid):
        """Preparses custom blocks"""
        mutation = block['mutation']

        proccode = mutation['proccode']
        warp = mutation['warp'] in (True, 'true')
        arg_ids = json.loads(mutation['argumentids'])
        arg_names = json.loads(mutation['argumentnames'])

        self.prototypes.add_prototype(
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

        logging.warning("Skipping topLevel block '%s' with opcode '%s'",
                        blockid, block['opcode'])
        return ""

    def parse_stack(self, blockid, prototype=None, parent_bm=None, is_stack=False):
        """
        Parses a stack/input
        """

        code = ""
        block = self.blocks.get(blockid)

        while block:
            logging.debug("Parsing block '%s' with opcode '%s'",
                          blockid, block['opcode'])

            # Get fields, used for blockmap switches
            fields = {}
            for name in block['fields']:
                fields[name] = self.parse_field(block, name, prototype)

            # Get the block's conversion map
            blockmap = self.specmap.get(block, fields, self.prototypes)

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
                args['NAME'] = self.events.name_hat(blockmap.name, args)

            # Create the code for the block
            code = code + blockmap.format(args) + "\n"

            # Get the next block
            block = self.blocks.get(block['next'])

        code = code.strip()
        if parent_bm and parent_bm.do_yield and is_stack and not (prototype and prototype.warp):
            code = code + "\n" + self.specmap.code("yield") + "\n"

        # TODO Better warp handling
        if parent_bm and parent_bm.prototype and parent_bm.prototype.warp:
            code = "self.warp = True\n" + code + "\nself.warp = False"

        return blockmap.return_type, code

    def parse_field(self, block, name, prototype):
        """Parses and sanitizes fields"""
        # Get the value of the field
        value = block['fields'][name]

        if name == 'BROADCAST_OPTION':
            return 'field', value[0]

        if name == 'VARIABLE':
            return 'field', self.vars.get_reference('var', value[0])

        # TODO Fix very hacky property parsing
        # Need to redo variable system first?
        # Possibly also make a two pass system?
        if name == 'PROPERTY':
            vars_: naming.Variables = self.vars_dict.get(block['inputs']['OBJECT'][0])
            if not vars_:
                # logging.warning("Unkown sprite %s")
                return 'field', "var_" + sanitizer.clean_identifier(value[0])
            return 'field', vars_.get_local('var_', value[0])

        if name == 'LIST':
            return 'field', self.vars.get_reference('list', value[0])

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
                if self.blocks[value]['shadow']:
                    return 'value', \
                        self.blocks[value]['fields'].popitem()[1][0]

                # A block
                return 'blockid', value

        # 4-8 Number, 9-10 String, # 11 Broadcast
        if 4 <= value[0] <= 11:
            return 'value', value[1]

        # 12 Variable
        if value[0] == 12:
            return "any", self.vars.get_reference('var', value[1])

        # 13 List
        if value[0] == 13:
            return "string", self.vars.get_reference('var', value[1]) + ".join()"

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
        for name, identifier in self.targets.items():
            sprites.append(sanitizer.quote_field(name) + ": " + identifier)
        items = indent(',\n'.join(sprites), "    ")
        sprites_code = self.specmap.code(
            "sprites").format(items=items)

        # Create an if __name__ == '__main__' statement
        main_code = self.specmap.code("main")

        return sprites_code + "\n\n" + main_code
