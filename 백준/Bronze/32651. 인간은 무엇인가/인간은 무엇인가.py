n = int(input())
if 1 <= n <= 100000:
    if n % 2024 == 0:
        print("Yes")
    else:
        print("No")
else:
    print("No")