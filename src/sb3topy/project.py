"""
project.py

Holds a class which holds the project.json and other info
"""

import json
import logging
import os
import tempfile
from os import path

from .parser import sanitizer

__all__ = ('Project',)


class Project:
    """
    Represents an sb3 project

    Attributes:
        json: The project.json data
        assets: A set of all valid asset md5ext in the project
        output_dir: A folder containing data for this project

        _tempdir: If an output folder is not specified in config,
            this is a TemporaryDirectory which will be used for path
    """

    def __init__(self, project_json, output_dir=None):
        # Save the project json
        self.json = project_json

        # Get a folder to save the output to
        if output_dir:
            self._tempdir = None
            self.output_dir = output_dir
        else:
            self._tempdir = tempfile.TemporaryDirectory()
            self.output_dir = self._tempdir.name
            logging.info("Created temp file at '%s'", self.output_dir)

        # Create an assets folder if one doesnt exist
        assets_dir = path.join(self.output_dir, "assets")
        if not path.isdir(assets_dir):
            os.mkdir(assets_dir)

        # Read assets from the project json
        self.assets = {}
        self._init_assets()

    def _init_assets(self):
        """Reads and validates md5exts from the project json"""
        # Add valid md5exts to the assets set
        for sprite in self.json['targets']:
            # Read costume md5exts
            for costume in sprite['costumes']:
                if sanitizer.valid_md5ext(costume['md5ext']):
                    self.assets[costume['md5ext']] = None
                else:
                    logging.error("Invalid costume md5ext '%s'",
                                  costume['md5ext'])

            # Read sound md5exts
            for sound in sprite['sounds']:
                if sanitizer.valid_md5ext(sound['md5ext']):
                    self.assets[sound['md5ext']] = None
                else:
                    logging.error("Invalid sound md5ext '%s'", sound['md5ext'])

    def save_json(self, pretty=False):
        """Saves the project.json data in the output directory"""
        save_path = path.join(self.output_dir, "project.json")

        logging.info("Saving project.json to '%s'", save_path)

        with open(save_path, 'w') as json_file:
            json.dump(self.json, json_file,
                      indent=4 if pretty else None)

    def __getitem__(self, key):
        return self.json[key]
