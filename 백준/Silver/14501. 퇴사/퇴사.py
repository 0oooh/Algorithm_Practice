N = int(input())
listed = []
for _ in range(N):
    day, price = map(int, input().split())
    listed.append((day, price))
dp = [0 for i in range(N + 1)]

for i in range(N):
    for j in range(i+listed[i][0], N+1):
        if dp[j] < dp[i] + listed[i][1]:
            dp[j] = dp[i] + listed[i][1]

print(dp[-1])