from collections import deque
from math import log10


BLINKS = 25
with open('input') as f:
    stones = [(int(x), BLINKS) for x in f.read().strip().split()]


def count_deque(stones):
    res = 0
    stream = deque(stones)

    while stream:
        stone, blinks = stream.popleft()

        for blinks_left in range(blinks, 0, -1):
            if stone == 0:
                stone = 1
                continue

            size = int(log10(stone)) + 1
            if size % 2 == 0:
                mid_magnitude = 10 ** (size // 2)
                left, right = divmod(stone, mid_magnitude)
                stone = left 
                stream.appendleft((right, blinks_left-1))
                continue
            
            stone *= 2024
        
        res += 1

    return res
                

print(count_deque(stones))
