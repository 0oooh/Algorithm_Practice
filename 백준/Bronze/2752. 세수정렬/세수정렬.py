import sys
a, b, c = map(int, sys.stdin.readline().split())
listed = [a, b, c]
print(*sorted(listed))


