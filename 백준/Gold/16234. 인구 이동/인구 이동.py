import sys
from collections import deque

def bfs(x, y):
    queue = deque()
    union = []
    queue.append((x, y))
    union.append((x, y))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n or visited[nx][ny] ==1:
                continue
            if L <= abs(graph[nx][ny] - graph[x][y]) <= R:
                visited[nx][ny] = 1
                queue.append((nx, ny))
                union.append((nx, ny))


    if len(union) <= 1:
        return 0
    result = sum(graph[a][b] for a, b in union) // len(union)

    for a, b in union:
        graph[a][b] = result
    return 1






dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
n, L, R = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

day = 0
while True:
    stop = 0
    visited = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if visited[i][j] == 0:
                visited[i][j] = 1
                stop += bfs(i, j)
    if stop == 0:
        break
    day += 1
print(day)


bfs(1, 1)

