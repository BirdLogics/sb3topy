"""
extract.py

Used to extract a project into the temp folder.
"""

import json
import logging
import zipfile
from hashlib import md5
from os import path

from .. import config, project

__all__ = ['extract_project', 'Extract']

logger = logging.getLogger(__name__)


def extract_project(manifest: project.Manifest, project_path):
    """
    Extracts a project's json and assets, and returns a Project using
    the json. The assets are extracted into the folder provided by
    by `manifest`, but the project.json is not saved.

    All assets are added to the manifest. If an asset was not
    successfully extracted, the stored dict value will be `None`.
    Otherwise, the md5ext value will be stored.
    """

    logger.info("Extracting project...")
    logger.debug("Extracting project from '%s'", project_path)

    project_zip = None
    try:
        project_zip = zipfile.ZipFile(project_path, 'r')

        if not "project.json" in project_zip.namelist():
            logger.error(
                "Could not find 'project.json' in '%s'", project_path)
            return None

        return Extract(manifest, project_zip).project

    except FileNotFoundError:
        logger.error("Invalid project path '%s'", project_path)
        return None

    except zipfile.BadZipFile:
        logger.error("Invalid project sb3 '%s'", project_path)
        return None

    finally:
        if project_zip is not None:
            project_zip.close()


class Extract:
    """
    Helper class to create a Project given a ZipFile of a project sb3
    and a Manifest to provide the output directory. Successfully
    extracted assets are added to the manifest.

    Attributes:
        project: The Project instance containing the project.json data.

        output_dir: The output folder provided by the manifest.

        project_zip: The input sb3 ZipFile.
    """

    def __init__(self, manifest: project.Manifest, project_zip: zipfile.ZipFile):
        self.output_dir = manifest.output_dir
        self.project_zip = project_zip

        # Extract the project json
        project_json = self.extract_json()

        # Create the Project instance
        self.project = project.Project(project_json)

        # Extract assets from the project
        for md5ext in self.project.get_costumes():
            manifest.costumes[md5ext] = self.extract_asset(md5ext)
        for md5ext in self.project.get_sounds():
            manifest.sounds[md5ext] = self.extract_asset(md5ext)

    def extract_json(self):
        """Extracts and returns the project.json"""
        with self.project_zip.open("project.json", 'r') as project_json:
            return json.load(project_json)

    def extract_asset(self, md5ext):
        """
        Extracts an asset and saves it to the output folder
        based on a md5ext. The md5ext must be validated.
        """
        # Get the save path from the md5ext
        save_path = path.join(self.output_dir, "assets", md5ext)

        # If the file already exists, don't download it
        if path.isfile(save_path) and not config.FRESHEN_ASSETS:
            logger.debug(
                "Skipping extraction of asset '%s' (already exists)", md5ext)
            return md5ext

        logger.debug("Extracting asset '%s'", md5ext)

        # Extract the asset
        asset = self.project_zip.read(md5ext)

        # Verify the asset's md5 hash
        if config.VERIFY_ASSETS:
            md5_hash = md5(asset).hexdigest()
            if not md5_hash + '.' + md5ext.partition('.')[2] == md5ext:
                logger.error(
                    "Extracted asset '%s' has the wrong md5: '%s'", md5ext, md5_hash)
                return None

        # Save the asset
        with open(save_path, 'wb') as asset_file:
            asset_file.write(asset)

        return md5ext
