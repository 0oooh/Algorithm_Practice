from collections import deque
def bfs(x, y, graph, visited, color):
    # 큐(Queue) 구현을 위해 deque 라이브러리 사용
    queue = deque()
    queue.append((x, y))
    visited[x][y] = True
    # 큐가 빌 때까지 반복하기
    while queue:
        x, y = queue.popleft()

        # 현재 위치에서 4가지 방향으로의 위치 확인
        for i in range(4):  # 상하좌우 4가지
            nx = x + dx[i]
            ny = y + dy[i]
            # 미로 찾기 공간을 벗어난 경우 무시
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue

            # 해당 노드를 처음 방문하는 경우에만 큐에 추가
            if not visited[nx][ny] and graph[nx][ny] == color:
                # 같은 색깔일 때만 방문
                visited[nx][ny] = True
                queue.append((nx, ny))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]




# 첫 번째 입력: 행의 개수
n = int(input())

# 이후 n줄 입력 받아서 리스트로 변환
graphs = [list(input().strip()) for _ in range(n)]

graph = [row[:] for row in graphs]  # ✅ 새로운 리스트 생성 (깊은 복사)
graph_2 = [row[:] for row in graphs]

visited = [[False] * n for _ in range(n)]



# 출력 확인
count = 0
for row in range(n):
    for col in range(len(graph_2[row])):  # 🔹 col을 인덱스로 사용
        if graph_2[row][col] == "R":
            graph_2[row][col] = "G"  # 🔹 인덱스를 이용해 값 수정



final = []

for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            bfs(i, j, graph, visited, graph[i][j])
            count += 1
final.append(count)


visited = [[False] * n for _ in range(n)]
count = 0

for p in range(n):
    for q in range(n):
        if not visited[p][q]:
            bfs(p, q, graph_2, visited, graph_2[p][q])
            count += 1
final.append(count)

print(*final, sep=' ')

