
import sys


def dfs(graph, v, visited):
    # 현재 노드를 방문 처리
    visited[v] = True
    final.append(v)

    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

n = int(sys.stdin.readline())  # 노드 개수
m = int(sys.stdin.readline())  # 간선 개수

final = []

graph = [[] for _ in range(n + 1)]
for _ in range(m):
    first, second = map(int, sys.stdin.readline().split())
    graph[first].append(second)
    graph[second].append(first)

visited = [False] * (n + 1)


dfs(graph, 1, visited)
print(len(final) - 1)
