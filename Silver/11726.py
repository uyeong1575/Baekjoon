# n칸 기준 세로 블럭 쓰는 경우는 n-1의 경우
# 가로 블럭 쓰는 경우는 n-2의 경우
# 둘의 합이 현재 n칸의 경우의 수

n = int(input())

dp = [0 for _ in range(n+1)]
dp[1] = 1
if n >= 2:
    dp[2] = 2
if n >= 3:
    for i in range(3, n+1):
        dp[i] = (dp[i-1] + dp[i-2]) % 10007

print(dp[n])