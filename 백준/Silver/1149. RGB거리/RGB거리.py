n = int(input())
houses = [tuple(map(int, input().split())) for _ in range(n)]

mem = [[0] * 3 for _ in range(n)]
mem[0] = list(houses[0])

for house in range(1, n):
    mem[house][0] = houses[house][0] + min(mem[house-1][1], mem[house-1][2])
    mem[house][1] = houses[house][1] + min(mem[house-1][0], mem[house-1][2])
    mem[house][2] = houses[house][2] + min(mem[house-1][0], mem[house-1][1])

print(min(mem[n-1]))