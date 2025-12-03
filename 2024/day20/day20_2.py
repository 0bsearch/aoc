# data: 141x141
# ideas:
# =========================================================================================
#   1. Walk through, save cost; save step coords in separate list
#   2. Iterate over list, compare cost diff & distance
# =========================================================================================


from time import time
from array import array

FIELD = []
WALL = 2**16 - 1
EMPTY = -1

with open('input') as f:
    for y, l in enumerate(f):
        if 'S' in l:
            START_X, START_Y = l.index('S'), y
        elif 'E' in l:
            END_X, END_Y = l.index('E'), y

        FIELD.append(array('i', [WALL if c == '#' else EMPTY for c in l.strip()]))

    MIN_SKIP = 50 if f.name == 'example' else 100


SPAN = 20


def naive(field):
    x, y = START_X, START_Y
    cost = 0
    path = [(x, y)]
    field[y][x] = cost
    cheats = 0

    while x != END_X or y != END_Y:
        cost += 1

        for dx, dy in (1, 0), (0, 1), (-1, 0), (0, -1):
            tx, ty = x + dx, y + dy
            if field[ty][tx] == EMPTY:
                x, y = tx, ty
                field[y][x] = cost
                path.append((x, y))
                break

    for i, (base_x, base_y) in enumerate(path):
        for x, y in path[i+MIN_SKIP:]:
            span = abs(x-base_x) + abs(y-base_y)
            if span > SPAN:
                continue
            save = field[y][x] - i - span
            if save >= MIN_SKIP:
                cheats += 1

    return cheats


start = time()
print(f'naive>\t{naive(FIELD)}\tin {time() - start:.3f} s')
# 1013106

