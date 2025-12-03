# data:
#   rules R ~ 1000
#   numbers N ~ 100
#   updates U ~ 200
# naive way with mapping numbers to rules is:
#   ~R ammortized time for parsing rules
#   ~N² memory for storing rules
#   ~U for checking updates
# let's go naive for now

from collections import defaultdict

followers = defaultdict(set)

with open('input') as f:
    for line in f:
        if line == '\n':
            # consume rest eagerly
            updates = [[int(x) for x in l.strip().split(',')] for l in f.readlines()]
            break

        x, y = line.split('|')
        followers[int(x)].add(int(y))

total = 0
for update in updates:
    for i in range(len(update)-1):
        left = update[i]
        right = update[i+1]
        if right not in followers[left]:
            break
    else:
        middle = len(update) // 2
        total += update[middle]
        
print(total)
