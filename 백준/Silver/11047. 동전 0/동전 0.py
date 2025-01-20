import sys



n, k = map(int, sys.stdin.readline().split())
money_type = []
for i in range(n):
    money = int(sys.stdin.readline())
    money_type.append(money)

money_type.sort(reverse=True)


count = 0
for mon in money_type:
    if k % mon == 0:
        count += k // mon
        k = 0
        break
    else:
        count += k // mon
        k %= mon

print(count)

