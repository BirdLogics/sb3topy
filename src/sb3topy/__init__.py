"""
__init__.py
"""

# flake8: noqa

from . import config, packer, parser, project, unpacker
from .parser import sanitizer


def load_config(path):
    """Reloads config with a given json path"""
    import importlib
    config.CONFIG_PATH = path
    importlib.reload(config)
