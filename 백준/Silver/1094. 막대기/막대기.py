from collections import deque

x = int(input())
k = x
status = True
division = 64
stick = deque([])
while sum(stick) != k:
    if k != division:
        division = division // 2
    else:
        division = division

    if division <= x:
        stick.append(division)
        x -= division

print(len(stick))