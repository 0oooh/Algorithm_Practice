N, M = map(int, input().split())  # N과 M을 입력받아 정수로 변환
baskets = list(range(1, N+1))

for listed in range(M):
    i, j = map(int, input().split())

    baskets[i - 1], baskets[j - 1] = baskets[j - 1], baskets[i - 1]

print(' '.join(map(str, baskets)))
