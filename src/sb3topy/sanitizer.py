"""
sanitizer.py

Contains classes which handle naming and
functions which are useful for sanitization

TODO Make Identfiers a base class for specialized classes
TODO Make broadcast identifers retain case
Perhaps make an case insensitive event list used to
obtain the capitilization of the first event discovered


Handles the naming of:
sprites
hats & broadcasts
variables / lists
prototypes (custom blocks)
"""

import itertools
import logging
import math
import re


def clean_identifier(text, default='identifier'):
    """Strips invalid character from an identifier"""
    # TODO Keep preluding underscores?
    cleaned = re.sub((
        r"(?a)(?:^([\d_]+))?"  # Preluding digits and _
        r"((?<!\\)%[sbn]|\W|__)*?"  # Other invalid characters
    ), "", text)

    if not cleaned:
        logging.warning("Stripped all characters from identifier '%s'")
        cleaned = default

    if not cleaned.isidentifier():
        logging.error("Failed to clean identifier '%s'", text)
        return "identifier"

    return cleaned


def quote_string(text):
    """Double "quotes" text"""
    return '"' + re.sub(r'()(?=\\|")', r"\\", str(text)) + '"'


def quote_field(text):
    """Single 'quotes' text"""
    return "'" + re.sub(r"()(?=\\|')", r"\\", str(text)) + "'"


def quote_number(text):
    """
    Does not quote valid ints, but
    does quote everything else.

    Used to sanitize a value which may contain
    a large int which doesn't need quotes
    """
    try:
        if str(int(str(text))) == str(text):
            return str(text)
        return quote_string(text)
    except ValueError:
        try:
            if str(float(str(text))) == str(text):
                int(float(str(text)))
                return str(text)
            return quote_string(text)
        except ValueError:
            return quote_string(text)
        except OverflowError:
            return quote_string(text)


def cast_number(value, default=0):
    """Casts a value to a number"""
    # Get number or return default
    try:
        value = float(value)

        if value.is_integer():
            return int(value)
        if math.isnan(value):
            return default

        return value

    except ValueError:
        try:
            return int(value, base=0)
        except ValueError:
            return default


def valid_md5ext(md5ext):
    """Verifies a md5ext path is valid"""
    return re.fullmatch(r"[a-z0-9]{32}\.[a-z3]{3}", md5ext) is not None


def strip_pcodes(text):
    """Strips % format codes from a proccode"""
    return re.sub(
        r"(?<!\\)%[sbn]",
        "", text
    )


def cast_value(value, to_type):
    """
    Casts a value to a type
    Always returns a string
    """
    if to_type == "string":
        return quote_string(value)

    if to_type == "float":
        return str(cast_number(value))

    if to_type == "int":
        return str(round(cast_number(value)))

    if to_type == "bool":
        return str(bool(value))

    if value in (True, False, None):
        return str(value)
    return str(quote_number(value))


def cast_wrapper(value, to_type):
    """Puts a runtime cast wrapper around code"""
    if to_type == 'string':
        return "str(" + value + ")"

    if to_type == 'int':
        return "toint(" + value + ")"

    if to_type == 'intR':
        return f"round(tonum({value}))"

    if to_type == 'float':
        return 'tonum(' + value + ")"

    # Ignore bool, any
    return value


# class Identifiers:
#     """
#     Handles cleaning text to make valid
#     identifiers and ensuring identifiers are unique.

#     The first time a identifier is added:
#     1. Clean identifier
#     2. Add a suffix letter
#     3. Add a number (for each hat)
#     4. Repeat step 3 if necesary

#     Variables:
#         original - Dict containing original names and
#             their suffixed variant
#         suffixed - Set containing all claimed suffixed names
#         numbered - Set containing all claimed numbered names
#         events - Dict linking event names to numbered names

#     broadcast: 'LoweredText': [broadcast_loweredtext1, ]
#     target: 'Cat': SpriteCat

#     """

#     def __init__(self):
#         self.original = {}
#         self.suffixed = set()
#         self.numbered = set()
#         self.events = {}

#     def get_suffixed(self, text, prefix="", create=True):
#         """
#         Get a suffixed identifier

#         This is used for custom blocks which only have
#         one hat, which can be called multiple times

#         create is used for variables, which may check
#         the existence of a global variable identifier
#         """

#         # Add a prefix if necesary
#         if not text.startswith(prefix.rstrip('_')):
#             text = prefix + text

#         # Remove illegal characters
#         cleaned = clean_identifier(text)

#         # Get suffixed or create and save it
#         suffixed = self.original.get(text)
#         if suffixed is None:
#             if not create:
#                 return None
#             suffixed = self._suffix_ident(cleaned)
#             self.original[text] = suffixed
#             self.suffixed.add(suffixed)

#         return suffixed

#     def get_numbered(self, text):
#         """Get a numbered identifier"""
#         # Clean and suffix the identifier
#         suffixed = self.get_suffixed(text)

#         # Add the number to the end
#         numbered = self._number_ident(suffixed)
#         self.numbered.add(numbered)

#         return numbered

#     def get_broadcast(self, text):
#         """Gets a broadcast hat identifier"""
#         # Remove illegal characters
#         cleaned = clean_identifier(text)

#         # Get suffixed or create and save it
#         suffixed = self.original.get(text.lower())
#         if suffixed is None:
#             suffixed = self._suffix_ident(cleaned)
#             self.original[text.lower()] = suffixed
#             self.suffixed.add(suffixed)

#         ident = self.get_numbered("broadcast_" + text)

#         # Add the hat to the event dict
#         event = text.lower()
#         if not event.startswith("broadcast"):
#             event = "broadcast_" + event
#         self.events.setdefault(event, []).append(ident)

#         return ident

#     def get_hat(self, blockmap, args):
#         """Gets a new hat identifier given the event name"""
#         # Get the prefix/name from blocks
#         prefix, text = blockmap.name
#         text = text.format(**args)

#         ident = self.get_number(text, prefix)
#         self.events.setdefault(prefix+text, []).append(ident)
#         return ident

#     def link_event(self, event, ident):
#         """Adds a identifier to an event's list"""
#         self.events.setdefault(event, []).append(ident)

#     def get_target(self, text):
#         """Gets a target class identifier"""
#         if not text == 'Stage' or text.startswith("Sprite"):
#             ident = "Sprite" + text
#         else:
#             ident = text

#         self.events[text] = ident

#         return self.get_suffixed(text)

#     def _suffix_ident(self, ident):
#         """Adds a letter to the end of ident"""
#         if ident not in self.suffixed:
#             return ident
#         for suffix in _letter_iter():
#             if ident + suffix not in self.suffixed:
#                 return ident + suffix
#         raise Exception("_letter_iter empty")

#     def _number_ident(self, ident):
#         """Adds a number to the end of ident"""
#         if ident not in self.numbered:
#             return ident

#         # Instead of broadcast12, broadcast1_2
#         if ident[-1].isdigit():
#             ident = ident + "_"

#         for number in itertools.count(1):
#             if ident + str(number) not in self.numbered:
#                 return ident + str(number)
#         raise Exception("itertools.count empty")


# class Prototypes:
#     """
#     Handles custom block prototypes

#     prototypes need to be referenced by:
#         - blockid for procedure_definitions
#         - proccode for procedures_call
#     arguments need to be referenced by:
#         - arg name for argument_reporters
#         - argid for ?
#     """

#     def __init__(self, hats: naming.Events):
#         self.hats = hats
#         self.prototypes = {}
#         self.prototypes_id = {}

#     def add_prototype(self, blockid, proccode, warp, arg_zip):
#         """Names, saves, and returns a prototype"""
#         # Clean the name
#         name = self.hats.get_event(
#             "cb_{name}", {'name': strip_pcodes(proccode)})

#         # Clean argument names
#         args_id = {}  # Arg names by id
#         args_name = {}  # Arg names by original name
#         for id_, arg in arg_zip:
#             arg_name = clean_identifier(arg)

#             # Ensure the name is unique
#             if arg_name in args_id.values():
#                 for suffix in _letter_iter():
#                     if not arg_name + suffix in args_id.values():
#                         arg_name = arg_name + suffix
#                         break

#             args_id[id_] = arg_name
#             args_name[arg] = arg_name

#         # Return the prototype dict
#         prototype = {
#             'name': name,
#             'warp': warp,
#             'args': args_id,
#             'arg_names': args_name
#         }
#         self.prototypes[proccode] = prototype
#         self.prototypes_id[blockid] = prototype
#         return prototype

#     def get_definition(self, blockid):
#         """Gets a prototype by blockid"""
#         return self.prototypes_id[blockid]


# class Broadcasts(Identifiers):
#     """
#     Handles broadcast naming
#     """


# class Variables:
#     """Handles variable and list naming"""

#     global_hats = Identifiers()

#     def __init__(self, local_hats, stage=False):
#         self.local_hats: Identifiers = local_hats
#         if stage:
#             Variables.global_hats: Identifiers = local_hats

#     def get_variable(self, name, local=False):
#         """
#         Gets a variable reference,
#         eg. self.var_x or util.sprites.stage.var_x

#         If local is True, no prefix will be added,
#         eg. var_x
#         """
#         if not local:
#             return self._get_ident(name, "var_")
#         return self.local_hats.get_suffixed(name, "var_")

#     def get_list(self, name, local=False):
#         """
#         Gets a list reference,
#         eg. self.list_x

#         If local is True, no prefix is added,
#         eg. list_x
#         """
#         if not local:
#             return self._get_ident(name, "list_")
#         return self.local_hats.get_suffixed(name, "list_")

#     def _get_ident(self, name, prefix):
#         """Gets either stage.ident or self.ident"""
#         ident = self.global_hats.get_suffixed(name, prefix, False)
#         if ident:
#             return "util.sprites.stage." + ident
#         ident = self.local_hats.get_suffixed(name, prefix)
#         return "self." + ident


def _letter_iter():
    """
    Creates an iterator of this pattern:
        A, B, C, ... AA, AB, AC, ... AZZ, ...
    """
    return map(
        ''.join,
        itertools.chain.from_iterable(
            map(
                lambda r: itertools.permutations(
                    "ABCDEFGHIJKLMNOPQRSTUVWXYZ", r),
                itertools.count(1)
            )
        )
    )
