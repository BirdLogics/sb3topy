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
