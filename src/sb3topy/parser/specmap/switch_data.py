"""
switch_data.py

Contains functions to handle more complex blocks

TODO Define hats with a single switch instead of also in block_data
TODO Apply solo broadcast optimization to 'event_broadcast'?
"""

import logging

from ... import config
from . import specmap
from .block_data import BLOCKS, Block


def switch(switch_: str):
    """Creates a function to create a new opcode based on fields"""
    def func(block, _):
        # Get fields from the block
        fields = {}
        for field, value in block['fields'].items():
            fields[field] = value[0].lower().replace(' ', '_')

        # Format the switch using the fields
        new_opcode = switch_.format(**fields)

        # Try to get a new blockmap
        return BLOCKS.get(new_opcode)

    return func


def hat(name):
    """
    Creates a function to modify a hat block. When the created function
    is run on a block, the base event name of the block is saved under
    a new IDENT field, and the next block is moved to a SUBSTACK input.
    """
    def func(block, _):
        # Get fields from the block
        # fields = {}
        # for field, value in block['fields'].items():
        #     fields[field] = value[0]

        # Save the base identifier name as a field
        block['fields']['IDENT'] = (name,)  # .format(**fields),)

        # Create a substack input with the next block
        block['inputs']['SUBSTACK'] = (2, block['next'])
        block['next'] = None

        # None return; defaults to BLOCKS[opcode]

    return func


SWITCHES = {
    # Hat switches
    'event_whenflagclicked': hat('green_flag'),

    'event_whenkeypressed': hat('key_{KEY_OPTION}_pressed'),

    'event_whenthisspriteclicked': hat('sprite_clicked'),

    'event_whenstageclicked': hat('sprite_clicked'),

    'event_whenbackdropswitchesto': hat('on_backdrop_{BACKDROP}'),

    'event_whengreaterthan': hat('on_{WHENGREATERTHANMENU}'),

    # Custom switch for event_whenbroadcastreceived
    # 'event_whenbroadcastreceived': hat('broadcast_{BROADCAST_OPTION}'),


    'control_start_as_clone': hat('clone_start'),

    # Basic switches
    'looks_gotofrontback': switch("looks_goto_{FRONT_BACK}"),

    'looks_goforwardbackwardlayers': switch(
        "looks_go_{FORWARD_BACKWARD}_layers"),

    'looks_costumenumbername': switch("looks_costume_{NUMBER_NAME}"),

    'looks_backdropnumbername': switch("looks_backdrop_{NUMBER_NAME}"),

    'control_stop': switch("control_stop_{STOP_OPTION}"),

    'sensing_touchingobject': switch("sensing_touching"),

    # TODO sensing_of switch
    'sensing_of': switch("sensing_{PROPERTY}_of"),

    'sensing_current': switch("sensing_current_{CURRENT_MENU}"),

    'operator_mathop': switch("operator_mathop_{OPERATOR}"),

}


def fswitch(opcode):
    """Adds a function to SWITCHES under opcode"""
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
    return Block('stack', {'SUBSTACK': 'stack'}, code, {'SUBSTACK': '    '})


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
        return BLOCKS["default"]

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
    return Block('stack', args, code, {})


@fswitch('argument_reporter_string_number')
def proc_arg(block, target):
    """Switch for a procedure argument reporter"""
    return Block(
        target.prototype.get_type(block['fields']['VALUE'][0]),
        {'VALUE': 'proc_arg'}, '{VALUE}', {}
    )


@fswitch('data_variable')
def var_get(block, target):
    """Type switch for a variable reporter"""
    return Block(
        target.vars.get_type('var', block['fields']['VARIABLE'][0]),
        {'VARIABLE': 'variable'}, '{VARIABLE}', {}
    )


@fswitch('data_setvariableto')
def var_set(block, target):
    """Type switch for a set variable statement"""
    return Block(
        'stack',
        {'VARIABLE': 'variable',
         'VALUE': target.vars.get_type('var', block['fields']['VARIABLE'][0])},
        '{VARIABLE} = {VALUE}', {}
    )


@fswitch('data_changevariableby')
def var_change(block, target):
    """Type switch for a change variable by statement"""
    var_type = target.vars.get_type('var', block['fields']['VARIABLE'][0])

    if var_type in ('int', 'float'):
        return Block(
            'stack', {'VARIABLE': 'variable', 'VALUE': var_type},
            '{VARIABLE} += {VALUE}', {}
        )

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
        return BLOCKS['data_deleteoflist_legacy'] if config.LEGACY_LISTS else None

    # Check if the if the index is special
    if value[1] == 'all':
        return BLOCKS['data_deletealloflist']
    if value[1] in ('first', 'last', 'random'):
        return BLOCKS['data_deleteoflist_legacy']
    return None


@fswitch('data_insertatlist')
def list_insert(block, _):
    """Switch for list insert item"""
    # Check the block text index
    value = block['inputs']['INDEX'][1]

    # If the index is a block and not a literal,
    # use legacy list mode depending on config
    if not (isinstance(value, list) and value[0] == 7):
        return BLOCKS['data_insertatlist_legacy'] if config.LEGACY_LISTS else None

    # Check if the if the index is special
    if value[1] == 'last':
        return BLOCKS['data_addtolist']
    if value[1] in ('first', 'random'):
        return BLOCKS['data_insertatlist_legacy']
    return None


@fswitch('data_replaceitemoflist')
def list_replace(block, _):
    """Switch for list replace item"""
    # Check the block text index
    value = block['inputs']['INDEX'][1]

    # If the index is a block and not a literal,
    # use legacy list mode depending on config
    if not (isinstance(value, list) and value[0] == 7):
        return BLOCKS['data_replaceitemoflist_legacy'] if config.LEGACY_LISTS else None

    # Check if the if the index is special
    if value[1] in ('first', 'last', 'random'):
        return BLOCKS['data_replaceitemoflist_legacy']
    return None


@fswitch('data_itemoflist')
def list_item(block, _):
    """Switch for item of list"""
    # Check the block text index
    value = block['inputs']['INDEX'][1]

    # If the index is a block and not a literal,
    # use legacy list mode depending on config
    if not (isinstance(value, list) and value[0] == 7):
        return BLOCKS['data_itemoflist_legacy'] if config.LEGACY_LISTS else None

    # Check if the if the index is special
    if value[1] in ('first', 'last', 'random'):
        return BLOCKS['data_itemoflist_legacy']
    return None


# Switches for single broadcast reciever optimizations

broadcast_recieved = hat('broadcast_{BROADCAST_OPTION}')


@fswitch('event_whenbroadcastreceived')
def broadcast_recieved_solo(block, target):
    """
    Checks if a broadcast is a solo reciever, and if it is, returns
    a special blockmap which tells the parser to use an existing hat
    for the base event IDENT field.
    """
    # Modify the block with the normal hat switch
    broadcast_recieved(block, target)

    if config.SOLO_BROADCASTS:
        broadcast = block['fields']['BROADCAST_OPTION'][0].lower()
        target_name = target.broadcasts.get(broadcast)
        if target_name is not None and target_name not in target.cloned_targets:
            logging.debug(
                "Solo broadcast '%s' in target '%s'",
                broadcast, target_name)
            block['fields']['TARGET'] = (target_name,)
            return BLOCKS['event_whenbroadcastreceived_solo']

    return None


@fswitch('event_broadcastandwait')
def broadcast_sendwait_solo(block, target):
    """
    Checks if the broadcast is a solo reciver, and if it is, saves the
    base broadcast event name under a new field IDENT, the target name
    under a new field TARGET, and returns a special blockmap to await
    the broadcast like a custom block.
    """
    if config.SOLO_BROADCASTS:
        broadcast = specmap.get_broadcast(block, target)
        target_name = target.broadcasts.get(broadcast)
        if target_name is not None and target_name not in target.cloned_targets:
            block['fields']['TARGET'] = (target_name,)
            block['fields']['IDENT'] = ('broadcast_{BROADCAST_INPUT}',)

            return BLOCKS['event_broadcastandwait_solo']

    return None
