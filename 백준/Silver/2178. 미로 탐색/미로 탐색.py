from collections import deque

def bfs(x, y, graph):
    queue = deque()
    queue.append((x, y))
    graph[x][y] = 0  # 방문 처리
    count = 0
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 범위 체크를 먼저 수행
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue

            # 벽인 경우 무시
            if graph[nx][ny] == 0:
                continue

            # 아직 방문하지 않은 곳이라면 최단 거리 기록 후 큐에 삽입
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
                count += 1


    return graph[n - 1][m - 1]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

n, m = map(int, input().split())
graph = []
for _ in range(n):
    row = list(map(int, input().strip()))  # 각 줄을 입력받고 숫자로 변환
    graph.append(row)

result = bfs(0, 0, graph)  # (0, 0)부터 시작
print(result+1)