"""
project.py

Contains a helper class for managing the project and output directory.
"""

import json
import logging
import os
import tempfile
from os import path

from .parser import sanitizer

__all__ = ('Project', 'Manifest')

logger = logging.getLogger(__name__)


class Project:
    """
    Contains helper functions for managing the project.json. Also
    handles the asset manifest and ensures an output directory is
    available and correctly structured.

    Attributes:
        json: The project.json dictionary.

        assets: A dictionary manifest mapping the original md5ext of
            assets to the potentially new md5ext.

        output_dir: A folder which can be used to store the converted
            output of the project.

        _tempdir: If an output folder is not provided, this is a
            TemporaryDirectory tied to the output_dir.
    """

    def __init__(self, project_json):
        self.json = project_json

    def get_costumes(self):
        """
        Reads and validates all costume md5exts from the project json.
        """
        assets = {}
        for target in self.json.get('targets', []):
            for costume in target['costumes']:
                # Validate the md5ext
                if sanitizer.valid_md5ext(costume['md5ext']):
                    assets[costume['md5ext']] = None

                # Log invalid md5exts
                else:
                    logger.error(
                        "Invalid md5ext for costume '%s'", costume['md5ext'])
        return assets

    def get_sounds(self):
        """
        Reads and validates all sound md5exts from the project json.
        """
        assets = {}
        for target in self.json.get('targets', []):
            for sound in target['sounds']:
                # Validate the md5ext
                if sanitizer.valid_md5ext(sound['md5ext']):
                    assets[sound['md5ext']] = None

                # Log invalid md5exts
                else:
                    logger.error(
                        "Invalid md5ext for sound '%s'", sound['md5ext'])
        return assets

    def is_sb3(self):
        """
        Verifies the project is in the sb3 format. In the event of a
        failed detection, logs an error providing feedback. If the json
        is in the sb2 format, conversion info will be provided.
        """

        if not 'targets' in self.json:
            if 'objName' in self.json:
                logger.error((
                    "Project is in the sb2 format.\nPlease save the "
                    "project with Scratch 3 to convert it to an sb3."))
            else:
                logger.error("Invalid project.json.")

            return False
        return True

    def __getitem__(self, key):
        return self.json[key]


class Manifest:
    """
    Handles the output directory for a project.

    """

    def __init__(self, output_dir=None):
        # Create the manifest dicts
        self.sounds = {}
        self.costumes = {}

        # Save the output directory
        if output_dir:
            self._tempdir = None
            self.output_dir = output_dir

        # Get a temporary directory
        else:
            self._tempdir = tempfile.TemporaryDirectory()
            self.output_dir = self._tempdir.name
            logger.info("Created a temporary directory at '%s'",
                        self.output_dir)

        # Create the assets folder if one doesn't exist
        assets_dir = path.join(self.output_dir, "assets")
        if not path.isdir(assets_dir):
            os.mkdir(assets_dir)


def save_json(project: Project, manifest: Manifest, pretty=False):
    """Saves the project.json data in the output directory"""
    save_path = path.join(manifest.output_dir, "project.json")

    logger.info("Saving project.json to '%s'", save_path)

    with open(save_path, 'w', encoding='utf-8') as json_file:
        json.dump(project.json, json_file,
                  indent=4 if pretty else None)
