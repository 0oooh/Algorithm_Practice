import sys
from collections import deque

N = int(sys.stdin.readline())
queue = deque()

if 1 <= N <= 10000:
    for _ in range(N):
        command = sys.stdin.readline().strip()
        if command.startswith("push"):
            _, value = command.split()
            queue.append(int(value))

        elif command == "front":
            print(queue[0] if queue else -1)

        elif command == "size":
            print(len(queue))

        elif command == "empty":
            print(1 if not queue else 0)

        elif command == "back":
            print(queue[-1] if queue else -1)

        elif command == "pop":
            print(queue.popleft() if queue else -1)