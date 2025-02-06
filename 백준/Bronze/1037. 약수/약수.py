import sys
num = int(sys.stdin.readline())
number = list(map(int, sys.stdin.readline().split()))

sorted = sorted(number)

if len(sorted) == 1:
    print(sorted[0] * sorted[0])
else:

    print(sorted[0] * sorted[-1])