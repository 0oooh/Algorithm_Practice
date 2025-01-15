T, M = input().split()
Time = int(T)
Minutes = int(M)
newtime = Minutes - 45
if Time >= 1:
    if Minutes >= 45:
        print(f"{Time} {newtime}")
    elif Minutes < 45:
        print(f"{Time - 1} {60 + newtime}")
elif Time == 0:
    if Minutes >= 45:
        print(f"{Time} {newtime}")
    elif Minutes < 45:
        print(f"{24 - Time - 1} {60 + newtime}")