
# 2839 설탕배달
n = int(input()) # 총 무게 (킬로그램)

kilogram_types = [5, 3]


dp = [float('inf')] * (n + 1)
dp[0] = 0

# DP 점화식 적용
for i in range(1, n + 1):
    for kg in kilogram_types:
        if i >= kg:
            dp[i] = min(dp[i], dp[i - kg] + 1)


if dp[n] == float('inf'):
    print(-1)

else:
    print(dp[n])