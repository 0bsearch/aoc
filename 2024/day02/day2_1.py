total_safe = 0

with open('input') as f:
    for report in f:
        levels = (int(l) for l in report.split())
        left = next(levels)
        right = next(levels)

        delta = left - right
        sign = 1 if delta > 0 else -1
        safe = True

        while True:
            if not 1 <= (left - right) * sign <= 3:
                safe = False
                break

            left = right
            try:
                right = next(levels)
            except StopIteration:
                break

        if safe:
            total_safe += 1
        
print(total_safe)
