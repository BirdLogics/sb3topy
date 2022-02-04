# specmap

The specmap contains the information needed to generate Python code for sb3 blocks.

## block

Handles the raw block_data and switches. Provides simple functions to access the data.


## block_switches

Handles more complex blocks which may have a different blockmap depending on how they are used.


## type_switches

Handles blocks such as variables which don't have a fixed type


## codemap

Contains functions for parsing parts of the project such as the `__init__` function into Python.

