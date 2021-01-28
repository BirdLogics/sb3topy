"""
pen.py

Contains the Pen class
"""

__all__ = ['Pen']

import pygame as pg

from .config import STAGE_SIZE
from .util import tonum


class Pen:
    """Handles the pen for a sprite"""

    # Shared image for all sprites
    image = None
    dirty = False

    def __init__(self, util, sprite):
        self.util = util
        self.display = util.runtime.display
        self.target = sprite
        self.isdown = False
        self.color = pg.Color("blue")
        self.size = 1
        self.position = (self.target.xpos + STAGE_SIZE[0]//2,
                         STAGE_SIZE[1]//2 - self.target.ypos)

        if Pen.image is None:
            Pen.image = pg.Surface(self.display.rect.size).convert_alpha()
            Pen.scale = self.display.scale
            self.clear_all()

    @classmethod
    def resize(cls, size):
        """Resize the Pen image"""
        cls.image = pg.transform.smoothscale(cls.image, size)
        cls.dirty = True

    @classmethod
    def clear_all(cls):
        """Clear the pen image"""
        cls.image.fill((255, 255, 255, 0))
        cls.dirty = True

    def down(self):
        """Puts the pen down"""
        self.isdown = True
        self.move()

    def up(self):
        """Puts the pen up"""
        self.isdown = False

    def move(self):
        """Moves and draws with the pen"""
        end_pos = (self.target.xpos + STAGE_SIZE[0]//2,
                   STAGE_SIZE[1]//2 - self.target.ypos)
        if self.isdown:
            size = round(self.size * self.display.scale / 2)
            pg.draw.line(Pen.image, self.color, self._scale_point(
                self.position), self._scale_point(end_pos), size * 2)
            pg.draw.circle(Pen.image, self.color,
                           self._scale_point(self.position), size)
            pg.draw.circle(Pen.image, self.color,
                           self._scale_point(end_pos), size)
            Pen.dirty = True
        self.position = end_pos

    def _scale_point(self, point):
        """Scales and rounds point to match the display"""
        return (round(point[0]*self.display.scale),
                round(point[1]*self.display.scale))

    def stamp(self):
        """Stamp the sprite image"""
        self.target.update(self.util)
        self.image.blit(
            self.target.sprite.image, self.target.sprite.rect.move(
                -self.display.rect.x, -self.display.rect.y))
        Pen.dirty = True

    def change_size(self, value):
        """Changes and clamps the pen size"""
        self.set_size(self.size + value)

    def set_size(self, value):
        """Sets and clamps the pen size"""
        self.size = max(1, min(1200, value))

    def set_color(self, value):
        """Sets the exact pen color"""
        # Translate the color
        if isinstance(value, str) and value.startswith("#"):
            try:
                self.color = pg.Color(value)
            except ValueError:
                self.color = pg.Color("black")
        else:
            self.color = pg.Color(tonum(value) % 0xFFFFFFFF)

    def set_hue(self, value):
        """Set and wrap pen color"""
        _, sat, val, alp = self.color.hsva
        self.color.hsva = (value*3.6 % 360, sat, val, alp)

    def change_hue(self, value):
        """Change and wrap pen color"""
        hue, sat, val, alp = self.color.hsva
        self.color.hsva = ((hue + value*3.6) % 360, sat, val, alp)

    def set_saturation(self, value):
        """Set and wrap pen saturation"""
        hue, _, val, alp = self.color.hsva
        self.color.hsva = (hue, value % 100, val, alp)

    def change_saturation(self, value):
        """Change and wrap pen saturation"""
        hue, sat, val, alp = self.color.hsva
        self.color.hsva = (hue, (sat + value) % 100, val, alp)

    def set_brightness(self, value):
        """Set and wrap pen brightness"""
        hue, sat, _, alp = self.color.hsva
        self.color.hsva = (hue, sat, value % 100, alp)

    def change_brightness(self, value):
        """Change and wrap pen brightness"""
        hue, sat, val, alp = self.color.hsva
        self.color.hsva = (hue, sat, (val + value) % 100, alp)

    def set_alpha(self, value):
        """Set and wrap pen transparency"""
        hue, sat, val, _ = self.color.hsva
        self.color.hsva = (hue, sat, val, value % 100)

    def change_alpha(self, value):
        """Change and wrap pen transparency"""
        hue, sat, val, alp = self.color.hsva
        self.color.hsva = (hue, sat, val, (alp + value) % 100)

    def color_set(self, prop, value):
        """Sets a certain color property"""
        if prop == "color":
            self.set_color(value)
        elif prop == "saturation":
            self.set_saturation(value)
        elif prop == "brightness":
            self.set_brightness(value)
        elif prop == "transparency":
            self.set_alpha(value)
        else:
            print("Invalid color property ", prop)

    def color_change(self, prop, value):
        """Changes a certain color property"""
        if prop == "color":
            self.change_hue(value)
        elif prop == "saturation":
            self.change_saturation(value)
        elif prop == "brightness":
            self.change_brightness(value)
        elif prop == "transparency":
            self.change_alpha(value)
        else:
            print("Invalid color property ", prop)

    def set_shade(self, value):
        """Sets and wraps pen shade"""
        # TODO Pen shade

    def change_shade(self, value):
        """Changes and wraps pen shade"""

    def copy(self, clone):
        """Create a copy of the pen"""
        pen = Pen(self.util, clone)
        pen.isdown = self.isdown
        pen.color = pg.Color(self.color.r, self.color.g,
                             self.color.b, self.color.a)
        pen.size = self.size
        return pen
