import sys

from collections import deque
def bfs(x, y, graph, final):
    queue = deque()
    queue.append((x, y))
    final.append(0)
    graph[x][y] = -1
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue

            if graph[nx][ny] == 0:
                continue

            if graph[nx][ny] == 1:
                graph[nx][ny] = -1  # 방문 표시
                queue.append((nx, ny))
                final.append(0)

final = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

n = int(sys.stdin.readline())
graph = [list(map(int, sys.stdin.readline().strip())) for _ in range(n)]

count = 0
fi = []
for p in range(n):
    for q in range(n):
        if graph[p][q] == 1:
            bfs(p, q, graph, final)
            count += 1
            fi.append(len(final))
            final = []

print(count)
fi.sort()
print(*fi, sep='\n')