from collections import deque
import sys

def is_prime_number(x):
    stack = deque()
    if x < 2:
        return None
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return None
    return x



m, n = map(int, sys.stdin.readline().split())

primes = deque()
for num in range(m, n + 1):
    prime = is_prime_number(num)
    if prime:
        primes.append(prime)

print('\n'.join(map(str, primes)))