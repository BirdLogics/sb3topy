"""

"""

import asyncio
import math
import random

from engine import SpriteBase

# pylint:disable=missing-function-docstring, invalid-name


class MotionBlocks(SpriteBase):
    """Holds the code for motion block."""

    def motion_movesteps(self, STEPS):  # dr
        radians = math.radians(90 - self.direction)
        self.xpos += STEPS * math.cos(radians)
        self.ypos += STEPS * math.sin(radians)

    def motion_gotoxy(self, X, Y):  # dr
        self.xpos = X
        self.ypos = Y

    # def goto(self, TO):  # dr
    #     raise NotImplementedError

    def motion_turnright(self, DEGREES):  # di
        self.set_direction(self.direction + DEGREES)

    def motion_turnleft(self, DEGREES):  # di
        self.set_direction(self.direction - DEGREES)

    def motion_pointindirection(self, DIRECTION):  # di
        self.set_direction(DIRECTION)

    # def motion_pointtowards(self, TOWARDS):  # di
    #     raise NotImplementedError

    # def motion_glidesecstoxy(self, SECS, X, Y):  # dr
    #     raise NotImplementedError

    # def motion_setrotationstyle(self, STYLE):  # di
    #     raise NotImplementedError
        # #styles = ["don't rotate","left-right","all around"]
        # if style == "don't rotate":
        #     self.rotationStyle = 0
        # elif style == "left-right":
        #     self.rotationStyle = 1
        # elif style == "all around":
        #     self.rotationStyle = 2

    def motion_ifonedgebounce(self):  # di
        raise NotImplementedError

    def motion_changexby(self, DX):  # dr
        self.xpos += DX

    def motion_setx(self, X):  # dr
        self.xpos = X

    def motion_changeyby(self, DY):  # dr
        self.ypos += DY

    def motion_sety(self, Y):  # dr
        self.ypos = Y

    #pylint: disable=pointless-statement
    def motion_xposition(self):
        self.xpos

    def motion_yposition(self):
        self.ypos

    def motion_direction(self):
        self.direction


class LooksBlocks(SpriteBase):
    """Holds the code for looks blocks"""

    # def looks_sayforsecs(self, MESSAGE, SECS):
    #     raise NotImplementedError

    # def looks_say(self, MESSAGE):
    #     raise NotImplementedError

    # def looks_thinkforsecs(self, MESSAGE, SECS):
    #     raise NotImplementedError

    # def looks_think(self, MESSAGE):
    #     raise NotImplementedError

    def looks_show(self):  # d
        self.visible = 1

    def looks_hide(self):  # d
        self.visible = 0

    # TODO Costume name/number?
    def looks_switchcostumeto(self, COSTUME):  # di
        self.switch_costume(COSTUME)

    def looks_nextcostume(self):  # di
        self.current_costume += 1
        if self.current_costume > len(self.costumes):
            self.current_costume = 0

    # def looks_switchbackdropto(self, BACKDROP):  # di
    #     raise NotImplementedError

    # def looks_changeeffectby(self, EFFECT, CHANGE):  # di
    #     raise NotImplementedError

    # def looks_seteffectto(self, EFFECT, VALUE):  # di
    #     raise NotImplementedError

    # def looks_cleargraphiceffects(self):  # di
    #     raise NotImplementedError

    def looks_changesizeby(self, CHANGE):  # di
        self.size += CHANGE

    def looks_setsizeto(self, SIZE):  # di
        self.size = SIZE

    # TODO Foward/backwards field?
    # def looks_gotofrontback(self):  # d
    #     raise NotImplementedError

    # def looks_gofowardsbackwardslayers(self, NUM):  # d
    #     raise NotImplementedError

    #pylint: disable=pointless-statement
    # TODO Name/number field?
    def looks_costumenumbername(self):
        self.current_costume

    # def looks_backdropnumbername(self):
    #     raise NotImplementedError

    def looks_size(self):
        self.size

    # def looks_switchbackdroptoandwait(self, BACKDROP):
    #     raise NotImplementedError

    # def looks_nextbackdrop(self):
    #     raise NotImplementedError


class EventsBlocks(SpriteBase):
    """Holds the code for Events blocks"""

    # pylint: disable=pointless-statement,unused-variable,unused-argument

    def event_whenflagclicked(self, SUBSTACK, ID):  # h
        async def green_flagID(self):
            SUBSTACK

    def event_whenkeypressed(self, SUBSTACK, ID, KEY):  # h
        async def keyKEY_pressedID(self):
            SUBSTACK

    def event_whenthisspritelicked(self, SUBSTACK, ID):  # h
        async def sprite_clickedID(self):
            SUBSTACK

    def event_whenbackdropswitchesto(self, SUBSTACK, ID, BACKDROP):  # h
        async def on_BACKDROP_ID(self):
            SUBSTACK

    def event_whenbroadcastreceived(self, SUBSTACK, ID, BROADCAST_OPTION):  # h
        async def on_BROADCAST_OPTION_ID(self):
            SUBSTACK

    # def event_broadcast(self, BROADCAST_INPUT):
    #     raise NotImplementedError

    # def event_broadcastandwait(self, BROADCAST_INPUT):
    #     raise NotImplementedError

    def control_wait(self, DURATION):
        await asyncio.sleep(DURATION)

    #pylint: disable=pointless-statement
    def control_repeat(self, TIMES, SUBSTACK):
        for _ in range(TIMES):
            SUBSTACK

    def control_forever(self, SUBSTACK):
        while True:
            SUBSTACK

    def control_if(self, CONDITION, SUBSTACK):
        if CONDITION:
            SUBSTACK

    def control_if_else(self, CONDITION, SUBSTACK, SUBSTACK2):
        if CONDITION:
            SUBSTACK
        else:
            SUBSTACK2

    def control_wait_until(self, CONDITION):
        while not CONDITION:
            await asyncio.sleep(0)

    def control_repeat_until(self, CONDITION, SUBSTACK):
        while not CONDITION:
            SUBSTACK

    # def control_stop(self, STOP_OPTION):
    #     raise NotImplementedError

    def control_start_as_clone(self, SUBSTACK, ID):  # h
        async def clone_startID(self):
            SUBSTACK

    # def control_delete_this_clone(self):
    #     raise NotImplementedError


class OperatorBlocks(SpriteBase):
    """Holds the code for Operator blocks"""

    #pylint: disable=pointless-statement

    def operator_add(self, NUM1, NUM2):
        NUM1 + NUM2

    def operator_subtract(self, NUM1, NUM2):
        NUM1 - NUM2

    def operator_multiply(self, NUM1, NUM2):
        NUM1 * NUM2

    def operator_divide(self, NUM1, NUM2):
        NUM1 / NUM2

    # TODO Decimal random
    def operator_random(self, FROM, TO):
        random.randint(FROM, TO)

    # TODO String num '123' comparison
    def operator_lt(self, OPERAND1, OPERAND2):
        OPERAND1 < OPERAND2

    def operator_equals(self, OPERAND1, OPERAND2):
        OPERAND1 == OPERAND2

    def operator_gt(self, OPERAND1, OPERAND2):
        OPERAND1 > OPERAND2

    def operator_and(self, OPERAND1, OPERAND2):
        OPERAND1 and OPERAND2

    def operator_or(self, OPERAND1, OPERAND2):
        OPERAND1 or OPERAND2

    def operator_not(self, OPERAND):
        not OPERAND

    # TODO Limited length join
    def operator_join(self, STRING1, STRING2):
        STRING1 + STRING2

    def operator_letter_of(self, LETTER, STRING):
        STRING[LETTER]

    def operator_mod(self, NUM1, NUM2):
        NUM1 % NUM2

    # def operator_mathop(self, OPERATOR, NUM):
    #     raise NotImplementedError


class DataBlocks(SpriteBase):
    """Holds the code for Data Blocks"""

    #pylint: disable=pointless-statement

    def data_variable(self, VARIABLE):
        self.variable['VARIABLE']

    def data_setvariableto(self, VARIABLE, VALUE):
        self.variable['VARIABLE'] = VALUE

    def data_changevariableby(self, VARIABLE, VALUE):
        self.variable['VARIABLE'] += VALUE

    # def data_showvariable(self, VARIABLE):
    #     raise NotImplementedError

    # def data_hidevariable(self, VARIABLE):
    #     raise NotImplementedError

    # TODO Single character join
    def data_listcontents(self, LIST):
        ' '.join(self.lists['LIST'])

    # TODO List item limit
    def data_addtolist(self, ITEM, LIST):
        self.lists['LIST'].append(ITEM)

    # TODO Last, first, random, all
    def data_deleteoflist(self, INDEX, LIST):
        self.lists['LIST'].pop(INDEX)

    def data_deletealloflist(self, LIST):
        self.lists['LIST'] = []

    def data_insertatlist(self, ITEM, INDEX, LIST):
        self.lists['LIST'].insert(INDEX, ITEM)

    def data_replaceitemoflist(self, INDEX, LIST, ITEM):
        self.lists['LIST'][INDEX] = ITEM

    def data_itemoflist(self, INDEX, LIST):
        self.lists['LIST'][INDEX]

    def data_lengthoflist(self, LIST):
        len(self.lists['LIST'])

    def data_listcontainsitem(self, LIST, ITEM):
        ITEM in self.lists['LIST']

    # def data_showlist(self, LIST):
    #     raise NotImplementedError

    # def data_hidelist(self, LIST):
    #     raise NotImplementedError


if __name__ == '__main__':
    pass
