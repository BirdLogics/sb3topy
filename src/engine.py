#!/usr/bin/env python3
"""


Contains the framework which allows the project to run.
Requires Python 3.x and pygame.

USERNAME - The value provided by the username block
TARGET_FPS - The target number of frames per second. A delay
    is used to meet this number.
TURBO_MODE - Runs quickly regardless of display changes
WORK_TIME - How long to run blocks each frame (seconds)
WARP_TIME - How long custom blocks are allowed to run
    without refresh (seconds)

STAGE_SIZE - The size of the stage
DISPLAY_SIZE - The initial window size
DISPLAY_FLAGS - Passed to pygame.display.set_mode. Do not use FULLSCREEN
    or RESIZABLE; these are managed automatically.
FS_SCALE - Changes the display size in fullscreen, potentially increacing
    performance at the cost of quality. With a factor of 2, the window
    size is half that of your computer, changing your resolution.

AUDIO_CHANNELS - The number of audio channels created for the pygame mixer

KEY_MAP - Maps pygame keys to their names in the project
"""

import asyncio
import logging
import math
import random
import time
from itertools import zip_longest

import pygame as pg

USERNAME = ""

TARGET_FPS = 31
TURBO_MODE = False
WORK_TIME = 1 / 60
WARP_TIME = 0.5

STAGE_SIZE = (480, 360)
DISPLAY_SIZE = (480, 360)
DISPLAY_FLAGS = pg.DOUBLEBUF | pg.HWSURFACE
FS_SCALE = 1

AUDIO_CHANNELS = 8
MAX_CLONES = 300

DEBUG_RECTS = False
DEBUG_FPS = True


KEY_MAP = {
    pg.K_SPACE: "space",
    pg.K_UP: "up arrow",
    pg.K_DOWN: "down arrow",
    pg.K_RIGHT: "right arrow",
    pg.K_LEFT: "left arrow",
    pg.K_RETURN: "enter"
}


DISPLAY_SCALE = 1


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

        # Save the calculate info
        self.size = size
        self.scale = scale
        self.rect = rect


class BlockUtil:
    """Useful functions for targets to interface with Runtime"""
    down_keys = []
    targets = {}
    _timer = time.monotonic()
    runtime = None
    cache = None
    stage = None
    sprites = None
    _broadcasts = {}

    def __init__(self, runtime):
        self.runtime = runtime
        self.input = Inputs(runtime, self)

    def send_event(self, event, restart=False):
        """Starts an event for all sprites"""
        # Get sprites in the recieving order
        sprites = self.sprites.sprites()
        sprites.reverse()

        # Get a list of tasks to runs
        tasks = []
        for sprite in sprites:
            tasks.extend(sprite.target.start_event(self, event, restart))
        tasks.extend(self.stage.start_event(self, event, restart))

        # Return an awaitable task
        return asyncio.create_task(self._handle_tasks(tasks))

    def send_event_to(self, event, target):
        """Starts an event for a single target"""
        tasks = target.start_event(self, event)
        return asyncio.create_task(self._handle_tasks(tasks))

    async def _handle_tasks(self, tasks):
        """Waits on a list of tasks and catches any errors"""
        # Handle an empty list
        if not tasks:
            return

        # Will not stop for a cancelation, only errors
        done, _ = await asyncio.wait(
            tasks, return_when=asyncio.FIRST_EXCEPTION)

        # Handle any errors
        for task in done:
            if not task.cancelled() and task.exception() is not None:
                raise task.exception()

    def send_broadcast(self, event):
        """Parses a broadcast name and sends it"""
        event = 'broadcast_' + event.title()
        return self.send_event(event, True)

    def stop_all(self):
        """Ends execution of the main loop"""
        print("Stopping all...")
        self.runtime.running = False

    def key_event(self, key, state):
        """Presses or releases a key and sends press events"""
        if state:
            if not key in self.down_keys:
                self.down_keys.append(key)
        else:
            if key in self.down_keys:
                self.down_keys.remove(key)
            if len(self.down_keys) == 1:
                self.down_keys = []  # Remove 'any'
                self.send_event(f"keyany_pressed")
            self.send_event(f"key{key.upper()}_pressed")

    def key_down(self, event):
        """Called by runtime to handle key down events"""
        if event.key in KEY_MAP:
            self.key_event("any", True)
            self.key_event(KEY_MAP[event.key], True)
        elif event.unicode:  # TODO event.unicode doesn't exist for esc
            self.key_event("any", True)
            self.key_event(event.unicode.lower(), True)
        else:
            return False
        return True

    def key_up(self, event):
        """Called by runtime to handle key up events"""
        if event.key in KEY_MAP:
            self.key_event(KEY_MAP[event.key], False)
        elif event.unicode:
            self.key_event(event.unicode.lower(), False)
        else:
            return False
        return True

    def timer(self):
        """Gets the timer"""
        return time.monotonic() - self._timer

    def reset_timer(self):
        """Resets timer"""
        self._timer = time.monotonic()

    def mouse_down(self, event):
        """Checks if the mouse clicked a sprite"""
        point = event.pos
        sprites = self.sprites.sprites()
        sprites.reverse()
        for sprite in sprites:
            if not sprite.target.visible:
                continue
            offset = sprite.rect.topleft
            offset = (point[0] - offset[0], point[1] - offset[1])
            try:
                if sprite.mask.get_at(offset):
                    self.send_event_to("sprite_clicked", sprite.target)
                    return
            except IndexError:
                pass
        self.send_event_to("sprite_clicked", self.stage)

    def get_key(self, key):
        """Gets if a key is down"""
        return key in self.down_keys


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
                    Pen.resize(self.display.size)
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

                # Get the Pen bg
                bg_image.blit(
                    pg.transform.smoothscale(
                        Pen.image, self.display.rect.size),
                    self.display.rect.topleft
                )
                Pen.dirty = False

                self.sprites.set_clip(self.display.rect)
                self.sprites.clear(self.display.screen, bg_image.convert())
                self.sprites.draw(self.display.screen)

                if DEBUG_FPS:
                    self.debug_fps()

                pg.display.flip()
            elif DEBUG_RECTS or DEBUG_FPS:
                self.sprites.draw(self.display.screen)
                if DEBUG_RECTS:
                    self.debug_rects()
                if DEBUG_FPS:
                    self.debug_fps()
                pg.display.flip()
            else:
                pg.display.update(self.sprites.draw(self.display.screen))

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

    # draggable = False
    # rotationStyle
    # volume = 100
    # tempo = 60
    # videoTransparency = 50
    # videoState
    # textToSpeechLanguage

    def __init__(self, _, parent=None):
        # Default values
        self.xpos = 0
        self.ypos = 0
        self.direction = 90
        self.size = 100
        self.visible = True

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
        for cor, task in zip_longest(self.hats.get(name, []), self._tasks.get(name, [])):
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

    def update(self, util):
        """Clears the dirty flag by updating the sprite, rect and/or image"""
        self.sprite.visible = self.visible
        if self.dirty == 1:
            # Hiden/Shown, needs redrawing
            self.sprite.dirty = 1
        if self.dirty == 2:
            # Position change, only update rect
            self._update_rect(util)
        elif self.dirty == 3:
            # Major change, update image + rect
            self._update_image(util)
        self.dirty = 0

    def _update_image(self, util):
        """Updates and transforms the sprites image"""
        # Update the image
        image = self.costume.get_image(
            self.size * util.runtime.display.scale,
            self.direction)
        self.sprite.image = image
        self.sprite.mask = pg.mask.from_surface(image)

        # The rect now needs updating
        self._update_rect(util)

    def _update_rect(self, util):
        """Updates the rect to match the sprite's position and orientation"""
        display = util.runtime.display

        # Rotate the rect properly
        offset = self.costume.costume['offset']
        offset = offset.rotate(self.direction-90)
        self.sprite.rect = self.sprite.image.get_rect(
            center=(display.scale*(offset + pg.math.Vector2(self.xpos + STAGE_SIZE[0]//2,
                                                            STAGE_SIZE[1]//2 - self.ypos))))

        # Move the rect by the stage offset
        self.sprite.rect.move_ip(*display.rect.topleft)

        # TODO Stage position restrictions
        # self.sprite.rect.clamp(display.rect)

        self.sprite.dirty = 1

    def set_dirty(self, dirty):
        """Indicate the sprite's appearance has changed"""
        if dirty > self.dirty:
            self.dirty = dirty

    async def _yield(self, dirty=0):
        """Yields and sets the dirty flag if not in warp mode"""
        # Also checks if running longer than WARP_TIME
        if not self.warp or time.monotonic() - self.warp_timer > WARP_TIME:
            if self.warp:
                print("Overtime!")
            await self.sleep(0, dirty)

    async def sleep(self, delay, dirty=0):
        """Yields for the given delay and set the dirty flag"""
        # TODO Sleep for min 1 whole tick
        # Should not run again in same tick, flags/states?

        # Check if the sprite has become dirtier
        if dirty > self.dirty:
            self.dirty = dirty

        # Yield for the duration
        if self.warp:
            # Toggle warp off for other scripts in this sprite
            self.warp = False
            print("yield")
            await asyncio.sleep(delay)
            self.warp = True

            # Reset the warp timer
            self.warp_timer = time.monotonic()
        else:
            await asyncio.sleep(delay)

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
            await self._yield(2)
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
            xpos = util.input.m_xpos
            ypos = util.input.m_ypos
        else:
            other = util.targets.get(other, self)
            xpos = other.xpos
            ypos = other.ypos
        return math.sqrt((self.xpos - xpos)**2 + (self.ypos - ypos)**2)

    def distance_to_point(self, point):
        """"Calculate the distance to a point (x, y)"""
        return math.sqrt((self.xpos - point[0])**2 + (self.ypos - point[1])**2)

    def get_touching(self, util, other):
        """Check if this sprite is touching another or its clones"""
        if other == "_mouse_":
            self.update(util)
            xpos, ypos = pg.mouse.get_pos()

            offset = self.sprite.rect.topleft
            offset = (xpos - offset[0], ypos - offset[1])
            try:
                return bool(self.sprite.mask.get_at(offset))
            except IndexError:
                return False

        other = util.targets.get(other)
        if not other:
            return False

        # Must update this sprite and the other before testing
        self.update(util)
        other.update(util)

        # Check if touching the original
        if pg.sprite.collide_mask(other.sprite, self.sprite):
            return True

        # Check if touching a clone
        for clone in other.clones:
            # Update the clones image too
            clone.update(util)

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
        start = util.sprites.get_layer_of_sprite(self.sprite)
        top = util.sprites.get_top_layer()
        value = max(0, min(top, start + value)) - start
        self._move_layers(util.sprites, start, value)

    def front_layer(self, util):
        """Moves the sprite to the front layer"""
        start = util.sprites.get_layer_of_sprite(self.sprite)
        top = util.sprites.get_top_layer()
        self._move_layers(util.sprites, start, top - start)

    def back_layer(self, util):
        """Moves the sprite to the back layer"""
        start = util.sprites.get_layer_of_sprite(self.sprite)
        self._move_layers(util.sprites, start, -start)

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
        other = util.targets.get(other)
        if other:
            self.xpos = other.xpos
            self.ypos = other.ypos

    def create_clone_of(self, util, name):
        """Create a clone of this target"""
        if len(self._clones) < MAX_CLONES:
            # Get the target to clone
            if name == "_myself_":
                target = self
            else:
                target = util.targets.get(name)
                if target is None:
                    return

            # Get a layer for the clone
            # Move the top sprite where the clone will go,
            # Then move it back to the top leaving an empty space
            top = util.sprites.get_top_layer()
            bottom = util.sprites.get_layer_of_sprite(self.sprite)
            top_sprite = util.sprites.get_top_sprite()
            self._move_layers(util.sprites, top, bottom-top)
            util.sprites.change_layer(top_sprite, top+1)

            # __class__ is the Sprite's subclass
            clone = target.__class__(util, target)
            self._clones.append(clone)  # Shared between targets
            target.clones.append(clone)
            util.sprites.add(clone.sprite, layer=bottom)
            util.send_event_to("clone_start", clone)
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

    def point_towards(self, util, other):
        """Point towards another sprite"""
        if other == "_mouse_":
            xpos = util.input.m_xpos
            ypos = util.input.m_ypos
        else:
            other = util.targets.get(other, self)
            xpos = other.xpos
            ypos = other.ypos
        xpos -= self.xpos
        ypos -= self.ypos
        direction = 90 - math.degrees(math.atan2(ypos, xpos))
        # if ypos > 0:
        # direction += 180
        self.direction = direction


class Inputs:
    """
    Handles keyboard and mouse inputs.

    m_xpos - Mouse x position
    m_ypos - Mouse y position
    m_down - Mouse down?
    """

    def __init__(self, runtime, util):
        self.util = util
        self.runtime = runtime
        self.m_xpos = 0
        self.m_ypos = 0
        self.m_down = False

    def update(self):
        """Update mouse position"""
        xpos, ypos = pg.mouse.get_pos()
        display = self.runtime.display
        self.m_xpos = round((xpos - display.rect.x)/display.scale - 240)
        self.m_ypos = round(180 - (ypos - display.rect.y)/display.scale)
        self.m_down = bool(pg.mouse.get_pressed()[0])


class Sounds:
    """
    Handles sounds for a target

        sounds - A dict referencing sounds (pg.mixer.Sound) by name
        sounds_list - Used to reference sounds by number
        volume - The current volume. If set directly, currently playing
            channels will not update. Use set_volume to update them.

        _channels - A dict with in use sound channels as keys and waiting
            tasks as values. The channels are kept so the volume can be
            adjusted and the tasks are there to be cancelled.
    """

    _cache = {}

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
        self._channels = {}
        self.set_volume(volume)

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
        for channel in self._channels:
            channel.set_volume(self.volume / 100)

    def change_volume(self, volume):
        """Changes and updates the volume by an amount"""
        self.set_volume(self.volume + volume)

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
                return asyncio.create_task(self._handle_channel(sound, channel))
        return asyncio.create_task(asyncio.sleep(0))

    async def _handle_channel(self, sound, channel):
        """Saves the channel and waits for it to finish"""
        # Start the sound
        delay = sound.get_length()
        channel.set_volume(self.volume / 100)
        channel.play(sound)

        # Create a cancelable waiting task
        self._channels[channel] = asyncio.create_task(asyncio.sleep(delay))

        # Pop the channel once it is done or cancelled
        await asyncio.wait((self._channels[channel],))
        self._channels.pop(channel)

    @staticmethod
    def stop_all(util):
        """Stops all sounds for all sprites"""
        for sprite in util.sprites.sprites():
            sprite.target.sounds.stop()
        util.stage.sounds.stop()

    def stop(self):
        """Stops all sounds for just this sprite"""
        for channel, task in self._channels.items():
            channel.stop()
            task.cancel()

    def copy(self):
        """Returns a copy of this Sounds"""
        return Sounds(self.volume, self.sounds_list, self.sounds)

    def set_effect(self, effect, value):
        """Set a sound effect, not implemented"""
        # TODO Pan effect with Channel.set_volume(left, right)

    def change_effect(self, effect, value):
        """Change a sound effect, not implemented"""


class Costumes:
    """
    Handles costumes for a target

    costumes - A dict referencing costume by name
    costumes_list - Used to reference costumes by number

    name - The name of the current costume
    number - The number of the current costume

    effects - A dict of current effects and values

    _cache - A shared cache containing loaded images
    """

    _cache = {}

    def __init__(self, costume_number, rotation_style, costumes):
        self.number = costume_number + 1
        self.costume = costumes[costume_number]
        self.name = self.costume['name']
        self.rotation_style = rotation_style

        self.costumes = {}
        self.costume_list = []

        self.effects = {}

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
            self.costume_list.append(asset)

    def switch(self, costume):
        """Sets the costume"""
        asset = self.costumes.get(costume)
        if asset:
            self.name = costume
            self.costume = asset
            self.number = asset['number']
        else:
            try:
                self.number = (round(float(costume)) %
                               len(self.costume_list))
                self.costume = self.costume_list[self.number - 1]
                self.name = self.costume['name']
            except ValueError:
                pass
            except OverflowError:
                pass

    def next(self):
        """Go to the next costume"""
        self.number += 1
        if self.number > len(self.costume_list):
            self.number = 1
        self.costume = self.costume_list[self.number - 1]
        self.name = self.costume['name']

    def _load_image(self, path):
        """Loads an image or retrieves it from cache"""
        image = self._cache.get(path)
        if not image:
            image = pg.image.load("assets/" + path).convert_alpha()
            self._cache[path] = image
        return image

    def get_image(self, size, direction):
        """Get the current image with a size and direction"""
        # Get the base image
        image = self.costume['image']

        # TODO Proper image scale clamping

        # Scale the image
        scale = max(0.05, size/100 / self.costume['scale'])
        image = pg.transform.smoothscale(
            image, (max(5, int(image.get_width() * scale)),
                    max(5, int(image.get_height() * scale)))
        )

        # Rotate the image
        if self.rotation_style == "all around":
            # Segmentation fault here if image size is too small
            image = pg.transform.rotate(image, 90-direction)
        elif self.rotation_style == "left-right":
            if direction > 0:
                image = pg.transform.flip(image, True, False)

        # Apply effects
        image = self._apply_effects(image)

        return image

    def set_effect(self, effect, value):
        """Sets and wraps/clamps a graphics effect"""
        if effect == 'ghost':
            self.effects[effect] = min(max(value, 0), 100)
        elif effect == 'brightness':
            self.effects[effect] = min(max(value, -100), 100)
        elif effect == 'color':
            self.effects[effect] = value % 200

    def change_effect(self, effect, value):
        """Changes and wraps/clamps a graphics effect"""
        value = self.effects.get(effect, 0) + value
        self.set_effect(effect, value)

    def clear_effects(self):
        """Clear all graphic effects"""
        self.effects = {}

    def _apply_effects(self, image):
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
            image.fill(
                (255, 255, 255, ghost),
                special_flags=pg.BLEND_RGBA_MULT)

        # Hue change
        color = self.effects.get('color', 0)
        if color:
            color = 360 * color / 200
            image = self._hue_effect(image, color)

        return image

    @staticmethod
    def _hue_effect(image, value):
        """
        Changes the hue of an image for the color effect
        Value should be between 0 and 360. Coverts the image
        to an 8-bit surface and adjusts the color palette.
        Transparency is copied first to preserve it.
        """

        # Get a copy of the alpha channel
        transparency = image.convert_alpha()
        transparency.fill((255, 255, 255, 0),
                          special_flags=pg.BLEND_RGBA_MAX)

        # Get an 8-bit surface with a color palette
        image = image.convert(8)

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

    def copy(self):
        """Return a copy of this list"""
        cost = Costumes(self.number - 1, self.rotation_style,
                        self.costume_list)
        cost.effects = self.effects.copy()
        return cost


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
        self.position = (round((self.target.xpos + 240) * self.display.scale + self.display.rect[0]),
                         round((180 - self.target.ypos) * self.display.scale + self.display.rect[1]))

        if Pen.image is None:
            Pen.image = pg.Surface(self.display.size).convert_alpha()
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
        end_pos = (round((self.target.xpos + 240) * self.display.scale + self.display.rect[0]),
                   round((180 - self.target.ypos) * self.display.scale + self.display.rect[1]))
        if self.isdown:
            size = round(self.size * self.display.scale / 2)
            pg.draw.line(Pen.image, self.color, self.position,
                         end_pos, size * 2)
            pg.draw.circle(Pen.image, self.color,
                           self.position, size)
            pg.draw.circle(Pen.image, self.color,
                           end_pos, size)
            Pen.dirty = True
        self.position = end_pos

    def stamp(self):
        """Stamp the sprite image"""
        self.target.update(self.util)
        self.image.blit(
            self.target.sprite.image, self.target.sprite.rect)
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
            self.color = pg.Color(number(value) % 0xFFFFFFFF)

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


def number(value):
    """Attempts to cast a value to a number"""
    if isinstance(value, str):
        try:
            value = float(value)
            if value.is_integer():
                value = int(value)
        except ValueError:
            return 0
    if value == float('NaN'):
        return 0
    return value


class List:
    """Handles special list behaviors"""

    def __init__(self, values):
        self.list = values

    def __getitem__(self, key):
        key = self._to_index(key)
        if key is not None:
            return self.list[key]
        return ""

    def __setitem__(self, key, value):
        key = self._to_index(key)
        if key is not None:
            self.list[key] = value

    def append(self, value):
        """Add up to 200,000 items to list"""
        if len(self.list) < 200000:
            self.list.append(value)

    def insert(self, key, value):
        """Insert up to 200,000 items in list"""
        if len(self.list) < 200000:
            if key == "first":
                key = 0
            elif key == "last":
                key = -1
            elif key == "random":
                key = random.randint(0, len(self.list))
            else:
                key = round(number(key)) - 1

            if key is not None and 0 <= key <= len(self.list):
                self.list.insert(key, value)

    def delete(self, key):
        """Remove an item from list"""
        if key == "all":
            self.list = []
        else:
            key = self._to_index(key)
            if key is not None:
                self.list.pop(key)

    def delete_all(self):
        """Delete all items in list"""
        self.list = []

    def _to_index(self, key):
        """Gets the index of first, last, random strings"""
        if self.list:
            if key == "first":
                return 0
            if key == "last":
                return -1
            if key == "random":
                return random.randint(0, len(self.list) - 1)
            key = round(number(key))
            if 0 < key <= len(self.list):
                return key - 1
        return None

    def __contains__(self, item):
        item = str(item).casefold()
        for value in self.list:
            if item == str(value).casefold():
                return True
        return False

    def __str__(self):
        char_join = True
        for item in self.list:
            if len(str(item)) != 1:
                char_join = False
                break
        if char_join:
            return ''.join(self.list)
        return ' '.join(self.list)

    def __len__(self):
        return self.list.__len__()

    # TODO Variable/list reporters
    def show(self):
        """Print list"""
        print(self.list)

    def hide(self):
        """Do nothing"""

    def index(self, item):
        """Find the index of an item, case insensitive"""
        item = str(item).casefold()
        for i, value in enumerate(self.list):
            if str(value).casefold() == item:
                return i + 1
        return 0

    def index1(self, item):
        """Find the index of an item in the list"""
        try:
            return self.list.index(item) + 1
        except ValueError:
            return 0

    def copy(self):
        """Return a copy of this List"""
        return List(self.list.copy())


def main(sprites):
    """Run the program"""
    runtime = None
    logging.basicConfig(level=logging.DEBUG)
    try:
        runtime = Runtime(sprites)
        asyncio.run(runtime.main_loop())
    finally:
        if runtime:
            runtime.quit()


def letter(text, index):
    """Gets a letter from string"""
    try:
        return str(text)[number(index) - 1]
    except IndexError:
        return ""


def gt(val1, val2):
    try:
        return float(val1) > float(val2)
    except ValueError:
        return str(val1) > str(val2)


def lt(val1, val2):
    try:
        return float(val1) < float(val2)
    except ValueError:
        return str(val1) < str(val2)


def eq(val1, val2):
    return str(val1).lower() == str(val2).lower()


def div(val1, val2):
    try:
        return number(val1) / number(val2)
    except ZeroDivisionError:
        return float('infinity')


def randrange(val1, val2):
    val1 = number(val1)
    val2 = number(val2)
    val1, val2 = min(val1, val2), max(val1, val2)
    if isinstance(val1, float) or isinstance(val2, float):
        return random.random() * abs(val2-val1) + val1
    return random.randint(val1, val2)


if __name__ == '__main__':
    main({})
