import sys
T = int(input())
A = 0
for i in range(T):
    A += 1
    T += -1
    print(' '.strip("\n") * T + '*'.strip("\n") * A)

