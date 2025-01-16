def is_prime_number(x):
    if x < 2:
        return False  # 2보다 작은 숫자는 소수가 아님
    for i in range(2, int(x ** 0.5) + 1):  # 2부터 √x까지만 확인
        if x % i == 0:
            return False  # 나누어떨어지면 소수가 아님
    return True


t = int(input())  # 숫자 개수 입력
N = map(int, input().split())  # 숫자 리스트 입력

listed = [num for num in N if is_prime_number(num)]  # 소수만 필터링
print(len(listed))
