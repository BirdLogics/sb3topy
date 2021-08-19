"""
project.py

Contains configuration values which change how the project runs.
Note that this module contains the *default* values.

Timing Settings:
    TARGET_FPS: The fps at which to try to run the program

    TURBO_MODE: Whether to ignore redraw requests instead of waiting
        for the screen to be redrawn. Also disables the frame rate
        limit.

    WORK_TIME: How much time to spend running blocks before
        redrawing (seconds).
      = 1 / WORK_TIME_INV

    WARP_TIME: How long custom blocks are allowed to run without a
        screen refresh (seconds).

    FLIP_THRESHOLD: How long a screen redraw should take before Pygame
        should switch to flipping the entire screen (seconds.)
      = 1000 / FLIP_THRESHOLD_INV

Display Settings:
    STAGE_SIZE: The size of the stage.
      = (STAGE_WIDTH, STAGE_HEIGHT)

    DISPLAY_SIZE: The initial size of the window.
      = (DISPLAY_WIDTH, DISPLAY_HEIGHT)

    ALLOW_RESIZE: Allows the user to adjust the display size.

    FS_SCALE: Changes the display size in fullscreen, providing a
        performace boost at the cost of quality. When set to 2, the
        window size will be half that of the native computer
        resolution.

    SCALED_DISPLAY: Enables the Pygame 2 SCALED_DISPLAY option.

Title Settings:
    DYNAMIC_TITLE: Enables updating the title with information such
        as the current fps.

    TITLE: The title text to draw. May include formatting options such
        as {FPS} and {TURBO}

Audio Settings:
    AUDIO_CHANNELS: The number of audio channels to tell the pygame
        mixer to create.

    MASTER_VOLUME: Adjusts the volume of the entire project.

Limit Settings:
    MAX_CLONES: The maximum number of clones which may be created.
    TODO Set to None to disable

    MAX_LIST: The maximum number of items which may be added to a list.

Hotkey Settings:
    TURBO_HOTKEY: Whether to enable the turbo mode hotkey (f10)

    FULLSCREEN_HOTKEY: Whether to enable the fullscreen hotkey (f11)

    DEBUG_HOTKEYS: Whether to enable the debug hotkeys (f3 + s,r,d,p)

Debug Settings:
    DRAW_FPS: Draws a fps counter to the upper left corner of the
        screen.

    SPRITE_RECTS: Draws a rectangle around all visible sprites.

    REDRAW_RECTS: Draws a rectangle around every redraw area.

    PEN_RECTS: Draws a rectangle around every redrawn pen area.

Miscellaneous:
    USERNAME: The username to use for the username block.

    RANDOM_SEED: A number to seed the random number generator with
        before the project starts.
"""

PROJECT_DOCS = ''.join(__doc__.splitlines(True)[6:])

# Timing Settings
TARGET_FPS = 31
TURBO_MODE = False
WORK_TIME_INV = 60
WARP_TIME = 0.5

FLIP_THRESHOLD_INV = 40

# Display Settings
STAGE_WIDTH = 480
STAGE_HEIGHT = 360
DISPLAY_WIDTH = 480
DISPLAY_HEIGHT = 360

ALLOW_RESIZE = True

FS_SCALE = 1
SCALED_DISPLAY = False

# Title Settings
DYNAMIC_TITLE = True
TITLE = "project.py (fps: {FPS:.2f}{TURBO})"

# Audio Settings
AUDIO_CHANNELS = 8
MASTER_VOLUME = 1

# Limit Settings
MAX_CLONES = 300
MAX_LIST = 200000

# Hotkey Settings
TURBO_HOTKEY = True
FULLSCREEN_HOTKEY = True
DEBUG_HOTKEYS = True

# Debug Settings
DRAW_FPS = False
SPRITE_RECTS = False
REDRAW_RECTS = False
PEN_RECTS = False

# Miscellaneous
USERNAME = ""
RANDOM_SEED = None
