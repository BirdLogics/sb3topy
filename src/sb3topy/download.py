"""
download.py

Downloads projects from the internet
"""

import logging
from multiprocessing.pool import ThreadPool
from os import path
from tempfile import TemporaryDirectory
from zipfile import ZipFile

import requests

from .parser import sanitizer

# from . import config

PROJECT_SERVER = "https://projects.scratch.mit.edu/{}"
ASSET_SERVER = "https://assets.scratch.mit.edu/internalapi/asset/{}/get/"


def download(project_id, zip_path):
    """Downloads a project into a zip file"""
    with ZipFile(zip_path, 'w') as sb3_zip:
        # First, get the project json
        print("Downloading 'project.json'")
        resp = requests.get(PROJECT_SERVER.format(project_id))
        sb3_zip.writestr('project.json', resp.content)
        sb3_json = resp.json()

        # Download all assets
        for md5ext in asset_list(sb3_json):
            print(f"Downloading '{md5ext}'")
            asset = requests.get(ASSET_SERVER.format(md5ext)).content
            sb3_zip.writestr(md5ext, asset)


def download2(project_id, zip_path):
    """Downloads a project into a zip file"""
    project_json = requests.get(PROJECT_SERVER.format(project_id)).json()
    assets = asset_list(project_json)

    with TemporaryDirectory() as temp_dir:
        pool = ThreadPool(32)
        result = pool.imap_unordered(
            download_file,
            ((ASSET_SERVER.format(md5ext), path.join(temp_dir, md5ext))
             for md5ext in assets)
        )
        for r in result:
            print(r)
        # pool.close()
        # pool.join()
        input(temp_dir)


def download_file(args):
    """Downloads url and saves to file_path"""
    url, file_path = args
    # print(url)
    resp = requests.get(url)
    with open(file_path, 'wb') as file:
        file.write(resp.content)
    return url


def asset_list(sb3_json):
    """Gets a list of assets to download"""
    assets = set()
    for sprite in sb3_json['targets']:
        # Get a list of costume md5exts
        for costume in sprite['costumes']:
            if sanitizer.valid_md5ext(costume['md5ext']):
                assets.add(costume['md5ext'])
            else:
                logging.error("Invalid costume md5ext '%s'", costume['md5ext'])

        for sound in sprite['sounds']:
            if sanitizer.valid_md5ext(sound['md5ext']):
                assets.add(sound['md5ext'])
            else:
                logging.error("Invalid sound md5ext '%s'", sound['md5ext'])
    return assets


if __name__ == '__main__':
    download2("339207237", "test.zip")
