"""
config.py

Loads converter configuration
"""

import sys
import json


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
TEMP_FOLDER = _CONFIG.get('temp_folder', "temp")

# Parser options
SPECMAP_PATH = _CONFIG.get("specmap_path", "data/specmap2.txt")

WARP_ALL = _CONFIG.get("warp_all", False)

# Unpacker options
IMAGE_TYPES = ('png', 'svg', 'jpg')
SOUND_TYPES = ('wav', 'mp3')

SVG_COMMAND = _CONFIG.get(
    'svg_convert_cmd',
    '"C:/Program Files/Inkscape/bin/inkscape.exe" -l -o "{OUTPUT}" "{INPUT}"'
)
SVG_DPI = _CONFIG.get('svg_dpi')
SVG_SCALE = _CONFIG.get('svg_scale')

MP3_COMMAND = _CONFIG.get(
    'mp3_convert_cmd',
    '"C:\\Program Files\\VideoLAN\\VLC\\vlc.exe" -I dummy --sout "#transcode{{acodec=s16l,channels=2}}:std{{access=file,mux=wav,dst=\'{OUTPUT}\'}}" "{INPUT}" vlc://quit'
)

LOG_LEVEL = _CONFIG.get('log_level', 20)
DEBUG_JSON = _CONFIG.get('debug_json', True)

# Max number of digits to convert str to float
SIG_DIGITS = 17

# Disable variable type guessing
VAR_TYPES = True
ARG_TYPES = True
