import sys
input = sys.stdin.readline

arr = []
n = int(input())

for i in range(n):
    arr.append(list(map(int, input().split())))

dp = [[0,0] for _ in range(3)]

for i in range(n):
    for j in range(3):
        if j == 0:
            tmpm0 = max(dp[0][0], dp[1][0]) + arr[i][j]
            tmpl0 = min(dp[0][1], dp[1][1]) + arr[i][j]
        elif j == 1:
            tmpm1 = max(dp[0][0], dp[1][0], dp[2][0]) + arr[i][j]
            tmpl1 = min(dp[0][1], dp[1][1], dp[2][1]) + arr[i][j]
        elif j == 2:
            tmpm2 = max(dp[1][0], dp[2][0]) + arr[i][j]
            tmpl2 = min(dp[1][1], dp[2][1]) + arr[i][j]
    dp[0][0]=tmpm0
    dp[0][1]=tmpl0
    dp[1][0]=tmpm1
    dp[1][1]=tmpl1
    dp[2][0]=tmpm2
    dp[2][1]=tmpl2

mx = 0
mn = 10**6
for i in range (3):
    for j in range(2):
        tmp = dp[i][j]
        if tmp > mx:
            mx = tmp
        if tmp < mn:
            mn = tmp
print(mx, mn)


