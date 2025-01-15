a, b, c = input().split()
one = int(a)
two = int(b)
three = int(c)
list1 = [one, two, three]
list2 = sorted(list1)

if list2[0] == list2[1] == list2[2]:
    print(10000 + list2[0] * 1000)

elif list2[0] == list2[1] != list2[2] or list2[0] != list2[1] == list2[2]:
    print(1000 + list2[1] * 100)

elif list2[0] != list2[1] != list2[2]:
    print(list2[2] * 100)