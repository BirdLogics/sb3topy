"""
convert.py

Handles the conversion of assets from unsupported formats, such as svg
and mp3, to supported formats, such as png and wav.

The conversion is run with multiple threads, each of which calls a
a command in a subprocess to convert the asset.

The conversion is intended to run with Inkscape or cairosvg for svgs
and VLC for mp3s, but other tools which can be run with a command
should work as well.

It is not necesary to convert mp3s to wav when using Pygame 2+, but it
may a good idea since, according to the Pygame docs, mp3 support is
limited and can crash with certain formats on some systems.
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
        pool = ThreadPool(config.CONVERT_THREADS)
        results = pool.imap_unordered(self.convert_asset, self.assets_iter())
        for md5ext, new_md5ext in results:
            project.assets[md5ext] = new_md5ext
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
                yield md5ext

            elif ext == 'svg':
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

        logging.error("Unexpected asset type for '%s'", md5ext)
        return md5ext, None

    def convert_mp3(self, md5ext):
        """Converts an mp3 asset to wav"""
        # Get the new md5ext reflecting the conversion
        new_md5ext = md5ext.rstrip('.mp3') + '-mp3.wav'

        # Get the input and output paths
        asset_path = path.join(self.project.output_dir, "assets", md5ext)
        save_path = path.join(self.project.output_dir, "assets",
                              md5ext.rstrip('.mp3') + '-mp3.wav')

        # Possibly don't reconvert the asset
        if path.isfile(save_path) and not config.RECONVERT_SOUNDS:
            logging.debug(
                "Skipping conversion of mp3 '%s' (already converted)", md5ext)
            return md5ext, new_md5ext

        # Get the conversion command
        cmd = shlex.split(config.MP3_COMMAND.format(
            INPUT=shlex.quote(asset_path),
            OUTPUT=shlex.quote(save_path),
            VLC_PATH=config.VLC_PATH
        ))

        # Attempt to run the command
        try:
            logging.debug("Converting mp3 '%s' to wav", md5ext)
            result = subprocess.run(cmd, check=True, capture_output=True,
                                    text=True, timeout=config.CONVERT_TIMEOUT)
        except subprocess.CalledProcessError as error:
            logging.error("Failed to convert mp3 '%s':\n%s\n%s\n",
                          md5ext, shlex.join(cmd), error.stderr.rstrip())
            return md5ext, None
        except subprocess.TimeoutExpired:
            logging.error(
                "Failed to convert mp3 '%s': Timeout expired.", md5ext)
            return md5ext, None

        # Verify the file exists
        if not path.isfile(save_path):
            logging.error("Failed to convert svg '%s':\n%s\n%s\n",
                          md5ext, shlex.join(cmd), result.stderr.rstrip())
            return md5ext, None

        return md5ext, new_md5ext

    def convert_svg(self, md5ext):
        """Converts an svg asset to png"""
        # Get the new md5ext reflecting the conversion
        new_md5ext = f"{md5ext.rstrip('.svg')}-svg-{config.SVG_SCALE}x.png"

        # Get the input and output paths
        asset_path = path.join(self.project.output_dir, "assets", md5ext)
        save_path = path.join(self.project.output_dir, "assets", new_md5ext)

        # Possibly don't reconvert the asset
        if path.isfile(save_path) and not config.RECONVERT_IMAGES:
            logging.debug(
                "Skipping conversion of svg '%s' (already converted)", md5ext)
            return md5ext, new_md5ext

        # Some blank svg files fail to convert with cariosvg
        # Use a fallback pre-converted png image instead
        if md5ext in config.BLANK_SVG_HASHES:
            self.fallback_image(save_path)
            logging.debug("Used fallback image for blank svg '%s'", md5ext)
            return md5ext, new_md5ext

        # Get the conversion command
        cmd = shlex.split(config.SVG_COMMAND.format(
            INPUT=shlex.quote(asset_path),
            OUTPUT=shlex.quote(save_path),
            DPI=config.BASE_DPI*config.SVG_SCALE,
            SCALE=config.SVG_SCALE,
            INKSCAPE_PATH=config.INKSCAPE_PATH
        ))

        # Attempt to run the command
        try:
            logging.debug("Converting svg '%s' to png", md5ext)
            result = subprocess.run(cmd, check=True, capture_output=True,
                                    text=True, timeout=config.CONVERT_TIMEOUT)
        except subprocess.CalledProcessError as error:
            logging.error("Failed to convert svg '%s':\n%s\n%s\n",
                          md5ext, shlex.join(cmd), error.stderr.rstrip())
            return md5ext, None
        except subprocess.TimeoutExpired:
            logging.error(
                "Failed to convert svg '%s': Timeout expired.", md5ext)
            return md5ext, None

        # Verify the file exists
        if not path.isfile(save_path):
            logging.error("Failed to save svg '%s':\n%s\n%s\n",
                          md5ext, shlex.join(cmd), result.stderr.rstrip())
            return md5ext, None

        return md5ext, new_md5ext

    @staticmethod
    def fallback_image(save_path):
        """Saves a fallback image to save path"""
        with open(save_path, 'wb') as image_file:
            image_file.write(config.FALLBACK_IMAGE)
