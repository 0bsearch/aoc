# ideas:
#   1. towels as trie -- very similar "access pattern",
#       but probably slower than stupid list/tuple b/c of no memory locality
#   2. towels as list/tuple and naive cycle
#   3. towels as sorted list/tuple with bin search or fast exit
#   4. any reason for right-to-left?
#   5. instead of string, left-justed/right-padded bits, so we can
#       check == and .startwith in single bitwise op?
# Let's start with #3

from time import time


with open('input') as f:
    TOWELS = [t.encode() for t in next(f).strip().split(', ')]
    next(f)
    PATTERNS = [l.strip().encode() for l in f]

def is_buildable(towels, pattern):
    pattern_len = len(pattern)
    stack = {b''}
    while stack:
        prefix = stack.pop()
        # print(f'prefix: {prefix}\t{len(stack)}')
        if prefix == pattern:
            # print(f'Got match for {pattern}')
            return True

        prefix_len = len(prefix)

        for i in range(1, pattern_len - prefix_len + 1):
            head = pattern[prefix_len:prefix_len+i]
            
            look_wider = False
            for towel in towels:
                if towel == head:
                    stack.add(prefix+towel)
                    # TODO: fix towel pre-sorting
                    # break
                elif towel.startswith(head):
                    look_wider = True

            if not look_wider:
                break
    else:
        return False


def naive(towels, patterns):
    max_towel_len = max(len(t) for t in towels)
    # FIXME
    # towels = tuple(sorted(towels, key=lambda t: t.ljust(max_towel_len, b'z')))
    
    total = 0
    for i, pattern in enumerate(patterns):
        if is_buildable(towels, pattern):
            print(f'{i}\t{pattern} -> True')
            total += 1
        else:
            print(f'{i}\t{pattern} -> False')

    return total


start = time()
print(f'naive> \t {naive(TOWELS, PATTERNS)} \t in {time() - start:.3f} sec')




