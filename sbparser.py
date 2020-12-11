"""

"""


import json
# import keyword
import logging
import re
import shutil
import textwrap

JSON_PATH = "results/project.json"
OUTPUT_PATH = "results/result.py"
OUTPUT_FOLDER = "results"

LOWER_FIELDS = ('EFFECT')


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


class Parser:
    """Main parse class"""

    queue = None
    targets = {}
    dirty = 0
    hats = []

    def __init__(self, path):
        with open(path, 'r') as sb3_file:
            self.sb3 = json.load(sb3_file)

        # Creates the specmap dict
        # {'opcode': {'args': (), 'flags': "", 'switch': "", 'code': ""}}
        self.load_specmap("specmap2.txt")

    def load_specmap(self, path):
        """Reads and parses the specmap file"""
        # Read the specmap file
        with open(path, 'r') as file:
            specmap = file.read()

        # Parse the specmap file
        pattern = (
            r"(?s)#: ?((?:\w|')+)(?# opcode) ?"
            r"(?:\(([\w, ]+)?\))?(?# args) ?"
            r"(?:-(\w+))?(?# flags)"
            r"(?:\n#\? ?([\w{}]+))?(?# switch)"
            r"\n(.+?)\n\n(?# code)")
        specmap = re.findall(pattern, specmap)

        # Create the specmap dict
        self.specmap = {block[0]: {
            "args": re.split(", ?", block[1]),
            "flags": block[2],
            "switch": block[3],
            "code": block[4]
        } for block in specmap}

    def parse(self):
        """Parse the sb3 to python"""
        # Top of the file
        code = (
            '"""\nGenerated with sb3topy\n"""'
            "\nimport asyncio"
            "\nimport math"
            "\nimport random"
            "\nimport time"
            "\n\nimport engine"
        )

        # Identifier names
        names = []

        # Parse each individual target
        for target in self.sb3["targets"]:
            # Get a unique name for the class
            target['name'] = clean_identifier(target['name'])
            if target['name'] in names:
                target['name'] = target['name'] + \
                    str(names.count(target['name']))
            names.append(target['name'])

            # Parse the target
            code = code + self.parse_target(target)

        # Create the __main__ statement
        run = "SPRITES = {"
        for name in names:
            run = run + f"\n    '{name}': {name},"
        run = run + (
            "\n}\n\n"
            "if __name__ == '__main__':\n"
            "    engine.main(SPRITES)\n"
        )

        return code + run

    def parse_target(self, target):
        """Parse a sprite"""

        logging.info("Parsing target '%s'", target['name'])

        # Class function names
        self.hats = {}

        code = ""

        # Find block hats
        for block_id, block in target["blocks"].items():
            # Verify the block is not a variable and is top level
            if isinstance(block, dict) and block["topLevel"]:
                # Verify the block is a known hat
                blockmap = self.specmap.get(block['opcode'])
                if blockmap and 'h' in blockmap['flags']:
                    # Add a fake SUBSTACK to the hat to be parsed
                    block['inputs']['SUBSTACK'] = [2, block['next']]
                    block['next'] = None

                    # Parse the block
                    line = self.parse_block(block_id, target['blocks'])

                    # If the function is empty, add pass
                    if len(line.strip().split('\n')) == 1:
                        line = line + "    pass"

                    # Indent the code and verify it is a function
                    if line.strip().startswith("async def"):
                        code = code + textwrap.indent(line, '    ') + '\n'
                    else:
                        raise Exception("Invalid function")

                else:
                    logging.debug("Skipping top level block '%s' with opcode '%s'",
                                  block_id, block['opcode'])

        if len(code.strip().split('\n')) == 1:
            code = code + '\n    pass\n'

        # Add the top of the code
        top = f"\n\nclass {target['name']}(engine.Target):"

        # Add sprite info (costumes, etc.)
        top = top + textwrap.indent(self.parse_info(target), '    ')

        # Add the __init__ function
        top = top + textwrap.indent(self.create_init(target), '    ')

        return top + code

    @staticmethod
    def parse_info(target):
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

        # Put it all together
        return (
            f"\ncostume = {target.get('currentCostume', 1) }"
            f"\nxpos, ypos = {target.get('x', 0)}, {target.get('y', 0)}"
            f"\ndirection = {target.get('direction', 90)}"
            f"\nvisible = {target.get('visible', True)}"
            f"\n\n{costumes}"
            f"\n{sounds}"
        )

    def create_init(self, target):
        """Creates the target __init__ saving hats"""
        code = "\ndef __init__(self, util):"
        code = code + "\n    self.hats = {"
        for hat, names in self.hats.items():
            code = code + f"\n        '{hat}': ["
            for name in names:
                code = code + f"\n            self.{name},"
            code = code + "\n        ],"

        code = code + (
            "\n    }"
            "\n    super().__init__(util)"
            f"\n    self.sprite.layer = {int(target.get('layerOrder'))}\n"
        ) # TODO Better layer parsing

        return code

    def pre_parse_script(self, block, blocks):
        """Creates a queue to parse scripts in the correct order"""
        tree = []
        self.queue = [(block, tree)]

        block['inputs']['SUBSTACK'] = [2, block['next']]
        block['next'] = None

        while self.queue:
            # block - the sb3 json block
            # current - the parsed sb3 block
            # node - the list current is appended to
            # parameters - parsed inputs and fields

            args = {}
            block, node = self.queue.pop()
            current = {'block': block, 'args': args,
                       'opcode': block['opcode']}

            # TODO arg validation from map

            # Parse fields
            for field, value in block['fields'].items():
                args[field] = value[0]

            # Parse inputs
            for inp in block['inputs']:
                args[inp] = self.parse_input(block, inp, blocks)

            # Save the block if necesary
            if not node is False:
                node.append(current)

            # Add the next block to the queue
            if block['next']:
                self.queue.append((blocks[block['next']], node))

    def parse_block(self, block_id, blocks, end_yield=False):
        """Parses a block into string python code"""
        entire_code = ""
        dirty = 0

        block = blocks.get(block_id)

        if not block:
            logging.warning("Failed to find block with uuid '%s'", block_id)

        while block:
            logging.debug("Parsing block '%s' with opcode '%s'",
                          block_id, block['opcode'])

            parameters = {}

            # Get the conversion map for the block
            blockmap = self.get_blockmap(block, blocks)
            if not blockmap:
                logging.warning("Unrecognized opcode '%s'", block['opcode'])
                break  # TODO Better way to handle?

            # Check for dirty flags
            if 'i' in blockmap['flags'] and dirty < 3:
                dirty = 3
            elif 'r' in blockmap['flags'] and dirty < 2:
                dirty = 2
            elif 'd' in blockmap['flags'] and dirty < 1:
                dirty = 1

            # Parse fields
            for field in block['fields']:
                parameters[field] = self.parse_field(block, field)

            # Parse inputs
            for inp in block['inputs']:
                # Parse the input
                parameters[inp], is_block = self.parse_input(
                    block, inp, blocks)

                # If it is a block, recursivly parse it
                if is_block:
                    parameters[inp] = self.parse_block(
                        parameters[inp], blocks,

                        # Tell substacks if they need to yield
                        inp.startswith('SUBSTACK') and 'y' in blockmap['flags']
                    ).strip()

            # Use diffrent maps based on parameters
            if blockmap['switch']:
                blockmap = self.specmap.get(
                    blockmap['switch'].format(**parameters), blockmap)

            # Special hat block parsing
            if blockmap['flags'] == 'h':
                # Clean the name
                name = clean_identifier(blockmap['code'].format(**parameters))

                # TODO Improved duplicate identifier naming
                # Get a unique name
                self.hats.setdefault(name, [])
                names = self.hats[name]
                if names:
                    name = name + ('_' if blockmap['code'][-1] == '}' else '') + str(len(names))
                names.append(name)

                # Create the code
                code = f"\nasync def {name}(self, util):\n{{SUBSTACK}}"
            else:
                code = blockmap['code']

            # Indent any substacks
            for name, value in parameters.items():
                if name[:8] == 'SUBSTACK':
                    if value:
                        parameters[name] = textwrap.indent(value, '    ')
                    else:
                        parameters[name] = "    pass"

            # Dirty must be saved before substack blocks run
            if 's' in blockmap['flags'] and dirty:
                code = self.specmap['special_dirty']['code'].format(
                    DIRTY=dirty) + '\n' + code
                dirty = 0

            # Parse custom block parameters
            if block['opcode'] == 'procedures_call':
                # Dicts are not ordered before Python 3.7 or CPython 3.6
                # Need to order parameters in a list and join them
                # def func(self, util, {PARAMETERS})
                parameters = {
                    'PARAMETERS':
                        ', '.join([parameters[id][1]
                                   for id in blockmap['args']]),
                    'NAME': ''  # TODO CB Name
                }

            # Verify that all expected parameters exist
            for name in blockmap['args']:
                if name and not parameters.setdefault(name, ""):
                    logging.info("Block '%s' missing '%s'", blockmap, name)
            # parameters.keys() ^ blockmap['parameters']

            # Insert parameters into code
            code = code.format(**parameters)

            # Get the next block to parse
            block_id = block['next']
            block = blocks.get(block_id)

        # return '\n' + tree[0] + textwrap.indent('\n'.join(tree[1:]), '    ')

            entire_code = entire_code + code + '\n'

        # Check if the parent block requires yielding
        if end_yield:
            entire_code = entire_code + \
                self.specmap['special_yield']['code'].format(DIRTY=dirty)

        # Check if dirty needs to be set
        elif dirty:
            entire_code = entire_code + \
                self.specmap['special_dirty']['code'].format(DIRTY=dirty)

        return entire_code

    def get_blockmap(self, block, blocks):
        """Gets the block map or creates one for custom blocks"""

        # TODO Custom block support

        blockmap = self.specmap.get(block['opcode'])



        if block['opcode'] == "procedures_definition":
            mutation = blocks[block['inputs']['custom_block'][1]]['mutation']

            blockmap['args'] = {
                'PARAMETERS': ', '.join(json.loads(mutation['argumentnames'])),
                'NAME': ""  # TODO CB paramater NAME
            }

        elif block['opcode'] == "procedures_call":
            mutation = block['mutation']
            blockmap['args'] = json.loads(mutation['argumentids'])

        elif block['opcode'] == "procedures_prototype":
            pass  # TODO handle procedures_prototype

        elif block['opcode'] == "argument_reporter_string_number":
            pass  # TODO Handle argument_reporter_string_number

        # elif 'c' in blockmap['flags']:  # TODO What is c flag for?
        #     raise Exception("Unexpected custom block map flag.")

        return blockmap

    def parse_input(self, block, inp, blocks):
        """
        Parse the input of a block
        Returns value, is_block
        """
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
            if not isinstance(value, list):
                if value in blocks:
                    # It is a valid block id
                    if blocks[value]["shadow"] and inp in blocks[value]["fields"]:
                        # The id points to a menu
                        value = quote_string(blocks[value]['fields'][inp][0])
                    else:  # if inp in ["SUBSTACK", "SUBSTACK2"]:
                        # The id points to a block
                        return value, True
                elif value is not None:
                    # If None, it is an empty block input
                    logging.warning("Invalid input block id '%s'", value)
                return value, False

        # Handle numbers
        if 4 <= value[0] <= 8:
            try:
                value = float(value[1])
                if value.is_integer():
                    value = int(value)
            except ValueError:
                value = quote_string(value[1], '"')
        elif 9 <= value[0] <= 10:
            value = quote_string(value[1], '"')

        # Handle broadcast inputs
        elif value[0] == 11:
            value = clean_identifier(value[1])

        # Handle variables and lists
        elif value[0] == 12:
            value = self.specmap['data_variable']['code'].format(
                VARIABLE=quote_string(value[1]))
        elif value[1] == 13:
            # TODO Is list handling correct?
            value = self.specmap['data_listcontents']['code'].format(
                LIST=quote_string(value[1]))

        # Log other value types
        else:
            logging.error("Unexpected input type %i", value[0])
            value = value[1]

        return value, False

    @staticmethod
    def parse_field(block, field):
        """Parses the field to ensure compatibility"""
        # TODO Lowercase some fields?
        if field in LOWER_FIELDS:
            block['fields'][field][0] = block['fields'][field][0].lower()
        return quote_string(block['fields'][field][0])


def main():
    """Main function"""
    logging.basicConfig(format="[%(levelname)s] %(message)s", level=10)
    parse = Parser(JSON_PATH)
    code = parse.parse()

    # import timeit
    # print(timeit.timeit("parse.parse()", "parse = Parser('test2.json')", number=1000))

    with open(OUTPUT_PATH, 'w') as code_file:
        code_file.write(code)

    # Copy the engine
    shutil.copyfile("engine.py", OUTPUT_FOLDER + "/engine.py")

    print()


if __name__ == '__main__':
    main()
