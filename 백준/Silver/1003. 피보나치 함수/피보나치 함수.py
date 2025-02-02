import sys

# DP 테이블 (캐싱)
dp = {0: (1, 0), 1: (0, 1)}  # (0의 개수, 1의 개수)


def fibo(num):
    if num in dp:
        return dp[num]  # 이미 계산된 값이면 반환

    a = fibo(num - 1)  # (0의 개수, 1의 개수)
    b = fibo(num - 2)

    dp[num] = (a[0] + b[0], a[1] + b[1])  # 두 값 합치기
    return dp[num]


T = int(sys.stdin.readline())
for _ in range(T):
    num = int(sys.stdin.readline())
    result = fibo(num)
    print(result[0], result[1])