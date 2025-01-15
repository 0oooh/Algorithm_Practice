n, x = map(int, input().split())
suyeol = list(map(int, input().split()))

for num in suyeol:
    if num < x:
        print(f"{num}", end=" ")
