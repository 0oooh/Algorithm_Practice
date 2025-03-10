n = int(input())
numbers = list(map(int, input().split()))

mem = [1] * n
mem_reversed = [1] * n


for i in range(1, n):
    for j in range(i):
        if numbers[j] < numbers[i]:
            mem[i] = max(mem[i], mem[j] + 1)

for i in range(n - 2, -1, -1):
    for j in range(i + 1, n):
        if numbers[j] < numbers[i]:
            mem_reversed[i] = max(mem_reversed[i], mem_reversed[j] + 1)

max_length = 0
for i in range(n):
    max_length = max(max_length, mem[i] + mem_reversed[i] - 1)

print(max_length)