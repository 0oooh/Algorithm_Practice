import sys
from collections import deque

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m or graph[nx][ny] == 0:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

remember = deque()
n, m = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

for i in range(n): 
    for j in range(m):
        if graph[i][j] == 2:
            bfs(i, j)
            remember.append((i, j))

for i in range(n):
    for j in range(m):
        if graph[i][j] != 0:
            graph[i][j] -= 2
        if graph[i][j] == -1: 
            graph[i][j] = -1

graph[remember[0][0]][remember[0][1]] = 0

for row in graph:
    print(*row)