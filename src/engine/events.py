"""
events.py

Contains a class for managing events,
and a class for managing user inputs.
"""

import asyncio
import logging

import pygame as pg

from . import config


class Events:
    """Contains useful functions for sending events"""

    def __init__(self):
        self.events = {}

    def _send(self, util, sprites, event, restart):
        """
        Creates a tasks for every couroutine tied to an event, and
        creates a parent task waiting for each of the child tasks to
        finish.

        When an event is restarted, both the child tasks and the parent
        tasks are cancelled. Although the parent task would eventually
        return if just the children were cancelled, there is a delay
        which makes it necesary to cancel the parent as well.

        Because the parent task can be cancelled, it is necesary to
        wrap awaits for the parent in a try except block to catch the
        cancellation.
        """
        if restart:
            # If a parent is in self.events, cancel it
            task = self.events.pop(event, None)
            if task is not None:
                task.cancel()

        # Get a list of child tasks to runs
        tasks = []
        for sprite in sprites.sprites():
            tasks.extend(sprite.target.start_event(util, event, restart))
        tasks.extend(sprites.stage.start_event(util, event, restart))

        # Save and return the parent task
        task = asyncio.create_task(self._handle_tasks(tasks))
        self.events[event] = task
        return task

    def send(self, util, sprites, event, restart=False):
        """Starts an event for all sprites. Cannot be awaited."""
        self._send(util, sprites, event, restart)

    async def send_wait(self, util, sprites, event, restart):
        """Starts an event for all sprites. Should be awaited."""
        # Get the task
        task = self._send(util, sprites, event, restart)

        # Wait for it, but catch if it is cancelled
        try:
            await task
        except asyncio.CancelledError:
            # Verify the task was cancelled and not this function
            if not task.cancelled():
                raise

    def send_to(self, util, target, event):
        """Starts an event for a single target"""
        tasks = target.start_event(util, event)
        return asyncio.create_task(self._handle_tasks(tasks))

    async def _handle_tasks(self, tasks):
        """Waits on a list of tasks and catches any errors"""
        # Handle an empty list
        if not tasks:
            return

        done, _ = await asyncio.wait(
            tasks, return_when=asyncio.FIRST_EXCEPTION)

        # Handle any errors
        for task in done:
            try:
                task.result()
            except asyncio.CancelledError:
                pass
            except Exception:  # pylint: disable=broad-except
                logging.exception("Error in gathered task '%s'", task)

    def broadcast(self, util, sprites, event):
        """Parses a broadcast name and sends it. Not awaitable."""
        event = 'broadcast_' + event.lower()
        self._send(util, sprites, event, True)

    async def broadcast_wait(self, util, sprites, event):
        """Parses a broadcast name and sends it. Awaitable."""
        event = 'broadcast_' + event.lower()
        await self.send_wait(util, sprites, event, True)


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
        self.f3_down = False

        self.pressed_keys = set()

    def e_keydown(self, util, event):
        """Handles a keydown event"""
        # Get a name for the key
        key = config.KEY_MAP.get(event.key)
        if key is None:
            key = event.__dict__.get('unicode')
            if key is None:
                key = pg.key.name(event.key)
            else:
                key = key.lower()

        # Add the key to the key list
        if not self.pressed_keys:
            self.pressed_keys = {'any'}
        self.pressed_keys.add(key)

        # Send the event to sprites
        util.send_event("key" + key + "_pressed")
        util.send_event("keyany_pressed")

        # Handle hotkeys
        self.hotkey(util, event)

    def e_keyup(self, event):
        """Handles a keyup event"""
        # Get a name for the key
        key = config.KEY_MAP.get(event.key)
        if key is None:
            key = event.__dict__.get('unicode')
            if key is None:
                key = pg.key.name(event.key)
            else:
                key = key.lower()

        # Remove the key from the key list
        self.pressed_keys.discard(key)
        if len(self.pressed_keys) == 1:
            self.pressed_keys = set()

        # Handle hotkeys
        if event.key == pg.K_F3:
            self.f3_down = False

    def e_mousedown(self, util, events, sprites, event):
        """Handles a mouse click"""
        # Mouse down only for button 1
        if event.button == 1:
            self.mouse_down = True

        # Check for a clicked sprite
        point = event.pos
        for sprite in sprites.sprites():
            if not sprite.visible or sprite.target.costume.effects.get('ghost') == 100:
                continue
            offset = sprite.rect.topleft
            offset = (point[0] - offset[0], point[1] - offset[1])
            sprite.target.update(util.display, True)
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
        return key.lower() in self.pressed_keys

    def hotkey(self, util, event):
        """Checks for hotkeys with KEYDOWN events"""
        if event.key == pg.K_F10:
            config.TURBO_MODE = not config.TURBO_MODE

        elif event.key == pg.K_F11:
            util.display.toggle_fullscreen()
            util.runtime.render.dirty_all()

        elif event.key == pg.K_ESCAPE:
            if util.display.fullscreen:
                util.display.toggle_fullscreen()
                util.runtime.render.dirty_all()
            else:
                util.runtime.running = False

        elif event.key == pg.K_F3:
            self.f3_down = True

        elif self.f3_down:
            if event.key == pg.K_r:
                config.REDRAW_RECTS = not config.REDRAW_RECTS

            elif event.key == pg.K_s:
                config.SPRITE_RECTS = not config.SPRITE_RECTS

            elif event.key == pg.K_p:
                config.PEN_RECTS = not config.PEN_RECTS

            elif event.key == pg.K_f:
                config.DRAW_FPS = not config.DRAW_FPS
