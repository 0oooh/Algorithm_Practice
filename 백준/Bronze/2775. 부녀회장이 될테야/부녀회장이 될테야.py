T = int(input())  # 테스트 케이스 개수 입력

final = []
for _ in range(T):
    k = int(input())  # 층 입력
    n = int(input())  # 호 입력

    def fibo(memo, j, k, n):
        for floor in range(k):  # k층까지 반복
            for i in range(n):  # 1호부터 n호까지 누적 덧셈
                if i == 0:
                    memo[i] = memo[i]  # 첫 번째 요소 유지
                else:
                    memo[i] = memo[i] + memo[i - 1]  # 누적 덧셈 적용

    memo = [i for i in range(1, n + 1)]  # 0층 초기화: i호에는 i명 거주
    j = 1  # j는 따로 사용되지 않지만 유지

    fibo(memo, j, k, n)  # 계산 수행
    final.append(memo[-1])

print(*final, sep="\n")
