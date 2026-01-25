import sys
input = sys.stdin.readline

n, k = map(int, input().split())

dp = [[0 for _ in range(n+1)] for _ in range(k+1)]

for i in range(n+1):
    dp[1][i] = 1
for i in range(k+1):
    dp[i][0] = 1

for i in range(2, k+1):
    for j in range(1,n+1):
        tmp = 0
        for x in range(j+1):
            tmp += dp[i-1][j-x]
        dp[i][j] = tmp % 10**9

print(dp[k][n])