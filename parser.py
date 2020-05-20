"""

"""

import json
import re
import textwrap


def clean_identifier(text):
    """Makes an identifier valid"""
    text = re.sub(r"(\d|_)?(\W|__)?", "", text)
    if text.isidentifier():
        return text
    else:
        return ""


class Parser:
    """Main parse class"""

    queue = None
    hats = {}

    def __init__(self):
        with open("test2.json", 'r') as sb3_file:
            self.sb3 = json.load(sb3_file)

        # Gets a list of specmap tuples,
        # In the format (opcode, parameters, flags, code)
        with open("specmap.py", 'r') as map_file:
            text = map_file.read()
        specmap = re.findall(
            r"(?s)    def (\w+)\(self(?:, ([\w|, ]+))?\):(?:  # (\w+))?\n(?!\w+#)(.+?)\n\n", text)

        # Change format to opcode:(parameters, flags, code)
        self.specmap = {}
        for block in specmap:
            self.specmap[block[0]] = (block[1].split(
                ", "), block[2], textwrap.dedent(block[3]))

    def parse(self):
        """Parse the sb3 to python"""
        code = '"""\nGenerated with sb3topy\n"""\nimport asyncio\nimport math\
            \nimport random\n\nfrom engine import SpriteBase'

        for target in self.sb3["targets"]:
            code = code + self.parse_target(target)
        return code + '\n'

    def parse_target(self, target):
        """Parse a sprite"""
        # TODO Class name validation
        code = f"\n\nclass {clean_identifier(target['name'])}(SpriteBase):"

        for block in target["blocks"].values():
            if isinstance(block, dict) and block["topLevel"] and "proc" not in block["opcode"]:
                line = self.parse_script(block, target['blocks'])
                line = self.parse_script2(line)
                if len(line.strip().split('\n')) == 1:
                    line = line + "    pass"
                if line.strip().startswith("async def"):
                    code = code + textwrap.indent(line, '    ') + '\n'
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

            parameters = {}
            block, node = self.queue.pop()
            current = {'block': block, 'parameters': parameters,
                       'opcode': block['opcode']}

            # Parse fields
            for field, value in block['fields'].items():
                parameters[field] = value[0]  # TODO Field and input parsing

            # Parse inputs
            for inp in block['inputs']:
                parameters[re.escape(inp)] = self.parse_input(
                    block, inp, blocks)

            # Save the block if necesary
            if not node is False:
                node.append(current)

            # Add the next block to the queue
            if block['next']:
                self.queue.append((blocks[block['next']], node))

        return tree

    def parse_script2(self, tree):
        """Finishes parsing into python"""

        # Container, key
        self.queue = [(tree, 0)]
        #[(tree, key) for key, _ in enumerate(tree)]

        while self.queue:
            node, key = self.queue[-1]
            block = node[key]

            # Check if the parameters are fully parsed
            done = True
            for name, value in block['parameters'].items():
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
                        block['parameters'][name] = '\n'.join(value)

            if done:
                # Turn this block into a string
                self.queue.pop(-1)
                block_map = self.specmap.get(
                    block['opcode'], ([], '', f"{block['opcode']}"))
                code = block_map[2]

                # Hat blocks require special parsing
                if block_map[1] == 'h':
                    name = re.search(
                        f"def (.+?)_?{block_map[0][1]}", code).group(1)
                    block['parameters'][block_map[0][1]] = self.hats[name] =\
                        self.hats.get(name, 0) + 1
                    if len(block_map[0]) == 3:
                        block['parameters'][block_map[0][2]] = clean_identifier(
                            block['parameters'][block_map[0][2]])

                if block['parameters']:
                    # Indent the parameter code properly
                    for name, value in block['parameters'].items():
                        # if re.escape(name) != name:
                        #     block['parameters'].pop(name) # TODO Proc definitions
                        #     continue
                        # Get the indentation
                        indent = re.search(f"( +){(name)}", code)
                        if indent and len(indent.group(1)) > 1:
                            block['parameters'][name] = textwrap.indent(
                                value, indent.group(1))

                        # Substitute in the actual code
                        #code = re.sub(f"(?:  +)?({name})", str(value), code)

                    # Substitute in the parameters
                    code = re.sub(f"(?:  +)?({'(?!2)|'.join(block['parameters'].keys())}(?!2))",
                                  lambda match: str(block['parameters'].get(match.group(1), "pass")), code)

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
    parse = Parser()
    code = parse.parse()
    with open("result.py", 'w') as code_file:
        code_file.write(code)
    print()


if __name__ == '__main__':
    main()
