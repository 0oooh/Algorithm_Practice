import sys
from collections import deque


def bfs(x, y, graph, n, final):
    queue = deque([(x, y)])
    graph[x][y] = "X"  # 방문 표시
    perimeter = 0

    while queue:
        cx, cy = queue.popleft()
        final.append(0)  # 면적 증가

        # 4방향 탐색
        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]

            # 그리드 범위 체크
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                perimeter += 1  # 경계를 만나면 perimeter 증가
            elif graph[nx][ny] == "#":
                graph[nx][ny] = "X"  # 방문 표시
                queue.append((nx, ny))
            elif graph[nx][ny] == ".":
                perimeter += 1  # 빈 공간을 만나면 perimeter 증가

    return len(final), perimeter


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

n = int(sys.stdin.readline())
graph = [list(sys.stdin.readline().strip()) for _ in range(n)]

max_area = 0
min_perimeter = float('inf')
count = 0

for p in range(n):
    for q in range(n):
        if graph[p][q] == "#":
            final = []  # 각 덩어리의 면적을 추적할 리스트
            area, perimeter = bfs(p, q, graph, n, final)
            count += 1
            # 최대 면적을 찾고, 동일 면적일 경우 최소 둘레를 선택
            if area > max_area:
                max_area = area
                min_perimeter = perimeter
            elif area == max_area:
                min_perimeter = min(min_perimeter, perimeter)

print(max_area, min_perimeter)