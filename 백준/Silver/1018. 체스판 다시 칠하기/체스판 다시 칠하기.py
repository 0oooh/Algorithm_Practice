N, M = map(int, input().split())
original = []
count = []

for i in range(N):
    original.append(input())


for a in range(N-7):
    for b in range(M-7):
        x = 0
        y = 0
        for i in range(a, a + 8):
            for j in range(b, b + 8):
                if (i+j) % 2 == 0:
                    if original[i][j] != 'W':
                        x += 1

                    if original[i][j] != 'B':
                        y += 1

                else:
                    if original[i][j] != 'B':
                        x += 1

                    if original[i][j] != 'W':
                        y += 1

        count.append(min(x, y))

print(min(count))

