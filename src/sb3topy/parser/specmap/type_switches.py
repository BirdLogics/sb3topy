"""
type_switches.py

Determines the return_type of more complex blocks.

TODO Switches for arithmetic operators
"""

from typing import Any, Callable, Dict


SWITCHES: Dict[str, Callable[[Any, Any], Any]] = {}


def switch(opcode):
    """Adds a funtion to the SWITCHES dict"""
    def wrapper(func):
        SWITCHES[opcode] = func
        return func
    return wrapper


@switch("argument_reporter_string_number")
def arg_reporter(target, block):
    """Determines the type of a argument reporter"""
    return target.prototypes.get_arg_node(target, block)


@switch("data_itemoflist")
def list_item(target, block):
    """Determines the type of a list item reporter"""
    name = block['fields']['LIST'][0]
    return target.vars.get_var('list', name).node
