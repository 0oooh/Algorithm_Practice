numbers = input()
reversed = ''

for num in numbers:
    reversed = num + reversed
new_reverse = reversed.split()


if int(new_reverse[0]) - int(new_reverse[1]) > 0:
    print(int(new_reverse[0]))
else:
    print(int(new_reverse[1]))