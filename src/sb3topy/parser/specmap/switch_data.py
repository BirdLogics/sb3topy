"""
switch_data.py

Contains functions to handle more complex blocks

TODO Update engine to support event decorators
"""

from typing import Callable

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
    """Creates a function to create a custom blockmap"""
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

    'event_whenbroadcastreceived': hat('broadcast_{BROADCAST_OPTION}'),

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


@fswitch('procedures_definition')
def proc_def(block, target):
    """Switch for a procedure definition hat"""
    # Get the block's prototype
    prototype = target.prototypes.get_definition(
        block['inputs'].pop('custom_block')[1])

    # # Create the code string for the block
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

    # Replace input names with cleaned arg names
    block['inputs'] = {prototype.arg_from_id(
        argid): value for argid, value in block['inputs'].items()}

    # Get the argument list for the block
    args = {clean_name: 'value' for clean_name in prototype.args.values()}

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
def proc_arg(_, _1):
    """Switch for a procedure argument reporter"""
    return Block('any', {'VALUE': 'proc_arg'}, '{VALUE}', {})
