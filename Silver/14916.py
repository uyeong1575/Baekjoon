n = int(input())

arr = [2, 5]
INF = 10**5
dp = [[INF for _ in range(n+1)] for _ in range(3)]
dp[1][0] = 0
dp[2][0] = 0

for i in range(1,3):
    for j in range(1, n+1):
        if j-arr[i-1]>=0:
            dp[i][j] = min(dp[i][j-arr[i-1]] + 1, dp[i-1][j])
        else:
            dp[i][j] = dp[i-1][j]

for row in dp:
    print(row)

ans = min(dp[1][n], dp[2][n])
if ans == 10**5:
    print(-1)
else:
    print(ans)
