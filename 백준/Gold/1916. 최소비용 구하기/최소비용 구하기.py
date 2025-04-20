import sys


def dijkstra(start, Visited, INF, Q):
    global MAP
    global M
    Visited[start] = True
    Q.remove(start)

    while Q:
        for i in range(M):
            if MAP[i][0] == start and INF[start] + MAP[i][2] <= INF[MAP[i][1]]:
                INF[MAP[i][1]] = INF[start] + MAP[i][2]

        min_value = float('inf')
        min_index = -1
        for j in range(1, N + 1):
            if not Visited[j] and INF[j] < min_value:
                min_value = INF[j]
                min_index = j

        if min_index == -1:
            break  # 더 이상 방문할 정점이 없다면 종료

        start = min_index
        Visited[start] = True
        Q.remove(start)

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

Visited = [False] * (N + 1)
MAP = []
num = float('inf')
INF = [num] * (N + 1)
Q = [i for i in range(1, N + 1)]

for _ in range(M):
    bus_start, bus_stop, price = map(int, sys.stdin.readline().split())
    MAP.append((bus_start, bus_stop, price))

start, stop = map(int, sys.stdin.readline().split())

INF[start] = 0

dijkstra(start, Visited, INF, Q)
print(INF[stop])



