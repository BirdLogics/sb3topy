"""
naming.py

Handles the naming of:
sprites
hats & broadcasts
prototypes (custom blocks)

TODO Move prototypes to new file
"""

import itertools
import json
import logging
from time import monotonic_ns
from typing import Dict

from .. import config
from . import sanitizer, specmap


class Identifiers:
    """
    Handles the naming of a set of identifiers.

    Attributes:
        dict: A dictionary linking original identifiers to their
            cleaned, safe variants.

        set: A set containing all cleaned, unique identifiers.
    """

    def __init__(self):
        self.dict = {}
        self.set = set()

    def suffix(self, ident):
        """
        Creates an unique identifier which is not in the internal set.
        To make the identifier unique, a letter is appended to it.
        The new unique identifier is then added to the internal set.
        """
        for suffix in self._letter_iter():
            if not ident + suffix in self.set:
                self.set.add(ident + suffix)
                return ident + suffix

        raise Exception("_letter_iter empty")  # impossible

    def number(self, ident, start=0):
        """
        Creates a unique identifier which is not in the internal set.
        To make the identifier unique, a number is appended to it.
        The new unique identifier is then added to the internal set.
        """
        # If the identifier ends with a number, add an underscore
        sep = '_' if ident[-1].isdigit() else ''

        # Add a unique
        for suffix in itertools.count(start):
            # Don't append anything when suffix = 0
            name = ident + sep + str(suffix) if suffix else ident

            # Return when the suffix makes the name unique
            if name not in self.set:
                self.set.add(name)
                return name

        raise Exception("itertools.count empty")  # impossible

    @staticmethod
    def _letter_iter():
        """
        Creates an iterator of this pattern:
            '', 'A', 'B', 'C', ... 'AA', ... 'AZZ', ...
        """
        return map(
            ''.join,
            itertools.chain.from_iterable(
                map(
                    lambda r: itertools.permutations(
                        "ABCDEFGHIJKLMNOPQRSTUVWXYZ", r),
                    itertools.count()
                )
            )
        )


class Sprites:
    """
    Handles sprite class naming.

    sprites: An instance of Identifiers.
    """

    def __init__(self):
        self.sprites = Identifiers()

    def get_sprite(self, name):
        """Gets or creates an identifier for the sprite"""
        # Verify the identifier has been created
        if name in self.sprites.dict:
            return self.sprites.dict[name]

        # This should not occur, but can be handled
        logging.warning("Unregistered sprite '%s'", name)

        return self.create_identifier(name)

    def create_identifier(self, name):
        """Creates an identifier for a sprite"""
        # Verify the identifier hasn't already been created
        if name in self.sprites.dict:
            logging.error("Duplicate sprite name '%s'", name)
            return self.sprites.dict[name]

        # Remove invalid characters
        ident = sanitizer.clean_identifier(name)

        # Ensure the identifier starts with 'Sprite'
        if not (ident.startswith('Sprite') or ident == 'Stage'):
            ident = "Sprite" + ident

        # Ensure the identifier is unique
        ident = self.sprites.suffix(ident)

        # Save the identifier for future use
        self.sprites.dict[name] = ident

        return ident

    def items(self):
        """Returns the items iterator of the internal dict"""
        return self.sprites.dict.items()


class Events:
    """
    Gets hat identifiers based on event names

    Event names must be clean and unique. Identifiers are made by
    appending a unique number to the end of the corresponding event.

    This class also handles assigning safe event names to broadcasts.

    Class Attributes,
        events: An Identifiers instance used to safely name events

    Attributes:
        identifiers: An identfiers instance used to safely name hats
    """

    events = None

    def __init__(self):
        if Events.events is None:
            Events.events = Identifiers()
        self.identifiers = Identifiers()

    def get_identifier(self, event):
        """Gets a safe, unique identifier from an event"""
        # Get the list of identifiers tied to the event
        identifiers = self.identifiers.dict.setdefault(event, [])

        # Get a unique identifier by appending an number
        ident = self.identifiers.number(event, len(identifiers))

        # Add the identifier to the list
        identifiers.append(ident)

        return ident

    @classmethod
    def clean_event(cls, name, args):
        """Gets a safe, unique event name for a hat"""
        # Seperate the text into two parts
        prefix, *text = name.partition('{')

        # Format the right part using args
        text = ''.join(text).format(**args)

        # Prepend the left part if it isn't already
        if not text.startswith(prefix.rstrip('_')):
            text = prefix + text

        # Check if a safe name has already been created
        if text.lower() in cls.events.dict:
            return cls.events.dict[text.lower()]

        # Remove invalid characters
        event = sanitizer.clean_identifier(text)

        # Ensure the event name is unique
        event = cls.events.suffix(event)

        # Save the event so it can be used again
        cls.events.dict[text.lower()] = event

        return event

    @classmethod
    def get_event(cls, name, args):
        """Get a raw, uncleaned event name for a hat"""
        # Seperate the text into two parts
        prefix, *text = name.partition('{')

        # Format the right part using args
        text = ''.join(text).format(**args)

        # Prepend the left part if it isn't already
        if not text.startswith(prefix.rstrip('_')):
            text = prefix + text

        return text.lower()

    def name_hat(self, name, args):
        """Gets a safe, unique identifier for a hat"""
        event = self.clean_event(name, args)
        return self.get_identifier(event)

    def existing_hat(self, name, args):
        """Gets the existing safe, unique identifier of a hat"""
        event = self.clean_event(name, args)

        assert event in self.identifiers.dict, "Existing hat ident doesn't exist"
        assert len(self.identifiers.dict[event]
                   ) == 1, "Existing hat ident should be solo"

        return self.identifiers.dict[event][0]

    def event_items(self):
        """A generator returning event names and functions"""
        for event, cleaned in self.events.dict.items():
            if cleaned in self.identifiers.dict:
                yield event.lower(), self.identifiers.dict[cleaned]


class Prototype:
    """
    Represents a custom block

    TODO Unittest to verify args_list() uses cleaned names

    Attributes:
        name: The cleaned name of the prototype proccode

        warp: Whether the prototype has run without screen refresh set

        args: A dictionary linking original argument names to cleaned
            argument names. {orginal_name: clean_name}

        args_id: A dictionary linking argument ids to cleaned argument
            names. {arg_id: clean_name}


    """

    def __init__(self, target, mutation, clean_name):
        # Get information from the block
        proccode = mutation['proccode']
        warp = mutation['warp'] in (True, 'true')
        arg_ids = json.loads(mutation['argumentids'])
        arg_names = json.loads(mutation['argumentnames'])

        # Get clean argument names
        clean_names = Identifiers()
        clean_names_id = {}
        for id_, arg_name in zip(arg_ids, arg_names):
            # Prefix the argument name
            if not arg_name.startswith('arg'):
                new_name = "arg_" + arg_name
            else:
                new_name = arg_name

            # Remove invalid characters
            new_name = sanitizer.clean_identifier(new_name)

            # Ensure the name is unique
            new_name = clean_names.number(new_name)

            # Save the name by original name
            clean_names.dict[arg_name] = new_name

            # Save the name by arg id
            clean_names_id[id_] = new_name

        self.name = clean_name
        self.warp = warp or config.WARP_ALL
        self.args = clean_names.dict
        self.args_id = clean_names_id

        self.arg_nodes = {name: target.digraph.add_node(
            ('proc_arg', target['name'], proccode, name)
        ) for name in clean_names_id.values()}
        self.arg_nodes_unclean = {
            unclean: self.arg_nodes[clean] for unclean, clean in self.args.items()}

    def get_arg(self, name):
        """Gets an argument identifier based on the name"""
        ident = self.args.get(name)
        if ident is None:
            logging.warning(
                "Unknown argument name '%s' for prototype '%s'", name, self.name)
            ident = "0"
        return ident

    def arg_from_id(self, argid):
        """Gets an argument identifier from the name"""
        ident = self.args_id.get(argid)
        if ident is None:
            logging.warning(
                "Unknown argument id '%s' for prototype '%s'", argid, self.name)
            ident = "arg" + str(monotonic_ns())
        return ident

    def args_list(self, sep=', '):
        """Returns cleaned arguments seperated by ', '"""
        return sep.join(self.args.values())

    def mark_called(self, target, block):
        """
        Saves the type of the calling block's arguments
        """

        for id_, value in block['inputs'].items():
            # Ignore unknown inputs not in the prototype
            arg_name = self.args_id.get(id_)
            if arg_name is not None:
                # Add the type of the input to the node
                input_type = specmap.get_input_type(target, value)
                self.arg_nodes[arg_name].add_type(input_type)

    def get_type(self, arg_name):
        """Gets the guessed type of an argument"""
        argid = self.args.get(arg_name)
        if argid is not None:
            return self.arg_nodes[argid].known_type

        logging.warning("Prototype '%s' missing argument '%s",
                        self.name, arg_name)
        return None


class Prototypes:
    """
    Handles the naming and typing of custom blocks and their arguments

    Attributes:
        events: The Events instance used to name prototypes.

        prototypes: A dictionary linking prototype proccodes to their
            Prototype instances. {proccode: prototype_instance}

        prototypes_id: A dictionary linking the blockids of prototypes
            to their Prototype instances. {blockid: prototype_instance}
    """

    def __init__(self, events: Events):
        self.events = events
        self.prototypes: Dict[str, Prototype] = {}
        self.prototypes_id: Dict[str, Prototype] = {}

    def add_prototype(self, target, mutation, blockid):
        """Names, saves, and returns a prototype"""
        # Get a clean prototype name
        proccode = mutation['proccode']
        clean_name = self.events.clean_event(
            "my_{name}", {'name': sanitizer.strip_pcodes(proccode)})

        # Create the protype tuple
        prototype = Prototype(target, mutation, clean_name)

        # Save the tuple by proccode and blockid
        self.prototypes[proccode] = prototype
        self.prototypes_id[blockid] = prototype

        return prototype

    def get_definition(self, blockid) -> Prototype:
        """Gets a prototype by blockid"""
        return self.prototypes_id[blockid]

    def from_proccode(self, proccode):
        """Gets a prototype by proccode"""
        return self.prototypes.get(proccode)

    def mark_called(self, target, block):
        """Runs type guessing for a procedure call"""
        prototype = self.from_proccode(block['mutation']['proccode'])
        if prototype:
            prototype.mark_called(target, block)

    def get_arg_node(self, target, block):
        """
        Gets a type node given the name of a proc arg. If no node is
        found, returns 'any'

        If mulitple prototypes have the same arg name, also figures
        out which custom block the proc arg is used in.
        """

        name = block['fields']['VALUE'][0]

        # Get all prototypes which have the arg by blockid
        protos = {blockid: prototype for blockid,
                  prototype in self.prototypes_id.items() if name in prototype.arg_nodes_unclean}

        # Verify at least one prototype was found
        if not protos:
            logging.warning("Unknown proc arg '%s'", name)

        # If only one was found, assume the arg belongs to it
        if len(protos) == 1:
            return protos.popitem()[1].arg_nodes_unclean[name]

        # Get the hat block parent above the block
        hat_block = target.get_parent_hat(block)

        # If hat_block is None, this block isn't actually used
        if hat_block is None:
            return 'any'

        # If the hat is a procedure, get the arg node from it
        if hat_block['opcode'] == "procedures_definition":
            # Get the prototype blockid
            blockid = hat_block['inputs']['custom_block'][1]
            if blockid in protos:
                return protos[blockid].arg_nodes_unclean[name]

            # The prototype doesn't contain the arg
            logging.warning(
                "Unknown proc arg '%s' for prototype '%s'",
                name, self.prototypes_id[blockid].name)
            return 'any'

        logging.warning("Proc arg '%s' used outside of a custom block",
                        name)
        return 'any'
