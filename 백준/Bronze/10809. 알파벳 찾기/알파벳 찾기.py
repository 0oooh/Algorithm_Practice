word = input()
alist = [chr(i) for i in range(ord('a'),ord('z')+1)]
blank = {}

for alphabet in alist:
    blank[alphabet] = -1
    for character in word:
        if character == alphabet:
            blank[character] = word.index(alphabet)

for key, value in sorted(blank.items()):
    print(value, end=' ')