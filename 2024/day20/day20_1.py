# data: 141x141
# ideas:
#   1. Walk through maze, marking cost on every tile
#   2. For every pair of "walkable" tiles within 2 tiles range, count cheat efficiency

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

SIZE = len(FIELD)


def naive(field):
    x, y = START_X, START_Y
    cost = 0
    field[y][x] = cost

    while not (x == END_X and y == END_Y):
        for dx, dy in (1, 0), (0, 1), (-1, 0), (0, -1):
            tx, ty = x + dx, y + dy
            if field[ty][tx] == EMPTY:
                x, y = tx, ty
                cost += 1
                field[y][x] = cost
                break

   
    from collections import defaultdict
    shortcuts = defaultdict(int)
    total = 0

    for y in range(1, SIZE-1):
        for x in range(1, SIZE-1):
            if field[y][x] != WALL:
                continue

            a = field[y][x-1]
            b = field[y][x+1]
            if a != WALL and b != WALL:
                cut = abs(a - b) - 2
                shortcuts[cut] += 1
                if cut >= 100:
                    total += 1

            a = field[y-1][x]
            b = field[y+1][x]
            if a != WALL and b != WALL:
                cut = abs(a - b) - 2
                shortcuts[cut] += 1
                if cut >= 100:
                    total += 1
    
    for k in sorted(shortcuts.keys()):
        print(f'{k} -> {shortcuts[k]}')
    return total


start = time()
print(f'naive>\t{naive(FIELD)}\tin {time() - start:.3f} s')
# 1521

