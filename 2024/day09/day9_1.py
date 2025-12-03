# data: ~20k numbers
# example:
# 2333133121414131402
# 00...111...2...333.44.5555.6666.777.888899
# TODO: don't create any intermediate arrays, just count from input
# TODO: do bitmasking instead of auxilliary array

from array import array
from time import time

def timer(func):
    def w():
        start = time()
        res = func()
        print(f'{func.__name__} done in {time() - start:.3f}')
        return res

    return w

with open('input', 'rb') as f:
    disk_map = array('B', (x-48 for x in f.read()[:-2]))


@timer
def count_naive():
    disk = array('i')

    EMPTY = -1
    ID = 0
    is_file = True
    for size in disk_map:
        if is_file:
            for i in range(size):
                disk.append(ID)
            ID += 1
        else:
            for i in range(size):
                disk.append(EMPTY)
        is_file = not is_file

    lcur = 0
    rcur = len(disk) - 1
    print(f'last is {disk[-1]}')
    while lcur < rcur:
        left = disk[lcur]
        right = disk[rcur]
        if right == EMPTY:
            rcur -= 1
            continue
        if left != EMPTY:
            lcur += 1
            continue
        disk[lcur], disk[rcur] = disk[rcur], disk[lcur]

    checksum = 0
    for i, v in enumerate(disk):
        if v == EMPTY:
            break
        checksum += i * v

    return checksum


print(count_naive())
