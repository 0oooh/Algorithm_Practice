import sys

n = int(sys.stdin.readline())
T = list(map(int, sys.stdin.readline().split()))
erase = int(sys.stdin.readline())

def preorder(v):
    T[v] = -2
    for i in range(n):
        if v == T[i]:
            preorder(i)


preorder(erase)
subT_counter = 0

for i in range(n):
    if T[i] != -2 and i not in T:
        subT_counter += 1

print(subT_counter)

