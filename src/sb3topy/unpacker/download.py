"""
download.py

Used to download a project into the temp folder.
"""

import logging
import re
from hashlib import md5, sha256
from multiprocessing.pool import ThreadPool
from os import path

import requests

from .. import config
from ..project import Project

__all__ = ['download_project', 'Download']


def download_project(project_url, output_dir=None):
    """
    Downloads a project's assets into a folder. The project.json
    is not saved, but it is returned as part of a Project object.

    project_url: Either a full project_url, or just a project id.
    output_dir: An optional folder to save the downloaded data to.
        If a folder is not provided, one will be created by Project.
    """
    match = re.search(r"\d+", project_url)
    if match is None:
        logging.error("Invalid project url '%s'", project_url)
        return None

    logging.info("Downloading project...")

    return Download(match[0], output_dir).project


class Download:
    """
    Downloads a project given a project id

    Attributes:
        project_id: The project id of the project to download
        project: The Project instance containing the project.json,
            output directory, and asset md5ext set.
    """

    def __init__(self, project_id, output_dir=None):
        self.project_id = project_id

        # Download the project json
        project_json = self.download_json()

        # Verify the json was loaded correctly
        if project_json is None:
            self.project = None
            return

        # Create the Project instance
        self.project = Project(project_json, output_dir)

        # Download the assets
        pool = ThreadPool(config.DOWNLOAD_THREADS)
        results = pool.imap_unordered(
            self.download_asset, self.project.assets)
        for _ in results:
            pass
        pool.close()

    def download_json(self):
        """Downloads and returns the project.json"""
        url = f"{config.PROJECT_HOST}/{self.project_id}"

        # Download the project.json
        try:
            resp = requests.get(url)
            resp.raise_for_status()
        except requests.exceptions.RequestException as exc:
            logging.error(
                "Failed to download project json from '%s':\n%s", url, exc)
            return None

        # Verify the json SHA256 matches
        if config.JSON_SHA:
            json_hash = sha256(resp.content).hexdigest()
            if json_hash != config.JSON_SHA:
                logging.error(
                    "SHA256 of JSON failed (project has been modified):\n%s", json_hash)
                return None

        return resp.json()

    def download_asset(self, md5ext):
        """
        Downloads an asset and saves it to the output folder
        based on a md5ext. The md5ext must be validated.

        Intended for use in a Pool.
        """
        # Get download and save paths from md5ext
        url = f"{config.ASSET_HOST}/internalapi/asset/{md5ext}/get/"
        save_path = path.join(self.project.output_dir, "assets", md5ext)

        # If the file already exists, don't download it
        if path.isfile(save_path) and not config.FRESHEN_ASSETS:
            logging.debug(
                "Skipping download of asset '%s' (already exists)", md5ext)
            return True

        logging.debug("Downloading asset '%s' to '%s'", url, save_path)

        # Download the asset
        try:
            resp = requests.get(url)
            resp.raise_for_status()
        except requests.exceptions.RequestException as exc:
            logging.error(
                "Failed to download asset from '%s':\n%s", url, exc)
            return False

        # Verify the asset's md5 hash
        if config.VERIFY_ASSETS:
            md5_hash = md5(resp.content).hexdigest()
            if not md5_hash + '.' + md5ext.partition('.')[2] == md5ext:
                logging.error(
                    "Downloaded asset '%s' has an invalid md5: '%s'", md5ext, md5_hash)
                return False

        # Save the asset
        with open(save_path, 'wb') as asset_file:
            asset_file.write(resp.content)

        return True
