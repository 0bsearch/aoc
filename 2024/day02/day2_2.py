total_safe = 0


def check(levels):
    sign = 1 if levels[0] > levels[1] else -1
    for i in range(len(levels)-1):
        left = levels[i]
        right = levels[i+1]
        if not 1 <= (left - right) * sign <= 3:
            return i

    return None


with open('input') as f:
    for report in f:
        levels = [int(l) for l in report.split()]
        error = check(levels)
        if error is None:
            total_safe += 1
        else:
            # this ugliness only works in sane time b/c of input data
            for i in (-1, 0, 1):
                lels = levels.copy()
                lels.pop(error + i)
                if check(lels) is None:
                    total_safe += 1
                    break
        
print(total_safe)
