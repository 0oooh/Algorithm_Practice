
n = int(input())
dic = {0: 0, 1: 1, 2: 2}


def tiling(n):
    if n in dic:
        return dic[n]

    dic[n] = tiling(n - 1) + tiling(n - 2)
    return dic[n]

print(tiling(n)%10007)