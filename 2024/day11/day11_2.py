from collections import deque
from math import log10
from time import time
from functools import cache


BLINKS = 75

with open('input') as f:
    stones = [(int(x), BLINKS) for x in f.read().strip().split()]


def recurse_cached_rtl(stones):
    total = 0

    @cache
    def count(stone, blinks):
        if blinks == 0:
            return 1

        if stone == 0:
            res = count(1, blinks-1)
            return res

        size = int(log10(stone)) + 1
        if size % 2 == 0:
            mid_magnitude = 10 ** (size // 2)
            left, right = divmod(stone, mid_magnitude)
            res = count(left, blinks-1) + count(right, blinks-1)
            return res

        res = count(stone*2024, blinks-1)
        return res

    for stone, blinks in stones:
        total += count(stone, blinks)

    return total
                
start = time()
print(recurse_cached_rtl(stones))
print(f'{time() - start:.3f}')

