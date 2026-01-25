import sys
input = sys.stdin.readline

n, k = map(int, input().split())
coin = [0]
for _ in range(n):
    coin.append(int(input()))

dp = [0 for _ in range(k+1)]
dp[0]= 1

for i in range(1, n+1):
    for j in range(1,k+1):
        if j - coin[i] >= 0:
            dp[j] = dp[j] + dp[j-coin[i]]

print(dp[k])



# import sys
# input = sys.stdin.readline

# n, k = map(int, input().split())
# coin = [0]
# for _ in range(n):
#     coin.append(int(input()))

# dp = [[0 for _ in range(k+1)] for _ in range(n+1)]

# for i in range(1, n+1):
#     dp[i][0] = 1

# for i in range(1, n+1):
#     for j in range(1,k+1):
#         if j - coin[i] < 0:
#             dp[i][j] = dp[i-1][j]
#         else:
#             dp[i][j] = dp[i-1][j] + dp[i][j-coin[i]]

# print(dp[n][k])