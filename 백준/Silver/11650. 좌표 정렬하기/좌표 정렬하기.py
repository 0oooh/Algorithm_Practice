from functools import cmp_to_key

N = int(input())
new_list = []
for age_name in range(N):
    x, y = map(int, input().split())
    new_list.append([x, y])


def compare(x, y):
	if(x[0] > y[0]): # x[0] 값이 y[0]값 보다 작으면
		return 1 # y 내용을 앞으로 보냄
	elif(x[0] < y[0]):
		return -1
	else: # x[0] 값이 y[0]값과 동일하면
		if(x[1] < y[1]): # x[1]과 y[1]을 비교해서 y[1]이 크면
			return -1 # x 내용을 앞으로 보냄
		elif(x[1] > y[1]):
			return 1
		else:
			return 0

final = sorted(new_list, key=cmp_to_key(compare))
for num in final:
    print(num[0], num[1])
