w1 = list(input())
w2 = list(input())
l1 = len(w1)
l2 = len(w2)

dp = [[0 for _ in range(l1+1)] for _ in range(l2+1)]

for i in range (1, l2+1):
    for j in range(1, l1+1):
        if w2[i-1] == w1[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else: # 다르면
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

print(dp[l2][l1])