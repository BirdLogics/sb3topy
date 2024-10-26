"""
download.py

Used to download a project into the temp folder.
"""

import logging
import re
from hashlib import md5, sha256
from multiprocessing.pool import ThreadPool
from os import path

try:
    import requests
except ImportError:
    requests = None

from .. import config, project

__all__ = ['download_project', 'Download']

logger = logging.getLogger(__name__)


def download_project(manifest: project.Manifest, project_url):
    """
    Downloads a project's json and assets, and returns a Project using
    the json. The assets are downloaded into the folder provided by
    by `manifest`, but the project.json is not saved.

    All assets are added to the manifest. If an asset was not
    successfully extracted, the stored dict value will be `None`.
    Otherwise, the md5ext value will be stored.
    """

    match = re.search(r"\d+", project_url)
    if match is None:
        logger.error("Invalid project url '%s'", project_url)
        return None

    logger.info("Downloading project...")
    logger.debug("Downloading project '%s'", match[0])

    return Download(manifest, match[0]).project


class Download:
    """
    Downloads a project given a project id

    Helper class to download and create a Project given a project id
    and a Manifest to provide the output directory. Successfully
    downloaded assets are added to the manifest.

    Attributes:
        project: The Project instance containing the project.json data.

        output_dir: The output folder provided by the manifest.

        project_id: The project id of the project to download
    """

    def __init__(self, manifest: project.Manifest, project_id, output_dir=None):
        self.output_dir = manifest.output_dir
        self.project_id = project_id

        metadata = self.project_metadata()
        if metadata is None or "project_token" not in metadata:
            logger.critical(
                "Is the project shared? Failed to get project token.")
            self.project = None
            return

        # Download the project json
        project_json = self.download_json(metadata["project_token"])
        if project_json is None:
            self.project = None
            return

        # Create the Project instance
        self.project = project.Project(project_json)

        # Download the assets
        pool = ThreadPool(config.DOWNLOAD_THREADS)
        manifest.costumes.update(pool.imap_unordered(
            self.download_asset, self.project.get_costumes()))
        manifest.sounds.update(pool.imap_unordered(
            self.download_asset, self.project.get_sounds()))

        pool.close()

    def project_metadata(self):
        """Requests a token for the project."""

        url = f"{config.PROJECT_TOKEN_HOST}/{self.project_id}"

        try:
            resp = requests.get(url)
            resp.raise_for_status()
        except requests.exceptions.RequestException:
            logger.exception("Failed to get project metadata from '%s':", url)
            return None

        return resp.json()

    def download_json(self, token):
        """Downloads and returns the project.json"""
        # Verify requests is installed
        if requests is None:
            logger.error(
                "Failed to download project json; requests not installed.")
            return None

        url = f"{config.PROJECT_HOST}/{self.project_id}?token={token}"

        # Download the project.json
        try:
            resp = requests.get(url)
            resp.raise_for_status()
        except requests.exceptions.RequestException:
            logger.exception(
                "Failed to download project json from '%s':", url)
            return None

        # Verify the json SHA256 matches
        if config.JSON_SHA:
            logger.debug("Validating JSON SHA256...")
            json_hash = sha256(resp.content).hexdigest()

            # If JSON_SHA is set to True, give a warning
            # Tkinter variables treat True as 1
            if config.JSON_SHA in (True, 1):
                logger.warning("SHA256 not provided for JSON:\n%s", json_hash)
            elif json_hash != config.JSON_SHA:
                logger.error(
                    "SHA256 of JSON failed (project has been modified):\n%s", json_hash)
                return None

        return resp.json()

    def download_asset(self, md5ext):
        """
        Downloads an asset and saves it to the output folder
        based on a md5ext. The md5ext must be validated.

        Returns (md5ext, md5ext) if the asset was successfully
        downloaded, otherwise (md5ext, None).

        Intended for use in a Pool.
        """
        # Get download and save paths from md5ext
        url = f"{config.ASSET_HOST}/internalapi/asset/{md5ext}/get/"
        save_path = path.join(self.output_dir, "assets", md5ext)

        # If the file already exists, don't download it
        if path.isfile(save_path) and not config.FRESHEN_ASSETS:
            logger.debug(
                "Skipping download of asset '%s' (already exists)", md5ext)
            return md5ext, md5ext

        logger.debug("Downloading asset '%s'", md5ext)

        # Download the asset
        try:
            resp = requests.get(url)
            resp.raise_for_status()
        except requests.exceptions.RequestException:
            logger.exception(
                "Failed to download asset from '%s':", url)
            return md5ext, None

        # Verify the asset's md5 hash
        if config.VERIFY_ASSETS:
            md5_hash = md5(resp.content).hexdigest()
            if not md5_hash + '.' + md5ext.partition('.')[2] == md5ext:
                logger.error(
                    "Downloaded asset '%s' has the wrong md5: '%s'", md5ext, md5_hash)
                return md5ext, None

        # Save the asset
        with open(save_path, 'wb') as asset_file:
            asset_file.write(resp.content)

        return md5ext, md5ext
