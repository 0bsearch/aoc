# data: ~20k numbers
# example:
# 2333133121414131402
# 00...111...2...333.44.5555.6666.777.888899
# TODO: fix this insanity;
# should be possible to count chksum w/o eagerly creating array &
# probably in single disk_map pass

from array import array
from time import time

def timer(func):
    def w(*args):
        start = time()
        res = func(*args)
        print(f'{func.__name__} done in {time() - start:.3f}s')
        return res

    return w

with open('input', 'rb') as f:
    disk_map = array('B', (x-48 for x in f.read()[:-2]))


@timer
def count_naive(disk_map):
    disk = []
    offset = 0
    for i, size in enumerate(disk_map):
        ID, is_free = divmod(i, 2)
        disk.extend([(ID, is_free, offset, offset+size-1)] * size)
        offset += size

    rcur = len(disk) - 1

    while rcur > 0:
        # print('=======================================================')
        # print(''.join('.' if free else str(ID) for ID, free, *_ in disk), '\n', ' '*rcur + '^', sep='')
        ID, is_free, file_start, _ = disk[rcur]
        file_end = rcur
        file_size = file_end - file_start + 1
        # skip free chunks from right side
        if is_free:
            # print(f'skipping free chunk')
            rcur -= file_size
            continue

        # skip already relocated files
        if file_start > rcur:
            # print(f'skipping relocated file')
            rcur -= 1
            continue

        # find leftmost suitable free chunk
        lcur = 0
        while lcur < file_start:
            # print(''.join('.' if free else str(ID) for ID, free, *_ in disk), '\n', ' '*lcur + '@', sep='')
            _, is_free, _, free_end = disk[lcur]
            if not is_free:
                lcur += 1
                continue

            free_start = lcur
            free_size = free_end - free_start + 1
            # print(f'searching for {file_size} blocks, got {free_size}')
            if free_size < file_size:
                lcur += free_size
                continue
            else:
                break
        else:
            # can not find big enough free chunk
            rcur -= file_size
            continue

        # print(f'Relocating ID {ID} from {file_start}_{file_end} to {free_start}')

        disk[free_start:free_start+file_size], disk[file_start:file_start+file_size] =\
        disk[file_start:file_start+file_size], disk[free_start:free_start+file_size]
        rcur -= file_size

    checksum = 0
    for i, (ID, free, *_) in enumerate(disk):
        if not free:
            checksum += i * ID

    return checksum

dmap = array('B', [2, 3, 3, 3, 1])
print(count_naive(disk_map))
