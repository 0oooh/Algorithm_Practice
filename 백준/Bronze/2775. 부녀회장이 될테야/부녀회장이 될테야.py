final = []
T = int(input())  # 테스트 케이스 개수 입력

for _ in range(T):
    k = int(input())  # 층 입력
    n = int(input())  # 호 입력

    memo = [i for i in range(1, n + 1)]  # 0층 초기화: i호에는 i명이 거주
    j = 1  # j는 따로 사용되지 않지만 유지

    for floor in range(k):  # k층까지 반복
        for i in range(n):  # 1호부터 n호까지 누적 덧셈
            if i == 0:
                memo[i] = memo[i]  # 첫 번째 호는 그대로 유지
            else:
                memo[i] = memo[i] + memo[i - 1]  # 이전 값 더하기

    final.append(memo[n - 1])  # 최종 결과 출력
print(*final, sep='\n')