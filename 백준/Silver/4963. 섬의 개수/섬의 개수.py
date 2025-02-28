import sys
from collections import deque
def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    while queue:
        x, y = queue.popleft()
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if graph[nx][ny] == 0:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = -1  # 방문 표시
                queue.append((nx, ny))

dx = [-1, 1, 1, -1, -1, 1, 0, 0]
dy = [-1, -1, 1, 1, 0, 0, -1, 1]

status = True
island = []
while status:
    m,  n = map(int, sys.stdin.readline().split())
    graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
    count = 0
    if m == 0 and n == 0:
        status = False
    else:
        for i in range(n):
            for j in range(m):
                if graph[i][j] == 1:
                    bfs(i, j)
                    count += 1
        island.append(count)

print(*island, sep="\n")