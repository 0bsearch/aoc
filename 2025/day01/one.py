def count_zeros(filename):
    current = 50
    passes = 0
    with open(filename) as f:
        for shift in f:
            current += int(shift.replace('L', '-').replace('R', '+'))
            current = current % 100
            
            if current == 0:
                passes += 1

    return passes


print(count_zeros('input'))
