from collections import deque


N, K = map(int, input().split())

queue = deque([i for i in range(1, N + 1)])
semi_queue = []

while queue:  
    for _ in range(K - 1):
        queue.rotate(-1)
    semi_queue.append(queue.popleft())  

print(f"<{', '.join(map(str, semi_queue))}>")