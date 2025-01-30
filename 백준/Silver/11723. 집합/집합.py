import sys


m = int(sys.stdin.readline())
number_set = set()
for _ in range(m):
    listed = sys.stdin.readline().split()
    if len(listed) == 2:
        command = listed[0]
        number = int(listed[1])

    elif len(listed) == 1:
        command = listed[0]


    if command == "add":
        number_set.add(number)

    elif command == "remove":
        number_set.discard(number)

    elif command == "check":
        if number in number_set:
            print(1)

        else:
            print(0)

    elif command == "toggle":
        if number in number_set:
            number_set.discard(number)

        else:
            number_set.add(number)

    elif command == "all":
        number_set = set(x for x in range(1, 21))

    elif command == "empty":
        number_set = set()

