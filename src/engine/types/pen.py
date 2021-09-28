"""
pen.py

Contains the Pen class and helper functions

TODO Consider using properties for the Pen?
"""

__all__ = ['Pen']


import pygame as pg

from ..operators import tonum
from ..config import STAGE_SIZE


class Pen:
    """
    Handles the pen for a sprite

    Attributes:
        target: The sprite of this Pen intance

        isdown: Whether the pen is down

        size: The current pen size

        color: The rgb pygame.Color instance

        hsva: Saved for greater accuracy

        shade: Legacy shade value

        position: Position since last moved

        _alpha_img:  Used internally for transparent blitting

        _scale: The screen scale

        _rect: The stage rect

    Class Attributes:
        image: Shared image of the pen

        dirty: Shared list of dirty rects, screen coords

        util: Shared for internal use, must be set
    """

    image: pg.Surface = None
    dirty = []

    _scale: float
    _rect: pg.Rect

    _alpha_img: pg.Surface

    def __init__(self, sprite):
        self.target = sprite

        self.isdown = False
        self.size = 1

        self.color = pg.Color("blue")
        self.alpha = 255
        self.hsva = self.color.hsva
        self.shade = 50

        self.position = (self.target.xpos + STAGE_SIZE[0]//2,
                         STAGE_SIZE[1]//2 - self.target.ypos)

    @classmethod
    def clear_all(cls):
        """Clear the pen image"""
        cls.image.fill((255, 255, 255, 0))
        cls.dirty = [cls.image.get_rect()]

    def down(self):
        """Puts the pen down"""
        self.isdown = True
        self.move(self.target.xpos, self.target.ypos)

    def up(self):  # pylint: disable=invalid-name
        """Puts the pen up"""
        self.isdown = False

    def stamp(self, util):
        """Stamp the sprite image"""
        self.target.update(util.display)
        rect = self.image.blit(
            self.target.sprite.image, self.target.sprite.rect.move(
                -self._rect.x, -self._rect.y))
        Pen.dirty.append(rect.move(self._rect.topleft))

        # pg.draw.rect(Pen.image, (0, 200, 100), rect, 1)

    def move(self, xpos, ypos):
        """Moves and draws with the pen"""
        if self.isdown:
            # Get the pen offset
            offset = 0.5 if self.size in (1, 3) else 0

            # Get new position
            end_pos = (xpos + STAGE_SIZE[0]//2,
                       STAGE_SIZE[1]//2 - ypos)

            size = max(1, round(self.size * self._scale))

            # Used to draw transparent lines in pg
            # TODO Pen transparency with colorkey faster?
            if self.color.a == 255:
                surf = Pen.image
            else:
                surf = Pen._alpha_img

            # Draw the line
            rect = pg.draw.line(
                surf, self.color,
                scale_point(self.position, self._scale, offset),
                scale_point(end_pos, self._scale, offset), size)
            rect.union_ip(pg.draw.circle(
                surf, self.color,
                scale_point(self.position, self._scale, offset), size/2))
            rect.union_ip(pg.draw.circle(
                surf, self.color,
                scale_point(end_pos, self._scale, offset), size/2))
            Pen.dirty.append(rect.move(self._rect.topleft))

            # Blit with blending transparency
            if self.color.a != 255:
                Pen.image.blit(surf, rect.topleft, rect)
                Pen._alpha_img.fill((0, 0, 0, 0), rect)

            # pg.draw.rect(Pen.image, (0, 200, 100), rect, 1)
            self.position = end_pos
        else:
            self.position = (xpos + STAGE_SIZE[0]//2,
                             STAGE_SIZE[1]//2 - ypos)

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
                self._hex_color(int(value.lstrip('#'), 16))
            except ValueError:
                self.color = pg.Color("black")
        else:
            self._hex_color(tonum(value))

        self.hsva = self.color.hsva
        self.shade = self.hsva[2] / 2

    def _hex_color(self, value):
        """Gets alpha from a int color"""
        # Rotate the 8 most significant bits to the end
        # Pygame reads RGBA rather than ARGB
        value = value % 0xFFFFFFFF
        self.color = pg.Color(
            ((value & 0xFFFFFF) << 8) + ((value >> 24) or 255))
        # self.alpha = (value >> 24) or 255

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
            self.hsva = (hue, sat, val, max(0, min(100, 100 - value)))
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
            self.hsva = (hue, sat, val, max(0, min(100, alp - value)))
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

        # Create the alpha img
        cls._alpha_img = pg.Surface(display.rect.size).convert_alpha()
        cls._alpha_img.fill((0, 0, 0, 0))

        # Save info about the display
        cls._rect = display.rect
        cls._scale = display.scale


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


def scale_point(point, disp_scale, offset):
    """Scales and rounds point to match the display"""
    return (round((point[0]+offset)*disp_scale),
            round((point[1]+offset)*disp_scale))
