# data: 850 lines; ~10 operands; 3-digit operands
# ideas:
#   prefer mul for bigger & account magnitude
#   factorize & check right to left

# factorization with concat stops being fun, let's bruteforce for now

from operator import add, mul
from itertools import product
from math import log10

def concat(a, b):
    m = int(log10(b)) + 1
    return a * 10**m + b

data = []
with open('input') as f:
    for l in f:
        target, ops = l.split(':')
        data.append((int(target), [int(op) for op in ops.strip().split()]))

total = 0
from time import time
start = time()

for target, _elements in data:

    for operator_set in product((add, mul, concat), repeat=len(_elements)-1):
        elements = iter(_elements)
        res = next(elements)
        for e, op in zip(elements, operator_set):
            res = op(res, e)
            if res > target:
                break
        if res == target:
            total += target
            break


print(f'{total}, finished in {time() - start:.0f} secs')

