import sys
input = sys.stdin.readline

t = int(input())

for k in range(t):

    n = int(input()) # 동전 종류
    clist = list(map(int, input().split())) # 동전 종류 list

    m = int(input()) # 금액

    dp = [[0 for _ in range(m+1)] for _ in range(n+1)]

    for i in range(n+1):
        dp[i][0] = 1

    for i in range(1, n+1):
        for mj in range(1, m+1):

            if mj-clist[i-1] < 0:
                dp[i][mj] = dp[i-1][mj]
            else:
                dp[i][mj] = dp[i-1][mj] + dp[i][mj-clist[i-1]]

    print(dp[n][m])

    # for i in range(1, n+1): # 초기화
    #     for j in range(1, m+1):
    #         dp[i][j] = 0


