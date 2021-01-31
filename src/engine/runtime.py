"""
runtime.py

Contains classes used to manage
base program functions
"""

import asyncio
import logging
import time

import pygame as pg

from .config import *  # pylint: disable=W0401, W0614
from .pen import Pen
from .util import BlockUtil


class Runtime:
    """Container for everything needed to run the project"""

    def __init__(self, targets):
        pg.init()

        # Initialize target and sprite containers
        self.sprites = pg.sprite.LayeredDirty()

        # Initialize the asset cache

        # Initialize the various clocks

        self.work_timer = time.monotonic()
        self.clock = pg.time.Clock()

        self.util = BlockUtil(self)
        Pen.util = self.util

        self.display = Display()
        pg.mixer.set_num_channels(AUDIO_CHANNELS)

        # Initialize targets
        for name, target in targets.items():
            if name == "Stage":
                self.util.stage = target(self.util)
            else:
                self.util.targets[name] = target(self.util)
                self.sprites.add(self.util.targets[name].sprite)
        self.util.sprites = self.sprites

        self.running = False

    def quit(self):
        """Ensures fullscreen is exited to return normal display resolution"""
        if self.display.fullscreen:
            self.display.toggle_fullscreen()
        pg.quit()

    async def main_loop(self):
        """Run the main loop"""
        asyncio.get_running_loop().slow_callback_duration = 0.49
        self.util.send_event("green_flag")
        self.running = True
        turbo2 = False
        while self.running:
            # Allow pygame to update
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.running = False
                elif event.type == pg.KEYDOWN:
                    self.util.key_down(event)  # TODO When key pressed
                elif event.type == pg.KEYUP:
                    # self.util.key_down(event)
                    if event.key == pg.K_F11:
                        self.display.toggle_fullscreen()
                    elif event.key == pg.K_F10:
                        turbo2 = not turbo2
                elif event.type == pg.VIDEORESIZE:
                    self.display.size = (event.w, event.h)
                    self.display.setup_display()
                    for sprite in self.util.sprites.sprites():
                        sprite.target.dirty = 3
                    self.util.stage.dirty = 3
                    Pen.resize(self.display.rect.size)
                elif event.type == pg.MOUSEBUTTONDOWN:
                    self.util.mouse_down(event)
            self.util.input.update()

            # Allow the threads to run
            dirty = False
            work_timer = time.monotonic()
            while (time.monotonic() < work_timer + WORK_TIME) and \
                    (TURBO_MODE or not dirty):
                # Allow targets to run for 1 tick
                await asyncio.sleep(0)

                # Check if any sprites need drawing
                for target in self.util.targets.values():
                    if target.dirty and target.visible:
                        dirty = True
                    for clone in target.clones:
                        if clone.dirty and clone.visible:
                            dirty = True
                if Pen.dirty:
                    dirty = True

            if turbo2:
                continue

            # Update sprite rects, images, etc.
            self.update_sprites()

            # Update the screen
            if self.util.stage.dirty or Pen.dirty:
                self.util.stage.update(self.util)

                # Get the stage bg
                bg_image = pg.Surface(self.display.size)
                bg_image.fill((255, 255, 255))
                bg_image.blit(
                    self.util.stage.sprite.image,
                    (self.display.rect.x, self.display.rect.y))
                # self.util.stage.dirty = False

                # Get the Pen bg
                bg_image.blit(Pen.image, self.display.rect.topleft)
                Pen.dirty = False

                self.sprites.set_clip(self.display.rect)
                self.sprites.clear(self.display.screen, bg_image.convert())
                self.sprites.draw(self.display.screen)

                # if DEBUG_FPS:
                #     self.debug_fps()
                pg.display.set_caption("sb3topy (%.2f fps)" % self.clock.get_fps())

                pg.display.flip()
            # elif DEBUG_RECTS or DEBUG_FPS:
            #     self.sprites.draw(self.display.screen)
            #     if DEBUG_RECTS:
            #         self.debug_rects()
            #     if DEBUG_FPS:
            #         self.debug_fps()
            #     pg.display.flip()
            else:
                pg.display.update(self.sprites.draw(self.display.screen))
                pg.display.set_caption("sb3topy (%.2f fps)" % self.clock.get_fps())

            # Limit the frame rate
            if not TURBO_MODE:
                self.clock.tick(TARGET_FPS)
            else:
                self.clock.tick()

        pg.quit()

    def update_sprites(self):
        """Update dirty sprites"""
        any_dirty = False
        for target in self.util.targets.values():
            if target.dirty:
                any_dirty = True
                target.update(self.util)
            for clone in target.clones:
                if clone.dirty:
                    any_dirty = True
                    clone.update(self.util)
        return any_dirty

    def debug_rects(self):
        """Draws debug rects"""
        for sprite in self.sprites:
            if sprite.visible:
                pg.draw.rect(self.display.screen,
                             (255, 0, 0), sprite.rect, 1)
        pg.draw.circle(self.display.screen, (0, 0, 255),
                       self.display.rect.center, 4)
        pg.draw.circle(self.display.screen, (0, 255, 255),
                       (240+70, 180), 2)

    def debug_fps(self):
        """Draw debug fps"""
        font = pg.font.Font(None, 28)
        fps = "%.1f FPS" % self.clock.get_fps()
        pg.draw.rect(self.display.screen, (255, 255, 255),
                     pg.Rect((5, 5), font.size(fps)))
        self.display.screen.blit(font.render(
            fps, True, (0, 100, 20)), (5, 5))


class Display:
    """Handles the display"""
    size = DISPLAY_SIZE
    fullscreen = False
    scale = 1

    rect = None
    screen = None

    def __init__(self):
        self.setup_display()

    def setup_display(self):
        """Setup the display mode"""
        # Gets the rect and scale
        self.on_resize(self.size)

        # Get flags
        if self.fullscreen:
            flags = DISPLAY_FLAGS | pg.FULLSCREEN
        else:
            flags = DISPLAY_FLAGS | pg.RESIZABLE

        # Mouse should be visible
        pg.mouse.set_visible(True)

        # Setup and redraw screen
        self.screen = pg.display.set_mode(self.size, flags)
        self.screen.fill((250, 250, 250))

    def toggle_fullscreen(self):
        """Toggle between fullscreen and windowed mode"""
        # Restart the display
        pg.display.quit()
        pg.display.init()

        self.fullscreen = not self.fullscreen

        # Get the display size
        if self.fullscreen:
            info = pg.display.Info()
            self.size = (info.current_w // FS_SCALE,
                         info.current_h // FS_SCALE)
        else:
            self.size = DISPLAY_SIZE

        # Setup the screen again
        self.setup_display()

    def on_resize(self, size):
        """Recalculates the rect and scale"""
        # Get a centered rectangle to draw in
        if size[0] / STAGE_SIZE[0] < size[1] / STAGE_SIZE[1]:
            # Width is the limiting factor
            # height = scale * stage height
            scale = size[0] / STAGE_SIZE[0]
            rect = pg.Rect(
                0, (size[1] - scale * STAGE_SIZE[1]) // 2,
                size[0], scale * STAGE_SIZE[1])
        else:
            # Height is the limiting factor
            scale = size[1] / STAGE_SIZE[1]
            rect = pg.Rect(
                (size[0] - scale * STAGE_SIZE[0]) // 2,
                0, scale * STAGE_SIZE[0], size[1])

        # Save the calculated info
        self.size = size
        self.scale = scale
        self.rect = rect


def start(sprites):
    """Run the program"""
    runtime = None
    logging.basicConfig(level=logging.DEBUG)
    try:
        runtime = Runtime(sprites)
        asyncio.run(runtime.main_loop())
    finally:
        if runtime:
            runtime.quit()
