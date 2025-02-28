import sys
from collections import deque

def bfs(x, y, graph):
    queue = deque([(x, y)])
    graph[x][y] = -1
    area_size = 1
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= m or ny < 0 or ny >= n:
                continue
            if graph[nx][ny] == 0:
                graph[nx][ny] = -1
                queue.append((nx, ny))
                area_size += 1
    return area_size

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

m, n, k = map(int, sys.stdin.readline().split())
graph = [[0] * n for _ in range(m)]

for _ in range(k):
    left_x, left_y, right_x, right_y = map(int, sys.stdin.readline().split())
    for i in range(left_y, right_y):
        for j in range(left_x, right_x):
            graph[i][j] = 1

areas = []
for p in range(m):
    for q in range(n):
        if graph[p][q] == 0:
            area_size = bfs(p, q, graph)
            areas.append(area_size)

print(len(areas))
areas.sort()
print(*areas, sep=" ")