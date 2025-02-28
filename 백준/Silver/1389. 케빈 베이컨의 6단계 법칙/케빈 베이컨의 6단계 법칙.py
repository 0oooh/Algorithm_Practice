import sys
from collections import deque

def bfs(start, n, graph):
    queue = deque([start])
    visited = [-1] * (n + 1)
    visited[start] = 0

    while queue:
        node = queue.popleft()
        for neighbor in graph[node]:
            if visited[neighbor] == -1:
                visited[neighbor] = visited[node] + 1
                queue.append(neighbor)

    return sum(visited[1:])

n, m = map(int, sys.stdin.readline().split())
graph = {i: [] for i in range(1, n + 1)}

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

result = []
for i in range(1, n + 1):
    result.append((bfs(i, n, graph), i))

result.sort()
print(result[0][1])