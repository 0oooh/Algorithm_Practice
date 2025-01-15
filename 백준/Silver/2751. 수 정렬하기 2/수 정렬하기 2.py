import sys
N = int(sys.stdin.readline())
listed = [int(sys.stdin.readline()) for _ in range(N)]
listed.sort()

sys.stdout.write("\n".join(map(str, listed)))
