# input data: 140x140
directions = {
    '↘': ( 1,  1),
    '↙': (-1,  1),
    '↖': (-1, -1),
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
total = 0

for y in range(y_min+1, y_max-1):
    for x in range(x_min+1, x_max-1):
        if M[y][x] != 'A':
            continue
        
        intersected = 0
        for dx, dy in directions.values():
            ax = x + dx
            ay = y + dy
            bx = x - dx
            by = y - dy

            if (M[ay][ax], M[y][x], M[by][bx]) == ('M', 'A', 'S'):
                intersected += 1

        if intersected == 2:
            total += 1

print(total)

