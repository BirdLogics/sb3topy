"""
config

Handles configuration for sb3topy.

The values in this package may be modified before starting the
conversion process. Currently, the the configuration may be modified
by either the GUI, a config file, or by command line arguments.

Neither the GUI or a config file can be loaded without command line
arguments.

For details about modifiable configuration values, see config.defaults.
For details about modifiable project config values, see config.project.
"""


from .config import *
from .consts import *
from .defaults import *
from .project import *
