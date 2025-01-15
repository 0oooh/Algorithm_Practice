full_chess = [1, 1, 2, 2, 2, 8]
input_chess = input()
splited = input_chess.split()
new_set = []
for i in splited:
    new_set.append(int(i))
final = []
for ai, bi in zip(full_chess, new_set):
    final.append(ai - bi)
for num in final:
    print(num, end=' ')
