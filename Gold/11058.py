n = int(input())

dp = [i for i in range(n+1)]

for i in range(7, n+1):
    ans = []
    for j in range(i-3):
        ans.append(dp[i-3-j]*(j+2))
    dp[i] = max(ans)

print(dp)
print(dp[n])