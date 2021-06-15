"""
main.py

Run the parser with the settings in config
"""

import json
import logging
import shutil
from os import path

from . import config, parser, unpacker


def main():
    """Handles the module being called from the command line"""
    logging.basicConfig(
        format="[%(levelname)s] %(message)s", level=config.LOG_LEVEL)

    sb3, manifest = unpacker.unpack()

    # json_path = path.join(config.TEMP_FOLDER, "project.json")
    # logging.info("Saving debug json to '%s'", json_path)
    # with open(json_path, 'w') as file:
    #     json.dump(sb3, file)

    # logging.getLogger().setLevel(0)
    code = parser.Parser().parse(sb3)

    save_path = path.join(config.TEMP_FOLDER, "project.py")
    with open(save_path, 'w', encoding="utf-8", errors="ignore") as file:
        file.write(code)
    print(f"Saved to '{save_path}'")

     # Copy engine files
    logging.info("Copying engine files")
    shutil.rmtree(path.join(config.TEMP_FOLDER, "engine"), )
    shutil.copytree("engine", path.join(config.TEMP_FOLDER, "engine"))


if __name__ == '__main__':
    main()
