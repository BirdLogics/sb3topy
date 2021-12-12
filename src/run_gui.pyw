#!/usr/bin/env python3
"""
A quick helper file to run the GUI.

Identical to calling `python3 -m sb3topy --gui` on the command line.
Additional arguments cannot be passed via this helper file.
"""

import sb3topy.main

if __name__ == '__main__':
    sb3topy.main.main(["--gui"])
