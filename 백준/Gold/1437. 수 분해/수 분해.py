import sys

k = int(sys.stdin.readline())

if k == 0:
    print(0)
elif k == 1:
    print(1)
else:
    result = 1
    while k > 4:
        result = (result * 3) % 10007
        k -= 3
    print((result * k) % 10007)