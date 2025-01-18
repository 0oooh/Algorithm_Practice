import sys
n = int(sys.stdin.readline())
num_list = list(map(int, sys.stdin.readline().split()))
num_sorted = sorted(num_list)
print(num_sorted[-1] - num_sorted[0])