"""
convert.py


"""

import logging
import shlex
import subprocess
from multiprocessing.pool import ThreadPool
from os import path

from .. import config
from ..project import Project

__all__ = ('convert_assets', 'Convert')


def convert_assets(project: Project):
    """
    Converts all assets in project to a supported format
    """
    logging.info("Converting project assets...")
    Convert(project)


class Convert:
    """Converts all assets in project to a supported format"""

    def __init__(self, project: Project):
        self.project = project

        # Convert assets
        pool = ThreadPool()
        results = pool.imap_unordered(self.convert_asset, self.assets_iter())
        for sucesss, msg in results:
            if sucesss:
                logging.debug(msg)
            else:
                logging.error(msg)
        pool.close()
        pool.join()

    def assets_iter(self):
        """
        Iterates through project.assets and yields assets
        which need to be converted. Logs when each item is consumed.
        """
        for md5ext in self.project.assets:
            ext = md5ext.partition('.')[-1]

            if ext == 'mp3':
                logging.debug("Converting sound '%s' to wav", md5ext)
                yield md5ext

            elif ext == 'svg':
                logging.debug("Converting image '%s' to png", md5ext)
                yield md5ext

            elif ext not in ('png', 'bmp', 'jpg', 'jpeg', 'wav'):
                logging.warning("Unrecognized asset type '%s'", ext)

    def convert_asset(self, md5ext):
        """Converts an asset and saves it to the output folder
        based on a md5ext. The md5ext must be validated.

        Returns a success bool and a message to be logged.

        mp3 files are converted to wav
        svg files are converted to png

        Intended for use in a Pool.
        """
        ext = md5ext.partition('.')[-1]

        if ext == 'mp3' and config.CONVERT_MP3:
            return self.convert_mp3(md5ext)

        if ext == 'svg':
            return self.convert_svg(md5ext)

    def convert_mp3(self, md5ext):
        """Converts an mp3 asset to wav"""
        # Get the input and output paths
        asset_path = path.join(self.project.output_dir, md5ext)
        save_path = path.join(self.project.output_dir,
                              md5ext.rstrip('.mp3') + '-mp3.wav')

        # Possibly don't reconvert the asset
        if path.isfile(save_path) and not config.RECONVERT_SOUNDS:
            return True, f"Skipping conversion of mp3 '{md5ext}' (already converted)"

        # Get the conversion command
        cmd = shlex.split(config.MP3_COMMAND.format(
            INPUT=shlex.quote(asset_path),
            OUTPUT=shlex.quote(save_path),
            VLC_PATH=config.VLC_PATH
        ))

        # Attempt to run the command
        try:
            subprocess.run(cmd, check=True, capture_output=True, text=True)
        except subprocess.CalledProcessError as error:
            return False, f"Error when converting mp3 '{md5ext}':" + \
                f"\n{cmd}\n{error.stderr.rstrip()}"

        return True, f"Converted sound '{md5ext}' to wav"

    def convert_svg(self, md5ext):
        """Converts an svg asset to png"""
        # Get the input and output paths
        asset_path = path.join(self.project.output_dir, md5ext)
        save_path = path.join(self.project.output_dir,
                              md5ext.rstrip('.svg') + '-svg.png')

        # Possibly don't reconvert the asset
        if path.isfile(save_path) and not config.RECONVERT_IMAGES:
            return True, f"Skipping conversion of svg '{md5ext}' (already converted)"

        # Some blank svg files fail to convert with cariosvg
        # Use a fallback pre-converted png image instead
        if md5ext in config.BLANK_SVG_HASHES:
            self.fallback_image(save_path)
            return True, f"Used fallback image for blank svg '{md5ext}'"

        # Get the conversion command
        cmd = shlex.split(config.SVG_COMMAND.format(
            INPUT=shlex.quote(asset_path),
            OUTPUT=shlex.quote(save_path),
            INKSCAPE_PATH=config.INKSCAPE_PATH
        ))

        # Attempt to run the command
        try:
            subprocess.run(cmd, check=True, text=True, capture_output=True)
        except subprocess.CalledProcessError as error:
            return False, f"Error when converting svg '{md5ext}':" + \
                f"\n{cmd}\n{error.stderr.rstrip()}"

        return True, f"Converted image '{md5ext}' to png"

    @staticmethod
    def fallback_image(save_path):
        """Saves a fallback image to save path"""
        with open(save_path, 'wb') as image_file:
            image_file.write(config.FALLBACK_IMAGE)
