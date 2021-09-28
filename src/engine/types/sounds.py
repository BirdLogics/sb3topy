"""
sounds.py

Contains the Sounds class.

TODO Consider using properties for the Sounds class.
"""

__all__ = ['Sounds']


import asyncio

import pygame as pg


class Sounds:
    """
    Handles sounds for a target

    Attributes:
        sounds: A dict referencing sounds (pg.mixer.Sound) by name

        sounds_list: Used to reference sounds by number

        volume: The current volume. If set directly, currently playing
            channels will not update. Use set_volume to update them.

        effects: A dict containing current sound effects

        _channels: A dict with sound channels as keys and waiting tasks
            as values. The channels are kept so the volume can be
            adjusted and the tasks are there to be cancelled.

    Class Attributes
        _cache: A shared dict containing md5ext / Sound pairs

        _all_sounds: Contains all sound tasks ready for cancellation
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
