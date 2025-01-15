status = True
output = []
while status:
    a, b, c = map(int, input().split())
    if a == b == c == 0:
        status = False
        break
    sides = sorted([a, b, c])
    if sides[0] ** 2 + sides[1] ** 2 == sides[2] ** 2:
        output.append("right")

    else:
        output.append("wrong")

for ans in output:
    print(ans)
