# data: 50x50 field, ~20k moves
# TODO/ideas:
#   - "compress" all crates in single move
#   - have field with bit flags and don't recurse

from time import time

raw_field = []
raw_moves = []

with open('input') as f:
    for l in f:
        if l == '\n':
            break
        raw_field.append(list(l.strip()))

    for l in f:
        raw_moves.extend(list(l.strip()))


def naive(field, moves):
    EMPTY = '.'
    WALL  = '#'
    CRATE = 'O'
    ROBOT = '@'
    move_map = {
        '>': ( 1,  0),
        'v': ( 0,  1),
        '<': (-1,  0),
        '^': ( 0, -1)
    }
    
    def push(x, y, dx, dy):
        tx, ty = x + dx, y + dy
        if field[ty][tx] == EMPTY:
            field[ty][tx] = field[y][x]
            field[y][x] = EMPTY
            return True
        elif field[ty][tx] == WALL:
            return False
        else:
            if push(tx, ty, dx, dy):
                field[ty][tx] = field[y][x]
                field[y][x] = EMPTY
                return True
            return False


    def pp(field):
        for l in field:
            print(''.join(l))


    for y, row in enumerate(raw_field):
        if ROBOT in row:
            x = row.index(ROBOT)
            break

    for move in moves:
        # pp(field)
        # input()
        dx, dy = move_map[move]

        if push(x, y, dx, dy):
            x += dx
            y += dy

    gps_sum = 0
    for y, row in enumerate(field):
        for x, cell in enumerate(row):
            if cell == CRATE:
                gps_sum += (x + 100 * y)

    return gps_sum



start = time()
print(naive(raw_field, raw_moves))
print(f'{time() - start:.3f}')
