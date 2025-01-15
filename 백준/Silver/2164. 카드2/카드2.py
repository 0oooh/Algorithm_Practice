import sys
from collections import deque

def is_even(num):
    return num % 2 == 0

N = int(sys.stdin.readline())
my_deque = deque(range(1, N + 1))
count = 1

while len(my_deque) > 1:
    if is_even(count):
        # 짝수일 경우 맨 앞 원소를 뒤로 보냄
        my_deque.rotate(-1)
    else:
        # 홀수일 경우 맨 앞 원소 제거
        my_deque.popleft()
    count += 1

# 마지막 남은 원소 출력
print(my_deque[0])