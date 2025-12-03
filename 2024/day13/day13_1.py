# data: 380 "machines"
import re
from time import time
machines = []

COST_A = 3
COST_B = 1
MAX_CLICKS = 100

with open('input') as f:
    raw = f.read().split('\n\n')
    machines = [[int(x) for x in re.findall(r'\d+', r)] for r in raw if r]

def naive(machines):
    total_cost = 0

    for i, (ax, ay, bx, by, x, y) in enumerate(machines):
        # print('\n', i, ax, ay, bx, by, x, y)
        machine_min = MAX_CLICKS * (COST_A + COST_B)
        reachable = False

        for ai in range(MAX_CLICKS):
            for bi in range(MAX_CLICKS):
                if ai * ax + bi * bx == x and ai * ay + bi * by == y:
                    # print(f'reached at {ai}:{bi}')
                    reachable = True
                    machine_min = min(machine_min, COST_A * ai + COST_B * bi)
                else:
                    pass
                    # print(f'{ai}*{ax} + {bi}*{bx}')

        if reachable:
            total_cost += machine_min
            # print(f'machine {i} got cost {machine_min}')


    return total_cost


start = time()
print(naive(machines))
print(f'{time() - start:.3f}')
