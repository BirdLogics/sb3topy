"""
render.py

Contains the Display class for managing the screen.

Contains the Render class which handles drawing everything.
"""
import pygame as pg

from . import config
from .types import Pen


class Display:
    """
    Handles the display

    Attributes:
        size: The current screen size (w, h)

        scale: The current scale of a sigle pixel of the Stage

        fullscreen: Whether the screen is in fullscreen

        rect: Represents the stage position and size on the screen

        screen: The screen surface from pygame.display.set_mode
    """

    def __init__(self):
        self.size = config.DISPLAY_SIZE
        self.scale = 1
        self.fullscreen = False

        self.rect: pg.Rect
        self.screen: pg.Surface

        self.setup_display(config.DISPLAY_SIZE)

    def setup_display(self, size):
        """Setup the display mode"""
        # Get a centered rectangle to draw in
        if size[0] / config.STAGE_SIZE[0] < size[1] / config.STAGE_SIZE[1]:
            # Width is the limiting factor
            # height = scale * stage height
            scale = size[0] / config.STAGE_SIZE[0]
            rect = pg.Rect(
                0, (size[1] - scale * config.STAGE_SIZE[1]) // 2,
                size[0], scale * config.STAGE_SIZE[1])
        else:
            # Height is the limiting factor
            scale = size[1] / config.STAGE_SIZE[1]
            rect = pg.Rect(
                (size[0] - scale * config.STAGE_SIZE[0]) // 2,
                0, scale * config.STAGE_SIZE[0], size[1])

        # Save the calculated info
        self.size = size
        self.scale = scale
        self.rect = rect

        # Get flags
        if self.fullscreen:
            flags = config.DISPLAY_FLAGS | pg.FULLSCREEN
        else:
            flags = config.DISPLAY_FLAGS | pg.RESIZABLE

        # Mouse should be visible
        pg.mouse.set_visible(True)

        # Setup and redraw screen
        self.screen = pg.display.set_mode(self.size, flags)
        self.screen.fill((250, 250, 250))
        pg.display.flip()
        Pen.resize(self)

    def toggle_fullscreen(self):
        """Toggle between fullscreen and windowed mode"""
        # Restart the display
        pg.display.quit()
        pg.display.init()

        self.fullscreen = not self.fullscreen

        # Get the display size
        if self.fullscreen:
            info = pg.display.Info()
            size = (info.current_w // config.FS_SCALE,
                    info.current_h // config.FS_SCALE)
        else:
            size = config.DISPLAY_SIZE

        # Setup the screen again
        self.setup_display(size)

    def video_resize(self, event):
        """Recalculates the rect and scale"""
        # Resize the display
        self.setup_display((event.w, event.h))


class Render:
    """
    Handles drawing the screen

    Attributes:
        group: pygame LayeredDirty sprite group

        stage: The stage Sprite

        rects: A list of dirty rects to update

        font: Used for debug text
    """

    def __init__(self, sprites):
        self.group = sprites.group
        self.stage = sprites.stage.sprite
        self.group.set_timing_treshold(config.FLIP_THRESHOLD)

        self.rects = []

        # Debug font
        self.font = pg.font.Font(None, 28)

    def draw(self, display):
        """Handles drawing everything"""
        # Update the background, if necessary
        if self.stage.dirty:
            # Create a new bg_image
            bg_image = pg.Surface(display.size).convert()
            bg_image.fill((255, 255, 255))
            bg_image.blit(self.stage.image, display.rect.topleft)
            self.stage.dirty = 0

            # Draw the pen
            bg_image.blit(Pen.image, display.rect.topleft)
            Pen.dirty = []

            # Update the DirtySprite group
            # Even when passed screen, group.clear
            # doesn't draw anything. Using set_clip
            # forces a full redraw next call of draw
            self.group.clear(None, bg_image)
            self.group.set_clip(display.rect)

        elif Pen.dirty:
            # Create a new bg_image
            bg_image = pg.Surface(display.size).convert()
            bg_image.fill((255, 255, 255))
            bg_image.blit(self.stage.image, display.rect.topleft)
            bg_image.blit(Pen.image, display.rect.topleft)
            self.group.clear(None, bg_image)

            # Update rects on the screen
            for rect in Pen.dirty:
                self.group.repaint_rect(rect)

        # Draw the sprites
        self.rects.extend(self.group.draw(display.screen))

    def draw_fps(self, display, clock):
        """Draws fps to the screen"""
        text = "%.1f FPS" % clock.get_fps()
        self.draw_text(display, text, (5, 5))

    def draw_sprite_rects(self, display):
        """Draws rects around every sprite"""
        # Draw rects
        for sprite in self.group:
            if sprite.visible:
                pg.draw.rect(
                    display.screen, (0, 0, 255), sprite.rect, 1)

        # Draw the stage center
        pg.draw.circle(display.screen, (0, 0, 255),
                       display.rect.center, 4)

    def draw_redraw_rects(self, display):
        """Draws rects in self.rects"""
        for rect in self.rects:
            pg.draw.rect(display.screen, (255, 100, 0), rect, 1)

    @staticmethod
    def draw_pen_rects(display):
        """Draws rects in Pen.dirty"""
        for rect in Pen.dirty:
            pg.draw.rect(display.screen, (0, 200, 100), rect, 1)

    def draw_text(self, display, text, pos, color=(0, 200, 200)):
        """Draws text for a single frame"""
        # Mark the drawn area as dirty
        rect = pg.Rect(pos, self.font.size(text))
        self.group.repaint_rect(rect)
        self.rects.append(rect)

        # Draw a rect for text off the stage
        if not display.rect.contains(rect):
            pg.draw.rect(display.screen, (255, 255, 255), rect)
            surf = self.font.render(text, True, color, (255, 255, 255))
        else:
            surf = self.font.render(text, True, color)
        display.screen.blit(surf, pos)

    def flip(self):
        """Update the display after drawing"""
        pg.display.update(self.rects)
        # pg.display.flip()
        self.rects = []
        Pen.dirty = []

    def dirty_all(self):
        """Marks all sprites as dirty"""
        # Resize sprites, stage, and Pen
        for sprite in self.group.sprites():
            sprite.target.costume.dirty = True
        self.stage.target.costume.dirty = True
