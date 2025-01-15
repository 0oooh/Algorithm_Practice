N, M = map(int, input().split())  # N과 M을 입력받아 정수로 변환
list1 = list(range(1, N+1))  # N개의 바구니를 0으로 초기화


for listed in range(M):     #역순 만들기
    i, j = map(int, input().split())
    newlist = list(reversed(list1[i-1:j]))
    list1[i-1:j] = newlist

print(" ".join(map(str, list1)))


