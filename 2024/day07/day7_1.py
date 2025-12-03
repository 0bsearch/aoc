# data: 850 lines; ~10 operands; 3-digit operands
# ideas:
#   prefer mul for bigger & account magnitude
#   factorize & check right to left

# let's try bruteforce and factorization

from operator import add, mul
from itertools import product

data = []
with open('input') as f:
    for l in f:
        target, ops = l.split(':')
        data.append((int(target), [int(op) for op in ops.strip().split()]))

total = 0

for target, _elements in data:

    for operator_set in product((add, mul), repeat=len(_elements)-1):
        elements = iter(_elements)
        res = next(elements)
        for e, op in zip(elements, operator_set):
            res = op(res, e)
            if res > target:
                break
        if res == target:
            total += target
            break


print(f'{total}')

