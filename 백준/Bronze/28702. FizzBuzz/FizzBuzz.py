import sys
dict = {}

def is_it_Fizz_Buzz(num):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 3 == 0 and not num % 5 == 0:
        print("Fizz")
    elif num % 5 == 0 and not num % 3 == 0:
        print("Buzz")
    else:
        print(num)

for i in range(3):
    input = sys.stdin.readline().strip()
    dict[input] = i + 1

for name, index in dict.items():
    if name.isnumeric():
        if index == 1:
            is_it_Fizz_Buzz(int(name) + 3 )
            break
        elif index == 2:
            is_it_Fizz_Buzz(int(name) + 2)
            break
        elif index == 3:
            is_it_Fizz_Buzz(int(name) + 1)
            break