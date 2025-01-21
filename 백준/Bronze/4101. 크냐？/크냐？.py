status = True
while status:
    n, m = map(int, input().split())
    if n == m == 0:
        status = False
    else:
        if n > m:
            print("Yes")
        elif n <= m:
            print("No")