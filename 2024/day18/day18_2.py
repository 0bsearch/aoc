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


def pf(field):
    for row in field:
        print(''.join(row))

def bfs(drops):
    end_x, end_y = SIZE - 1, SIZE - 1
    MAX_COST = 2**32 - 1 

    # binary search for passable/blocked mazes by # of bytes dropped
    passable, blocked = BYTES, len(drops)
    while passable != blocked - 1:
        bytes_to_drop = passable + (blocked - passable) // 2

        field = [array('u', EMPTY * SIZE) for _ in range(SIZE)]
        for drop_x, drop_y in drops[:bytes_to_drop + 1]:
            field[drop_y][drop_x] = WALL

        q = deque([(0, 0, 0)])
        cost = [array('I', [MAX_COST] * SIZE) for _ in range(SIZE)]

        while q:
            x, y, current_cost = q.popleft()
            if x == end_x and y == end_y:
                connected = True
                break

            if current_cost >= cost[y][x]:
                continue
            else:
                cost[y][x] = current_cost

            for dx, dy in ((1, 0), (0, 1), (-1, 0), (0, -1)):
                tx, ty = x + dx, y + dy
                if 0 <= tx < SIZE and 0 <= ty < SIZE and field[ty][tx] != WALL:
                    q.append((tx, ty, current_cost + 1))
        else:
            connected = False

        if connected:
            passable = bytes_to_drop
        else:
            blocked = bytes_to_drop

    print(f'{drops[blocked]} @ {blocked}')
    return ','.join(str(x) for x in drops[blocked])


start = time()
print(f'bfs:\t{bfs(drops)}\tin {time() - start:.3f}')
# 24,48 @ 2881
