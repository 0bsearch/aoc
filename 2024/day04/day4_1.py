# input data: 140x140
directions = {
    '→': ( 1,  0),
    '↘': ( 1,  1),
    '↓': ( 0,  1),
    '↙': (-1,  1),
    '⟵': (-1,  0),
    '↖': (-1, -1),
    '↑': ( 0, -1),
    '↗': ( 1, -1)
}
    
M = []
with open('input') as f:
    for line in f:
        M.append(line.strip('\n'))

x_min = 0
y_min = 0
x_max = len(M[0])
y_max = len(M)
needle = 'XMAS'
total = 0

for x in range(x_min, x_max):
    for y in range(y_min, y_max):
        if M[y][x] != needle[0]:
            continue

        for dx, dy in directions.values():
            for i, c in enumerate(needle[1:], 1):
                tx = x + dx * i
                ty = y + dy * i
                if not (x_min <= tx < x_max and y_min <= ty < y_max):
                    break
                if M[ty][tx] != c:
                    break
            else:
                total += 1

print(total)

