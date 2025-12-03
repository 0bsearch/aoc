# data: 140x140
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
        vertices = 0
        while group:
            x, y = group.pop()
            if ids[y][x] == 0:
                ids[y][x] = gid
            else:
                continue
            area += 1

            # count vertices
            # a|b  A has     b|c  A has     a|a  A has   
            # -+-  inner     -+-  outer     -+-  no   
            # A|a  vertex    A|d  vertex    A|a  vertex  
            # print(f'\tchecking vertices for {x}:{y}')
            for (dax, day), (dbx, dby) in zip(
                    ((-1,  0), ( 0,  1), ( 1,  0), ( 0, -1)),
                    (( 0,  1), ( 1,  0), ( 0, -1), (-1,  0))):
                ax, ay = x + dax, y + day
                bx, by = x + dbx, y + dby
                cx, cy = x + dax + dbx, y + day + dby
                a_is_same = bound(ax, ay) and field[y][x] == field[ay][ax]
                b_is_same = bound(bx, by) and field[y][x] == field[by][bx]
                c_is_same = bound(cx, cy) and field[y][x] == field[cy][cx]
                if (not bound(ax, ay)) and (not bound(bx, by)):
                    vertices += 1
                elif a_is_same and b_is_same and (not c_is_same):
                    vertices += 1
                elif (not a_is_same) and (not b_is_same):
                    vertices += 1

            # advance search
            for dx, dy in (-1, 0), (0, 1), (1, 0), (0, -1):
                tx, ty = x + dx, y + dy
                if not bound(tx, ty):
                    continue
                if field[ty][tx] == field[y][x]:
                    if ids[ty][tx] == 0:
                        group.append((tx, ty))
                else:
                    if ids[ty][tx] == 0:
                        others.append((tx, ty))

        print(f'Finished group {chr(field[ry][rx])} @ {rx}:{ry}. A: {area}\tV: {vertices}')
        total_price += area * vertices

    return total_price



start = time()
print(walk(field))
print(f'{time() - start:.3f}')
