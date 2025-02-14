import sys
def fibo(a, b, count, n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    a = a+b
    count += 1
    if count == n:
        return(a)
    b = a + b
    count += 1
    if count == n:
        return(b)
    return fibo(a, b, count, n)


count = 1
a, b = 0, 1
n = int(sys.stdin.readline())

print(fibo(a, b, count, n))