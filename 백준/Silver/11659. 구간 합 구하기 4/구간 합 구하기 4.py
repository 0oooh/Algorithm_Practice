import sys

N, M = map(int, sys.stdin.readline().split())
numbers = list(map(int, sys.stdin.readline().split()))

# 누적 합 배열 만들기
prefix_sum = [0] * (N + 1)
for i in range(1, N + 1):
    prefix_sum[i] = prefix_sum[i - 1] + numbers[i - 1]  # O(N)

# 쿼리 처리
listed = []
for _ in range(M):
    i, j = map(int, sys.stdin.readline().split())
    listed.append(prefix_sum[j] - prefix_sum[i - 1])  # O(1)

print(*listed, sep='\n')

