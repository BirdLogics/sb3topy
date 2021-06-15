"""
__init__.py
"""

# flake8: noqa

from . import config
from . import parser
from . import sanitizer
from . import unpacker


def load_config(path):
    """Reloads config with a given json path"""
    import importlib
    config.CONFIG_PATH = path
    importlib.reload(config)
