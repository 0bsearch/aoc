# data: constant width of 100, no zeros

import sys
from os.path import dirname, join
from timeit import repeat


WIDTH = 12
FILE = join(dirname(__file__), sys.argv[-1])
with open(FILE) as f:
    data = [line.strip() for line in f]


def slice(packs):
    total = 0
    for _pack in packs:
        pack = [int(x) for x in _pack]
        joltage = 0
        offset = 0
        for place in range(WIDTH-1, -1, -1):
            digit = max(pack[offset:-place or None])
            offset = pack.index(digit, offset) + 1
            joltage += digit * 10 ** place
        total += joltage

    return total


# 171741365473332
print(slice(data))
print(repeat(
      'slice(data)',
      setup='from __main__ import slice',
      globals=globals(),
      repeat=3,
      number=1000
))
