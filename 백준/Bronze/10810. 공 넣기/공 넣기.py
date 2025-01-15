N, M = map(int, input().split())  # N과 M을 입력받아 정수로 변환
list1 = [0] * N  # N개의 바구니를 0으로 초기화

for listed in range(M):
    i, j, k = map(int, input().split())
    for x in range(i - 1, j):
        list1[x] = k
print(' '.join(map(str, list1)))
