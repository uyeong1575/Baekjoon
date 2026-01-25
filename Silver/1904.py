# N번째의 갯수는 N-1번째 경우의 수 + N-2번째 경우의 수
import sys
input = sys.stdin.readline

n = int(input().strip())

dp = [[] for _ in range(n+1)]

def Tail(x):

    dp[1] = 1
    if x>=2:
        dp[2] = 2
    if x >= 3:
        for i in range(3, x+1):
            dp[i] = (dp[i-1] + dp[i-2]) % 15746 # 분배법칙

    return dp[x]

print(Tail(n))
