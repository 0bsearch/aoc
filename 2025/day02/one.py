import sys
from os.path import dirname, join


FILE = join(dirname(__file__), sys.argv[-1])
with open(FILE) as f:
    data = [line.split('-') for line in f.read().strip().split(',')]


def count_naive(data):
    _sum = 0
    for start, end in data:
        r = range(int(start), int(end)+1)
        for e in r:
            s = str(e)
            h = len(s) // 2
            if s[:h] == s[h:]:
                _sum += e

    return _sum


print(count_naive(data))
