"""
convert.py

Handles the conversion of assets from unsupported formats, such as svg
and mp3, to supported formats, such as png and wav.

The conversion is run with multiple threads, each of which calls a
a command in a subprocess to convert the asset.

The conversion is intended to run with Inkscape or cairosvg for svgs
and VLC for mp3s, but other tools which can be run with a command
should work as well.

It is not necessary to convert mp3s to wav when using Pygame 2+, but it
may a good idea since, according to the Pygame docs, mp3 support is
limited and can crash with certain formats on some systems.
"""

import logging
import shlex
import shutil
import subprocess
from multiprocessing import pool
from os import path

from .. import config, project

__all__ = ('convert_assets', 'Convert')


def convert_assets(manifest: project.Manifest):
    """
    Converts all assets in project to a supported format
    """
    logging.info("Converting project assets...")
    Convert(manifest)


class Convert:
    """Converts all assets in project to a supported format"""

    def __init__(self, manifest: project.Manifest):
        self.output_dir = manifest.output_dir

        # Create a pool of workers
        workers = pool.ThreadPool(config.CONVERT_THREADS)

        # Convert all costumes
        if config.CONVERT_COSTUMES:
            # Verify the command is available
            command = shlex.split(config.SVG_COMMAND)
            if shutil.which(command[0]) is None:
                logging.error((
                    "SVG conversion is enabled but '%s' "
                    "does not appear to be installed."),
                    command[0]
                )

            # Convert the sounds
            else:
                manifest.costumes.update(workers.imap_unordered(
                    self.convert_costume, manifest.costumes.items()))
        else:
            logging.warning((
                "Costume conversion is disabled. "
                "Any svgs in the project will prevent it from running."
            ))

        # Convert all sounds
        if config.CONVERT_SOUNDS:
            # Verify the command is available
            command = shlex.split(config.MP3_COMMAND)
            if shutil.which(command[0]) is None:
                logging.error((
                    "MP3 conversion is enabled but '%s' "
                    "does not appear to be installed."),
                    command[0]
                )

            # Convert the sounds
            else:
                manifest.sounds.update(workers.imap_unordered(
                    self.convert_sound, manifest.sounds.items()))

        # Close the pool of workers
        workers.close()
        workers.join()

    def convert_costume(self, md5ext_oldnew):
        """
        Converts a costume and saves it to the output folder. The
        filename is the same as the md5ext unless a problem prevented
        the asset from being extracted or downloaded.
        """
        md5ext, filename = md5ext_oldnew

        # Get the file extension
        ext = filename.rpartition('.')[2] if filename is not None else None

        # Convert SVG assets
        if ext == "svg":
            filename = self.convert_svg(filename)

        # Use a fallback image if necessary
        if filename is None:
            filename = self.fallback_image(md5ext)

        return md5ext, filename

    def convert_sound(self, md5ext_oldnew):
        """
        Converts a sound and saves it to the output folder. The
        filename is the same as the md5ext unless a problem prevented
        the asset from being extracted or downloaded.
        """
        md5ext, filename = md5ext_oldnew

        # Get the file extension
        ext = filename.partition('.')[2] if filename is not None else None

        # Convert MP3 assets
        if ext == "mp3":
            filename = self.convert_mp3(filename)

        # if filename is None:
        #     filename = self.fallback_sound(md5ext)

        return md5ext, filename

    def convert_mp3(self, md5ext):
        """Converts an mp3 asset to wav"""
        # Get the new md5ext reflecting the conversion
        new_md5ext = md5ext.rstrip('.mp3') + '-mp3.wav'

        # Get the input and output paths
        asset_path = path.join(self.output_dir, "assets", md5ext)
        save_path = path.join(self.output_dir, "assets",
                              md5ext.rstrip('.mp3') + '-mp3.wav')

        # Possibly don't reconvert the asset
        if path.isfile(save_path) and not config.RECONVERT_SOUNDS:
            logging.debug(
                "Skipping conversion of mp3 '%s' (already converted)", md5ext)
            return new_md5ext

        # Get the conversion command
        cmd_str = config.MP3_COMMAND.format(
            INPUT=shlex.quote(asset_path),
            OUTPUT=shlex.quote(save_path)
        )

        # Attempt to run the command
        try:
            logging.debug("Converting mp3 '%s' to wav", md5ext)
            result = subprocess.run(shlex.split(cmd_str), check=True, capture_output=True,
                                    text=True, timeout=config.CONVERT_TIMEOUT)

        except subprocess.CalledProcessError as error:
            logging.error("Failed to convert mp3 '%s':\n%s\n%s\n",
                          md5ext, cmd_str, error.stderr.rstrip())
            return md5ext

        except subprocess.TimeoutExpired:
            logging.error(
                "Failed to convert mp3 '%s': Timeout expired.", md5ext)
            return md5ext

        # Verify the converted file exists
        if not path.isfile(save_path):
            logging.error("Failed to convert svg '%s':\n%s\n%s\n",
                          md5ext, cmd_str, result.stderr.rstrip())
            return md5ext

        return new_md5ext

    def convert_svg(self, md5ext):
        """Converts an svg asset to png"""
        # Get the new md5ext reflecting the conversion
        new_md5ext = f"{md5ext.rstrip('.svg')}-svg-{config.SVG_SCALE}x.png"

        # Get the input and output paths
        asset_path = path.join(self.output_dir, "assets", md5ext)
        save_path = path.join(self.output_dir, "assets", new_md5ext)

        # Possibly don't reconvert the asset
        if path.isfile(save_path) and not config.RECONVERT_IMAGES:
            logging.debug(
                "Skipping conversion of svg '%s' (already converted)", md5ext)
            return new_md5ext

        # Some blank svg files fail to convert with cairosvg
        # Use a fallback pre-converted png image instead
        if md5ext in config.BLANK_SVG_HASHES:
            logging.debug("Using fallback image for blank svg '%s'", md5ext)
            return self.fallback_image(md5ext, ".png")

        # Get the conversion command
        cmd_str = config.SVG_COMMAND.format(
            INPUT=shlex.quote(asset_path),
            OUTPUT=shlex.quote(save_path),
            DPI=config.BASE_DPI*config.SVG_SCALE,
            SCALE=config.SVG_SCALE
        )

        # Attempt to run the command
        try:
            logging.debug("Converting svg '%s' to png", md5ext)
            result = subprocess.run(shlex.split(cmd_str), check=True, capture_output=True,
                                    text=True, timeout=config.CONVERT_TIMEOUT)

        except subprocess.CalledProcessError as error:
            logging.error("Failed to convert svg '%s':\n%s\n%s\n",
                          md5ext, cmd_str, error.stderr.rstrip())
            return None

        except subprocess.TimeoutExpired:
            logging.error(
                "Failed to convert svg '%s': Timeout expired.", md5ext)
            return None

        # Verify the file exists
        if not path.isfile(save_path):
            logging.error("Failed to save svg '%s':\n%s\n%s\n",
                          md5ext, cmd_str, result.stderr.rstrip())
            return None

        return new_md5ext

    def fallback_image(self, md5ext, new_ext="-fallback.png"):
        """Saves a fallback image for a md5ext"""
        filename = md5ext.partition('.')[0] + new_ext
        save_path = path.join(self.output_dir, "assets", filename)

        with open(save_path, 'wb') as image_file:
            image_file.write(config.FALLBACK_IMAGE)

        return filename
