import sys
from os.path import dirname, join


FILE = join(dirname(__file__), '../../data/2025/day01/', sys.argv[-1])
with open(FILE) as f:
    data = f.readlines()


def naive(shifts):
    current = 50
    passes = 0
    for shift in shifts:
        current += int(shift.replace('L', '-').replace('R', '+'))
        current = current % 100
        
        if current == 0:
            passes += 1

    return passes


print(naive(data))

# from timeit import repeat
# print(repeat(
#       'naive(data)',
#       setup='from __main__ import naive',
#       globals=globals(),
#       repeat=3,
#       number=10,
# ))
