# sb3topy

sb3topy is a tool which can convert [Scratch 3.0](https://scratch.mit.edu) projects into Python. The project is converted into a single file which can run using the sb3topy engine and Pygame. The engine files are automatically copied when the converter is run.

Currently, sb3topy is in Beta and may have bugs or missing features which could prevent some project from running correctly. In addition, there may be bugs which allow arbitrary Python code to run, so be cautious when running untrusted projects.

A full list of supported blocks can be found [here](docs/supported_blocks.md).

## Quickstart

1. Using Python 3.7+, install the recommended packages (pygame, requests, and cairosvg) with pip. Note that some users may need to take additional steps to support SVG conversion (see Requirements).

   ```pip install -r requirements.txt```

2. Run the GUI.

    ```python run_gui.pyw```

3. Pick an example and hit Download & Run.

## Requirements

Before using sb3topy, there are a few Python packages which you may need to install using [pip](https://pypi.org/project/pip/). The program should still work without any of these installed, but there may be reduced functionality. You can install each package individually, or you can install all packages at once using [requirements.txt](requirements.txt).

| Package  | Description                                                                                                                    |
| -------- | ------------------------------------------------------------------------------------------------------------------------------ |
| pygame   | Used by the engine to run converted projects.                                                                                  |
| requests | Used to download projects and example thumbnails in the GUI.                                                                   |
| cairosvg | Used to convert SVG files, which are not supported by Pygame, into PNGs. It may be difficult to install this package on some systems. |

Note that Pygame 2+ is required to play MP3 files. MP3 files can optionally be converted using VLC player. To enable MP3 conversion or convert using a custom command, see the assets tab of the GUI.

Note that CairoSVG may be difficult to install on some systems. See CairoSVG's instructions [here](https://cairosvg.org/documentation/). Inkscape can be used as an alternative, but it must be configured under the Assets tab of the GUI. You may need to replace "inkscape" in the convert command with the full path to the executable.

Note that one of the examples, "The Taco Incident," does not contain any SVG costumes. If you want to get started without installing an SVG conversion tool, you should still be able to run this example. You can also manually convert every costume to bitmap to allow a project to run.

Support for alternate SVG conversion tools with an easier installation process is being looked into.

## Command Usage

```
python -m sb3topy --help
usage: __main__.py [-h] [-c [file]] [--gui] [-r] [PROJECT_PATH] [OUTPUT_PATH]

Converts sb3 files to Python.

positional arguments:
  PROJECT_PATH  path to a sb3 project
  OUTPUT_PATH   specifies an output directory

options:
  -h, --help    show this help message and exit
  -c [file]     path to a config json, disables autoload
  --gui         starts the graphical user interface
  -r            automatically runs the project when done
```
