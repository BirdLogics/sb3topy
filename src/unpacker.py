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

OPTIONS = {
    "project_path": "results/The Taco Incident_ Remake.sb3",
    "svg_convert_cmd": '"C:/Program Files/Inkscape/bin/inkscape.exe" -o {OUTPUT} {INPUT}',
    "mp3_convert_cmd": '"C:/Program Files (x86)/VideoLAN/VLC/vlc.exe" -I dummy --sout "#transcode{{acodec=s16l,channels=2}}:std{{access=file,mux=wav,dst={OUTPUT}}}" {INPUT} vlc://quit',
    "output_folder": "results",
    "assets_path": "results/assets/",
    "debug_json": "results/project.json"
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

    def unpack(self):
        """
        Run the module.
        Returns json, manifest
        """
        with zipfile.ZipFile(OPTIONS['project_path'], 'r') as project_zip:
            self._zip = project_zip
            self.namelist = project_zip.namelist()

            # Verify project.json exists
            if "project.json" not in self.namelist:
                logging.error("File '%s' does not contain 'project.json'")
                return None

            # Load the json
            with project_zip.open("project.json", 'r') as project_json:
                self.json = json.load(project_json)

            # Verify the project is an sb3 file and not sb2
            if not self.json.get("meta") and self.json.get("info"):
                logging.error("File '%s' is in the sb2 format; please try the sb3 format instead.",
                              OPTIONS['project_path'])
                return None

            # Load the assets
            for target in self.json.setdefault('targets', []):
                for costume in target.setdefault('costumes', []):
                    self.extract_costume(costume)

                for sound in target.setdefault('sounds', []):
                    self.extract_sound(sound)

        return self.json, self.manifest

    def extract_costume(self, costume):
        """
        Extracts a costume from the zip and converts it from
        svg to png if neccesary.

        To prevent a command injection attack during svg conversion,
        the asset details must be strictly validated. The dataFormat
        must be a known value and the assetId must match the md5 hash
        of the file. This also prevents path traversal.
        """

        # logging.debug("Extracting costume %s", costume['md5ext'])

        # if path.isfile(OPTIONS['assets_path'] + costume.get('md5ext', '')):
        #     if

        # Verify the asset's type is known
        if not costume.setdefault('dataFormat') in IMAGE_TYPES:
            logging.warning("Unkown image type '%s'",
                            costume['dataFormat'])
            asset_path = None
        else:
            # Validate and extract the asset
            asset_path = self.extract_asset(
                costume['assetId'], costume['dataFormat'])

        # Use a fallback costume if neccesary
        if not asset_path:
            asset_path = self.fallback_costume(costume)

        # If the asset is an svg, convert it
        elif costume['dataFormat'] == 'svg':
            logging.info("Converting asset '%s' to png", costume['assetId'])
            output_path = OPTIONS['assets_path'] + costume['assetId'] + ".png"
            if not path.isfile(output_path):
                try:
                    subprocess.run(
                        OPTIONS['svg_convert_cmd'].format(
                            INPUT=asset_path,
                            OUTPUT=output_path
                        ), check=True, capture_output=True, shell=False
                    )
                except subprocess.CalledProcessError as error:
                    logging.error("SVG conversion error: %s", error.stderr)
                    raise
            asset_path = OPTIONS['assets_path'] + costume['assetId'] + ".png"
            costume['dataFormat'] = 'png'

        # Update the md5ext
        costume['md5ext'] = costume['assetId'] + "." + costume['dataFormat']
        self.manifest.append((path, "assets"))

    def extract_sound(self, sound):
        """Extracts a sound from the zip."""

        # Verify the asset's type is known
        if not sound.setdefault('dataFormat') in SOUND_TYPES:
            logging.warning("Unkown sound type '%s'",
                            sound['dataFormat'])
            asset_path = None
        else:
            # Validate and extract the asset
            asset_path = self.extract_asset(
                sound['assetId'], sound['dataFormat'])

        # Use a fallback sound if neccesary
        if not asset_path:
            asset_path = self.fallback_sound(sound)

        elif sound['dataFormat'] == 'mp3':
            logging.info("Converting sound '%s' to wav", sound['assetId'])
            output_path = OPTIONS['assets_path'] + sound['assetId'] + ".wav"
            if not path.isfile(output_path):
                try:
                    subprocess.run(
                        OPTIONS['mp3_convert_cmd'].format(
                            INPUT=asset_path,
                            OUTPUT=output_path
                        ), check=True, capture_output=True, shell=False
                    )
                except subprocess.CalledProcessError as error:
                    logging.error("MP3 conversion error: %s", error.stderr)
                    raise
            asset_path = OPTIONS['assets_path'] + sound['assetId'] + ".wav"
            sound['dataFormat'] = 'wav'

        # Update the md5ext
        sound['md5ext'] = sound['assetId'] + "." + sound['dataFormat']
        self.manifest.append((asset_path, "assets"))

    def extract_asset(self, asset_md5, asset_ext):
        """
        Extracts an asset to asset_path, verifies the asset md5,
        and returns the extraction path.

        The asset_ext should be verified to prevent path traversal.
        """

        md5ext = asset_md5 + "." + asset_ext
        logging.debug("Extracting asset '%s'", md5ext)

        if not md5ext in self.namelist:
            logging.error("Failed to locate asset '%s'", md5ext)
            return None

        # The assetId must be a valid, matching md5
        data = self._zip.read(md5ext)
        if md5(data).hexdigest() != asset_md5:
            logging.error("Detail verification failed for asset '%s'", md5ext)
            return None

        # Extract the asset
        return self._zip.extract(md5ext, OPTIONS['assets_path'])

    def fallback_costume(self, costume):
        """Replace costume with a blank"""
        raise NotImplementedError("Fallback costumes not yet supported")

    def fallback_sound(self, sound):
        """Replace sound with a blank"""
        raise NotImplementedError("Fallback sounds not yet supported")


def main():
    """Setup the Unpacker and run it"""
    logging.basicConfig(format="[%(levelname)s] %(message)s", level=LOG_LEVEL)
    sb3, _ = Project().unpack()

    if OPTIONS['debug_json']:
        with open(OPTIONS['debug_json'], 'w') as file:
            json.dump(sb3, file)


if __name__ == "__main__":
    main()
