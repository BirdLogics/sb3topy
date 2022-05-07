"""
convert_svg.py

Handles svg conversion.
"""

import logging
import shlex
import shutil
import subprocess
from os import path

from .. import config

logger = logging.getLogger(__name__)


def get_svg_function():
    """
    Attempts find a way to convert SVG files. If USE_SVG_CMD is
    enabled, either the command will be used or nothing.

    Returns `None` if no conversion method could be found.
    """

    # If the command is enabled, try to use it
    if config.USE_SVG_CMD:
        func = _convert_svg_cmd()
        if func is not None:
            return func
        logger.warning(
            "Attempting to import cairosvg for SVG support.")

    # Try to use pyvips
    # func = _convert_svg_pyvips()
    # if func is not None:
    #     return func

    # Try to use cairosvg
    func = _convert_svg_cairo()
    if func is not None:
        return func

    logger.error((
        "SVG conversion is enabled but cairosvg does not "
        "appear to be installed. Consider configuring "
        "Inkscape under Asset settings in the GUI."
    ))

    # Failed
    return None


def uses_workers(use_workers):
    """
    Decorator used to mark whether a function is thread safe.
    """
    def decorator(func):
        func.use_workers = use_workers
        return func
    return decorator


def _convert_svg_cairo():
    """
    Attempts to import cairosvg and return a function
    which uses cairosvg to convert an SVG to a PNG.
    """
    try:
        import cairosvg
    except ImportError:
        return None
    except OSError:
        logger.warning("Package cairosvg is not installed correctly.")
        return None

    @uses_workers(False)
    def convert_svg(svg_path, output_dir, md5ext):
        # Get the output path
        filename = f"{md5ext.rpartition('.')[0]}-svg-{config.SVG_SCALE}x.png"
        png_path = path.join(output_dir, filename)

        # Verify the file hasn't already been converted
        if not config.RECONVERT_IMAGES and path.isfile(png_path):
            logger.debug(
                "Skipping conversion of %s, already converted.", md5ext)
            return filename

        logger.debug("Converting %s to PNG using a cariosvg.", md5ext)

        # Convert the svg
        try:
            cairosvg.svg2png(url=svg_path, write_to=png_path,
                             scale=config.SVG_SCALE)

        # Handle an unexpected error
        except ValueError:
            logger.exception(
                "Failed to convert SVG %s with cairosvg:", md5ext)

            return None
        return filename

    return convert_svg


def _convert_svg_pyvips():
    """
    Attempts to import cairosvg and return a function
    which uses cairosvg to convert an SVG to a PNG.
    """
    try:
        import pyvips
    except ImportError:
        return None
    except OSError:
        logger.warning("Package pyvips is not installed correctly.")
        return None

    @uses_workers(True)
    def convert_svg(svg_path, output_dir, md5ext):
        # Get the output path
        filename = f"{md5ext.rpartition('.')[0]}-svg-{config.SVG_SCALE}x.png"
        png_path = path.join(output_dir, filename)

        # Verify the file hasn't already been converted
        if not config.RECONVERT_IMAGES and path.isfile(png_path):
            logger.debug(
                "Skipping conversion of %s, already converted.", md5ext)
            return filename

        logger.debug("Converting %s to PNG using a pyvips.", md5ext)

        # Convert the SVG
        pyvips.Image.svgload(
            svg_path, memory=True, scale=config.SVG_SCALE
        ).pngsave(png_path)

        return filename
    return convert_svg


def _convert_svg_cmd():
    """
    Attempts to verify that the SVG_COMMAND is valid and returns the
    function which uses the command to convert an SVG to a PNG.
    """
    # Verify the command exists
    prog = shlex.split(config.SVG_COMMAND)[0]
    if shutil.which(prog) is None:
        logger.error((
            "SVG conversion with a command is enabled "
            "but '%s' does not appear to be installed."),
            prog
        )
        return None
    return convert_svg_cmd


@uses_workers(True)
def convert_svg_cmd(svg_path, output_dir, md5ext):
    """
    Converts the svg using the configured command. The md5ext is
    used for logging purposes.
    """
    # Get the output path
    filename = f"{md5ext.rpartition('.')[0]}-svg-{config.SVG_SCALE}x.png"
    png_path = path.join(output_dir, filename)

    # Verify the file hasn't already been converted
    if not config.RECONVERT_IMAGES and path.isfile(png_path):
        logger.debug(
            "Skipping conversion of %s, already converted.", md5ext)
        return filename

    logger.debug("Converting %s to PNG using a command.", md5ext)

    # Get the conversion command
    cmd_str = config.SVG_COMMAND.format(
        INPUT=shlex.quote(svg_path),
        OUTPUT=shlex.quote(png_path),
        DPI=config.BASE_DPI*config.SVG_SCALE,
        SCALE=config.SVG_SCALE
    )

    # Attempt to run the command
    try:
        print(repr(config.CONVERT_TIMEOUT))
        result = subprocess.run(shlex.split(cmd_str), check=True, capture_output=True,
                                text=True, timeout=config.CONVERT_TIMEOUT)

    # Command gave an error
    except subprocess.CalledProcessError as error:
        logger.error("Failed to convert svg '%s':\n%s\n%s\n",
                     md5ext, cmd_str, error.stderr.rstrip())
        return None

    # Command timed out
    except subprocess.TimeoutExpired:
        logger.error(
            "Failed to convert svg %s: Timeout expired.", md5ext)
        return None

    # Verify the command created a file
    if not path.isfile(png_path):
        logger.error("Failed to save svg %s:\n%s\n%s\n",
                     md5ext, cmd_str, result.stderr.rstrip())
        return None
    return filename


@uses_workers(True)
def fallback_image(_svg_path, output_dir, md5ext):
    """Save a blank PNG image instead of converting."""
    logger.debug("Saving fallback PNG for %s.", md5ext)

    # Get the output filename
    filename = f"{md5ext.rpartition('.')[0]}-fallback.png"
    png_path = path.join(output_dir, filename)

    # Save the fallback image
    with open(png_path, 'wb') as image_file:
        image_file.write(config.FALLBACK_IMAGE)

    return filename
