import sys
input = sys.stdin.readline

arr = []
n = int(input())
for i in range(n):
    arr.append(list(map(int, input().split())))

dp = [[0 for _ in range(n)] for _ in range(n)]

dp[0][0] = 1

for i in range(n):
    for j in range(n):
        value = arr[i][j]
        if value == 0:
            continue
        if i != 0 and j != 0:
            if dp[i][j] == 0:
                continue
        if 0 <= j + value < n: # 가로 범위 내이면
            dp[i][j+value] += dp[i][j]
        if 0 <= i + value < n: # 세로 범위 내이면
            dp[i+value][j] += dp[i][j]

print(dp[n-1][n-1])

# if arr[0][0] != 0:
#     dp[0][0] = 1
# else:
#     dp[0][0] = 0

# for i in range(n):
#     for j in range(n):
#         # 위 확인
#         for y in range(1,j+1):
#             if dp[i][j-y] != 0 and y == arr[i][j-y]:
#                 dp[i][j] += dp[i][j-y]
#         # 왼 확인
#         for x in range(1,i+1):
#             if dp[i-x][j] != 0 and x == arr[i-x][j]:
#                 dp[i][j] += dp[i-x][j]

# print(dp[n-1][n-1])