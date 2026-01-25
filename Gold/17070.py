import sys
input = sys.stdin.readline

n = int(input())

board = [list(map(int, input().split())) for _ in range(n)]

dp = [[[0,0,0] for _ in range(n)] for _ in range(n)]

for i in range(1, n):
    if board[0][i] == 1:
        break
    else:
        dp[0][i][2] = 1 

for i in range(1,n):
    for j in range(2,n):
        for k in range(3):
            if k == 0: # 대각
                if board[i-1][j] == 1 or board[i][j-1] == 1 or board[i][j] == 1:
                    dp[i][j][k] = 0
                else:
                    dp[i][j][0] = dp[i-1][j-1][0] + dp[i-1][j-1][1] + dp[i-1][j-1][2]
            elif k == 1: # 세로
                if board[i][j] == 1:
                    dp[i][j][k] = 0
                else:
                    dp[i][j][1] = dp[i-1][j][0] + dp[i-1][j][1]
            else: # 가로
                if board[i][j] == 1:
                    dp[i][j][k] = 0
                else:
                    dp[i][j][2] = dp[i][j-1][0] + dp[i][j-1][2]
a = 0
for i in range(3):
    a += dp[n-1][n-1][i]
print(a)