"""
block_data.py

Contains a dictionary with code and data for most blocks
"""

import re
from collections import namedtuple

INDENT_PAT = r"(?m)^(\s+)\{(\w+)\}"
Block = namedtuple(
    'Block', ['return_type', 'args', 'code', 'indents'])


def block(return_type, args, code):
    """Creates a Block tuple and saves indentation"""
    # Convert the arg type string into a tuple
    # from 'float X, ... to (('float', 'X'), ...)
    args = {
        arg[1]: arg[0] for arg in map(
            lambda s: s.split(), re.split(", ?", args))
    } if args else {}

    # Read indents prefixing format {} tags
    indents = {
        name: space for space, name in re.findall(
            INDENT_PAT, code)
    }

    # Strip indents prefixing format {} tags
    code = re.sub(INDENT_PAT, "{\\2}", code)

    return Block(return_type, args, code, indents)


def hat_block(args, code):
    """Creates a block with some default hat code"""
    args = "hat_ident IDENT, stack SUBSTACK" + (f", {args}" if args else '')
    code = code + '\n' + (
        "async def {IDENT}(self, util): \n"
        "    {SUBSTACK}"
    )

    return block('stack', args, code)


HATS = {
    'procedures_definition',
    'event_whenflagclicked',
    'event_whenkeypressed',
    'event_whenthisspriteclicked',
    'event_whenstageclicked',
    'event_whenbackdropswitchesto',
    'event_whengreaterthan',
    'event_whenbroadcastreceived',
    'control_start_as_clone'
}

LOOPS = {
    'control_repeat',
    'control_forever',
    'control_repeat_until'
}

BLOCKS = {
    # Motion blocks
    'motion_movesteps': block(
        'stack', 'float STEPS',
        "self.move({STEPS})"
    ),

    'motion_turnright': block(
        'stack', 'float DEGREES',
        "self.direction += {DEGREES}"
    ),

    'motion_turnleft': block(
        'stack', 'float DEGREES',
        "self.direction -= {DEGREES}"
    ),

    'motion_pointindirection': block(
        'stack', 'float DIRECTION',
        "self.direction = {DIRECTION}"
    ),

    'motion_pointtowards': block(
        'stack', 'str TOWARDS',
        "self.point_towards(util, {TOWARDS})"
    ),

    'motion_gotoxy': block(
        'stack', 'float X, float Y',
        "self.gotoxy({X}, {Y})"
    ),

    'motion_goto': block(
        'stack', 'str TO',
        "self.goto(util, {TO})"
    ),

    'motion_glidesecstoxy': block(
        'stack', 'float SECS, float X, float Y',
        "await self.glide({SECS}, {X}, {Y})"
    ),

    'motion_glideto': block(
        'stack', 'str TO',
        "self.glideto(util, {TO})"
    ),

    'motion_changexby': block(
        'stack', 'float DX',
        "self.xpos += {DX}"
    ),

    'motion_setx': block(
        'stack', 'float X',
        "self.xpos = {X}"
    ),

    'motion_changeyby': block(
        'stack', 'float DY',
        "self.ypos += {DY}"
    ),

    'motion_sety': block(
        'stack', 'float Y',
        "self.ypos = {Y}"
    ),
    'motion_ifonedgebounce': block(
        'stack', '',
        "self.bounce_on_edge()"
    ),

    'motion_setrotationstyle': block(
        'stack', 'str STYLE',
        "self.costume.rotation_style = {STYLE}"
    ),

    'motion_xposition': block(
        'float', '',
        "self.xpos"
    ),

    'motion_yposition': block(
        'float', '',
        "self.ypos"
    ),

    'motion_direction': block(
        'float', '',
        "self.direction"
    ),

    # Looks blocks
    'looks_sayforsecs': block(
        'stack', 'str MESSAGE, float SECS',
        "pass # looks_sayforsecs({MESSAGE}, {SECS})"
    ),

    'looks_say': block(
        'stack', 'str MESSAGE',
        "pass # looks_say({MESSAGE})"
    ),

    'looks_thinkforsecs': block(
        'stack', 'str MESSAGE, float SECS',
        "pass # looks_thinkforsecs({MESSAGE}, {SECS})"
    ),

    'looks_think': block(
        'stack', 'str MESSAGE',
        "pass # looks_think({MESSAGE})"
    ),

    'looks_show': block(
        'stack', '',
        "self.shown = True"
    ),

    'looks_hide': block(
        'stack', '',
        "self.shown = False"
    ),

    'looks_switchcostumeto': block(
        'stack', 'any COSTUME',
        "self.costume.switch({COSTUME})"
    ),

    'looks_nextcostume': block(
        'stack', '',
        "self.costume.next()"
    ),

    'looks_switchbackdropto': block(
        'stack', 'any BACKDROP', (
            "util.sprites.stage.costume.switch({BACKDROP})\n"
            "util.send_event('onbackdrop_' + util.sprites.stage.costume.name, True)"

        )
    ),

    'looks_switchbackdroptoandwait': block(
        'stack', 'any BACKDROP', (
            "util.sprites.stage.costume.switch({BACKDROP})"
            "await util.send_event('onbackdrop_' + util.sprites.stage.costume.name, True)"
        )
    ),

    'looks_nextbackdrop': block(
        'stack', '', (
            "util.sprites.stage.costume.next()"
            "util.send_event('onbackdrop_' + util.sprites.stage.costume.name, True)"
        )
    ),

    'looks_changeeffectby': block(
        'stack', 'field EFFECT, float CHANGE',
        "self.costume.change_effect({EFFECT}, {CHANGE})"
    ),

    'looks_seteffectto': block(
        'stack', 'field EFFECT, float VALUE',
        "self.costume.set_effect({EFFECT}, {VALUE})"
    ),

    'looks_cleargraphiceffects': block(
        'stack', '',
        "self.costume.clear_effects()"
    ),

    'looks_changesizeby': block(
        'stack', 'float CHANGE',
        "self.costume.size += {CHANGE}"
    ),

    'looks_setsizeto': block(
        'stack', 'float SIZE',
        "self.costume.size = {SIZE}"
    ),

    # 'looks_gotofrontback': block(
    #       'stack', 'str FRONT_BACK',
    #       "#? looks_goto_{FRONT_BACK}"
    #       ),

    'looks_goto_front': block(
        'stack', '',
        "self.front_layer(util)"
    ),

    'looks_goto_back': block(
        'stack', '',
        "self.back_layer(util)"
    ),

    # TODO Decimal behavior
    # 'looks_goforwardbackwardlayers': block(
    #       'stack', 'field FORWARD_BACKWARD, int NUM',
    #       "#? looks_go_{FORWARD_BACKWARD}_layers"
    #       ),

    'looks_go_forward_layers': block(
        'stack', 'int NUM',
        "self.change_layer(util, {NUM})"
    ),

    'looks_go_backward_layers': block(
        'stack', 'int NUM',
        "self.change_layer(util, -{NUM})"
    ),

    # 'looks_costumenumbername': block(
    #       'int', 'field NUMBER_NAME',
    #       "#? looks_costume_{NUMBER_NAME}"
    #       ),

    'looks_costume_number': block(
        'int', '',
        "self.costume.number"
    ),

    'looks_costume_name': block(
        'str', '',
        "self.costume.name"
    ),

    # 'looks_backdropnumbername': block(
    #       'int', 'field NUMBER_NAME',
    #       "#? looks_backdrop_{NUMBER_NAME}"
    #       ),

    'looks_backdrop_number': block(
        'int', '',
        "util.sprites.stage.costume.number"
    ),

    'looks_backdrop_name': block(
        'str', '',
        "util.sprites.stage.costume.name"
    ),

    'looks_size': block(
        'int', '',
        "round(self.costume.size)"
    ),

    # Sound blocks
    'sound_play': block(
        'stack', 'any SOUND_MENU',
        "self.sounds.play({SOUND_MENU})"
    ),

    'sound_playuntildone': block(
        'stack', 'any SOUND_MENU',
        "await self.sounds.play({SOUND_MENU})"
    ),

    'sound_stopallsounds': block(
        'stack', '',
        "self.sounds.stop_all()"
    ),

    'sound_changevolumeby': block(
        'stack', 'float VOLUME',
        "self.sounds.change_volume({VOLUME})"
    ),

    'sound_setvolumeto': block(
        'stack', 'float VOLUME',
        "self.sounds.set_volume({VOLUME})"
    ),

    'sound_volume': block(
        'float', '',
        "self.sounds.volume"
    ),

    'sound_seteffectto': block(
        'stack', 'field EFFECT, float VALUE',
        "self.sounds.set_effect({EFFECT}, {VALUE})"
    ),

    'sound_changeeffectby': block(
        'stack', 'field EFFECT, float VALUE',
        "self.sounds.change_effect({EFFECT}, {VALUE})"
    ),

    'sound_cleareffects': block(
        'stack', '',
        "self.sounds.clear_effects()"
    ),

    # Pen blocks
    'pen_clear': block(
        'stack', '',
        "self.pen.clear_all()"
    ),

    'pen_stamp': block(
        'stack', '',
        "self.pen.stamp(util)"
    ),

    'pen_penDown': block(
        'stack', '',
        "self.pen.down()"
    ),

    'pen_penUp': block(
        'stack', '',
        "self.pen.up()"
    ),

    'pen_setPenColorToColor': block(
        'stack', 'any COLOR',
        "self.pen.exact_color({COLOR})"
    ),

    'pen_changePenColorParamBy': block(
        'stack', 'str COLOR_PARAM, float VALUE',
        "self.pen.change_color({COLOR_PARAM}, {VALUE})"
    ),

    'pen_setPenColorParamTo': block(
        'stack', 'str COLOR_PARAM, float VALUE',
        "self.pen.set_color({COLOR_PARAM}, {VALUE})"
    ),

    'pen_changePenSizeBy': block(
        'stack', 'float SIZE',
        "self.pen.change_size({SIZE})"
    ),

    'pen_setPenSizeTo': block(
        'stack', 'float SIZE',
        "self.pen.set_size({SIZE})"
    ),

    # Legacy pen blocks
    'pen_setPenShadeToNumber': block(
        'stack', 'float SHADE',
        "self.pen.set_shade({SHADE})"
    ),

    'pen_changePenShadeBy': block(
        'stack', 'float SHADE',
        "self.pen.change_shade({SHADE})"
    ),

    'pen_setHueTo': block(
        'stack', 'float HUE',
        "self.pen.set_hue({HUE})"
    ),

    'pen_changePenHueBy': block(
        'stack', 'float HUE',
        "self.pen.change_hue({HUE})"
    ),

    # Event blocks
    'event_whenflagclicked': hat_block(
        '', "@on_greenflag"
    ),

    'event_whenkeypressed': hat_block(
        'field KEY_OPTION', "@on_pressed({KEY_OPTION})"
    ),

    'event_whenthisspriteclicked': hat_block(
        '', "@on_clicked"
    ),

    'event_whenstageclicked': hat_block(
        '', "@on_clicked"
    ),

    'event_whenbackdropswitchesto': hat_block(
        'field BACKDROP', "@on_backdrop({BACKDROP})"
    ),

    'event_whengreaterthan': hat_block(
        'field WHENGREATERTHANMENU, float VALUE',
        "@on_greater({WHENGREATERTHANMENU}, {VALUE})"
    ),

    'event_whenbroadcastreceived': hat_block(
        'field BROADCAST_OPTION',
        "@on_broadcast({BROADCAST_OPTION})"
    ),

    'event_broadcast': block(
        'stack', 'str BROADCAST_INPUT',
        "util.send_broadcast({BROADCAST_INPUT})"
    ),

    'event_broadcastandwait': block(
        'stack', 'str BROADCAST_INPUT',
        "await util.send_broadcast({BROADCAST_INPUT})"
    ),

    # Control blocks
    'control_wait': block(
        'stack', 'float DURATION',
        "await self.sleep({DURATION})",
    ),

    'control_repeat': block(
        'stack', 'int TIMES, stack SUBSTACK',
        "for _ in range({TIMES}):\n    {SUBSTACK}"
    ),

    'control_forever': block(
        'stack', 'stack SUBSTACK',
        "while True:\n    {SUBSTACK}"
    ),

    'control_if': block(
        'stack', 'bool CONDITION, stack SUBSTACK',
        "if {CONDITION}:\n    {SUBSTACK}"
    ),

    'control_if_else': block(
        'stack', 'bool CONDITION, stack SUBSTACK, stack SUBSTACK2',
        "if {CONDITION}:\n    {SUBSTACK}\n" +\
        "else:\n    {SUBSTACK2}"
    ),

    'control_wait_until': block(
        'stack', 'bool CONDITION',
        "while not {CONDITION}:\n    await self.yield_()"
    ),

    'control_repeat_until': block(
        'stack', 'bool CONDITION, stack SUBSTACK',
        "while not {CONDITION}:\n    {SUBSTACK}"
    ),

    'control_stop_this_script': block(
        'stack', 'field STOP_OPTION',
        "return None"
    ),

    # TODO Stop other scripts
    'control_stop_other_scripts_in_sprite': block(
        'stack', 'field STOP_OPTION',
        "pass  # self.stop_other()"
    ),

    'control_stop_all': block(
        'stack', 'field STOP_OPTION',
        "util.stop_all()\nreturn None"
    ),

    'control_start_as_clone': hat_block(
        '', "@on_clone_start"
    ),

    'control_create_clone_of': block(
        'stack', 'str CLONE_OPTION',
        "self.create_clone_of(util, {CLONE_OPTION})"
    ),

    'control_delete_this_clone': block(
        'stack', '',
        "self.delete_clone(util)"
    ),

    # Sensing blocks
    'sensing_touchingobject': block(
        'bool', 'field TOUCHINGOBJECTMENU',
        "self.get_touching(util, {TOUCHINGOBJECTMENU})"
    ),

    # TODO sensing_touchingcolor
    'sensing_touchingcolor': block(
        'bool', 'color COLOR',
        "False"
    ),

    'sensing_coloristouchingcolor': block(
        'bool', 'color COLOR, color COLOR2',
        "False",
    ),

    'sensing_distanceto': block(
        'float', 'field DISTANCETOMENU',
        "self.distance_to(util, {DISTANCETOMENU})"
    ),

    # TODO sensing_askandwait
    'sensing_askandwait': block(
        'stack', 'str QUESTION',
        "answer = input({QUESTION})"
    ),

    'sensing_answer': block(
        'str', '',
        'answer'
    ),

    'sensing_keypressed': block(
        'bool', 'str KEY_OPTION',
        "util.inputs[{KEY_OPTION}]"
    ),

    'sensing_mousedown': block(
        'bool', '',
        "util.inputs.mouse_down"
    ),

    'sensing_mousex': block(
        'int', '',
        "util.inputs.mouse_x"
    ),

    'sensing_mousey': block(
        'int', '',
        "util.inputs.mouse_y"
    ),

    'sensing_loudness': block(
        'int', '',
        "0"
    ),

    'sensing_loud': block(
        'bool', '',
        "False"
    ),

    'sensing_timer': block(
        'float', '',
        "util.timer()"
    ),

    'sensing_resettimer': block(
        'stack', '',
        "util.timer.reset()"
    ),

    # TODO {OBJECT} Stage = _stage_
    'sensing_of': block(
        'any', 'property PROPERTY, str OBJECT',
        "util.sprites[{OBJECT}].{PROPERTY}"
    ),

    'sensing_x_position_of': block(
        'float', 'field PROPERTY, str OBJECT',
        "util.sprites[{OBJECT}].xpos"
    ),

    'sensing_y_position_of': block(
        'float', 'field PROPERTY, str OBJECT',
        "util.sprites[{OBJECT}].ypos"
    ),

    'sensing_direction_of': block(
        'float', 'field PROPERTY, str OBJECT',
        "util.sprites[{OBJECT}].direction"
    ),

    'sensing_costume_of': block(
        'int', 'field PROPERTY, str OBJECT',
        "util.sprites[{OBJECT}].costume.number"
    ),

    'sensing_costume_name_of': block(
        'str', 'field PROPERTY, str OBJECT',
        "util.sprites[{OBJECT}].costume.name"
    ),

    'sensing_size_of': block(
        'int', 'field PROPERTY, str OBJECT',
        "round(util.sprites[{OBJECT}].costume.size)"
    ),

    'sensing_volume_of': block(
        'float', 'field PROPERTY, str OBJECT',
        "util.sprites[{OBJECT}].volume"
    ),

    'sensing_backdrop_of': block(
        'int', 'field PROPERTY, str OBJECT',
        "round(util.sprites[{OBJECT}].costume.number)"
    ),

    'sensing_backdrop_name_of': block(
        'str', 'field PROPERTY, field OBJECT',
        "util.sprites[{OBJECT}].costume.name"
    ),

    # 'sensing_current': block(
    #       'int', 'field CURRENT_MENU',
    #       "#? sensing_current_{CURRENT_MENU}"
    #       ),

    'sensing_current_year': block(
        '', '',
        "time.localtime()['tm_year']"
    ),

    'sensing_current_month': block(
        '', '',
        "time.localtime()['tm_month']"
    ),

    'sensing_current_date': block(
        '', '',
        "time.localtime()['tm_mday']"
    ),

    'sensing_current_day_of_week': block(
        '', '',
        "(time.localtime()['tm_wday'] + 2)"
    ),

    'sensing_current_hour': block(
        '', '',
        "time.localtime()['tm_hour']"
    ),

    'sensing_current_minute': block(
        '', '',
        "time.localtime()['tm_min']"
    ),

    'sensing_current_second': block(
        '', '',
        "time.localtime()['tm_sec']"
    ),

    # TODO Diffrent epoches?
    'sensing_dayssince2000': block(
        'float', '',
        "(time.time() / 86400 - 10957)"
    ),

    'sensing_username': block(
        'str', '',
        "config.USERNAME"
    ),

    # Operator blocks
    'operator_add': block(
        'float', 'float NUM1, float NUM2',
        "({NUM1} + {NUM2})"
    ),

    'operator_subtract': block(
        'float', 'float NUM1, float NUM2',
        "({NUM1} - {NUM2})"
    ),

    'operator_multiply': block(
        'float', 'float NUM1, float NUM2',
        "({NUM1} * {NUM2})"
    ),

    'operator_divide': block(
        'float', 'any NUM1, any NUM2',
        "div({NUM1}, {NUM2})"
    ),

    'operator_random': block(
        'float', 'float FROM, float TO',
        "pick_rand({FROM}, {TO})"
    ),

    'operator_lt': block(
        'bool', 'any OPERAND1, any OPERAND2',
        "lt({OPERAND1}, {OPERAND2})"
    ),

    'operator_equals': block(
        'bool', 'any OPERAND1, any OPERAND2',
        "eq({OPERAND1}, {OPERAND2})"
    ),

    'operator_gt': block(
        'bool', 'any OPERAND1, any OPERAND2',
        "gt({OPERAND1}, {OPERAND2})"
    ),

    'operator_and': block(
        'bool', 'bool OPERAND1, bool OPERAND2',
        "({OPERAND1} and {OPERAND2})"
    ),

    'operator_or': block(
        'bool', 'bool OPERAND1, bool OPERAND2',
        "({OPERAND1} or {OPERAND2})"
    ),

    'operator_not': block(
        'bool', 'bool OPERAND',
        "not {OPERAND}"
    ),

    'operator_join': block(
        'str', 'str STRING1, str STRING2',
        "({STRING1} + {STRING2})"
    ),

    'operator_letter_of': block(
        'str', 'int LETTER, str STRING',
        "letter_of({STRING}, {LETTER})"
    ),

    'operator_length': block(
        'int', 'str STRING',
        "len({STRING})"
    ),

    'operator_contains': block(
        'bool', 'str STRING1, str STRING2',
        "({STRING2} in {STRING1})"
    ),

    'operator_mod': block(
        'float', 'float NUM1, float NUM2',
        "({NUM1} % {NUM2})"
    ),

    'operator_round': block(
        'int', 'int NUM',
        "{NUM}"
    ),

    'operator_mathop': block(
        'float', 'str OPERATOR, float NUM',
        "#? operator_mathop_{OPERATOR}"
    ),

    'operator_mathop_abs': block(
        'int', 'float NUM',
        "abs({NUM})"
    ),

    'operator_mathop_floor': block(
        'int', 'float NUM',
        "math.floor({NUM})"
    ),

    'operator_mathop_ceiling': block(
        'int', 'float NUM',
        "math.ceil({NUM})"
    ),

    'operator_mathop_sqrt': block(
        'int', 'float NUM',
        "math.sqrt({NUM})"
    ),

    'operator_mathop_sin': block(
        'float', 'float NUM',
        "math.sin(math.radians({NUM}))"
    ),

    'operator_mathop_cos': block(
        'float', 'float NUM',
        "math.cos(math.radians({NUM}))"
    ),

    'operator_mathop_tan': block(
        'float', 'float NUM',
        "math.tan(math.radians({NUM}))"
    ),

    'operator_mathop_asin': block(
        'float', 'float NUM',
        "math.degrees(math.asin({NUM}))"
    ),

    'operator_mathop_acos': block(
        'float', 'float NUM',
        "math.degrees(math.acos({NUM}))"
    ),

    'operator_mathop_atan': block(
        'float', 'float NUM',
        "math.degrees(math.atan({NUM}))"
    ),

    'operator_mathop_ln': block(
        'float', 'float NUM',
        "math.log({NUM})"
    ),

    # math.log(x, 10) is closer to Scratch's log10
    'operator_mathop_log': block(
        'float', 'float NUM',
        "math.log({NUM}, 10)"
    ),

    'operator_mathop_e_^': block(
        'float', 'float NUM',
        "math.exp({NUM})"
    ),

    # TODO Use 10** instead?
    'operator_mathop_10_^': block(
        'float', 'float NUM',
        "math.pow(10, {NUM})"
    ),

    'data_variable': block(
        'any', 'variable VARIABLE',
        "{VARIABLE}"
    ),

    'data_setvariableto': block(
        'stack', 'variable VARIABLE, any VALUE',
        "{VARIABLE} = {VALUE}"
    ),

    'data_changevariableby': block(
        'stack', 'variable VARIABLE, float VALUE',
        "{VARIABLE} = tonum({VARIABLE}) + {VALUE}"
    ),

    'data_showvariable': block(
        'stack', 'variable VARIABLE',
        "print({VARIABLE})"
    ),

    'data_hidevariable': block(
        'stack', 'variable VARIABLE',
        "pass # hide variable"
    ),

    'data_listcontents': block(
        'str', 'list LIST',
        "{LIST}.join()"
    ),

    'data_addtolist': block(
        'stack', 'any ITEM, list LIST',
        "{LIST}.append({ITEM})"
    ),

    'data_deleteoflist': block(
        'stack', 'int INDEX, list LIST',
        "{LIST}.delete({INDEX})"
    ),

    'data_deleteoflist_legacy': block(
        'stack', 'any INDEX, list LIST',
        "{LIST}.delete2({INDEX})"
    ),

    'data_deletealloflist': block(
        'stack', 'list LIST',
        "{LIST}.delete_all()"
    ),

    'data_insertatlist': block(
        'stack', 'any ITEM, int INDEX, list LIST',
        "{LIST}.insert({INDEX}, {ITEM})"
    ),

    'data_insertatlist_legacy': block(
        'stack', 'any ITEM, any INDEX, list LIST',
        "{LIST}.insert2({INDEX}, {ITEM})"
    ),

    'data_replaceitemoflist': block(
        'stack', 'int INDEX, list LIST, any ITEM',
        "{LIST}[{INDEX}] = {ITEM}"
    ),

    'data_replaceitemoflist_legacy': block(
        'stack', 'any INDEX, list LIST, any ITEM',
        "{LIST}.set({INDEX}, {ITEM})"
    ),

    'data_itemoflist': block(
        'any', 'int INDEX, list LIST',
        "{LIST}[{INDEX}]"
    ),

    'data_itemoflist_legacy': block(
        'any', 'any INDEX, list LIST',
        "{LIST}.get({INDEX})"
    ),

    'data_itemnumoflist': block(
        'int', 'list LIST, any ITEM',
        "{LIST}.index({ITEM})"
    ),

    'data_lengthoflist': block(
        'int', 'list LIST',
        "len({LIST})"
    ),

    'data_listcontainsitem': block(
        'bool', 'list LIST, any ITEM',
        "{ITEM} in {LIST}"
    ),

    'data_showlist': block(
        'stack', 'list LIST',
        "{LIST}.show()"
    ),

    'data_hidelist': block(
        'stack', 'list LIST',
        "{LIST}.hide()"
    ),

    'default': block(
        'literal', '', '0'
    )
}
