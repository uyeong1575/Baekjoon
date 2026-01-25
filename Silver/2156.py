import sys
input = sys.stdin.readline

n = int(input())
arr=[]
for i in range(n):
    arr.append(int(input()))

dp = [0 for _ in range(n+1)]

if n == 1:
    print(arr[0])
elif n == 2:
    print(arr[1] + arr[0])
else:
    dp[1] = arr[0]
    dp[2] = arr[1] + arr[0]

    for i in range(3, n+1):
        dp[i] = max(dp[i-1], dp[i-2]+arr[i-1], dp[i-3]+arr[i-2]+arr[i-1])

    print(max(dp))


