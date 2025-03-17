import sys

n = int(sys.stdin.readline())
houses = [tuple(map(int, sys.stdin.readline().split())) for _ in range(n)]

prev_A, prev_B, prev_C = houses[0]

for house in range(1, n):
    A, B, C = houses[house]
    currA = A + max(prev_A, prev_B)
    currB = B + max(prev_A, prev_B, prev_C)
    currC = C + max(prev_B, prev_C)
    prev_A, prev_B, prev_C = currA, currB, currC

print(max(prev_A, prev_B, prev_C))


prev_A, prev_B, prev_C = houses[0]

for house in range(1, n):
    A, B, C = houses[house]
    currA = A + min(prev_A, prev_B)
    currB = B + min(prev_A, prev_B, prev_C)
    currC = C + min(prev_B, prev_C)
    prev_A, prev_B, prev_C = currA, currB, currC

print(min(prev_A, prev_B, prev_C)) 