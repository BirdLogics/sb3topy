"""
config

Handles configuration for sb3topy.

The values in this package may be modified before starting the
conversion process. Currently, the the configuration may be modified
by either the GUI, a config file, or by command line arguments.

The default values can be overriden by modifying the config.json file
in this package. The values will be read when the module is loaded.

It is not recommended to override defaults with the config.json.
Instead, you should use the command line argument -c or create a
user config file (see below).

When using the GUI, a user config file can be automatically loaded
from CONFIG_PATH, which by default is "~/.sb3topy.json". The default
CONFIG_PATH can be modified in the config.json mentioned above.

Automatic loading of the user config file can be disabled by setting
AUTOLOAD_CONFIG to false in either the user config file or the
config.json.

For details about modifiable configuration values, see config.defaults.
For details about modifiable project config values, see config.project.
"""


from .config import *
from .consts import *
from .defaults import *
from .project import *
