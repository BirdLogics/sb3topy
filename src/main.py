"""


This module's job is to run the unpacker and parser together.
"""

import argparse
import json
import logging
import os
import shutil
import zipfile
from os import path

import sbparser
import unpacker

CONFIG = {
    "temp_folder": "./temp/",
    "specmap_file": "./data/specmap2.txt",
    "project_path": "../examples/Taco2.sb3.zip",

    "zip_path": "",
    "zip_overwrite": True,
    "zip_compression": "DEFLATED",
    "zip_compression_level": -1,

    "no_code": False,

    "debug_json": True,
    "debug_manifest": True,
    "log_level": 20
}

COMPRESS_MAP = {
    "STORED": zipfile.ZIP_STORED,
    "DEFLATED": zipfile.ZIP_DEFLATED,
    "BZIP2": zipfile.ZIP_BZIP2,
    "LZMA": zipfile.ZIP_LZMA
}

ARGS = None  # ["-c", "data/config.json",
#         "C:/Users/username/OneDrive/Documents/GitHub/sb3topy/examples/Beneath a Steel Sky.sb3.zip"]


def main(args=None):
    """Main function"""
    parse_args(args)

    logging.basicConfig(
        format="[%(levelname)s] %(message)s", level=CONFIG['log_level'])

    # Create an assets folder
    assets_dir = path.join(CONFIG['temp_folder'], "assets")
    if not path.isdir(assets_dir):
        os.mkdir(assets_dir)

    # Extract assets, read json
    sb3, manifest = unpacker.unpack(CONFIG)

    if not sb3:
        logging.critical("Failed to unpack sb3 file.")

    if CONFIG['debug_json']:
        logging.info("Saving parsed json")
        with open(path.join(CONFIG['temp_folder'], "project.json"), 'w') as file:
            json.dump(sb3, file)

    if CONFIG['debug_manifest']:
        logging.info("Saving asset manifest")
        with open(path.join(CONFIG['temp_folder'], "manifest.json"), 'w') as file:
            json.dump(manifest, file)

    if CONFIG['no_code']:
        return

    # Parse the sb3 json into python code
    logging.info("Parsing to Python")
    code = sbparser.parse(sb3, CONFIG)

    # Save the results
    logging.info("Saving converted code")
    project_path = path.join(CONFIG['temp_folder'], "project.py")
    with open(project_path, 'w') as file:
        file.write(code)

    # Format with autopep
    # logging.info("Formatting code...")
    # os.system("python3 -m autopep8 --in-place \"" + project_path + '"')

    # Copy engine files
    logging.info("Copying engine files")
    shutil.copyfile("engine.py", path.join(CONFIG['temp_folder'], "engine.py"))

    if CONFIG['zip_create']:
        logging.info("Creating zip file")
        zip_result(manifest)

    print("Done!")

    os.chdir(CONFIG['temp_folder'])
    os.system("py -3 project.py")


def zip_result(manifest):
    """Put the results in a zip file"""
    if not CONFIG['zip_overwrite'] and path.isfile(CONFIG['zip_path']):
        logging.error("ZIP file already exists '%s'")
        raise FileExistsError()

    compression = COMPRESS_MAP.get(
        'zip_compression', CONFIG['zip_compression'])

    with zipfile.ZipFile(CONFIG['zip_path'], 'w', compression,
                         compresslevel=CONFIG['zip_level']) as zfile:
        for name in manifest['assets']:
            zfile.write(path.join(CONFIG['temp_folder'], name), "assets/"+name)

        for name in manifest['scripts']:
            zfile.write(path.join(CONFIG['temp_folder'], name), name)


def exe_result(_):
    """Put the results in a exe file"""
    logging.error("EXE conversion not implemented.")


def parse_args(args=None):
    """Read arguments into CONFIG"""
    parser = argparse.ArgumentParser(
        prog="sb3topy",
        description="Converts sb3 files to Python.",
        epilog="Additional options can be set using a config file."
    )

    parser.add_argument(
        "project", help="path to the .sb3 project", nargs='?')
    parser.add_argument(
        "folder", help="specify a workspace folder", nargs='?')
    parser.add_argument("-c", dest="config_path",
                        metavar="file", help="path to a config json")
    parser.add_argument("-z", nargs="?", const=True, default=None,
                        dest="zip_path", metavar="path", help="save result to a zipfile")
    parser.add_argument("-o", action="store_true", dest="no_code",
                        help="only extract assets; don't modify code")
    parser.add_argument("-w", action="store_true", dest="overwrite",
                        help="enable overwriting of zip/exe files")
    parser.add_argument("-v", action="store_true", dest="verbose",
                        help="show debug output")

    args = parser.parse_args(args)

    if args.config_path:
        load_config(args.config_path)
    if args.folder:
        CONFIG['temp_folder'] = args.folder
    if args.zip_path:
        CONFIG["zip_create"] = True
    if isinstance(args.zip_path, str):
        CONFIG["zip_path"] = args.zip_path
    if args.no_code:
        CONFIG["no_code"] = True
    if args.overwrite:
        CONFIG["zip_overwrite"] = True
    if args.verbose:
        CONFIG["log_level"] = 0
    if args.project is not None:
        CONFIG["project_path"] = args.project


def load_config(config_path):
    """Load a configuration into CONFIG"""
    with open(config_path, 'r') as file:
        CONFIG.update(json.load(file))


if __name__ == "__main__":
    main(ARGS)
