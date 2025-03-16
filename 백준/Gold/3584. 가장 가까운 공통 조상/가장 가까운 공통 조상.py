import sys
sys.setrecursionlimit(10**6)
from collections import defaultdict

def backtrack(node, tree, near_par):
    near_par.append(node)


    for parent in tree:
        if node in tree[parent]:
            backtrack(parent, tree, near_par)
            break
    return

T = int(sys.stdin.readline())
x = []
for _ in range(T):
    N = int(sys.stdin.readline())
    tree = defaultdict(list)


    for _ in range(N - 1):
        A, B = map(int, sys.stdin.readline().split())
        tree[A].append(B)

    node1, node2 = map(int, sys.stdin.readline().split())

    near_par1 = []
    near_par2 = []

    backtrack(node1, tree, near_par1)
    backtrack(node2, tree, near_par2)
    common_ancestor = -1
    for a in near_par1:
        if a in near_par2:
            common_ancestor = a
            break

    x.append(common_ancestor)
print(*x, sep="\n")