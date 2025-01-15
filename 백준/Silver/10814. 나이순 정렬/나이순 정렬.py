
N = int(input())
new_list = []

# 입력 받기
for _ in range(N):
    age, name = input().split()
    new_list.append((int(age), name))  # 나이를 정수로 변환

# 나이 기준으로 정렬 (안정 정렬로 가입 순서 유지)
new_list.sort(key=lambda x: x[0])

# 출력
for age, name in new_list:
    print(age, name)