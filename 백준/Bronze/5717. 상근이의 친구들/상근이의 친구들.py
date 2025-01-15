status = True
new_list = []
while status:
    a, b = map(int, input().split())
    if a == b == 0:
        status = False
        break
    else:
        new_list.append([a, b])

for num in new_list:
    print(num[0] + num[1])