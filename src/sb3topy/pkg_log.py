"""
pkg_log.py

Handles the package logger.
"""

import logging
from logging import handlers

from . import config, packer, parser, unpacker

pkg_logger = logging.getLogger(__package__)

packer_logger = logging.getLogger(packer.__name__)
parser_logger = logging.getLogger(parser.__name__)
unpacker_logger = logging.getLogger(unpacker.__name__)


def init_logger():
    """
    Initializes the package logger.

    Called in `__init__` when the package loads.
    """

    # Create a handle to print to the console
    std_handle = logging.StreamHandler()

    # Add a formatter for formatted messages
    std_fmt = logging.Formatter("[%(levelname)s] %(message)s")
    std_handle.setFormatter(std_fmt)

    # Add the handler to the package's logger
    pkg_logger.addHandler(std_handle)


def config_logger():
    """
    Applies settings from `config` to the package logger.
    """
    pkg_logger.setLevel(config.LOG_LEVEL)


def config_queue(queue):
    """
    Configures the logger to send data over a queue.
    """
    handler = handlers.QueueHandler(queue)
    pkg_logger.addHandler(handler)
