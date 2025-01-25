import sys
n, target = map(int, sys.stdin.readline().split())
cards = list(map(int, sys.stdin.readline().split()))

final = []
# 이렇게 인덱스만 뽑아서 하는 거임.
for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            total = cards[i] + cards[j] + cards[k]
            if total <= target:
                final.append(total)

closest_sum = min(final, key=lambda x: abs(target - x))
print(closest_sum)