"""
config.py

Contains functions for handling configuration files, parsing command
line arguments, and creating config dicts.

Although this method of storing config feels a little hacky, the end
result seems to work quite well.
"""

import argparse
import json
import logging
from os import path

from ..config import __dict__ as _config
from .consts import __dict__ as _consts
from .defaults import __dict__ as _defaults
from .project import __dict__ as _project

__all__ = ('restore_defaults', 'save_config', 'load_config',
           'parse_args', 'get_config', 'set_config', 'AUTOLOAD_PATH')

logger = logging.getLogger(__name__)


all_defaults = {}
for _key, _value in _defaults.items():
    if _key[0] != '_':
        all_defaults[_key] = _value
for _key, _value in _project.items():
    if _key[0] != '_':
        all_defaults[_key] = _value


def get_config(skip_unmodified=False):
    """
    Returns a dict containing modifiable config values, optionally
    omitting config values which have not been modified.
    """

    if skip_unmodified:
        # Return modifiable config values which have been modified
        return {
            name: value for name, value in _config.items()
            if name in all_defaults and value != all_defaults[name]
        }

    # Return all modified config values
    return {
        name: value for name, value in _config.items()
        if name in all_defaults
    }


def set_config(new_config, skip_none=False):
    """
    Sets modifiable config values from a dict.

    If the value of a setting is None, it may be skipped.
    """
    for name, value in new_config.items():
        if name in all_defaults:
            if not skip_none or value is not None:
                _config[name] = value
        elif name in _consts:
            logger.warning(
                "Attempt to set constant config value '%s' to '%s'", name, value)
        else:
            logger.warning(
                "Cannot set unknown config value '%s' to '%s'", name, value)

    # Remove names not in all_defaults and None values
    filtered = {name: value for name, value in new_config.items()
                if name in all_defaults and value is not None}
    _config.update(filtered)


def restore_defaults():
    """Sets modifiable config values to their defaults"""
    _config.update(all_defaults)


def save_config(save_path, skip_unmodified=True):
    """
    Saves the configuration in a json file, optionally skipping
    unmodified config values.
    """
    # Get the current configuration
    current_config = get_config(skip_unmodified)

    # Save the configuration
    with open(save_path, 'w') as config_file:
        json.dump(current_config, config_file, indent=4)


def load_config(load_path, load_defaults=True):
    """
    Loads the configuration from a json file, optionally restoring
    defaults before doing so.

    Config files may contain an AUTOLOAD value. If autoloaded is True
    and the config file's AUTOLOAD value is false, the file will not be
    loaded.
    """
    # Restore defaults
    if load_defaults:
        restore_defaults()

    # Load the json
    with open(load_path, 'r') as config_file:
        new_config = json.load(config_file)

    # Read the configuration
    set_config(new_config)


def _autoload_config(load_path):
    """
    Used when autoloading a config file. Reads the file with caution,
    and if it has the value set to False, doesn't load the config.
    """
    # Verify the path is valid
    if not path.isfile(load_path):
        _config['AUTOLOAD_CONFIG'] = False
        return

    # Open and try to decode the file
    with open(load_path, 'r') as config_file:
        try:
            new_config = json.load(config_file)
        except json.JSONDecodeError:
            logger.error("Failed to autoload config '%s'", load_path)
            _config['AUTOLOAD_CONFIG'] = False
            return

    # Read the configuration
    if new_config.get("AUTOLOAD_CONFIG", True):
        set_config(new_config)
    else:
        _config['AUTOLOAD_CONFIG'] = False


def parse_args(args=None):
    """
    Allows configuration through a command line interface
    """
    # Initialize the parser
    parser = argparse.ArgumentParser(
        prog="sb3topy",
        description="Converts sb3 files to Python.",
        epilog="Additional options can be set using a config file."
    )

    # Add arguments
    parser.add_argument("PROJECT_PATH", nargs='?',
                        help="path to a sb3 project")
    parser.add_argument("OUTPUT_PATH", nargs='?',
                        help="specifies an output directory")
    parser.add_argument("-c", dest="CONFIG_PATH", metavar="file",
                        nargs='?', default=None, const=False,
                        help="path to a config json, disables autoload")
    # parser.add_argument("-d", dest="DOWNLOAD_PROJECT", action="store_true",
    #                     help="marks the project path as a URL")
    parser.add_argument("--gui", dest="USE_GUI", action="store_true",
                        help="starts the graphical user interface")
    parser.add_argument("-r", dest="AUTORUN", action="store_true",
                        help="automatically runs the project when done")

    # Parse arguments
    args = parser.parse_args(args)

    # Load a config file
    autoload = args.CONFIG_PATH is None
    if args.CONFIG_PATH:
        args.CONFIG_PATH = path.abspath(args.CONFIG_PATH)
        load_config(args.CONFIG_PATH)
    else:
        args.CONFIG_PATH = AUTOLOAD_PATH

    # Load the default user config file
    if args.USE_GUI and autoload and AUTOLOAD_PATH:
        _autoload_config(AUTOLOAD_PATH)
    else:
        _config['AUTOLOAD_CONFIG'] = None

    # Read config data
    set_config(vars(args), True)


def set_all(value=1):
    """Used for debugging the gui, sets every setting to value"""
    for _key in all_defaults:
        _config[_key] = value


# Load config file from the directory of this module
load_config(path.join(path.dirname(__file__), "config.json"))
AUTOLOAD_PATH = path.normpath(path.expanduser(_config['CONFIG_PATH']))
