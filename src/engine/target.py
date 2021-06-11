"""
target.py

Contains the Target class
"""

__all__ = ['Target']

import asyncio
import math
import time
from itertools import zip_longest

import pygame as pg

from . import config


class Target:
    """Holds common code for targets

    The following attributes should be set by the child:
        variables - A dict of variables and their default values
        lists - A dict of lists and their default values
        costumes - A list of costume dicts
        sounds - A list of sound dicts
        costume - The intial costume #. Will be changed into a
            dict from costumes by Target.__init__
        xpos, ypos, direction, size, visible
        hats - A dict of aync functions which should be started
            upon certain events. Must be initialized in __init__

    In addition to these, the following are managed by Target:
        sprite - A pygame sprite drawn to the screen
        dirty - Marks the Target as, 1. Having a dirty sprite,
            2. Having dirty sprite rect, 3. Having a dirty image
        warp - Marks the Target as running "without screen refresh"
        warp_timer - Keeps track of time to ensure the target
            doesn't run longer than WARP_TIME
        costume_dict - Allows easy acess to costumes by name
        sounds_dict - Allows east acess to sounds by name
        effects - A dict which tracks costume effects
    """

    # These values should be overriden

    # Clones for all sprites
    _clones = []

    xpos = 0
    ypos = 0
    direction = 90
    visible = True

    # draggable = False
    # tempo = 60
    # videoTransparency = 50
    # videoState
    # textToSpeechLanguage

    def __init__(self, parent=None):
        # These must be set by the subsclass
        self.costume = None
        self.sounds = None

        self.hats = {}

        # Share the parent's clone list
        self.clones = parent.clones if parent else []
        self.parent = parent

        # Create the pygame sprite
        self.sprite = pg.sprite.DirtySprite()
        self.sprite.target = self

        # 1 dirty sprite, 2 dirty rect, 3 dirty image
        self.dirty = 3
        self.warp = False
        self.warp_timer = 0

        # Clear effects
        self.effects = {}

        # Reset the task dict
        self._tasks = {}

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

    def update(self, display):
        """Clears the dirty flag by updating the sprite, rect and/or image"""
        # self.sprite.dirty = 1
        if self.sprite.visible != self.visible:  # dirty == 1
            self.sprite.visible = self.visible
            self.sprite.dirty = 1  # Not necesary, technically

        if self.dirty == 2:
            # Position change, only update rect
            self._update_rect(display)
        elif self.dirty == 3:
            # Image change, update image + rect
            self._update_image(display)
        self.dirty = 0

    def _update_image(self, display):
        """Updates and transforms the sprites image"""
        # Update the image
        image = self.costume.get_image(display, self.direction)
        self.sprite.image = image
        self.sprite.mask = pg.mask.from_surface(image)

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

    def set_dirty(self, dirty):
        """Indicate the sprite's appearance has changed"""
        if dirty > self.dirty:
            self.dirty = dirty

    async def yield_(self):
        """Yields if not in warp mode"""
        # If warp is on, avoid yielding
        if self.warp:
            if time.monotonic() - self.warp_timer > config.WARP_TIME:
                print("Overtime!")

                # Sleep handles warp and forces screen refresh
                await self.sleep(0)
        else:
            await asyncio.sleep(0)

    async def sleep(self, delay):
        """Yields for at least 1 tick and delay"""
        # Disable warp
        warp = self.warp
        self.warp = False

        # Force screen refresh before running again
        self.dirty = self.dirty or 1

        # Sleep the correct amount of time
        await asyncio.sleep(delay)

        # Reset warp
        self.warp = warp
        self.warp_timer = time.monotonic()

    def set_direction(self, degrees):
        """Sets and wraps the direction"""
        self.direction = degrees - ((degrees + 179) // 360) * 360

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
            self.set_dirty(2)
            await self.yield_()
        self.xpos = endx
        self.ypos = endy

    def move(self, steps):
        """Moves steps in the current direction"""
        radians = math.radians(90-self.direction)
        self.xpos += steps * math.cos(radians)
        self.ypos += steps * math.sin(radians)

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

    def get_touching(self, util, other):
        """Check if this sprite is touching another or its clones"""
        if other == "_mouse_":
            self.update(util.display)
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
        self.update(util.display)
        other.update(util.display)

        # Check if touching the original
        if pg.sprite.collide_mask(other.sprite, self.sprite):
            return True

        # Check if touching a clone
        for clone in other.clones:
            # Update the clones image too
            clone.update(util.display)

            # Check if touching a clone
            if pg.sprite.collide_mask(self.sprite, clone.sprite):
                return True
        return False

    def change_effect(self, effect, value):
        """Changes and wraps/clamps a graphics effect"""
        value = self.effects.get(effect, 0) + value
        self.set_effect(effect, value)

    def set_effect(self, effect, value):
        """Sets and wraps/clamps a graphics effect"""
        if effect == 'ghost':
            # Clamp between 0 and 100
            self.effects[effect] = min(max(value, 0), 100)
        elif effect == 'brightness':
            # Clamp between -100 and 100
            self.effects[effect] = min(max(value, -100), 100)
        elif effect == 'color':
            # Wrap between 0 and 200
            self.effects[effect] = value % 200
        # Other effects are not supported (yet)

    def clear_effects(self):
        """Defaults all graphic effects to 0"""
        self.effects = {}

    def change_layer(self, util, value):
        """Moves number layers fowards"""
        group = util.sprites.group
        start = group.get_layer_of_sprite(self.sprite)
        top = group.get_top_layer()
        value = max(0, min(top, start + value)) - start
        self._move_layers(group, start, value)

    def front_layer(self, util):
        """Moves the sprite to the front layer"""
        group = util.sprites.group
        start = group.get_layer_of_sprite(self.sprite)
        top = group.get_top_layer()
        self._move_layers(group, start, top - start)

    def back_layer(self, util):
        """Moves the sprite to the back layer"""
        group = util.sprites.group
        start = group.get_layer_of_sprite(self.sprite)
        self._move_layers(group, start, -start)

    @staticmethod
    def _move_layers(group, start, value):
        """Used to switch sprite layers around"""
        sign = math.copysign(1, value)
        for i in range(int(abs(value))):
            group.switch_layer(
                start + i*sign,
                start + i*sign + sign
            )

    async def _warp(self, awaitable):
        """Enables warp and disables it even if cancelled"""
        old_warp = self.warp
        self.warp = True
        if not old_warp:
            self.warp_timer = time.monotonic()
        await awaitable
        self.warp = old_warp

    def goto(self, util, other):
        """Goto the position of another sprite"""
        other = util.sprites.targets.get(other)
        if other:
            self.xpos = other.xpos
            self.ypos = other.ypos

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

    def point_towards(self, util, other):
        """Point towards another sprite"""
        if other == "_mouse_":
            xpos = util.inputs.mouse_x
            ypos = util.inputs.mouse_y
        else:
            other = util.sprites.targets.get(other, self)
            xpos = other.xpos
            ypos = other.ypos
        xpos -= self.xpos
        ypos -= self.ypos
        direction = 90 - math.degrees(math.atan2(ypos, xpos))
        # if ypos > 0:
        # direction += 180
        self.direction = direction
