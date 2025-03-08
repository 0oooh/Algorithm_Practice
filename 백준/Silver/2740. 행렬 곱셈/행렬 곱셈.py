N, M = map(int, input().split())
A = []
for i in range(N):
    row = list(map(int, input().split()))
    A.append(row)
M2, K = map(int, input().split())
B = []
for i in range(M2):
    row = list(map(int, input().split()))
    B.append(row)
result = []
for i in range(N):
    row = []
    for j in range(K):
        row.append(sum(A[i][k] * B[k][j] for k in range(M)))
    result.append(row)

for row in result:
    print(*row)