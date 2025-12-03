from array import array
from timeit import repeat
from collections import deque


heights = []
heightsA = array('b')

with open('input') as f:
    for l in f:
        heights.append(array('b', (int(x) for x in l.strip())))
        heightsA.extend(int(x) for x in l.strip())

x_size = len(heights[0])
y_size = len(heights)

def scan(heights):
    def bound(x, y):
        return 0 <= x < x_size and 0 <= y < y_size

    ratings = [array('b', b'\00'*x_size) for _ in range(y_size)]
    for x in range(x_size):
        for y in range(y_size):
            if heights[y][x] == 9:
                ratings[y][x] = 1

    for level in range(8, -1, -1):
        for x in range(x_size):
            for y in range(y_size):
                if heights[y][x] != level:
                    continue

                for dx, dy in (-1, 0), (0, 1), (1, 0), (0, -1):
                    tx, ty = x + dx, y + dy
                    if bound(tx, ty) and heights[ty][tx] == level + 1:
                        ratings[y][x] += ratings[ty][tx]

    rating = 0
    for x in range(x_size):
        for y in range(y_size):
            if heights[y][x] == 0:
                rating += ratings[y][x]

    return rating


def scan_array(heights):
    ratings = array('b', b'\00'*x_size*y_size)
    size = len(heights)

    for x in range(x_size):
        for y in range(y_size):
            z = x + y*x_size
            if heights[z] == 9:
                ratings[z] = 1
    
    for level in range(8, -1, -1):
        for x in range(x_size):
            for y in range(y_size):
                z = x + y*x_size
                if heights[z] != level:
                    continue

                for dx, dy in (-1, 0), (0, 1), (1, 0), (0, -1):
                    tx, ty = x + dx, y + dy
                    if 0 <= tx < x_size and 0 <= ty < y_size:
                        tz = tx + ty * x_size
                        if heights[tz] == level + 1:
                            ratings[z] += ratings[tz]

    rating = 0
    for x in range(x_size):
        for y in range(y_size):
            z = x + y*x_size
            if heights[z] == 0:
                rating += ratings[z]

    return rating


def searchDF(heights):
    def bound(x, y):
        return 0 <= x < x_size and 0 <= y < y_size

    rating = 0
    for y in range(y_size):
        for x in range(x_size):
            if heights[y][x] == 0:
                stack = [(x,y)]
                while stack:
                    bx, by = stack.pop()
                    bv = heights[by][bx]
                    if bv == 9:
                        rating += 1
                        continue

                    for dx, dy in (-1, 0), (0, 1), (1, 0), (0, -1):
                        tx, ty = bx + dx, by + dy
                        if bound(tx, ty) and heights[ty][tx] == bv + 1:
                            stack.append((tx, ty))

    return rating


def searchBF(heights):
    def bound(x, y):
        return 0 <= x < x_size and 0 <= y < y_size

    rating = 0
    for y in range(y_size):
        for x in range(x_size):
            if heights[y][x] == 0:
                q = deque([(x,y)])
                while q:
                    bx, by = q.popleft()
                    bv = heights[by][bx]
                    if bv == 9:
                        rating += 1
                        continue

                    for dx, dy in (-1, 0), (0, 1), (1, 0), (0, -1):
                        tx, ty = bx + dx, by + dy
                        if bound(tx, ty) and heights[ty][tx] == bv + 1:
                            q.append((tx, ty))

    return rating


t = repeat(lambda: scan(heights), number=100, repeat=10)
print(min(t))
print(f'Scan:', scan(heights))

t = repeat(lambda: scan_array(heightsA), number=100, repeat=10)
print(min(t))
print(f'Scan array:', scan_array(heightsA))

t = repeat(lambda: searchDF(heights), number=100, repeat=10)
print(min(t))
print(f'Depth-first search', searchDF(heights))

t = repeat(lambda: searchBF(heights), number=100, repeat=10)
print(min(t))
print(f'Breadth-first search', searchBF(heights))
