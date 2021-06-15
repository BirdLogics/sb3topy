"""
naming.py

Handles the naming of:
sprites
hats & broadcasts
variables / lists
prototypes (custom blocks)
"""

import itertools
import logging
from time import monotonic_ns

from sbparser import clean_identifier

from . import sanitizer


class Sprites:
    """
    Handles sprite class naming

    sprites - An instance of Identifiers
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

    events - Class attribute, an Identifiers
        instance used to get safe event names

    identifiers - An identfiers instance used to get safe hat identifiers
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
    def get_event(cls, name, args):
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

    def name_hat(self, name, args):
        """Gets an safe, unique identifier for a hat"""
        event = self.get_event(name, args)
        return self.get_identifier(event)

    def event_items(self):
        """A generator returning event names and functions"""
        for event, cleaned in self.events.dict.items():
            if cleaned in self.identifiers.dict:
                yield event.lower(), self.identifiers.dict[cleaned]


class Variables:
    """
    Handles variable and list naming

    global_vars - Class attribute, a dict linking global variable names to safe identifiers

    global_idents - Class attribute, a set containing all global variable identifiers

    local_vars - A dict linking local variable names to safe identifiers

    local_idents - A set containing all local variable identifiers

    """
    global_vars = None

    def __init__(self, is_stage=False):
        if self.global_vars is None:
            Variables.global_vars = Identifiers()

        if is_stage:
            self.local_vars = self.global_vars
        else:
            self.local_vars = Identifiers()

    def get_reference(self, prefix, name):
        """
        Gets a variable reference,
        eg. self.var_x or util.sprites.stage.var_x
        """
        # Ensure the name starts with the prefix
        if not name.startswith(prefix):
            name = prefix + '_' + name

        # Check if a local variable exists with the name
        if name in self.local_vars.dict:
            return "self." + self.local_vars.dict[name]

        # Check if a global variable exists with the name
        if name in self.global_vars.dict:
            return "util.sprites.stage." + self.global_vars.dict[name]

        # This should not occur, but can be handled
        logging.warning("Unregistered var '%s'", name)

        # Create a new local variable
        return "self." + self.create_local('', name)

    def get_local(self, prefix, name):
        """
        Gets the identifier for a local variable
        No self. prefix is added.
        """
        # Ensure the name starts with the prefix
        if not name.startswith(prefix):
            name = prefix + '_' + name

        # Check if a local variable exists with the name
        if name in self.local_vars.dict:
            return self.local_vars.dict[name]

        # This should not normally occur, but can be handled
        logging.warning("Unregistered local var '%s'", name)

        # Create a new local variable
        return self.create_local('', name)

    def create_local(self, prefix, name):
        """Creates a safe identifier name"""
        # Ensure the name starts with the prefix
        if not name.startswith(prefix):
            name = prefix + '_' + name

        # Verify the variable doesn't already exist
        if name in self.local_vars.dict:
            logging.warning("Duplicate local var '%s'", name)
            return self.local_vars.dict[name]

        # Remove invalid characters
        ident = sanitizer.clean_identifier(name)

        # Ensure the identifier is unique
        ident = self.local_vars.suffix(ident)

        # Save the identifier for future use
        self.local_vars.dict[name] = ident

        return ident


class Prototype:
    """
    Represents a custom block

    TODO Unittest to verify args_list() uses cleaned names
    """

    def __init__(self, name, warp, args, args_id):
        self.name = name
        self.warp = warp
        self.args = args
        self.args_id = args_id

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


class Prototypes:
    """
    Handles the naming of custom blocks and their arguments

    TODO Remove arg referencing by id?
    """

    def __init__(self, events: Events):
        self.events = events
        self.prototypes = {}
        self.prototypes_id = {}

    def add_prototype(self, blockid, proccode, warp, args):
        """Names, saves, and returns a prototype"""
        # Get a clean prototype name
        cb_name = self.events.get_event(
            "cb_{name}", {'name': sanitizer.strip_pcodes(proccode)})

        # Get clean argument names
        arg_names = Identifiers()
        arg_ids = {}
        for id_, arg_name in args:
            # Prefix the argument name
            if not arg_name.startswith('arg'):
                new_name = "arg_" + arg_name
            else:
                new_name = arg_name

            # Remove invalid characters
            new_name = clean_identifier(new_name)

            # Ensure the name is unique
            new_name = arg_names.number(new_name)

            # Save the name by original name
            arg_names.dict[arg_name] = new_name

            # Save the name by arg id
            arg_ids[id_] = new_name

        # Create the protype tuple
        prototype = Prototype(cb_name, bool(warp), arg_names.dict, arg_ids)

        # Save the tuple by proccode and blockid
        self.prototypes[proccode] = prototype
        self.prototypes_id[blockid] = prototype

        return prototype

    def get_definition(self, blockid) -> Prototype:
        """Gets a prototype by blockid"""
        return self.prototypes_id[blockid]

    def from_proccode(self, proccode) -> Prototype:
        """Gets a prototype by proccode"""
        return self.prototypes[proccode]


class Identifiers:
    """
    Handles the naming of a set of identifiers

    dict - A dictionary linking original identifiers
        to their cleaned, safe variants

    set - A set containing all cleaned, unique identifiers
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
            if not name in self.set:
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
