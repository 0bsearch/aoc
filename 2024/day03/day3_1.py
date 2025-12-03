# valid instruction: mul(XXX,YYY)
# no spaces, max 3 digits in operand. Max insturction len -> 12
# input is ~20k symbols
# TODO: regex is boring, do non-AST parsing instead

import re

total = 0

with open('input') as f:
    s = f.read()
    matches = re.findall(r'mul\((\d{1,3}),(\d{1,3})\)', s)
    for x, y in matches:
        total += int(x) * int(y) 

print(total)
