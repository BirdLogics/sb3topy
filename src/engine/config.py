"""
config.py

Contains configuration constants.

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
FS_SCALE - Changes the display size in fullscreen, potentially increasing
    performance at the cost of quality. With a factor of 2, the window
    size is half that of your computer, changing your resolution.

AUDIO_CHANNELS - The number of audio channels created for the pygame mixer

KEY_MAP - Maps pygame keys to their names in the project
"""

import json
import sys

import pygame as pg

# Load config json
try:
    with open('config.json', 'r') as _file:
        _CONFIG = json.load(_file)
except FileNotFoundError:
    _CONFIG = {}

# Version info
PG_VERSION = pg.version.vernum
PY_VERSION = sys.version_info
CF_VERSION = tuple(_CONFIG.get('config_version', ()))

# Timing options
TARGET_FPS = _CONFIG.get('target_fps', 31)
TURBO_MODE = _CONFIG.get('turbo_mode', False)
WORK_TIME = _CONFIG.get('work_time', 1 / 60)
WARP_TIME = _CONFIG.get('warp_time', 0.5)

FLIP_THRESHOLD = _CONFIG.get('flip_threshold', 1000 / 40)

# Display options
STAGE_SIZE = (480, 360)  # Legacy support
STAGE_WIDTH = _CONFIG.get('stage_width', 480)
STAGE_HEIGHT = _CONFIG.get('stage_height', 360)

DISPLAY_SIZE = (
    _CONFIG.get('display_width', 480),
    _CONFIG.get('display_height', 360)
)
FS_SCALE = 1
SCALED_DISPLAY = _CONFIG.get('display_scaled', False)
ALLOW_RESIZE = _CONFIG.get('allow_resize', True)
DISPLAY_FLAGS = 0

if SCALED_DISPLAY and PG_VERSION < (2,):
    print("Scaled display requires Pygame 2.")
    SCALED_DISPLAY = False

# Audio options
AUDIO_CHANNELS = _CONFIG.get('audio_channels', 8)
MASTER_VOLUME = _CONFIG.get('audio_volume', 1)

# Default limits
MAX_CLONES = _CONFIG.get('max_clones', 300)
MAX_LIST = _CONFIG.get('max_list_items', 200000)

# Debug config
SPRITE_RECTS = _CONFIG.get('sprite_rects', False)
REDRAW_RECTS = _CONFIG.get('redraw_rects', False)
PEN_RECTS = _CONFIG.get('pen_rects', False)
DRAW_FPS = _CONFIG.get('drawn_fps', False)

# Title config
DYNAMIC_TITLE = _CONFIG.get('dynamic_title', True)
TITLE = _CONFIG.get('title_text', "project.py (fps: {FPS:.2f}{TURBO})")

# Input option
ENABLE_TURBO = _CONFIG.get('turbo_hotkey', True)
ENABLE_FULLSCREEN = _CONFIG.get('fullscreen_hotkey', True)
DEBUG_HOTKEYS = _CONFIG.get('debug_hotkey', True)

KEY_MAP = {
    pg.K_SPACE: "space",
    pg.K_UP: "up arrow",
    pg.K_DOWN: "down arrow",
    pg.K_RIGHT: "right arrow",
    pg.K_LEFT: "left arrow",
    pg.K_RETURN: "enter"
}

# Misc
USERNAME = _CONFIG.get('username', "")
