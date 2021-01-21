"""

"""

import itertools
import json
import logging
import math
import re
import textwrap
from os import path

CONFIG_PATH = "data/config.json"
CONFIG = {
    "specmap_path": "data/specmap2.txt",
    "temp_folder": "temp"
}

LOWER_FIELDS = ('EFFECT')

# Used run directly
LOG_LEVEL = 40


def clean_identifier(text):
    """Makes an identifier valid by stripping invalid characters.
    Also strips % format codes used by custom blocks."""
    # Matches leading digits, % format codes, invalid characters, and __
    text = re.sub(r"(?a)(?:^([\d_]+))?((?<!\\)%[sbn]|\W|__)*?", "", text)
    if not text.isidentifier():
        logging.error("Failed to clean identifier '%s'", text)
    return text


def quote_string(text, quote="'"):
    """Escapes and quotes a string"""
    if quote == "'":
        return "'" + re.sub(r"()(?=\\|')", r"\\", text) + "'"
    if quote == '"':
        return '"' + re.sub(r'()(?=\\|")', r"\\", text) + '"'
    raise Exception("Invalid string quote")


def quote_or_num(value):
    """Either quotes a value or turns it into a number"""
    try:
        value = float(value)
        if value.is_integer():
            value = int(value)
        if math.isfinite(value):
            return str(int(value))
        return quote_string(str(value))
    except ValueError:
        return quote_string(value, '"')


def to_number(value):
    """Attempts to cast a value to a number"""
    if isinstance(value, str):
        try:
            value = float(value)
            if value.is_integer():
                value = int(value)
        except ValueError:
            return 0
    if value == float('NaN'):
        return 0
    return value


class Parser:
    """Main parse class"""

    hats = None
    blocks = None
    name = ""

    def __init__(self, sb3_json):
        # with open(path, 'r') as sb3_file:
        #     self.sb3 = json.load(sb3_file)
        self.sb3 = sb3_json

        # Creates the specmap dict
        # {'opcode': {'args': (), 'flags': "", 'switch': "", 'code': ""}}
        self.load_specmap(CONFIG['specmap_path'])

        self.broadcasts = Identifiers()
        self.variables = {}

    def load_specmap(self, spec_path):
        """Reads and parses the specmap file"""
        # Read the specmap file
        with open(spec_path, 'r') as file:
            specmap = file.read()

        # Parse the specmap file
        pattern = (
            r"(?s)#: ?(\w*?)?(?# type)"
            r" ?((?:\w|'|\^)+)(?# opcode) ?"
            r"(?:\(([\w, ]+)?\))?(?# args) ?"
            r"(?:-(\w+))?(?# flags)"
            r"(?:\n#\? ?([\w{}]+))?(?# switch)"
            r"\n(.+?)\n\n(?# code)")
        specmap = re.findall(pattern, specmap)

        # Create the specmap dict
        self.specmap = {}
        for block in specmap:
            args = {}
            self.specmap[block[1]] = {
                "return": block[0],
                "args": args,
                "flags": block[3],
                "switch": block[4],
                "code": block[5]
            }
            for arg in re.split(", ?", block[2]):
                arg = tuple(re.split(" +", arg))
                if len(arg) == 2:
                    args[arg[1]] = arg[0]
                elif len(arg) > 2:
                    print()

    def parse(self):
        """Parse the sb3 to python"""
        # Top of the file
        code = (
            '"""\nGenerated with sb3topy\n"""'
            "\nimport asyncio"
            "\nimport math"
            "\nimport random"
            "\nimport time"
            "\n\nimport pygame as pg"
            "\n\nimport engine"
            "\nfrom engine import List"
            "\nfrom engine import number, gt, lt, eq"
        )

        # Init variable Identifier handlers
        for target in self.sb3["targets"]:
            self.read_variables(target)

        t_names = Identifiers()
        for target in self.sb3["targets"]:
            # Get a unique name for the class
            target['identifier'] = t_names.get_cammel("Sprite", target['name'])

            # Parse the target
            code = code + self.parse_target(target)

        # Create the SPRITES dict and __main__
        code = code + "SPRITES = {"
        for target in self.sb3["targets"]:
            code = code + \
                f"\n    {quote_string(target['name'])}: {target['identifier']},"
        code = code + (
            "\n}\n\n"
            "if __name__ == '__main__':\n"
            "    engine.main(SPRITES)\n"
        )

        return code

    def parse_target(self, target):
        """Parse a sprite"""

        logging.info("Parsing target '%s'", target['name'])

        # Class function names
        self.hats = Identifiers()
        self.blocks = target.get('blocks', {})

        self.name = target['name']

        code = ""

        # Find block hats
        for block_id, block in self.blocks.items():
            # Verify the block is not a variable and is top level
            if isinstance(block, dict) and block.get('topLevel'):
                blockmap = self.specmap.get(block.get('opcode'))

                # Verify the block is a known hat
                if blockmap and 'h' in blockmap['flags']:
                    # Add a fake SUBSTACK to the hat to be parsed
                    block['inputs']['SUBSTACK'] = [2, block['next']]
                    block['next'] = None

                    # Parse the block
                    line = self.parse_stack(block_id, target['blocks'])

                    # If the function is empty, add pass
                    if len(line.strip().split('\n')) == 1:
                        line = line + "    pass"

                    # Indent the code
                    code = code + textwrap.indent(line, '    ') + '\n'

                    # Fails with custom blocks
                    # Indent the code and verify it is a function
                    # if line.strip().startswith("async def"):
                    #     code = code + textwrap.indent(line, '    ') + '\n'
                    # else:
                    #     raise Exception("Invalid function")

                else:
                    logging.info("Skipping top level block '%s' with opcode '%s'",
                                 block_id, block['opcode'])

        if len(code.strip().split('\n')) == 1:
            code = code + '\n    pass\n'

        # Add the top of the code
        top = f"\n\nclass {target['identifier']}(engine.Target):"

        # Add sprite info (costumes, etc.)
        top = top + textwrap.indent(self.parse_info(target), '    ')

        # Add the __init__ function
        top = top + textwrap.indent(self.create_init(target), '    ')

        return top + code

    def read_variables(self, target):
        """Initializes the Identifier for a Sprite"""
        self.name = target['name']
        if target.get('isStage'):
            self.name = "Stage"

        self.variables[self.name] = Identifiers()

        for var in target.get('variables', {}).values():
            self.variables[self.name].get_existing("var_" + var[0])

        for lst, _ in target.get('lists', {}).values():
            self.variables[self.name].get_existing("list_" + lst)

    def parse_info(self, target):
        """Gets costume info"""
        # TODO!! Validate asset details

        # Costumes string
        costumes = "costumes = ["
        for costume in target.get('costumes', []):
            # TODO Support for svg conversion
            path = costume.get('md5ext', '')
            name = costume.get('name', '')
            scale = costume.get('bitmapResolution', 1)

            center = (
                costume.get('rotationCenterX'),
                costume.get('rotationCenterY')
            )
            if center[0] is None or center[1] is None:
                center = None
            else:
                center = f"({center[0]}, {center[1]})"

            costumes = costumes + (
                "\n    {"
                f"\n        'name': \"{name}\","
                f"\n        'path': \"{path}\","
                f"\n        'center': {center},"
                f"\n        'scale': {scale}"
                "\n    },"
            )
        costumes = costumes + "\n]\n"

        # Sounds string
        sounds = "sounds = ["
        for sound in target.get('sounds', []):
            path = sound.get('md5ext', '')
            name = sound.get('name', '')

            sounds = sounds + (
                "\n    {"
                f"\n        'name': \"{name}\","
                f"\n        'path': \"{path}\""
                "\n    },"
            )
        sounds = sounds + "\n]\n"

        # Variables string
        variables = ""
        for var in target.get('variables', {}).values():
            variables = variables +\
                self.variables[self.name].get_existing("var_" + var[0], False) +\
                " = " + str(quote_or_num(var[1])) + "\n"

        lists = ""
        for name, values in target.get('lists', {}).values():
            lists = lists +\
                self.variables[self.name].get_existing(
                    "list_" + name, False) + " = List(\n"
            for value in values:
                lists = lists + "    " + str(quote_or_num(value)) + ",\n"
            lists = lists + ")\n\n"

        # Put it all together
        return (
            f"\ncostume = {target.get('currentCostume', 1) }"
            f"\nxpos, ypos = {target.get('x', 0)}, {target.get('y', 0)}"
            f"\ndirection = {target.get('direction', 90)}"
            f"\nvisible = {target.get('visible', True)}"
            f"\n\n{costumes}"
            f"\n{sounds}"
            f"\n\n{variables}"
            f"\n\n{lists}"
        )

    def create_init(self, target):
        """Creates the target __init__ saving hats"""
        code = "\ndef __init__(self, util):"
        code = code + "\n    self.hats = {"
        for hat, names in self.hats.specific.items():
            code = code + "\n        " + quote_string(hat) + ": ["
            for name in names[1]:
                code = code + "\n            self." + name + ","
            code = code + "\n        ],"

        code = code + (
            "\n    }"
            "\n    super().__init__(util)"
            f"\n    self.sprite._layer = {int(target.get('layerOrder'))}\n"
        )  # TODO Better layer parsing

        return code

    def parse_stack(self, blockid, input_type=None, end_yield=False):
        """
        Parses the block of blockid from blocks, and also any blocks
        which came "next" after it and any SUBSTACKS or conditions

        input_type is a type, such as string or stack, which is
        used to cast the end result of the block, if neccesary.

        emd_yield is used only if the input_type is stack. It indicates
        that the stack should yield at the end, such as with a loop.
        """

        code = ""  # Parsing results
        dirty = 0  # For set_dirty or _yield

        block = self.blocks.get(blockid)

        if not block:
            logging.warning("Failed to find block with uuid '%s'", blockid)

        while block:
            logging.debug("Parsing block '%s' with opcode '%s'",
                          blockid, block.setdefault('opcode'))

            # Get fields, used for blockmap switches
            parameters = self.get_fields(block)

            # Get the conversion map for the block
            blockmap = self.get_blockmap(blockid, parameters)

            # Check for dirty flags
            if 'd3' in blockmap['flags'] and dirty < 3:
                dirty = 3
            elif 'd2' in blockmap['flags'] and dirty < 2:
                dirty = 2
            elif 'd1' in blockmap['flags'] and dirty < 1:
                dirty = 1

            # Check if dirty needs to be set
            if 's' in blockmap['flags'] and dirty:
                code = code + self.specmap['special_dirty']['code'].format(
                    DIRTY=dirty) + '\n\n'
                dirty = 0

            # Add inputs to parameters
            self.get_inputs(parameters, block, blockmap)

            # Perform special parsing
            self.post_parse(parameters, block)

            # Get the block's converted code
            code = code + self.get_code(blockid, blockmap, parameters)
            if input_type == "stack":
                code = code + "\n"

            # Get the next block
            blockid = block['next']
            block = self.blocks.get(blockid)

        # Check if the parent block requires yielding
        if end_yield and input_type == "stack":
            code = code + \
                self.specmap['special_yield']['code'].format(
                    DIRTY=dirty) + "\n"

        # Check if dirty needs to be set
        elif dirty:
            code = code + \
                self.specmap['special_dirty']['code'].format(
                    DIRTY=dirty) + "\n"

        # Check if this block's value needs to be casted
        if blockmap['return'] != input_type:  # TODO block = None here
            code = self.cast_wrapper(code, input_type)

        return code

    def get_fields(self, block):
        """Gets, lowercases, and quotes fields from block"""
        parameters = {}
        fields = block.get('fields', {})
        for field, value in fields.items():
            # Get an existing broadcast name
            if field == "BROADCAST_OPTION":
                value = self.broadcasts.get_existing("broadcast_" + value[0])
                parameters[field] = value

            # Get an existing variable name
            elif field == "VARIABLE":
                value = "var_" + value[0]
                name = self.variables[self.name].get_existing(value, False)
                parameters["PREFIX"] = "self" if name else "util.stage"
                if not name:
                    name = self.variables['Stage'].get_existing(value)
                parameters["VARIABLE"] = name

            # Get an existing list name
            elif field == "LIST":
                value = "list_" + value[0]
                name = self.variables[self.name].get_existing(value, False)
                parameters["PREFIX"] = "self" if name else "util.stage"
                if not name:
                    name = self.variables['Stage'].get_existing(value)
                parameters["LIST"] = name

            elif field in ("PROPERTY", "OBJECT"):
                # These need to not be lowered/quoted
                parameters[field] = value[0]
                print(value[0])

            # CB Parameter
            elif block['opcode'] == "argument_reporter_string_number":
                parameters["VALUE"] = clean_identifier("arg_" + value[0])

            elif block['opcode'] == "argument_reporter_boolean":
                parameters["VALUE"] = clean_identifier("arg_" + value[0])

            else:
                value = value[0].lower()
                parameters[field] = quote_string(value)

        return parameters

    def get_blockmap(self, blockid, parameters):
        """Gets the block map or creates one for custom blocks"""
        # Get the block's blockmap
        block = self.blocks[blockid]
        opcode = block['opcode']
        blockmap = self.specmap.get(opcode)

        # Verify a blockmap was found
        if not blockmap:
            logging.warning(
                "No blockmap for block '%s' with opcode '%s'",
                blockid, opcode)
            blockmap = {
                "return": "",
                "args": {},
                "flags": "",
                "switch": "",
                "code": ""
            }

        # Check for a switch
        switch = blockmap['switch']
        blockmap = self.specmap.get(switch.format(
            **parameters).replace(" ", "_"), blockmap)

        # TODO Custom block support
        if opcode == "procedures_definition":
            blockmap = blockmap.copy()
            mutation = self.blocks[block['inputs']
                                   ['custom_block'][1]]['mutation']

            # TODO CB, var name conflicts
            blockmap['code'] = "async def " + clean_identifier(
                "cb_" + mutation['proccode']) + "(self, util," +\
                ', '.join(clean_identifier("arg_" + arg) for arg in json.loads(mutation['argumentnames'])) +\
                "):\n{SUBSTACK}"
            self.blocks[blockid]['inputs'].pop("custom_block")
            blockmap['flags'] = ""

        elif opcode == "procedures_call":
            mutation = block['mutation']
            blockmap['args'] = {
                name: 'any' for name in json.loads(mutation['argumentids'])}
            blockmap['code'] = "await self._warp(self." + \
                clean_identifier(
                    "cb_" + mutation['proccode']) + "(util, {PARAMETERS}))"
            #  + "(" + ', '.join(
            #     "{" + arg + "}" for arg in blockmap['args']
            # )

        elif opcode == "procedures_prototype":
            pass  # TODO handle procedures_prototype

        elif opcode == "argument_reporter_string_number":
            pass  # TODO Handle argument_reporter_string_number

        return blockmap

    def get_inputs(self, parameters, block, blockmap):
        """
        Parses inputs and adds them to parameters.

        Also verifies that all parameters expected by blockmap exist.
        """
        # TODO Missing parameters are not caught before an error
        # Maybe check before that all fields exist?
        for inp in block.get('inputs', ""):
            parameters[inp] = self.parse_input(
                block, blockmap, inp)

    def parse_input(self, block, blockmap, inp):
        """
        Parse the input of a block. If it is a block, it will be parsed.
        Returns value, is_block
        """
        # Get the expected input type
        itype = blockmap['args'].get(inp)

        # Get the input from the block
        value = block["inputs"][inp]

        # Handle possible block input
        if value[0] == 1:
            # Wrapper; block or value
            if isinstance(value[1], list):
                value = value[1]
            else:
                value = [2, value[1]]
        elif value[0] == 3:
            # Block covering a value
            value = [2, value[1]]

        # Handle a block
        if value[0] == 2:
            value = value[1]

            # Make sure it's not a variable
            if isinstance(value, str):
                if value in self.blocks:
                    # It is a valid block id
                    if self.blocks[value]["shadow"] and inp in self.blocks[value]["fields"]:
                        # The id points to a menu
                        value = quote_string(
                            self.blocks[value]['fields'][inp][0])
                    else:  # if inp in ["SUBSTACK", "SUBSTACK2"]:
                        # The id points to a block
                        return self.parse_stack(value, itype, 'y' in blockmap['flags'])
                elif value is not None:
                    # Empty block input
                    logging.warning("Invalid input block id '%s'", value)
                return value
            elif value is None:
                # Empty block
                return None

            # Else it is a variable/list, handled below

        # 4-8 = Number, 9-10 = String
        if 4 <= value[0] <= 9:
            # TODO! Some values are not properly quoted
            value = self.cast_value(value[1], itype)
        elif value[0] == 10:
            value = quote_string(str(value[1]))

        # Broadcast
        elif value[0] == 11:
            value = "broadcast_" + value[1]
            value = quote_string(
                self.broadcasts.get_existing(value))

        # Variable
        elif value[0] == 12:
            # TODO Variable selection by id
            value = "var_" + value[1]
            name = self.variables[self.name].get_existing(value, False)
            prefix = "self" if name else "util.stage"
            if not name:
                name = self.variables['Stage'].get_existing(value)
            value = self.specmap['data_variable']['code'].format(
                VARIABLE=name, PREFIX=prefix)
            value = self.cast_wrapper(value, itype)

        # List
        elif value[0] == 13:
            value = "list_" + value[1]
            name = self.variables[self.name].get_existing(value, False)
            prefix = "self" if name else "util.stage"
            if not name:
                name = self.variables['Stage'].get_existing(value)
            value = self.specmap['data_listcontents']['code'].format(
                LIST=name, PREFIX=prefix)

        # Unkown
        else:
            logging.error("Unexpected input type %i", value[0])
            value = value[1]

        return value

    def post_parse(self, parameters, block):
        """Perform block specific parsing"""
        if block['opcode'] == "sensing_of":
            name = parameters['OBJECT']
            if not name in self.variables:
                logging.warning(
                    "Block input to sensing_of OBJECT, guessing variable name")
                parameters['PROPERTY'] = self.get_variable(
                    None, parameters['PROPERTY'])
            else:
                parameters['PROPERTY'] = self.get_variable(
                    name, parameters['PROPERTY'])

    def get_variable(self, sprite, name):
        """Gets a variable name from a sprite"""
        # Try to get an existing variable name
        if sprite in self.variables:
            new_name = self.variables[sprite].get_existing(
                "var_" + name, False)
            if not new_name:
                logging.error(
                    "Unkown variable name '%s' for sprite '%s'",
                    name, sprite)
            return new_name

        # Guess the name, clean the identifier
        if sprite:
            logging.warning(
                "Unkown sprite '%s', guessing variable name", sprite)
        return clean_identifier("var_" + name)

    @staticmethod
    def cast_value(value, to_type):
        """Casts a value to a certain type"""
        if to_type == "string":
            return str(to_type)
        if to_type == "float":
            return to_number(value)
        if to_type == "intR":  # Rounded int
            return round(to_number(value))
        if to_type == "int":  # Floored int
            return int(to_number(value))
        return value  # Bool and any type don't require conversion

    @staticmethod
    def cast_wrapper(value, wrap_type):
        """Wraps an expression for runtime casting"""
        if wrap_type == "string":
            return "str(" + value + ")"
        if wrap_type == "float":
            return "number(" + value + ")"
        if wrap_type == "intR":
            return "round(number(" + value + "))"
        if wrap_type == "int":
            return "int(number(" + value + "))"
        return value

    def get_code(self, blockid, blockmap, parameters):
        """Generates a block's code from the blockmap and parsed parameters"""
        if self.blocks[blockid]['opcode'] == "procedures_call":
            # TODO str(parameter) should be done earlier
            parameters['PARAMETERS'] = ", ".join(
                str(parameters[arg]) for arg in blockmap['args'])

        for arg, itype in blockmap['args'].items():
            # Verify expected parameters are present
            if not arg in parameters:
                # TODO Empty if statements
                parameters[arg] = "None"
                logging.warning(
                    "Block '%s' with opcode '%s' missing '%s'",
                    blockid, self.blocks[blockid]['opcode'], arg)

            # Indent stacks
            if itype == "stack":
                if parameters[arg]:
                    parameters[arg] = textwrap.indent(parameters[arg], '    ')
                else:
                    parameters[arg] = "    pass"

        # Create the code
        code = blockmap['code'].format(**parameters)

        # If this is a hat, code is the base name
        if 'h' in blockmap['flags']:
            name = self.hats.get_unique(code)
            code = f"\nasync def {name}(self, util):\n{{SUBSTACK}}"
            code = code.format(**parameters)  # Insert substacks

        return code


class Identifiers:
    """
    Handles identifiers which cannot collide

    general - A dict of cleaned identifiers
        {
            cleaned: iterator_AZ
        }
    specific - A dict of unique identifiers
        {
            specific: (iterator_name19, [name, name1, ...])
        }
    modified - A set of all identifiers in use
        {name, name1, ...}

    Specific means the original name of an identifier
    General means the cleaned name of an identifier
    Modified mean the cleaned name made unique

    Example:
        specific name:
            broadcast 1
            broadcast 1*
        general name:
            broadcast1
            broadcast1
        modified name:
            broadcast1
            broadcast1A
    """

    def __init__(self):
        self.general = {}
        self.specific = {}
        self.modified = set()

    def get_unique(self, specific):
        """Gets a unique identifier from a specific (uncleaned) identifier"""
        # Check for an existing group
        # specific = clean_identifier(specific)
        iterator, names = self.specific.get(specific, (None, None))

        # Create a new group
        if not names:
            iterator, names = self._new_specific(specific)

        # Verify the name is unique
        modified = next(iterator)
        while modified in self.modified:
            modified = next(iterator)

        # Save the modified identifier
        names.append(modified)
        self.modified.add(modified)

        return modified

    def get_existing(self, specific, create_new=True):
        """
        Gets an existing identifier without modifying it

        This is mainly used for custom blocks which need to
        have the same name when being defined and called.
        """
        # Either get the first item of the names list
        modified = self.specific.get(specific)
        if modified:
            return modified[1][0]

        # Or create the list and return the name
        if create_new:
            return self.get_unique(specific)
        return None

    def get_cammel(self, pre, name):
        """
        Like get unique, but adds pre to the beginning of the name.

        Trys to combine in cammel case fashion, but will insert a _ if
        name starts with a lowercase letter.
        """

        if name[0].islower():
            return self.get_unique(pre + '_' + name)
        return self.get_unique(pre + name)

    def _new_specific(self, specific):
        """Sets up an iterator for a specific identifier"""
        # Clean the identifier
        general = clean_identifier(specific)

        # Iterator = A, B, ... AA, AB, ... ZZZZ
        iterator = self.general.get(general)
        if not iterator:
            self.general[general] = self._general_iterator()
            modified = general  # No need for a letter
        else:
            # Modify the cleaned name with a letter
            modified = general + '_' + next(iterator)

        # Return the tuple pair (iterator, names)
        return self.specific.setdefault(
            specific, (self._specific_iterator(modified), []))

    @staticmethod
    def _general_iterator():
        """
        Creates an iterator of this pattern:
            A, B, C, ... AA, AB, AC, ... ZZZY, ZZZZ
        This is used to create a diffrence between similar names,
            eg. broadcast_hi@! and broadcast_hi
        """
        return map(
            ''.join,
            itertools.chain.from_iterable(
                map(
                    lambda r: itertools.permutations(
                        "ABCDEFGHIJKLMNOPQRSTUVWXYZ", r),
                    range(1, 4)
                )
            )
        )

    @staticmethod
    def _specific_iterator(name):
        """
        Depending on if name ends with a digit, this will either be:
            name, name1, name2, name3 ...
        Or:
            name9, name9_1, name9_2, name9_3 ...
        """
        if name[-1].isdigit():
            return itertools.chain((name,), map(
                lambda n: name + '_' + str(n),
                itertools.count(1)))

        return itertools.chain((name,), map(
            lambda n: name + str(n),
            itertools.count(1)))


def main():
    """Main function"""
    logging.basicConfig(format="[%(levelname)s] %(message)s", level=LOG_LEVEL)

    if path.isfile(CONFIG_PATH):
        with open(CONFIG_PATH, 'r') as file:
            CONFIG.update(json.load(file))

    json_path = path.join(CONFIG['temp_folder'], "project.json")
    with open(json_path, 'r') as sb3_file:
        sb3_json = json.load(sb3_file)

    code = Parser(sb3_json).parse()

    output_path = path.join(CONFIG['temp_folder'], "project.py")
    with open(output_path, 'w') as code_file:
        code_file.write(code)


def parse(sb3_json, config):
    """Run the parser from a config file"""
    CONFIG.update(config)

    return Parser(sb3_json).parse()


if __name__ == '__main__':
    main()
