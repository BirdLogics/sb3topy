"""


This module's job is to run the unpacker and parser together.
"""

import logging
import unpacker
import sbparser

LOG_LEVEL = 20
OUTPUT_PATH = "results/result.py"


def main():
    """Main function"""
    logging.basicConfig(format="[%(levelname)s] %(message)s", level=LOG_LEVEL)

    sb3, _ = unpacker.Project().unpack()
    code = sbparser.Parser(sb3).parse()

    with open(OUTPUT_PATH, 'w') as code_file:
        code_file.write(code)


if __name__ == "__main__":
    main()
