"""
config.py

Contains default configuration settings. All of the values in this file
should be considered modifiable through user configuration.

Do not modify the values of this module at runtime.
    eg. config.defaults.AUTORUN = True
Instead, modify the values imported from this module into config.
    eg. config.AUTORUN = True

General Settings:
    OUTPUT_PATH: The default folder in which to save the converted
        project, download/extracted assets, and converted assets.

    PROJECT_PATH: The path to a project sb3 file to extract and convert

    PROJECT_URL: The path to a project to download and convert

    CONFIG_PATH: The config path specified by the command line -c
        argument.

    AUTOLOAD_CONFIG: Whether the config file should be autoloaded by
        the GUI if the default CONFIG_PATH points to it.

    USE_GUI: Whether the GUI should be run rather than running the
        converter directly.

    AUTORUN: Automatically run the project after the conversion has
        completed.
    TODO Disable autorun if there were warnings/errors

    PARSE_PROJECT: Whether to parse the project. Normally True.

    COPY_ENGINE: Whether to attempt to copy engine files. Normally
        True. To avoid overwritting modified engine files, use
        OVERWRITE_ENGINE instead.

    JSON_SHA: The expected SHA256 of a downloaded project.json. If
        the hash doesn't match when the json is downloaded, the
        conversion process will be aborted. Used as a safety measure to
        prevent a vulnerability from being exploited in one of the
        example projects. Not checked for extracted projects.

    IS_COMPILED: Whether to replace <is compiled?> procedure arguments
        with True, to emulate TurboWarp's behavior.

Asset Settings:
    FRESHEN_ASSETS: Overwrite existing assets when downloading or
        extracting the project rather than skipping them.
    VERIFY_ASSETS: Validate downloaded or extracted assets before
        saving them.

    CONVERT_SOUNDS: Allows disabling of mp3 conversion. When using
        Pygame 2+, mp3 conversion is not required, but it is still
        recommended.
    CONVERT_COSTUMES: Allows disabling of SVG conversion. When using
        Pygame 2+, SVG conversion is no required, but it is still
        recommended for maximum image quality.
    CONVERT_ASSETS: Allows disabling of all asset conversion.

    RECONVERT_SOUNDS: Convert and overwrite previously converted
        sounds. Useful if sounds were corrupted during conversion.
    RECONVERT_IMAGES: Convert and overwrite previously converted
        images. Useful if images were corrupted during conversion.

    CONVERT_THREADS: The number of threads to use when converting
        assets. Note that each thread usually creates a process.
    TODO Default CONVERT_THREADS to cpu_count?

    CONVERT_TIMEOUT: The amount of time to allow an asset to convert.
        Useful to diagnose hanging during asset conversion.

    USE_SVG_CMD: Enables use of the cairosvg Python package. Using the
        cairosvg package is much faster than calling a command.
    SVG_COMMAND: The command used to convert an svg file to a png file.
        The input and output path will be passed through {INPUT} and
        {OUTPUT} format parameters. {DPI} or {SCALE} should also be
        used to allow adjustable bitmap resolution.

    BASE_DPI: The DPI of an unscaled SVG image.

    SVG_SCALE: How much to scale SVGs when converting to bitmap.

    MP3_COMMAND: The command used to convert an mp3 file to a wav file.
        The input and output path will be passed through {INPUT} and
        {OUTPUT} format parameters.

Optimizations Settings:
    LEGACY_LISTS: Use list classes wth maximum compatibility for legacy
        indices (first, last, random, all). Only necessary if a block
        containing a legacy index is used instead of directly putting
        first/last/random/all in the list block.

    VAR_TYPES: Enables variable type guessing. Disabling may improve
        compatibility as type guessing is still a work in progress.

    ARG_TYPES: Enables type guessing for custom block arguments. As
        with VAR_TYPES, disabling may improve compatibility.

    LIST_TYPES: Enables lists to be detected a Static, or unchanging.
    TODO LIST_TYPES is a bad name

    SOLO_BROADCASTS: Treats broadcasts with only a single receiver in
        sprites which aren't cloned sort of like cross sprite custom
        blocks. May cause issues with projects which use a block in the
        create clone of block.

    DISABLE_ANY_CAST: Causes the type guesser to ignore items with the
        'any' type when guessing the type of an object. If the object
        is set to a item of any type, the item will be casted to the
        guessed type of the object. Is likely to cause incorrect type
        guesses unless variables are only used for a single type.

    AGGRESSIVE_NUM_CAST: If an object is ever set to a number, assume
        the object is of a numeric type.

    CHANGED_NUM_CAST: If a variable is ever changed using the
        "data_changevariableby" block, assume the variable is of a
        numeric type. NOTE: This is NOT disabled by VAR_TYPES.

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

    WARP_ALL: Enables warp on every custom block. May improve
        performance with certain projects, but will cause major issues
        with other projects.

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

    TARGET_CLUSTERS: Whether to group nodes belonging to each target
        when rendering the type graph

    PROC_CLUSTERS: Whether to group nodes belonging to a procedure when
        rendering the type graph
"""


# General Settings
OUTPUT_PATH = ""

PROJECT_PATH = ""
PROJECT_URL = ""

CONFIG_PATH = ""
AUTOLOAD_CONFIG = True

USE_GUI = False

AUTORUN = False

PARSE_PROJECT = True
COPY_ENGINE = True

JSON_SHA = None

IS_COMPILED = False

# Asset Settings
FRESHEN_ASSETS = False
VERIFY_ASSETS = True

CONVERT_SOUNDS = False
CONVERT_COSTUMES = True
CONVERT_ASSETS = True
RECONVERT_SOUNDS = False
RECONVERT_IMAGES = False

CONVERT_THREADS = 8
CONVERT_TIMEOUT = 30

# SVG Conversion
USE_SVG_CMD = False
SVG_COMMAND = 'inkscape -l -d {DPI} -o {OUTPUT} {INPUT}'
# SVG_COMMAND = "cairosvg {INPUT} -o {OUTPUT} -s {SCALE}"

BASE_DPI = 96
SVG_SCALE = 2

# MP3 Conversion
MP3_COMMAND = (
    r'"C:\Program Files\VideoLAN\VLC\vlc.exe" '
    '-I dummy --sout "#transcode{{acodec=s16l,channels=2}}:'
    'std{{access=file,mux=wav,dst={OUTPUT}}}" {INPUT} vlc://quit'
)

# Optimization Settings
LEGACY_LISTS = False

VAR_TYPES = True
ARG_TYPES = True
LIST_TYPES = True

SOLO_BROADCASTS = True

# Adjust Aggression
DISABLE_ANY_CAST = False
AGGRESSIVE_NUM_CAST = False
CHANGED_NUM_CAST = False
DISABLE_STR_CAST = False  # TODO Set to True
DISABLE_INT_CAST = True

SIG_DIGITS = 17

# Download Settings
PROJECT_TOKEN_HOST = "https://api.scratch.mit.edu/projects"
PROJECT_HOST = "https://projects.scratch.mit.edu"
ASSET_HOST = "https://assets.scratch.mit.edu"

DOWNLOAD_THREADS = 16

# Debug Settings
LOG_LEVEL = 20
DEBUG_JSON = False
FORMAT_JSON = True
OVERWRITE_ENGINE = True
DEFAULT_GUI_TAB = "convert"
EXAMPLES_PATH = None

GRAPH_ENGINE = 'dot'
RENDER_GRAPH = False
TARGET_CLUSTERS = False
PROC_CLUSTERS = False

# Miscellaneous
WARP_ALL = False
