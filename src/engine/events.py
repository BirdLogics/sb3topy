"""
events.py

Contains a class for managing events,
and a class for managing user inputs.
"""

import asyncio

import pygame as pg

from . import config


class Events:
    """Contains useful functions for sending events"""

    def send(self, util, sprites, event, restart=False):
        """Starts an event for all sprites"""
        # Get a list of tasks to runs
        tasks = []
        for sprite in sprites.sprites():
            tasks.extend(sprite.target.start_event(util, event, restart))
        tasks.extend(sprites.stage.start_event(util, event, restart))

        # Return an awaitable task
        return asyncio.create_task(self._handle_tasks(tasks))

    def send_to(self, util, target, event):
        """Starts an event for a single target"""
        tasks = target.start_event(util, event)
        return asyncio.create_task(self._handle_tasks(tasks))

    async def _handle_tasks(self, tasks):
        """Waits on a list of tasks and catches any errors"""
        # Handle an empty list
        if not tasks:
            return

        # Will not stop for a cancellation, only errors
        done, _ = await asyncio.wait(
            tasks, return_when=asyncio.FIRST_EXCEPTION)

        # Handle any errors
        for task in done:
            if not task.cancelled() and task.exception() is not None:
                raise task.exception()

    def broadcast(self, util, sprites, event):
        """Parses a broadcast name and sends it"""
        event = 'broadcast_' + event.title()
        return self.send(util, sprites, event, True)


class Inputs:
    """
    Handles keyboard and mouse inputs.

    mouse_x - Mouse x position
    mouse_y - Mouse y position
    mouse_down - Mouse down?
    """

    def __init__(self):
        self.mouse_x = 0
        self.mouse_y = 0
        self.mouse_down = False

        self.pressed_keys = set()

    def e_keydown(self, util, event):
        """Handles a keydown event"""
        # Get a name for the key
        key = config.KEY_MAP.get(event.key)
        if key is None:
            key = event.__dict__.get('unicode').upper()
            if key is None:
                key = pg.key.name(event.key)

        # Add the key to the key list
        if not self.pressed_keys:
            self.pressed_keys = {'any'}
        self.pressed_keys.add(key)

        # Send the event to sprites
        util.send_event("key" + key + "_pressed")
        util.send_event("keyany_pressed")

    def e_keyup(self, event):
        """Handles a keyup event"""
        # Get a name for the key
        key = config.KEY_MAP.get(event.key)
        if key is None:
            key = event.__dict__.get('unicode').upper()
            if key is None:
                key = pg.key.name(event.key)

        # Remove the key from the key list
        self.pressed_keys.remove(key)
        if len(self.pressed_keys) == 1:
            self.pressed_keys = set()

    def e_mousedown(self, util, events, sprites, event):
        """Handles a mouse click"""
        # Mouse down only for button 1
        if event.button == 1:
            self.mouse_down = True

        # Check for a clicked sprite
        point = event.pos
        for sprite in sprites.sprites():
            if not sprite.target.visible:
                continue
            offset = sprite.rect.topleft
            offset = (point[0] - offset[0], point[1] - offset[1])
            try:
                if sprite.mask.get_at(offset):
                    events.send_to(util, sprite.target, "sprite_clicked")
                    return  # Stop checking
            except IndexError:
                pass
        events.send_to(util, sprites.stage, "sprite_clicked")

    def e_mouseup(self, event):
        """Handles a mouse up"""
        if event.button == 1:
            self.mouse_down = False

    def e_mousemotion(self, display, event):
        """Updates mouse position"""
        xpos, ypos = event.pos
        self.mouse_x = round((xpos - display.rect.x) /
                             display.scale - 240)
        self.mouse_y = round(
            180 - (ypos - display.rect.y)/display.scale)

    def __getitem__(self, key):
        return key.upper() in self.pressed_keys