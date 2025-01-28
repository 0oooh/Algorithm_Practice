import sys

N = int(sys.stdin.readline())
for i in range(1, N+1):
    result = sum((map(int, str(i))))
    k = i + (result)
    if k == N:
        print(i)
        break
    if i == N:
        print(0)

