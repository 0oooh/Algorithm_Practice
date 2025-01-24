import sys
n = int(sys.stdin.readline())
listed = [0] * 10001
for _ in range(n):
    listed[int(sys.stdin.readline())] += 1

for i in range(10001):
    for _ in range(listed[i]):
        print(i)