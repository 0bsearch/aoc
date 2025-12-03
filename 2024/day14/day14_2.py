# data: input field: 101x103
# Field size is prime twins, i.e. complete cycle of any robot (and all robots together)
#   should be 101*103 == 10403. So we're looking for smth lower than that.
# Cycle for single axis would be 101 or 103 respectively, so looking manually
#   we should see _something_ cyclic every 101 and 103 ticks.
#
# If we'd know that shape is filled, maybe std would show smth, but alas.
# Maybe we can do fuzzy match matrixes with 101 ticks lag and find base point?
# Let's do manually for now

import re
from time import time, sleep

FIELD_X = 101
FIELD_Y = 103

robots = []
with open('input') as f:
    for l in f:
        robots.append([int(x) for x in re.findall(r'\-?\d+', l)])


def pr(field):
    for l in field:
        print(''.join(['*' if x else ' ' for x in l]))


def scroll(robots):
    for t in range(10169, 0, -101):
        field = [[0]*FIELD_X for _ in range(FIELD_Y)]

        for start_x, start_y, vx, vy in robots:
            x = (start_x + vx * t) % FIELD_X
            y = (start_y + vy * t) % FIELD_Y
            field[y][x] += 1

        pr(field)
        input(t)


start = time()
print(scroll(robots))
print(f'{time() - start:.3f}')
