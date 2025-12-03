# data: 380 "machines"
# TODO: fix this, there should be way better way
import re
from time import time
machines = []

# Button A: X+69, Y+23
# Button B: X+27, Y+71
# Prize: X=18641, Y=10279
COST_A = 3
COST_B = 1
SHIFT = 10_000_000_000_000
INF = float('inf')


with open('input') as f:
    raw = f.read().split('\n\n')
    machines = [[int(x) for x in re.findall(r'\d+', r)] for r in raw if r]


def naive(machines):
    total_cost = 0

    for i, (ax, ay, bx, by, base_x, base_y) in enumerate(machines):
        tx = base_x + SHIFT
        ty = base_y + SHIFT

        # let's "scroll" to (SHIFT, SHIFT), floor, and naively iterate to target
        # a * ax + b * bx == SHIFT == a * ay + b * by
        # a * (ax - ay) == b * (by - bx)
        # b == a * (ax - ay) / (by - bx) == a * k
        # a * ax + a * k * bx == SHIFT
        # a == SHIFT / ( ax + bx * k )

        k = (ax - ay) / (by - bx)
        start_a = int( SHIFT / ( ax + bx * k ) ) - 10**3  # probably should substract based on bx/by
        start_b = int( start_a * k ) - 10**3

        da = 0
        db = 0
        x = start_a * ax + start_b * bx
        y = start_a * ay + start_b * by
        cost = INF
        while True:
            while True:
                total_a = start_a + da
                total_b = start_b + db
                x = total_a * ax + total_b * bx
                y = total_a * ay + total_b * by
                if (x > tx) or (y > ty):
                    break
                elif x == tx and y == ty:
                    cost = min(cost, total_a * COST_A + total_b * COST_B)
                
                db += 1

            da += 1
            db = 0
            total_a = start_a + da
            total_b = start_b + db
            x = total_a * ax + total_b * bx
            y = total_a * ay + total_b * by
            if (x > tx) or (y > ty):
                break

        if cost < INF:
            total_cost += cost
        print(f'done {i}')

    return total_cost




start = time()
print(naive(machines))
print(f'{time() - start:.3f}')
# 54983306797216 low
# 78806430983689 low 
# 87582154060429 *
