T = int(input())
list1 = []
for testcase in range(T):
    R, S = map(str, input().split())
    R_int = int(R)
    for char in S:
        list1.append(char * R_int)
    list1.append("_")

a = (''.join(list1))
newlist = a.split("_")
for yoso in newlist:
    print(yoso.strip("\n"))
