"""
runtime.py

Contains classes used to manage base program functions.
"""


import asyncio
import logging
import random
import time

import pygame as pg

from . import config
from .events import SPRITES
from .render import Display, Render
from .types import Costumes, Pen
from .user_input import Inputs
from .util import Events, Util


class Runtime:
    """
    Container for everything needed to run the project

    Attributes:
        clock: pygame.time.Clock

        running: Controls the main loop
    """

    running = False

    def __init__(self, targets):
        # Initialize pygame
        pg.init()

        # Set mixer channels
        pg.mixer.set_num_channels(config.AUDIO_CHANNELS)

        # Get the loop clock
        self.clock = pg.time.Clock()

        # Initialize base classes
        self.inputs = Inputs()
        self.events = Events()
        self.display = Display()
        self.sprites = Sprites(targets)
        self.render = Render(self.sprites)

        # Create util for project.py
        self.util = Util(self)

        # Update sprite images
        self.sprites.update(self.display)

        Pen.resize(self.display)

    def quit(self):
        """
        Quit pygame and exit fullscreen to ensure the original display
        resolution is restored to the user's computer.
        """
        if self.display.fullscreen:
            self.display.toggle_fullscreen()
        pg.quit()

    async def main_loop(self):
        """Run the main loop"""
        # Setup asyncio debug
        asyncio.get_running_loop().slow_callback_duration = 0.49

        # Start green flag
        self.events.send(self.util, self.sprites, "green_flag")

        # Main loop
        self.running = True
        while self.running:
            # Handle the event queue
            self.handle_events()

            # Allow threads to run
            await self.step_threads()

            # Update targets, draw screen
            self.draw()

            # Limit the frame rate
            if not config.TURBO_MODE:
                self.clock.tick(config.TARGET_FPS)
            else:
                self.clock.tick()

    def handle_events(self):
        """Handles the event queue"""
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.running = False
                break
            if event.type == pg.KEYDOWN:
                self.inputs.e_keydown(self.util, event)
            elif event.type == pg.KEYUP:
                self.inputs.e_keyup(event)
            elif event.type == pg.MOUSEBUTTONDOWN:
                self.inputs.e_mousedown(
                    self.util, self.events, self.sprites, event)
            elif event.type == pg.MOUSEBUTTONUP:
                self.inputs.e_mouseup(event)
            elif event.type == pg.MOUSEMOTION:
                self.inputs.e_mousemotion(self.display, event)

            elif event.type == pg.VIDEORESIZE:
                self.display.video_resize(event)
                self.render.dirty_all()

    async def step_threads(self):
        """Run threads for WORK_TIME"""
        dirty = False
        work_timer = time.monotonic()
        while (time.monotonic() < work_timer + config.WORK_TIME) and \
                (config.TURBO_MODE or not dirty):
            # Allow targets to run for 1 tick
            await asyncio.sleep(0)

            # Check if any sprites need drawing
            if Costumes.redraw_requested or Pen.dirty:
                dirty = True
                Costumes.redraw_requested = False

    def draw(self):
        """Renders costumes and draws the screen"""
        self.sprites.update(self.display)
        self.render.draw(self.display)

        if config.SPRITE_RECTS:
            self.render.draw_sprite_rects(self.display)
        if config.REDRAW_RECTS:
            self.render.draw_redraw_rects(self.display)
        if config.PEN_RECTS:
            self.render.draw_pen_rects(self.display)

        if config.DRAW_FPS:
            self.render.draw_fps(self.display, self.clock)
        if config.DYNAMIC_TITLE:
            self.update_title()

        self.render.flip()

    def update_title(self):
        """Updates the dynamic title"""
        pg.display.set_caption(config.TITLE.format(
            FPS=self.clock.get_fps(),
            TURBO=" turbo" if config.TURBO_MODE else ""
        ))


class Sprites:
    """
    Handles the sprite list

    Attributes:
        targets: A dict of targets and their names, no clones.

        sprites: Pygame sprite group, all sprites but stage

        stage: The stage Target
    """

    def __init__(self, targets):
        self.targets = {}
        self.group = pg.sprite.LayeredDirty()
        self.stage = None

        # Init Targets, loading assets
        for name, target in targets.items():
            target = target()
            if name == "Stage":
                self.stage = target
            else:
                self.targets[name] = target
                self.group.add(target.sprite)

    def __getitem__(self, key):
        return self.targets[key]

    def sprites(self):
        """Returns a iter of pygame sprites, top to bottom"""
        return reversed(self.group.sprites())

    def update(self, display):
        """Update all targets, including stage and clones"""
        for target in self.targets.values():
            target.update(display)
            for clone in target.clones:
                clone.update(display)
        self.stage.update(display)


def start_program():
    """Run the program"""
    logging.basicConfig(level=logging.DEBUG)

    if config.RANDOM_SEED is not None:
        random.seed(config.RANDOM_SEED)

    runtime = None
    try:
        runtime = Runtime(SPRITES)
        asyncio.run(runtime.main_loop())
    finally:
        if runtime:
            runtime.quit()
