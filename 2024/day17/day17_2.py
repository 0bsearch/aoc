# ideas:
#   output should be size 16. Once a cycle, A is divided by 2 ** 3, we're looking for
#   8 ** 15 <= A <= 8 ** 16 ~> 10**13 <= A <= 10**15.
#   Bruteforcing does not seem as good idea even with fast exit.
#   Let's try some weirdo DFS bitwise backwards

import re
from time import time

with open('input') as f:
    raw = f.read()
    *REGISTERS, PROGRAM = re.findall(r'[\d,]+', raw)
    REGISTERS = [int(r) for r in REGISTERS]
    PROGRAM = [int(x) for x in PROGRAM.split(',')]

def check(A, B, C, program):
    def combo(operand):
        if operand == 4:
            return A
        elif operand == 5:
            return B
        elif operand == 6:
            return C
        else:
            return operand

    def adv(o):
        nonlocal A
        A = A >> combo(o)

    def bxl(o):
        nonlocal B
        B = B ^ o

    def bst(o):
        nonlocal B
        B = combo(o) % 8

    def jnz(o):
        # we don't care about jumps here
        return

    def bxc(o):
        nonlocal B
        B = B ^ C

    def out(o):
        return combo(o) % 8

    def bdv(o):
        nonlocal B
        B = A >> combo(o)

    def cdv(o):
        nonlocal C
        C = A >> combo(o)
    
    ops = [
        adv,
        bxl,
        bst,
        jnz,
        bxc,
        out,
        bdv,
        cdv,
    ]

    pointer = 0
    size = len(program)
    for pointer in range(0, len(program), 2):
        op = ops[program[pointer]]
        val = program[pointer+1]
        res = op(val)
        if op == out:
            return res

def dfs(registers, program):
    target = list(reversed(program))
    high_bits = 0
    lowest_triplet = 0
    target_idx = 0

    while target_idx < len(target):
        out = target[target_idx]
        print(f'========= {high_bits:b} ========= ')
        for triplet in range(lowest_triplet, 2**3):
            A = high_bits << 3 | triplet
            if check(A, 0, 0, program) == out:
                print(f'{triplet:b} -> {out}')
                high_bits = high_bits << 3 | triplet
                break
        else:
            # current triplet guess failed, lets go 1 step back and find other bits
            high_bits, low_bits = divmod(high_bits, 2**3)
            lowest_triplet = low_bits + 1
            target_idx -= 1
            continue

        target_idx += 1
        lowest_triplet = 0

    assert high_bits == 109019476330651
    return high_bits


start = time()
print(dfs(REGISTERS, PROGRAM))
print(f'dfs: {time() - start:.3f}')
# 109019476330651
