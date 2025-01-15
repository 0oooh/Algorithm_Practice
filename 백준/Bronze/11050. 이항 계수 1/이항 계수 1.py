import math
def wow(number):
    listed = []
    for i in range(number + 1):
        listed.append(i)
    return math.prod(listed[1:])
n, k = map(int, input().split())
final = wow(n)/(wow(n - k) * wow(k))
print(int(final))