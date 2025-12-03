import re
from time import time

with open('input') as f:
    raw = f.read()
    *REGISTERS, PROGRAM = re.findall(r'[\d,]+', raw)
    REGISTERS = [int(r) for r in REGISTERS]
    PROGRAM = [int(x) for x in PROGRAM.split(',')]


def naive(registers, program):
    A, B, C = registers
    i_pointer = 0
    output = []
    size = len(program)
    
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
        if A == 0:
            return
        nonlocal i_pointer
        i_pointer = o - 2

    def bxc(o):
        nonlocal B
        B = B ^ C

    def out(o):
        output.append(combo(o) % 8)

    def bdv(o):
        nonlocal B
        B = A // (2 ** combo(o))

    def cdv(o):
        nonlocal C
        C = A // (2 ** combo(o))
    
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

    while i_pointer < size:
        f = ops[program[i_pointer]]
        o = program[i_pointer+1]

        f(o)
        i_pointer += 2

    return ','.join([str(x) for x in output])


start = time()
print(naive(REGISTERS, PROGRAM))
print(f'naive: {time() - start:.3f}')
# 7,1,3,4,1,2,6,7,1
