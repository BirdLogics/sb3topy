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
import random
import time

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

ASSETS_PATH = "./results/assets/"
AUDIO_CHANNELS = 8

DEBUG_ASYNC = True
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
    sprites = None

    def __init__(self, runtime):
        self.runtime = runtime
        self.cache = AssetCache()

    def send_event(self, event):
        """Starts an event for all sprites"""
        threads = []
        sprites = self.sprites.sprites()
        sprites.reverse()
        for sprite in sprites:
            sprite.target.recieve_event(event, threads, self)
        self.stage.recieve_event(event, threads, self)
        return asyncio.gather(*threads)

    def send_event_to(self, event, target):
        """Starts an event for a single target"""
        threads = []
        target.recieve_event(event, threads, self)
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
        elif event.unicode:  # TODO event.unicode doesn't exist for esc
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

    def mouse_down(self, event):
        """Checks if the mouse clicked a sprite"""
        point = event.pos
        sprites = self.sprites.sprites()
        sprites.reverse()
        for sprite in sprites:
            offset = sprite.rect.topleft
            offset = (point[0] - offset[0], point[1] - offset[1])
            try:
                if sprite.mask.get_at(offset):
                    self.send_event_to("sprite_clicked", sprite.target)
                    return
            except IndexError:
                pass
        self.send_event_to("sprite_clicked", self.stage)


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
            if name == "SpriteStage":
                self.util.stage = target(self.util)
            else:
                self.util.targets[name] = target(self.util)
                self.sprites.add(self.util.targets[name].sprite)
        self.util.sprites = self.sprites

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
                # elif event.type == pg.KEYDOWN:
                #     self.util.key_down(event) # TODO When key pressed
                elif event.type == pg.KEYUP:
                    # self.util.key_down(event)
                    if event.key == pg.K_F11:
                        self.display.toggle_fullscreen()
                elif event.type == pg.VIDEORESIZE:
                    self.display.size = (event.w, event.h)
                    self.display.setup_display()
                    for target in self.util.targets.values():
                        target.dirty = 3
                    self.util.stage.dirty = 3
                elif event.type == pg.MOUSEBUTTONDOWN:
                    self.util.mouse_down(event)

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
                bg_image.blit(
                    self.util.stage.sprite.image,
                    (self.display.rect.x, self.display.rect.y))

                self.sprites.clear(self.display.screen, bg_image.convert())
                self.sprites.draw(self.display.screen)
                self.sprites.set_clip(self.display.rect)
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
        pg.draw.rect(self.display.screen, (0, 0, 0),
                     pg.Rect((5, 5), font.size(fps)))
        self.display.screen.blit(font.render(
            fps, True, (0, 100, 20)), (5, 5))


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
            ghost = 255 - 255 * ghost / 100
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

    variables = {}
    lists = {}

    costumes = []
    sounds = []

    costume = None

    xpos, ypos = 0, 0
    direction = 90
    size = 100
    visible = True

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
        self.update(util)

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
            center = pg.math.Vector2(image.get_size()) / 2
            # if costume['center'] is None:
            #     costume['offset'] = center
            # else:
            # Image center is pixels offset
            costume['offset'] = pg.math.Vector2(costume['center'])
            costume['offset'] *= -1
            costume['offset'] += center
            costume['offset'] /= costume['scale']

            # Save the index
            costume['number'] = index

            # Add the costume to the dict
            self.costumes_dict[costume['name']] = costume

        # Parse sounds
        self.sounds = Sounds(cache, self.sounds, 100)

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
        display = util.runtime.display

        # TODO Rotation style support
        # The image is scaled to the display scale
        image = util.cache.get_costume(
            self.costume, self.size/100 * display.scale)
        image = pg.transform.rotate(image, 90-self.direction)
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
        offset = (self.costume['offset']).rotate(self.direction-90)
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

    def set_costume(self, costume):
        """Sets the costume"""
        self.costume = self.get_costume(costume)

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

    def change_layer(self, util, value):
        """Moves number layers fowards"""
        # TODO Layering diffrences
        # Pygame has multiple sprites per layer
        util.sprites.change_layer(
            self.sprite,
            util.sprites.get_layer_of_sprite(self.sprite) + value)

    def front_layer(self, util):
        """Moves the sprite to the front layer"""
        util.sprites.move_to_front(self.sprite)

    def back_layer(self, util):
        """Moves the sprite to the back layer"""
        util.sprites.move_to_bback(self.sprite)


class Sounds:
    """
    Handles sounds for a sprite

        sounds - A dict referencing sounds (pg.mixer.Sound) by name
        sound_list - Used to reference sounds by number
        volume - The current volume. If set directly, currently playing
            channels will not update. Use set_volume to update them.

        _channels - A dict with in use sound channels as keys and waiting
            tasks as values. The channels are kept so the volume can be
            adjusted and the tasks are there to be canceled.
    """

    def __init__(self, cache, sounds, volume):
        self.sounds = {}
        self.sound_list = []

        for asset in sounds:
            self.sounds[asset['name']] = cache.get_sound(asset['path'])
            self.sound_list.append(self.sounds[asset['name']])
        self._channels = {}
        self.set_volume(volume)

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
                if 0 < name < len(self.sound_list):
                    sound = self.sound_list[name]
                else:
                    sound = self.sound_list[0]
            except ValueError:
                pass
            except OverflowError:  # round(Infinity)
                pass
        if sound:
            channel = pg.mixer.find_channel()
            if channel:
                return asyncio.ensure_future(self._handle_channel(sound, channel))
        return asyncio.sleep(0)

    async def _handle_channel(self, sound, channel):
        """Saves the channel and waits for it to finish"""
        delay = sound.get_length()
        channel.set_volume(self.volume / 100)
        channel.play(sound)
        try:
            self._channels[channel] = asyncio.ensure_future(
                asyncio.sleep(delay))
            await self._channels[channel]
        except asyncio.CancelledError:
            pass
        finally:
            self._channels.pop(channel)

    @staticmethod
    def stop_all(util):
        """Stops all sounds for all sprites"""
        for target in util.targets.values():
            target.sounds.stop()

    def stop(self):
        """Stops sounds for just this sprite"""
        for channel, task in self._channels.items():
            channel.stop()
            task.cancel()


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

    def __init__(self, lst):
        self.list = lst

    def __get_item__(self, key):
        key = self._to_index(key)
        if key is not None:
            return self.list[key - 1]
        return ""

    def __set_item__(self, key, value):
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
            key = self._to_index(key, 0)
            if key is not None:
                self.list.insert(key, value)

    def remove(self, key):
        """Remove an item from list"""
        key = self._to_index(key)
        if key is not None:
            self.list.remove(key)

    def _to_index(self, key, max_adj=-1):
        """Gets the index of first, last, random strings"""
        if self.list:
            if key == "first":
                return 0
            if key == "last":
                return -1
            if key == "random":
                return random.randint(0, len(self.list) + max_adj)
            key = round(number(key))
            if 0 < key <= len(self.list) + max_adj:
                return key - 1
        return None

    def __str__(self):
        char_join = True
        for item in self.list:
            if len(str(item)) != 1:
                char_join = False
                break
        if char_join:
            return ''.join(self.list)
        return ' '.join(self.list)

    # TODO Variable/list reporters
    def show(self):
        """Do nothing"""

    def hide(self):
        """Do nothing"""


def main(sprites):
    """Run the program"""
    runtime = None
    try:
        runtime = Runtime(sprites)
        asyncio.run(runtime.main_loop(), debug=DEBUG_ASYNC)
    finally:
        if runtime:
            runtime.quit()


if __name__ == '__main__':
    main({})
