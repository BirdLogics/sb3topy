"""
specmap.py

Contains functions used parse inputs and certain blocks.
"""


import logging

logger = logging.getLogger(__name__)


def parse_input(blocks, value):
    """
    Parses an input value and returns (type, value).

    The returned type determines what value is:
        'literal': A literal value which needs to be sanitized
        'blockid': A blockid which needs to be parsed
        'variable': An unparsed variable reporter
        'list_reporter': An unparsed list reporter
        'none': The literal None
    """

    # Handle a wrapped value
    if value[0] == 1 and isinstance(value[1], list):
        value = value[1]

    # Handle a block input
    # 1 wrapper with block, 2 block, 3 block over value
    if value[0] in (1, 2, 3):
        value = value[1]

        # Empty block
        if value is None:
            return 'none', None

        # Verify not a variable
        if isinstance(value, str):
            # Shadow block (dropdown)
            if blocks[value]['shadow']:
                # Get the only field from the dropdown menu
                value = next(iter(blocks[value]['fields'].values()))

                # Return the value of the field
                return 'literal', value[0]

            # Just a block
            return 'blockid', value

    # 12 Variable
    if value[0] == 12:
        return 'variable', value[1]

    # 13 List
    if value[0] == 13:
        return 'list_reporter', value[1]

    # Default to a literal
    # 4-8 Number, 9-10 String, # 11 Broadcast
    if not 4 <= value[0] <= 11:
        logger.error("Unexpected input type %i", value[0])

    return 'literal', value[1]


def get_broadcast(block, target):
    """
    Parses a event_broadcast(andwait) block to get the name of the
    sent broadcast. Returns the lowered broadcast name unless a block
    is in the input.
    """

    type_, value = parse_input(
        target.blocks, block['inputs']['BROADCAST_INPUT'])

    if type_ == 'literal':
        return value.lower()
    return None


def get_clone(block, target):
    """
    Parses a control_create_clone_of block to get the name of the
    target which is cloned. Returns the uncleaned target name unless
    a block is in the input.
    """

    type_, value = parse_input(target.blocks, block['inputs']['CLONE_OPTION'])

    if type_ == 'literal':
        if value == '_myself_':
            return target['name']

        return value

    return None
