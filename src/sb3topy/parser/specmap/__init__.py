"""
Handles converting parsed block data into code

When given an opcode, it gets a BlockMap which handles
formatting parsed inputs and fields into Python code.
"""

from . import codemap
from .blockmap import *
from .data import *
from .specmap import *
from .typing import *

data.init_data()
