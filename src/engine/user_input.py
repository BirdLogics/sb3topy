"""
user_input.py

Contains the Inputs class which handles user input.
"""

import pygame as pg

from . import config


class Inputs:
    """
    Handles keyboard and mouse inputs.

    Attributes:
        mouse_x: Mouse x position

        mouse_y: Mouse y position

        mouse_down: Mouse down?
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
