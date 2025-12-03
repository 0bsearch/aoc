# data: 130x130
# amount of steps to go through is ~5k,
# brute-forcing cyclic check over whole field would be ~130x130x5k,
# brute-forcing cyclic check over firth pass would be ~5k x 5k
# some smarter branching from path should be magnitudes lower, but idk

# let's do restricted bruteforce for now

from itertools import cycle
from collections import namedtuple
from array import array

Vec2 = namedtuple('Vector2d', ['x', 'y'])

directions = {
    '↑': Vec2( 0, -1),
    '→': Vec2( 1,  0),
    '↓': Vec2( 0,  1),
    '⟵': Vec2(-1,  0),
}

BLOCK = '#'
START = '^'
EMPTY = '.'
field = []

with open('input') as f:
    for i, l in enumerate(f):
        field.append(array('u', l.strip()))
        if START in l:
            start_x = l.index(START)
            start_y = i

x_min, x_max = 0, len(field[0]) 
y_min, y_max = 0, len(field)
obstacles = 0

def solve(x, y):
    rota = cycle(directions.values())
    v = next(rota)
    steps = set()  # waste of N² of memory for now

    while True:
        if (x, y, v) in steps:
            # been here, done this
            return True, None

        steps.add((x, y, v))
        tx, ty = x + v.x, y + v.y

        if not x_min <= tx < x_max or not y_min <= ty < y_max:
            # facing outside of field
            return False, steps

        if field[ty][tx] == BLOCK:
            v = next(rota)
        else:
            x, y = x + v.x, y + v.y

_, path = solve(start_x, start_y)
candidates = {(x, y) for x, y, _ in path}
for x, y in candidates:
    cell = field[y][x]
    if cell == START:
        continue

    field[y][x] = BLOCK
    cyclic, _ = solve(start_x, start_y)
    if cyclic:
        obstacles += 1

    field[y][x] = EMPTY

print(obstacles)
