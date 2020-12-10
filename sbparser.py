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
        code = '"""\nGenerated with sb3topy\n"""\nimport asyncio\nimport math\
            \nimport random\nimport time\n\nimport engine'

        # Identifier names
        names = []

        for target in self.sb3["targets"]:
            # Get a unique name for the sprite class
            target['name'] = clean_identifier(target['name'])
            if target['name'] in names:
                target['name'] = target['name'] + \
                    str(names.count(target['name']))
            names.append(target['name'])

            # Parse the code
            code = code + self.parse_target(target)

        return code + '\n'

    def parse_target(self, target):
        """Parse a sprite"""

        logging.info("Parsing target '%s'", target['name'])

        # Top of the sprite
        code = f"\n\nclass {target['name']}(engine.Target):"

        # Class function names
        self.hats = []

        # Find block hats
        for block_id, block in target["blocks"].items():
            # Verify the block is not a variable and is top level
            if isinstance(block, dict) and block["topLevel"]:
                # Verify the block is a known hat
                block_map = self.specmap.get(block['opcode'])
                if block_map and 'h' in block_map['flags']:
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
            block_map = self.specmap.get(block['opcode'])
            if block['opcode'] == "procedures_definition":
                mutation = blocks[block['inputs']
                                  ['custom_block'][1]]['mutation']

                block_map['args'] = {
                    'PARAMETERS': ', '.join(json.loads(mutation['argumentnames'])),
                    'NAME': ""  # TODO Name
                }

            elif block['opcode'] == "procedures_call":
                mutation = block['mutation']
                block_map['args'] = json.loads(mutation['argumentids'])

            elif block['opcode'] == "procedures_prototype":
                pass  # TODO handle procedures_prototype

            elif block['opcode'] == "argument_reporter_string_number":
                pass  # TODO Handle argument_reporter_string_number

            elif 'c' in block_map['flags']:
                raise Exception("Unexpected custom block map flag.")

            if not block_map:
                logging.warning("Unrecognized opcode '%s'", block['opcode'])
                break  # TODO Better way to handle?

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
                    # Also tells substacks if they should yield at the end
                    parameters[inp] = self.parse_block(parameters[inp], blocks, inp.startswith(
                        'SUBSTACK') and 'y' in block_map['flags'])

            # Check if a diffrent map should be used based on parameters
            if block_map['switch']:
                block_map = self.specmap.get(
                    block_map['switch'].format(**parameters), block_map)

            # Hat blocks require special parsing
            if block_map['flags'] == 'h':
                # Clean the name
                name = clean_identifier(block_map['code'].format(**parameters))

                # Get a unique name
                if name in self.hats:
                    if code[-1] == '}':
                        name = name + "_"
                    self.hats.append(name)
                    name = name + str(self.hats.count(name))

                # Create the code
                code = f"\nasync def {name}(self, runtime):\n{{SUBSTACK}}"
            else:
                code = block_map['code']

            # Indent any substacks
            for name, value in parameters.items():
                if name[:8] == 'SUBSTACK':
                    if value:
                        parameters[name] = textwrap.indent(value, '    ')
                    else:
                        parameters[name] = "    pass"

            # Check if the block has substacks and
            # needs to set dirty before they run
            if 's' in block_map['flags']:
                code = self.specmap['special_dirty']['code'].format(
                    DIRTY=dirty) + '\n' + code

            # Parse custom block parameters
            if block['opcode'] == 'procedures_call':
                # Dicts are not ordered before Python 3.7 or CPython 3.6
                # Need to order parameters in a list and join them
                # def func(self, util, {PARAMETERS})
                parameters = {
                    'PARAMETERS':
                        ', '.join([parameters[id][1]
                                   for id in block_map['args']]),
                    'NAME': ''  # TODO Better identifier unique naming
                }

            # Verify that all expected parameters are parsed
            for name in block_map['args']:
                if name and not parameters.setdefault(name, ""):
                    logging.info("Block '%s' missing '%s'",
                                 block_id, name)
            # parameters.keys() ^ block_map['parameters']

            # Substitute in parameters
            code = code.format(**parameters)

            # Get the next block to parse
            block_id = block['next']
            block = blocks.get(block_id)

        # return '\n' + tree[0] + textwrap.indent('\n'.join(tree[1:]), '    ')

            entire_code = entire_code + code + '\n'
        # Check if dirty needs to be set
        if dirty:
            # Check if the parent block needs to yield
            if end_yield:
                entire_code = entire_code + \
                    self.specmap['special_yield']['code'].format(DIRTY=dirty)
            else:
                entire_code = entire_code + \
                    self.specmap['special_dirty']['code'].format(DIRTY=dirty)

        return entire_code

    def parse_script(self, block, blocks):
        """Parses a script from the top block down"""
        # block, block_map, code

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

                block_map = self.specmap.get(block['opcode'])

                if not block_map:
                    continue

                # Check if a diffrent block should be used
                if block_map['switch']:
                    block_map = self.specmap.get(
                        block_map['switch'].format(**block['args']), block_map)

                code = block_map['code']

                # Hat blocks require special parsing
                if block_map['flags'] == 'h':
                    name = clean_identifier(
                        code.format(**block['args']))
                    if name in self.hats:
                        if code[-1] == '}':
                            name = name + "_"
                        self.hats.append(name)
                        name = name + str(self.hats.count(name))
                    code = f"async def {name}(self, runtime):{{SUBSTACK}}"

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
        # block_map = self.specmap.get(block["opcode"], ('', '', ''))

        # if block_map[1] == 'h':
        #     line = block_map[2].split('"')[3]
        #     code = f"\n    async def {line}(self):\n"
        #     if not block["next"]:
        #         code = code + "        pass\n"

        #     while block and block["next"]:
        #         block = target["blocks"][block["next"]]
        #         block_map = self.specmap.get(block["opcode"], None)
        #         if not block_map:
        #             continue

        #         code = code + block_map[2] + "\n"

    def parse_input(self, block, inp, blocks):
        """Parse the input of a block"""
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
        return quote_string(block['fields'][field][0])


def main():
    """Main function"""
    logging.basicConfig(format="[%(levelname)s] %(message)s", level=20)
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
