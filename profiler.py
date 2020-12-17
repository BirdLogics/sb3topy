"""
Profiler reader
"""

import pstats
from pstats import SortKey
p = pstats.Stats('profiler.log')

p.sort_stats("cumulative").print_stats("pygame|sb3topy")