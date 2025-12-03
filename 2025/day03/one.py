# data: constant width of 100, no zeros

import sys
from os.path import dirname, join
from timeit import repeat


FILE = join(dirname(__file__), '../../data/2025/day03/', sys.argv[-1])
with open(FILE) as f:
    data = [line.strip() for line in f]


def naive(packs):
    total = 0
    for _pack in packs:
        pack = [int(x) for x in _pack]
        left, right = 0, 0
        size = len(pack)
        for i in range(size):
            if pack[i] > left:
                if i+1 < size:
                    left = pack[i]
                    right = pack[i+1]
                elif pack[i] > right:
                    right = pack[i]
            elif pack[i] > right:
                right = pack[i]
        total += (left * 10 + right)

    return total


def slice(packs):
    total = 0
    for _pack in packs:
        pack = [int(x) for x in _pack]
        left = max(pack[:-1])
        left_i = pack.index(left)
        right = max(pack[left_i+1:])
        total += left * 10 + right

    return total


# 17316
print(naive(data))
print(repeat(
      'naive(data)',
      setup='from __main__ import naive',
      globals=globals(),
      repeat=3,
      number=1000
))

print(slice(data))
print(repeat(
      'slice(data)',
      setup='from __main__ import slice',
      globals=globals(),
      repeat=3,
      number=1000
))
