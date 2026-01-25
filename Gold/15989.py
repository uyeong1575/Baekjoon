import sys
input = sys.stdin.readline

t = int(input())

c = []
for i in range(t):
    c.append(int(input()))
n = max(c)

dp = [[1 for _ in range(n+1)] for _ in range(4)]

for i in range(2, 4):
    for j in range(1,n+1):
        if j-i >= 0:
            dp[i][j] = dp[i-1][j] + dp[i][j-i]
        else: 
            dp[i][j] = dp[i-1][j]

for i in range(t):
    print(dp[3][c[i]])
