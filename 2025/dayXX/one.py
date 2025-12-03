import sys
from os.path import dirname, join
from timeit import repeat


FILE = join(dirname(__file__), '../../data/2025/dayXX/', sys.argv[-1])
with open(FILE) as f:
    data = ...


def naive():
    return


print(naive(data))
# print(repeat(
#       'naive(data)',
#       setup='from __main__ import naive',
#       globals=globals(),
#       repeat=3,
#       number=10,
# ))
