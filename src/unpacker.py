"""
unpacker.py


This module's job is to unpack .sb3 files, to verify
that they actually are sb3 files, to verify the
integrity of imported assets, and to convert
unsupported assets to a supported format.
"""

import json
import logging
import subprocess
import zipfile
from hashlib import md5
from os import path

CONFIG_PATH = "data/config.json"
CONFIG = {
    "project_path": "../examples/The Taco Incident_ Remake.sb3",
    "temp_folder": "temp",

    "svg_convert_cmd": '"C:/Program Files/Inkscape/bin/inkscape.exe" -l -o "{OUTPUT}" "{INPUT}"',
    "mp3_convert_cmd": '"C:/Program Files (x86)/VideoLAN/VLC/vlc.exe" -I dummy --sout "#transcode{{acodec=s16l,channels=2}}:std{{access=file,mux=wav,dst=\'{OUTPUT}\'}}" "{INPUT}" vlc://quit',

    "base_dpi": 96,
    "svg_scale": 4
}

IMAGE_TYPES = ('png', 'svg', 'jpg')
SOUND_TYPES = ('wav', 'mp3')
LOG_LEVEL = 10


class Project:
    """
    Handles unpacking the sb3 project.

    manifest - A list of extracted assets [(name, dir_path), ...]
    json - The potentially modified project json
    namelist - A list of files in the project zipfile

    _zip - Internally used to share the zipfile during unpack
    """

    def __init__(self):
        self.manifest = []
        self.json = None
        self._zip = None
        self.namelist = ()
        self.extracted = {}

    def unpack(self, project_path, assets_path):
        """
        Run the module.
        Returns json, manifest
        """
        with zipfile.ZipFile(project_path, 'r') as project_zip:
            self._zip = project_zip
            self.namelist = project_zip.namelist()

            # Verify project.json exists
            if "project.json" not in self.namelist:
                logging.error("File '%s' does not contain 'project.json'")
                return None, None

            # Load the json
            with project_zip.open("project.json", 'r') as project_json:
                self.json = json.load(project_json)

            # Verify the project is an sb3 file and not sb2
            if not self.json.get("meta") and self.json.get("info"):
                logging.error("File '%s' is in the sb2 format; please try the sb3 format instead.",
                              project_path)
                return None, None

            # Extract the assets
            for target in self.json.setdefault('targets', []):
                for costume in target.setdefault('costumes', []):
                    self.extract_costume(costume, assets_path)

                for sound in target.setdefault('sounds', []):
                    self.extract_sound(sound, assets_path)

        return self.json, {"assets": self.manifest}

    def extract_costume(self, costume, assets_dir):
        """
        Extracts a costume from the zip and converts it from
        svg to png if neccesary.

        To prevent a command injection attack during svg conversion,
        the asset details must be strictly validated. The dataFormat
        must be a known value and the assetId must match the md5 hash
        of the file. This also prevents path traversal.
        """

        costume.setdefault('md5ext', costume['assetId'] + '.' + costume['dataFormat'])
        logging.debug("Validating costume %s", costume['md5ext'])

        # Avoid validating twice
        if costume.setdefault('assetId') in self.extracted:
            costume.update(self.extracted[costume['assetId']])
            return

        # Verify the asset's type is known
        if not costume.setdefault('dataFormat') in IMAGE_TYPES:
            logging.warning("Unkown image type '%s'",
                            costume['dataFormat'])
            asset_path = None
        else:
            # Validate the md5 and extract the asset
            asset_path = self.extract_asset(
                costume['assetId'], costume['dataFormat'], assets_dir)

        # Use a fallback costume if neccesary
        if not asset_path:
            asset_path = self.fallback_costume(costume)

        # If the asset is an svg, convert it
        elif costume['dataFormat'] == 'svg':
            # Check if the file has been converted before
            new_path = path.join(assets_dir, costume['assetId'] + ".png")

            # costume['bitmapResolution'] = CONFIG['svg_scale']
            # costume['rotationCenterX'] *= CONFIG['svg_scale']
            # costume['rotationCenterY'] *= CONFIG['svg_scale']

            if not path.isfile(new_path):
                logging.info("Converting costume '%s' to png",
                             costume['md5ext'])

                # Get the conversion command
                cmd = CONFIG['svg_convert_cmd'].format(
                    INPUT=path.normpath(asset_path),
                    OUTPUT=path.normpath(new_path),
                )  # DPI=CONFIG['base_dpi']*CONFIG['svg_scale'])
                logging.debug("Converting costume: %s", cmd)

                # Run the command
                try:
                    subprocess.run(cmd, check=True,
                                   capture_output=True, text=True)
                except subprocess.CalledProcessError as error:
                    logging.error("SVG conversion error: %s",
                                  error.stderr.rstrip())
                    raise
                if not path.isfile(new_path):
                    logging.error("Failed to convert file '%s'",
                                  costume['md5ext'])
            else:
                logging.info("Asset '%s' already converted to png",
                             costume['md5ext'])

            # Update asset details
            asset_path = new_path
            costume['dataFormat'] = 'png'

        # Update the md5ext
        costume['md5ext'] = costume['assetId'] + "." + costume['dataFormat']
        self.manifest.append(asset_path)

        self.extracted[costume['assetId']] = {
            'md5ext': costume['md5ext'],
            'assetId': costume['assetId'],
            'dataFormat': costume['dataFormat']
        }

    def extract_sound(self, sound, assets_dir):
        """
        Extracts a sound from the zip.

        Measures are taken to prevent command injection and
        path traversal. See extract_costume for details.
        """

        logging.debug("Validating sound %s", sound['md5ext'])

        # Avoid validating twice
        if sound.setdefault('assetId') in self.extracted:
            sound.update(self.extracted[sound['assetId']])
            return

        # Verify the asset's type is known
        if not sound.setdefault('dataFormat') in SOUND_TYPES:
            logging.warning("Unkown sound type '%s'",
                            sound['dataFormat'])
            asset_path = None
        else:
            # Validate and extract the asset
            asset_path = self.extract_asset(
                sound['assetId'], sound['dataFormat'], assets_dir)

        # Use a fallback sound if neccesary
        if not asset_path:
            asset_path = self.fallback_sound(sound)

        # If the asset is an mp3, convert it
        elif sound['dataFormat'] == 'mp3':
            new_path = path.join(assets_dir, sound['assetId'] + ".wav")
            if not path.isfile(new_path):
                logging.info("Converting sound '%s' to wav", sound['md5ext'])

                # Get the conversion command
                cmd = CONFIG['mp3_convert_cmd'].format(
                    INPUT=path.normpath(asset_path),
                    OUTPUT=path.normpath(new_path))
                logging.debug("Converting sound: %s", cmd)

                # Run the command
                try:
                    done = subprocess.run(cmd, check=True,
                                          capture_output=True, text=True)
                except subprocess.CalledProcessError as error:
                    logging.error("MP3 conversion error:\n%s",
                                  error.stderr.rsrtrip())
                    raise
                if not path.isfile(new_path):
                    logging.error("Failed to convert file '%s'",
                                  sound['md5ext'])
            else:
                logging.debug(
                    "Asset '%s' already converted to wav", sound['md5ext'])

            # Update asset details
            asset_path = new_path
            sound['dataFormat'] = 'wav'

        # Update the md5ext
        sound['md5ext'] = sound['assetId'] + "." + sound['dataFormat']
        self.manifest.append((asset_path, "assets"))

        self.extracted[sound['assetId']] = {
            'md5ext': sound['md5ext'],
            'assetId': sound['assetId'],
            'dataFormat': sound['dataFormat']
        }

    def extract_asset(self, asset_md5, asset_ext, assets_path):
        """
        Extracts an asset to asset_path, verifies the asset md5,
        and returns the extraction path.

        The asset_ext should be verified to prevent path traversal.
        """

        md5ext = asset_md5 + "." + asset_ext

        if not md5ext in self.namelist:
            logging.error("Failed to locate asset '%s'", md5ext)
            return None

        # The assetId must be a valid, matching md5
        data = self._zip.read(md5ext)
        if md5(data).hexdigest() != asset_md5:
            logging.error("Detail verification failed for asset '%s'", md5ext)
            return None

        asset_path = path.join(assets_path, md5ext)
        if path.isfile(asset_path):
            return asset_path

        # Extract the asset
        logging.debug("Extracting asset '%s'", md5ext)
        self._zip.extract(md5ext, assets_path)
        return asset_path

    def fallback_costume(self, costume):
        """Replace costume with a blank"""
        raise NotImplementedError("Fallback costumes not yet supported")

    def fallback_sound(self, sound):
        """Replace sound with a blank"""
        raise NotImplementedError("Fallback sounds not yet supported")


def main():
    """Setup the Unpacker and run it"""
    logging.basicConfig(format="[%(levelname)s] %(message)s", level=LOG_LEVEL)

    if path.isfile(CONFIG_PATH):
        with open(CONFIG_PATH, 'r') as file:
            CONFIG.update(json.load(file))

    sb3, _ = unpack({})


def unpack(config):
    """Unpack using a config json"""
    CONFIG.update(config)

    return Project().unpack(
        CONFIG['project_path'],
        path.join(CONFIG['temp_folder'], "assets")
    )


if __name__ == "__main__":
    main()
