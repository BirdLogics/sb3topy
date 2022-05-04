"""
packer.py

Handles several tasks specific to saving files
"""

import logging
import os
import shutil
import sys
from os import path

from .. import config, project

__all__ = ('save_code', 'copy_engine', 'run_project')

logger = logging.getLogger(__name__)


def save_code(manifest: project.Manifest, code: str):
    """
    Saves the codefile into project's directory
    """
    save_path = path.join(manifest.output_dir, "project.py")

    logger.info("Saving converted project to '%s'", save_path)

    with open(save_path, 'w', encoding="utf-8", errors="ignore") as code_file:
        code_file.write(code)


def copy_engine(manifest: project.Manifest):
    """
    Copies the engine files into the project's directory

    If the engine files already exist, they will
    """

    # Get the path to copy from and to
    read_dir = path.join(path.dirname(__file__), "..", "..", "engine")
    save_dir = path.join(manifest.output_dir, "engine")

    if path.isfile(path.join(save_dir, "DISABLE_OVERWRITE")):
        logger.info(
            "Did not copy engine files; 'DISABLE_OVERWRITE' file exists.")
        return

    # Delete and copy the engine files
    if path.isdir(save_dir):
        if config.OVERWRITE_ENGINE:
            logger.info("Overwriting engine files at '%s'", save_dir)
            shutil.rmtree(save_dir)
            shutil.copytree(read_dir, save_dir, )
            create_config(save_dir)
        else:
            logger.info(
                "Did not copy engine files; OVERWRITE_ENGINE disabled.")
    else:
        logger.info("Copying engine files to '%s'", save_dir)
        shutil.copytree(read_dir, save_dir)
        create_config(save_dir)

    # Create a warning message
    warn_path = path.join(save_dir, "WARNING.txt")
    with open(warn_path, 'w') as warn_file:
        warn_file.write((
            "The files in this directory will be deleted if the sb3topy "
            "converter is run again. All additional files and changes to "
            "existing files will be lost. If you want to prevent this from "
            "happening, set OVERWRITE_ENGINE to False in the configuration. "
            "Alternatively, you can create a file named 'DISABLE_OVERWRITE'"
            "to disable modifying these files.\n"
        ))


def create_config(engine_dir):
    """Creates a config.py file for the engine"""
    # Read a formatable spec file
    spec_path = path.join(path.dirname(__file__), "config.txt")
    with open(spec_path, 'r') as spec_file:
        spec_data = spec_file.read()

    # Format the spec file into Python code
    config_data = spec_data.format(**config.__dict__)

    # Save the config data
    config_path = path.join(engine_dir, "config.py")
    with open(config_path, 'w') as config_file:
        config_file.write(config_data)


def run_project(output_dir):
    """
    Runs the project.py stored in output_dir.
    """
    # pylint: disable=all
    logger.info("Running project...")

    old_cwd = os.getcwd()
    os.chdir(output_dir)

    sys.path.insert(1, output_dir)
    import project  # type:ignore

    project.engine.start_program()

    sys.path.pop(1)
    os.chdir(old_cwd)
