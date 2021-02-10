"""
pen.py

Contains the Pen class
"""

__all__ = ['Pen']

import pygame as pg

from .config import STAGE_SIZE
from .blockutil import tonum


class Pen:
    """
    Handles the pen for a sprite

    image - Shared image of the pen
    dirty - Shared list of dirty rects, screen coords
    util - Shared for internal use, must be set

    target - The sprite of this Pen intance
    isdown - Whether the pen is down
    size - The current pen size

    color - The rgb pygame.Color instance
    hsva - Saved for greater accuracy
    shade - Legacy shade value

    position - Position since last moved
    """

    # Shared image for all sprites
    image = None
    dirty = []
    util = None

    def __init__(self, sprite):
        self.target = sprite

        self.isdown = False
        self.size = 1

        self.color = pg.Color("blue")
        self.hsva = self.color.hsva
        self.shade = 50

        self.position = (self.target.xpos + STAGE_SIZE[0]//2,
                         STAGE_SIZE[1]//2 - self.target.ypos)

    @classmethod
    def clear_all(cls):
        """Clear the pen image"""
        cls.image.fill((255, 255, 255, 0))
        cls.dirty = [cls.image.get_rect()]

    def down(self, util):
        """Puts the pen down"""
        self.move(util)
        self.isdown = True

    def up(self):  # pylint: disable=invalid-name
        """Puts the pen up"""
        self.isdown = False

    def stamp(self, util):
        """Stamp the sprite image"""
        disp_rect = util.display.rect
        self.target.update(util.display)
        rect = self.image.blit(
            self.target.sprite.image, self.target.sprite.rect.move(
                -disp_rect.x, -disp_rect.y))
        Pen.dirty.append(rect.move(disp_rect.topleft))

        # pg.draw.rect(Pen.image, (0, 200, 100), rect, 1)

    def move(self, util):
        """Moves and draws with the pen"""
        # Get new position
        end_pos = (self.target.xpos + STAGE_SIZE[0]//2,
                   STAGE_SIZE[1]//2 - self.target.ypos)
        if self.isdown:
            disp_scale = util.display.scale
            size = round(self.size * disp_scale / 2)

            # Draw the line
            rect = pg.draw.line(
                Pen.image, self.color,
                scale_point(self.position, disp_scale),
                scale_point(end_pos, disp_scale), size * 2)
            rect.union_ip(pg.draw.circle(
                Pen.image, self.color,
                scale_point(self.position, disp_scale), size))
            rect.union_ip(pg.draw.circle(
                Pen.image, self.color,
                scale_point(end_pos, disp_scale), size))
            Pen.dirty.append(rect.move(util.display.rect.topleft))

            # pg.draw.rect(Pen.image, (0, 200, 100), rect, 1)

        self.position = end_pos

    def set_size(self, value):
        """Sets and clamps the pen size"""
        self.size = max(1, min(1200, value))

    def change_size(self, value):
        """Changes and clamps the pen size"""
        self.set_size(self.size + value)

    def exact_color(self, value):
        """Sets the exact pen color"""
        # Translate the color
        if isinstance(value, str) and value.startswith("#"):
            try:
                self.color = pg.Color(value)
            except ValueError:
                self.color = pg.Color("black")
        else:
            self.color = pg.Color(tonum(value) % 0xFFFFFFFF)
        self.hsva = self.color.hsva
        self.shade = self.hsva[2] / 2

    def set_color(self, prop, value):
        """Sets a certain color property"""
        # Round as a workaround to pygame bug
        # Color(128, 196, 0).hsva[1] > 100
        hue, sat, val, alp = map(round, self.hsva, (9, 9, 9, 9))
        if prop == "color":
            self.hsva = (value*3.6 % 360, sat, val, alp)
        elif prop == "saturation":
            self.hsva = (hue, value % 100, val, alp)
        elif prop == "brightness":
            self.hsva = (hue, sat, max(0, min(100, value)), alp)
        elif prop == "transparency":
            self.hsva = (hue, sat, val, value % 100)
        else:
            print("Invalid color property ", prop)
        self.color.hsva = self.hsva

    def change_color(self, prop, value):
        """Changes a certain color property"""
        hue, sat, val, alp = map(round, self.hsva, (9, 9, 9, 9))
        if prop == "color":
            self.hsva = ((hue+(value*3.6)) % 360, sat, val, alp)
        elif prop == "saturation":
            self.hsva = (hue, max(0, min(100, sat + value)), val, alp)
        elif prop == "brightness":
            self.hsva = (hue, sat, max(0, min(100, val+value)), alp)
        elif prop == "transparency":
            self.hsva = (hue, sat, val, max(0, min(100, alp + value)))
        else:
            print("Invalid color property ", prop)
        self.color.hsva = self.hsva

    def set_shade(self, value):
        """Legacy set shade"""
        # Wrap the shade value
        # Python mod is different from JS
        shade = value % 200
        self.shade = shade
        self._legacy_update_color()

    def change_shade(self, value):
        """Legacy change shade"""
        self.set_shade(self.shade + value)

    def set_hue(self, hue):
        """Legacy set color"""
        self.set_color("color", hue/2)
        self._legacy_update_color()

    def change_hue(self, value):
        """Legacy change color"""
        self.change_color("color", value/2)
        self._legacy_update_color()

    def _legacy_update_color(self):
        """Update color using shade"""
        self.color.hsva = (self.hsva[0], 100, 100, self.hsva[3])
        shade = (200 - self.shade) if self.shade > 100 else self.shade
        if shade < 50:
            self.color = lerp((0, 0, 0), self.color, (10 + shade) / 60)
        else:
            self.color = lerp(self.color, (255, 255, 255), (shade - 50) / 60)
        self.hsva = self.color.hsva

    def copy(self, clone):
        """Create a copy of the pen"""
        pen = Pen(clone)
        pen.isdown = self.isdown
        pen.color = pg.Color(self.color.r, self.color.g,
                             self.color.b, self.color.a)
        pen.size = self.size
        return pen

    @classmethod
    def resize(cls, display):
        """Create/resize the Pen image"""
        if cls.image is None:
            cls.image = pg.Surface(display.rect.size).convert_alpha()
            cls.scale = display.scale
            cls.clear_all()
        else:
            cls.image = pg.transform.smoothscale(cls.image, display.rect.size)
            cls.dirty = []


def lerp(color0, color1, fraction1):
    """Linear interpolation of colors"""
    if fraction1 <= 0:
        return pg.Color(*color0)
    if fraction1 >= 1:
        return pg.Color(*color1)
    fraction0 = 1 - fraction1
    return pg.Color(
        round((fraction0 * color0[0]) + (fraction1 * color1[0])),
        round((fraction0 * color0[1]) + (fraction1 * color1[1])),
        round((fraction0 * color0[2]) + (fraction1 * color1[2]))
    )


def scale_point(point, disp_scale):
    """Scales and rounds point to match the display"""
    return (round(point[0]*disp_scale),
            round(point[1]*disp_scale))
