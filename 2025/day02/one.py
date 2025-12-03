import sys
from os.path import dirname, join


FILE = join(dirname(__file__), '../../data/2025/day02/', sys.argv[-1])
with open(FILE) as f:
    data = [line.split('-') for line in f.read().strip().split(',')]


def naive(data):
    _sum = 0
    for start, end in data:
        r = range(int(start), int(end)+1)
        for e in r:
            s = str(e)
            h = len(s) // 2
            if s[:h] == s[h:]:
                _sum += e

    return _sum


print(naive(data))
# print(repeat(
#       'naive(data)',
#       setup='from __main__ import naive',
#       globals=globals(),
#       repeat=3,
#       number=10,
# ))
