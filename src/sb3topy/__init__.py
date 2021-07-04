"""
__init__.py
"""

# flake8: noqa

from . import config, unpacker
from .parser import parser, sanitizer


def load_config(path):
    """Reloads config with a given json path"""
    import importlib
    config.CONFIG_PATH = path
    importlib.reload(config)
