"""
main.py

Orchastrates unpacking, converting assets, parsing
the project, and copying files based on configuration.

To allow simple configuration from the command line, the
path to a configuration json can be passed as an argument.
"""


import logging
from logging.handlers import QueueHandler
from multiprocessing import Process, Queue

from . import config, packer, parser, project, unpacker


def main(args=None):
    """
    Reads configuration from the command line and runs the converter
    """
    # Load configuration from the command line
    config.parse_args(args)

    # Setup the logger
    logging.basicConfig(
        format="[%(levelname)s] %(message)s", level=config.LOG_LEVEL)

    # Run the gui if it is enabled
    if config.USE_GUI:
        # Lazy import of gui. If tkinter is not installed or the GUI is
        # otherwise broken, the terminal interface should still work.
        from . import gui  # pylint: disable=import-outside-toplevel

        gui.run_app()

    # Run the conversion
    else:
        run()


def run():
    """
    Converts the project using the settings saved in config
    """

    # Initialize the manifest
    manifest = project.Manifest(config.OUTPUT_PATH)

    # Download the project from the internet
    if config.PROJECT_URL:
        sb3 = unpacker.download_project(manifest, config.PROJECT_URL)

    # Extract the project from an sb3
    elif config.PROJECT_PATH:
        sb3 = unpacker.extract_project(manifest, config.PROJECT_PATH)

    else:
        logging.error("A project url/path was not provided.")
        sb3 = None

    # Verify the project was unpacked
    if sb3 is None or not sb3.is_sb3():
        return False

    # Save a debug json
    if config.DEBUG_JSON:
        project.save_json(sb3, manifest, config.FORMAT_JSON)

    # Convert project assets
    if config.CONVERT_ASSETS:
        unpacker.convert_assets(manifest)

    # Copy engine files
    if config.COPY_ENGINE:
        packer.copy_engine(manifest)

    if config.PARSE_PROJECT:
        # Parse the project
        code = parser.parse_project(sb3, manifest)

        # Save the project's code
        packer.save_code(manifest, code)

        logging.info("Finished converting project. Saved in '%s'",
                     manifest.output_dir)

    if config.AUTORUN:
        packer.run_project(manifest.output_dir)

    logging.info("Done!")

    return True


def _run_worker(queue, config_data):
    """
    Runs and attaches a QueueHandler to the log
    """
    try:
        config.set_config(config_data)

        handler = QueueHandler(queue)
        logger = logging.getLogger()
        logger.addHandler(handler)
        logger.setLevel(logging.DEBUG)

        run()

    # Catch any errors so they can be shown in the GUI
    except Exception:
        logging.critical(
            "Unhandled exception during the conversion process:",
            exc_info=True)
        raise


def run_mp():
    """
    Runs in a new Process. Returns a Process, Queue pair.

    The Queue is tied to a QueueHandler to get log messages.
    """
    config_data = config.get_config()
    queue = Queue(-1)
    process = Process(target=_run_worker, args=(
        queue, config_data), daemon=True)
    process.start()

    return process, queue
