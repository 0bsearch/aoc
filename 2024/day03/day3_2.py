# valid instructions: mul(XXX,YYY), do(), don't()
# no spaces, max 3 digits in operand. Max insturction len -> 12
# input is ~20k symbols
# TODO: regex is boring, do non-AST parsing instead

import re

total = 0
k_map = {
    "do()": 1,
    "don't()": 0
}

with open('input') as f:
    s = f.read()
    matches = re.findall(r'mul\((\d{1,3}),(\d{1,3})\)|(do\(\)|don\'t\(\))', s)

    k = 1
    for x, y, op in matches:
        if op:
            k = k_map[op]
            continue
        total += int(x) * int(y) * k

print(total)
