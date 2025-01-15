a, b = map(int, input().split())
n = a if a>b else b
def uclidian(n, b):
    status = True
    while status:
        remains = n % b
        if remains == 0:
            return b
            status = False
        else:
            n, b = b, remains

least_common_multiple = (a*b)/ uclidian(a, b)



print(uclidian(a, b))
print(int(least_common_multiple)

      )