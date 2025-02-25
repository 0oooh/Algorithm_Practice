import sys
import math
listed = []
for _ in range(3):
    x = int(sys.stdin.readline())
    listed.append(x)

k = str(math.prod(listed))
print(k.count("0"))
number_list = [int(digit) for digit in str(k)]
dicted = {i:0 for i in range(1, 10)}

for x in number_list:
    for key, value in dicted.items():
        if x == key:
            dicted[key] += 1

for key,value in dicted.items():
    print(value)

