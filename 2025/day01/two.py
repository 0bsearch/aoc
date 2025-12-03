import sys
from os.path import dirname, join


FILE = join(dirname(__file__), '../../data/2025/day01/', sys.argv[-1])
with open(FILE) as f:
    data = f.readlines()


def naive(shifts):
    current = 50
    passes = 0
    for shift in shifts:
        direction, steps = shift[0], shift[1:]
        if direction == 'R':
            for _ in range(int(steps)):
                current += 1
                if current == 100:
                    current = 0
                if current == 0:
                    passes += 1
        elif direction == 'L':
            for _ in range(int(steps)):
                current -= 1
                if current == 0:
                    passes += 1
                if current == -1:
                    current = 99
        else:
            raise ValueError

    return passes


def mod(shifts):
    current = 50
    passes = 0
    for move in shifts:
        start = current

        sign = -1 if move[0] == 'L' else 1
        step = int(move[1:])
        clicks = step // 100
        passes += clicks
        step = sign * (step % 100)
        current += step

        if not (0 < current < 100) and start != 0:
            passes += 1
        current %= 100

    return passes


# 5782
print(naive(data))
print(mod(data))

# from timeit import repeat
# print(repeat(
#       'naive(data)',
#       setup='from __main__ import naive',
#       globals=globals(),
#       repeat=3,
#       number=10,
# ))
