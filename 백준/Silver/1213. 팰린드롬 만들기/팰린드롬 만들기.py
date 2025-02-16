import sys

word = sys.stdin.readline().strip()
alpha_dict = {}

# 문자 개수 세기
for char in word:
    alpha_dict[char] = alpha_dict.get(char, 0) + 1

odd = 0
this_is_odd = []  # 빈 리스트로 초기화

# 홀수 개수 찾기
for key, value in alpha_dict.items():
    if value % 2 != 0:
        odd += 1

# 홀수 개수가 1개 초과면 불가능
if odd > 1:
    print("I'm Sorry Hansoo")
else:
    temp_dict = {}

    for key_1, value_1 in alpha_dict.items():
        if value_1 % 2 != 0:
            this_is_odd = [key_1]  # 리스트 형태로 저장
        temp_dict[key_1] = value_1 // 2

    # 딕셔너리 업데이트
    alpha_dict.update(temp_dict)

    # 정렬하면서 문자 리스트 생성
    listed = []
    while any(value > 0 for value in alpha_dict.values()):
        for key in sorted(alpha_dict.keys()):  # 정렬된 키 순서로 탐색
            if alpha_dict[key] > 0:
                listed.append(key)
                alpha_dict[key] -= 1

    # 결과 출력
    final = sorted(listed) + this_is_odd + sorted(listed, reverse=True)
    print("".join(final))  # 공백 없이 출력









