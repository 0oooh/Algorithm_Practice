
import sys
size = int(sys.stdin.readline())
triangle = []
for _ in range(size):
    numbers = list(map(int, sys.stdin.readline().split()))
    triangle.append(numbers)




dp = [[0] * len(row) for row in triangle]
dp[-1] = triangle[-1]

for i in range(len(triangle) - 2, -1, -1):
    for j in range(len(triangle[i])):
        dp[i][j] = triangle[i][j] + max(dp[i+1][j], dp[i+1][j+1])

print(dp[0][0])