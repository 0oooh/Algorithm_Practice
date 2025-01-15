status = True
listed = []
reverse_listed = []
while status:
    num = str(input())
    if num != "0":
        listed.append(num)
        revers = ''.join(reversed(num))
        reverse_listed.append(revers)
    else:
        status = False



final = []

i = 0
j = 0
for _ in range(len(listed)):
    if listed[i] == reverse_listed[j]:
        print("yes")
        i += 1
        j += 1
    else:
        print("no")
        i += 1
        j += 1

print()
