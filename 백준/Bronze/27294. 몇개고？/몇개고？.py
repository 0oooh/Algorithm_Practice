import sys
n, m  = map(int, sys.stdin.readline().split())

if m > 0:
    print(280)

elif m == 0 and 12 <= n <= 16:
    print(320)

else:
    print(280)