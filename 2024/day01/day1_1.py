left = []
right = []

with open('input') as f:
    for l in f:
        a, b = l.split()
        left.append(int(a))
        right.append(int(b))

print(left[:20])
print(right[:20])
left = sorted(left)
right = sorted(right)

print(sum(abs(l-r) for l, r in zip(left, right)))
