"""

"""

import json
import re
import textwrap


def clean_identifier(text):
    """Makes an identifier valid"""
    text = re.sub(r"(?a)(?:^([\d_]+))?(\W|__)*?", "", text)
    if text.isidentifier():
        return text
    raise Exception("Failed to clean identifier")


def escape_string(text, quote="'"):
    """Escapes and quotes a string"""
    if quote == "'":
        return re.sub(r"()(?=\\|')", r"\\", text)
    if quote == '"':
        return re.sub(r'()(?=\\|")', r"\\", text)
    raise Exception("Invalid string quote")


class Block:
    """Represents a block being parsed"""
    code = ""  # Python representation
    args = {}  # Blocks and values


class Parser:
    """Main parse class"""

    queue = None
    targets = {}
    hats = []

    def __init__(self, path):
        with open(path, 'r') as sb3_file:
            self.sb3 = json.load(sb3_file)

        # Gets a list of specmap tuples,
        # In the format (opcode, parameters, flags, code)
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
        # Top of the sprite
        code = f"\n\nclass {target['name']}(SpriteBase):"

        # Class function names
        self.hats = []

        # Find block hats
        for block in target["blocks"].values():
            if isinstance(block, dict) and block["topLevel"]:
                # Parse the line
                line = self.parse_script(block, target['blocks'])

                # If the function is empty, add pass
                if len(line.strip().split('\n')) == 1:
                    line = line + "    pass"
                if line.strip().startswith("async def"):
                    code = code + textwrap.indent(line, '    ') + '\n'
                else:
                    raise Exception("Invalid function")
        if len(code.strip().split('\n')) == 1:
            code = code + '\n    pass\n'

        return code

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
        #[(tree, key) for key, _ in enumerate(tree)]

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
                    pass#print()

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
        if value[0] == 1:  # Wrapper; block or value
            if isinstance(value[1], list):
                value = value[1]
            else:
                value = [2, value[1]]
        elif value[0] == 3:  # Block covering a value
            value = [2, value[1]]
        if value[0] == 2:  # Block
            value = value[1]

            if not isinstance(value, list):  # Make sure it's not a variable
                if value in blocks:
                    blockid = value
                    if blocks[blockid]["shadow"] and inp in blocks[blockid]["fields"]:
                        # It's probably be a menu
                        value = f"'{blocks[blockid]['fields'][inp][0]}'"
                    else:  # if inp in ["SUBSTACK", "SUBSTACK2"]:
                        value = []
                        self.queue.append([blocks[blockid], value])

                elif value is None:
                    value = ""
                    # # Blank value in bool input is null in sb3 but false in sb2
                    # if not inp in ["SUBSTACK", "SUBSTACK2"]:
                    #     value = False

                return value

        # TODO Variables and lists, value[0] == 12 or 13
        if 4 <= value[0] <= 8:
            try:
                float(value[0])
            except ValueError:
                value[1] = f'"{value[1]}"'
        elif 9 <= value[0] <= 10:
            value[1] = f'"{value[1]}"'
        elif value[0] == 11:
            value[1] = clean_identifier(value[1])
        elif value[0] == 12:
            value[1] = f"self.variable['{value[1]}']"
        elif value[1] == 13:
            value[1] = f"self.lists['{value[1]}']"

        return value[1]  # + f" #{value[0]}"


def main():
    """Main function"""
    parse = Parser("test3.json")
    code = parse.parse()
    with open("result.py", 'w') as code_file:
        code_file.write(code)
    print()


if __name__ == '__main__':
    main()
