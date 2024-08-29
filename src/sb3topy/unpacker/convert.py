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







TODO Better fallback support.
"""

import logging
import shlex
import shutil
import subprocess
from multiprocessing import pool
from os import path

from .. import config, project
from . import convert_svg

__all__ = ('convert_assets', 'Convert')

logger = logging.getLogger(__name__)


def convert_assets(manifest: project.Manifest):
    """
    Converts all assets in project to a supported format
    """
    logger.info("Converting project assets...")
    Convert(manifest)


class Convert:
    """Converts all assets in project to a supported format"""

    def __init__(self, manifest: project.Manifest):
        self.output_dir = manifest.output_dir

        workers = pool.ThreadPool(config.CONVERT_THREADS)
        logger.debug("Created %i worker threads for asset conversion.",
                     config.CONVERT_THREADS)

        # Treat a timeout of 0 as no timeout
        if config.CONVERT_TIMEOUT == 0 or isinstance(config.CONVERT_TIMEOUT, str):
            config.CONVERT_TIMEOUT = None

        # Get an SVG conversion function
        self.convert_svg_func = None
        if config.CONVERT_COSTUMES:
            self.convert_svg_func = convert_svg.get_svg_function()

        # Convert the SVGs
        if self.convert_svg_func:
            if self.convert_svg_func.use_workers:
                # Convert using multiple threads
                manifest.costumes.update(workers.imap_unordered(
                    self.convert_costume, manifest.costumes.keys()))
            else:
                # Convert using a single thread
                manifest.costumes.update(map(
                    self.convert_costume, manifest.costumes.keys()))
        else:
            logger.warning((
                "Costume conversion is disabled. "
                "Pygame SVG support will be used instead. "
                "Pygame does not have support for adjusting the DPI "
                "of images, so SVGs will be a bit blurry."
            ))

        # Convert all sounds
        if config.CONVERT_SOUNDS:
            # Verify the conversion method is available
            command = shlex.split(config.MP3_COMMAND)
            if shutil.which(command[0]) is None:
                logger.error((
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

    def convert_costume(self, md5ext):
        """
        At this point, the costume has been saved to the output folder
        using the md5ext as the filename.

        If the md5ext indicates that the image is an SVG, attempt to
        convert it.

        The new filename after conversion will be returned.
        """
        # Default to no change in the filename
        new_md5ext = md5ext

        # Get the file extension
        ext = md5ext.rpartition('.')[2]

        # Convert SVG assets
        if ext == "svg":
            new_md5ext = self.convert_svg(md5ext)

        # If the output file doesn't exist, use a fallback
        if not path.isfile(path.join(self.output_dir, "assets", new_md5ext)):
            logger.warning("Failed to locate %s after conversion.",
                           new_md5ext)

            new_md5ext = convert_svg.fallback_image(
                "", self.output_dir, md5ext)

        return md5ext, new_md5ext

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
            logger.debug(
                "Skipping conversion of mp3 '%s' (already converted)", md5ext)
            return new_md5ext

        # Get the conversion command
        cmd_str = config.MP3_COMMAND.format(
            INPUT=shlex.quote(asset_path),
            OUTPUT=shlex.quote(save_path)
        )

        # Attempt to run the command
        try:
            logger.debug("Converting mp3 '%s' to wav", md5ext)
            result = subprocess.run(shlex.split(cmd_str), check=True, capture_output=True,
                                    text=True, timeout=config.CONVERT_TIMEOUT)

        except subprocess.CalledProcessError as error:
            logger.error("Failed to convert mp3 '%s':\n%s\n%s\n",
                         md5ext, cmd_str, error.stderr.rstrip())
            return md5ext

        except subprocess.TimeoutExpired:
            logger.error(
                "Failed to convert mp3 '%s': Timeout expired.", md5ext)
            return md5ext

        # Verify the converted file exists
        if not path.isfile(save_path):
            logger.error("Failed to convert svg '%s':\n%s\n%s\n",
                         md5ext, cmd_str, result.stderr.rstrip())
            return md5ext

        return new_md5ext

    def convert_svg(self, md5ext):
        """Converts an svg asset to png"""
        # Get the input and output paths
        output_dir = path.join(self.output_dir, "assets")
        svg_path = path.join(output_dir, md5ext)

        # Some blank svg files fail to convert with cairosvg
        # Use a fallback pre-converted png image instead
        if md5ext in config.BLANK_SVG_HASHES:
            logger.debug("Using fallback image for blank svg %s", md5ext)
            return convert_svg.fallback_image("", output_dir, md5ext)

        # Convert the svg with the configured method
        new_md5ext = self.convert_svg_func(svg_path, output_dir, md5ext)

        # Use a fallback image if conversion failed
        if new_md5ext is None:
            return convert_svg.fallback_image("", output_dir, md5ext)
        return new_md5ext
