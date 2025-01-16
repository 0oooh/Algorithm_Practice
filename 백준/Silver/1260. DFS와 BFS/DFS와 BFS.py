
import sys
from collections import deque




def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

def bfs(graph, v, visited):
    queue = deque([v])
    visited[v] = True
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True



n, m, v = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    first, second = map(int, sys.stdin.readline().split())
    graph[first].append(second)
    graph[second].append(first)

for node in graph:
    node.sort()

visited = [False] * (n + 1)


dfs(graph, v, visited)
visited = [False] * (n + 1)
print()
bfs(graph, v, visited)
