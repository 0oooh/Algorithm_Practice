import sys
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y, graph, four_in_a_row):
    start_alpha = graph[x][y]
    queue = deque([(x, y)])
    visited = set([(x, y)])
    current_group = [(x, y)]

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < 12 and 0 <= ny < 6 and (nx, ny) not in visited and graph[nx][ny] == start_alpha:
                queue.append((nx, ny))
                visited.add((nx, ny))
                current_group.append((nx, ny))

    if len(current_group) >= 4:
        four_in_a_row.extend(current_group)

def apply_gravity(graph):
    for col in range(6):
        new_col = []
        for row in range(12):
            if graph[row][col] != ".":
                new_col.append(graph[row][col])
        
        for row in range(12 - len(new_col)):
            graph[row][col] = "."
        for row in range(12 - len(new_col), 12):
            graph[row][col] = new_col[row - (12 - len(new_col))]

graph = []
for _ in range(12):
    line = sys.stdin.readline().strip()
    graph.append(list(line))

combo_count = 0

while True:
    four_in_a_row = []

    for i in range(12):
        for j in range(6):
            if graph[i][j] != ".":
                bfs(i, j, graph, four_in_a_row)

    if not four_in_a_row:
        break

    for x, y in four_in_a_row:
        graph[x][y] = "."

    apply_gravity(graph)

    combo_count += 1

print(combo_count)