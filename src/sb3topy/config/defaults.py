"""
config.py

Contains default configuration settings

General Settings:
    OUTPUT_PATH: The default folder in which to save the converted
        project, download/extracted assets, and converted assets.

    PROJECT: The path to a project sb3 file to convert
    DOWNLOAD_PROJECT: Specifies that the project path is a url

    CONFIG_PATH: The config path specified by the command line -c
        argument.

    USE_GUI: Whether the GUI should be run rather than running the
        converter directly.

    AUTORUN: Automatically run the project after the conversion has
        completed.
    TODO Disable autorun if there were warnings/errors

    PARSE_PROJECT: Whether to parse the project. Normally True.

    COPY_ENGINE: Whether to attempt to copy engine files. Normally
        True. To avoid overwritting modified engine files, use
        OVERWRITE_ENGINE instead.

Asset Settings:
    IMAGE_TYPES: A tuple of known supported image types
    SOUND_TYPES: A tuple of known supported sound types

    FRESHEN_ASSETS: Overwrite existing assets when downloading or
        extracting the project rather than skipping them.
    VERIFY_ASSETS: Validate downloaded or extracted assets before
        saving them.

    CONVERT_MP3: Allows disabling of mp3 conversion. When using
        Pygame 2+, mp3 conversion is not required, but it is still
        recommended.
    CONVERT_ASSETS: Allows disabling of asset conversion. The project
        will not be able to if any svgs are in the project.

    RECONVERT_SOUNDS: Convert and overwrite previously converted
        sounds. Useful if sounds were corrupted during conversion.
    RECONVERT_IMAGES: Convert and overwrite previously converted
        images. Useful if images were corrupted during conversion.

    CONVERT_THREADS: The number of threads to use when converting
        assets. Note that each thread usually creates a process.
    TODO Default CONVERT_THREADS to cpu_count?

    CONVERT_TIMEOUT: The amount of time to allow an asset to convert.
        Useful to diagnose hanging during asset conversion.

    SVG_COMMAND: The command used to convert an svg file to a png file.
        The input and output path will be passed through {INPUT} and
        {OUTPUT} format parameters. {DPI} or {SCALE} should also be
        used to allow adjustable bitmap resolution.
    INKSCAPE_PATH: Passed to SVG_COMMAND as {INKSCAPE_PATH}
    TODO Remove INKSCAPE_PATH

    BASE_DPI: The DPI of an unscaled SVG image.
    SVG_SCALE: How much to scale SVGs when converting to bitmap.
    SVG_DPI: The calculated DPI of the SVG conversion.

    BLANK_SVG_HASHES: A tuple of md5exts which are blanks svg images.
        Some svg converters (cairosvg) don't work with these svgs, so
        the FALLBACK_IMAGE is used rather than attempting conversion.
    FALLBACK_IMAGE: The binary data of a blank png image.

    MP3_COMMAND: The command used to convert an mp3 file to a wav file.
        The input and output path will be passed through {INPUT} and
        {OUTPUT} format parameters.
    VLC_PATH: Passed to MP3_COMMAND as {VLC_PATH}.
    TODO Remove VLC_PATH

Typing Settings:
    LEGACY_LISTS: Use list classes wth maximum compatibility for legacy
        indices (first, last, random, all). Only necesary if a block
        containing a legacy index is used instead of directly putting
        first/last/random/all in the list block.

    VAR_TYPES: Enables variable type guessing. Disabling may improve
        compatibility as type guessing is still a work in progress.

    ARG_TYPES: Enables type guessing for custom block arguments. As
        with VAR_TYPES, disabling may improve compatibility.

    LIST_TYPES: Enables lists to be detected a Static, or unchanging.
    TODO LIST_TYPES is a bad name

    DISABLE_ANY_CAST: Causes the type guesser to ignore items with the
        'any' type when guessing the type of an object. If the object
        is set to a item of any type, the item will be casted to the
        guessed type of the object.

    AGGRESSIVE_NUM_CAST: If an object is ever set to a number, assume
        the object is of a numeric type.

    CHANGED_NUM_CAST: If a variable is ever changed using the "data_change
       variableby" block, assume the variable is of a numeric type.

    DISABLE_STR_CAST: If an object is set to both a string and a
        number assume the object is of the any type rather than the str
        type. Assuming the object is any prevents a primarily numeric
        object from frequently casting a number to a string, and then
        back to a number again when the object is used.
    TODO Used as type detection?

    DISABLE_INT_CAST: Due to flaws in type detection, float objects can
        sometimes be incorrectly detected as integer objects.
    TODO Use block return types in type detection

    SIG_DIGITS: Floating point values lose accuracy when they get too
        long. Only values which have fewer characters than SIG_DIGITS
        after the decimal point (or the entire value for ints) will be
        detected a number. Other values are assumed to be strings.

Download Settings:
    PROJECT_HOST: The path to the projects website.
    ASSET_HOST: The path to the assets website.

    DOWNLOAD_THREADS: The number of threads to use when downloading
        project assets.

DEBUG_SETTINGS:
    LOG_LEVEL: The log level to set when initializing the logger.

    DEBUG_JSON: Saves a copy of the project.json when converting the
        project. Adds a small amount of time to the conversion
        process.

    FORMAT_JSON: Adds indentation to the saved debug json. Adds even
        more time to the conversion process.

    OVERWRITE_ENGINE: Deletes the engine folder from the output
        directory before copying files. Otherwise, if the engine folder
        exists, the engine will not be copied, even if it has been
        modified.
    
    DEFAULT_GUI_TAB: The default tab to switch to in the GUI. It can be
        useful to automatically switch to examples when testing. May be
        'convert', 'examples', 'output', or 'settings'

Miscellaneous:
    WARP_ALL: Enables warp on every custom block. May improve
        performance with certain projects, but will cause major issues
        with other projects.
"""


# General Settings
OUTPUT_PATH = ""

PROJECT_PATH = ""
PROJECT_URL = ""

CONFIG_PATH = ""

USE_GUI = False

AUTORUN = False

PARSE_PROJECT = True
COPY_ENGINE = True

# Asset Settings
IMAGE_TYPES = ('png', 'svg', 'jpg')
SOUND_TYPES = ('wav', 'mp3')

FRESHEN_ASSETS = False
VERIFY_ASSETS = True

CONVERT_MP3 = True
CONVERT_ASSETS = True
RECONVERT_SOUNDS = False
RECONVERT_IMAGES = False

CONVERT_THREADS = 8
CONVERT_TIMEOUT = None

# SVG Conversion
SVG_COMMAND = "cairosvg {INPUT} -o {OUTPUT} -s {SCALE}"
# SVG_COMMAND = '{INKSCAPE_PATH} -l -d {DPI} -o {OUTPUT} {INPUT}'
INKSCAPE_PATH = '"C:/Program Files/Inkscape/bin/inkscape.com"'

BASE_DPI = 96
SVG_SCALE = 2
SVG_DPI = BASE_DPI * SVG_SCALE

BLANK_SVG_HASHES = (
    '3339a2953a3bf62bb80e54ff575dbced.svg',

    # TODO Verify these are actually blank (pokemon4.sb3)
    '14e46ec3e2ba471c2adfe8f119052307.svg',
    '09f60d713153e3d836152b1db500afd1.svg',
    '5adf038af4cd6319154b5601237092fa.svg'
)
FALLBACK_IMAGE = (
    b"\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\x01\x00\x00\x00\x01"
    b"\x08\x06\x00\x00\x00\x1f\x15\xc4\x89\x00\x00\x00\x0bIDAT\x18Wc`\x00"
    b"\x02\x00\x00\x05\x00\x01\xaa\xd5\xc8Q\x00\x00\x00\x00IEND\xaeB`\x82"
)

# MP3 Conversion
MP3_COMMAND = (
    '{VLC_PATH} -I dummy --sout "#transcode{{acodec=s16l,channels=2}}:'
    'std{{access=file,mux=wav,dst={OUTPUT}}}" {INPUT} vlc://quit'
)
VLC_PATH = r'"C:\Program Files\VideoLAN\VLC\vlc.exe"'

# Typing Settings
LEGACY_LISTS = False

VAR_TYPES = False
ARG_TYPES = False
LIST_TYPES = True

# Adjust Aggression
DISABLE_ANY_CAST = True
AGGRESSIVE_NUM_CAST = False
CHANGED_NUM_CAST = True
DISABLE_STR_CAST = True
DISABLE_INT_CAST = True

SIG_DIGITS = 17

# Download Settings
PROJECT_HOST = "https://projects.scratch.mit.edu"
ASSET_HOST = "https://assets.scratch.mit.edu"

DOWNLOAD_THREADS = 16

# Debug Settings
LOG_LEVEL = 20
DEBUG_JSON = True
FORMAT_JSON = True
OVERWRITE_ENGINE = True
DEFAULT_GUI_TAB = "convert"

# Miscellaneous
WARP_ALL = False
