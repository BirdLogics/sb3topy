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
            r"(?s)#: ?(\w+)(?# opcode) ?"
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
        top = top + textwrap.indent(self.create_init(), '    ')

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
                f"\n        'scale': {scale},"
                f"\n        'center': {center}"
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
            f"\ncostume = {target.get('currentCostume', 1) - 1}"
            f"\n\n{costumes}"
            f"\n{sounds}"
        )

    def create_init(self):
        """Creates the target __init__ saving hats"""
        code = "\ndef __init__(self, util):"
        code = code + "\n    self.hats = {"
        for hat, names in self.hats.items():
            code = code + f"\n        '{hat}': ["
            for name in names:
                code = code + f"\n            self.{name},"
            code = code + "\n        ],"
        code = code + "\n    }\n    super().__init__(util)\n"

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
                    )

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
                    name = name + (code[-1] == '}' and '_') + str(len(names))
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

        elif 'c' in blockmap['flags']:  # TODO What is c flag for?
            raise Exception("Unexpected custom block map flag.")

        return blockmap

    def parse_script(self, block, blocks):
        """Parses a script from the top block down"""
        # block, blockmap, code

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

        # Container, key
        self.queue = [(tree, 0)]
        # [(tree, key) for key, _ in enumerate(tree)]

        while self.queue:
            node, key = self.queue[-1]
            block = node[key]

            # Check if the parameters are fully parsed
            done = True
            for name, value in block['args'].items():
                # Check if this is a value or script
                if isinstance(value, list):
                    # Ensure each block has been parsed
                    for key2, block2 in enumerate(value):
                        if isinstance(block2, dict):
                            # It hasn't, add to queue
                            self.queue.append((value, key2))
                            done = False
                    if done:
                        # Compile the parsed script into a single string
                        block['args'][name] = '\n'.join(value)
                else:
                    pass  # print()

            if done:
                # Turn this block into a string
                self.queue.pop(-1)

                if block['opcode'] == 'procedures_prototype':
                    print()

                blockmap = self.specmap.get(block['opcode'])

                if not blockmap:
                    continue

                # Check if a diffrent block should be used
                if blockmap['switch']:
                    blockmap = self.specmap.get(
                        blockmap['switch'].format(**block['args']), blockmap)

                code = blockmap['code']

                # Hat blocks require special parsing
                if blockmap['flags'] == 'h':
                    name = clean_identifier(
                        code.format(**block['args']))
                    if name in self.hats:
                        if code[-1] == '}':
                            name = name + "_"
                        self.hats.append(name)
                        name = name + str(self.hats.count(name))
                    code = f"async def {name}(self, util):{{SUBSTACK}}"

                # Indent the parameter code properly
                for name, value in block['args'].items():
                    if name[:8] == 'SUBSTACK':
                        block['args'][name] = textwrap.indent(
                            value, '    ')

                # Substitute in the parameters
                code = code.format(**block['args'])

                # Save the block
                node[key] = code
        return '\n' + tree[0] + textwrap.indent('\n'.join(tree[1:]), '    ')

        # code = ""
        # block = top_block
        # blockmap = self.specmap.get(block["opcode"], ('', '', ''))

        # if blockmap[1] == 'h':
        #     line = blockmap[2].split('"')[3]
        #     code = f"\n    async def {line}(self):\n"
        #     if not block["next"]:
        #         code = code + "        pass\n"

        #     while block and block["next"]:
        #         block = target["blocks"][block["next"]]
        #         blockmap = self.specmap.get(block["opcode"], None)
        #         if not blockmap:
        #             continue

        #         code = code + blockmap[2] + "\n"

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
                value = float(value[0])
                if value.is_integer():
                    value = int(value)
            except ValueError:
                value[1] = quote_string(value[1], '"')
        elif 9 <= value[0] <= 10:
            value[1] = quote_string(value[1], '"')

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

    def parse_field(self, block, field):
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
