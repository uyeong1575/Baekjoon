# j번째 집을 i_1 색으로 칠할 때 최소 값은
# j-1번쨰 집을 i_2, i_3 색으로 칠할때 중 최소값에 + 현재 i색 비용

import sys
input = sys.stdin.readline

n = int(input())
w = [[0,0,0]]
for i in range(n):
    r, g, b = map(int, input().split())
    w.append([r,g,b])

dp = [[0 for _ in range(n+1)] for _ in range(4)]
for i in range(1, 4):
    dp[i][1] = w[1][i-1]

for j in range(2, n+1):
    for i in range(1, 4):
        if i == 1:
            i1 = 2
            i2 = 3
        elif i ==2:
            i1 = 1
            i2 = 3
        else:
            i1 = 1
            i2 = 2
        dp[i][j] = min(dp[i1][j-1], dp[i2][j-1]) + w[j][i-1]

ans = []
for i in range(1,4):
    ans.append(dp[i][n])
print(min(ans))
