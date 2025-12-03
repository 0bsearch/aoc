# data: 50x50 field, ~20k moves

from time import time
from array import array

raw_field = []
raw_moves = []


with open('input') as f:
    for l in f:
        if l == '\n':
            break
        row = array('u')
        for c in l:
            if c == '#':
                row.extend('##')
            elif c == '.':
                row.extend('..')
            elif c == '@':
                row.extend('@.')
            elif c == 'O':
                row.extend('[]')
            elif c == '\n':
                break
            else:
                raise ValueError(c)
        raw_field.append(row)

    for l in f:
        raw_moves.extend(list(l.strip()))


def naive(field, moves):
    EMPTY = '.'
    WALL  = '#'
    LBOX  = '['
    RBOX  = ']'
    ROBOT = '@'
    move_map = {
        '>': ( 1,  0),
        'v': ( 0,  1),
        '<': (-1,  0),
        '^': ( 0, -1)
    }
    
    def pushable(x, y, move):
        dx, dy = move_map[move]
        tx, ty = x + dx, y + dy
        self = field[y][x]
        
        if self == RBOX and (move == '^' or move == 'v'):
            return pushable(tx, ty, move) and pushable(tx-1, ty, move)

        if self == LBOX and (move == '^' or move == 'v'):
            return pushable(tx, ty, move) and pushable(tx+1, ty, move)

        if self == EMPTY:
            return True

        if self == WALL:
            return False

        if pushable(tx, ty, move):
            return True

        return False

    def push(x, y, move, lazy=False):
        dx, dy = move_map[move]
        tx, ty = x + dx, y + dy
        self = field[y][x]
        target = field[ty][tx]
        
        if self == EMPTY:
            return True

        if self == RBOX and (move == '^' or move == 'v') and not lazy:
            if pushable(tx, ty, move) and pushable(tx-1, ty, move):
                push(tx, ty, move)
                field[ty][tx] = field[y][x]
                field[y][x] = EMPTY
                push(x-1, y, move, True)
                return True
            else:
                return False

        if self == LBOX and (move == '^' or move == 'v') and not lazy:
            if pushable(tx, ty, move) and pushable(tx+1, ty, move):
                push(tx, ty, move)
                field[ty][tx] = field[y][x]
                field[y][x] = EMPTY
                push(x+1, y, move, True)
                return True
            else:
                return False
        
        if target == WALL:
            return False

        if push(tx, ty, move):
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

    for i, move in enumerate(moves):
        dx, dy = move_map[move]

        if push(x, y, move):
            x += dx
            y += dy

    gps_sum = 0
    for y, row in enumerate(field):
        for x, cell in enumerate(row):
            if cell == LBOX:
                gps_sum += (x + 100 * y)

    return gps_sum



start = time()
print(naive(raw_field, raw_moves))
print(f'{time() - start:.3f}')
# 1416313 -- too high
# 1412866
