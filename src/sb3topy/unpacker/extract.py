"""
extract.py

Used to extract a project into the temp folder.
"""

import json
import logging
import zipfile
from hashlib import md5
from os import path

from .. import config
from ..project import Project

__all__ = ['extract_project', 'Extract']


def extract_project(project_path, output_dir=None):
    """
    Extracts a project's assets assets into a folder. The project.json
    is not saved, but is returned as part of the Project object.

    project_path: The path to the project sb3 file.
    output_dir: An optional folder to save the downloaded data to.
        If a folder is not provided, one will be created by Project.
    """
    project_zip = None
    try:
        project_zip = zipfile.ZipFile(project_path, 'r')

        if not "project.json" in project_zip.namelist():
            logging.error(
                "Could not find 'project.json' in '%s'", project_path)
            return None

        logging.info("Extracting project...")
        return Extract(project_zip, output_dir).project

    except FileNotFoundError:
        logging.error("Invalid project path '%s'", project_path)
        return None

    except zipfile.BadZipFile:
        logging.error("Invalid project sb3 '%s'", project_path)
        return None

    finally:
        if project_zip is not None:
            project_zip.close()


class Extract:
    """
    Extracts a project given a ZipFile of the project sb3
    """

    def __init__(self, project_zip: zipfile.ZipFile, output_dir=None):
        self.project_zip = project_zip

        # Extract the project json
        project_json = self.extract_json()

        # Create the Project instance
        self.project = Project(project_json, output_dir)

        # Extract assets from the project
        for md5ext in self.project.assets:
            self.extract_asset(md5ext)

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
        save_path = path.join(self.project.output_dir, "assets", md5ext)

        # If the file already exists, don't download it
        if path.isfile(save_path) and not config.FRESHEN_ASSETS:
            logging.debug("Skipping existing asset '%s'", md5ext)
            return True

        logging.debug("Extracting asset '%s' to '%s'", md5ext, save_path)

        # Extract the asset
        asset = self.project_zip.read(md5ext)

        # Verify the asset's md5 hash
        if config.VERIFY_ASSETS:
            md5_hash = md5(asset).hexdigest()
            if not md5_hash + '.' + md5ext.partion('.')[2] == md5ext:
                logging.error(
                    "Extracted asset '%s' has an invalid md5: '%s'", md5ext, md5_hash)
                return False

        # Save the asset
        with open(save_path, 'wb') as asset_file:
            asset_file.write(asset)

        return True
