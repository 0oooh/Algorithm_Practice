alist = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
word = input()
input_word = list(word)
i = 0
y = 0
num_list = []
status = True
while status:
    if input_word[y] in alist[i]:
        num_list.append(i + 3)
        y += 1
        i = 0
        if y == len(input_word):
            print(sum(num_list))
            status = False
    else:
        i += 1