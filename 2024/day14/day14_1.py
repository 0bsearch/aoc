# data:
#   example field: 11x7
#   input field: 101x103

import re
from time import time

# FIELD_X = 11
# FIELD_Y = 7
TICKS = 100
FIELD_X = 101
FIELD_Y = 103


robots = []
with open('input') as f:
    for l in f:
        robots.append([int(x) for x in re.findall(r'\-?\d+', l)])


def scroll(robots):
    Q = [0, 0, 0, 0, 0]
    MID_X = FIELD_X // 2
    MID_Y = FIELD_Y // 2

    for start_x, start_y, vx, vy in robots:
        x = (start_x + vx * TICKS) % FIELD_X
        y = (start_y + vy * TICKS) % FIELD_Y

        if x == MID_X or y == MID_Y:
            i = 0
        elif x > MID_X and y < MID_Y:
            i = 1
        elif x < MID_X and y < MID_Y:
            i = 2
        elif x < MID_X and y > MID_Y:
            i = 3
        elif x > MID_X and y > MID_Y:
            i = 4
        else:
            raise ValueError('fix your typo')

        # print(f'Started at ({start_x}, {start_y}) with ({vx}, {vy}), got into ({x}, {y}) @ Q{i}')
        Q[i] += 1

    return Q[1] * Q[2] * Q[3] * Q[4]


start = time()
print(scroll(robots))
print(f'{time() - start:.3f}')
