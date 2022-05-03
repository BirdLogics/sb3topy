"""
sanitizer.py

Contains functions which are useful for sanitization.

TODO Would repr() be a better way to quote strings?
"""

import logging
import math
import re

logger = logging.getLogger(__name__)


def clean_identifier(text, default='identifier'):
    """Strips invalid character from an identifier"""
    # TODO Keep preluding underscores?
    cleaned = re.sub((
        r"(?a)(?:^([\d_]+))?"  # Preluding digits and _
        r"((?<!\\)%[sbn]|\W|__)*?"  # Other invalid characters
    ), "", text)

    if not cleaned:
        logger.warning("Stripped all characters from identifier '%s'")
        cleaned = default

    if not cleaned.isidentifier():
        logger.error("Failed to clean identifier '%s'", text)
        return "identifier"

    return cleaned


def quote_string(text):
    """Double "quotes" text"""
    # Escape back slashes and double quotes
    text = re.sub(r'()(?=\\|")', r"\\", str(text))

    # Escape newlines
    text = '\\n'.join(text.splitlines())

    # Double quote the string
    return '"' + text + '"'


def quote_field(text):
    """Single 'quotes' text"""
    # Escape back slashes and single quotes
    text = re.sub(r"()(?=\\|')", r"\\", str(text))

    # Escape newlines
    text = '\\n'.join(text.splitlines())

    # Single quote the string
    return "'" + text + "'"


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


def cast_literal(value, to_type):
    """
    Casts a value to a type
    Always returns a string
    """
    # Quote a string
    if to_type == "str":
        return quote_string(value)

    # Try to cast a float
    if to_type == "float":
        return str(cast_number(value))

    # Try to cast and round an int
    if to_type == "int":
        return str(round(cast_number(value)))

    # Get the bool value
    if to_type == "bool":
        return str(bool(value))

    # Get either a number or string
    if to_type == 'any':
        return str(quote_number(value))

    # Default behavior
    logger.warning("Unknown literal type '%s'", to_type)
    if value in (True, False, None):
        return str(value)
    return str(quote_number(value))


def cast_wrapper(value, from_type, to_type):
    """Puts a runtime cast wrapper around code"""

    # assert from_type in ('any', 'stack', 'int', 'float', 'str', 'bool', 'none')
    # assert to_type in ('any', 'stack', 'int', 'float', 'str', 'bool', 'none')

    # Don't cast any type
    if to_type == 'any':
        # logger.debug("Did not cast wrap '%s' to any", from_type)
        return value

    # Don't cast if both types are the same
    if to_type == from_type:
        # logger.debug("Did not cast wrap '%s' to '%s'", from_type, to_type)
        return value

    # Cast wrapper for strings
    if to_type == 'str':
        return "str(" + value + ")"

    # Cast wrapper for ints
    if to_type == 'int':
        # if from_type == 'float':
        #     return "round(" + value + ")"
        return "toint(" + value + ")"

    # Cast wrapper for floats
    if to_type == 'float':
        if from_type == 'int':
            return value
        return 'tonum(' + value + ")"

    # Handle blank stacks
    if to_type == 'stack' and from_type == 'none':
        return 'pass'

    # Handle blank bool inputs
    if to_type == 'bool' and from_type == 'none':
        return 'False'

    logger.warning("Unknown cast wrap for '%s' to '%s'", from_type, to_type)

    return value
