"""
naming.py

Handles the naming of:
sprites
hats & broadcasts
prototypes (custom blocks)

TODO Move prototypes to new file
"""

import itertools
import logging

from . import sanitizer

logger = logging.getLogger(__name__)


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
        logger.warning("Unregistered sprite '%s'", name)

        return self.create_identifier(name)

    def create_identifier(self, name):
        """Creates an identifier for a sprite"""
        # Verify the identifier hasn't already been created
        if name in self.sprites.dict:
            logger.error("Duplicate sprite name '%s'", name)
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
