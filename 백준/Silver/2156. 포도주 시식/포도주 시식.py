import sys

N = int(sys.stdin.readline())
Stair = [0]
dp = [0]*(N+1)


for i in range(1,N+1):
    Stair.append(int(input()))
    if i == 1 :
        dp[1] = Stair[1]
    elif i == 2 :
        dp[2] = Stair[1] + Stair[2]

    else :
        dp[i] = max(Stair[i]+Stair[i-1]+dp[i-3], Stair[i]+dp[i-2],Stair[i]+Stair[i-1]+dp[i-4],)


print(max(dp))