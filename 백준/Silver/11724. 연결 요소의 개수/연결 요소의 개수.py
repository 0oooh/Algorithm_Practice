import sys
sys.setrecursionlimit(10**6)  # 재귀 깊이를 충분히 늘려줍니다.

def dfs(graph, v, visited):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

# 입력 받기
n, m = map(int, sys.stdin.readline().split())

# 그래프 초기화
graph = [[] for _ in range(n + 1)]  # 1-based index로 처리

# 간선 정보 받기
for _ in range(m):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

# 방문 여부를 체크하는 배열
visited = [False] * (n + 1)

connected_components = 0  # 연결 요소의 개수를 셀 변수

# 모든 정점에 대해서 DFS를 실행하여 연결 요소 개수를 셈
for v in range(1, n + 1):  # 정점 1부터 n까지 순회
    if not visited[v]:  # 방문하지 않은 정점에서 DFS를 시작
        dfs(graph, v, visited)
        connected_components += 1  # 하나의 연결 요소가 발견될 때마다 증가


print(connected_components)