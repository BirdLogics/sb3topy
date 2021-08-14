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

from ..config import __dict__ as config
from .consts import __dict__ as consts
from .defaults import __dict__ as defaults

__all__ = ('restore_defaults', 'save_config', 'load_config',
           'parse_args', 'get_config', 'set_config')


def get_config(skip_unmodified=False):
    """
    Returns a dict containing modifiable config values, optionally
    omitting config values which have not been modified.
    """
    if skip_unmodified:
        # Return modifiable config values which have been modified
        return {
            name: value for name, value in config.items()
            if name in defaults and value != defaults[name]
        }

    # Return all modified config values
    return {
        name: value for name, value in config.items()
        if name in defaults
    }


def set_config(new_config):
    """
    Sets modifiable config values from a dict.

    If the value of a setting is None, it will be skipped.
    """
    for name, value in new_config.items():
        if name in defaults:
            if value is not None:
                config[name] = value
        elif name in consts:
            logging.warning(
                "Attempt to set constant config value '%s' to '%s", name, value)
        else:
            logging.warning(
                "Cannot set unknown config value '%s' to '%s'", name, value)

    # Remove names not in defaults and None values
    filtered = {name: value for name, value in new_config.items()
                if name in defaults and value is not None}
    config.update(filtered)


def restore_defaults():
    """Sets modifiable config values to their defaults"""
    config.update(defaults)


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
    """
    # Restore defaults
    if load_defaults:
        restore_defaults()

    # Load the json
    with open(load_path, 'r') as config_file:
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
    parser.add_argument("PROJECT_PATH", nargs='?',
                        help="path to a sb3 project")
    parser.add_argument("OUTPUT_PATH", nargs='?',
                        help="specifies an output directory")
    parser.add_argument("-c", dest="CONFIG_PATH", metavar="file",
                        help="path to a configuration json")
    # parser.add_argument("-d", dest="DOWNLOAD_PROJECT", action="store_true",
    #                     help="marks the project path as a URL")
    parser.add_argument("--no-gui", dest="USE_GUI", action="store_false",
                        help="disables the gui even when PROJECT is not specified")
    parser.add_argument("-r", dest="AUTORUN", action="store_true",
                        help="automatically runs the project when done")

    # Parse arguments
    args = parser.parse_args(args)

    # If a project is specified, disable GUI
    if args.PROJECT_PATH:
        args.USE_GUI = False

    # Load a config file
    if args.CONFIG_PATH:
        load_config(args.CONFIG_PATH)

    # Read config data
    set_config(vars(args))


# Load config file from the directory of this module
load_config(path.join(path.dirname(__file__), "config.json"))
