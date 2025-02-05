import sys
from collections import deque
n = int(sys.stdin.readline())
listed = deque([i for i in range(1, n + 1)])
bin = deque([])
for _ in range(len(listed)):
    bin.append(listed.popleft())

    listed.rotate(-1)

print(*bin, end=' ')