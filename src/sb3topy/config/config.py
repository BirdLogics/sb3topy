"""
config_funcs.py

Handles reading and writing the configuration to a json file.

MODIFIABLE: A set of all converter settings which can be set
    using a config file.

DEFAULTS: A dict containing the default values of all modifiable config
    values.

TODO This method of configuration feels hacky
"""

import argparse
import json

from .. import config
from . import defaults

__all__ = ('restore_defaults', 'save_config', 'load_config', 'parse_args')

MODIFIABLE = {
    "OUTPUT_PATH",
    "PROJECT_PATH",
    "PROJECT_URL",
    "AUTORUN",

    "FRESHEN_ASSETS",
    "VERIFY_ASSETS",
    "CONVERT_MP3",
    "CONVERT_ASSETS",
    "RECONVERT_SOUNDS",
    "RECONVERT_IMAGES",
    "CONVERT_THREADS",
    "SVG_COMMAND",
    "INKSCAPE_PATH",
    "SVG_SCALE",
    "MP3_COMMAND",
    "VLC_PATH",

    "LEGACY_LISTS",
    "VAR_TYPES",
    "ARG_TYPES",
    "LIST_TYPES",
    "DISABLE_ANY_CAST",
    "AGGRESSIVE_NUM_CAST",
    "CHANGED_NUM_CAST",
    "DISABLE_STR_CAST",
    "DISABLE_INT_CAST",

    "PROJECT_HOST",
    "ASSET_HOST",
    "DOWNLOAD_THREADS",

    "LOG_LEVEL",
    "DEBUG_JSON",
    "FORMAT_JSON",
    "OVERWRITE_ENGINE",

    "WARP_ALL"
}


def get_config():
    """Returns a dict containing modifiable config values"""
    # Get current configuration values
    return {value: getattr(config, value)
            for value in MODIFIABLE}


def set_config(new_config):
    """
    Sets modifiable config values from a dict.

    If the value of a setting is None, it will be skipped.
    """
    for name, value in new_config.items():
        if name in MODIFIABLE and value is not None:
            setattr(config, name, value)


def restore_defaults():
    """Restores the default values of modifiable options"""
    for name in MODIFIABLE:
        value = getattr(defaults, name)
        setattr(config, name, value)


def save_config(path, skip_unmodified=True):
    """
    Saves the configuration in a json file, optionally skipping
    unmodified configuration values.
    """
    current_config = get_config()

    # Remove unmodified config values
    if skip_unmodified:
        for name, value in current_config.items():
            if value == getattr(defaults, name):
                del current_config[name]

    # Save the configuration
    with open(path, 'w') as config_file:
        json.dump(current_config, config_file)


def load_config(path, load_defaults=True):
    """
    Loads a configuration from a json file, optionally restoring
    defaults before doing so.
    """
    # Restore defaults
    if load_defaults:
        restore_defaults()

    # Load the json
    with open(path, 'r') as config_file:
        new_config = json.load(config_file)

    # Read the settings
    set_config(new_config)


def parse_args(args=None):
    """
    Allows configuration through a command line interface
    """
    # Initialize the parser
    parser = argparse.ArgumentParser(
        description="Converts sb3 files to Python.",
        epilog="Additional options can be set using a config file."
    )

    # Add arguments
    parser.add_argument("PROJECT", nargs='?',
                        help="path to a sb3 project")
    parser.add_argument("OUTPUT_DIR", nargs='?',
                        help="specifies an output directory")
    parser.add_argument("-c", dest="CONFIG_PATH", metavar="file",
                        help="path to a configuration json")
    parser.add_argument("-d", dest="DOWNLOAD_PROJECT", action="store_true",
                        help="marks the project path as a URL")

    # Parse arguments
    args = parser.parse_args(args)

    # Load a config file
    if args.CONFIG_PATH:
        load_config(args.CONFIG_PATH)

    # Read config data
    set_config(vars(args))
