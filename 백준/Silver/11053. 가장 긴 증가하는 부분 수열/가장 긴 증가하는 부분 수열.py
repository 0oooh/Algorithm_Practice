import sys
n = int(input())
a = list(map(int, sys.stdin.readline().split()))
mem = [1] * n  
for i in range(1, n):
    for j in range(i):
        if a[i] > a[j]:  
            mem[i] = max(mem[i], mem[j] + 1)
print(max(mem))