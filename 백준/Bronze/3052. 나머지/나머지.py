n = 10
list1 = []
list2 = []
same = 0
for i in range(n):
    list1.append(int(input()))
    same += 1
    for num in list1:
        per = num % 42
        if per not in list2:
            list2.append(per)

print(len(list2))
