from collections import deque
import sys
n = int(sys.stdin.readline())  # 목표 수열의 길이
y = deque(int(sys.stdin.readline()) for _ in range(n))  # 목표 수열 저장

x = [i for i in range(1, n + 1)]  # 1부터 n까지 넣을 수 있는 리스트
memory = []  # 스택 역할
result = []  # 연산 결과 저장

for i in range(len(y)):
    target = y[i]

    while not memory or memory[-1] != target:  # memory가 비었거나, 원하는 값이 없으면 push
        if x:  # x에 값이 있으면 memory에 push
            memory.append(x.pop(0))
            result.append("+")
        else:  # x가 비었는데도 target을 못 찾으면 NO 출력
            print("NO")
            exit()

    if memory and memory[-1] == target:  # memory의 top이 target이면 pop
        memory.pop()
        result.append("-")
    else:
        print("NO")
        exit()

print("\n".join(result))  # 연산 결과 출력