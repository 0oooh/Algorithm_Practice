import sys
n, m  = map(int, sys.stdin.readline().split())
x = (n + m) * (n - m)
print(x)