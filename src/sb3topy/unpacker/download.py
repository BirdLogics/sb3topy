"""
download.py

Used to download a project into the temp folder.
"""

import logging
import re
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
    match = re.match(r"\d+", project_url)
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
        resp = requests.get(url)
        return resp.json()

    def download_asset(self, md5ext):
        """
        Downloads an asset and saves it to the output folder
        based on a md5ext. The md5ext must be validated.

        Intended for use in a Pool.
        """
        # Get download and save paths from md5ext
        url = f"{config.ASSET_HOST}/internalapi/asset/{md5ext}/get/"
        save_path = path.join(self.project.output_dir, md5ext)

        logging.debug("Downloading %s to %s", url, save_path)

        # Download the asset
        resp = requests.get(url)

        # Save the set
        with open(save_path, 'wb') as asset_file:
            asset_file.write(resp.content)
