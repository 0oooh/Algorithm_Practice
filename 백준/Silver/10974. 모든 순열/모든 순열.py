n = int(input())
perm = [i + 1 for i in range(n)]
visited = [False] * n
result = []

def permu(element):
    if len(element) == n:
        print(*element)
        return

    for i in range(n):
        if not visited[i]:
            visited[i] = True
            element.append(perm[i])
            permu(element)
            element.pop()
            visited[i] = False

permu([])