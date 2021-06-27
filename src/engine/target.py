"""
target.py

Contains the Target class

TODO Position clamping
TODO Random/mouse pos for glide/goto
TODO Warp deorator?
"""

# pylint: disable=protected-access

__all__ = ['Target']

import asyncio
import math
import time
import types
from itertools import zip_longest

import pygame as pg
from pygame.sprite import DirtySprite

from . import config
from .assets import Costumes, Sounds
from .pen import Pen


class Target:
    """Holds common code for targets

    The following attributes should be set by the child:
        variables - A dict of variables and their default values
        lists - A dict of lists and their default values
        costumes - A list of costume dicts
        sounds - A list of sound dicts
        costume - The intial costume #. Will be changed into a
            dict from costumes by Target.__init__
        hats - A dict of aync functions which should be started
            upon certain events. Must be initialized in __init__

    In addition to these, the following are managed by Target:
        sprite - A pygame sprite drawn to the screen
        dirty - Indicates the sprite's rect is dirty
        warp - Marks the Target as running "without screen refresh"
        warp_timer - Keeps track of time to ensure the target
            doesn't run longer than WARP_TIME
        costume_dict - Allows easy acess to costumes by name
        sounds_dict - Allows east acess to sounds by name
        effects - A dict which tracks costume effects

        need_redraw - A class method used to determine if
            any targets need to be redrawn

    TODO Additional Target properties
        draggable = False
        tempo = 60
        videoTransparency = 50
        videoState
        textToSpeechLanguage
    """

    # Clones for all sprites
    _clones = []

    # Type hints
    pen: Pen
    costume: Costumes
    sounds: Sounds

    def __init__(self, parent=None):

        self.hats = {}

        # Share the parent's clone list
        self.clones = parent.clones if parent else []
        self.parent = parent

        # Create the pygame sprite
        self.sprite = DirtySprite()
        self.sprite.target = self

        # Set dirty
        self.dirty = True

        # Clear effects
        self.effects = {}

        # Reset the task dict
        self._tasks = {}

        self.warp = False

        if parent is not None:
            # Copy variables from parent
            for name, var in parent.__dict__.items():
                if name.startswith('var'):
                    self.__dict__[name] = var
                elif name.startswith('list'):
                    self.__dict__[name] = var.copy()

            # Copy attributes
            self._xpos = parent._xpos
            self._ypos = parent._ypos
            self._direction = parent._direction
            self._shown = parent._shown
            self.pen = parent.pen.copy(self)

            self.costume = parent.costume.copy()
            self.sounds = parent.sounds.copy()

    @property
    def xpos(self):
        """Current x coordinate on the stage"""
        return self._xpos

    @xpos.setter
    def xpos(self, xpos):
        self._xpos = float(xpos)

        # Set dirty, move pen
        self.dirty = True
        if self.sprite.visible:
            Costumes.redraw_requested = True
        self.pen.move()

    @property
    def ypos(self):
        """Current y coordinate on the stage"""
        return float(self._ypos)

    @ypos.setter
    def ypos(self, ypos):
        self._ypos = ypos

        # Set dirty, move pen
        self.dirty = True
        if self.sprite.visible:
            Costumes.redraw_requested = True
        self.pen.move()

    @property
    def direction(self):
        """Current angle on the stage"""
        return self._direction

    @direction.setter
    def direction(self, degrees):
        """Sets and wraps the direction"""
        # Wrap the new direction
        self._direction = degrees - ((degrees + 179) // 360) * 360

        # Set dirty
        self.costume.dirty = True
        if self.sprite.visible:
            Costumes.redraw_requested = True

    def move(self, steps):
        """Moves steps in the current direction"""
        radians = math.radians(90-self._direction)
        self._xpos += steps * math.cos(radians)
        self._ypos += steps * math.sin(radians)

        # Set dirty and move the pen
        self.dirty = True
        if self.sprite.visible:
            Costumes.redraw_requested = True
        self.pen.move()

    def gotoxy(self, xpos, ypos):
        """Set xpos and ypos simultaneously"""
        self._xpos = xpos
        self._ypos = ypos

        # Set dirty, move pen
        self.dirty = True
        if self.sprite.visible:
            Costumes.redraw_requested = True
        self.pen.move()

    def goto(self, util, other):
        """Goto the position of another sprite"""
        # Copy the position of the other sprite
        other = util.sprites.targets.get(other)
        if other:
            self._xpos = other._xpos
            self._ypos = other._ypos

        # Set dirty
        self.dirty = True
        if self.sprite.visible:
            Costumes.redraw_requested = True
        self.pen.move()

    def point_towards(self, util, other):
        """Point towards another sprite"""
        # Get the position of other
        if other == "_mouse_":
            xpos = util.inputs.mouse_x
            ypos = util.inputs.mouse_y
        else:
            other = util.sprites.targets.get(other, self)
            xpos = other.xpos
            ypos = other.ypos

        # Calculate the angle to point in
        xpos -= self.xpos
        ypos -= self.ypos
        self._direction = 90 - math.degrees(math.atan2(ypos, xpos))

        # Set dirty
        self.costume.dirty = True
        if self.sprite.visible:
            Costumes.redraw_requested = True

    async def glide(self, duration, endx, endy):
        """Glides to a position"""
        start_time = time.monotonic()
        elapsed = 0
        startx, starty = self.xpos, self.ypos
        while elapsed < duration:
            elapsed = time.monotonic() - start_time
            frac = elapsed / duration
            self.xpos = startx + frac*(endx - startx)
            self.ypos = starty + frac*(endy - starty)

            # Set dirty, move pen
            self.dirty = True
            if self.sprite.visible:
                Costumes.redraw_requested = True
            self.pen.move()

            await self.yield_()
        self.xpos = endx
        self.ypos = endy

    async def glideto(self, util, duration, other):
        """Glides to the position of another sprite"""
        # Copy the position of the other sprite
        other = util.sprites.targets.get(other)
        if other:
            await self.glide(duration, other._xpos, other._ypos)

    def bounce_on_edge(self):
        """If on edge, bounce. Not implemented."""
        # TODO Bounce on edge

    @property
    def rotation_style(self):
        """The rotation style of the sprite"""
        return self.costume.rotation_style

    @rotation_style.setter
    def rotation_style(self, style):
        if style in ('all around', 'left-right', "don't rotate"):
            self.costume.rotation_style = style

        # Set dirty
        self.dirty = True
        if self.sprite.visible:
            Costumes.redraw_requested = True

    @property
    def size(self):
        """Current sprite size"""
        return self.costume.size

    @size.setter
    def size(self, value):
        self.costume._set_size(value)

        # Set dirty
        self.costume.dirty = True
        if self.sprite.visible:
            Costumes.redraw_requested = True

    def distance_to(self, util, other):
        """Calculate the distance to another target"""
        if other == "_mouse_":
            xpos = util.inputs.mouse_x
            ypos = util.inputs.mouse_y
        else:
            other = util.sprites.targets.get(other, self)
            xpos = other.xpos
            ypos = other.ypos
        return math.sqrt((self.xpos - xpos)**2 + (self.ypos - ypos)**2)

    def distance_to_point(self, point):
        """"Calculate the distance to a point (x, y)"""
        return math.sqrt((self.xpos - point[0])**2 + (self.ypos - point[1])**2)

    @property
    def shown(self):
        """Whether the sprite is currently visible"""
        # Getter not actually used
        return bool(self.sprite.visible)

    @shown.setter
    def shown(self, value):
        self.sprite.visible = bool(value)

        # Update dirty
        # sprite.dirty is set by the visible property
        Costumes.redraw_requested = True

    def start_event(self, util, name, restart=True):
        """Starts and returns a list of tasks"""
        tasks = []
        for cor, task in zip_longest(self.hats.get(name, []),
                                     self._tasks.get(name, [])):
            # Either restart the task or skip it
            if task is not None and not task.done():
                if not restart:
                    continue
                task.cancel()

            # Start the task
            tasks.append(asyncio.create_task(cor(util)))

        self._tasks[name] = tasks
        return tasks

    def stop_other(self):
        """Stop scripts other than the current"""
        this_task = asyncio.current_task()
        this_name = None

        for name in self._tasks:
            for task in self._tasks[name]:
                if task is this_task:
                    this_name = name
                else:
                    task.cancel()
            self._tasks[name] = []
        if this_name is None:
            print("Failed to find name for ", this_task)
        self._tasks[this_name] = [this_task]

    def update(self, display, create_mask=False):
        """Clears dirty flags by updating the rect and image"""
        # Update the image and rect, if necessary
        if self.costume.dirty:
            self._update_image(display)
            # Rect updated by _update_image

            self.costume.dirty = False
            self.dirty = False

        # Update the rect, if necessary
        elif self.dirty:
            self._update_rect(display)
            self.dirty = False

        # Update the sprite mask, if requested
        if create_mask and not self.sprite.mask:
            self.sprite.mask = pg.mask.from_surface(self.sprite.image)

    def _update_image(self, display):
        """Updates and transforms the sprites image"""
        # Update the image
        image = self.costume.get_image(display, self.direction)
        self.sprite.image = image
        self.sprite.mask = None

        # The rect now needs updating
        self._update_rect(display)

    def _update_rect(self, display):
        """Updates the rect to match the sprite's position and orientation"""
        # Rotate the rect properly
        offset = self.costume.costume['offset'] * self.costume.size/100
        offset = offset.rotate(self.direction-90)
        self.sprite.rect = self.sprite.image.get_rect(
            center=display.scale*(offset + pg.math.Vector2(
                self.xpos + config.STAGE_SIZE[0]//2,
                config.STAGE_SIZE[1]//2 - self.ypos)))

        # Move the rect by the stage offset
        self.sprite.rect.move_ip(*display.rect.topleft)

        # TODO Stage position restrictions
        # self.sprite.rect.clamp(display.rect)

        self.sprite.dirty = 1

    @types.coroutine
    def yield_(self):
        """Yields for a tick"""
        if not self.warp:
            yield

    async def sleep(self, delay):
        """Yields for at least 1 tick and delay"""
        # Force screen refresh before running again
        Costumes.redraw_requested = True

        # Sleep the correct amount of time
        await asyncio.sleep(delay)

    def get_touching(self, util, other):
        """Check if this sprite is touching another or its clones"""
        if other == "_mouse_":
            self.update(util.display, True)
            xpos, ypos = pg.mouse.get_pos()

            offset = self.sprite.rect.topleft
            offset = (xpos - offset[0], ypos - offset[1])
            try:
                return bool(self.sprite.mask.get_at(offset))
            except IndexError:
                return False

        other = util.sprites.targets.get(other)
        if not other:
            return False

        # Must update this sprite and the other before testing
        self.update(util.display, True)
        other.update(util.display, True)

        # Check if touching the original
        if pg.sprite.collide_mask(other.sprite, self.sprite):
            return True

        # Check if touching a clone
        for clone in other.clones:
            # Update the clones image too
            clone.update(util.display, True)

            # Check if touching a clone
            if pg.sprite.collide_mask(self.sprite, clone.sprite):
                return True
        return False

    def change_layer(self, util, value):
        """Moves number layers fowards"""
        group = util.sprites.group
        start = group.get_layer_of_sprite(self.sprite)
        top = group.get_top_layer()
        value = max(0, min(top, start + value)) - start
        self._move_layers(group, start, value)

        # Set dirty
        self.sprite.dirty = True
        if self.sprite.visible:
            Costumes.redraw_requested = True

    def front_layer(self, util):
        """Moves the sprite to the front layer"""
        group = util.sprites.group
        start = group.get_layer_of_sprite(self.sprite)
        top = group.get_top_layer()
        self._move_layers(group, start, top - start)

        # Set dirty
        self.sprite.dirty = True
        if self.sprite.visible:
            Costumes.redraw_requested = True

    def back_layer(self, util):
        """Moves the sprite to the back layer"""
        group = util.sprites.group
        start = group.get_layer_of_sprite(self.sprite)
        self._move_layers(group, start, -start)

        self.sprite.dirty = True
        if self.sprite.visible:
            Costumes.redraw_requested = True

    @staticmethod
    def _move_layers(group, start, value):
        """Used to switch sprite layers around"""
        sign = math.copysign(1, value)
        for i in range(int(abs(value))):
            group.switch_layer(
                start + i*sign,
                start + i*sign + sign
            )

    def create_clone_of(self, util, name):
        """Create a clone of this target"""
        if len(self._clones) < config.MAX_CLONES:
            # Get the target to clone
            if name == "_myself_":
                target = self
            else:
                target = util.sprites.targets.get(name)
                if target is None:
                    return

            # Get a layer for the clone
            # Move the top sprite where the clone will go,
            # Then move it back to the top leaving an empty space
            group = util.sprites.group
            top = group.get_top_layer()
            bottom = group.get_layer_of_sprite(self.sprite)
            top_sprite = group.get_top_sprite()
            self._move_layers(group, top, bottom-top)
            group.change_layer(top_sprite, top+1)

            # __class__ is the Sprite's subclass
            clone = target.__class__(target)
            self._clones.append(clone)  # Shared between targets
            target.clones.append(clone)
            group.add(clone.sprite, layer=bottom)
            util.events.send_to(util, clone, "clone_start")
        else:
            print("Max clones!")

    def delete_clone(self, util):
        """Delete this clone, will not delete original"""
        if self.parent:
            self._clones.remove(self)
            self.clones.remove(self)

            # Get rid of this sprite layer
            self.front_layer(util)
            self.sprite.kill()

            # Stop all running scripts
            for tasks in self._tasks.values():
                for task in tasks:
                    task.cancel()

            # Stop all playing sounds
            self.sounds.stop()
