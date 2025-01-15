import sys

n, m = map(int, sys.stdin.readline().split())
name_list = []
name_to_index = {}

for i in range(n):
    name = sys.stdin.readline().strip()
    name_list.append(name)
    name_to_index[name] = i + 1

final = []
for j in range(m):
    find = sys.stdin.readline().strip()
    if find.isnumeric():
        final.append(name_list[int(find) - 1])

    else:
        final.append(name_to_index[find])

print(*final, sep='\n')