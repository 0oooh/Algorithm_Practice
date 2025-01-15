students = list(range(1, 31))
set1 = set(students)
list1 = []
for i in range(28):
    list1.append(int(input()))
    set2 = set(list1)
A = sorted(list(set1 - set2))
print(A[0])
print(A[1])

