t, m = input().split()
amount = int(input())

time = int(t)
minute = int(m)

add = minute + amount

if (time + (add // 60)) <= 23:

    if add < 60:
        print(f"{time} {add}")
    if add >= 60:
        print(f"{time + (add // 60)} {add % 60}")

elif (time + (add // 60)) >= 24:
    if add < 60:
        print(f"{time} {add}")
    if add >= 60:
        print(f"{(time + (add // 60)) - 24} {add % 60}")
