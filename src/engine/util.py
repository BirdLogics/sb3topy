"""
util.py

Contains helper functions and classes
primarily used by project.py
"""

__all__ = ['BlockUtil', 'Inputs', 'List',
           'tonum', 'letter_of', 'pick_rand',
           'gt', 'lt', 'eq', 'div']

import asyncio
import random
import time

import pygame as pg

from .config import KEY_MAP


class BlockUtil:
    """Useful functions for targets to interface with Runtime"""
    down_keys = []
    targets = {}
    _timer = time.monotonic()
    runtime = None
    cache = None
    stage = None
    sprites = None
    _broadcasts = {}

    def __init__(self, runtime):
        self.runtime = runtime
        self.input = Inputs(runtime, self)

    def send_event(self, event, restart=False):
        """Starts an event for all sprites"""
        # Get sprites in the recieving order
        sprites = self.sprites.sprites()
        sprites.reverse()

        # Get a list of tasks to runs
        tasks = []
        for sprite in sprites:
            tasks.extend(sprite.target.start_event(self, event, restart))
        tasks.extend(self.stage.start_event(self, event, restart))

        # Return an awaitable task
        return asyncio.create_task(self._handle_tasks(tasks))

    def send_event_to(self, event, target):
        """Starts an event for a single target"""
        tasks = target.start_event(self, event)
        return asyncio.create_task(self._handle_tasks(tasks))

    async def _handle_tasks(self, tasks):
        """Waits on a list of tasks and catches any errors"""
        # Handle an empty list
        if not tasks:
            return

        # Will not stop for a cancelation, only errors
        done, _ = await asyncio.wait(
            tasks, return_when=asyncio.FIRST_EXCEPTION)

        # Handle any errors
        for task in done:
            if not task.cancelled() and task.exception() is not None:
                raise task.exception()

    def send_broadcast(self, event):
        """Parses a broadcast name and sends it"""
        event = 'broadcast_' + event.title()
        return self.send_event(event, True)

    def stop_all(self):
        """Ends execution of the main loop"""
        print("Stopping all...")
        self.runtime.running = False

    def key_event(self, key, state):
        """Presses or releases a key and sends press events"""
        if state:
            if not key in self.down_keys:
                self.down_keys.append(key)
        else:
            if key in self.down_keys:
                self.down_keys.remove(key)
            if len(self.down_keys) == 1:
                self.down_keys = []  # Remove 'any'
                self.send_event(f"keyany_pressed")
            self.send_event(f"key{key.upper()}_pressed")

    def key_down(self, event):
        """Called by runtime to handle key down events"""
        if event.key in KEY_MAP:
            self.key_event("any", True)
            self.key_event(KEY_MAP[event.key], True)
        elif event.unicode:  # TODO event.unicode doesn't exist for esc
            self.key_event("any", True)
            self.key_event(event.unicode.lower(), True)
        else:
            return False
        return True

    def key_up(self, event):
        """Called by runtime to handle key up events"""
        if event.key in KEY_MAP:
            self.key_event(KEY_MAP[event.key], False)
        elif event.unicode:
            self.key_event(event.unicode.lower(), False)
        else:
            return False
        return True

    def timer(self):
        """Gets the timer"""
        return time.monotonic() - self._timer

    def reset_timer(self):
        """Resets timer"""
        self._timer = time.monotonic()

    def mouse_down(self, event):
        """Checks if the mouse clicked a sprite"""
        point = event.pos
        sprites = self.sprites.sprites()
        sprites.reverse()
        for sprite in sprites:
            if not sprite.target.visible:
                continue
            offset = sprite.rect.topleft
            offset = (point[0] - offset[0], point[1] - offset[1])
            try:
                if sprite.mask.get_at(offset):
                    self.send_event_to("sprite_clicked", sprite.target)
                    return
            except IndexError:
                pass
        self.send_event_to("sprite_clicked", self.stage)

    def get_key(self, key):
        """Gets if a key is down"""
        return key in self.down_keys


class Inputs:
    """
    Handles keyboard and mouse inputs.

    m_xpos - Mouse x position
    m_ypos - Mouse y position
    m_down - Mouse down?
    """

    def __init__(self, runtime, util):
        self.util = util
        self.runtime = runtime
        self.m_xpos = 0
        self.m_ypos = 0
        self.m_down = False

    def update(self):
        """Update mouse position"""
        xpos, ypos = pg.mouse.get_pos()
        display = self.runtime.display
        self.m_xpos = round((xpos - display.rect.x)/display.scale - 240)
        self.m_ypos = round(180 - (ypos - display.rect.y)/display.scale)
        self.m_down = bool(pg.mouse.get_pressed()[0])


class List:
    """Handles special list behaviors"""

    def __init__(self, values):
        self.list = values

    def __getitem__(self, key):
        key = self._to_index(key)
        if key is not None:
            return self.list[key]
        return ""

    def __setitem__(self, key, value):
        key = self._to_index(key)
        if key is not None:
            self.list[key] = value

    def append(self, value):
        """Add up to 200,000 items to list"""
        if len(self.list) < 200000:
            self.list.append(value)

    def insert(self, key, value):
        """Insert up to 200,000 items in list"""
        if len(self.list) < 200000:
            if key == "first":
                key = 0
            elif key == "last":
                key = -1
            elif key == "random":
                key = random.randint(0, len(self.list))
            else:
                key = round(tonum(key)) - 1

            if key is not None and 0 <= key <= len(self.list):
                self.list.insert(key, value)

    def delete(self, key):
        """Remove an item from list"""
        if key == "all":
            self.list = []
        else:
            key = self._to_index(key)
            if key is not None:
                self.list.pop(key)

    def delete_all(self):
        """Delete all items in list"""
        self.list = []

    def _to_index(self, key):
        """Gets the index of first, last, random strings"""
        if self.list:
            if key == "first":
                return 0
            if key == "last":
                return -1
            if key == "random":
                return random.randint(0, len(self.list) - 1)
            key = round(tonum(key))
            if 0 < key <= len(self.list):
                return key - 1
        return None

    def __contains__(self, item):
        item = str(item).casefold()
        for value in self.list:
            if item == str(value).casefold():
                return True
        return False

    def __str__(self):
        char_join = True
        for item in self.list:
            if len(str(item)) != 1:
                char_join = False
                break
        if char_join:
            return ''.join(self.list)
        return ' '.join(self.list)

    def __len__(self):
        return self.list.__len__()

    # TODO Variable/list reporters
    def show(self):
        """Print list"""
        print(self.list)

    def hide(self):
        """Do nothing"""

    def index(self, item):
        """Find the index of an item, case insensitive"""
        item = str(item).casefold()
        for i, value in enumerate(self.list):
            if str(value).casefold() == item:
                return i + 1
        return 0

    def index1(self, item):
        """Find the index of an item in the list"""
        try:
            return self.list.index(item) + 1
        except ValueError:
            return 0

    def copy(self):
        """Return a copy of this List"""
        return List(self.list.copy())


def tonum(value):
    """Attempt to cast a value to a number"""
    if isinstance(value, str):
        try:
            value = float(value)
            if value.is_integer():
                value = int(value)
        except ValueError:
            return 0
    if value == float('NaN'):
        return 0
    return value


def letter_of(text, index):
    """Gets a letter from string"""
    try:
        return str(text)[tonum(index) - 1]
    except IndexError:
        return ""


def pick_rand(val1, val2):
    """Rand int or float depending on values"""
    val1 = tonum(val1)
    val2 = tonum(val2)
    val1, val2 = min(val1, val2), max(val1, val2)
    if isinstance(val1, float) or isinstance(val2, float):
        return random.random() * abs(val2-val1) + val1
    return random.randint(val1, val2)


def gt(val1, val2):  # pylint: disable=invalid-name
    """Either numerical or string comparison"""
    try:
        return float(val1) > float(val2)
    except ValueError:
        return str(val1).casefold() > str(val2).casefold()


def lt(val1, val2):  # pylint: disable=invalid-name
    """Either numerical or string comparison"""
    try:
        return float(val1) < float(val2)
    except ValueError:
        return str(val1).casefold() < str(val2).casefold()


def eq(val1, val2):  # pylint: disable=invalid-name
    """Either numerical or string comparison"""
    try:
        return float(val1) == float(val2)
    except ValueError:
        return str(val1).casefold() == str(val2).casefold()


def div(val1, val2):
    """Divide handling division by zero"""
    try:
        return tonum(val1) / tonum(val2)
    except ZeroDivisionError:
        return float('infinity')
