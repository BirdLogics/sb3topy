"""
codemap.py

Used to store and generate code snippets
"""

import logging
import re
from textwrap import indent

from .. import sanitizer
from ..targets import Target


def create_header(target: Target):
    """Creates code between "class ...:" and "def __init__" """

    comment = '"""Sprite ' + \
        sanitizer.quote_string(target['name']).strip('"') + '"""'

    return comment


def file_header():
    """Primarily contain imports for the file"""
    return (
        "import math\n"
        "import time\n\n"
        "import engine\n"
        "from engine import Target, sprite, warp\n"
        "from engine.lists import *\n"
        "from engine.block_events import *\n"
        "from engine.blockutil import *"
    )


def file_footer():
    """Creates the code at the end to run the program"""
    # Create an if __name__ == '__main__' statement
    return (
        "if __name__ == '__main__':\n"
        "    engine.start_program()"
    )


def create_init(target, assets):
    """Creates Python __init__ code for a target dict"""
    info = (
        "self._xpos = {xpos}\n"
        "self._ypos = {ypos}\n"
        "self._direction = {direction}\n"
        "self.shown = {visible}\n"
        "self.pen = engine.Pen(self)"
    ).format(
        xpos=target.get('x', 0),
        ypos=target.get('y', 0),
        direction=target.get('direction', 90),
        visible=target.get('visible', True)
    ) + "\n\n"

    costumes = parse_costumes(target, assets) + "\n\n"
    sounds = parse_sounds(target) + "\n\n"

    vars_init = parse_variables(target) + "\n\n"
    lists_init = parse_lists(target) + "\n"

    init_code = info + costumes + sounds + vars_init + lists_init

    return (
        "def __init__(self, parent=None):\n"
        "    super().__init__(parent)\n"
        "    if parent is not None:\n"
        "        return\n\n"
        "{init_code}\n"
        "    self.sprite.layer = {layer}"
    ).format(
        init_code=indent(init_code, "    "),
        layer=int(target['layerOrder'])
    )


def target_class(code, name, clean_name):
    """Creates the class code for a Target"""
    return (
        "@sprite({name})\n"
        "class {ident}(Target):\n"
        "{code}"
    ).format(
        code=indent(code, "    "),
        name=sanitizer.quote_field(name),
        ident=clean_name
    )


def parse_costumes(target, assets):
    """Creates code to init costumes for a target"""
    costumes = []

    # Create a dict str for each costume
    for costume in target['costumes']:
        name = sanitizer.quote_string(costume['name'])

        # Get the validated and modified md5ext from assets
        if costume['md5ext'] not in assets:
            logging.error("Missing costume asset '%s'", costume['md5ext'])
            costumes.append("{'name': " + name + "}")
            continue
        md5ext = assets[costume['md5ext']] or costume['md5ext']

        # Get the bitmap scale for converted svgs
        if "-svg" in md5ext:
            scale = int(re.search(r"-svg-(\d+)x", md5ext)[1])
        else:
            scale = int(costume['bitmapResolution'])

        # Create the costume dict
        costumes.append((
            "{{\n"
            "    'name': {name},\n"
            "    'path': {path},\n"
            "    'center': {center},\n"
            "    'scale': {scale}\n"
            "}}"
        ).format(
            name=name,
            path=sanitizer.quote_string(md5ext),
            center=(
                int(costume['rotationCenterX']),
                int(costume['rotationCenterY'])
            ),
            scale=scale
        ))

    # Create the costumes list string
    costumes = "[\n" + \
        indent(',\n'.join(costumes), "    ") + "\n]"

    return (
        "self.costume = engine.Costumes(\n"
        "   {costume}, {size}, {rotation}, {costumes})"
    ).format(
        costume=int(target['currentCostume']),
        size=target.get('size', 100),
        rotation=sanitizer.quote_string(target.get('rotationStyle')),
        costumes=costumes
    )


def parse_sounds(target: Target):
    """Creates code to init sounds for a target"""
    sounds = []

    # Create a dict string for each sound
    for sound in target['sounds']:
        name = sanitizer.quote_string(sound['name'])

        # Validate the sound path
        if not sanitizer.valid_md5ext(sound['md5ext']):
            logging.error(
                "Invalid sound format or path '%s'", sound['md5ext'])
            sounds.append("{'name': " + name + "}")
            continue

        sounds.append((
            "{{\n"
            "    'name': {name},\n"
            "    'path': {path}\n"
            "}}"
        ).format(
            name=name,
            path=sanitizer.quote_string(sound['md5ext'])
        ))

    # Create the sounds list string
    sounds = "[\n" + indent(',\n'.join(sounds), "    ") + "\n]"

    return (
        "self.sounds = engine.Sounds(\n"
        "    {volume}, {sounds})"
    ).format(
        volume=int(target['volume']),
        sounds=sounds
    )


def parse_variables(target: Target):
    """Creates code to init variables for a target and clones"""
    vars_init = []

    for var in target['variables'].values():
        name = target.vars.get_local('var', var[0])
        vars_init.append(
            "self.{name} = {value}".format(
                name=name,
                value=sanitizer.quote_number(var[1])
            ))

    return '\n'.join(vars_init).rstrip()


def parse_lists(target: Target):
    """Creates code to init lists for a target and clones"""
    list_init = []

    # Used for duplicate detection
    lists = {}

    for lst in target['lists'].values():
        # Hack for duplicate lists
        if lst[0] in lists and lists[lst[0]] and not lst[1]:
            continue
        lists[lst[0]] = lst[1]

        # Validate list items
        items = []
        for value in lst[1]:
            items.append(sanitizer.quote_number(value))

        # Get the list Variable object
        var = target.vars.get_var('list', lst[0])
        list_class = 'BaseList' if var.is_modified else 'StaticList'
        logging.debug("Treating list '%s' as %s", var.clean_name, list_class)

        # Create code to initialize the list
        list_init.append((
            "self.{name} = {class_}(\n"
            "{items}\n"
            ")"
        ).format(
            name=var.clean_name,
            items=indent("[" + ', '.join(items) + "]", "    "),
            class_=list_class
        ))

    return "\n".join(list_init).rstrip()


def yield_():
    """Returns the code for a yield"""
    return "await self.yield_()"
