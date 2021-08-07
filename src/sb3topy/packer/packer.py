"""
packer.py

Handles several tasks specific to saving files
"""

import logging
import shutil
import os
from os import path
import sys

from . import config
from ..project import Project

__all__ = ('save_code', 'copy_engine', 'run_project')


def save_code(project: Project, code: str):
    """
    Saves the codefile into project's directory
    """
    save_path = path.join(project.output_dir, "project.py")

    logging.info("Saving converted project to '%s'", save_path)

    with open(save_path, 'w', encoding="utf-8", errors="ignore") as code_file:
        code_file.write(code)


def copy_engine(project: Project):
    """
    Copys the engine files into the project's directory

    If the engine files already exist, they will
    """

    # Get the path to copy from and to
    read_dir = path.join(path.dirname(__file__), "..", "engine")
    save_dir = path.join(project.output_dir, "engine")

    if path.isfile(path.join(save_dir, "DISABLE_OVERWRITE")):
        logging.info(
            "Did not copy engine files; 'DISABLE_OVERWRITE' file exists.")
        return

    # Delete and copy the engine files
    if path.isdir(save_dir):
        if config.OVERWRITE_ENGINE:
            logging.info("Overwriting engine files at '%s'", save_dir)
            shutil.rmtree(save_dir)
            shutil.copytree(read_dir, save_dir, )
        else:
            logging.info(
                "Did not copy engine files; OVERWRITE_ENGINE disabled.")
    else:
        logging.info("Copying engine files to '%s'", save_dir)
        shutil.copytree(read_dir, save_dir)

    # Create a warning message
    warn_path = path.join(save_dir, "WARNING.txt")
    with open(warn_path, 'w') as warn_file:
        warn_file.write((
            "The files in this directory will be deleted if the sb3topy "
            "converter is run again. All additional files and changes to "
            "existing files will be lost. If you want to prevent this from "
            "happening, set OVERWRITE_ENGINE to False in the configuration. "
            "Alternatively, you can create a file name 'DISABLE_OVERWRITE'"
            "to disable modifying these files.\n"
        ))


def run_project(output_dir):
    """
    Runs the project.py stored in output_dir.
    """
    # pylint: disable=all
    logging.info("Running project...")

    old_cwd = os.getcwd()
    os.chdir(output_dir)

    sys.path.insert(1, output_dir)
    import project  # type:ignore

    project.engine.start_program()

    sys.path.pop(1)
    os.chdir(old_cwd)
