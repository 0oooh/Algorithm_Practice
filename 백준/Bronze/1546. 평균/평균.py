N = int(input())

scores = list(map(int, input().split()))

if len(scores) == N:
    M = max(scores)
    new_scores = []
    i = 0
    for score in scores:
        new_score = scores[i] / M * 100
        new_scores.append(new_score)
        i += 1

    n = 0
    total = 0
    while n < len(new_scores):
        total += new_scores[n]
        n += 1
print(total / N)
