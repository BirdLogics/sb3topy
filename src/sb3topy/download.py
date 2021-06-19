"""
download.py

Downloads projects from the internet
"""

from zipfile import ZipFile

import requests

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


def asset_list(sb3_json):
    """Gets a list of assets to download"""
    assets = set()
    for sprite in sb3_json['targets']:
        for costume in sprite['costumes']:
            assets.add(costume['md5ext'])
        for sound in sprite['sounds']:
            assets.add(sound['md5ext'])
    return assets


if __name__ == '__main__':
    download("312305395", "test.zip")
