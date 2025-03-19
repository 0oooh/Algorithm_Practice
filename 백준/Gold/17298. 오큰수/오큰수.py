import sys
n = int(sys.stdin.readline())
num = list(map(int, sys.stdin.readline().split()))
num.reverse()



stack = []
big = [-1] * n

for i in range(n):
    while stack and num[stack[-1]] <= num[i]:
        stack.pop()
    if stack:
        big[i] = num[stack[-1]]
    stack.append(i)
big.reverse()
print(*big, sep=" ")
