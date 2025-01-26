import sys

n = int(sys.stdin.readline())
listed = []

# 키와 몸무게 입력 받기
for _ in range(n):
    weight, height = map(int, sys.stdin.readline().split())
    listed.append((weight, height))

# 등수 리스트 초기화
ranks = [1] * n

# 브루트포스 비교
for i in range(n):
    for j in range(n):
        if i != j:  # 자기 자신 비교 제외
            if listed[i][0] < listed[j][0] and listed[i][1] < listed[j][1]:
                ranks[i] += 1  # 더 큰 덩치가 있다면 등수 증가

# 결과 출력
print(*ranks)