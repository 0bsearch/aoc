# data: 140x140
# TODO: single-pass over field with sliding window and remove "borders"
from array import array
from time import time
from itertools import count


field = []
with open('input', 'rb') as f:
    for l in f:
        field.append(array('b', l.strip()))


def walk(field):
    x_size = len(field[0])
    y_size = len(field)
    I_SIZE = array('I').itemsize
    ids = [array('I', b'\00'*I_SIZE*x_size) for _ in range(y_size)]
    id_seq = count(1)
    total_price = 0
    others = [(0, 0)]

    def bound(x, y):
        return 0 <= x < x_size and 0 <= y < y_size

    while others:
        rx, ry = others.pop()
        if ids[ry][rx] != 0:
            continue
        group = [(rx, ry)]
        gid = next(id_seq)

        area = 0
        perimeter = 0
        while group:
            x, y = group.pop()
            if ids[y][x] == 0:
                ids[y][x] = gid
            else:
                continue
            area += 1
            for dx, dy in (-1, 0), (0, 1), (1, 0), (0, -1):
                tx, ty = x + dx, y + dy
                if not bound(tx, ty):
                    perimeter += 1
                    continue
                if field[ty][tx] == field[y][x]:
                    if ids[ty][tx] == 0:
                        group.append((tx, ty))
                else:
                    perimeter += 1
                    if ids[ty][tx] == 0:
                        others.append((tx, ty))

        # print(f'Finished group {chr(field[ry][rx])} @ {rx}:{ry}. A: {area}\tP: {perimeter}')
        total_price += area * perimeter

    return total_price



start = time()
print(walk(field))
print(f'{time() - start:.3f}')
