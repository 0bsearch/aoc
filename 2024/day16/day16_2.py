# data: 141x141
# ideas:
#   heapq
#   graph

from array import array
from pprint import pp
from time import time
from enum import Enum
from collections import deque, defaultdict

E = ( 1,  0)
N = ( 0, -1)
W = (-1,  0)
S = ( 0,  1)
TURN_COST = 1000
STEP_COST = 1
WALL = '#'
FLOOR = '.'


maze = []
with open('input') as f:
    for y, l in enumerate(f):
        maze.append(l.strip().replace('S', '.').replace('E', '.'))
        # maze.append(array('B', [WALL if c == '#' else FLOOR for c in l.strip()]))
        if 'S' in l:
            start_x = l.index('S')
            start_y = y
        elif 'E' in l:
            end_x = l.index('E')
            end_y = y


def bfs(maze, start_x, start_y, end_x, end_y):
    cost = {}
    record = 133584  # yoink from part 1
    record_routes = defaultdict(list)
    queue = deque([(start_x, start_y, E, 0, [])])

    while queue:
        *pos, facing, current_cost, route = queue.popleft()
        pos = tuple(pos)
        x, y = pos

        route.append(pos)
        if x == end_x and y == end_y:
            record = min(record, current_cost)
            record_routes[current_cost].append(route)
            continue

        if current_cost >= record:
            continue

        if pos not in cost:
            cost[pos] = current_cost, facing
        else:
            prev_cost, prev_facing = cost[pos]
            if prev_facing == facing and prev_cost < current_cost:
                continue
            elif prev_cost < current_cost - TURN_COST:
                continue
            if prev_cost > current_cost:
                cost[pos] = current_cost, facing
        
        fx, fy = facing

        for dx, dy in N, E, W, S:
            tx, ty = x + dx, y + dy
            if maze[ty][tx] == WALL:
                continue
            elif dx == -fx and dy == -fy:
                continue
            elif dx == fx and dy == fy:
                turn_cost = 0
                next_cost = turn_cost + STEP_COST + current_cost
                queue.append((tx, ty, (dx, dy), next_cost, route))
            else:
                turn_cost = TURN_COST
                next_cost = turn_cost + STEP_COST + current_cost
                queue.append((tx, ty, (dx, dy), next_cost, route.copy()))


    spots = set()
    for route in record_routes[record]:
        for tile in route:
            spots.add(tile)

    return record, len(spots)


start = time()
print(bfs(maze, start_x, start_y, end_x, end_y))
print(f'BFS: {time() - start:.3f}')


