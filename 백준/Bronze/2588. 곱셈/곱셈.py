x = input()
y = input()

xlist = x.split()
ylist = y.split()
split_x = list(xlist[0])
split_y = list(ylist[0])

print(int(x) * int(split_y[2]))
print(int(x) * int(split_y[1]))
print(int(x) * int(split_y[0]))
print(int(x) * int(y))
