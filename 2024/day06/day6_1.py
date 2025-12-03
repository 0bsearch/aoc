# data: 130x130
from itertools import cycle
from collections import namedtuple

Vec2 = namedtuple('Vector2d', ['x', 'y'])

directions = {
    '↑': Vec2( 0, -1),
    '→': Vec2( 1,  0),
    '↓': Vec2( 0,  1),
    '⟵': Vec2(-1,  0),
}

BLOCK = '#'
START = '^'
field = []
pos_x, pos_y = ..., ...

with open('input') as f:
    for i, l in enumerate(f):
        field.append(l.strip())
        if START in l:
            pos_x = l.index(START)
            pos_y = i

x_min, x_max = 0, len(field[0]) - 1
y_min, y_max = 0, len(field) - 1
rota = cycle(directions.values())
facing = next(rota)
steps = set()  # waste of N² of memory for now


while True:
    steps.add((pos_x, pos_y))
    tx, ty = pos_x + facing.x, pos_y + facing.y
    if not x_min <= tx <= x_max or not y_min <= ty <= y_max:
        break

    if field[ty][tx] == BLOCK:
        facing = next(rota)
    else:
        pos_x, pos_y = tx, ty

print(len(steps))
