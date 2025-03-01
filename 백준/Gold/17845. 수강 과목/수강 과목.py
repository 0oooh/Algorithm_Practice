import sys
bag_1 = []
N, target_time = map(int, input().split())
N, target_time = target_time, N
for _ in range(N):
    w, v = map(int, sys.stdin.readline().split())
    w, v = v, w
    bag_1.append((w, v))


dp = [0] * (target_time + 1)


for expected_study_time, score in bag_1:
    for current_time in range(target_time, expected_study_time - 1, -1):
        dp[current_time] = max(dp[current_time], dp[current_time - expected_study_time] + score)


print(dp[target_time])

