import sys
bag_1 = []
N, target_weight = map(int, input().split())
for _ in range(N):
    w, v = map(int, sys.stdin.readline().split())
    bag_1.append((w, v))


dp = [0] * (target_weight + 1)


for weight, value in bag_1:
    for current_weight in range(target_weight, weight - 1, -1):
        dp[current_weight] = max(dp[current_weight], dp[current_weight - weight] + value)


print(dp[target_weight])
