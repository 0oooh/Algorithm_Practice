import sys
n, m = map(int, sys.stdin.readline().split())
dicted = {}
for i in range(n):
    key, value = map(str, sys.stdin.readline().split())
    dicted[key] = value

for j in range(m):
    find = input()
    print(dicted[find])