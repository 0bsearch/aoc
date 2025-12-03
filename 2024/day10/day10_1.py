# TODO:
#   BFS/DFS

from array import array
from collections import deque
from timeit import repeat

def bound(x, y):
    return 0 <= x < x_size and 0 <= y < y_size


heights = []
with open('input') as f:
    for l in f:
        heights.append(array('b', (int(x) for x in l.strip())))

x_size = len(heights[0])
y_size = len(heights)


def searchDF(heights):
    total_score = 0
    for y in range(y_size):
        for x in range(x_size):
            if heights[y][x] == 0:
                peaks = set()
                stack = [(x,y)]
                while stack:
                    bx, by = stack.pop()
                    bv = heights[by][bx]
                    if bv == 9:
                        peaks.add((bx, by))
                        continue

                    for dx, dy in (-1, 0), (0, 1), (1, 0), (0, -1):
                        tx, ty = bx + dx, by + dy
                        if bound(tx, ty) and heights[ty][tx] == bv + 1:
                            stack.append((tx, ty))
                total_score += len(peaks)

    return total_score
    

def searchBF(heights):
    total_score = 0
    for y in range(y_size):
        for x in range(x_size):
            if heights[y][x] == 0:
                peaks = set()
                q = deque([(x,y)])
                while q:
                    bx, by = q.popleft()
                    bv = heights[by][bx]
                    if bv == 9:
                        peaks.add((bx, by))
                        continue

                    for dx, dy in (-1, 0), (0, 1), (1, 0), (0, -1):
                        tx, ty = bx + dx, by + dy
                        if bound(tx, ty) and heights[ty][tx] == bv + 1:
                            q.append((tx, ty))
                total_score += len(peaks)

    return total_score


def recurse(heights):
    def get_peaks(x, y):
        # print(f'Traversing from {heights[y][x]} at {x}:{y}')
        if heights[y][x] == 9:
            # print(f'Got to the peak at {x}:{y}')
            return ((x, y),)

        peaks = set()
        for dx, dy in (-1, 0), (0, 1), (1, 0), (0, -1):
            tx, ty = x + dx, y + dy
            if bound(tx, ty) and heights[ty][tx] == heights[y][x] + 1:
                peaks.update(get_peaks(tx, ty))

        # print(f'Returning peaks from {x}:{y}: {peaks}')
        return peaks

    total_score = 0
    for y in range(y_size):
        for x in range(x_size):
            if heights[y][x] == 0:
                total_score += len(get_peaks(x, y))

    return total_score


def recurse_cached(heights):
    cache = {}

    def get_peaks(x, y):
        if (x, y) in cache:
            return cache[(x, y)]

        if heights[y][x] == 9:
            peaks = {(x, y)}
        else:
            peaks = set()
            for dx, dy in (-1, 0), (0, 1), (1, 0), (0, -1):
                tx, ty = x + dx, y + dy
                if bound(tx, ty) and heights[ty][tx] == heights[y][x] + 1:
                    peaks.update(get_peaks(tx, ty))

        cache[(x,y)] = peaks
        return peaks

    total_score = 0
    for y in range(y_size):
        for x in range(x_size):
            if heights[y][x] == 0:
                total_score += len(get_peaks(x, y))

    return total_score


t = repeat(lambda: recurse(heights), number=100, repeat=10)
print(f'Recurse:', recurse(heights), 'in', min(t))

t = repeat(lambda: recurse_cached(heights), number=100, repeat=10)
print(f'Recurse cached:', recurse_cached(heights), 'in', min(t))

t = repeat(lambda: searchDF(heights), number=100, repeat=10)
print(f'Depth-first search', searchDF(heights), 'in', min(t))

t = repeat(lambda: searchBF(heights), number=100, repeat=10)
print(f'Breadth-first search', searchBF(heights), 'in', min(t))
