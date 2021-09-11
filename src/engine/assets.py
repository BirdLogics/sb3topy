"""
assets.py

Contains classes used to manage assets.
"""

__all__ = ['Sounds', 'Costumes']


import asyncio

import pygame as pg

from .config import STAGE_SIZE


class Sounds:
    """
    Handles sounds for a target

    sounds - A dict referencing sounds (pg.mixer.Sound) by name
    sounds_list - Used to reference sounds by number
    volume - The current volume. If set directly, currently playing
        channels will not update. Use set_volume to update them.
    effects - A dict containing current sound effects

    _channels - A dict with sound channels as keys and waiting
        tasks as values. The channels are kept so the volume can be
        adjusted and the tasks are there to be cancelled.

    _cache - A shared dict containing md5ext / Sound pairs
    _all_sounds - Contains all sound tasks ready for cancellation
    """

    _cache = {}
    _all_sounds = {}

    def __init__(self, volume, sounds, copy_dict=None):
        if copy_dict is None:
            self.sounds = {}
            self.sounds_list = []

            for asset in sounds:
                self.sounds[asset['name']] = self._load_sound(asset['path'])
                self.sounds_list.append(self.sounds[asset['name']])
        else:
            self.sounds = copy_dict
            self.sounds_list = sounds

        self.volume = volume
        self.effects = {}
        self._channels = {}

    def _load_sound(self, path):
        """Load a sound or retrieve it from cache"""
        sound = self._cache.get(path)
        if not sound:
            sound = pg.mixer.Sound("assets/" + path)
            self._cache[path] = sound
        return sound

    def set_volume(self, volume):
        """Sets the volume and updates it for playing sounds"""
        self.volume = max(0, min(100, volume))
        self._update_volume()

    def change_volume(self, volume):
        """Changes and updates the volume by an amount"""
        self.set_volume(self.volume + volume)

    def _update_volume(self):
        """Updates the volume for every channel"""
        lvol, rvol = self._get_volume()
        for channel in self._channels:
            channel.set_volume(lvol, rvol)

    def _get_volume(self):
        """Gets the left and right volume levels"""
        pan = self.effects.get("pan", 0)
        return (max(0, min(100, self.volume - pan)) / 100,
                max(0, min(100, self.volume + pan)) / 100)

    def play(self, name):
        """Plays the sound and returns an awaitable."""
        # Get the sound from name or number
        sound = self.sounds.get(name)
        if not sound:
            try:
                name = round(float(name)) - 1
                if 0 < name < len(self.sounds_list):
                    sound = self.sounds_list[name]
                else:
                    sound = self.sounds_list[0]
            except ValueError:
                pass
            except OverflowError:  # round(Infinity)
                pass

        # Play the sound
        if sound:
            # Stop the sound if it is already playing
            for channel, task in self._channels.items():
                if channel.get_sound == sound:
                    channel.stop()
                    task.cancel()

            # Try to play it on an open channel
            channel = pg.mixer.find_channel()
            if channel:
                return asyncio.create_task(
                    self._handle_channel(sound, channel))
        return asyncio.create_task(asyncio.sleep(0))

    async def _handle_channel(self, sound, channel):
        """Saves the channel and waits for it to finish"""
        # Start the sound
        delay = sound.get_length()
        channel.set_volume(*self._get_volume())
        channel.play(sound)

        # Create a cancelable waiting task
        task = asyncio.create_task(asyncio.sleep(delay))
        self._channels[channel] = task
        self._all_sounds[channel] = task

        # Pop the channel once it is done or cancelled
        await asyncio.wait((task,))
        self._channels.pop(channel)
        self._all_sounds.pop(channel)

    @classmethod
    def stop_all(cls):
        """Stops all sounds for all sprites"""
        for channel, task in cls._all_sounds.items():
            task.cancel()
            channel.stop()

    def stop(self):
        """Stop all sounds for this sprite"""
        for channel, task in self._channels.items():
            task.cancel()
            channel.stop()

    def copy(self):
        """Returns a copy of this Sounds"""
        return Sounds(self.volume, self.sounds_list, self.sounds)

    def set_effect(self, effect, value):
        """Set a sound effect"""
        if effect == 'pan':
            self.effects['pan'] = max(-100, min(100, value))
            self._update_volume()

    def change_effect(self, effect, value):
        """Change a sound effect"""
        value = self.effects.get(effect, 0) + value
        self.set_effect(effect, value)

    def clear_effects(self):
        """Clear sound effects"""
        self.effects = {}
        self._update_volume()


# Costume = namedtuple(
#     'Costume', ['name', 'number', 'image',
#                 'offset', 'scale', 'center'])


class Costumes:
    """
    Handles costumes for a target

    costumes - A dict referencing costume by name
    costumes_list - Used to reference costumes by number

    name - The name of the current costume, readonly
    number - The number of the current costume, readonly

    size - The current costume size
    rotation_style - The current rotation style

    target - The parent target, used to set dirty TODO Here

    effects - A dict of current effects and values

    dirty - Whether the image needs to be updated

    redraw_requested - Class method, used to indicate
        a sprite has requested a screen redraw
    _cache - A shared cache containing loaded images
    """

    redraw_requested = False
    _cache = {}

    def __init__(self, costume_number, size,
                 rotation_style, costumes, copy_dicts=None):
        self.number = costume_number + 1
        self.costume = costumes[costume_number]
        self._size = size
        self.rotation_style = rotation_style

        self.dirty = True

        self.costume_list = costumes

        # Last gotten image without effects
        # Used to get the sprite mask
        self.last_image: pg.Surface = None

        if copy_dicts is None:
            self.effects = {}
            self.costumes = {}

            # Initialize the costume lists
            for index, asset in enumerate(costumes):
                # Load the image
                asset['image'] = self._load_image(asset['path'])

                # Calculate the rotation offset
                center = pg.math.Vector2(asset['image'].get_size()) / 2
                asset['offset'] = pg.math.Vector2(asset['center'])
                asset['offset'] *= -1
                asset['offset'] += center
                asset['offset'] /= asset['scale']

                # Add the costume to the dict
                asset['number'] = index + 1
                self.costumes[asset['name']] = asset
        else:
            self.costumes = copy_dicts[0]
            self.effects = copy_dicts[1]

    def _load_image(self, path):
        """Loads an image or retrieves it from cache"""
        image = self._cache.get(path)
        if not image:
            image = pg.image.load("assets/" + path).convert_alpha()
            self._cache[path] = image
        return image

    def switch(self, costume):
        """Sets the costume"""
        asset = self.costumes.get(costume)
        if asset:
            self.costume = asset
            self.number = asset['number']
        else:
            try:
                self.number = (round(float(costume)) %
                               len(self.costume_list))
                self.costume = self.costume_list[self.number - 1]
            except ValueError:
                pass
            except OverflowError:
                pass

        # Set dirty
        self.dirty = True
        Costumes.redraw_requested = True

    def next(self):
        """Go to the next costume"""
        self.number += 1
        if self.number > len(self.costume_list):
            self.number = 1
        self.costume = self.costume_list[self.number - 1]

        # Set dirty
        self.dirty = True
        Costumes.redraw_requested = True

    @property
    def size(self):
        """The current costume size"""
        return self._size

    @size.setter
    def size(self, value):
        image = self.costume['image']

        cost_w = image.get_width() / self.costume['scale']
        cost_h = image.get_height() / self.costume['scale']

        min_scale = min(1, max(5 / cost_w, 5 / cost_h))
        max_scale = min(1.5 * STAGE_SIZE[0] / cost_w,
                        1.5 * STAGE_SIZE[1] / cost_h)

        self._size = max(min_scale, min(max_scale, value/100)) * 100

        # Set dirty
        self.dirty = True
        Costumes.redraw_requested = True

    @property
    def name(self):
        """The name of the current costume"""
        return self.costume['name']

    def set_effect(self, effect, value):
        """Sets and wraps/clamps a graphics effect"""
        if effect == 'ghost':
            self.effects[effect] = min(max(value, 0), 100)
        elif effect == 'brightness':
            self.effects[effect] = min(max(value, -100), 100)
        elif effect == 'color':
            self.effects[effect] = value % 200

        # Set dirty
        self.dirty = True
        Costumes.redraw_requested = True

    def change_effect(self, effect, value):
        """Changes and wraps/clamps a graphics effect"""
        value = self.effects.get(effect, 0) + value
        self.set_effect(effect, value)

    def clear_effects(self):
        """Clear all graphic effects"""
        self.effects.clear()

        # Set dirty
        self.dirty = True
        self.redraw_requested = True

    def _apply_effects(self, image: pg.Surface):
        """Apply current effects to an image"""
        # Brighten/Darken
        brightness = self.effects.get('brightness', 0)
        if brightness > 0:
            brightness = 255 * brightness / 100
            image.fill(
                (brightness, brightness, brightness),
                special_flags=pg.BLEND_RGB_ADD)
        elif brightness < 0:
            brightness = -255 * brightness / 100
            image.fill(
                (brightness, brightness, brightness),
                special_flags=pg.BLEND_RGB_SUB)

        # Transparency
        ghost = self.effects.get('ghost', 0)
        if ghost:
            ghost = 255 - 255 * ghost / 100
            image = image.copy()
            image.fill(
                (255, 255, 255, ghost),
                special_flags=pg.BLEND_RGBA_MULT)

        # Hue change
        color = self.effects.get('color', 0)
        if color:
            color = 360 * color / 200
            image = hue_effect(image, color)

        return image

    def get_image(self, display, direction):
        """Get the current image with a size and direction"""
        # Get the base image
        image = self.costume['image']

        # Scale the image
        scale = self._size/100 / \
            self.costume['scale'] * display.scale
        image = pg.transform.smoothscale(
            image, (min(9000, max(4, int(image.get_width() * scale))),
                    min(9000, max(4, int(image.get_height() * scale))))
        )

        # Rotate the image
        if self.rotation_style == "all around":
            # Segmentation fault here if image size is too small
            image = pg.transform.rotate(image, 90-direction)
        elif self.rotation_style == "left-right":
            if direction > 0:
                image = pg.transform.flip(image, True, False)

        # Save the image without effects
        self.last_image = image

        # Apply effects
        image = self._apply_effects(image)

        return image

    def copy(self):
        """Return a copy of this list"""
        cost = Costumes(self.number - 1, self._size,
                        self.rotation_style, self.costume_list,
                        (self.costumes, self.effects.copy()))
        return cost

    def get_mask(self):
        """Get a sprite mask using the last gotten image without effects"""
        return pg.mask.from_surface(self.last_image)


def hue_effect(src_image, value):
    """
    Changes the hue of an image for the color effect
    Value should be between 0 and 360. Coverts the image
    to an 8-bit surface and adjusts the color palette.
    Transparency is copied first to preserve it.
    """

    # Get a copy of the alpha channel
    transparency = src_image.convert_alpha()
    transparency.fill((255, 255, 255, 0),
                      special_flags=pg.BLEND_RGBA_MAX)

    # Get an 8-bit surface with a color palette
    # Workaround, see Pygame Issue #2477
    image = pg.Surface(src_image.get_size(), depth=8)
    image.blit(src_image, (0, 0))

    # Change the hue of the palette
    for index in range(256):
        # Get the palette color at index
        color = pg.Color(*image.get_palette_at(index))

        # Get the new hue
        hue = color.hsva[0] + value
        if hue > 360:
            hue -= 360

        # Update the hue
        color.hsva = (hue, *color.hsva[1:3])
        image.set_palette_at(index, color)

    # Return the image transparency
    image.set_alpha()
    image = image.convert_alpha()
    image.blit(transparency, (0, 0), special_flags=pg.BLEND_RGBA_MULT)

    return image
