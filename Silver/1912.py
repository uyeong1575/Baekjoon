# import sys
# input = sys.stdin.readline

# n = int(input())
# arr = list(map(int, input().split()))

# dp = [0 for _ in range(n)]
# dp[0] = arr[0]

# for i in range(1, n):
#     dp[i] = max(arr[i], dp[i-1] + arr[i])

# print(max(dp))


import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

dp = [0 for _ in range(n+2)]

maxvalue = max(arr)
index = 0
while index <= n:
    print(dp)
    index += 1
    for i in range(1, n+2-index):
        dp[i] = dp[i+1] + arr[i-1]
        if maxvalue < dp[i]:
            maxvalue = dp[i]

print(maxvalue)