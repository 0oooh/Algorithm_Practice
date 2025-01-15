n = int(input())
new = range(n)
list1 = []
for i in new:
    user = str(input())
    x = user[0] + user[-1]
    i+= 1
    list1.append(x)

for x in list1:
    print(x)
