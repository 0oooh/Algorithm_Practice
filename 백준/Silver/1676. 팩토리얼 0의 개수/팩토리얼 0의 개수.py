import math
import sys
n = int(sys.stdin.readline())
listed = list(range(1, n + 1))
factorial = math.prod(listed)
str_fact = str(factorial)
semi_rev = []
for num in str_fact:
    semi_rev.append(int(num))
semi_rev.reverse()
count= 0
for i in semi_rev:
    if i == 0:
        count+= 1
    else:
        break
print(count)