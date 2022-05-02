"""
switch_data.py

Contains functions to handle more complex blocks

TODO Define hats with a single switch instead of also in block_data
TODO Apply solo broadcast optimization to 'event_broadcast'?
"""

import logging

from ... import config
from . import block_data, specmap

SWITCHES = {}


def get_switch(opcode):
    """Get a custom blockswitch given an opcode"""
    return SWITCHES.get(opcode)


def hat_switch(block, target, blockmap):
    """
    Modifies a hat block so the next block becomes an SUBSTACK input.
    """
    # Get fields from the block
    # fields = {}
    # for field, value in block['fields'].items():
    #     fields[field] = value[0]

    # Save the base identifier name as a field
    block['fields']['IDENT'] = (blockmap.basename)  # .format(**fields),)

    # Create a substack input with the next block
    block['inputs']['SUBSTACK'] = (2, block['next'])
    block['next'] = None


def fswitch(opcode):
    """Decorator which adds a function to SWITCHES"""
    def decorator(func):
        SWITCHES[opcode] = func
        return func
    return decorator

# Switches for custom blocks


@fswitch('procedures_definition')
def proc_def(block, target):
    """Switch for a procedure definition hat"""
    # Get the block's prototype
    prototype = target.prototypes.get_definition(
        block['inputs'].pop('custom_block')[1])

    # Create the code string for the block
    args = prototype.args_list()
    warp = "@warp\n" if prototype.warp else ""
    code = f"{warp}async def {prototype.name}(self, util, {args}):\n{{SUBSTACK}}"

    # Create a substack input with the next block
    block['inputs']['SUBSTACK'] = (2, block['next'])
    block['next'] = None

    # Save the prototype to the target
    target.prototype = prototype

    # Create the block
    return block_data.Block('stack', {'SUBSTACK': 'stack'}, code, {'SUBSTACK': '    '}, "", "")


@fswitch('procedures_call')
def proc_call(block, target):
    """Switch for a procedure call block"""
    # Get the block's prototype
    prototype = target.prototypes.from_proccode(
        block['mutation']['proccode'])

    # If the block doesn't exist, ignore it
    if prototype is None:
        logging.warning("Procedure called without definition '%s'",
                        block['mutation']['proccode'])
        return block_data.BLOCKS["default"]

    # Replace input names with cleaned arg names
    block['inputs'] = {prototype.arg_from_id(
        argid): value for argid, value in block['inputs'].items()}

    # Get the argument list for the block
    args = {clean_name: prototype.get_type(
        arg_name) for arg_name, clean_name in prototype.args.items()}

    # Create arg code formatted by the BlockMap
    # Eg. {input1}, {input2}, ...
    args_code = prototype.args_list('}, {')
    if args_code:
        args_code = '{' + args_code + '}'

    # # Create the code string for the block
    code = f"await self.{prototype.name}(util, {args_code})"

    # Create the block
    return block_data.Block('stack', args, code, {}, "", "")


@fswitch('argument_reporter_string_number')
def proc_arg(block, target):
    """Switch for a procedure argument reporter"""
    arg_type = None
    if target.prototype is not None:
        arg_type = target.prototype.get_type(block['fields']['VALUE'][0])

    # The argument wasn't found, default to 0
    if arg_type is None:
        return block_data.Block("int", {}, "0", {}, "", "")

    # Return the code with the correct return_type
    return block_data.Block(arg_type, {'VALUE': 'proc_arg'}, '{VALUE}', {}, "", "")


@fswitch('argument_reporter_boolean')
def proc_arg_bool(block, target):
    """Switch for bool procedure argument reporters"""
    # Optionally replace turbowarp is compiled tags
    arg_name = block['fields']['VALUE'][0]
    if config.IS_COMPILED and arg_name == "is compiled?" and (
            target.prototype is None or
            arg_name not in target.prototype.args):
        return block_data.Block('bool', {}, 'True', {}, "", "")

    return proc_arg(block, target)


@fswitch('data_variable')
def var_get(block, target):
    """Type switch for a variable reporter"""
    return block_data.Block(
        target.vars.get_type('var', block['fields']['VARIABLE'][0]),
        {'VARIABLE': 'variable'}, '{VARIABLE}', {}, "", ""
    )


@fswitch('data_setvariableto')
def var_set(block, target):
    """Type switch for a set variable statement"""
    return block_data.Block(
        'stack',
        {'VARIABLE': 'variable',
         'VALUE': target.vars.get_type('var', block['fields']['VARIABLE'][0])},
        '{VARIABLE} = {VALUE}', {}, "", ""
    )


@fswitch('data_changevariableby')
def var_change(block, target):
    """Type switch for a change variable by statement"""
    var_type = target.vars.get_type('var', block['fields']['VARIABLE'][0])

    if var_type in ('int', 'float'):
        return block_data.Block(
            'stack', {'VARIABLE': 'variable', 'VALUE': var_type},
            '{VARIABLE} += {VALUE}', {}, "", ""
        )

    if var_type == "str":
        return block_data.Block(
            'stack', {'VARIABLE': 'variable', 'VALUE': 'float'},
            "{VARIABLE} = str(tonum({VARIABLE}) + {VALUE})", {}, "", ""
        )

    if var_type != "any":
        logging.warning("Unexpected type '%s' for changevariableby", var_type)

    return None


# Switches for legacy list indices (first, last, random)


@fswitch('data_deleteoflist')
def list_delete(block, _):
    """Switch for list delete item"""
    # Check the block text index
    value = block['inputs']['INDEX'][1]

    # If the index is a block and not a literal,
    # use legacy list mode depending on config
    if not (isinstance(value, list) and value[0] == 7):
        return block_data.BLOCKS['data_deleteoflist_legacy'] if config.LEGACY_LISTS else None

    # Check if the if the index is special
    if value[1] == 'all':
        return block_data.BLOCKS['data_deletealloflist']
    if value[1] in ('first', 'last', 'random'):
        return block_data.BLOCKS['data_deleteoflist_legacy']
    return None


@fswitch('data_insertatlist')
def list_insert(block, _):
    """Switch for list insert item"""
    # Check the block text index
    value = block['inputs']['INDEX'][1]

    # If the index is a block and not a literal,
    # use legacy list mode depending on config
    if not (isinstance(value, list) and value[0] == 7):
        return block_data.BLOCKS['data_insertatlist_legacy'] if config.LEGACY_LISTS else None

    # Check if the if the index is special
    if value[1] == 'last':
        return block_data.BLOCKS['data_addtolist']
    if value[1] in ('first', 'random'):
        return block_data.BLOCKS['data_insertatlist_legacy']
    return None


@fswitch('data_replaceitemoflist')
def list_replace(block, _):
    """Switch for list replace item"""
    # Check the block text index
    value = block['inputs']['INDEX'][1]

    # If the index is a block and not a literal,
    # use legacy list mode depending on config
    if not (isinstance(value, list) and value[0] == 7):
        return block_data.BLOCKS['data_replaceitemoflist_legacy'] if config.LEGACY_LISTS else None

    # Check if the if the index is special
    if value[1] in ('first', 'last', 'random'):
        return block_data.BLOCKS['data_replaceitemoflist_legacy']
    return None


@fswitch('data_itemoflist')
def list_item(block, _):
    """Switch for item of list"""
    # Check the block text index
    value = block['inputs']['INDEX'][1]

    # If the index is a block and not a literal,
    # use legacy list mode depending on config
    if not (isinstance(value, list) and value[0] == 7):
        return block_data.BLOCKS['data_itemoflist_legacy'] if config.LEGACY_LISTS else None

    # Check if the if the index is special
    if value[1] in ('first', 'last', 'random'):
        return block_data.BLOCKS['data_itemoflist_legacy']
    return None


# Switches for single broadcast reciever optimizations

# broadcast_recieved = hat('broadcast_{BROADCAST_OPTION}')


# @fswitch('event_whenbroadcastreceived')
# def broadcast_recieved_solo(block, target):
#     """
#     Checks if a broadcast is a solo receiver, and if it is, returns
#     a special blockmap which tells the parser to use an existing hat
#     for the base event IDENT field.
#     """
#     # Modify the block with the normal hat switch
#     broadcast_recieved(block, target)

#     if config.SOLO_BROADCASTS:
#         broadcast = block['fields']['BROADCAST_OPTION'][0].lower()
#         target_name = target.broadcasts.get(broadcast)
#         if target_name is not None and target_name not in target.cloned_targets:
#             logging.debug(
#                 "Solo broadcast '%s' in target '%s'",
#                 broadcast, target_name)
#             block['fields']['TARGET'] = (target_name,)
#             return block_data.BLOCKS['event_whenbroadcastreceived_solo']

#     return None


# @fswitch('event_broadcastandwait')
# def broadcast_sendwait_solo(block, target):
#     """
#     Checks if the broadcast is a solo reciver, and if it is, saves the
#     base broadcast event name under a new field IDENT, the target name
#     under a new field TARGET, and returns a special blockmap to await
#     the broadcast like a custom block.
#     """
#     if config.SOLO_BROADCASTS:
#         broadcast = specmap.get_broadcast(block, target)
#         target_name = target.broadcasts.get(broadcast)
#         if target_name is not None and target_name not in target.cloned_targets:
#             block['inputs']['TARGET'] = (9, target_name)
#             block['fields']['IDENT'] = ('broadcast_{BROADCAST_INPUT}',)

#             return block_data.BLOCKS['event_broadcastandwait_solo']

#     return None
