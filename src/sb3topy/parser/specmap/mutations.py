"""
mutations.py

Contains "mutations", which are a special function can create a custom
bm depending on context. Mutations can also modify the block
itself and the parent target, if necessary.

TODO Define hats with a single switch instead of also in data
TODO Apply solo broadcast optimization to 'event_broadcast'?
"""

import logging

from ... import config
from . import blockmap as bm
from . import data, specmap

logger = logging.getLogger(__name__)


MUTATIONS = {}


def get_mutation(opcode):
    """Find mutation given an opcode"""
    return MUTATIONS.get(opcode)


def hat_mutation(block, _target, blockmap):
    """
    Modifies a hat block so the next block becomes an SUBSTACK input.
    """
    # Save the base identifier name as a field
    block['fields']['IDENT'] = (blockmap.basename,)

    # Create a substack input with the next block
    block['inputs']['SUBSTACK'] = (2, block['next'])
    block['next'] = None

    return blockmap


def mutation(opcode):
    """Decorator which adds a function to MUTATIONS"""
    def decorator(func):
        assert opcode not in MUTATIONS, \
            f"Duplicate mutation for '{opcode}'."
        assert func.__code__.co_argcount == 3, \
            f"Mutation for '{opcode}' must have 3 arguments."

        MUTATIONS[opcode] = func
        return func
    return decorator


# Custom block mutations

@mutation('procedures_definition')
def proc_def(block, target, _):
    """Switch for a procedure definition hat"""
    # Get the block's prototype
    prototype = target.prototypes.get_definition(
        block['inputs'].pop('custom_block')[1])

    # Create the code string for the block
    args = prototype.args_list()
    warp = "@warp\n" if prototype.warp else ""
    code = f"{warp}async def {prototype.name}(self, util, {args}):\n{{SUBSTACK}}"

    # Save the prototype to the target
    target.prototype = prototype

    # Create the block
    return bm.BlockMap('stack', {'SUBSTACK': 'stack'}, code, {'SUBSTACK': '    '}, "", "")


@mutation('procedures_call')
def proc_call(block, target, _):
    """Switch for a procedure call block"""
    # Get the block's prototype
    prototype = target.prototypes.from_proccode(
        block['mutation']['proccode'])

    # If the block doesn't exist, ignore it
    if prototype is None:
        logger.warning("Procedure called without definition '%s'",
                        block['mutation']['proccode'])
        return data.BLOCKS["default"]

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
    return bm.BlockMap('stack', args, code, {})


@mutation('argument_reporter_string_number')
def proc_arg(block, target, _):
    """Switch for a procedure argument reporter"""
    arg_type = None
    if target.prototype is not None:
        arg_type = target.prototype.get_type(block['fields']['VALUE'][0])

    # The argument wasn't found, default to 0
    if arg_type is None:
        return bm.BlockMap("int", {}, "0", {})

    # Return the code with the correct return_type
    return bm.BlockMap(arg_type, {'VALUE': 'proc_arg'}, '{VALUE}', {})


@mutation('argument_reporter_boolean')
def proc_arg_bool(block, target, blockmap):
    """Switch for bool procedure argument reporters"""
    # Optionally replace turbowarp is compiled tags
    arg_name = block['fields']['VALUE'][0]
    if config.IS_COMPILED and arg_name == "is compiled?" and (
            target.prototype is None or
            arg_name not in target.prototype.args):
        return bm.BlockMap('bool', {}, 'True', {})

    return proc_arg(block, target, blockmap)


# Variable mutations

@mutation('data_variable')
def var_get(block, target, _):
    """Type switch for a variable reporter"""
    return bm.BlockMap(
        target.vars.get_type('var', block['fields']['VARIABLE'][0]),
        {'VARIABLE': 'variable'}, '{VARIABLE}', {}
    )


@mutation('data_setvariableto')
def var_set(block, target, _):
    """Type switch for a set variable statement"""
    return bm.BlockMap(
        'stack',
        {'VARIABLE': 'variable',
         'VALUE': target.vars.get_type('var', block['fields']['VARIABLE'][0])},
        '{VARIABLE} = {VALUE}', {},
    )


@mutation('data_changevariableby')
def var_change(block, target, blockmap):
    """Type switch for a change variable by statement"""
    var_type = target.vars.get_type('var', block['fields']['VARIABLE'][0])

    if var_type in ('int', 'float'):
        return bm.BlockMap(
            'stack', {'VARIABLE': 'variable', 'VALUE': var_type},
            '{VARIABLE} += {VALUE}', {}
        )

    if var_type == "str":
        return bm.BlockMap(
            'stack', {'VARIABLE': 'variable', 'VALUE': 'float'},
            "{VARIABLE} = str(tonum({VARIABLE}) + {VALUE})", {},
        )

    if var_type != "any":
        logger.warning("Unexpected type '%s' for changevariableby", var_type)

    return blockmap


# Legacy list mutations (first, last, random)
# TODO Replace these with switches?

@mutation('data_deleteoflist')
def list_delete(block, _, blockmap):
    """Switch for list delete item"""
    # Check the block text index
    value = block['inputs']['INDEX'][1]

    # If the index is a block and not a literal,
    # use legacy list mode depending on config
    if not (isinstance(value, list) and value[0] == 7):
        if config.LEGACY_LISTS:
            return data.BLOCKS['data_deleteoflist_legacy']
        return blockmap

    # Check if the if the index is special
    if value[1] == 'all':
        return data.BLOCKS['data_deletealloflist']
    if value[1] in ('first', 'last', 'random'):
        return data.BLOCKS['data_deleteoflist_legacy']
    return blockmap


@mutation('data_insertatlist')
def list_insert(block, _, blockmap):
    """Switch for list insert item"""
    # Check the block text index
    value = block['inputs']['INDEX'][1]

    # If the index is a block and not a literal,
    # use legacy list mode depending on config
    if not (isinstance(value, list) and value[0] == 7):
        if config.LEGACY_LISTS:
            return data.BLOCKS['data_insertatlist_legacy']
        return blockmap

    # Check if the if the index is special
    if value[1] == 'last':
        return data.BLOCKS['data_addtolist']
    if value[1] in ('first', 'random'):
        return data.BLOCKS['data_insertatlist_legacy']
    return blockmap


@mutation('data_replaceitemoflist')
def list_replace(block, _, blockmap):
    """Switch for list replace item"""
    # Check the block text index
    value = block['inputs']['INDEX'][1]

    # If the index is a block and not a literal,
    # use legacy list mode depending on config
    if not (isinstance(value, list) and value[0] == 7):
        if config.LEGACY_LISTS:
            return data.BLOCKS['data_replaceitemoflist_legacy']
        return blockmap

    # Check if the if the index is special
    if value[1] in ('first', 'last', 'random'):
        return data.BLOCKS['data_replaceitemoflist_legacy']
    return blockmap


@mutation('data_itemoflist')
def list_item(block, _, blockmap):
    """Switch for item of list"""
    # Check the block text index
    value = block['inputs']['INDEX'][1]

    # If the index is a block and not a literal,
    # use legacy list mode depending on config
    if not (isinstance(value, list) and value[0] == 7):
        if config.LEGACY_LISTS:
            return data.BLOCKS['data_itemoflist_legacy']
        return blockmap

    # Check if the if the index is special
    if value[1] in ('first', 'last', 'random'):
        return data.BLOCKS['data_itemoflist_legacy']
    return blockmap


# Switches for single broadcast receiver optimizations

@mutation('event_whenbroadcastreceived')
def broadcast_received_solo(block, target, blockmap):
    """
    Checks if a broadcast is a solo receiver, and if it is, returns
    a special blockmap which tells the parser to use an existing hat
    for the base event IDENT field.
    """
    if config.SOLO_BROADCASTS:
        broadcast = block['fields']['BROADCAST_OPTION'][0].lower()
        target_name = target.broadcasts.get(broadcast)
        if target_name is not None and target_name not in target.cloned_targets:
            logger.debug(
                "Solo broadcast '%s' in target '%s'",
                broadcast, target_name)
            block['fields']['TARGET'] = (target_name,)

            return data.BLOCKS['event_whenbroadcastreceived_solo']

    return blockmap


@mutation('event_broadcastandwait')
def broadcast_sendwait_solo(block, target, blockmap):
    """
    Checks if the broadcast is a solo receiver, and if it is, saves the
    base broadcast event name under a new field IDENT, the target name
    under a new field TARGET, and returns a special blockmap to await
    the broadcast like a custom block.
    """
    if config.SOLO_BROADCASTS:
        broadcast = specmap.get_broadcast(block, target)
        target_name = target.broadcasts.get(broadcast)
        if target_name is not None and target_name not in target.cloned_targets:
            block['inputs']['TARGET'] = (9, target_name)
            block['fields']['IDENT'] = ('broadcast_{BROADCAST_INPUT}',)

            return data.BLOCKS['event_broadcastandwait_solo']

    return blockmap
