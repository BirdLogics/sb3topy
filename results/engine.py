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

ASSETS_PATH - The path the assets folder; f"{ASSETS_PATH}md5.ext"
AUDIO_CHANNELS - The number of audio channels created for the pygame mixer

KEY_MAP - Maps pygame keys to their names in the project
"""

import asyncio
import math
import time

import pygame as pg

USERNAME = ""

TARGET_FPS = 30
TURBO_MODE = False
WORK_TIME = 1 / 60
WARP_TIME = 0.5

STAGE_SIZE = (480, 360)
DISPLAY_SIZE = (480, 360)
DISPLAY_FLAGS = 0
FS_SCALE = 1

ASSETS_PATH = "./assets/"
AUDIO_CHANNELS = 8

KEY_MAP = {
    pg.K_SPACE: "space",
    pg.K_UP: "up arrow",
    pg.K_DOWN: "down arrow",
    pg.K_RIGHT: "right arrow",
    pg.K_LEFT: "left arrow",
    pg.K_RETURN: "enter"
}


DISPLAY_SCALE = 1


class Effects:
    """Static methods for applying effects"""
    # def apply_effects(self, image, effects):
    #     """Currently doesn't use cache but could in future"""

    #     # Brighten/Darken
    #     brightness = effects.get('brightness', 0)
    #     if brightness > 0:
    #         brightness = 255 * brightness / 100
    #         image.fill(
    #             (brightness, brightness, brightness),
    #             special_flags=pg.BLEND_RGB_ADD)
    #     elif brightness < 0:
    #         brightness = -255 * brightness / 100
    #         image.fill(
    #             (brightness, brightness, brightness),
    #             special_flags=pg.BLEND_RGB_SUB)

    #     # Transparent
    #     ghost = effects.get('ghost', 0)
    #     if ghost:
    #         ghost = 255 * ghost / 100
    #         image.fill(
    #             (255, 255, 255, ghost),
    #             special_flags=pg.BLEND_RGBA_MULT)

    #     # Hue change
    #     color = effects.get('color', 0)
    #     if color:
    #         color = 360 * color / 200
    #         image = self.change_hue(image, color)

    #     return image

    @staticmethod
    def change_brightness(image, value):
        """Returns a lightened or darkened image"""
        brightness = 255 * value
        if brightness > 0:
            image.fill(
                (brightness, brightness, brightness),
                special_flags=pg.BLEND_RGB_ADD)
        elif brightness < 0:
            image.fill(
                (-brightness, -brightness, -brightness),
                special_flags=pg.BLEND_RGB_SUB)

    @staticmethod
    def change_transparency(image, value):
        """Returns an image with altered per-pixel transparency"""
        image = image.copy()
        image.fill(
            (255, 255, 255, 255 * value),
            special_flags=pg.BLEND_RGBA_MULT)
        return image

    @staticmethod
    def change_hue(image, value):
        """Returns an image with altered hue

        As part of the process, the image is converted to an 8-bit
        surface so the color palette can be adjusted. Transparency
        is preserved, but some color quality may be lost."""

        # Gets a copy of the alpha channel
        transparency = image.convert_alpha()
        transparency.fill((255, 255, 255, 0), special_flags=pg.BLEND_RGBA_MAX)

        # Get an 8-bit surface with a color palette
        image = image.convert(8)

        # Change the hue of the palette
        for index in range(256):
            # Get the palette color at index
            color = pg.Color(*image.get_palette_at(index))

            # Get and wrap the new hue
            hue = (color.hsva[0] + value) % 360

            # Update the hue
            color.hsva = (hue, *color.hsva[1:3])
            image.set_palette_at(index, color)

        # Return the image transparency
        image.set_alpha()
        image = image.convert_alpha()
        image.blit(transparency, (0, 0), special_flags=pg.BLEND_RGBA_MULT)

        return image


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

    def __init__(self, runtime):
        self.runtime = runtime
        self.cache = AssetCache()
        self.stage = Stage()  # TODO BlockUtil stage

    def send_event(self, name):
        """Starts an event for all sprites"""
        threads = []
        sprites = self.runtime.sprites.sprites()
        sprites.reverse()
        for sprite in sprites:
            sprite.target.recieve_event(name, threads, self)
        return asyncio.gather(*threads)

    def key_event(self, key, state):
        """Presses or releases a key and sends press events"""
        if state:
            if key in self.down_keys:
                self.down_keys.remove(key)
        else:
            if not key in self.down_keys:
                self.down_keys.append(key)
                if len(self.down_keys) == 1:
                    self.down_keys = []  # Remove 'any'
        self.send_event(f"key{key}_pressed")

    def key_down(self, event):
        """Called by runtime to handle key down events"""
        if event.key in KEY_MAP:
            self.key_event("any", True)
            self.key_event(KEY_MAP[event.key], True)
        elif event.unicode: # TODO event.unicode doesn't exist for esc
            self.key_event("any", True)
            self.key_event(event.unicode.upper(), True)
        else:
            return False
        return True

    def key_up(self, event):
        """Called by runtime to handle key up events"""
        if event.key in KEY_MAP:
            self.key_event(KEY_MAP[event.key], False)
        elif event.unicode:
            self.key_event(event.unicode.upper(), False)
        else:
            return False
        return True

    def timer(self):
        """Gets the timer"""
        return time.monotonic() - self._timer

    def reset_timer(self):
        """Resets timer"""
        self._timer = time.monotonic()


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

    def quit(self):
        """Ensures fullscreen is exited to return normal display resolution"""
        if self.display.fullscreen:
            self.display.toggle_fullscreen()
        pg.quit()

    async def main_loop(self):
        """Run the main loop"""
        self.util.send_event("green_flag")
        running = True
        while running:
            # Allow pygame to update
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    running = False
                elif event.type == pg.KEYDOWN:
                    self.util.key_down(event)
                elif event.type == pg.KEYUP:
                    self.util.key_down(event)
                elif event.type == pg.VIDEORESIZE:
                    self.display.size = (event.w, event.h)
                    self.display.setup_display()
                    for target in self.util.targets.values():
                        target.dirty = 3
                    self.util.stage.dirty = 3

            # Allow the threads to run
            dirty = False
            work_timer = time.monotonic()
            while (time.monotonic() < work_timer + WORK_TIME) and \
                    (TURBO_MODE or not dirty):
                # Allow targets to run for 1 tick
                await asyncio.sleep(0)

                # Check if any sprites need drawing
                for target in self.util.targets.values():
                    if target.dirty:
                        dirty = True

            # Update sprite rects, images, etc.
            self.update_sprites()

            # Update the screen
            if self.util.stage.dirty:
                self.util.stage.update(self.util)

                # Get the stage bg
                bg_image = pg.Surface(self.display.size)
                bg_image.fill((255, 255, 255))  # TODO Stage bg
                # bg_image.blit(
                #     self.util.stage.sprite.image,
                #     (self.display.rect.x, self.display.rect.y))

                self.sprites.clear(self.display.screen, bg_image.convert())
                self.sprites.draw(self.display.screen)
                self.sprites.set_clip(self.display.rect)

                pg.display.flip()
            else:
                pg.display.update(self.sprites.draw(self.display.screen))

            # Limit the frame rate
            if not TURBO_MODE:
                self.clock.tick(TARGET_FPS)

        pg.quit()

    def update_sprites(self):
        """Update dirty sprites"""
        any_dirty = False
        for target in self.util.targets.values():
            if target.dirty:
                any_dirty = True
                target.update(self.util)
        return any_dirty


class AssetCache:
    """Handles sounds and costumes"""
    costumes = {}
    sounds = {}

    def get_costume(self, costume, scale):
        """Gets or loads a costume"""
        # Try to get the costume from the cache
        image = self.costumes.get((costume['path'], scale), None)
        if not image:
            # Need to scale a new image
            image = self.costumes.get(
                (costume['path'], costume['scale']), None)
            if not image:
                # Need to load the image first
                image = pg.image.load(
                    ASSETS_PATH + costume['path']).convert_alpha()
                self.costumes[(costume['path'], costume['scale'])] = image

            # Smooth scale the image
            image = pg.transform.smoothscale(
                image,
                (int(image.get_width() * scale / costume['scale']),
                 int(image.get_height() * scale / costume['scale'])))
            self.costumes[(costume['path'], scale)] = image
        return image

    def apply_effects(self, image, effects):
        """Currently doesn't use cache but could in future"""

        # Brighten/Darken
        brightness = effects.get('brightness', 0)
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

        # Transparent
        ghost = effects.get('ghost', 0)
        if ghost:
            ghost = 255 * ghost / 100
            image.fill(
                (255, 255, 255, ghost),
                special_flags=pg.BLEND_RGBA_MULT)

        # Hue change
        color = effects.get('color', 0)
        if color:
            color = 360 * color / 200
            image = self.change_hue(image, color)

        return image

    @staticmethod
    def change_hue(image, value):
        """Changes the hue of an image for the color effect
        Value should be between 0 and 360. Coverts the image
        to an 8-bit surface and adjusts the color palette.
        Transparency is copied first to preserve it."""

        # Gets a copy of the alpha channel
        transparency = image.convert_alpha()
        transparency.fill((255, 255, 255, 0), special_flags=pg.BLEND_RGBA_MAX)

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

    def get_sound(self, md5ext):
        """Gets or loads a sound"""
        if not md5ext in self.sounds:
            self.sounds[md5ext] = pg.mixer.Sound(ASSETS_PATH + md5ext)
        return self.sounds[md5ext]


class Stage:
    variables = {}
    lists = {}

    backdrops_dict = {}
    backdrops = []
    backdrop = 0

    sounds_dict = {}
    sounds = []

    warp = False
    warp_timer = 0

    hats = {}

    effects = {}

    # 1 dirty sprite, 2 dirty rect, 3 dirty image
    dirty = 3

    def __init__(self):
        self.sprite = pg.sprite.Sprite()
        self.sprite.image = pg.surface.Surface((480, 360))

    def update(self, _):
        """Update the stage's appearence"""
        self.dirty = 0  # TODO Stage update


class Target:
    """Holds common code for targets

    The following attributes should be set by the child:
        variables - A dict of variables and their default values
        lists - A dict of lists and their default values
        costumes - A list of costume dicts
        sounds - A list of sound dicts
        costume - The intial costume #. Will be changed into a
            dict from costumes by __init__
        xpos, ypos, direction, size - Number attributes
        hats - A list of aync functions which should be started
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

    variables = {}
    lists = {}

    costumes = []
    sounds = []

    costume = None

    xpos, ypos = 0, 0
    direction = 90
    size = 100

    hats = None

    # draggable = False
    # rotationStyle
    # volume = 100
    # tempo = 60
    # videoTransparency = 50
    # videoState
    # textToSpeechLanguage

    def __init__(self, util, parent=None):
        super().__init__()

        # Create the pygame sprite
        self.sprite = pg.sprite.DirtySprite()
        self.sprite.target = self

        # Only brightness, color, ghost supported
        # 1 dirty sprite, 2 dirty rect, 3 dirty image
        self.dirty = 3
        self.warp = False
        self.warp_timer = 0

        if parent is None:
            # Get assets by name
            self.costumes_dict = {}
            self.sounds_dict = {}

            # Parse assets and fill the dicts
            self._parse_assets(util.cache)

            # Get the current costume
            self.costume = self.costumes[self.costume]

            # Clear effects
            self.effects = {}

        else:
            # This is a clone of parent
            self.costumes_dict = parent.costumes_dict
            self.sounds_dict = parent.costumes_dict

            self.variables = parent.variable.copy()
            self.lists = parent.lists.copy()

            self.xpos, self.ypos = parent.xpos, parent.ypos
            self.direction = parent.direction
            self.size = parent.size

            self.effects = parent.effects.copy()

            # TODO Clone start
            # await self.recieve_event("clone_start")#, [], None)

        # Update the sprite rect, image, mask
        self._update_image(util)

    def recieve_event(self, name, threads, util):
        """Start an event"""
        threads.extend(c(util) for c in self.hats.get(name, []))

    def _parse_assets(self, cache):
        """Parses the costume list and creates the costume dict"""
        # Parse costumes
        for index, costume in enumerate(self.costumes):
            # Preload the costume
            image = cache.get_costume(costume, costume['scale'])

            # Calculate the rotation offset
            if costume['center'] is None:
                costume['offset'] = pg.math.Vector2(0, 0)
            else:
                center = pg.math.Vector2(image.get_size()) / 2
                costume['offset'] = pg.math.Vector2(costume['center']) - center

            # Save the index
            costume['number'] = index

            # Add the costume to the dict
            self.costumes_dict[costume['name']] = costume

        # Parse sounds
        for asset in self.sounds:
            # Load the sound
            asset['sound'] = cache.get_sound(asset['path'])

            # Add the asset to the dict
            self.sounds_dict[asset['name']] = asset

    def update(self, util):
        """Clears the dirty flag by updating the sprite, rect and/or image"""
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
        display = util.runtime.display

        # The image is scaled to the display scale
        image = util.cache.get_costume(
            self.costume, self.size/100 * display.scale)
        image = pg.transform.rotate(image, -self.direction)
        self.sprite.mask = pg.mask.from_surface(image)

        if self.effects:
            self.sprite.image = util.cache.apply_effects(image, self.effects)
        else:
            self.sprite.image = image  # change_hue(image, 20)

        self._update_rect(util)

    def _update_rect(self, util):
        """Updates the rect to match the sprite's position and orientation"""
        display = util.runtime.display

        # Rotate the rect properly
        offset = self.costume['offset'].rotate(self.direction)
        self.sprite.rect = self.sprite.image.get_rect(
            center=(offset + display.scale *
                    pg.math.Vector2(self.xpos + STAGE_SIZE[0]//2,
                                    self.ypos + STAGE_SIZE[1]//2)))

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
        if not self.warp or time.monotonic() > self.warp_timer + WARP_TIME:
            await self.sleep(0, dirty)

    async def sleep(self, delay, dirty=0):
        """Yields for the given delay and set the dirty flag"""
        # Check if the sprite has become dirtier
        if dirty > self.dirty:
            self.dirty = dirty

        # Yield for the duration
        if self.warp:
            # Toggle warp off for other scripts in this sprite
            self.warp = False
            await asyncio.sleep(delay)
            self.warp = True

            # Reset the warp timer
            self.warp_timer = time.monotonic()
        else:
            await asyncio.sleep(delay)

    def set_direction(self, degrees):
        """Sets and wraps the direction"""
        self.direction = degrees - ((degrees + 179) // 360) * 360

    def get_costume(self, costume):
        """Gets a costume of name/number, or returns the current costume"""
        if isinstance(costume, str) and costume in self.costumes_dict:
            return self.costumes_dict[costume]
        try:
            return self.costumes[round(float(costume))]
        except ValueError:
            return self.costume
        except IndexError:
            return self.costume

    def play_sound(self, sound):
        """Plays a sound"""
        # TODO Better sound parity?
        # A sound cannot be played twice at the same time
        # by a sprite and its clones. Need a currently
        # playing list and a way to make a task wait for
        # the sound to finish. Need a shared list of currently
        # playing sounds?
        sound.play()

    def distance_to(self, other):
        """Calculate the distance to another target"""
        return math.sqrt((self.xpos - other.xpos)**2 + (self.ypos - other.ypos)**2)

    def distance_to_point(self, point):
        """"Calculate the distance to a point (x, y)"""
        return math.sqrt((self.xpos - point[0])**2 + (self.ypos - point[1])**2)

    def get_touching(self, util, other):
        """Check if this sprite is touching another or its clones"""
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

    # TODO Test touching point (mouse)
    def get_touching_point(self, util, point):
        """Check if this sprite is touching a point"""
        # Update the image and position if necesary
        self.update(util)

        # Transform the point to match pygame coords
        point = (point[0] * util.scale, point[1] * util.scale)

        # Check if the mask contains the point
        return self.sprite.mask.get_at(point)

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


def main(sprites):
    """Run the program"""
    runtime = None
    try:
        runtime = Runtime(sprites)
        asyncio.run(runtime.main_loop(), debug=True)
    finally:
        if runtime:
            runtime.quit()


if __name__ == '__main__':
    main({})
