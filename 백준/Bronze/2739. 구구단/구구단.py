N = int(input())

if N >= 1 and N <= 9:
    for x in range(1, 10): 
        print(f"{N} * {x} = {N * x}")
