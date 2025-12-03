from time import time
from array import array
from collections import deque

EMPTY = '.'
WALL = '#'

with open('input') as f:
    drops = [[int(x) for x in l.strip().split(',')] for l in f]
    if f.name == 'example':
        SIZE = 7
        BYTES = 12
    else:
        SIZE = 71
        BYTES = 1024


def bfs(drops):
    end_x, end_y = SIZE - 1, SIZE - 1
    field = [array('u', EMPTY * SIZE) for _ in range(SIZE)]
    for x, y in drops[:BYTES]:
        field[y][x] = WALL

    MAX_COST = 2**32 - 1 
    cost = [array('I', [MAX_COST] * SIZE) for _ in range(SIZE)]
    q = deque([(0, 0, 0)])

    while q:
        x, y, current_cost = q.popleft()

        if current_cost >= cost[y][x]:
            continue
        else:
            cost[y][x] = current_cost

        if x == end_x and y == end_y:
            continue

        for dx, dy in ((1, 0), (0, 1), (-1, 0), (0, -1)):
            tx, ty = x + dx, y + dy
            if 0 <= tx < SIZE and 0 <= ty < SIZE and field[ty][tx] != WALL:
                q.append((tx, ty, current_cost + 1))


    return cost[end_y][end_x]


start = time()
print(f'bfs:\t{bfs(drops)}\tin {time() - start:.3f}')
# 140: low
