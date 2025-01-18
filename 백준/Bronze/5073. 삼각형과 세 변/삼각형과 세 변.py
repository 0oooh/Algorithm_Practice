import sys

status = True
while status:
    a, b, c = map(int, sys.stdin.readline().split())
    list_1 = sorted([a, b, c])

    setted = set(list_1)
    re_list = list(setted)

    if a == b == c == 0:
        status = False
    else:
        if list_1[0] + list_1[1] > list_1[2]:
            if len(re_list) == 1:
                print("Equilateral")
            elif len(re_list) == 2:
                print("Isosceles")
            elif len(re_list) == 3:
                print("Scalene")
        else:
            print("Invalid")
