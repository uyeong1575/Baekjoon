# n번째 계단까지 j칸 점프해서 왔을 때 최대 점수 S(N,J) 라고 하면
# S(N,J) = max(S(N-1,2), S(N-2,1), S(N-2,2)) + N칸의 점수
# N칸일때 기준으로 열로 탐색 해야할듯

import sys
input = sys.stdin.readline

t = int(input())
arr = [int(input()) for _ in range(t)] # n번째 계단 점수, i = n-1

# dp[i][j]  = j칸에서 i칸 점프해 온 점수
dp = [[0 for _ in range(t+1)] for _ in range(2)]

if t == 1:
    print(arr[0])
else:
    dp[0][1] = arr[0]
    dp[0][2] = arr[0] + arr[1]
    dp[1][2] = arr[1]

    for j in range(3, t+1):
        for i in range(2):
            if i == 0: # 1칸 점프해온 경우
                dp[i][j] = dp[1][j-1] + arr[j-1]
            if i == 1: # 2칸 점프해온 경우
                dp[i][j] = max(dp[0][j-2], dp[1][j-2]) + arr[j-1]

    ans = []
    for i in range(2):
        ans.append(dp[i][t])
    print(max(ans))