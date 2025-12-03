from collections import defaultdict

left = []
right = defaultdict(int)

with open('input') as f:
    for l in f:
        a, b = l.split()
        left.append(int(a))
        right[int(b)] += 1

score = sum(x * right[x] for x in left)
print(score)

