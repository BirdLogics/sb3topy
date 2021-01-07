"""
tools.py


Currently unused
"""

import re
import logging


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
