from collections import deque
import sys
def calculate(number_stack):
    stack = deque()
    for num in number_stack:
        if num == 0 and stack:
            stack.pop()
        else:
            stack.append(num)
    return stack

k = int(sys.stdin.readline())
number_stack = []
for _ in range(k):
    num = int(sys.stdin.readline())
    number_stack.append(num)

result = calculate(number_stack)
print(sum(result))
