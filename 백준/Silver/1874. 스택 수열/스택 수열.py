import sys
from collections import deque

n = int(input())
y = deque([int(input()) for _ in range(n)])  # 목표 수열


x = []  # 스택 역할 (push)
memory = []  # 실제 pop할 때 사용하는 스택 역할

result = []  # 연산 저장

num = 1  # push할 숫자

for target in y:
    while num <= target:  # 목표 숫자까지 push 진행
        x.append(num)
        result.append("+")
        num += 1  # 다음 숫자 준비

    if x and x[-1] == target:  # 스택의 top이 목표 숫자면 pop
        x.pop()
        result.append("-")
    else:
        print("NO")  # 만들 수 없는 수열
        exit()

print("\n".join(result))  # 결과 출력