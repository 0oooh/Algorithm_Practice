numbers = list(map(int, input().split()))
square_list = []
for num in numbers:
    square = num * num
    square_list.append(square)

print(sum(square_list) % 10)