import sys
from os.path import dirname, join
from timeit import repeat


FILE = join(dirname(__file__), sys.argv[-1])
with open(FILE) as f:
    data = [line.split('-') for line in f.read().strip().split(',')]


def count_naive(data):
    _sum = 0
    for start, end in data:
        r = range(int(start), int(end)+1)
        for e in r:
            s = str(e)
            cur_len = len(s)
            for width in range(1, cur_len//2 + 1):
                if cur_len % width != 0:
                    continue
                if s[:width] * (cur_len // width) == s:
                    _sum += e
                    break

    return _sum


# 69564213293
res = count_naive(data)
assert res == 69564213293
print(res)

print(repeat(
    'count_naive(data)',
    setup="from __main__ import count_naive",
    globals=globals(),
    repeat=3,
    number=1,
))

