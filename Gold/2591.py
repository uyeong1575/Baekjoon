s = input()
n = len(s)


dp = [0 for _ in range(n+1)]
dp[0] = 1 

for i in range(1, n+1):
    # 한 자리: s[i-1]이 1~9면 가능
    if 1 <= int(s[i-1]) <= 9:
        dp[i] += dp[i-1]

    # 두 자리: s[i-2:i]가 10~34면 가능
    if i >= 2 and s[i-2] != '0':
        if 10 <= int(s[i-2:i]) <= 34:
            dp[i] += dp[i-2]
print(dp)
print(dp[-1])


for i in range(2,n+1):
    if s[i-1] == '0' or s[i-2] == '0':
        dp[i] = dp[i-1]

    else:
        if int(s[i-2:i]) <= 34:
            dp[i] = dp[i-1] + dp[i-2]
        else:
            dp[i] = dp[i-1]