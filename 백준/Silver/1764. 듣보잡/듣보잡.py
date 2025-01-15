import sys
n, m  = map(int, sys.stdin.readline().split())
listed = []
for i in range(n+m):
    name = sys.stdin.readline().strip()
    listed.append(name)

never_heard = set(listed[:n])
never_saw = set(listed[n:])

# 교집합 구하기
never_heard_saw = never_heard.intersection(never_saw)

print(len(never_heard_saw))
for name in sorted(never_heard_saw):
    print(name)