import math
import sys
N = int(sys.stdin.readline())
size = list(map(int, sys.stdin.readline().split()))
t, p = map(int, sys.stdin.readline().split())
listed = []
for each in size:
    bunch = math.ceil(each/t)
    listed.append(bunch)

a = N//p
b = N % p

print(sum(listed))
print(a, b)