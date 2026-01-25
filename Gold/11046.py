import sys
input = sys.stdin.readline

n = int(input())

dp = [ [ [0, 0, 0] for _ in range(n+1)] for _ in range(n+1) ]

for i in range(n):
    r, c = map(int, input().split())
    dp[i+1][1] = [0,r,c]

arr = []
for i in range(2, n+1):
    for j in range(2, i+1):
        
        for k in range(1, j):
            arr.append(dp[i-k][j-k][0] + dp[i][k][0] + (dp[i-k][j-k][1]*dp[i][k][1]*dp[i][k][2]))
                
        dp[i][j][0] = min(arr)
        arr = []

        dp[i][j][1] = dp[i-1][j-1][1]
        dp[i][j][2] = dp[i][1][2]

print(dp[n][n][0])