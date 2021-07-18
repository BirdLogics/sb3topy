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

    except TypeError:
        # value == None
        # TODO Check number casts when value == None
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

    # if to_type == 'intR':
    #     return f"round(tonum({value}))"

    if to_type == 'float':
        return 'tonum(' + value + ")"

    # Ignore bool, any
    return value


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
