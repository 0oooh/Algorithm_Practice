n = int(input())
suyeol = list(map(int, input().split()))

suyeol.sort()
print(f"{suyeol[0]} {suyeol[-1]}")