"""
config.py

Loads converter configuration
"""

# pylint: disable=line-too-long

import json
import sys

# Allows CONFIG_PATH to be set with a module reload
try:
    CONFIG_PATH  # type: ignore
except NameError:
    CONFIG_PATH = sys.argv[1] if len(sys.argv) == 2 else 'data/config.json'

# Load config json
try:
    with open(CONFIG_PATH, 'r') as _file:
        _CONFIG = json.load(_file)
except FileNotFoundError:
    _CONFIG = {}

PROJECT_PATH = _CONFIG.get('project_path')
TEMP_FOLDER = _CONFIG.get('temp_folder')

# Parser options
SPECMAP_PATH = _CONFIG.get("specmap_path", "data/specmap2.txt")

WARP_ALL = _CONFIG.get("warp_all", False)

# Unpacker options
IMAGE_TYPES = ('png', 'svg', 'jpg')
SOUND_TYPES = ('wav', 'mp3')

INKSCAPE_PATH = '"C:/Program Files/Inkscape/bin/inkscape.exe"'
SVG_COMMAND = _CONFIG.get(
    'svg_convert_cmd', '{INKSCAPE_PATH} -l -o "{OUTPUT}" "{INPUT}"'
)
SVG_DPI = _CONFIG.get('svg_dpi')
SVG_SCALE = _CONFIG.get('svg_scale')

VLC_PATH = r'"C:\Program Files\VideoLAN\VLC\vlc.exe"'
MP3_COMMAND = _CONFIG.get(
    'mp3_convert_cmd', (
        '{VLC_PATH} -I dummy --sout "#transcode{{acodec=s16l,channels=2}}:'
        'std{{access=file,mux=wav,dst={OUTPUT}}}" {INPUT} vlc://quit'
    )
)

LOG_LEVEL = _CONFIG.get('log_level', 20)
DEBUG_JSON = _CONFIG.get('debug_json', True)

# Max number of digits to convert str to float
SIG_DIGITS = 17

# Disable variable type guessing
VAR_TYPES = True
ARG_TYPES = True
ENABLE_INT_ARGS = False

# Force legacy list indexing (first, last, random all)
LEGACY_LISTS = False

# If a variable is set to an unkown type, attempt to cast the
# unkown type rather than assuming the variable's type is unkown
DISABLE_ANY_CAST = True

# If a variable is ever set to a numeric value, assume
# it's type is numeric even if it is also set to a string
AGGRESSIVE_NUM_CAST = False

# If a variable is set to both a string and a number, assume the variable's
# type is unkown and don't cast when setting rather than casting to string
# Safer than AGGRESSIVE_NUM_CAST
DISABLE_STR_CAST = True

# If a variable is changed using the change by block, assume it is numeric
CHANGED_NUM_CAST = True

# Replace all int casts with float
# TODO This option shouldn't be necesary
DISABLE_INT_CAST = True

# Number of threads to use to download projects
DOWNLOAD_THREADS = 16

# Website to download projects from
PROJECT_HOST = "https://projects.scratch.mit.edu"
ASSET_HOST = "https://assets.scratch.mit.edu"

# TODO Define config values here
PROJECT_URL = "339207237"
OUTPUT_FOLDER = TEMP_FOLDER
CONVERT_ASSETS = True
CONVERT_MP3 = True
USE_CAIROSVG = True

# Blank PNG fallback image
FALLBACK_IMAGE = b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\x01\x00\x00\x00\x01\x08\x06\x00\x00\x00\x1f\x15\xc4\x89\x00\x00\x00\x0bIDAT\x18Wc`\x00\x02\x00\x00\x05\x00\x01\xaa\xd5\xc8Q\x00\x00\x00\x00IEND\xaeB`\x82'
BLANK_SVG_HASHES = ('3339a2953a3bf62bb80e54ff575dbced.svg',)
FORMAT_JSON = False
OVERWRITE_ENGINE = True

# Redownload/extract existing assets
FRESHEN_ASSETS = False

# Reconvert already converted assets
RECONVERT_SOUNDS = False
RECONVERT_IMAGES = False

# Verify the md5 of downloaded/extracted assets
VERIFY_ASSETS = True
