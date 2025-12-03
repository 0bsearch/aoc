# TODO: trie

from time import time
from collections import defaultdict


with open('input') as f:
    TOWELS = [t.encode() for t in next(f).strip().split(', ')]
    next(f)
    PATTERNS = [l.strip().encode() for l in f]


def count_combos(towels, pattern):
    pattern_len = len(pattern)
    nodes = [0] * (pattern_len + max(len(t) for t in towels))

    for t in towels:
        if pattern.startswith(t):
            nodes[len(t) - 1] = 1

    for i, node in enumerate(nodes):
        if i == pattern_len - 1:
            return node

        for t in towels:
            if pattern.startswith(t, i + 1):
                nodes[i + len(t)] += node


def naive(towels, patterns):
    towels = tuple(sorted(towels))
    
    total = 0
    for i, pattern in enumerate(patterns):
        combos = count_combos(towels, pattern)
        total += combos

    return total


start = time()
print(f'naive> \t {naive(TOWELS, PATTERNS)} \t in {time() - start:.3f} sec')
# 601201576113503



