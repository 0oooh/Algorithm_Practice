n = 9
list1 = []
for i in range(n):
    list1.append(int(input()))
newlist = sorted(list1)
x = newlist[-1]
print(newlist[-1])
y = list1.index(x)
print(y + 1)

