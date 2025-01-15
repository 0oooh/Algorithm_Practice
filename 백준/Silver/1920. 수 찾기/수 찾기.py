n = int(input())
original = set(map(int, input().split()))
k = int(input())
compare = list(map(int, input().split()))  # 순서 유지

ones = [1] * k

for index, value in enumerate(compare):
    if value not in original:
        ones[index] = 0

print("\n".join(map(str, ones)))