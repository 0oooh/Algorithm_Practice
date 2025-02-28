import sys
from collections import deque

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    temp_graph[x][y] = -1 

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < n and 0 <= ny < n and temp_graph[nx][ny] > this:
                temp_graph[nx][ny] = -1 
                queue.append((nx, ny))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

n = int(sys.stdin.readline())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

maxn = max(map(max, graph)) 
minn = min(map(min, graph))  

result = 0 

for this in range(0, maxn + 1): 
    temp_graph = [row[:] for row in graph] 
    count = 0 

    for p in range(n):
        for q in range(n):
            if temp_graph[p][q] > this:  
                bfs(p, q)
                count += 1  
    result = max(result, count)  

print(result)